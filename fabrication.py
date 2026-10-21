"""Orçamentos de forja; os requisitos do personagem são presumidos."""
from dataclasses import dataclass
from decimal import Decimal

from crafting_core import format_money

RACES = ('Outra', 'Hobgoblin', 'Kliren', 'Goblin')
POWERS = {
    'Síntese Rápida': ('alchemical', 'Dobra a produção de itens alquímicos e poções no mesmo tempo, pagando todas as unidades. T20, p. 70.'),
    'Catalisador Instável': ('alchemical', 'Fabrica um preparado ou poção em uma ação completa, por metade do custo e sem teste. Gasta 3 PM; dura até o fim da cena. Não se aplica a venenos ou catalisadores. T20, p. 69.'),
    'Tinta do Mago': ('scroll', 'Com Escrever Pergaminho, reduz à metade o custo de fabricação de pergaminhos. A habilidade básica é presumida na forja. T20, p. 39.'),
    'Copista': ('scroll', 'Com Escrever Pergaminho, dobra a produção no mesmo tempo, pagando ambas as unidades. A habilidade básica é presumida. Deuses de Arton, p. 40.'),
    'Psicografia': ('scroll', 'Simula pergaminho de magia divina desconhecida: CD +5, sem mudar preço ou tempo. Deuses de Arton, p. 40.'),
    'Zelador dos Vinhedos': ('potion', 'Simula a bebida especial com alvo 1 criatura: CD +5 e gasto adicional da bebida. Usa Ofício (cozinheiro). A versão comum não altera o orçamento. Deuses de Arton, p. 41.'),
    'Golpe de Gênio': ('equipment', 'Fabrica um item superior ou mágico em uma semana em vez de um mês, uma vez por aventura ou mês. Heróis de Arton, p. 71.'),
    'Gênio Inovador': ('equipment', 'Uma melhoria extra gratuita, fora do limite, e dois materiais especiais diferentes. Heróis de Arton, p. 71.'),
}

DISTINCTIONS = {
    'Laboratório Natural': dict(group='Drogadora', scope='alchemical', source='Heróis de Arton, p. 156 (PDF 158)',
        description='Fabrica um item alquímico ou poção sem gastar tempo. Ainda faz o teste de Ofício e paga a matéria-prima. Usos por dia iguais ao número de poderes da distinção.'),
    'Remédios da Floresta': dict(group='Drogadora', scope='potion', source='Heróis de Arton, p. 156 (PDF 158)',
        description='Uma poção de receita da drogadora em uma ação padrão, sem tibares. Paga PV iguais ao custo em PM da magia; só os recupera com descanso. A poção dura até o fim da cena. Receitas de 1º e 2º círculos.'),
    'Remédios': dict(group='Médico de Salistick', scope='prepared', source='Heróis de Arton, p. 183 (PDF 185)',
        description='Preparados que fornecem PV ou PM podem ser fabricados em 10 minutos em vez de um dia. Duram até o fim da cena; CD e matéria-prima normais.'),
    'Efeito Placebo': dict(group='Vigarista', scope='potion', source='Heróis de Arton, p. 213 (PDF 215)',
        description='Poção elegível de 1º círculo em uma ação completa: 3 PM, metade do custo e sem teste. Dura até o fim da cena. A escolha das magias da distinção é presumida.'),
    'Virtude do Forjador': dict(group='Forjador Litúrgico', scope='weapon', source='Deuses de Arton, p. 94 (PDF 96)',
        description='Se já sabe fabricar armas superiores por outra habilidade, fabrica-as na metade do tempo. O acesso às melhorias é presumido na forja.'),
    'Forja Devocional': dict(group='Forjador Litúrgico', scope='weapon', source='Deuses de Arton, p. 94 (PDF 96)',
        description='Transfere os encantos de uma arma doadora para uma arma fabricada por você: metade do tempo da arma mágica e a CD de fabricação dela. A doadora perde os encantos. A forja orça apenas a transferência, com a receptora já pronta.'),
    'Prata da Casa': dict(group='Mestre de Armearia', scope='firearm', source='Deuses de Arton, p. 110 (PDF 112)',
        description='Armas de fogo não mágicas, inclusive superiores, em uma semana em vez de um mês. CD e custo normais.'),
    'À Moda da Casa': dict(group='Mestre Cozinheiro', scope='food', source='Heróis de Arton, p. 188–189 (PDF 190–191)',
        description='Combina os efeitos de dois pratos especiais. Consome os ingredientes de ambos, usa a maior CD e leva o mesmo tempo de um prato normal. Selecione o segundo prato abaixo desta opção.'),
}


@dataclass(frozen=True)
class Creator:
    # Dados antigos continuam legíveis nos snapshots; não bloqueiam o orçamento.
    kind: str = 'Forja'
    level: int = 1
    intelligence: int = 1
    wisdom: int = 1
    key_attribute: int = 1
    max_circle: int = 5
    race: str = 'Outra'
    trained: bool = True
    tools: bool = True
    skill_bonus: int = 0
    powers: tuple[str, ...] = ()
    book: bool = True
    origin: str = 'Outra'
    distinctions: tuple[str, ...] = ()
    transfer_dc: int | None = None

    @property
    def abilities(self):
        return set(self.powers)


def validate_creator(c):
    if c.race not in RACES:
        raise ValueError('Raça desconhecida.')
    if any(name not in DISTINCTIONS for name in c.distinctions):
        raise ValueError('Distinção desconhecida.')


@dataclass(frozen=True)
class FabricationQuote:
    cost: Decimal
    dc: int | None
    days: int | Decimal
    units_per_day: int = 1
    penalty: int = 0
    permanent_pm: int = 0
    notes: tuple[str, ...] = ()
    time_text: str = ''
    temporary: str = ''

    @property
    def time_label(self):
        if self.time_text:
            return self.time_text
        if self.days==1:
            return '1 dia'
        if self.days==7:
            return '1 semana'
        if self.days==30:
            return '1 mês'
        return f'{self.days} dias'.replace('.', ',')

    @property
    def dc_label(self):
        return 'Sem teste' if self.dc is None else str(self.dc)

    def summary(self):
        return (f'Matéria-prima: {format_money(self.cost)} · CD {self.dc_label} · {self.time_label}'
                + (f' · Penalidade do lote {self.penalty:+d}' if self.penalty else '')
                + (f' · Sacrifício permanente: {self.permanent_pm} PM' if self.permanent_pm else '')
                + ('\n' + '\n'.join(self.notes) if self.notes else ''))


def equipment_fabrication(design, item, quote, creator, *, genius_week=False):
    validate_creator(creator)
    weapon = item.get('category', '').startswith('Armas')
    firearm = item.get('category') == 'Armas de fogo'
    base_dc = 15 if item.get('category') == 'Armas simples' or item.get('group') in ('Armaduras Leves', 'Escudos') else 20
    raw = quote.due_now / 3
    notes = ['Ofício (armeiro). T20, p. 121–122 e 333–334.']
    if creator.race == 'Hobgoblin':
        raw = (quote.due_now-quote.improvement_due)/3 + quote.improvement_due/4
        notes.append('Metalurgia Hobgoblin: ¼ das melhorias; a habilitação adicional é presumida. Ameaças, p. 84.')
    days = Decimal(30 if quote.improvement_count or quote.enchantment_count or getattr(quote, 'innovation_count', 0) else 7)
    d = set(creator.distinctions)
    if 'Virtude do Forjador' in d and weapon and quote.improvement_count:
        days /= 2
        notes.append('Virtude do Forjador: metade do tempo das armas superiores.')
    if 'Prata da Casa' in d and firearm and not quote.enchantment_count:
        days = min(days, Decimal(7))
        notes.append('Prata da Casa: arma de fogo não mágica em uma semana.')
    if genius_week or 'Golpe de Gênio' in creator.abilities:
        if quote.improvement_count or quote.enchantment_count or getattr(quote, 'innovation_count', 0):
            days = min(days, Decimal(7))
            notes.append('Golpe de Gênio: uma semana, uso limitado por aventura/mês.')
    dc = base_dc + quote.improvement_dc + quote.enchantment_dc + getattr(quote, 'innovation_dc', 0)
    permanent_pm = max(0, quote.enchantment_count-design.existing_enchantments)
    if 'Forja Devocional' in d:
        if not weapon or not quote.enchantment_count:
            raise ValueError('Forja Devocional exige uma arma e encantos selecionados para transferir.')
        if d.intersection(('Virtude do Forjador', 'Prata da Casa')) or genius_week or 'Golpe de Gênio' in creator.abilities:
            raise ValueError('Orce Forja Devocional separadamente da fabricação da arma.')
        if creator.transfer_dc is None or not isinstance(creator.transfer_dc,int) or not 0<=creator.transfer_dc<=200:
            raise ValueError('Informe a CD de fabricação da arma doadora em Distinções.')
        dc=creator.transfer_dc
        raw, days, permanent_pm = Decimal(0), Decimal(15), 0
        notes.append('Somente transferência: receptora já pronta; a doadora perde os encantos. Sem custo em tibares indicado no poder.')
    return FabricationQuote(raw, dc, days, permanent_pm=permanent_pm, notes=tuple(notes))
