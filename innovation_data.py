"""Inovações do Mestre de Armearia. Deuses de Arton, p. 110–111 (PDF 112–113)."""
INNOVATIONS = {
    'Câmara de Bala': dict(target='weapon', description='Pode ser aplicada a qualquer arma. Armazena uma bala: ao acertar um ataque corpo a corpo, pode dispará-la para causar +2d6 de dano. Conta como arma de fogo para poderes de mestre de armearia. Recarregar é ação padrão.'),
    'Cano Duplo': dict(target='weapon', description='Dois canos e carregadores independentes. Pode disparar ambos como com Disparo Rápido; se já possui o poder, não sofre sua penalidade nos testes de ataque.'),
    'Cano Serrado': dict(target='weapon', description='Contra oponente adjacente, ataques à distância causam um dado extra do mesmo tipo. Contra alvos não adjacentes, –2 nos testes de ataque.'),
    'Empunhadura de Segurança': dict(target='weapon', description='+5 para resistir a desarmar e quebrar contra a arma, cumulativo com os outros bônus da arma.'),
    'Explosiva': dict(target='ammunition', prerequisite='Pólvora de Smokestone', description='Ao acertar, criaturas adjacentes ao alvo sofrem o dano do ataque; Reflexos CD Int reduz à metade. Requer Pólvora de Smokestone.'),
    'Fragmentável': dict(target='ammunition', description='Sempre que rolar o máximo em um dado de dano da arma, role um dado extra.'),
    'Mira Calibrável': dict(target='weapon', prerequisite='Mira Telescópica', description='Ao mirar, recebe +2 em testes de ataque e na margem de ameaça até o fim do turno. Requer a melhoria Mira Telescópica.'),
    'Pólvora de Smokestone': dict(target='ammunition', description='A munição causa +1 ponto de dano por dado, exceto dados extras.'),
    'Tambor': dict(target='weapon', prerequisite='Outra inovação', description='Tambor com quatro munições. Recarregar é ação completa. Requer outra inovação qualquer.'),
    'Tanque Flamejante': dict(target='weapon', description='Muda o dano para fogo e espalha a munição em linha de 6m; o ataque é comparado à Defesa de cada criatura. Recarregar é ação completa e gasta uma bala e um fogo alquímico.'),
}


def innovation_reason(name, selected, improvements=(), *, firearm=False, ammunition=False):
    row=INNOVATIONS[name]
    if (row['target']=='ammunition') != ammunition:
        return 'Exclusiva de munições de arma de fogo.' if row['target']=='ammunition' else 'Exclusiva de armas.'
    if not ammunition and name!='Câmara de Bala' and not firearm and 'Câmara de Bala' not in selected:
        return 'Exige arma de fogo, híbrida com modo de fogo ou Câmara de Bala.'
    prerequisite=row.get('prerequisite')
    if prerequisite=='Outra inovação' and not any(n!=name for n in selected):
        return 'Exige outra inovação.'
    if prerequisite and prerequisite!='Outra inovação' and prerequisite not in (*selected,*improvements):
        return 'Exige '+prerequisite+'.'
    return ''
