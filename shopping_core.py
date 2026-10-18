"""Catálogos, quantidades, orçamento, carga e persistência do SHOPING."""
from copy import deepcopy
from dataclasses import asdict, dataclass, replace
from decimal import Decimal, InvalidOperation
from hashlib import sha256
import json
import os
from pathlib import Path
import re
from tempfile import NamedTemporaryFile

from crafting_core import money, format_money
from shopping_data import SHOPPING_DATA
from weapon_catalog import base_name, search_key


def decimal_text(value):
    return format(value, "f").rstrip("0").rstrip(".") if value % 1 else str(int(value))


def parse_spaces(value):
    text = str(value).strip()
    if text in ("—", "–", "-"):
        return Decimal(0)  # Um travessão na coluna de espaços indica ausência de carga.
    if not re.fullmatch(r"\d+(?:[.,]\d+)?", text):
        return None
    return Decimal(text.replace(",", "."))


def source_price(row):
    text = row.get("price", "").strip()
    # Não transformar tetos, fórmulas ou valores por patamar em um preço fixo.
    if not re.fullmatch(r"(?:T\$\s*)?\d[\d.,]*", text):
        return None
    return money(text)


def json_value(value):
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, dict):
        return {key: json_value(v) for key, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_value(v) for v in value]
    return value


def catalog_item(category, index, row):
    price, spaces = source_price(row), parse_spaces(row.get("spaces", ""))
    return dict(row, id=f"catalog:{category}:{index}", category=category,
                price_value=None if price is None else str(price),
                spaces_value=None if spaces is None else str(spaces), special=price is None)


CATALOGS = {category: tuple(catalog_item(category, i, row) for i, row in enumerate(rows))
            for category, rows in SHOPPING_DATA.items()}


def filter_items(category="Todos", query="", custom_items=()):
    rows = (*[item for items in CATALOGS.values() for item in items], *custom_items)
    needle = search_key(query.strip())
    return [item for item in rows if (category == "Todos" or item["category"] == category)
            and (not needle or needle in search_key(" ".join(str(item.get(key, "")) for key in
                                     ("name", "category", "group", "description", "notes", "source"))))]


def custom_item(design, base, quote, profile):
    """Fotografia independente do criador; duas configurações homônimas não se misturam."""
    spaces = profile.get("spaces")
    if spaces is None:
        spaces = parse_spaces(base.get("spaces", ""))
        if spaces is not None:
            reduction = sum(base_name(name) == "Discreto" for name in design.improvements)
            reduction += base_name(design.material) == "Mitral"
            spaces = max(min(spaces, Decimal(1)), spaces - reduction)
    configuration = asdict(design)
    selected = [*design.improvements, *([design.material] if design.material else []), *design.enchantments]
    details = [f"Item-base: {base['name']}", f"Tamanho: {design.size}",
               "Configuração: " + (", ".join(selected) or "Sem modificações"),
               f"Valor completo: {format_money(quote.total_price)}",
               f"A pagar por unidade: {format_money(quote.due_now)}"]
    if profile.get("protection"):
        details.append(profile["protection"])
    if profile.get("can_attack", True):
        details.append(f"Dano: {profile['damage']} | Acerto adicional: {profile['attack_bonus'] or '0'} | "
                       f"Bônus de dano: {profile['flat_damage'] or '0'} | "
                       f"Crítico: {profile['threat']}/x{profile['critical_multiplier']}")
        if profile.get("extras"):
            details.append("Dano extra: " + " + ".join(profile["extras"]))
    if profile.get("description"):
        details.append(profile["description"])
    payload = json_value(dict(name=profile["name"], category="Customizados", group=base.get("category") or base.get("group", ""),
                              description="\n\n".join(details), source=base.get("source", ""),
                              price=format_money(quote.total_price), full_price=str(quote.total_price),
                              price_value=str(quote.due_now), spaces_value=spaces, spaces=spaces,
                              damage_type=profile.get("damage_type", ""), special=False,
                              configuration=configuration, profile=profile))
    digest = sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    return dict(payload, id="custom:" + digest)


def item_info(item):
    description = item.get("description", "")
    for key, title in (("damage", "Dano"), ("critical", "Crítico"), ("defense", "Defesa"),
                       ("penalty", "Penalidade")):
        if item.get(key):
            description += f"\n\n{title}: {item[key]}"
    if item.get("special"):
        description = "ESPECIAL — sem preço fixo de mercado. Combine o valor com o mestre.\n\n" + description
    return dict(item, description=description, catalog_entry=True, info_kind=item["category"],
                info_price=item.get("price") or "Especial — sem preço informado")


def default_inventory_path():
    return Path(os.environ.get("LOCALAPPDATA", Path.home())) / "MacroGenerator" / "inventory.json"


@dataclass(frozen=True)
class InventoryLine:
    item: dict
    quantity: int
    unit_price: Decimal | None
    unit_spaces: Decimal | None

    @property
    def key(self):
        return self.item["id"]


@dataclass(frozen=True)
class InventoryTotals:
    quantity: int
    cost: Decimal
    value: Decimal
    spaces: Decimal
    missing_price: int
    missing_spaces: int


def valid_quantity(value):
    if isinstance(value, bool) or not re.fullmatch(r"[1-9]\d*", str(value)):
        raise ValueError("Informe uma quantidade inteira maior que zero.")
    return int(value)


def optional_decimal(value):
    if value is None:
        return None
    try:
        return money(Decimal(str(value)))
    except InvalidOperation:
        raise ValueError("Preço ou carga inválidos no inventário.") from None


class Inventory:
    def __init__(self, path=None):
        self.path = Path(path) if path is not None else None
        self.lines = ()
        self.custom_items = {}
        self.load_error = ""
        if self.path is not None and self.path.exists():
            try:
                data = json.loads(self.path.read_text(encoding="utf-8"))
                if data["version"] != 1:
                    raise ValueError("Versão de inventário desconhecida.")
                customs = {item["id"]: self._validate_item(item) for item in data["custom_items"]}
                lines = tuple(InventoryLine(self._validate_item(row["item"]), valid_quantity(row["quantity"]),
                                            optional_decimal(row["unit_price"]), optional_decimal(row["unit_spaces"]))
                              for row in data["lines"])
                if len({row.key for row in lines}) != len(lines):
                    raise ValueError("Itens repetidos no arquivo.")
                self.lines, self.custom_items = lines, customs
            except (OSError, ValueError, KeyError, TypeError) as error:
                self.load_error = f"Não foi possível carregar {self.path}. Arquivo preservado: {error}"

    @staticmethod
    def _validate_item(item):
        for field in ("id", "name", "category"):
            if not isinstance(item[field], str) or not item[field]:
                raise ValueError("Item de inventário inválido.")
        optional_decimal(item["price_value"])
        optional_decimal(item["spaces_value"])
        return deepcopy(item)

    def _commit(self, lines, customs=None):
        if self.load_error:
            raise ValueError(self.load_error)
        customs = self.custom_items if customs is None else customs
        if self.path is not None:
            temporary = None
            try:
                self.path.parent.mkdir(parents=True, exist_ok=True)
                payload = dict(version=1, lines=[asdict(row) for row in lines], custom_items=list(customs.values()))
                with NamedTemporaryFile(mode="w", encoding="utf-8", dir=self.path.parent,
                                        prefix=self.path.name + ".", suffix=".tmp", delete=False) as stream:
                    temporary = Path(stream.name)
                    json.dump(json_value(payload), stream, ensure_ascii=False, indent=2)
                    stream.flush()
                    os.fsync(stream.fileno())
                os.replace(temporary, self.path)
            finally:
                if temporary is not None and temporary.exists():
                    temporary.unlink()
        self.lines, self.custom_items = tuple(lines), customs

    def add(self, item, quantity=1):
        quantity = valid_quantity(quantity)
        snapshot = self._validate_item(item)
        rows = list(self.lines)
        for i, row in enumerate(rows):
            if row.key == snapshot["id"]:
                rows[i] = replace(row, quantity=row.quantity + quantity)
                break
        else:
            rows.append(InventoryLine(snapshot, quantity, optional_decimal(snapshot["price_value"]),
                                      optional_decimal(snapshot["spaces_value"])))
        customs = dict(self.custom_items)
        if snapshot["category"] == "Customizados":
            customs[snapshot["id"]] = snapshot
        self._commit(rows, customs)

    def update(self, key, quantity, unit_price, unit_spaces):
        quantity = valid_quantity(quantity)
        row = next(row for row in self.lines if row.key == key)
        updated = replace(row, quantity=quantity, unit_price=optional_decimal(unit_price),
                          unit_spaces=optional_decimal(unit_spaces))
        self._commit([updated if r.key == key else r for r in self.lines])

    def remove(self, key):
        self._commit([row for row in self.lines if row.key != key])

    def clear(self, include_custom=False):
        remaining = [] if include_custom else [row for row in self.lines if row.item["category"] == "Customizados"]
        self._commit(remaining, {} if include_custom else dict(self.custom_items))

    def totals(self):
        cost = value = spaces = Decimal(0)
        missing_price = missing_spaces = quantity = 0
        for row in self.lines:
            quantity += row.quantity
            if row.unit_price is None:
                missing_price += row.quantity
            else:
                cost += row.unit_price * row.quantity
            full = optional_decimal(row.item.get("full_price"))
            value += (full if full is not None else row.unit_price or Decimal(0)) * row.quantity
            if row.unit_spaces is None:
                missing_spaces += row.quantity
            else:
                spaces += row.unit_spaces * row.quantity
        return InventoryTotals(quantity, cost, value, spaces, missing_price, missing_spaces)
