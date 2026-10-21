"""Magias, elegibilidade de poções/óleos/granadas e fabricação de pergaminhos."""
from dataclasses import asdict, dataclass
from decimal import Decimal
from hashlib import sha256
import json
from math import ceil
import re

from crafting_core import format_money, money
from fabrication import Creator, FabricationQuote, validate_creator
from spell_data import SPELL_DATA
from weapon_catalog import search_key

SPELLS = {row['id']: row for row in SPELL_DATA}
BASE_PM = (0, 1, 3, 6, 10, 15)
FORMS = ('Poção', 'Óleo', 'Granada')


def find_spells(query='', circle='Todos', book='Todos', tradition='Todos'):
    needle = search_key(query)
    return sorted((s for s in SPELLS.values()
        if (circle == 'Todos' or s['circle'] == int(circle))
        and (book == 'Todos' or s['book'] == book)
        and (tradition == 'Todos' or s['tradition'] in (tradition, 'Universal'))
        and needle in search_key(' '.join((s['name'], s['school'], s['source'], s['stats'])))),
        key=lambda s: search_key(s['name']))


def effective_parameters(spell, selected=()):
    params = {key: spell.get(key, '') for key in ('target', 'area', 'effect', 'duration')}
    for enhancement in selected:
        text = enhancement['text']
        for key, label in (('target', 'alvo'), ('area', 'área'), ('effect', 'efeito'), ('duration', 'duração')):
            change = re.search(r'(?:muda (?:o |a )?'+label+r'|(?:o |a )'+label+r') para ([^.;]+)', text, re.I)
            if change:
                value = re.split(r'\s+e (?:o |a )?(?:alvo|efeito|duração|alcance|área)\b', change[1], maxsplit=1)[0]
                params[key] = value
                if key in ('area', 'effect', 'target'):
                    for other in ('area', 'effect', 'target'):
                        if other != key:
                            params[other] = ''
    if search_key(params['area']).startswith('alvo'):
        target = re.search(r'\(([^)]+)\)', params['area'])
        params['target'] = target[1] if target else params['area'][4:].strip(' :')
        params['area'] = ''
    if search_key(params['target']).startswith(('area', 'uma area')):
        params['area'], params['target'] = params['target'], ''
    return params


def potion_forms(spell, selected=()):
    p = effective_parameters(spell, selected)
    target = search_key(p['target'])
    forms = []
    # Uma área alternativa continua disponível junto da opção de alvo.
    if p['area'] and not re.search(r'criaturas? escolhidas?', search_key(p['area'])):
        forms.append('Granada')
    if target:
        multiple = bool(re.search(r'\b(?:ate|duas|dois|[2-9])\b|aliados|criaturas escolhidas|objetos ', target))
        if not multiple:
            creature = any(w in target for w in ('voce', 'criatura', 'animal', 'humanoide', 'monstro', 'espirito', 'construto', 'morto-vivo', 'morto- -vivo'))
            obj = any(w in target for w in ('objeto', 'arma', 'armadura', 'escudo', 'vestuario', 'alimento',
                                         'texto', 'item ', 'superficie', 'cadaver', 'pocao', 'frasco', 'materia-prima'))
            if creature:
                forms.append('Poção')
            if obj:
                forms.append('Óleo')
    return tuple(dict.fromkeys(forms))


def eligibility_text(spell, selected=()):
    forms = potion_forms(spell, selected)
    if forms:
        return ' / '.join(forms) + ' — conforme o alvo ou a área da configuração selecionada.'
    return 'Não pode virar poção nesta configuração: exige alvo de uma criatura/objeto ou área. Consulte os aprimoramentos; pergaminho aceita qualquer magia.'


@dataclass(frozen=True)
class ConsumableDesign:
    spell_id: str
    kind: str = 'Poção'
    name: str = ''
    enhancements: tuple[tuple[str, int], ...] = ()
    quantity: int = 1
    known: bool = True
    double_batch: bool = False
    unstable: bool = False
    extra_cost: Decimal = Decimal(0)
    special_cost_confirmed: bool = False
    special_requirements_confirmed: bool = False
    magic_tradition: str = 'Arcana'
    special_drink: bool = False


@dataclass(frozen=True)
class ConsumableQuote:
    spell: dict
    selected: tuple[dict, ...]
    pm: int
    activation_pm: int
    market_price: Decimal
    unit_cost: Decimal
    fabrication: FabricationQuote
    notes: tuple[str, ...]


def potion_enhancement_allowed(enhancement):
    """Tempo de ativação e conjuração discreta não são opções de uma poção."""
    text = search_key(enhancement['text'])
    if enhancement['id'] in ('Magia Acelerada', 'Magia Discreta'):
        return False
    return not re.search(r'(?:muda|reduz|altera) (?:o tempo de |a )?execucao (?:da magia )?para (?:(?:uma?|a) )?(?:acao )?(?:reacao|livre)', text)


def selected_enhancements(spell, design, creator=None):
    """Valida a composição da receita, sem avaliar a ficha de quem a fabrica."""
    options = {e['id']: e for e in spell['enhancements']}
    for name, cost in (('Magia Ampliada', 2), ('Magia Acelerada', 4), ('Magia Discreta', 2)):
        options[name] = dict(id=name, text=f'{name} (+{cost} PM): ' + {
            'Magia Ampliada': 'aumenta o alcance em um passo ou dobra a área.',
            'Magia Acelerada': 'muda a execução para livre (uma por rodada).',
            'Magia Discreta': 'sem gestos nem palavras.'}[name],
            cost=cost, min_circle=2 if name == 'Magia Acelerada' else 1,
            repeatable=False, exclusive=False)
    selected, seen = [], set()
    for key, repeats in design.enhancements:
        if key in seen or key not in options:
            raise ValueError('Aprimoramento desconhecido ou repetido na configuração.')
        seen.add(key)
        e = options[key]
        if design.kind != 'Pergaminho' and not potion_enhancement_allowed(e):
            raise ValueError('Poções, óleos e granadas não usam aprimoramentos de reação, ação livre ou Magia Discreta.')
        if isinstance(repeats, bool) or not isinstance(repeats, int) or not 1 <= repeats <= 100:
            raise ValueError('Repetições devem ser inteiros entre 1 e 100.')
        if repeats > 1 and not e['repeatable']:
            raise ValueError('Este aprimoramento não permite repetição: '+e['text'])
        selected.append(dict(e, repeats=repeats))
    if len(selected) > 1 and any('não pode ser usado em conjunto' in e['text'].casefold() for e in selected):
        raise ValueError('Um aprimoramento selecionado proíbe combinação com outros.')
    if sum(e.get('exclusive', False) for e in selected) > 1:
        raise ValueError('Escolha uma alternativa de “em vez do normal” por configuração.')
    return tuple(selected)


def quote_consumable(design, creator, *, purchase=False):
    if purchase:
        creator = Creator()
    validate_creator(creator)
    if design.spell_id not in SPELLS or design.kind not in (*FORMS, 'Pergaminho'):
        raise ValueError('Escolha uma magia e um tipo de item válidos.')
    if isinstance(design.quantity, bool) or not isinstance(design.quantity, int) or not 1 <= design.quantity <= 9999:
        raise ValueError('Quantidade deve ser um inteiro entre 1 e 9999.')
    s, a = SPELLS[design.spell_id], creator.abilities
    selected = selected_enhancements(s, design)
    potion = design.kind != 'Pergaminho'
    if potion and design.kind not in potion_forms(s, selected):
        raise ValueError(eligibility_text(s, selected))
    upgrades_pm = sum(e['cost']*e['repeats'] for e in selected)
    base_pm = BASE_PM[s['circle']]
    pm = base_pm + (upgrades_pm if potion else 0)
    extra_cost = money(design.extra_cost)
    market = Decimal(30*max(1,pm)**2) + extra_cost
    cost = Decimal(10*max(1,pm)**2) + extra_cost
    if purchase:
        # A compra mantém a composição do item, sem aplicar métodos do fabricante.
        return ConsumableQuote(s, selected, pm, upgrades_pm if not potion else 0, market, market,
                               FabricationQuote(market*design.quantity, None, 0, 1), ())
    dc, notes = 20+pm, []
    if not potion and 'Tinta do Mago' in a:
        cost /= 2
        notes.append('Tinta do Mago: metade da matéria-prima, com Escrever Pergaminho presumido.')
    if not potion and 'Psicografia' in a:
        if design.magic_tradition != 'Divina' and s['tradition'] != 'Divina':
            raise ValueError('Psicografia altera a CD de pergaminhos de magias divinas.')
        dc += 5
        notes.append('Psicografia: pergaminho de magia divina desconhecida, CD +5.')
    vineyard = potion and (design.special_drink or 'Zelador dos Vinhedos' in a)
    if vineyard:
        if design.kind != 'Poção' or not re.fullmatch(r'1 criatura(?: voluntária)?', effective_parameters(s, selected)['target'], re.I):
            raise ValueError('A bebida de Zelador dos Vinhedos exige alvo 1 criatura.')
        dc += 5
        notes.append('Zelador dos Vinhedos, bebida especial: CD +5; gasto adicional informado na receita.')
    capacity = 1 + int(design.double_batch)
    if potion and 'Síntese Rápida' in a or not potion and 'Copista' in a:
        capacity += 1
        notes.append('Produção ampliada; paga todas as unidades. Dois efeitos de dobro resultam em triplo (T20, Clarificações de Regras).')
    penalty = -5 if design.double_batch else 0
    days, time_text, temporary = ceil(design.quantity/capacity), '', ''
    distinctions = set(creator.distinctions)
    modes = []
    if potion:
        if design.unstable or 'Catalisador Instável' in a:
            modes.append('Catalisador Instável')
        modes += [name for name in ('Laboratório Natural','Remédios da Floresta','Efeito Placebo') if name in distinctions]
    if len(modes) > 1:
        raise ValueError('Compare um método de fabricação por vez: '+', '.join(modes)+'.')
    if modes:
        if design.double_batch:
            raise ValueError('O método instantâneo cria uma unidade por uso; desmarque o lote duplo.')
        mode = modes[0]
        days, penalty, capacity = 0, 0, 1
        actions = '1 ação' if design.quantity==1 else str(design.quantity)+' ações'
        if mode == 'Laboratório Natural':
            time_text = 'Sem tempo de fabricação'
            notes.append('Laboratório Natural: mantém o teste e a matéria-prima; usos/dia conforme a distinção.')
        elif mode == 'Remédios da Floresta':
            if s['circle'] > 2:
                raise ValueError('Remédios da Floresta usa receitas de 1º e 2º círculos.')
            cost, dc, time_text, temporary = Decimal(0), None, actions+(' padrão' if design.quantity==1 else ' padrão'), 'Fim da cena'
            notes.append(f'Remédios da Floresta: {pm} PV por unidade, recuperáveis apenas com descanso; receita da drogadora presumida.')
        else:
            if mode == 'Efeito Placebo' and s['circle'] != 1:
                raise ValueError('Efeito Placebo produz poções de magias de 1º círculo.')
            cost /= 2
            dc, time_text, temporary = None, actions+(' completa' if design.quantity==1 else ' completas'), 'Fim da cena'
            notes.append(mode+': 3 PM por unidade; sem teste; expira no fim da cena.')
    if not potion:
        notes.append('Pergaminho fabricado sem aprimoramentos. As seleções são um plano de ativação e não alteram preço, CD ou tempo.')
        notes.append(f'Na ativação, o custo dos aprimoramentos selecionados é {upgrades_pm} PM; requisitos de leitura seguem o livro.')
    rules_text = ' '.join((s['stats'],s['description'],*[e['text'] for e in selected]))
    if re.search(r'componente material|custo adicional', rules_text, re.I):
        notes.append('Há componente/custo adicional no texto da magia. O orçamento inclui apenas o valor informado em Gasto adicional.')
    notes.append('Ofício ('+('cozinheiro' if vineyard else 'alquimista' if potion else 'escriba')+'). T20, p. 121–122 e 333.')
    if temporary:
        notes.append('Item temporário: '+temporary+'.')
    fabrication = FabricationQuote(cost*design.quantity, dc, days, capacity, penalty,
        notes=tuple(notes), time_text=time_text, temporary=temporary)
    return ConsumableQuote(s, selected, pm, upgrades_pm if not potion else 0, market, cost, fabrication, tuple(notes))


def consumable_description(design, quote, *, purchase=False):
    s = quote.spell
    text = f"{s['name']} · {s['tradition']} {s['circle']} ({s['school']})\n{s['stats']}\n\n{s['description']}"
    if quote.selected:
        text += '\n\n' + ('Plano de aprimoramentos na ativação:' if design.kind == 'Pergaminho' else 'Aprimoramentos da fórmula:')
        text += '\n' + '\n'.join(f"{e['repeats']}× {e['text']}" for e in quote.selected)
    if purchase:
        notes = [f'Comprando · Preço de compra: {format_money(quote.market_price)} por unidade.',
                 f'Total de {design.quantity} unidade(s): {format_money(quote.market_price*design.quantity)}.']
        if design.kind == 'Pergaminho':
            notes.append(f'O pergaminho contém a magia básica. Aprimoramentos são aplicados na leitura: +{quote.activation_pm} PM; não alteram o preço do item.')
    else:
        notes = ['Fabricando · '+quote.fabrication.summary(), *quote.notes]
    return text + '\n\n' + '\n'.join(notes) + '\nFonte: ' + s['source']


def consumable_macro(design, quote, *, purchase=False):
    def safe(text):
        return text.replace('{', '&#123;').replace('}', '&#125;').replace('|', '&#124;').replace('\n', '<br>')
    name = design.name.strip() or design.kind + ' de ' + quote.spell['name']
    return '&{template:t20}{{character=@{character_name}}}{{rollname='+safe(name)+'}}{{desc='+safe(consumable_description(design, quote, purchase=purchase))+'}}'


def consumable_item(design, creator, quote, *, purchase=False):
    from shopping_core import json_value
    payload = json_value(dict(name=design.name.strip() or design.kind+' de '+quote.spell['name'],
        category='Customizados', group=design.kind, source=quote.spell['source'],
        description=consumable_description(design, quote, purchase=purchase), special=False, spaces='0.5', spaces_value='0.5',
        price=format_money(quote.market_price), full_price=str(quote.market_price),
        price_value=str(quote.market_price if purchase else quote.unit_cost),
        configuration=asdict(design), creator=asdict(creator), macro=consumable_macro(design, quote, purchase=purchase),
        acquisition='purchase' if purchase else 'fabrication',
        expires='' if purchase else quote.fabrication.temporary))
    digest = sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode('utf8')).hexdigest()
    return dict(payload, id='custom:'+digest)
