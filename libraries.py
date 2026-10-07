ATTRIBUTES = {
    "Força": "@{for_mod}",
    "Destreza": "@{des_mod}",
    "Constituição": "@{con_mod}",
    "Inteligência": "@{int_mod}",
    "Sabedoria": "@{sab_mod}",
    "Carisma": "@{car_mod}",
}

COMMON_WEAPONS = {
    "Arco Longo": {
        "threat": "20",
        "skill": "Pontaria",
        "damage": "1d8",
        "attributes": (),
        "critical_multiplier": "3",
        "damage_type": "Perfurante",
    },
    "Espada Longa": {
        "threat": "19",
        "skill": "Luta",
        "damage": "?{estilo|uma mão,1d8|duas mãos,1d10}",
        "attributes": ("Força",),
        "critical_multiplier": "2",
        "damage_type": "Corte",
    },
    "Machado de Guerra": {
        "threat": "20",
        "skill": "Luta",
        "damage": "1d12",
        "attributes": ("Força",),
        "critical_multiplier": "3",
        "damage_type": "Corte",
    },
    "Martelo de Guerra": {
        "threat": "20",
        "skill": "Luta",
        "damage": "1d8",
        "attributes": ("Força",),
        "critical_multiplier": "3",
        "damage_type": "Esmagamento",
    },
    "Montante": {
        "threat": "19",
        "skill": "Luta",
        "damage": "2d6",
        "attributes": ("Força",),
        "critical_multiplier": "2",
        "damage_type": "Corte",
    },
}

GLOBALMODIFIERS = {
    "Bonus de Ataque": "@{ataquetemp}",
    "Bonus de Condição": "@{condicaomodataque}",
    "Bonus de Condição2": "@{condicaomodataquecc}",
    "Bonus dano Temporario": "@{danotemp}",
    "Bonus Rolagem": "@{rolltemp}",
    "Concatenaçao de ataque": "@{condicaomodataque}+@{condicaomodataquecc}]]+@{ataquetemp}",
    "Concatenaçao de Dano": "@{danotemp}+@{rolltemp}",
}

PERICIASATACK = {
    "Luta": "[[@{lutatotal}",
    "Pontaria": "[[@{pontariatotal}",
    "Atuação": "[[@{atuacaototal}",
    "Furtividade": "[[@{furtividadetotal}",
}

PERICIAS = {
    "Acrobacia": "@{acrobaciatotal}",
    "Adestramento": "@{adestramentototal}",
    "Atletismo": "@{atletismototal}",
    "Atuação": "@{atuacaototal}",
    "Cavalgar": "@{cavalgartotal}",
    "Conhecimento": "@{conhecimentototal}",
    "Cura": "@{curatotal}",
    "Diplomacia": "@{diplomaciatotal}",
    "Enganação": "@{enganacaototal}",
    "Furtividade": "@{furtividadetotal}",
    "Guerra": "@{guerratotal}",
    "Intimidação": "@{intimidacaototal}",
    "Intuição": "@{intuicaototal}",
    "Investigação": "@{investigacaototal}",
    "Jogatina": "@{jogatinatotal}",
    "Ladinagem": "@{ladinagemtotal}",
    "Luta": "@{lutatotal}",
    "Misticismo": "@{misticismototal}",
    "Nobreza": "@{nobrezatotal}",
    "Ofício": "@{oficiototal}",
    "Ofício2": "@{oficio2total}",
    "Percepção": "@{percepcaototal}",
    "Pilotagem": "@{pilotagemtotal}",
    "Pontaria": "@{pontariatotal}",
    "Religião": "@{religiaototal}",
    "Sobrevivência": "@{sobrevivenciatotal}",
}

RESISTENCIAS = {
    "Fortitude": "@{fortitudetotal}",
    "Reflexos": "@{reflexostotal}",
    "Vontade": "@{vontadetotal}",
}

PERICIAS_ESPECIALISTA = {
    skill: formula
    for skill, formula in PERICIAS.items()
    if skill != "Luta"
}
PERICIAS_ESPECIALISTA.update(RESISTENCIAS)

DADOSCOMUNS = {
    "d4": "1d4",
    "d6": "1d6",
    "d8": "1d8",
    "d10": "1d10",
    "d12": "1d12",
    "2d6": "2d6",
}

DADOSEXOTICOS = {
    "Min": "1d1",
    "d2": "1d2",
    "d3": "1d3",
    "2d4": "2d4",
    "3d4": "3d4",
    "3d6": "3d6",
    "2d8": "2d8",
    "2d10": "2d10",
    "4d6": "4d6",
    "4d8": "4d8",
    "3d10": "3d10",
    "4d10": "4d10",
    "Max": "4d12",
}

DADOSPADRAO = {
    "Comuns": DADOSCOMUNS,
    "Exóticos": DADOSEXOTICOS,
}

DAMAGE_STEP_TRACKS = {
    "Padrão": (
        "1d1", "1d2", "1d3", "1d4", "1d6", "1d8", "1d10", "1d12",
        "3d6", "4d6", "4d8", "4d10", "4d12",
    ),
    "Especial: 2d4": (
        "1d1", "1d2", "1d3", "1d4", "1d6", "2d4", "1d10", "1d12",
        "3d6", "4d6", "4d8", "4d10", "4d12",
    ),
    "Especial: 2d8": (
        "1d1", "1d2", "1d3", "1d4", "1d6", "1d8", "1d10", "2d6",
        "2d8", "3d8", "4d8", "4d10", "4d12",
    ),
    "Especial: 3d4": (
        "1d1", "1d2", "1d3", "1d4", "1d6", "1d8", "1d10", "3d4",
        "3d6", "4d6", "4d8", "4d10", "4d12",
    ),
    "Especial: 2d10": (
        "1d1", "1d2", "1d3", "1d4", "1d6", "1d8", "1d10", "2d6",
        "2d8", "2d10", "3d10", "4d10", "4d12",
    ),
}

DAMAGE_SPECIAL_TRACK_BY_DIE = {
    "2d4": "Especial: 2d4",
    "2d6": "Especial: 2d8",
    "3d4": "Especial: 3d4",
    "2d8": "Especial: 2d10",
    "2d10": "Especial: 2d10",
    "3d10": "Especial: 2d10",
}
