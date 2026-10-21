"""Forja dos itens mundanos, alquímicos e receitas especiais das distinções."""
from dataclasses import dataclass, asdict
from decimal import Decimal
from hashlib import sha256
import json
from math import ceil
import re

from crafting_core import money, format_money, IMPROVEMENT_COSTS
from fabrication import Creator, FabricationQuote, validate_creator
from shopping_core import CATALOGS, parse_spaces, source_price, json_value
from weapon_catalog import search_key, base_name

CATEGORIES = ('Aventura','Ferramentas','Vestuário','Esotéricos','Preparados','Catalisadores',
              'Venenos','Alimentos e bebidas','Munições','Aparatos')
ITEMS = {row['id']: dict(row) for category in CATEGORIES for row in CATALOGS[category]}
for row in CATALOGS['Animais e veículos']:
    if row.get('group') == 'Veículos' or row['name'] == 'Alforje' or any(word in row['name'] for word in ('Arreios','Estribos','Ornamento')):
        ITEMS[row['id']] = dict(row, category='Veículos e montaria')

SPECIALS = (
    ('mutagenico-tonificante','Mutagênico tonificante',60,15,1,'alquimista','Mutagenista',
     'Fornece +1 em um atributo específico; exaurir aumenta o bônus em +1. Uso exclusivo do fabricante; segue as regras de biochoque e sobrecarga.','Heróis de Arton, p. 201 (PDF 203)'),
    ('mutagenico-energizante','Mutagênico energizante',90,15,1,'alquimista','Mutagenista',
     'Permite uma magia arcana de 1º círculo específica como habilidade simulada. Uso exclusivo do fabricante; regras de biochoque e sobrecarga.','Heróis de Arton, p. 201 (PDF 203)'),
    ('mutagenico-despersonalizante','Mutagênico despersonalizante',150,15,1,'alquimista','Mutagenista',
     'Fornece uma habilidade racial específica, exceto de construtos ou mortos-vivos. Uso exclusivo do fabricante; regras de biochoque e sobrecarga.','Heróis de Arton, p. 201 (PDF 203)'),
    ('ornitoptero','Ornitóptero goblin',None,20,7,'artesão','Aeronauta Goblin',
     'Veículo Grande, voo 15m, um piloto Pequeno e 10 espaços de carga; operado apenas pelo criador. Custo de fabricação publicado: T$ 300. Melhorias de Engenharia Aeronáutica seguem a progressão de itens superiores.','Heróis de Arton, p. 108 (PDF 110)'),
    ('flecha-da-morte','Flecha da morte',None,None,1,'armeiro','Arqueiro de Lenórienn',
     'Custo direto de T$ 100 e um dia para criar uma flecha. Causa um dado extra e +2 na margem de ameaça; benefícios e limite de flechas variam com os poderes da distinção. Nenhum teste de fabricação é indicado no poder.','Heróis de Arton, p. 120 (PDF 122)'),
    ('arco-arcano','Ritual do Arco Arcano',None,None,1,'armeiro','Arqueiro de Lenórienn',
     'Transforma um arco já existente em arco arcano com um dia e T$ 100 de componentes. Não fabrica o arco-base; ele também conta como um esotérico à escolha.','Heróis de Arton, p. 120 (PDF 122)'),
    ('panela','Panela de Estimação',None,None,1,'cozinheiro','Mestre Cozinheiro',
     'Reposição da arma ou escudo que funciona como instrumentos de cozinheiro: um dia e gasto de T$ 100, conforme a marca da distinção.','Heróis de Arton, p. 188 (PDF 190)'),
)
for key,name,price,dc,days,profession,group,description,source in SPECIALS:
    ITEMS['recipe:'+key] = dict(id='recipe:'+key,name=name,price='' if price is None else str(price),
        category='Receitas de Distinções', group=group, description=description, source=source,
        spaces='0.5' if profession=='alquimista' else '', recipe_dc=dc, recipe_days=days,
        profession=profession, direct_cost=300 if key=='ornitoptero' else 100 if price is None else None)

ORNITHOPTER_MODS = {
    'Armado': 'Suporte para uma arma de fogo e 20 munições. Acoplar ou remover a arma é ação completa.',
    'Blindado': '+10 na Defesa.',
    'Bombardeiro': 'Compartimento para quatro preparados ou poções. Arremesso com alcance uma categoria maior e CD de resistência +2.',
    'Camuflado': '+10 em Furtividade; em voo pode se esconder mesmo sem cobertura ou camuflagem.',
    'Dobrável': 'Pode dobrar para veículo Médio terrestre, deslocamento 12m; dobrar/desdobrar é ação completa.',
    'Durável': 'PV iguais aos do criador, em vez de metade.',
    'Espaçoso': 'Mais um passageiro Pequeno ou 10 espaços de carga.',
    'Estável': '+5 nos testes de Pilotagem.',
    'Resistente': '+5 de redução de dano.',
    'Veloz': '+6m no deslocamento de voo.',
}


def find_general_items(query='', category='Todos'):
    key = search_key(query)
    return sorted((r for r in ITEMS.values() if (category=='Todos' or r['category']==category)
        and key in search_key(' '.join((r['name'],r.get('source',''),r.get('group',''))))), key=lambda r: search_key(r['name']))


def item_rules(item):
    category, name = item['category'], base_name(item['name'])
    if category == 'Receitas de Distinções':
        return item['profession'],item['recipe_dc'],item['recipe_days'],item['profession']=='alquimista',1
    dc = 15 if category in ('Aventura','Munições','Preparados','Catalisadores') else 20
    alchemical = category in ('Preparados','Catalisadores','Venenos')
    profession = 'alquimista' if alchemical else 'armeiro' if category=='Munições' else 'alfaiate' if category=='Vestuário' else 'cozinheiro' if category=='Alimentos e bebidas' else 'engenhoqueiro' if category=='Aparatos' else 'artesão'
    days = 1 if alchemical or category=='Munições' else 7
    capacity = 1
    if category=='Venenos':
        # T20 p. 161: modificadores publicados, não a CD de resistência da vítima.
        increase = re.search(r'CD para fabricar[^.]*aumenta em \+(\d+)', item['description'])
        if increase:
            dc += int(increase[1])
    if category=='Alimentos e bebidas':
        drink = name in ('Baba de troll','Barba queimada','Cerveja deheoni','Dilínio','Grogue negro','Grogue rubro',
                         'Hidromel uivante','Licor feérico','Sidra ahleniense','Vinho Pruss','Vinho élfico')
        if drink:
            dc,days = 20,1  # As CDs variáveis na descrição são de Fortitude ao beber, não de fabricação.
        else:
            dc,days,capacity = 15,Decimal(1)/24,5
    if category=='Aventura' and (name in ('Óleo','Tocha') or name.startswith('Água benta')):
        days=1
    return profession,dc,days,alchemical,capacity


@dataclass(frozen=True)
class GeneralDesign:
    item_id: str
    quantity: int = 1
    double_batch: bool = False
    price_override: Decimal | None = None
    dc_override: int | None = None
    extra_cost: Decimal = Decimal(0)
    second_dish: str = ''
    modifications: tuple[str,...] = ()
    innovations: tuple[str,...] = ()
    days_override: Decimal | None = None


@dataclass(frozen=True)
class GeneralQuote:
    item: dict
    market_price: Decimal | None
    unit_cost: Decimal
    fabrication: FabricationQuote
    description: str


def quote_general(design, creator=Creator(), *, purchase=False):
    if purchase:
        creator = Creator()
    validate_creator(creator)
    if design.item_id not in ITEMS:
        raise ValueError('Escolha um item do catálogo.')
    if isinstance(design.quantity,bool) or not isinstance(design.quantity,int) or not 1<=design.quantity<=9999:
        raise ValueError('Quantidade deve ser um inteiro entre 1 e 9999.')
    item = ITEMS[design.item_id]
    if not purchase and base_name(item['name'])=='Dilínio':
        raise ValueError('Dilínio não pode ser fabricado (Heróis de Arton, p. 237).')
    profession,dc,base_days,alchemical,food_capacity = item_rules(item)
    market = money(design.price_override) if design.price_override is not None else source_price(item)
    fixed = item.get('direct_cost')
    if not purchase and market is None and fixed is None:
        raise ValueError('O item tem preço variável: informe o preço de mercado para calcular a matéria-prima.')
    unit = Decimal(fixed) if fixed is not None else market/3 if market is not None else Decimal(0)
    if not purchase and design.dc_override is not None:
        if isinstance(design.dc_override,bool) or not isinstance(design.dc_override,int) or not 0<=design.dc_override<=200:
            raise ValueError('CD ajustada deve ser um inteiro entre 0 e 200.')
        dc = design.dc_override
    notes = [f'Ofício ({profession}). '+item.get('source','')]
    description = item['description']
    if design.modifications:
        if design.item_id!='recipe:ornitoptero' or len(set(design.modifications))!=len(design.modifications) or len(design.modifications)>4:
            raise ValueError('Ornitóptero permite até quatro melhorias diferentes de Engenharia Aeronáutica.')
        if any(n not in ORNITHOPTER_MODS for n in design.modifications):
            raise ValueError('Melhoria de ornitóptero desconhecida.')
        unit += Decimal(IMPROVEMENT_COSTS[len(design.modifications)])/3
        dc += 5*len(design.modifications)
        base_days = 30
        description += '\n\n'+'\n'.join(n+': '+ORNITHOPTER_MODS[n] for n in design.modifications)
    if design.innovations:
        from innovation_data import INNOVATIONS,innovation_reason
        if 'Balas' not in item['name'] or item['category']!='Munições':
            raise ValueError('Estas inovações são exclusivas de munições de arma de fogo.')
        if len(set(design.innovations))!=len(design.innovations) or len(design.innovations)>4:
            raise ValueError('Selecione até quatro inovações diferentes.')
        for name in design.innovations:
            if name not in INNOVATIONS:
                raise ValueError('Inovação desconhecida.')
            reason=innovation_reason(name,design.innovations,ammunition=True)
            if reason:
                raise ValueError(reason)
        increase=Decimal(IMPROVEMENT_COSTS[len(design.innovations)])
        unit+=increase/3
        market=None  # Inovações não possuem valor comercial.
        dc+=len(design.innovations)*5
        description+='\n\nInovações sem valor comercial, dependentes do criador:\n'+'\n'.join(n+': '+INNOVATIONS[n]['description'] for n in design.innovations)
    if design.second_dish:
        if not purchase and not set(creator.distinctions).intersection(('À Moda da Casa',)):
            raise ValueError('A combinação de pratos exige À Moda da Casa.')
        other = ITEMS.get(design.second_dish)
        if item['category']!='Alimentos e bebidas' or not other or other['category']!='Alimentos e bebidas':
            raise ValueError('Selecione dois pratos para combinar.')
        _,other_dc,other_days,_,_ = item_rules(other)
        other_price = source_price(other)
        if food_capacity!=5 or other_days!=Decimal(1)/24 or other_price is None:
            raise ValueError('À Moda da Casa combina pratos especiais, não bebidas ou itens sem preço fixo.')
        unit += other_price/3
        market = market+other_price if market is not None else None
        dc = max(dc,other_dc)
        description += '\n\nCombinado com '+other['name']+': '+other['description']
    elif 'À Moda da Casa' in creator.distinctions:
        raise ValueError('Escolha o segundo prato de À Moda da Casa.')
    extra = money(design.extra_cost)
    unit += extra
    if market is not None:
        market += extra
    if purchase:
        return GeneralQuote(item, market, market if market is not None else Decimal(0),
                            FabricationQuote((market or Decimal(0))*design.quantity, None, 0, 1), description)
    consumable=alchemical or item['category'] in ('Munições','Alimentos e bebidas') or item['category']=='Aventura' and base_days==1
    if design.double_batch and not consumable:
        raise ValueError('Produção em lote se aplica a consumíveis; itens comuns mantêm seu tempo por unidade.')
    capacity = (food_capacity if food_capacity==5 else 2) if design.double_batch else 1
    if alchemical and 'Síntese Rápida' in creator.abilities:
        capacity += 1
    penalty = -5 if design.double_batch else 0
    batches = ceil(design.quantity/capacity)
    if design.days_override is not None:
        base_days=money(design.days_override)
    days, time_text, temporary = base_days*batches,'',''
    if base_days==Decimal(1)/24:
        time_text = f'{batches} hora(s) de trabalho'
    methods = []
    if 'Catalisador Instável' in creator.abilities:
        if item['category']!='Preparados' and item.get('group')!='Mutagenista':
            raise ValueError('Catalisador Instável fabrica preparados; não se aplica a esta categoria.')
        methods.append('Catalisador Instável')
    if 'Laboratório Natural' in creator.distinctions:
        if not alchemical:
            raise ValueError('Laboratório Natural se aplica a itens alquímicos.')
        methods.append('Laboratório Natural')
    if 'Remédios' in creator.distinctions:
        if item['category']!='Preparados' or not re.search(r'PV|PM|pontos de (?:vida|mana)', description):
            raise ValueError('Remédios se aplica a preparados que fornecem PV ou PM.')
        methods.append('Remédios')
    if len(methods)>1:
        raise ValueError('Compare apenas um método especial de fabricação por vez.')
    if methods:
        method=methods[0]
        if method!='Remédios' and design.double_batch:
            raise ValueError('Desmarque o lote duplo para comparar este método especial.')
        if method!='Remédios':
            capacity,penalty=1,0
        if method=='Catalisador Instável':
            unit/=2
            dc,days,time_text,temporary=None,0,('1 ação completa' if design.quantity==1 else f'{design.quantity} ações completas'),'Fim da cena'
            notes.append('3 PM por unidade; metade do custo e sem teste.')
        elif method=='Laboratório Natural':
            days,time_text=0,'Sem tempo de fabricação'
            notes.append('Mantém teste e matéria-prima; usos por dia conforme os poderes da distinção.')
        else:
            medical_batches=ceil(design.quantity/capacity)
            days,time_text,temporary=Decimal(medical_batches)/144,f'{10*medical_batches} minutos','Fim da cena'
        notes.append(method+'.')
    if 'Golpe de Gênio' in creator.abilities and design.modifications:
        days=min(days,Decimal(7)*batches)
        time_text=''
        notes.append('Golpe de Gênio: uma semana por item superior; uso limitado por aventura/mês.')
    if temporary:
        notes.append('Item temporário: '+temporary+'.')
    if not design.item_id.startswith('recipe:'):
        notes.append('Regra de Ofício: matéria-prima = ⅓ do preço; CD simples 15 / complexo 20. Pratos: 1 hora e até cinco por lote com –5. CD ajustável para exceções do livro ou da mesa.')
    if item.get('group')=='Veículos':
        notes.append('Veículos muito grandes ou complexos podem exigir meses; o tempo-base pode ser ajustado na receita, conforme Ofício (T20, p. 122).')
    fabrication=FabricationQuote(unit*design.quantity,dc,days,capacity,penalty,notes=tuple(notes),time_text=time_text,temporary=temporary)
    return GeneralQuote(item,market,unit,fabrication,description)


def general_item(design,creator,quote,*,purchase=False):
    if purchase and quote.market_price is None:
        raise ValueError('Não há preço de compra para esta configuração. Informe uma cotação quando o item permitir comercialização.')
    item=quote.item
    payload=json_value(dict(name=item['name'],category='Customizados',group=item['category'],
        price=format_money(quote.market_price) if quote.market_price is not None else 'Sem preço de mercado publicado',
        price_value=str(quote.market_price if purchase else quote.unit_cost),full_price=None if quote.market_price is None else str(quote.market_price),
        spaces_value=parse_spaces(item.get('spaces','')),source=item.get('source',''),special=False,
        description=quote.description+'\n\n'+('Comprando · Preço de compra: '+format_money(quote.market_price)+' por unidade.' if purchase else 'Fabricando · '+quote.fabrication.summary()),configuration=asdict(design),
        acquisition='purchase' if purchase else 'fabrication',
        creator=asdict(creator),expires='' if purchase else quote.fabrication.temporary))
    return dict(payload,id='custom:'+sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True).encode('utf8')).hexdigest())
