"""Lembretes curtos para a macro; o catálogo mantém as descrições completas."""
from weapon_catalog import base_name


# Apenas ativações aplicáveis a armas. Custos de outras categorias não entram.
PM_ACTIVATIONS = {
    "Shuriken": ("1 PM", "ataque adicional de shuriken contra o mesmo alvo (1/rodada)."),
    "Couraça de kaiju": ("2 PM", "ignora efeitos que reduzem o dano, exceto RD."),
    "Anticriatura": ("2 PM", "+4d8 de dano ao acertar uma criatura do tipo escolhido (1/rodada)."),
    "Assassina": ("2 PM", "rerrola resultados 1 nos dados extras de Ataque Furtivo."),
    "Congelante": ("2 PM", "ao acertar, enreda o alvo por 1 rodada (1/rodada)."),
    "Corrosiva": ("2 PM", "ao acertar, causa 4d4 de ácido na próxima rodada (1/rodada)."),
    "Dançarina": ("1 PM", "ação de movimento: a arma flutua e ataca um alvo em alcance curto com suas estatísticas."),
    "Elétrica": ("2 PM", "ao acertar, causa 3d8 de eletricidade a outra criatura em alcance curto (1/rodada)."),
    "Flamejante": ("2 PM", "ao atacar, causa 6d6 de fogo; Ref CD For/Des reduz à metade (1/rodada)."),
    "Piedosa": ("1 PM", "ativa ou desativa o encanto."),
    "Tumular": ("2 PM", "ao atacar, aumenta o bônus de trevas para 2d8 e perde 1d8 PV (1/rodada)."),
    "Veloz": ("PM de Ataque Extra", "usa Ataque Extra com esta arma; −1 PM se já possui a habilidade."),
    "Venenosa": ("2 PM", "ao acertar, envenena: perde 1d12 PV/rodada por 3 rodadas (1/rodada)."),
    "Alvorada": ("2 PM", "cega uma criatura em alcance curto por 1 rodada; Fort CD For/Des evita (1/rodada, 1/cena por criatura)."),
    "Cantante": ("1 PM", "você e aliados em alcance curto recebem +1 no ataque por 1 rodada, cumulativo com itens."),
    "Ciclônica": ("1 PM", "cone de 9m empurra criaturas 3m; Fort CD For/Des evita (1/rodada)."),
    "Crescente": ("2 PM", "+1 passo de dano e +1,5m de alcance até o fim do turno."),
    "Cristalina": ("1 PM", "ao acertar, ofusca o alvo por 1 rodada (1/rodada)."),
    "Cronal": ("3 PM", "ao atacar, rola 2 dados e usa o melhor; no próximo ataque sofrido até seu próximo turno, o atacante usa o pior de 2 dados."),
    "Cuidadora": ("2 PM", "recebe RD 10 contra um dano sofrido (1/rodada)."),
    "Espreitadora": ("2 PM", "ao atacar, deixa o alvo desprevenido; Von CD For/Des evita (1/cena por criatura)."),
    "Frenética": ("1 PM", "ao acertar, +1 no ataque e dano até o fim da cena; acumula até +5."),
    "Gárgula": ("2 PM", "convoca parceiro combatente iniciante até o fim da cena."),
    "Infestada": ("2 PM", "ao acertar, alvo perde 2d6 PV por veneno e fica enjoado por 1d4 rodadas; Fort CD For/Des evita a condição."),
    "Reflexiva": ("PM iguais ao círculo da magia", "reflete a magia recebida contra o conjurador (1/rodada)."),
    "Ressonante": ("2 PM", "ao acertar, aplica o mesmo ataque contra outro alvo em alcance curto; se acertar, causa metade do dano como psíquico."),
    "Sepulcral": ("2 PM de Tumular, sem custo extra", "ao acertar com Tumular ativado, impede recuperar PV por 1d4 rodadas."),
    "Sombria": ("PM da magia Escuridão", "lança Escuridão; −1 PM se já conhece a magia."),
    "Vampírica": ("1 PM", "ao atacar, +2d6 de trevas e recupera PV iguais ao dano de trevas causado."),
}


def compact_weapon_description(design):
    names = [base_name(design.weapon_name), *(base_name(name) for name in design.improvements),
             base_name(design.material), base_name(design.second_material), *(base_name(name) for name in design.enchantments)]
    rd = sum({"Penetrante": 5, "Aço-rubi": 10, "Energética": 20}.get(name, 0) for name in names)
    parts = []
    # O machado de lenha só ignora esses 5 pontos contra objetos e construtos.
    if names[0] == "Machado de lenha":
        parts.append(f"Ignora {rd} de RD ({rd + 5} contra objetos e construtos)." if rd else
                     "Ignora 5 de RD contra objetos e construtos.")
    elif rd:
        parts.append(f"Ignora {rd} de RD.")
    for name in names:
        if name in PM_ACTIVATIONS:
            cost, effect = PM_ACTIVATIONS[name]
            parts.append(f"{name} ({cost}): {effect}")
    return " | ".join(parts)
