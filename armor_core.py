"""Armaduras e escudos: proteção, ataque e orçamento com limites compartilhados."""
from dataclasses import dataclass, replace
from decimal import Decimal
import re

from crafting_data import CRAFTING_DATA
from crafting_core import (WeaponDesign, IMPROVEMENTS, ENCHANTMENTS, MATERIALS as WEAPON_MATERIALS, SIZE_STEPS, money,
                           prerequisite_reason, incompatibility, quote_from_prices,
                           shift_damage, custom_weapon_profile)
from weapon_catalog import base_name

ARMOR_ITEMS = {row["name"]: row for row in CRAFTING_DATA["Armaduras e escudos"]}
DEFENSIVE_IMPROVEMENTS = {row["name"]: row for row in CRAFTING_DATA["Melhorias"]
                          if (any(word in row["application"].casefold() for word in ("armadur", "escudo"))
                              or row["application"].startswith("Todas")) and row["name"] != "Material Especial"}
DEFENSIVE_ENCHANTMENTS = {row["name"]: row for row in CRAFTING_DATA["Encantamentos"]
                         if row["group"] == "Encantos — Armaduras e escudos"}
ARMOR_IMPROVEMENTS = {**DEFENSIVE_IMPROVEMENTS, **IMPROVEMENTS}
ARMOR_ENCHANTMENTS = {**DEFENSIVE_ENCHANTMENTS, **ENCHANTMENTS}
ARMOR_MATERIALS = {row["name"]: row for row in CRAFTING_DATA["Materiais"]
                   if any(row[key] not in ("", "—") for key in ("light_price", "heavy_price", "shield_price"))}
SHIELD_NO_ATTACK = {"Escudo de vime", "Escudo torre"}
LIGHT_SHIELDS = {"Escudo leve", "Broquel", "Escudo de couro"}

ARMOR_PM_EFFECTS = {
    "Alado": ("2 PM", "voo 12m sustentado."),
    "Animado": ("1 PM", "movimento: escudo flutua até o fim da cena, mantendo a Defesa com as mãos livres."),
    "Assustador": ("2 PM", "movimento: gera uma onda de medo."),
    "Cáustica": ("2 PM", "movimento: ataques causam +1d4 de ácido até o fim da cena."),
    "Reluzente": ("2 PM", "movimento: emite um clarão de luz."),
    "Zeloso": ("1 PM", "torna-se o alvo de um ataque contra um aliado adjacente (1/rodada)."),
    "Fantasmagórico": ("PM da magia", "lança Manto de Sombras."),
    "Gélido": ("2 PM", "movimento: recebe 10 PV temporários até o fim da cena."),
    "Hipnótico": ("3 PM", "padrão: inimigos em alcance curto ficam fascinados por 1d6 rodadas; Von CD Car evita."),
    "Ilusório": ("1 PM", "movimento: disfarça o item como roupa comum; Visão da Verdade revela."),
    "Incandescente": ("2 PM", "movimento: até o fim da cena, causa 1d6 de fogo a criaturas adjacentes no início de seus turnos."),
    "Refletor": ("PM iguais ao custo da magia", "reflete a magia contra o conjurador (1/rodada)."),
    "Relampejante": ("2 PM", "movimento: gera arcos voltaicos até o fim da cena."),
    "Abissal": ("1 PM", "causa 2d6 de ácido ou fogo a uma criatura adjacente (1/rodada)."),
    "Ancorada": ("1 PM", "escalada 12m sustentada."),
    "Anulador": ("3 PM por círculo", "anula uma magia recebida (1/rodada)."),
    "Arbóreo": ("PM da magia", "lança Controlar Plantas (CD Sab); −1 PM se já conhece."),
    "Astuto": ("3 PM", "detecta localização de criaturas escondidas e invisíveis em alcance curto (1/rodada)."),
    "Densa": ("2 PM", "movimento: criaturas escolhidas em 9m ficam abaladas e lentas por 1d4 rodadas; CD For/Des evita (1/rodada)."),
    "Égide": ("3 PM", "ignora um dano de ataque à distância (1/cena)."),
    "Enraizada": ("2 PM", "+5 em um teste de resistência contra movimento."),
    "Esmérico": ("1 PM", "campo sustentado estende RD ácido 10 e resistência a veneno +5 a aliados em alcance curto."),
    "Estígio": ("5 PM", "se reduzido a 0 PV ou menos, permanece com 1 PV (1/cena)."),
    "Etéreo": ("3 PM", "incorpóreo por 1 rodada (1/cena); terminar dentro de objeto causa expulsão e dano."),
    "Geomântico": ("PM da magia", "lança Controlar Terra (CD Car); −1 PM se já conhece."),
    "Luminescente": ("PM da magia", "lança Luz; −1 PM se já conhece. Sensíveis à luz podem ficar cegos (Ref CD Car evita, 1/cena)."),
    "Prístino": ("2 PM", "remove doente, enjoado ou envenenado de uma criatura adjacente."),
    "Purificador": ("2 PM", "aliado em alcance curto repete resistência contra medo ou mental (1/efeito)."),
    "Reanimador": ("PM da magia", "lança Curar Ferimentos (CD Sab); −1 PM se já conhece."),
    "Replicante": ("1 PM", "ao sofrer ataque corpo a corpo, causa 2d6 do mesmo dano ao atacante e reduz essa quantia do dano sofrido."),
    "Resiliente": ("1 PM", "repete resistência contra atordoamento, paralisia ou petrificação (1/efeito)."),
    "Vórtice": ("1 PM", "puxa criatura em alcance curto para ponto adjacente; Fort CD For evita."),
}


def is_shield(item):
    return item["group"] == "Escudos"


def can_shield_attack(item):
    return is_shield(item) and base_name(item["name"]) not in SHIELD_NO_ATTACK


def armor_material_column(item):
    return "shield_price" if is_shield(item) else "heavy_price" if item["group"] == "Armaduras Pesadas" else "light_price"


def armor_material_price(name, item, override=None):
    if not name:
        return Decimal(0)
    raw = ARMOR_MATERIALS[name][armor_material_column(item)]
    if raw in ("", "—"):
        raise ValueError(f"{name} não se aplica a esta categoria de item.")
    if override is not None:
        return money(override)
    try:
        return money(raw)
    except ValueError:
        raise ValueError(f"{name}: exige {raw}; informe a cotação total em T$.") from None


def armor_construction(item):
    name = base_name(item["name"])
    if name in ("Escudo leve", "Escudo de vime", "Sagna"):
        return "Madeira"
    return "Metal" if is_shield(item) or item["group"] == "Armaduras Pesadas" or name == "Couraça" else "Outra"


def armor_item_profiles(item):
    if not can_shield_attack(item):
        return [{"label": "Proteção (sem ataque)"}]
    light = base_name(item["name"]) in LIGHT_SHIELDS
    return [{"label": "Ataque leve (1d4)" if light else "Ataque pesado (1d6)"}]


def shield_weapon(item):
    light = base_name(item["name"]) in LIGHT_SHIELDS
    return dict(item, group="Corpo a Corpo — Leves" if light else "Corpo a Corpo — Uma Mão",
                category="Escudos", damage="1d4" if light else "1d6", critical="20/x2", damage_type="Impacto")


def armor_incompatibility(item, entry, kind, construction="Metal"):
    name = base_name(entry["name"])
    shield, heavy = is_shield(item), item["group"] == "Armaduras Pesadas"
    if kind == "material":
        if base_name(item["name"]) in ("Armadura de pedra", "Veste de teia de aranha"):
            return "Este item não pode receber material especial."
        if entry[armor_material_column(item)] in ("", "—"):
            return "Material indisponível para esta categoria."
        if name == "Madeira Tollon" and (not shield or base_name(item["name"]) not in LIGHT_SHIELDS):
            return "Madeira Tollon só se aplica a escudos leves nesta tela."
    elif kind == "improvement":
        application = entry["application"].casefold()
        defensive = entry["name"] in DEFENSIVE_IMPROVEMENTS
        weapon_only = entry["name"] in IMPROVEMENTS and not defensive
        if weapon_only:
            if not can_shield_attack(item):
                return "Exige um escudo que possa atacar."
            return incompatibility(shield_weapon(item), entry, kind, construction)
        if "armaduras pesadas" in application and not heavy:
            return "Exige armadura pesada."
        if "armaduras" in application and "escudos" not in application and not application.startswith("todas") and shield:
            return "Melhoria exclusiva de armaduras."
        if application == "escudos" and not shield:
            return "Melhoria exclusiva de escudos."
        if name in ("Espinhoso", "Balístico") and not can_shield_attack(item):
            return "Este escudo não pode ser usado para atacar."
        if name in ("Ajustada", "Sob Medida") and item["name"].startswith("Armadura de engenhoqueiro"):
            return "A penalidade deste item não pode ser reduzida."
    else:
        if entry["name"] in ENCHANTMENTS:
            if not can_shield_attack(item):
                return "Exige um escudo que possa atacar."
            return incompatibility(shield_weapon(item), entry, kind, construction)
        if name in ("Animado", "Esmagador", "Relampejante") and not shield:
            return "Encantamento exclusivo de escudos."
        if name == "Esmagador" and not can_shield_attack(item):
            return "Este escudo não pode ser usado para atacar."
        if name in ("Ancorada", "Ligeira") and shield:
            return "Encantamento exclusivo de armaduras."
    return ""


def armor_enchantment_count(names):
    return sum(2 if "conta como dois encantos" in ARMOR_ENCHANTMENTS[name]["description"].casefold() else 1
               for name in names)


@dataclass(frozen=True)
class ArmorDesign(WeaponDesign):
    fitted: bool = True
    goblin_extra_spaces: int = 0
    ballistic_active: bool = False
    caustic_active: bool = False


def validate_armor_design(design):
    if design.weapon_name not in ARMOR_ITEMS:
        raise ValueError("Escolha uma armadura ou escudo não mágico do catálogo.")
    item = ARMOR_ITEMS[design.weapon_name]
    if design.size not in SIZE_STEPS or design.construction not in ("Metal", "Madeira", "Outra"):
        raise ValueError("Tamanho ou construção inválidos.")
    if not 0 <= design.goblin_extra_spaces <= 8:
        raise ValueError("A carga extra da armadura de engenhoqueiro deve estar entre 0 e 8 espaços.")
    for chosen, catalog, kind in ((design.improvements, ARMOR_IMPROVEMENTS, "improvement"),
                                  (design.enchantments, ARMOR_ENCHANTMENTS, "enchantment")):
        if len(chosen) != len(set(chosen)):
            raise ValueError("Não é possível repetir a mesma opção.")
        for name in chosen:
            if name not in catalog:
                raise ValueError(f"Opção desconhecida: {name}.")
            reason = (armor_incompatibility(item, catalog[name], kind, design.construction)
                      or prerequisite_reason(catalog[name], kind, design.improvements,
                                             design.enchantments, design.material))
            if reason:
                raise ValueError(f"{name}: {reason}")
    if design.material:
        if design.material not in ARMOR_MATERIALS:
            raise ValueError("Material especial inválido.")
        reason = armor_incompatibility(item, ARMOR_MATERIALS[design.material], "material", design.construction)
        if reason:
            raise ValueError(reason)
    if design.existing_material and design.existing_material not in ARMOR_MATERIALS:
        raise ValueError("Material anterior inválido.")
    count, enchants = len(design.improvements) + bool(design.material), armor_enchantment_count(design.enchantments)
    if count > 4 or enchants > 3:
        raise ValueError("O item compartilha o limite de 4 melhorias e 3 encantamentos entre defesa e ataque.")
    if not (0 <= design.existing_improvements <= count and 0 <= design.existing_enchantments <= enchants):
        raise ValueError("A configuração final deve incluir todas as melhorias e encantamentos anteriores.")
    if not design.owned and (design.existing_improvements or design.existing_enchantments or design.existing_material):
        raise ValueError("Marque que já possui o item para descontar os custos anteriores.")
    if design.existing_material and (not design.existing_improvements or not design.material):
        raise ValueError("O material anterior conta como melhoria e precisa ser mantido ou substituído.")
    names = {base_name(name) for name in design.improvements}
    if {"Delicada", "Reforçada"} <= names or {"Maciça", "Precisa"} <= names:
        raise ValueError("Melhorias incompatíveis: Delicada/Reforçada ou Maciça/Precisa.")
    if sum(name.startswith("Lancinante") for name in design.enchantments) > 1:
        raise ValueError("Escolha apenas uma versão de Lancinante.")
    return item, count, enchants


def quote_armor(design):
    item, count, enchants = validate_armor_design(design)
    base = money(design.base_price_override if design.base_price_override is not None else item["price"])
    material = armor_material_price(design.material, item, design.material_price_override)
    return quote_from_prices(design, base, material, count, enchants)


def _number(text, default=0):
    match = re.search(r"[-+]?\d+", text.replace("–", "-"))
    return int(match.group()) if match else default


def custom_armor_profile(design):
    item, _, _ = validate_armor_design(design)
    shield, heavy = is_shield(item), item["group"] == "Armaduras Pesadas"
    names = {base_name(name) for name in design.improvements}
    enchants = {base_name(name) for name in design.enchantments}
    material = base_name(design.material)
    base_defense, base_penalty = _number(item["defense"]), _number(item["penalty"])
    defense = base_defense + ("Reforçada" in names) + (4 if "Guardião" in enchants else 2 if "Defensor" in enchants else 0)
    if shield:
        defense += ("Guarda" in names) + (2 if "Defensora" in enchants else 0)
    if base_name(item["name"]) == "Broquel":
        defense = 0
    penalty = base_penalty - ("Reforçada" in names)
    if item["name"].startswith("Armadura de engenhoqueiro"):
        penalty -= design.goblin_extra_spaces
    else:
        reduction = 2 if "Sob Medida" in names and design.fitted else 1 if "Ajustada" in names else 0
        penalty = min(0, penalty + reduction + (2 if material == "Mitral" else 1 if material == "Casco de monstro" else 0))
    base_spaces = money(item["spaces"])
    spaces = max(min(base_spaces, Decimal(1)), base_spaces - ("Discreto" in names) - (material == "Mitral"))
    rd, bonuses = {}, []

    def reduction(kind, value):
        rd[kind] = rd.get(kind, 0) + value

    if base_name(item["name"]) == "Armadura de pedra":
        reduction("geral", 2)
    if base_name(item["name"]) == "Armadura de chumbo":
        reduction("mundano", 2)
        bonuses.append("Resistência a magia +2")
    if material == "Adamante":
        reduction("geral", 5 if heavy else 2)
    if material == "Gelo eterno":
        reduction("fogo", 10 if heavy else 5)
    if material == "Couraça de kaiju":
        reduction("mágico", 20 if heavy else 10)
    if material == "Couro de bulette":
        reduction("ácido", 10 if heavy else 5)
    if material == "Lanajuste":
        reduction("corte", 10 if heavy else 5)
    if material == "Prata":
        reduction("contra espíritos/mortos-vivos", 10 if heavy else 5)
    if material == "Madeira Tollon":
        bonuses.append("Resistência a magia +2")
    if material == "Matéria vermelha" and not design.red_matter_immune:
        bonuses.append(f"Falha de ataques recebidos: {25 if heavy else 10}%")
    for enchant, kind in (("Abençoado", "trevas"), ("Cáustica", "ácido"), ("Gélido", "frio"),
                          ("Incandescente", "fogo"), ("Relampejante", "eletricidade"), ("Esmérico", "ácido")):
        if enchant in enchants:
            reduction(kind, 10)
    for enchant, kinds in (("Opaco", ("ácido", "eletricidade", "fogo", "frio")), ("Abissal", ("ácido", "fogo"))):
        if enchant in enchants:
            for kind in kinds:
                rd[kind] = max(rd.get(kind, 0), 10)
    if "Invulnerável" in enchants:
        reduction("geral", 2 if shield else 5)
    if "Geomântico" in enchants:
        reduction("impacto", 10)
    fortification = (50 if heavy else 25) if material == "Aço-rubi" else 0
    fortification += max((25 if shield else 50) if "Fortificado" in enchants else 0,
                        25 if "Geomântico" in enchants else 0)
    if fortification:
        bonuses.append(f"Fortificação {min(100, fortification)}%")
    if "Abascanto" in enchants:
        bonuses.append("Resistência a magia +5")
    resistance_bonus = ("Selada" in names) + ("Inscrito" in names) + (2 if "Protetor" in enchants else 0)
    if resistance_bonus:
        bonuses.append(f"Resistências +{resistance_bonus}")
    if "Polida" in names:
        bonuses.append("Defesa +5 na primeira rodada em ambiente iluminado")
    if "Égide" in enchants:
        bonuses.append("Defesa +5 contra ataques à distância")
    dex_limit = max(1 if heavy and "Delicada" in names else 0, 2 if heavy and material == "Mitral" else 0,
                    1 if heavy and material == "Casco de monstro" else 0)
    if heavy:
        bonuses.append(f"Até {dex_limit} de Destreza na Defesa")
    if base_name(item["name"]) == "Broquel":
        bonuses.append("Sem bônus direto na Defesa; reduz dano com teste de ataque (1/rodada)")
    activations = [f"{name} ({ARMOR_PM_EFFECTS[name][0]}): {ARMOR_PM_EFFECTS[name][1]}"
                   for name in (base_name(n) for n in design.enchantments) if name in ARMOR_PM_EFFECTS]
    name = design.name.strip() or item["name"] + " customizado"
    attack = can_shield_attack(item)
    profile = dict(name=name, damage="", threat="", critical_multiplier="1", attributes=(), skill="",
                   damage_type="", attack_bonus="", flat_damage="", extras=[], critical="", description="")
    if attack:
        attack_base = shield_weapon(item)
        attack_steps = ("Espinhoso" in names) + ("Esmagador" in enchants)
        attack_base["damage"] = shift_damage(attack_base["damage"], attack_steps)
        # Materiais exclusivos de armaduras não ganham efeitos ofensivos inexistentes.
        attack_material = design.material if design.material in WEAPON_MATERIALS else ""
        if material == "Cristal de sol":
            attack_material = ""  # O dano do escudo é de impacto, sem corte/perfuração.
        attack_design = replace(design, material=attack_material, name=name, profile_index=0)
        profile = custom_weapon_profile(attack_design, weapon=attack_base,
                                        extra_magic_bonus=2 if "Esmagador" in enchants else 0)
        if design.ballistic_active and "Balístico" in names:
            profile["extras"].append("2d6")
            activations.append("Balístico (1 bala): +2d6 de dano; recarregar é ação completa.")
        if design.caustic_active and "Cáustica" in enchants:
            profile["extras"].append("1d4")
            if "Ácido" not in profile["damage_type"]:
                profile["damage_type"] += " | Ácido"
        activations.append("Ataque com escudo: exige armas marciais e perde o bônus de Defesa até seu próximo turno.")
    profile["description"] = " | ".join(filter(None, (profile["description"], *activations)))
    protection = f"Defesa +{defense} | Penalidade {penalty} | Espaços {spaces}"
    if rd:
        protection += " | " + "; ".join(f"RD {value}" + ("" if kind == "geral" else f"/{kind}") for kind, value in rd.items())
    if bonuses:
        protection += " | " + "; ".join(bonuses)
    profile.update(defense_bonus=defense, armor_penalty=penalty, spaces=spaces, rd=rd, bonuses=bonuses,
                   protection=protection, can_attack=attack, is_shield=shield)
    return profile
