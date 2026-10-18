"""Catálogo, validação, orçamento e efeitos das armas customizadas."""
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import re

from crafting_data import CRAFTING_DATA
from crafting_descriptions import compact_weapon_description
from libraries import ATTRIBUTES
from macro_core import build_critical_damage, get_damage_step_track, join_formula_parts
from weapon_catalog import WEAPON_CATEGORIES, base_name

IMPROVEMENT_COSTS = (0, 300, 3000, 9000, 18000)
ENCHANTMENT_COSTS = (0, 18000, 36000, 72000)
ENCHANTMENT_DC = (0, 10, 15, 20)
SIZE_STEPS = {"Pequena": -1, "Padrão": 0, "Aumentada": 1, "Colossal": 2}
WEAPONS = {w["name"]: dict(w, category=category)
           for category, rows in WEAPON_CATEGORIES.items() if category != "Armas mágicas"
           for w in rows}
IMPROVEMENTS = {r["name"]: r for r in CRAFTING_DATA["Melhorias"]
                if ("armas" in r["application"].casefold()
                    or r["application"].startswith("Todas") or r["application"] == "Kum’shrak")
                and r["name"] != "Material Especial"}
MATERIALS = {r["name"]: r for r in CRAFTING_DATA["Materiais"]
             if r["weapon_price"] not in ("", "—") or r["name"].startswith("Coral —")}
ENCHANTMENTS = {r["name"]: r for r in CRAFTING_DATA["Encantamentos"]
                if r["group"] == "Encantos — Armas"}


def entry_prerequisite(entry):
    match = re.search(r"Pré-requisito:\s*([^.;]+)", entry["description"], flags=re.IGNORECASE)
    return match.group(1).strip() if match else ""


def prerequisite_reason(entry, kind, improvements=(), enchantments=(), material=""):
    requirement = entry_prerequisite(entry)
    if not requirement:
        return ""
    selected = improvements if kind == "improvement" else enchantments
    if requirement.casefold().startswith("outra melhoria"):
        if material or any(name != entry["name"] for name in improvements):
            return ""
        return "Exige outra melhoria (o material especial também conta)."
    alternatives = re.split(r"\s+ou\s+", requirement.casefold())
    alternatives = ["reforçada" if name == "reforçado" else name for name in alternatives]
    if not any(name in {base_name(value).casefold() for value in selected} for name in alternatives):
        return f"Exige {requirement.capitalize()}."
    return ""


def catalog_hierarchy(catalog):
    """Retorna (nome, profundidade, pai), com cabeçalhos para requisitos sem pai no catálogo."""
    by_base = {base_name(name).casefold(): name for name in catalog}
    children, groups, roots = {}, {}, []
    for name, entry in catalog.items():
        requirement = entry_prerequisite(entry)
        alternatives = re.split(r"\s+ou\s+", requirement.casefold())
        parent = next((by_base.get("reforçada" if value == "reforçado" else value)
                       for value in alternatives if ("reforçada" if value == "reforçado" else value) in by_base), None)
        if parent:
            children.setdefault(parent, []).append(name)
        elif requirement:
            group = "Outra melhoria (qualquer)" if requirement.casefold().startswith("outra melhoria") else requirement.capitalize()
            groups.setdefault(group, []).append(name)
        else:
            roots.append(name)
    result = []

    def visit(name, depth=0, parent=""):
        result.append((name, depth, parent))
        for child in children.get(name, ()):
            visit(child, depth + 1, name)

    for root in roots:
        visit(root)
    for group, names in groups.items():
        result.append((None, 0, group))
        for name in names:
            visit(name, 1, group)
    return result


def money(value):
    if isinstance(value, Decimal):
        result = value
    else:
        text = str(value).replace("T$", "").replace(" ", "").strip()
        if "," in text:
            text = text.replace(".", "").replace(",", ".")
        elif re.fullmatch(r"\d{1,3}(?:\.\d{3})+", text):
            text = text.replace(".", "")
        try:
            result = Decimal(text)
        except InvalidOperation:
            raise ValueError("Informe um preço em tibares válido.") from None
    if not result.is_finite() or result < 0:
        raise ValueError("O preço deve ser um número maior ou igual a zero.")
    return result


def format_money(value):
    return "T$ " + f"{value:,.2f}".translate(str.maketrans({",": ".", ".": ","}))


def material_price(name, override=None):
    if not name:
        return Decimal(0)
    if override is not None:
        return money(override)
    item = MATERIALS[name]
    if name.startswith("Coral —"):
        return Decimal(1800)
    try:
        return money(item["weapon_price"])
    except ValueError:
        raise ValueError(f"{name}: exige {item['weapon_price']}; informe a cotação do material em T$.") from None


def default_construction(weapon):
    return "Madeira" if base_name(weapon["name"]) in (
        "Bordão", "Clava", "Tacape", "Porrete", "Bastão lúdico", "Malho") else "Metal"


def incompatibility(weapon, entry, kind, construction="Metal"):
    name = base_name(entry["name"])
    damage_type = weapon.get("damage_type", "").casefold()
    cutting = any(part in damage_type for part in ("corte", "perfura"))
    melee = weapon.get("group", "").startswith("Corpo a Corpo")
    if kind == "material":
        if name == "Madeira Tollon" and construction != "Madeira":
            return "Exige uma arma de madeira."
        if name in ("Adamante", "Mitral", "Aço-rubi", "Prata") and construction != "Metal":
            return "Exige uma parte de ataque metálica."
        if name == "Cristal de sol" and not cutting:
            return "Exige dano de corte ou perfuração."
        if name.startswith("Coral —") and base_name(weapon["name"]) != "Cimitarra":
            return "A fonte descreve este material para a cimitarra de coral."
    elif kind == "improvement":
        if entry["application"] == "Kum’shrak" and not weapon["name"].startswith("Kum’shrak"):
            return "Exclusiva da kum’shrak."
        if name == "Farpada" and not cutting:
            return "Exige dano de corte ou perfuração."
        if name == "Guarda" and not melee:
            return "Exige uma arma corpo a corpo."
        if name == "Pressurizada" and not (
                melee and "impacto" in damage_type or weapon.get("category") == "Armas de fogo"):
            return "Exige arma corpo a corpo de impacto ou arma de fogo."
        if name == "Mira Telescópica":
            thrown = {"Azagaia", "Funda", "Tai-tai", "Shuriken", "Arpão", "Boleadeira", "Chakram", "Rede"}
            if melee or base_name(weapon["name"]) in thrown:
                return "Exige arma de disparo, exceto fundas."
    elif name == "Crescente" and not melee:
        return "Exige uma arma corpo a corpo."
    return ""


@dataclass(frozen=True)
class WeaponDesign:
    weapon_name: str
    profile_index: int = 0
    name: str = ""
    size: str = "Padrão"
    construction: str = "Metal"
    improvements: tuple[str, ...] = ()
    enchantments: tuple[str, ...] = ()
    material: str = ""
    owned: bool = False
    existing_improvements: int = 0
    existing_enchantments: int = 0
    existing_material: str = ""
    base_price_override: Decimal | None = None
    material_price_override: Decimal | None = None
    damage_override: str = ""
    lancinante_mode: str = "+10"
    red_matter_immune: bool = False


@dataclass(frozen=True)
class WeaponQuote:
    base_price: Decimal
    improvement_price: Decimal
    enchantment_price: Decimal
    material_price: Decimal
    total_price: Decimal
    due_now: Decimal
    improvement_due: Decimal
    enchantment_due: Decimal
    material_due: Decimal
    improvement_count: int
    enchantment_count: int
    improvement_dc: int
    enchantment_dc: int


def validate_design(design):
    if design.weapon_name not in WEAPONS:
        raise ValueError("Escolha uma arma-base não mágica do catálogo.")
    weapon = WEAPONS[design.weapon_name]
    if design.size not in SIZE_STEPS or design.construction not in ("Metal", "Madeira", "Outra"):
        raise ValueError("Escolha um tamanho e uma construção válidos.")
    for selected, catalog, kind in ((design.improvements, IMPROVEMENTS, "improvement"),
                                     (design.enchantments, ENCHANTMENTS, "enchantment")):
        if len(selected) != len(set(selected)):
            raise ValueError("Uma mesma melhoria ou encanto não pode ser repetido.")
        for name in selected:
            if name not in catalog:
                raise ValueError(f"Opção desconhecida: {name}.")
            reason = incompatibility(weapon, catalog[name], kind, design.construction)
            if reason:
                raise ValueError(f"{name}: {reason}")
            reason = prerequisite_reason(catalog[name], kind, design.improvements,
                                         design.enchantments, design.material)
            if reason:
                raise ValueError(f"{name}: {reason}")
    if design.material:
        if design.material not in MATERIALS:
            raise ValueError("Escolha apenas um material especial válido.")
        reason = incompatibility(weapon, MATERIALS[design.material], "material", design.construction)
        if reason:
            raise ValueError(f"{design.material}: {reason}")
    if design.existing_material and design.existing_material not in MATERIALS:
        raise ValueError("Material anterior desconhecido.")
    improvements = len(design.improvements) + bool(design.material)
    enchantments = len(design.enchantments)
    if improvements > 4:
        raise ValueError("Limite de 4 melhorias, incluindo o material especial.")
    if enchantments > 3:
        raise ValueError("Limite de 3 encantamentos.")
    if not (0 <= design.existing_improvements <= improvements
            and 0 <= design.existing_enchantments <= enchantments):
        raise ValueError("A configuração final deve incluir as melhorias e os encantos que a arma já possui.")
    if not design.owned and (design.existing_improvements or design.existing_enchantments or design.existing_material):
        raise ValueError("Marque que já possui a arma para descontar custos anteriores.")
    if design.existing_material and not design.existing_improvements:
        raise ValueError("O material anterior já deve contar como uma das melhorias existentes.")
    if design.existing_material and not design.material:
        raise ValueError("Mantenha ou substitua o material anterior; não é possível simplesmente removê-lo.")
    if design.lancinante_mode not in ("+10", "Multiplicar bônus"):
        raise ValueError("Escolha o efeito de Lancinante.")
    names = {base_name(name).casefold() for name in design.improvements}
    if {"maciça", "precisa"} <= names:
        raise ValueError("Maciça e Precisa são incompatíveis.")
    if sum(name.startswith("Lancinante") for name in design.enchantments) > 1:
        raise ValueError("Escolha apenas uma das versões de Lancinante.")
    return weapon, improvements, enchantments


def quote_weapon(design):
    weapon, count, enchantments = validate_design(design)
    try:
        base = money(design.base_price_override if design.base_price_override is not None else weapon["price"])
    except ValueError:
        raise ValueError("Informe o preço-base desta arma em T$.") from None
    material = material_price(design.material, design.material_price_override)
    return quote_from_prices(design, base, material, count, enchantments)


def quote_from_prices(design, base, material, count, enchantments):
    """Progressões compartilhadas pelos criadores de equipamentos."""
    improvement = Decimal(IMPROVEMENT_COSTS[count])
    enchantment = Decimal(ENCHANTMENT_COSTS[enchantments])
    improvement_due = improvement - IMPROVEMENT_COSTS[design.existing_improvements]
    enchantment_due = enchantment - ENCHANTMENT_COSTS[design.existing_enchantments]
    material_due = Decimal(0) if design.material == design.existing_material else material
    due = improvement_due + enchantment_due + material_due + (0 if design.owned else base)
    return WeaponQuote(base, improvement, enchantment, material, base + improvement + enchantment + material,
                       due, improvement_due, enchantment_due, material_due, count, enchantments,
                       count * 5, ENCHANTMENT_DC[enchantments])


def shift_damage(damage, steps):
    if not damage or not steps:
        return damage
    _, track = get_damage_step_track(damage)
    if damage not in track:
        raise ValueError(f"{damage} não consta na tabela de passos. Informe o dano final manualmente.")
    index = track.index(damage) + steps
    if not 0 <= index < len(track):
        raise ValueError("O dano ultrapassa a tabela de passos. Informe o dano final manualmente.")
    return track[index]


def custom_weapon_profile(design, *, weapon=None, extra_magic_bonus=0):
    from weapon_catalog import get_weapon_profiles
    if weapon is None:
        weapon, _, _ = validate_design(design)
    profiles = get_weapon_profiles(weapon)
    if not 0 <= design.profile_index < len(profiles):
        raise ValueError("Escolha um modo de ataque válido.")
    profile = dict(profiles[design.profile_index])
    names = {base_name(n).casefold() for n in design.improvements}
    enchants = {base_name(n).casefold() for n in design.enchantments}
    material = base_name(design.material)
    steps = SIZE_STEPS[design.size] + (material in ("Adamante", "Couraça de kaiju"))
    original_damage = profile["damage"]
    if design.damage_override:
        if not re.fullmatch(r"\d+d\d+", design.damage_override):
            raise ValueError("O dano final manual deve ser um dado, como 2d6.")
        damage = design.damage_override
    else:
        damage = shift_damage(profile["damage"], steps)
    profile["damage"] = damage
    if profile["threat"]:
        threat = int(profile["threat"])
        if "ameaçadora" in enchants:
            threat = 21 - (21 - threat) * 2
        threat -= ("precisa" in names) + (material == "Mitral")
        profile["threat"] = str(max(2, threat))
        profile["critical_multiplier"] = str(int(profile["critical_multiplier"]) + ("maciça" in names))
    magic_bonus = max(extra_magic_bonus, 4 if "magnífica" in enchants else 2 if "formidável" in enchants else 0)
    attack_bonus = (2 if "pungente" in names else 1 if "certeira" in names else 0)
    attack_bonus += max(magic_bonus, 4 if "energética" in enchants else 0)
    flat_damage = (2 if "atroz" in names else 1 if "cruel" in names else 0) + magic_bonus
    extras = []
    types = [profile["damage_type"]] if profile["damage_type"] else []

    def extra(formula, damage_type):
        extras.append(formula)
        if damage_type not in types:
            types.append(damage_type)

    for name, die, kind in (("congelante", "1d6", "Frio"), ("corrosiva", "1d6", "Ácido"),
                            ("elétrica", "1d6", "Eletricidade"), ("flamejante", "1d6", "Fogo"),
                            ("tumular", "1d8", "Trevas"), ("cristalina", "1d6", "Luz")):
        if name in enchants:
            extra(die, kind)
    if material == "Gelo eterno":
        extra("2", "Frio")
    if material == "Cristal de sol":
        extra("2", "Fogo")
    if material == "Matéria vermelha" and not design.red_matter_immune:
        extra("1d6", profile["damage_type"] or "Dano")
    if "piedosa" in enchants:
        extra("1d8", profile["damage_type"] or "Dano")
    if "energética" in enchants:
        types = ["Essência"]
    profile["damage_type"] = " | ".join(types) + (" (não letal)" if "piedosa" in enchants else "")
    critical_steps = (2 if material == "Pena de kraken" else 0)
    critical_steps += (1 if base_name(weapon["name"]) == "Presa de serpente" else 0)
    critical_die = (shift_damage(design.damage_override, critical_steps) if design.damage_override
                    else shift_damage(original_damage, steps + critical_steps))
    if material == "Quitina razza":
        damage += "!"
        critical_die += "!"
        profile["damage"] = damage
    critical = build_critical_damage(critical_die, int(profile["critical_multiplier"])) if damage else ""
    lancinante = any(n.startswith("lancinante") for n in enchants)
    critical_bonus = 10 if "dilacerante" in enchants else 0
    if lancinante:
        optional = any("versão opcional" in n for n in enchants)
        if optional:
            critical_bonus *= int(profile["critical_multiplier"])
        elif design.lancinante_mode == "+10":
            critical_bonus += 10
        else:
            critical_bonus *= int(profile["critical_multiplier"])
            critical_bonus += flat_damage * (int(profile["critical_multiplier"]) - 1)
            # O editor adiciona os atributos uma vez; acrescente aqui as repetições restantes.
            for attribute in profile["attributes"]:
                critical = join_formula_parts(critical, *([ATTRIBUTES[attribute]] * (
                    int(profile["critical_multiplier"]) - 1)))
    critical = join_formula_parts(critical, str(flat_damage) if flat_damage and damage else "",
                                  str(critical_bonus) if critical_bonus and damage else "")
    profile.update(attack_bonus=str(attack_bonus) if attack_bonus else "",
                   flat_damage=str(flat_damage) if flat_damage and damage else "", extras=extras,
                   critical=critical)
    profile["description"] = compact_weapon_description(design)
    profile["name"] = design.name.strip() or weapon["name"] + " customizada"
    return profile
