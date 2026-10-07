import re


VERSAO = "0.01.8.0"  # 0-Versão oficial. 01-Versão funcional. 8-Teste. 0-Correção.
RELEASE_API_URL = "https://api.github.com/repos/GustavoREX/MacroGenerator/releases/tags/Newest"

BEST_DIE_FORMULA = "?{melhor dado|Não,1d20|Sim,2d20kh1}"
SKILL_MACRO_CLOSING = "]]}}"
ATTACK_PRIDE_EFFECT = "[[(?{Orgulho|0}*2)]]"
SKILL_MACRO_BASE = (
    "&{template:t20}{{character=@{character_name}}}"
    "{{rollname=Teste de Perícia}}"
    "{{theroll=?{Perícia: "
    "|Acrobacia,Acrobacia[[1d20+[[@{acrobaciatotal}]]"
    "| Adestramento,Adestramento[[1d20+[[@{adestramentototal}]]"
    "| Atletismo,Atletismo[[1d20+[[@{atletismototal}]]"
    "| Atuação,Atuação[[1d20+[[@{atuacaototal}]]"
    "| Cavalgar,Cavalgar[[1d20+[[@{cavalgartotal}]]"
    "| Conhecimento,Conhecimento[[1d20+[[@{conhecimentototal}]]"
    "| Cura,Cura[[1d20+[[@{curatotal}]]"
    "| Diplomacia,Diplomacia[[1d20+[[@{diplomaciatotal}]]"
    "| Enganação,Enganação[[1d20+[[@{enganacaototal}]]"
    "|  Furtividade,Furtividade[[1d20+[[@{furtividadetotal}]]"
    "| Guerra,Guerra[[1d20+[[@{guerratotal}]]"
    "| Intimidação,Intimidação[[1d20+[[@{intimidacaototal}]]"
    "| Intuição,Intuição[[1d20+[[@{intuicaototal}]]"
    "| Investigação,Investigação[[1d20+[[@{investigacaototal}]]"
    "| Jogatina,Jogatina[[1d20+[[@{jogatinatotal}]]"
    "| Ladinagem,Ladinagem[[1d20+[[@{ladinagemtotal}]]"
    "| Luta,Luta[[1d20+[[@{lutatotal}]]"
    "| Misticismo,Misticismo[[1d20+[[@{misticismototal}]]"
    "| Nobreza,Nobreza[[1d20+[[@{nobrezatotal}]]"
    "| Ofício,Oficio [[1d20+[[@{oficiototal}]]"
    "|Ofício2,Oficio2[[1d20+[[@{oficio2total}]]"
    "| Percepção,Percepção[[1d20+[[@{percepcaototal}]]"
    "| Pilotagem,Pilotagem[[1d20+[[@{pilotagemtotal}]]"
    "| Pontaria,Pontaria[[1d20+[[@{pontariatotal}]]"
    "|Religião,Religião[[1d20+[[@{religiaototal}]]"
    "| Sobrevivência,Sobrevivência"
    "[[1d20+[[@{sobrevivenciatotal}]]}"
)
RESISTANCE_MACRO_BASE = (
    "&{template:t20}{{character=@{character_name}}}"
    "{{rollname=Teste de Perícia}}"
    "{{theroll=?{Resistencia: "
    "| Fortitude,Fortitude[[1d20+[[@{fortitudetotal}]]"
    "| Reflexos,Reflexos[[1d20+[[@{reflexostotal}]]"
    "| Vontade,Vontade[[1d20+[[@{vontadetotal}]]}"
)
MACRO_BUTTON_PATTERN = re.compile(
    r"\[([^\]\r\n]+)\]\(~@\{character_name\}\|([^\)\r\n]+)\)",
    flags=re.IGNORECASE,
)

ADVANCED_QUESTION_ESCAPES = str.maketrans({
    "|": "&#124;",
    ",": "&#44;",
    "{": "&#123;",
    "}": "&#125;",
    "&": "&#38;",
    "=": "&#61;",
    "(": "&#40;",
    ")": "&#41;",
    "[": "&#91;",
    "]": "&#93;",
})
