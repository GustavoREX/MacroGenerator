"""Dados da planilha e perfis que o editor de macros consegue aplicar."""
import re
import unicodedata

from weapon_data import WEAPON_DATA


def search_key(text):
    return "".join(c for c in unicodedata.normalize("NFD", text.casefold())
                   if not unicodedata.combining(c))


def base_name(name):
    return name.split(" (")[0]


def parse_critical(value):
    """Na tabela, 19 significa 19/x2; x3 significa 20/x3."""
    match = re.fullmatch(r"(?:(\d+)(?:/x(\d+))?|x(\d+))", value.strip())
    if not match:
        return "", "1"
    return match.group(1) or "20", match.group(2) or match.group(3) or "2"


def get_weapon_profiles(weapon):
    """Cada perfil corresponde a uma escolha de empunhadura ou modo de ataque.

    Efeitos condicionais e encantos permanecem na descrição para customização.
    Armas duplas aplicam um ataque de uma ponta, sem somar as duas pontas.
    """
    base = weapon.get("base_weapon", weapon)
    name = base_name(base["name"])
    if name in ("Pistola-punhal", "Lança de fogo", "Espada-calibre"):
        melee = {"Pistola-punhal": ("1d6", "18", "Perfuração"),
                 "Lança de fogo": ("1d10", "x3", "Perfuração"),
                 "Espada-calibre": ("1d8", "19", "Corte")}[name]
        ranged = "2d8" if name == "Lança de fogo" else "2d6"
        modes = [("Corpo a corpo", *melee, "Luta", ("Força",)),
                 ("Disparo", ranged, "19/x3", "Perfuração", "Pontaria", ())]
    else:
        damage = base.get("damage", "")
        group = base.get("group", "")
        skill = "Pontaria" if group.startswith("Distância") else "Luta" if group else ""
        # Arremesso soma Força; disparos só a somam quando a própria fonte indica.
        strength = (skill == "Luta" or name in ("Azagaia", "Funda", "Shuriken", "Arpão",
                    "Boleadeira", "Chakram", "Arco longo", "Arco de guerra", "Balestra"))
        attributes = ("Força",) if strength else ()
        parts = damage.split("/")
        if len(parts) == 2 and parts[0] != parts[1]:
            choices = list(zip(("Uma mão", "Duas mãos"), parts))
        else:
            choices = [("Ataque", parts[0])]
        modes = [(label, die, base.get("critical", ""), base.get("damage_type", ""),
                  skill, attributes) for label, die in choices]
    profiles = []
    for label, damage, critical, damage_type, skill, attributes in modes:
        threat, multiplier = parse_critical(critical)
        damage = damage if re.fullmatch(r"\d+d\d+", damage) else ""
        profiles.append(dict(label=label, damage=damage,
                             threat=threat, critical_multiplier=multiplier, skill=skill,
                             attributes=attributes if damage else (),
                             damage_type="" if damage_type == "—" else damage_type))
    return profiles


def build_catalog():
    catalog = {category: [dict(row) for row in rows] for category, rows in WEAPON_DATA.items()}
    bases = {base_name(weapon["name"]).casefold(): weapon
             for category, rows in catalog.items() if category != "Armas mágicas"
             for weapon in rows}
    for weapon in catalog["Armas mágicas"]:
        description = weapon["description"].casefold()
        # A descrição desta linha começa com um fragmento de outro item na fonte.
        if base_name(weapon["name"]) == "Pistola Demoníaca":
            base = bases["pistola"]
        else:
            base = next((bases[name] for name in sorted(bases, key=len, reverse=True)
                         if re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", description)), None)
        if base:
            weapon["base_weapon"] = base
            weapon["profile_note"] = (
                f"Dados da arma-base: {base_name(base['name'])}. "
                "Ajuste melhorias, materiais, encantos e efeitos especiais no editor.")
        else:
            weapon["profile_note"] = (
                "Dano, crítico e arma-base não informados na planilha. "
                "Ao selecionar, preencha esses campos no editor.")
    return catalog


WEAPON_CATEGORIES = build_catalog()
