# Catálogo extraído dos livros oficias
# As páginas PDF e impressas acompanham cada registro.
SPELL_DATA = [{'name': 'Abençoar Alimentos',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 178 (PDF 184)',
  'pdf_page': 184,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: alimento para 1 criatura; Duração: cena.',
  'description': 'Você purifica e abençoa uma porção de comida ou dose de bebida. Isso torna um alimento '
                 'sujo, estragado ou envenenado próprio para consumo. Além disso, se for consumido até o '
                 'final da duração, o alimento oferece 5 PV temporários ou 1 PM temporário (além de '
                 'quaisquer bônus que já oferecesse). Bônus de alimentação duram um dia e cada personagem só '
                 'pode receber um bônus de alimentação por dia.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: o alimento é purificado (não causa nenhum efeito nocivo se estava '
                            'estragado ou envenenado), mas não fornece bônus ao ser consumido.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: aumenta o número de alvos em +1.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+1 PM: muda a duração para permanente, o alvo para 1 frasco com água e adiciona '
                            'componente material (pó de prata no valor de T$ 5). Em vez do normal, cria um '
                            'frasco de água benta.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'curto',
  'target': 'alimento para 1 criatura',
  'duration': 'cena',
  'id': 'jda:abencoar-alimentos'},
 {'name': 'Acalmar Animal',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 178 (PDF 184)',
  'pdf_page': 184,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 animal; Duração: cena; Resistência: Vontade anula.',
  'description': 'O animal fica prestativo em relação a você. Ele não fica sob seu controle, mas percebe '
                 'suas palavras e ações da maneira mais favorável possível. Você recebe +10 nos testes de '
                 'Adestramento e Diplomacia que fizer contra o animal.\n'
                 'Um alvo hostil ou que esteja envolvido em um combate recebe +5 em seu teste de '
                 'resistência. Se você ou seus aliados tomarem qualquer ação hostil contra o alvo, a magia é '
                 'dissipada e ele retorna à atitude que tinha antes (ou piorada, de acordo com o mestre). Se '
                 'tratar bem o alvo, a atitude pode permanecer mesmo após o término da magia.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para médio.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o alvo para 1 monstro ou espírito com Inteligência 1 ou 2.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o número de alvos em +1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+5 PM: muda o alvo para 1 monstro ou espírito. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 animal',
  'duration': 'cena',
  'id': 'jda:acalmar-animal'},
 {'name': 'Adaga Mental',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 178 (PDF 184)',
  'pdf_page': 184,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: instantânea; Resistência: Vontade '
           'parcial.',
  'description': 'Você manifesta e dispara uma adaga imaterial contra a mente do alvo, que sofre 2d6 pontos '
                 'de dano psíquico e fica atordoado por uma rodada. Se passar no teste de resistência, sofre '
                 'apenas metade do dano e evita a condição. Uma criatura só pode ficar atordoada por esta '
                 'magia uma vez por cena.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: você lança a magia sem gesticular ou pronunciar palavras (o que permite '
                            'lançar esta magia de armadura) e a adaga se torna invisível. Se o alvo falhar '
                            'no teste de resistência, não percebe que você lançou uma magia contra ele.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a duração para um dia. Além do normal, você “finca” a adaga na '
                            'mente do alvo. Enquanto a magia durar, você sabe a direção e localização do '
                            'alvo, desde que ele esteja no mesmo mundo.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o dano em +1d6.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:adaga-mental'},
 {'name': 'Alarme',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 178 (PDF 184)',
  'pdf_page': 184,
  'stats': 'Execução: padrão; Alcance: curto; Área: esfera com 9m de raio; Duração: 1 dia.',
  'description': 'Você cria uma barreira protetora invisível que detecta qualquer criatura que tocar ou '
                 'entrar na área protegida. Ao lançar a magia, você pode escolher quais criaturas podem '
                 'entrar na área sem ativar seus efeitos. Alarme pode emitir um aviso telepático ou sonoro, '
                 'decidido quando a magia é lançada. Um aviso telepático alerta apenas você, inclusive '
                 'acordando-o se estiver dormindo, mas apenas se estiver a até 1km da área protegida. Um '
                 'aviso sonoro alerta todas as criaturas em alcance longo.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para pessoal. A área é emanada a partir de você.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: além do normal, você também percebe qualquer efeito de adivinhação que '
                            'seja usado dentro da área ou atravesse a área. Você pode fazer um teste oposto '
                            'de Misticismo contra quem usou o efeito; se passar, tem um vislumbre de seu '
                            'rosto e uma ideia aproximada de sua localização (“três dias de viagem ao '
                            'norte”, por exemplo).',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+9 PM: muda a duração para um dia ou até ser descarregada e a resistência para '
                            'Vontade anula. Quando um intruso entra na área, você pode descarregar a magia. '
                            'Se o intruso falhar na resistência, ficará paralisado por 1d4 rodadas. Além '
                            'disso, pelas próximas 24 horas você e as criaturas escolhidas ganham +10 em '
                            'testes de Sobrevivência para rastrear o intruso.',
                    'cost': 9,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'area': 'esfera com 9m de raio',
  'duration': '1 dia',
  'id': 'jda:alarme'},
 {'name': 'Aliado Animal',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 178 (PDF 184)',
  'pdf_page': 184,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 animal prestativo; Duração: 1 dia.',
  'description': 'Você cria um vínculo mental com um animal prestativo em relação a você. O Aliado Animal '
                 'obedece a você no melhor de suas capacidades, mesmo que isso arrisque a vida dele. Ele '
                 'funciona como um parceiro veterano, de um tipo a sua escolha entre ajudante, combatente, '
                 'fortão, guardião, montaria ou perseguidor.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alvo para 1 animal Minúsculo e a duração para 1 semana. Em vez do '
                            'normal, o animal se desloca no melhor de suas capacidades até um local '
                            'designado por você — em geral, para levar um item, carta ou similar. Quando o '
                            'animal chega ao destino, fica esperando até o fim da magia, permitindo apenas '
                            'que uma ou mais criaturas escolhidas por você se aproximem e peguem o que ele '
                            'estiver carregando.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+7 PM: muda o parceiro para mestre. Requer 3º círculo.',
                    'cost': 7,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+12 PM: muda o alvo para 2 animais prestativos. Cada animal funciona como um '
                            'parceiro de um tipo diferente, e você pode receber a ajuda de ambos (mas ainda '
                            'precisa seguir o limite de parceiros de acordo com o seu nível de personagem). '
                            'Requer 4º círculo.',
                    'cost': 12,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 animal prestativo',
  'duration': '1 dia',
  'id': 'jda:aliado-animal'},
 {'name': 'Alterar Destino',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 179 (PDF 185)',
  'pdf_page': 185,
  'stats': 'Execução: reação; Alcance: pessoal; Alvo: você; Duração: instantânea.',
  'description': 'Sua mente visualiza todas as possibilidades de um evento, permitindo a você escolher o '
                 'melhor curso de ação. Você pode rolar novamente um teste de resistência com um bônus de '
                 '+10 ou um inimigo deve rolar novamente um ataque contra você com uma penalidade de –10.',
  'enhancements': [],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'instantânea',
  'id': 'jda:alterar-destino'},
 {'name': 'Alterar Memória',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 179 (PDF 185)',
  'pdf_page': 185,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: instantânea; Resistência: Vontade '
           'anula.',
  'description': 'Você invade a mente do alvo e altera ou apaga suas memórias da última hora.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para pessoal e o alvo para área cone de 4,5m.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: você pode alterar ou apagar as memórias das últimas 24 horas.',
                    'cost': 5,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:alterar-memoria'},
 {'name': 'Alterar Tamanho',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 179 (PDF 185)',
  'pdf_page': 185,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 objeto; Duração: 1 dia.',
  'description': 'Esta magia aumenta ou diminui o tamanho de um item mundano em até três categorias (um '
                 'objeto Enorme vira Pequeno, por exemplo). Você também pode mudar a consistência do item, '
                 'deixando-o rígido como pedra ou flexível como seda (isso não altera sua RD ou PV, apenas '
                 'suas propriedades físicas). Se lançar a magia num objeto de uma criatura involuntária, ela '
                 'pode fazer um teste de Vontade para anulá-la.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o número de alvos em +1.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alcance para toque e o alvo para 1 criatura. Em vez do normal, o '
                            'alvo aumenta uma categoria de tamanho (seu equipamento se ajusta ao novo '
                            'tamanho). O alvo também recebe Força +2. Um alvo involuntário pode fazer um '
                            'teste de Fortitude para negar o efeito.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: muda o alcance para toque e o alvo para 1 criatura. Em vez do normal, o '
                            'alvo diminui uma categoria de tamanho (seu equipamento se ajusta ao novo '
                            'tamanho). O alvo também recebe Destreza +2. Um alvo involuntário pode fazer um '
                            'teste de Fortitude para negar o efeito. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+7 PM: muda o alcance para toque, o alvo para 1 criatura, a duração para '
                            'permanente e a resistência para Fortitude anula. Em vez do normal, se falhar na '
                            'resistência o alvo e seu equipamento têm seu tamanho mudado para Minúsculo. O '
                            'alvo tem seu valor de Força reduzido a –5 e seus deslocamentos reduzidos a 3m. '
                            'Requer 4º círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 objeto',
  'duration': '1 dia',
  'id': 'jda:alterar-tamanho'},
 {'name': 'Amarras Etéreas',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 179 (PDF 185)',
  'pdf_page': 185,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 criatura; Duração: cena; Resistência: Reflexos anula.',
  'description': 'Três laços de energia surgem e se enroscam no alvo, deixando-o agarrado. A vítima pode '
                 'tentar se livrar, gastando uma ação padrão para fazer um teste de Atletismo. Se passar, '
                 'destrói um laço, mais um laço adicional para cada 5 pontos pelos quais superou a CD. Os '
                 'laços também podem ser atacados e destruídos: cada um tem Defesa 10, 10 PV, RD 5 e '
                 'imunidade a dano mágico. Se todos os laços forem destruídos, a magia é dissipada. Por '
                 'serem feitos de energia, os laços afetam criaturas incorpóreas.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de alvos em +1.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o número de laços em um alvo a sua escolha em +1 (bônus máximo '
                            'limitado pelo círculo máximo de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: em vez do normal, cada laço é destruído automaticamente com um único '
                            'ataque bem-sucedido; porém, cada laço destruído libera um choque de energia que '
                            'causa 1d8+1 pontos de dano de essência na criatura amarrada. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'médio',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:amarras-etereas'},
 {'name': 'Amedrontar',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 179 (PDF 185)',
  'pdf_page': 185,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 animal ou humanoide; Duração: cena; Resistência: '
           'Vontade parcial.',
  'description': 'O alvo é envolvido por energias sombrias e assustadoras. Se falhar na resistência, fica '
                 'apavorado por 1 rodada, depois abalado. Se passar, fica abalado por 1d4 rodadas.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: alvos que falhem na resistência ficam apavorados por 1d4+1 rodadas, em '
                            'vez de apenas 1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alvo para 1 criatura.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: afeta todos os alvos válidos a sua escolha dentro do alcance.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 animal ou humanoide',
  'duration': 'cena',
  'id': 'jda:amedrontar'},
 {'name': 'Âncora Dimensional',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 179 (PDF 185)',
  'pdf_page': 185,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura ou objeto; Duração: cena.',
  'description': 'O alvo é envolvido por um campo de força cor de esmeralda que impede qualquer movimento '
                 'planar. Isso inclui magias de convocação (como Salto Dimensional e Teletransporte), '
                 'viagens astrais e a habilidade incorpóreo.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para médio, a área para esfera com 3m de raio e o alvo '
                            'para criaturas escolhidas.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o efeito para criar um fio de energia cor de esmeralda que prende o '
                            'alvo a um ponto no espaço dentro do alcance. O ponto precisa ser fixo, mas não '
                            'precisa de nenhum apoio ou superfície (pode simplesmente flutuar no ar). O alvo '
                            'não pode se afastar mais de 3m do ponto, nem fisicamente, nem com movimento '
                            'planar. O fio possui 20 PV e redução de dano 20 (mas pode ser dissipado por '
                            'efeitos que libertam criaturas, como o Julgamento Divino: Libertação do '
                            'paladino).',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+4 PM: como acima, mas em vez de um fio, cria uma corrente de energia, com 20 '
                            'PV e redução de dano 40.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+4 PM: muda o alvo para área de cubo de 9m, a duração para permanente e '
                            'adiciona componente material (chave de esmeralda no valor de T$ 2.000). Em vez '
                            'do normal, nenhum tipo de movimento planar pode ser feito para entrar ou sair '
                            'da área.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+9 PM: muda o alcance para médio, a área para esfera com 3m de raio e o alvo '
                            'para criaturas escolhidas. Cria um fio de energia (veja acima) que prende todos '
                            'os alvos ao centro da área.',
                    'cost': 9,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura ou objeto',
  'duration': 'cena',
  'id': 'jda:ancora-dimensional'},
 {'name': 'Animar Objetos',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 179 (PDF 185)',
  'pdf_page': 185,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: até 8 objetos Minúsculos ou Pequenos, 4 objetos Médios, '
           '2 objetos Grandes ou 1 objeto Enorme; Duração: cena.',
  'description': 'Você concede vida a objetos inanimados. Cada objeto se torna um parceiro sob seu controle. '
                 'O tipo dele é escolhido da lista de tamanho e ele não conta em seu limite de parceiros. '
                 'Com uma ação de movimento, você pode comandar mentalmente qualquer objeto animado dentro '
                 'do alcance para que auxilie você ou outra criatura. Outros usos criativos para os objetos '
                 'ficam a cargo do mestre. Objetos animados\n'
                 'são construtos com valores de Força, Destreza e PV de acordo com seu tamanho. Todos os '
                 'outros atributos são nulos, eles não têm valor de Defesa ou testes de resistência e falham '
                 'automaticamente em qualquer teste oposto. Diferente de parceiros comuns, um objeto pode '
                 'ser alvo de um ataque direto.\n'
                 'Esta magia não afeta itens mágicos, nem objetos que estejam sendo carregados por outra '
                 'criatura.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: muda a duração para permanente e adiciona componente material (prataria '
                            'no valor de T$ 1.000). Você pode ter um máximo de objetos animados igual à '
                            'metade do seu nível. Estatísticas de objetos animados Minúsculo: For –3, Des 4, '
                            '5 PV; Assassino ou Combatente Iniciante. Pequeno: For –2, Des 2, 10 PV; '
                            'Combatente ou Guardião Iniciante. Médio: For 0, Des 1, 20 PV; Combatente ou '
                            'Guardião Veterano. Grande: For 2, Des 0, 40 PV; Fortão, Guardião ou Montaria '
                            '(cavalo) Veterano. Enorme: For 4, Des –2, 60 PV; Fortão, Guardião ou Montaria '
                            '(cavalo) Mestre.',
                    'cost': 5,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'target': 'até 8 objetos Minúsculos ou Pequenos, 4 objetos Médios, 2 objetos Grandes ou 1 objeto Enorme',
  'duration': 'cena',
  'id': 'jda:animar-objetos'},
 {'name': 'Anular a Luz',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 180 (PDF 186)',
  'pdf_page': 186,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: esfera com 6m de raio; Duração: ver texto.',
  'description': 'Esta magia cria uma onda de escuridão que causa diversos efeitos. Magias de até 3º círculo '
                 'na área são dissipadas se você passar num teste de Religião contra a CD de cada uma. Seus '
                 'aliados na área são protegidos por uma aura sombria e recebem +4 na Defesa até o fim da '
                 'cena. Inimigos na área ficam enjoados por 1d4 rodadas (apenas uma vez por cena). Anular a '
                 'Luz anula Dispersar as Trevas (este efeito tem duração instantânea).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o bônus na Defesa em +1.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: muda as magias dissipadas para até 4º círculo. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+9 PM: muda as magias dissipadas para até 5º círculo. Requer 5º círculo.',
                    'cost': 9,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'esfera com 6m de raio',
  'duration': 'ver texto',
  'id': 'jda:anular-a-luz'},
 {'name': 'Aparência Perfeita',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 180 (PDF 186)',
  'pdf_page': 186,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Esta magia lhe concede um rosto idealizado, porte físico garboso, voz melodiosa e olhar '
                 'sedutor. Caso seu Carisma seja 5 ou mais, você recebe +2 neste atributo. Do contrário, ele '
                 'se tor-\n'
                 'na 5 (isso conta como um bônus). Além disso, você recebe +5 em Diplomacia e Enganação. '
                 'Quando a magia acaba, quaisquer observadores percebem a mudança e tendem a suspeitar de '
                 'você. Da mesma maneira, pessoas que o viram sob o efeito da magia sentirão que “algo está '
                 'errado” ao vê-lo em condições normais. Quando a cena acabar, você pode gastar os PM da '
                 'magia novamente como uma ação livre para mantê-la ativa. Este efeito não fornece PV ou PM '
                 'adicionais.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para toque e o alvo para 1 humanoide.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:aparencia-perfeita'},
 {'name': 'Aprisionamento',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 180 (PDF 186)',
  'pdf_page': 186,
  'stats': 'Execução: completa; Alcance: curto; Alvo: 1 criatura; Duração: permanente; Resistência: Vontade '
           'anula.',
  'description': 'Você cria uma prisão mágica para aprisionar uma criatura. Se falhar no teste de '
                 'resistência, o alvo sofre o efeito da magia; se passar, fica imune a esta magia por uma '
                 'semana. Enquanto estiver aprisionada, a criatura não precisa respirar e alimentar-se, e '
                 'não envelhece. Magias de adivinhação não conseguem localizar ou perceber o alvo. Ao lançar '
                 'a magia, você escolhe uma das seguintes formas de prisão. O componente material varia, mas '
                 'todos custam T$ 1.000.\n'
                 'Acorrentamento: o alvo é preso por correntes firmemente enraizadas no chão, que o mantém '
                 'no lugar. O alvo fica paralisado e não pode se mover ou ser movido por qualquer meio. '
                 'Componente Material: uma fina corrente de mitral.\n'
                 'Contenção Mínima: o alvo diminui para 2 cm de altura e é preso dentro de uma pedra '
                 'preciosa ou objeto semelhante. Luz passa através da pedra, permitindo que o alvo veja o '
                 'lado de fora e seja visto, mas nada mais pode passar, nem por meio de teletransporte ou '
                 'viagem planar. A pedra não pode ser quebrada enquanto o alvo estiver dentro. Componente '
                 'Material: uma pedra preciosa, como um diamante ou rubi.\n'
                 'Prisão Dimensional: o alvo é transportado para um semiplano protegido contra '
                 'teletransporte e viagens planares. Pode ser um labirinto, uma gaiola, uma torre ou '
                 'qualquer estrutura ou área confinada e pequena a sua escolha. Componente Material: uma '
                 'representação em miniatura da prisão, feita de jade.\n'
                 'Sepultamento: o alvo é sepultado nas profundezas da terra, em uma esfera mágica. Nada pode '
                 'destruir ou atravessar a esfera, nem mesmo teletranspor-\n'
                 'te ou viagens planares. Componente Material: um pequeno orbe de adamante.\n'
                 'Sono Eterno: o alvo adormece e não pode ser acordado. Componente Material: fruta preparada '
                 'com ervas soníferas raras.\n'
                 'Quando a magia é lançada, você deve especificar uma condição que fará com que ela termine '
                 'e solte o alvo. A condição pode ser tão específica ou elaborada quanto você quiser, mas '
                 'deve ser possível de acontecer. As condições podem se basear no nome, identidade ou '
                 'divindade padroeira de uma criatura, ou em ações ou qualidades observáveis, mas nunca em '
                 'estatísticas intangíveis, como nível, classe ou pontos de vida. O mestre tem a palavra '
                 'final sobre se uma condição é válida ou não.',
  'enhancements': [],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'permanente',
  'id': 'jda:aprisionamento'},
 {'name': 'Área Escorregadia',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 180 (PDF 186)',
  'pdf_page': 186,
  'stats': 'Execução: padrão; Alcance: curto; Alvo ou Área: quadrado de 3m ou 1 objeto; Duração: cena; '
           'Resistência: Reflexos (veja texto).',
  'description': 'Esta magia recobre uma superfície com uma substância gordurosa e escorregadia. Criaturas '
                 'na área devem passar na resistência para não cair. Nas rodadas seguintes, criaturas que '
                 'tentem movimentar-se pela área devem fazer testes de Acrobacia para equilíbrio (CD 10).\n'
                 'Área Escorregadia pode tornar um item escorregadio. Uma criatura segurando um objeto '
                 'afetado deve passar na resistência para não deixar o item cair cada vez que usá-lo.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta a área em +1 quadrado de 1,5m.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a CD dos testes de Acrobacia para 15.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda a CD dos testes de Acrobacia para 20.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'area': 'quadrado de 3m ou 1 objeto',
  'duration': 'cena',
  'target': '1 objeto',
  'id': 'jda:area-escorregadia'},
 {'name': 'Arma Espiritual',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 180 (PDF 186)',
  'pdf_page': 186,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Você invoca a arma preferida de sua divindade (caso sua divindade possua uma), que surge '
                 'flutuando a seu lado. Uma vez por rodada, quando você sofre um ataque corpo a corpo, pode '
                 'usar uma reação para que a arma cause automaticamente 2d6 pontos de dano do tipo da arma — '
                 'por exemplo, uma espada longa causa dano de corte — no oponente que fez o ataque. Esta '
                 'magia se dissipa se você morrer.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, a arma o protege. Você recebe +1 na Defesa.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o bônus na Defesa em +1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda a duração para sustentada. Além do normal, uma vez por rodada, você '
                            'pode gastar uma ação livre para fazer a arma acertar automaticamente um alvo '
                            'adjacente. Se a arma atacar, não poderá contra-atacar até seu próximo turno. '
                            'Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: muda o tipo do dano para essência. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+2 PM: aumenta o dano causado pela arma em +1d6 (bônus máximo limitado pelo '
                            'círculo máximo de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e6',
                    'text': '+5 PM: invoca duas armas, permitindo que você contra-ataque (ou ataque, se usar '
                            'o aprimoramento acima) duas vezes por rodada. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:arma-espiritual'},
 {'name': 'Arma Mágica',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 181 (PDF 187)',
  'pdf_page': 187,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 arma empunhada; Duração: cena.',
  'description': 'A arma é considerada mágica e fornece +1 nos testes de ataque e rolagens de dano (isso '
                 'conta como um bônus de encanto). Caso você esteja empunhando a arma, pode usar seu '
                 'atributo-chave de magias em vez do atributo original nos testes de ataque (não cumulativo '
                 'com efeitos que somam este atributo).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o bônus em +1 (bônus máximo limitado pelo círculo máximo de '
                            'magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: a arma causa +1d6 de dano de ácido, eletricidade, fogo ou frio, '
                            'escolhido quando a magia é lançada. Este aprimoramento só pode ser usado uma '
                            'vez.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: muda o bônus de dano do aprimoramento acima para +2d6.',
                    'cost': 3,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 arma empunhada',
  'duration': 'cena',
  'id': 'jda:arma-magica'},
 {'name': 'Armadura Arcana',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 181 (PDF 187)',
  'pdf_page': 187,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Esta magia cria uma película protetora invisível, mas tangível, fornecendo +5 na Defesa. '
                 'Esse bônus é cumulativo com outras magias, mas não com bônus fornecido por armaduras.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda a execução para reação. Em vez do normal, você cria um escudo '
                            'mágico que fornece +5 na Defesa contra o próximo ataque que sofrer (cumulativo '
                            'com o bônus fornecido pelo efeito básico desta magia e armaduras).',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o bônus na Defesa em +1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda a duração para um dia.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:armadura-arcana'},
 {'name': 'Armamento da Natureza',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 181 (PDF 187)',
  'pdf_page': 187,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 arma (veja texto); Duração: cena.',
  'description': 'Você fortalece uma arma mundana primitiva (sem custo em T$, como bordão, clava, funda ou '
                 'tacape), uma arma natural ou um ataque desarmado. O dano da arma aumenta em um passo e ela '
                 'é considerada mágica. Ao lançar a magia, você pode mudar o tipo de dano da arma '
                 '(escolhendo entre corte, impacto ou perfuração).',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: fornece +1 nos testes de ataque com a arma.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a execução para ação de movimento.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: aumenta o bônus nos testes de ataque em +1.',
                    'cost': 3,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+5 PM: aumenta o dano da arma em mais um passo.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 arma (veja texto)',
  'duration': 'cena',
  'id': 'jda:armamento-da-natureza'},
 {'name': 'Assassino Fantasmagórico',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 181 (PDF 187)',
  'pdf_page': 187,
  'stats': 'Execução: padrão; Alcance: longo; Alvo: 1 criatura; Duração: cena, até ser descarregada; '
           'Resistência: Vontade anula, Fortitude parcial.',
  'description': 'Usando os medos subconscientes do alvo, você cria uma imagem daquilo que ele mais teme. '
                 'Apenas a própria vítima pode ver o Assassino Fantasmagórico com nitidez; outras criaturas '
                 'presentes (incluindo o conjurador) enxergam apenas um espectro sombrio.\n'
                 'Quando você lança a magia, o espectro surge adjacente a você e a vítima faz um teste de '
                 'Vontade. Se ela passar, percebe que o espectro é uma ilusão e a magia é dissipada. Se '
                 'falhar, acredita na existência do espectro, que então flutua 18m por rodada em direção à '
                 'vítima, sempre no fim do seu turno. Ele é incorpóreo e imune a magias (exceto magias que '
                 'dissipam outras).\n'
                 'Se o espectro terminar seu turno adjacente à vítima, ela deve fazer um teste de Fortitude. '
                 'Se passar, sofre 6d6 pontos de dano de trevas (este dano não pode reduzir o alvo a menos '
                 'de 0 PV e não o deixa sangrando). Se falhar, sofre um colapso, ficando imediatamente com '
                 '–1 PV e sangrando.\n'
                 'O espectro persegue o alvo implacavelmente. Ele desaparece se o alvo ficar inconsciente ou '
                 'se afastar além de alcance longo dele, ou se for dissipado.',
  'enhancements': [],
  'range': 'longo',
  'target': '1 criatura',
  'duration': 'cena, até ser descarregada',
  'id': 'jda:assassino-fantasmagorico'},
 {'name': 'Augúrio',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 181 (PDF 187)',
  'pdf_page': 187,
  'stats': 'Execução: completa; Alcance: pessoal; Alvo: você; Duração: instantânea.',
  'description': 'Esta magia diz se uma ação que você tomará em breve — no máximo uma hora no futuro — trará '
                 'resultados bons ou ruins. O mestre rola 1d6 em segredo; com um resultado de 2 a 6, a magia '
                 'funciona e você recebe uma das seguintes respostas: “felicidade” (a ação trará bons '
                 'resultados); “miséria” (a ação trará maus resultados); “felicidade e miséria” (para ambos) '
                 'ou “nada” (para ações que não trarão resultados bons ou ruins).\n'
                 'Com um resultado 1, a magia falha e oferece o resultado “nada”. Não há como saber se esse '
                 'resultado foi dado porque a magia falhou ou não. Lançar esta magia múltiplas vezes sobre o '
                 'mesmo assunto gera sempre o primeiro resultado.\n'
                 'Por exemplo, se o grupo está prestes a entrar em uma câmara, o augúrio dirá “felicidade” '
                 'se a câmara contém um tesouro desprotegido, “miséria” se contém um monstro, “felicidade e '
                 'miséria” se houver um tesouro e um monstro ou “nada” se a câmara estiver vazia.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: muda a execução para 1 minuto. Em vez do normal, você pode consultar uma '
                            'divindade, fazendo uma pergunta sobre um evento que acontecerá até um dia no '
                            'futuro. O mestre rola a chance de falha; com um resultado de 2 a 6, você recebe '
                            'uma resposta, desde uma simples frase até uma profecia ou enigma. Em geral, '
                            'este uso sempre oferece pistas, indicando um caminho a tomar para descobrir a '
                            'resposta que se procura. Numa falha você não recebe resposta alguma. Requer 3º '
                            'círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+7 PM: muda a execução para 10 minutos e a duração para 1 minuto. Em vez do '
                            'normal, você consulta uma divindade, podendo fazer uma pergunta por rodada, '
                            'desde que ela possa ser respondida com “sim”, “não” ou “não sei” (embora '
                            'poderosos, os deuses não são oniscientes). O mestre rola a chance de falha para '
                            'cada pergunta. Em caso de falha, a resposta também é “não sei”. Requer 4º '
                            'círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: o mestre rola 1d12; a magia só falha em um resultado 1.',
                    'cost': 7,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+12 PM: o mestre rola 1d20; a magia só falha em um resultado 1.',
                    'cost': 12,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'instantânea',
  'id': 'jda:augurio'},
 {'name': 'Aura Divina',
  'tradition': 'Divina',
  'circle': 5,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 182 (PDF 188)',
  'pdf_page': 188,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: esfera com 9m de raio; Duração: cena; Resistência: '
           'Vontade parcial.',
  'description': 'Você se torna um conduíte da energia de sua divindade, emanando uma aura brilhante. Você e '
                 'aliados devotos da mesma divindade ficam imunes a encantamento e recebem +10 na Defesa e '
                 'em testes de resistência. Aliados não devotos da mesma divindade recebem +5 na Defesa e em '
                 'testes de resistência. Além disso, inimigos que entrem na área devem fazer um teste de '
                 'Vontade; em caso de falha, recebem uma condição a sua escolha entre esmorecido, debilitado '
                 'ou lento até o fim da cena. O teste deve ser refeito cada vez que a criatura entrar '
                 'novamente na área.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta os bônus na Defesa e em testes de resistência em +1.',
                    'cost': 2,
                    'min_circle': 5,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'esfera com 9m de raio',
  'duration': 'cena',
  'id': 'jda:aura-divina'},
 {'name': 'Aviso',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 182 (PDF 188)',
  'pdf_page': 188,
  'stats': 'Execução: movimento; Alcance: longo; Alvo: 1 criatura; Duração: instantânea.',
  'description': 'Envia um aviso telepático para uma criatura, mesmo que não possa vê-la nem tenha linha de '
                 'efeito. Escolha um:\n'
                 'Alerta: o alvo recebe +5 em seu próximo teste de Iniciativa e de Percepção dentro da '
                 'cena.\n'
                 'Mensagem: o alvo recebe uma mensagem sua de até 25 palavras. Vocês devem ter um idioma em '
                 'comum para o alvo poder entendê-lo.\n'
                 'Localização: o alvo sabe onde você está naquele momento. Se você mudar de posição, ele não '
                 'saberá.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o alcance em um fator de 10 (90m para 900m, 900m para 9km e '
                            'assim por diante).',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: se escolher mensagem, o alvo pode enviar uma resposta de até 25 palavras '
                            'para você até o fim de seu próximo turno.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: se escolher localização, muda a duração para cena. O alvo sabe onde você '
                            'está mesmo que você mude de posição.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: aumenta o número de alvos em +1.',
                    'cost': 3,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:aviso'},
 {'name': 'Banimento',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 182 (PDF 188)',
  'pdf_page': 188,
  'stats': 'Execução: 1d3+1 rodadas; Alcance: curto; Alvo: 1 criatura; Duração: instantânea; Resistência: '
           'Vontade parcial.',
  'description': 'Você expulsa uma criatura não nativa de Arton. Um alvo nativo de outro mundo (como muitos '
                 'espíritos), é teletransportado de volta para um lugar aleatório de seu mundo de origem. Já '
                 'um alvo morto-vivo tem sua conexão com as energias negativas rompidas, sendo reduzido a 0 '
                 'PV. Se passar na resistência, em vez dos efeitos acima, o alvo fica enjoado por 1d4 '
                 'rodadas.\n'
                 'Se você tiver um ou mais itens que se oponham ao alvo de alguma maneira, a CD do teste de '
                 'resistência aumenta em +2 por item. Por exemplo, se lançar a magia contra demônios do frio '
                 '(vulneráveis a água benta e que odeiam luz e calor) enquanto segura um frasco de água '
                 'benta e uma tocha acesa, a CD aumenta em +4. O mestre decide se determinado item é forte o '
                 'bastante contra a criatura para isso.',
  'enhancements': [{'id': 'e1',
                    'text': '+0 PM: muda a resistência para nenhum. Em vez do normal, devolve '
                            'automaticamente uma criatura conjurada (como por uma magia de convocação) para '
                            'seu plano de origem.',
                    'cost': 0,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:banimento'},
 {'name': 'Barragem Elemental de Vectorius',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 182 (PDF 188)',
  'pdf_page': 188,
  'stats': 'Execução: padrão; Alcance: longo; Efeito: 4 esferas elementais; Duração: instantânea; '
           'Resistência: Reflexos parcial.',
  'description': 'Criada pelo arquimago Vectorius, esta magia produz quatro esferas, de ácido, eletricidade, '
                 'fogo e frio, que voam até um ponto a sua escolha. Quando atingem o ponto escolhido, '
                 'explodem causando 6d6 pontos de dano de seu respectivo tipo numa área com 12m de raio. Um '
                 'teste de Reflexos reduz o dano à metade. Você pode mirar cada esfera em uma criatura ou '
                 'ponto diferente. Uma criatura ao alcance da explosão de mais de uma esfera deve fazer um '
                 'teste de resistência para cada uma. Além disso, as esferas causam os seguintes efeitos em '
                 'criaturas que falharem em seus testes de resistência:\n'
                 '• Ácido: vulnerável até o fim da cena.\n'
                 '• Elétrica: atordoado por 1 rodada (apenas uma vez por cena).\n'
                 '• Fogo: em chamas.\n'
                 '• Frio: lento até o fim da cena.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: aumenta o dano de cada esfera em +2d6.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: muda o tipo de dano de todas as esferas para essência (mas elas ainda '
                            'causam os outros efeitos como se seu tipo de dano não mudasse).',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'effect': '4 esferas elementais',
  'duration': 'instantânea',
  'id': 'jda:barragem-elemental-de-vectorius'},
 {'name': 'Bênção',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 182 (PDF 188)',
  'pdf_page': 188,
  'stats': 'Execução: padrão; Alcance: curto; Alvos: aliados; Duração: cena.',
  'description': 'Abençoa seus aliados, que recebem +1 em testes de ataque e rolagens de dano. Bênção anula '
                 'Perdição.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alvo para 1 cadáver e a duração para 1 semana. O cadáver não se '
                            'decompõe nem pode ser transformado em morto-vivo.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta os bônus em +1 (bônus máximo limitado pelo círculo máximo de '
                            'magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': 'aliados',
  'duration': 'cena',
  'id': 'jda:bencao'},
 {'name': 'Bola de Fogo',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 182 (PDF 188)',
  'pdf_page': 188,
  'stats': 'Execução: padrão; Alcance: médio; Área: esfera com 6m de raio; Duração: instantânea; '
           'Resistência: Reflexos reduz à metade.',
  'description': 'Esta famosa magia de ataque cria uma poderosa explosão, causando 6d6 pontos de dano de '
                 'fogo em todas as criaturas e objetos livres na área.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em +2d6.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a área para efeito de esfera flamejante com tamanho Médio e a '
                            'duração para cena. Em vez do normal, cria uma esfera flamejante com 1,5m de '
                            'diâmetro que causa 3d6 pontos de dano a qualquer criatura no mesmo espaço. Você '
                            'pode gastar uma ação de movimento para fazer a esfera voar 9m em qualquer '
                            'direção. Ela é imune a dano, mas pode ser apagada com água. Uma criatura só '
                            'pode sofrer dano da esfera uma vez por rodada.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: muda a duração para um dia ou até ser descarregada. Em vez do normal, '
                            'você cria uma pequena pedra flamejante, que pode detonar como uma reação, '
                            'descarregando a magia. A pedra pode ser usada como uma arma de arremesso com '
                            'alcance curto. Uma vez detonada, causa o dano da magia numa área de esfera com '
                            '6m de raio.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'médio',
  'area': 'esfera com 6m de raio',
  'duration': 'instantânea',
  'id': 'jda:bola-de-fogo'},
 {'name': 'Buraco Negro',
  'tradition': 'Universal',
  'circle': 5,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 182 (PDF 188)',
  'pdf_page': 188,
  'stats': 'Execução: completa; Alcance: longo; Efeito: buraco negro; Duração: 3 rodadas; Resistência: '
           'Fortitude parcial.',
  'description': 'Esta magia cria um vácuo capaz de sugar tudo nas proximidades. Escolha um espaço '
                 'desocupado para o buraco negro. No início de cada um de seus três turnos seguintes, todas '
                 'as criaturas a até alcance longo do buraco negro, incluindo você, devem fazer um\n'
                 'teste de Fortitude. Em caso de falha, ficam caídas e são puxadas 30m na direção do buraco. '
                 'Objetos soltos também são puxados. Criaturas podem gastar uma ação de movimento para se '
                 'segurar em algum objeto fixo, recebendo +2 em seus testes de resistência. Criaturas e '
                 'objetos que iniciem seu turno no espaço do buraco negro devem gastar uma ação de movimento '
                 'e fazer um teste de Fortitude. Se passarem, podem escapar se arrastando (deslocamento de '
                 '1,5m) para longe dele. Se falharem, perdem a ação (mas podem gastar outra para tentar '
                 'novamente). Se terminarem seu turno no espaço do buraco negro, são sugadas, desaparecendo '
                 'para sempre. Não se conhece o destino das coisas sugadas pelo buraco negro. Alguns '
                 'estudiosos sugerem que são enviadas para outros mundos — provavelmente Sombria, reino da '
                 'deusa Tenebra.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: muda o efeito para que você não seja afetado.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'effect': 'buraco negro',
  'duration': '3 rodadas',
  'id': 'jda:buraco-negro'},
 {'name': 'Caminhos da Natureza',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 183 (PDF 189)',
  'pdf_page': 189,
  'stats': 'Execução: padrão; Alcance: curto; Área: criaturas escolhidas; Duração: 1 dia.',
  'description': 'Você invoca espíritos da natureza, pedindo que eles abram seu caminho. As criaturas '
                 'afetadas recebem deslocamento +3m e ignoram penalidades por terreno difícil em terrenos '
                 'naturais.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda o alcance para pessoal e o alvo para você. Em vez do normal, você '
                            'recebe +5 em testes de Sobrevivência para se orientar.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: além do normal, a CD para rastrear os alvos em terreno natural aumenta '
                            'em +10.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o bônus de deslocamento em +3m.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'area': 'criaturas escolhidas',
  'duration': '1 dia',
  'id': 'jda:caminhos-da-natureza'},
 {'name': 'Campo Antimagia',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 183 (PDF 189)',
  'pdf_page': 189,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: sustentada.',
  'description': 'Você é cercado por uma barreira invisível com 3m de raio que o acompanha. Qualquer '
                 'habilidade mágica ou item mágico que entre na área da barreira é suprimida enquanto '
                 'estiver lá.\n'
                 'Criaturas convocadas que entrem em um Campo Antimagia desaparecem. Elas reaparecem na '
                 'mesma posição quando a duração do Campo termina — supondo que a duração da magia que as '
                 'convocou ainda não tenha terminado.\n'
                 'Criaturas mágicas ou imbuídas com magia durante sua criação não são diretamente afetadas '
                 'pelo Campo Antimagia. Entretanto, como qualquer criatura, não poderão usar magias ou '
                 'habilidades mágicas dentro dele.\n'
                 'Uma magia que dissipa outras não dissipa um Campo Antimagia, e dois Campos na mesma área '
                 'não se neutralizam. Artefatos e deuses maiores não são afetados por um Campo Antimagia.',
  'enhancements': [],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'sustentada',
  'id': 'jda:campo-antimagia'},
 {'name': 'Campo de Força',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 183 (PDF 189)',
  'pdf_page': 189,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Esta magia cria uma película protetora sobre você. Você recebe 30 pontos de vida '
                 'temporários.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda a execução para reação e a duração para instantânea. Em vez do '
                            'normal, você recebe RD 30 contra o próximo dano que sofrer.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda os PV temporários ou a RD para 50. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: muda os PV temporários ou a RD para 70. Requer 4º círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+7 PM: muda o alcance para curto, o alvo para outra criatura ou objeto Enorme '
                            'ou menor e a duração para sustentada. Em vez do normal, cria uma esfera imóvel '
                            'e tremeluzente ao redor do alvo. Nenhuma criatura, objeto ou efeito de dano '
                            'pode passar pela esfera, embora criaturas possam respirar normalmente. '
                            'Criaturas na área podem fazer um teste de Reflexos para evitar serem '
                            'aprisionadas e sempre que você se concentrar. Requer 4º círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+9 PM: como o aprimoramento acima, mas tudo dentro da esfera fica praticamente '
                            'sem peso. Uma vez por rodada, você pode gastar uma ação livre para flutuar a '
                            'esfera e seu conteúdo 9m em uma direção. Requer 4º círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:campo-de-forca'},
 {'name': 'Camuflagem Ilusória',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 183 (PDF 189)',
  'pdf_page': 189,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena.',
  'description': 'O alvo fica com sua imagem nublada, como se vista através de um líquido, recebendo os '
                 'efeitos de camuflagem leve.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: muda a duração para sustentada. A imagem do alvo fica mais distorcida, '
                            'aumentando a chance de falha da camuflagem leve para 50%.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+7 PM: muda o alcance para curto e o alvo para criaturas escolhidas. Requer 4º '
                            'círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:camuflagem-ilusoria'},
 {'name': 'Chuva de Meteoros',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 183 (PDF 189)',
  'pdf_page': 189,
  'stats': 'Execução: completa; Alcance: longo; Área: quadrado com 18m de lado; Duração: instantânea; '
           'Resistência: Reflexos parcial.',
  'description': 'Meteoros caem dos céus, devastando a área afetada. Criaturas na área sofrem 15d6 pontos de '
                 'dano de impacto, 15d6 pontos de dano de fogo e ficam caídas e presas sob os escombros '
                 '(agarradas). Uma criatura que passe no teste de resistência sofre metade do dano total e '
                 'não fica caída e agarrada. Uma criatura agarrada pode escapar gastando uma ação padrão e '
                 'passando em um teste de Atletismo. Toda a área afetada fica coberta de escombros, sendo '
                 'considerada terreno difícil, e imersa numa nuvem de poeira (camuflagem leve). Esta magia '
                 'só pode ser utilizada a céu aberto.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de meteoros que atingem a área, o que aumenta o dano em '
                            '+2d6 de impacto e +2d6 de fogo.',
                    'cost': 2,
                    'min_circle': 5,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'area': 'quadrado com 18m de lado',
  'duration': 'instantânea',
  'id': 'jda:chuva-de-meteoros'},
 {'name': 'Círculo da Justiça',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 183 (PDF 189)',
  'pdf_page': 189,
  'stats': 'Execução: completa; Alcance: curto; Área: esfera com 9m de raio; Duração: 1 dia; Resistência: '
           'Vontade parcial.',
  'description': 'Também conhecida como Lágrimas de Hyninn, esta magia é usada em tribunais e para proteger '
                 'áreas sensíveis. Criaturas na área sofrem –10 em testes de Acrobacia, Enganação, '
                 'Furtividade e Ladinagem e não podem mentir deliberadamente — mas podem tentar evitar '
                 'perguntas que normalmente responderiam com uma mentira (sendo evasivas ou cometendo '
                 'omissões, por exemplo). Uma criatura que passe na resistência tem as penalidades reduzidas '
                 'para –5 e pode mentir.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda a execução para ação padrão, o alcance para pessoal, o alvo para '
                            'você, a duração para cena e a resistência para nenhuma. Em vez do normal, '
                            'qualquer criatura ou objeto invisível em alcance curto se torna visível. Isso '
                            'não dissipa o efeito mágico; se sair do seu alcance, a criatura ou objeto '
                            'voltam a ficar invisíveis.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda a penalidade nas perícias para –10 (se passar na resistência) e –20 '
                            '(se falhar). Requer 4º círculo.',
                    'cost': 3,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: muda a duração para permanente e adiciona componente material (balança '
                            'de prata no valor de T$ 5.000).',
                    'cost': 7,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'area': 'esfera com 9m de raio',
  'duration': '1 dia',
  'id': 'jda:circulo-da-justica'},
 {'name': 'Círculo da Restauração',
  'tradition': 'Divina',
  'circle': 4,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 184 (PDF 190)',
  'pdf_page': 190,
  'stats': 'Execução: padrão; Alcance: curto; Área: esfera com 3m de raio; Duração: 5 rodadas.',
  'description': 'Você evoca um círculo de luz que emana uma energia poderosa. Qualquer criatura viva que '
                 'termine o turno dentro do círculo recupera 3d8+3 PV e 1 PM. Mortos-vivos e criaturas que '
                 'sofrem dano por luz perdem PV e PM na mesma quantidade. Uma criatura pode recuperar no '
                 'máximo 5 PM por dia com esta magia.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta a regeneração de PV em 1d8+1.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'area': 'esfera com 3m de raio',
  'duration': '5 rodadas',
  'id': 'jda:circulo-da-restauracao'},
 {'name': 'Cólera de Azgher',
  'tradition': 'Divina',
  'circle': 4,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 184 (PDF 190)',
  'pdf_page': 190,
  'stats': 'Execução: padrão; Alcance: médio; Área: esfera com 6m de raio; Duração: instantânea.',
  'description': 'Resistência: Reflexos parcial.\n'
                 'Você cria um fulgor dourado e intenso. Criaturas na área ficam cegas por 1d4 rodadas e em '
                 'chamas, e sofrem 10d6 pontos de dano de fogo (mortos-vivos sofrem 10d8 pontos de dano). '
                 'Uma criatura que passe no teste de resistência não fica cega nem em chamas e sofre metade '
                 'do dano.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em +2d6 (+2d8 contra mortos-vivos).',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta a área em +6m de raio.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: a luz purificadora do Deus-Sol dissipa todas as magias de necromancia '
                            'ativas na área. Requer 5º círculo.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'area': 'esfera com 6m de raio',
  'duration': 'instantânea',
  'id': 'jda:colera-de-azgher'},
 {'name': 'Coluna de Chamas',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 184 (PDF 190)',
  'pdf_page': 190,
  'stats': 'Execução: padrão; Alcance: longo; Área: cilindro com 3m de raio e 30m de altura; Duração: '
           'instantânea; Resistência: Reflexos reduz à metade.',
  'description': 'Um pilar de fogo sagrado desce dos céus, causando 6d6 pontos de dano de fogo mais 6d6 '
                 'pontos de dano de luz nas criaturas e objetos livres na área.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o dano de fogo em +1d6.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: aumenta o dano de luz em +1d6.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'area': 'cilindro com 3m de raio e 30m de altura',
  'duration': 'instantânea',
  'id': 'jda:coluna-de-chamas'},
 {'name': 'Comando',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 184 (PDF 190)',
  'pdf_page': 190,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 humanoide; Duração: 1 rodada; Resistência: Vontade '
           'anula.',
  'description': 'Você dá uma ordem irresistível, que o alvo deve ser capaz de ouvir (mas não\n'
                 'precisa entender). Se falhar na resistência, ele deve obedecer ao comando em seu próprio '
                 'turno da melhor maneira possível. Escolha um dos efeitos.\n'
                 'Fuja: o alvo gasta seu turno se afastando de você (usando todas as suas ações).\n'
                 'Largue: o alvo solta quaisquer itens que esteja segurando e não pode pegá-los novamente '
                 'até o início de seu próximo turno. Como esta é uma ação livre, ele ainda pode executar '
                 'outras ações (exceto pegar aquilo que largou).\n'
                 'Pare: o alvo fica pasmo (apenas uma vez por cena).\n'
                 'Senta: com uma ação livre, o alvo senta no chão (se estava pendurado ou voando, desce até '
                 'o chão). Ele pode fazer outras ações, mas não se levantar até o início de seu próximo '
                 'turno.\n'
                 'Venha: o alvo gasta seu turno se aproximando de você (usando todas as suas ações).',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alvo para 1 criatura.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta a quantidade de alvos em +1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 humanoide',
  'duration': '1 rodada',
  'id': 'jda:comando'},
 {'name': 'Compreensão',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 184 (PDF 190)',
  'pdf_page': 190,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura ou texto; Duração: cena; Resistência: Vontade '
           'anula (veja descrição).',
  'description': 'Essa magia lhe confere compreensão sobrenatural. Você pode tocar um texto e entender as '
                 'palavras mesmo que não conheça o idioma. Se tocar numa criatura inteligente, pode se '
                 'comunicar com ela mesmo que não tenham um idioma em comum. Se tocar uma criatura não '
                 'inteligente, como um animal, pode perceber seus sentimentos.\n'
                 'Você também pode gastar uma ação de movimento para ouvir os pensamentos de uma criatura '
                 'tocada (você “ouve” o que o alvo está pensando), mas um alvo involuntário tem direito a um '
                 'teste de Vontade para proteger seus pensamentos e evitar este efeito.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para curto.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alcance para curto e o alvo para criaturas escolhidas. Você pode '
                            'entender todas as criaturas afetadas, mas só pode ouvir os pensamentos de uma '
                            'por vez.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o alvo para 1 criatura. Em vez do normal, pode vasculhar os '
                            'pensamentos do alvo para extrair informações. O alvo tem direito a um teste de '
                            'Vontade para anular este efeito. O mestre decide se a criatura sabe ou não a '
                            'informação que você procura. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+5 PM: muda o alcance para pessoal e o alvo para você. Em vez do normal, você '
                            'pode falar, entender e escrever qualquer idioma. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura ou texto',
  'duration': 'cena',
  'id': 'jda:compreensao'},
 {'name': 'Comunhão Com a Natureza',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 184 (PDF 190)',
  'pdf_page': 190,
  'stats': 'Execução: completa; Alcance: pessoal; Alvo: você; Duração: 1 dia.',
  'description': 'Após uma breve união com a natureza local, você obtém informações e intuições sobre a '
                 'região em que está, numa distância equivalente a um dia de viagem. Você recebe 6d4 dados '
                 'de auxílio. Enquanto a magia durar, sempre que for realizar um teste de perícia em áreas '
                 'naturais, você pode gastar 2d4 (mais 2d4 para cada círculo de magias acima do 3º que puder '
                 'lançar) e adicionar o resultado rolado como bônus no teste. A magia termina se você ficar '
                 'sem dados.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda a execução para 1 minuto e a duração para instantânea. Em vez do '
                            'normal, você descobre 1d4+1 informações sobre os seguintes temas: terreno, '
                            'animais, vegetais, minerais, cursos d’água e presença de criaturas antinaturais '
                            'numa região natural em que você esteja. Você pode, por exemplo, descobrir a '
                            'quantidade de cavernas (terreno), se uma planta rara existe (vegetais) e se há '
                            'mortos-vivos (criaturas antinaturais) na região.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: aumenta o número de dados de auxílio em +2.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+4 PM: muda o tipo dos dados de auxílio para d6.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+8 PM: muda o tipo dos dados de auxílio para d8.',
                    'cost': 8,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': '1 dia',
  'id': 'jda:comunhao-com-a-natureza'},
 {'name': 'Conceder Milagre',
  'tradition': 'Divina',
  'circle': 4,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 184 (PDF 190)',
  'pdf_page': 190,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: permanente até ser descarregada.',
  'description': 'Você transfere um pouco de seu poder divino a outra criatura. Escolha uma magia de até 2º '
                 'círculo que você conheça; o alvo pode lançar essa magia uma vez, sem pagar o custo dela em '
                 'PM (aprimoramentos podem ser usados, mas o alvo deve gastar seus próprios PM). Você sofre '
                 'uma penalidade de –3 PM até que o alvo lance a magia.',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: muda o círculo da magia concedida para 3º e a penalidade de PM para –6.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'permanente até ser descarregada',
  'id': 'jda:conceder-milagre'},
 {'name': 'Concentração de Combate',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 185 (PDF 191)',
  'pdf_page': 191,
  'stats': 'Execução: livre; Alcance: pessoal; Alvo: você; Duração: 1 rodada.',
  'description': 'Você amplia sua percepção, antecipando movimentos dos inimigos e achando brechas em sua '
                 'defesa. Quando faz um teste de ataque, você rola dois dados e usa o melhor resultado.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda a execução para padrão e a duração para cena. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: além do normal, ao atacar você, um inimigo deve rolar dois dados e usar '
                            'o pior resultado. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+9 PM: muda a execução para padrão, o alcance para curto, o alvo para criaturas '
                            'escolhidas e a duração para cena. Requer 4º círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+14 PM: muda a execução para padrão e a duração para um dia. Além do normal, '
                            'você recebe um sexto sentido que o avisa de qualquer perigo ou ameaça. Você '
                            'fica imune às condições surpreendido e desprevenido e recebe +10 na Defesa e '
                            'Reflexos. Requer 5º círculo.',
                    'cost': 14,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': '1 rodada',
  'id': 'jda:concentracao-de-combate'},
 {'name': 'Condição',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 185 (PDF 191)',
  'pdf_page': 191,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: até 5 criaturas; Duração: cena.',
  'description': 'Pela duração da magia, você sabe a posição e status (PV atuais, se estão com uma condição '
                 'ou sob efeito de magia...) dos alvos. Depois de lançada, a distância dos alvos não importa '
                 '— a magia só deixa de detectar um alvo se ele morrer ou for para outro plano.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o número de alvos em +1.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda a duração para um dia.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': 'até 5 criaturas',
  'duration': 'cena',
  'id': 'jda:condicao'},
 {'name': 'Conjurar Elemental',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 185 (PDF 191)',
  'pdf_page': 191,
  'stats': 'Execução: completa; Alcance: médio; Efeito: parceiro elemental; Duração: sustentada.',
  'description': 'Esta magia transforma uma porção de um elemento inerte em uma criatura elemental Grande do '
                 'tipo do elemento alvo. Por exemplo, lançar esta magia numa fogueira ou tocha cria um '
                 'elemental do fogo. Você pode criar elementais do ar, água, fogo e terra com essa magia. O '
                 'elemental obedece a todos os seus comandos e pode funcio-\n'
                 'nar como um parceiro do tipo destruidor (cuja habilidade custa apenas 2 PM para ser usada) '
                 'e mais um tipo entre os indicados na lista abaixo, ambos mestres. O elemental auxilia '
                 'apenas você e não conta em seu limite de parceiros.\n'
                 'Ar: assassino, perseguidor ou vigilante. Dano de eletricidade.\n'
                 'Água: ajudante, guardião ou médico. Dano de frio.\n'
                 'Fogo: atirador, combatente ou fortão. Dano de fogo.\n'
                 'Terra: combatente, guardião ou montaria. Dano de impacto.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: o elemental muda para Enorme e recebe dois tipos de parceiro indicados '
                            'no seu elemento.',
                    'cost': 5,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: você convoca um elemental de cada tipo. Quando lança a magia, você pode '
                            'escolher se cada elemental vai auxiliar você ou um aliado no alcance. Requer 5º '
                            'círculo.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'effect': 'parceiro elemental',
  'duration': 'sustentada',
  'id': 'jda:conjurar-elemental'},
 {'name': 'Conjurar Monstro',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 185 (PDF 191)',
  'pdf_page': 191,
  'stats': 'Execução: completa; Alcance: curto; Efeito: 1 criatura conjurada; Duração: sustentada.',
  'description': 'Você conjura um monstro Pequeno que ataca seus inimigos. Você escolhe a aparência do '
                 'monstro e o tipo de dano que ele pode causar, entre corte, impacto e perfuração. No '
                 'entanto, ele não é uma criatura real, e sim um construto feito de energia. Se for '
                 'destruído, ou quando a magia acaba, desaparece com um brilho, sem deixar nada para trás. '
                 'Você só pode ter um monstro conjurado por esta magia por vez.\n'
                 'O monstro surge em um espaço desocupado a sua escolha dentro do alcance e age no início de '
                 'cada um de seus turnos, a partir da próxima rodada. O monstro tem deslocamento 9m e pode '
                 'fazer uma ação de movimento por rodada. Você pode gastar uma ação padrão para dar uma das '
                 'seguintes ordens a ele.\n'
                 'Mover: o monstro se movimenta o dobro do deslocamento nessa rodada.\n'
                 'Atacar: o monstro causa 2d4+2 pontos de dano a uma criatura adjacente.\n'
                 'Lançar Magia: o monstro pode servir como ponto de origem para uma magia lançada por você '
                 'com execução de uma ação padrão ou menor. Ele pode descarregar um Toque Chocante em um '
                 'inimigo distante, ou mesmo “cuspir”\n'
                 'uma Bola de Fogo! Você gasta PM normalmente para lançar a magia.\n'
                 'Outros usos criativos para monstros conjurados ficam a critério do mestre. O monstro não '
                 'age sem receber uma ordem.\n'
                 'Para efeitos de jogo, o monstro conjurado tem For 2, Des 3 e todos os outros atributos '
                 'nulos. Ele tem Defesa igual a sua, 20 pontos de vid e usa o seu bônus para teste de '
                 'Reflexos. Ele é imune a efeitos que pedem um teste de Fortitude ou Vontade.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: o monstro ganha deslocamento de escalada ou natação igual ao seu '
                            'deslocamento terrestre.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: aumenta o deslocamento do monstro em +3m.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+1 PM: muda o tipo de dano do ataque do monstro para ácido, fogo, frio ou '
                            'eletricidade.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: aumenta os PV do monstro em +10 para cada categoria de tamanho a partir '
                            'de Pequeno (+10 PV para Pequeno, +20 PV para Médio etc.).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+2 PM: aumenta o tamanho do monstro para Médio. Ele tem For 4, Des 3, 45 PV, '
                            'deslocamento 12m e seu ataque causa 2d6+6 pontos de dano.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e6',
                    'text': '+2 PM: o monstro ganha resistência 5 contra dois tipos de dano (por exemplo, '
                            'corte e frio).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e7',
                    'text': '+4 PM: o monstro ganha uma nova ordem: Arma de Sopro. Para dar essa ordem você '
                            'gasta 1 PM, e faz o monstro causar o dobro de seu dano de ataque em um cone de '
                            '6m a partir de si (Reflexos reduz à metade).',
                    'cost': 4,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e8',
                    'text': '+5 PM: aumenta o tamanho do monstro para Grande. Ele tem For 7, Des 2, 75 PV, '
                            'deslocamento 12m e seu ataque causa 4d6+10 pontos de dano com 3m de alcance. '
                            'Requer 2º círculo.',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e9',
                    'text': '+9 PM: o monstro ganha deslocamento de voo igual ao dobro do deslocamento.',
                    'cost': 9,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e10',
                    'text': '+9 PM: o monstro ganha imunidade contra dois tipos de dano.',
                    'cost': 9,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e11',
                    'text': '+9 PM: aumenta o tamanho do monstro para Enorme. Ele tem For 11, Des 1, 110 PV, '
                            'deslocamento 15m e seu ataque causa 4d8+15 pontos de dano com 4,5m de alcance. '
                            'Requer 4º círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e12',
                    'text': '+14 PM: aumenta o tamanho do monstro para Colossal. Ele tem For 15, Des 0, 180 '
                            'PV, deslocamento 15m e seu ataque causa 4d12+20 pontos de dano com 9m de '
                            'alcance. Requer 5º círculo.',
                    'cost': 14,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'effect': '1 criatura conjurada',
  'duration': 'sustentada',
  'id': 'jda:conjurar-monstro'},
 {'name': 'Conjurar Mortos-Vivos',
  'tradition': 'Universal',
  'circle': 2,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 186 (PDF 192)',
  'pdf_page': 192,
  'stats': 'Execução: completa; Alcance: curto; Efeito: 6 mortos-vivos; Duração: sustentada.',
  'description': 'Você conjura seis esqueletos capangas de tamanho Médio feitos de energia negativa em '
                 'espaços desocupados dentro do alcance. Você pode gastar uma ação de movimento para fazer '
                 'os mortos-vivos andarem (eles têm deslocamento 9m) ou uma ação padrão para fazê-los causar '
                 'dano a criaturas adjacentes (1d6+2 pontos de dano de trevas cada). Os esqueletos têm For '
                 '2, Des 2, Defesa 18 e todos os outros atributos nulos; eles têm 1 PV e falham '
                 'automaticamente em qualquer teste de resistência ou oposto, mas são imunes a atordoamento, '
                 'dano não letal, doença, encantamento, fadiga, frio, ilusão, paralisia, sono e veneno. Eles '
                 'desaparecem quando são reduzidos a 0 PV ou no fim da cena. Os mortos-vivos não agem sem '
                 'receber uma ordem. Usos criativos para capangas fora de combate ficam a critério do '
                 'mestre.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de mortos-vivos conjurados em +1.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: em vez de esqueletos, conjura carniçais. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: em vez de esqueletos, conjura sombras. Requer 4º círculo. Carniçal: como '
                            'esqueletos, mas têm For 3, Des 3, Defesa 27 e causam 1d8+3 pontos de dano de '
                            'trevas mais perda de 1d8 PV por veneno. Além disso, criaturas atingidas por um '
                            'carniçal devem passar num teste de Fortitude ou ficam paralisadas por 1 rodada. '
                            'Uma criatura que passe no teste de resistência fica imune à paralisia dos '
                            'carniçais por um dia. Sombra: como esqueletos, mas têm Des 4, Defesa 35, a '
                            'habilidade incorpóreo e causam 2d10 pontos de dano de trevas. Além disso, '
                            'criaturas vivas atingidas por uma sombra devem passar num teste de Fortitude ou '
                            'perdem 1d4 PM. Sombras perdem a habilidade incorpóreo quando expostas à luz do '
                            'sol.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM (Apenas Arcanos): em vez de esqueletos, conjura soterrados. Requer 3° '
                            'círculo. Soterrado: como esqueletos, mas causam dano de frio. Além disso, '
                            'criaturas atingidas por um soterrado devem passar num teste de Fortitude ou '
                            'ficam enredadas por 1 rodada. [Ameaças de Arton p. 405; a critério do mestre.]',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': True,
                    'source': 'Ameaças de Arton, p. 405 (PDF 407); a critério do mestre'},
                   {'id': 'e5',
                    'text': '+3 PM: em vez de esqueletos, conjura fúrias de Tauron. Requer 3º círculo. Fúria '
                            'de Tauron: como esqueletos, mas têm tamanho Pequeno, deslocamento de voo 12m, a '
                            'habilidade incorpóreo, Des 5, Defesa 18 e causam 1d6 pontos de dano de trevas '
                            'mais 1d6 pontos de dano de fogo. Além disso, criaturas vivas atingidas ficam '
                            'desprevenidas por 1 rodada e em chamas (Fort CD igual à da magia evita). '
                            '[Ameaças de Arton p. 405; a critério do mestre.]',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False,
                    'source': 'Ameaças de Arton, p. 405 (PDF 407); a critério do mestre'},
                   {'id': 'e6',
                    'text': '+3 PM (Apenas Devotos de Arsenal): em vez de esqueletos, conjura guerreiros '
                            'perpétuos. Requer 3º círculo. Guerreiro Perpétuo: como esqueletos, mas têm For '
                            '5, Des 4, Defesa 33, a habilidade incorpóreo e causam 3d6 pontos de dano de '
                            'impacto duas vezes por ação. [Ameaças de Arton p. 405; a critério do mestre.]',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': True,
                    'source': 'Ameaças de Arton, p. 405 (PDF 407); a critério do mestre'},
                   {'id': 'e7',
                    'text': '+3 PM (Apenas Devotos de Sszzaas): em vez de esqueletos, conjura zumbis '
                            'peçonha. Requer 3º círculo. Zumbi Peçonha: como esqueletos, mas têm For 3, Des '
                            '1, Defesa 25 e causam 1d8+1 pontos de dano de trevas mais perda de 2d6 PV por '
                            'veneno. Além disso, criaturas atingidas por um zumbi peçonha ficam atordoadas '
                            'por 1 rodada (apenas uma vez por cena) e depois fracas (Fort reduz para fracas '
                            'por 1 rodada). [Ameaças de Arton p. 405; a critério do mestre.]',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': True,
                    'source': 'Ameaças de Arton, p. 405 (PDF 407); a critério do mestre'}],
  'range': 'curto',
  'effect': '6 mortos-vivos',
  'duration': 'sustentada',
  'id': 'jda:conjurar-mortos-vivos'},
 {'name': 'Consagrar',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 186 (PDF 192)',
  'pdf_page': 192,
  'stats': 'Execução: padrão; Alcance: longo; Área: esfera com 9m de raio; Duração: 1 dia.',
  'description': 'Você enche a área com energia positiva. Pontos de vida curados por efei-\n'
                 'tos de luz são maximizados dentro da área. Isso também afeta dano causado em mortos-vivos '
                 'por esses efeitos. Por exemplo, Curar Ferimentos cura automaticamente 18 PV. Esta magia '
                 'não pode ser lançada em uma área contendo um símbolo visível dedicado a uma divindade que '
                 'não a sua. Consagrar anula Profanar.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, mortos-vivos na área sofrem –2 em testes e Defesa.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta as penalidades para mortos-vivos em –1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+9 PM: muda a execução para 1 hora, a duração para permanente e adiciona '
                            'componente material (incenso e óleos no valor de T$ 1.000). Requer 4º círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'area': 'esfera com 9m de raio',
  'duration': '1 dia',
  'id': 'jda:consagrar'},
 {'name': 'Contato Extraplanar',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 186 (PDF 192)',
  'pdf_page': 192,
  'stats': 'Execução: completa; Alcance: pessoal; Alvo: você; Duração: 1 dia.',
  'description': 'Sua mente viaja até outro plano de existência, onde entra em contato com seres '
                 'extraplanares como gênios e demônios. Você firma um contrato com uma dessas entidades para '
                 'que o auxilie durante o dia, em troca de se alimentar de seu mana. Quando a magia é '
                 'lançada, você recebe 6d6 dados de auxílio. Enquanto a magia durar, sempre que for realizar '
                 'um teste de perícia, você pode gastar 1d6 (mais 1d6 para cada círculo de magias acima do '
                 '3º que puder lançar) e adicionar o resultado como bônus no teste. No entanto, sempre que '
                 'rolar um “6” num desses dados, a entidade “suga” 1 PM de você. A magia termina se você '
                 'gastar todos os dados, ficar sem PM ou no fim do dia (o que acontecer primeiro).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de dados de auxílio em +1.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+8 PM: Muda os dados de auxílio para d12. Sempre que rolar um resultado 12 num '
                            'desses dados, a entidade “suga” 2 PM de você. Requer 4º círculo.',
                    'cost': 8,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': '1 dia',
  'id': 'jda:contato-extraplanar'},
 {'name': 'Controlar a Gravidade',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 186 (PDF 192)',
  'pdf_page': 192,
  'stats': 'Execução: padrão; Alcance: médio; Área: cubo de 12m de lado; Duração: sustentada.',
  'description': 'Você controla os efeitos da gravidade dentro da área. Ao lançar a magia, escolha um dos '
                 'efeitos abaixo. Enquanto a magia durar, você pode gastar uma ação padrão para mudar o '
                 'efeito.\n'
                 'Aumentar: no início de seus turnos, cada criatura na área deve fazer um teste de '
                 'Atletismo. Se passar, fica fatigada. Se falhar, fica fatigada e caída.\n'
                 'Inverter: inverte a gravidade da área, fazendo com que criaturas e objetos “caiam” para '
                 'cima, atingindo o topo (12m) em uma rodada. Se um obstáculo (como um teto) impedir o '
                 'movimento das criaturas, elas sofrem 1d6 pontos de dano de impacto para cada 1,5m de '
                 '“queda”. Elas podem então se levantar e caminhar no obstáculo, de cabeça para baixo. Se '
                 'não houver obstáculo, as criaturas e objetos ficam ﬂutuando no topo da área afetada, sem '
                 'poder sair do lugar. Criaturas voadoras podem se movimentar normalmente. Alguém adjacente '
                 'a algo que possa agarrar tem direito a um teste de Reﬂexos para evitar a “queda”. A '
                 'criatura deve permanecer presa pela duração da magia; caso contrário “cairá”.\n'
                 'Reduzir: criaturas ou objetos livres Médios ou menores ﬂutuam para cima e para baixo '
                 'conforme sua vontade, com deslocamento de voo 6m. Criaturas na área recebem +20 em testes '
                 'de Atletismo para escalar e saltar. Uma criatura levitando fica instável, sofrendo –2 em '
                 'testes de ataque.',
  'enhancements': [],
  'range': 'médio',
  'area': 'cubo de 12m de lado',
  'duration': 'sustentada',
  'id': 'jda:controlar-a-gravidade'},
 {'name': 'Controlar Água',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 186 (PDF 192)',
  'pdf_page': 192,
  'stats': 'Execução: padrão; Alcance: longo; Área: esfera com 30m de raio; Duração: cena; Resistência: veja '
           'texto.',
  'description': 'Você controlar os movimentos e comportamentos da água. Ao lançar a magia, escolha um dos '
                 'efeitos abaixo.\n'
                 'Congelar: toda a água mundana na área é congelada. Criaturas nadando na área ficam '
                 'imóveis; escapar exige gastar uma ação padrão e passar num teste de Atletismo ou '
                 'Acrobacia.\n'
                 'Derreter: gelo mundano na área vira água e a magia termina. A critério do mestre, isso '
                 'pode criar terreno difícil.\n'
                 'Enchente: eleva o nível da água mundana na área em até 4,5m. A sua escolha, muda área para '
                 'alvo: uma embarcação. O alvo recebe +3m em seu deslocamento pela duração do efeito.\n'
                 'Evaporar: toda a água e gelo mundano na área evaporam instantaneamente e a magia termina. '
                 'Elementais da água, plantas monstruosas e criaturas com imunidade a frio na área sofrem '
                 '10d8 pontos de dano de fogo; outras criaturas vivas recebem metade desse dano (Fortitude '
                 'reduz à metade).\n'
                 'Partir: diminui o nível de toda água mundana na área em até 4,5m. Em um corpo d’água raso, '
                 'isso abre um caminho seco, que pode ser atravessado a pé. Em um corpo d’água profundo, '
                 'cria um redemoinho que pode prender barcos (um teste de Pilotagem permite ao piloto livrar '
                 'a embarcação). Elementais da água na área ficam lentos.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em +2d8.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'area': 'esfera com 30m de raio',
  'duration': 'cena',
  'id': 'jda:controlar-agua'},
 {'name': 'Controlar Fogo',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 187 (PDF 193)',
  'pdf_page': 193,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: veja texto; Duração: cena.',
  'description': 'Você pode criar, moldar, mover ou extinguir chamas e emanações de calor. Ao lançar a '
                 'magia, escolha um dos efeitos.\n'
                 'Chamejar: o alvo é armas escolhidas. Elas causam +1d6 de dano de fogo. Também afeta armas '
                 'naturais e ataques desarmados.\n'
                 'Esquentar: o alvo é 1 objeto, que começa a esquentar. Ele sofre 1d6 pontos de dano de fogo '
                 'por rodada e causa o mesmo dano a qualquer criatura que o esteja segurando ou vestindo. A '
                 'critério do mestre, o objeto ou a criatura vestindo-o também podem ficar em chamas. Uma '
                 'criatura pode gastar uma ação completa para resfriar o objeto (jogando areia ou se jogando '
                 'numa fonte de água próxima, por exemplo) e cancelar o efeito da magia.\n'
                 'Extinguir: o alvo é 1 chama de tamanho Grande ou menor, que é apagada. Isso cria uma nuvem '
                 'de fumaça que ocupa uma esfera com 3m de raio centrada onde estava a chama. Dentro da '
                 'fumaça, criaturas têm camuflagem leve.\n'
                 'Modelar: o alvo é 1 chama de tamanho Grande ou menor. A cada rodada, você pode gastar uma '
                 'ação livre para movimentá-la 9m em qualquer direção. Se atravessar o espaço ocupado por '
                 'uma criatura, causa 2d6 pontos de dano de fogo. Uma criatura só pode receber dano dessa '
                 'maneira uma vez por rodada.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda a duração para sustentada e a resistência para Reflexos reduz à '
                            'metade. Em vez do normal, você deve escolher o seguinte efeito. Labaredas: a '
                            'cada rodada, você pode gastar uma ação de movimento para projetar uma labareda, '
                            'acertando um alvo em alcance curto a partir da chama. O alvo sofre 4d6 pontos '
                            'de dano de fogo (Reflexos reduz à metade).',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano em +1d6 (exceto do efeito chamejar).',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: muda o alvo para 1 criatura composta principalmente por fogo, lava ou '
                            'magma (como um elemental do fogo) e a resistência para Fortitude parcial. Em '
                            'vez do normal, se a criatura falhar no teste de resistência, é reduzida a 0 PV. '
                            'Se passar, sofre 5d6 pontos de dano.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'curto',
  'target': 'veja texto',
  'duration': 'cena',
  'id': 'jda:controlar-fogo'},
 {'name': 'Controlar Madeira',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 187 (PDF 193)',
  'pdf_page': 193,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 objeto de madeira Grande ou menor; Duração: cena.',
  'description': 'Você molda, retorce, altera ou repele madeira. Se lançar esta magia num objeto de uma '
                 'criatura involuntária, ela tem direito a um teste de Vontade para anulá-la. Ao lançar a '
                 'magia, escolha.\n'
                 'Fortalecer: deixa o alvo mais resistente. Armas têm seu dano aumentado em um passo. '
                 'Escudos têm seu bônus de Defesa aumentado em +2 (isso é uma melhoria no item, portanto é '
                 'cumulativa com outras magias). Esses e outros itens de madeira recebem +5 na RD e dobram '
                 'seus PV.\n'
                 'Modelar: muda a forma do alvo. Pode transformar um galho em espada, criar uma porta onde '
                 'antes havia apenas uma parede, transformar um tronco em uma caixa... Mas não pode criar '
                 'mecanismos complexos (como uma besta) ou itens consumíveis.\n'
                 'Repelir: o alvo é repelido por você. Se for uma arma, ataques feitos com ela contra você '
                 'falham automaticamente. Se for uma porta ou outro objeto que possa ser aberto, ele vai se '
                 'abrir quando você se aproximar, mesmo que esteja trancado. Um objeto que vá atingi-lo, '
                 'como uma carroça, tronco ou barril, vai desviar ou parar adjacente a você, sem lhe causar '
                 'dano. Os efeitos de regras em outros objetos de madeira ficam a cargo do mestre.\n'
                 'Retorcer: estraga o alvo. Uma porta retorcida emperra (exigindo um teste de Força contra '
                 'CD 25 para ser aberta). Armas e itens retorcidos impõem –5 em testes de perícia. Escudos '
                 'retorcidos deixam de oferecer bônus (mas ainda impõem penalidades). Um barco retorcido '
                 'começa a afundar e naufraga ao final da cena. Os efeitos de regras em outros objetos de '
                 'madeira ficam a cargo do mestre.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para pessoal, o alvo para você e a duração para um dia. '
                            'Você e seu equipamento se transformam em uma árvore de tamanho Grande. Nessa '
                            'forma, você não pode falar ou fazer ações físicas, mas consegue perceber seus '
                            'arredores normalmente. Se for atacado nessa forma, a magia é dissipada. Um '
                            'teste de Sobrevivência (CD 30) revela que você não é uma árvore verdadeira.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda o alvo para área de quadrado com 9m de lado e a duração para cena. '
                            'Em vez do normal, qualquer vegetação na área fica rígida e afiada. A área é '
                            'considerada terreno difícil e criaturas que andem nela sofrem 1d6 pontos de '
                            'dano de corte para cada 1,5m que avancem.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: muda o tamanho do alvo para Enorme ou menor. Requer 3º círculo.',
                    'cost': 7,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+12 PM: muda o tamanho do alvo para Colossal ou menor. Requer 4º círculo.',
                    'cost': 12,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'target': '1 objeto de madeira Grande ou menor',
  'duration': 'cena',
  'id': 'jda:controlar-madeira'},
 {'name': 'Controlar o Clima',
  'tradition': 'Divina',
  'circle': 4,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 187 (PDF 193)',
  'pdf_page': 193,
  'stats': 'Execução: completa; Alcance: 2km; Área: esfera com 2km de raio; Duração: 4d12 horas.',
  'description': 'Você muda o clima da área onde se encontra, podendo criar qualquer condição climática: '
                 'chuva, neve, ventos, névoas... Veja o Capítulo 6: O Mestre para os efeitos do clima.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM (Apenas Druidas): muda o raio da área para 3km e duração para 1d4 dias.',
                    'cost': 1,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': '2km',
  'area': 'esfera com 2km de raio',
  'duration': '4d12 horas',
  'id': 'jda:controlar-o-clima'},
 {'name': 'Controlar o Tempo',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 187 (PDF 193)',
  'pdf_page': 193,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: veja texto; Duração: veja texto.',
  'description': 'Aquele que controla o tempo controla o mundo. Escolha um dos efeitos a seguir.\n'
                 'Congelar o tempo: você gera uma bolha do seu tamanho na qual o tempo passa mais '
                 'lentamente. Para outras criaturas, a bolha surge e desaparece instantaneamente, mas, para '
                 'você, ela dura 3 rodadas, durante as quais você pode agir e não é afetado por efeitos '
                 'contínuos (como chamas). Porém, durante essas 3 rodadas, você e quaisquer efeitos que você '
                 'gerar não podem sair da área que você ocupava quando lançou esta magia. Efeitos de área '
                 'com duração maior que a da bolha voltam a agir normalmente quando ela termina.\n'
                 'Saltar no tempo: você e até 5 criaturas voluntárias são transportadas de 1 a 24 horas para '
                 'o futuro, desaparecendo com um brilho. Vocês ressurgem no mesmo lugar, com a mesma '
                 'velocidade e orientação; do seu ponto de vista, nenhum tempo se passou. Se\n'
                 'um objeto sólido agora ocupa o espaço de uma criatura, ela ressurge na área vazia mais '
                 'próxima.\n'
                 'Voltar no tempo: você revive os últimos segundos. Todas as ações da rodada anterior são '
                 'desfeitas (incluindo perda de PV e PM — exceto os gastos nesta magia). Tudo retorna à '
                 'posição em que estava no início do seu turno na última rodada e você é o único que sabe o '
                 'que acontecerá. Outros personagens devem repetir as mesmas ações — exceto se você fizer '
                 'algo a respeito (como avisar seus aliados sobre o que vai acontecer). Você só pode reviver '
                 'uma mesma rodada uma vez.',
  'enhancements': [],
  'range': 'curto',
  'target': 'veja texto',
  'duration': 'veja texto',
  'id': 'jda:controlar-o-tempo'},
 {'name': 'Controlar Plantas',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 188 (PDF 194)',
  'pdf_page': 194,
  'stats': 'Execução: padrão; Alcance: curto; Área: quadrado com 9m de lado; Duração: cena; Resistência: '
           'Reflexos anula.',
  'description': 'Esta magia só pode ser lançada em uma área com vegetação. As plantas se enroscam nas '
                 'criaturas da área. Aquelas que falharem na resistência ficam enredadas. Uma vítima pode se '
                 'libertar com uma ação padrão e um teste de Acrobacia ou Atletismo. Além disso, a área é '
                 'considerada terreno difícil. No início de seus turnos, a vegetação tenta enredar novamente '
                 'qualquer criatura na área, exigindo um novo teste de Reflexos.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda a área para alvo de 1 planta e a resistência para nenhuma. Em vez '
                            'do normal, você pode fazer a planta se mover como se fosse animada. Ela não '
                            'pode causar dano ou atrapalhar a concentração de um conjurador.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda a duração para instantânea. Em vez do normal, as plantas na área '
                            'diminuem, como se tivessem sido podadas. Terreno difícil muda para terreno '
                            'normal e não fornece camuflagem. Esse efeito dissipa o uso normal de Controlar '
                            'Plantas.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+1 PM: além do normal, criaturas que falhem na resistência também ficam '
                            'imóveis.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: muda o alcance para pessoal, a área para alvo (você) e a resistência '
                            'para nenhuma. Em vez do normal, você consegue se comunicar com plantas, que '
                            'começam com atitude prestativa em relação a você. Além disso, você pode fazer '
                            'testes de Diplomacia com plantas. Em geral, plantas têm uma percepção limitada '
                            'de seus arredores e normalmente fornecem respostas simplórias.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'curto',
  'area': 'quadrado com 9m de lado',
  'duration': 'cena',
  'id': 'jda:controlar-plantas'},
 {'name': 'Controlar Terra',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 188 (PDF 194)',
  'pdf_page': 194,
  'stats': 'Execução: padrão; Alcance: longo; Área: 9 cubos com 1,5m de lado; Duração: instantânea; '
           'Resistência: veja texto.',
  'description': 'Você manipula a densidade e a forma de toda terra, pedra, lama, argila ou areia na área. '
                 'Ao lançar a magia, escolha.\n'
                 'Amolecer: se afetar o teto, uma coluna ou suporte, provoca um desabamento que causa 10d6 '
                 'pontos de dano de impacto às criaturas na área (Reflexos reduz à metade). Se afetar um '
                 'piso de terra ou pedra, cria terreno difícil de areia ou argila, respectivamente.\n'
                 'Modelar: pode usar pedra ou argila para criar um ou mais objetos simples de tamanho Enorme '
                 'ou menor (sem mecanismos ou partes móveis). Por exemplo, pode transformar um tijolo em uma '
                 'maça, criar uma passagem onde antes havia apenas uma parede ou levantar uma ou mais '
                 'paredes que oferecem cobertura total (RD 8 e 50 PV para cada 3m).\n'
                 'Solidificar: transforma lama ou areia em terra ou pedra. Criaturas com os pés na '
                 'superfície ficam agarradas. Elas podem se soltar com uma ação padrão e um teste de '
                 'Acrobacia ou Atletismo.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o número de cubos de 1,5m em +2.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o alcance para pessoal, o alvo para você e a duração para um dia. '
                            'Você e seu equipamento fundem-se a uma superfície ou objeto adjacente feito de '
                            'pedra, terra, argila ou areia que possa acomodá-lo. Você pode voltar ao espaço '
                            'adjacente como uma ação livre, dissipando a magia. Enquanto mesclado, você não '
                            'pode falar ou fazer ações físicas, mas consegue perceber seus arredores '
                            'normalmente. Pequenos danos não o afetam, mas se o objeto (ou o trecho onde '
                            'você está imerso) for destruído, a magia é dissipada, você volta a um espaço '
                            'livre adjacente e sofre 10d6 pontos de dano de impacto.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'area': '9 cubos com 1,5m de lado',
  'duration': 'instantânea',
  'id': 'jda:controlar-terra'},
 {'name': 'Convocação Instantânea',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 188 (PDF 194)',
  'pdf_page': 194,
  'stats': 'Execução: padrão; Alcance: ilimitado; Alvo: 1 objeto de até 2 espaços; Duração: instantânea.',
  'description': 'Você invoca um objeto de qualquer lugar para sua mão. O item deve ter sido previamente '
                 'preparado com uma runa pessoal sua (ao custo de T$ 5).\n'
                 'A magia não funciona se o objeto estiver com outra criatura, mas você saberá onde ele está '
                 'e quem o está carregando (ou sua descrição física, caso não conheça a criatura).',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, até 1 hora após ter lançado a magia, você pode gastar '
                            'uma ação de movimento para enviar o objeto de volta para o local em que ele '
                            'estava antes.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o alvo para um baú Médio, a duração para permanente e adiciona '
                            'sacrifício de 1 PM. Em vez do normal, você esconde o baú no Éter Entre Mundos, '
                            'com até 20 espaços de equipamento. A magia faz com que qualquer objeto caiba no '
                            'baú, independentemente do seu tamanho. Uma vez escondido, você pode convocar o '
                            'baú para um espaço livre adjacente, ou de volta para o Éter, com uma ação '
                            'padrão. Componente material: baú construído com matéria-prima da melhor '
                            'qualidade (T$ 1.000). Você deve ter em mãos uma miniatura do baú, no valor de '
                            'T$ 100, para invocar o baú verdadeiro.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o número de alvos em +1.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: muda o alvo para 1 objeto de até 10 espaços. Um objeto muito grande ou '
                            'pesado para aparecer em suas mãos surge em um espaço adjacente a sua escolha.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'ilimitado',
  'target': '1 objeto de até 2 espaços',
  'duration': 'instantânea',
  'id': 'jda:convocacao-instantanea'},
 {'name': 'Crânio Voador de Vladislav',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 188 (PDF 194)',
  'pdf_page': 194,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 criatura; Duração: instantânea; Resistência: Fortitude '
           'parcial.',
  'description': 'Esta magia cria um crânio envolto em energia negativa. Quando atinge o alvo, ele causa '
                 '4d8+4 pontos de dano de trevas e se desfaz emitindo um som horrendo, deixando abalado o '
                 'alvo e todos os inimigos num raio de 3m dele (criaturas já abaladas ficam apavoradas por '
                 '1d4 rodadas). Passar no teste de resistência diminui o dano à metade e evita a condição '
                 '(as demais criaturas na área também tem direito ao teste de resistência, para evitar a '
                 'condição).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em +1d8+1.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o número de alvos em +1.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:cranio-voador-de-vladislav'},
 {'name': 'Criar Elementos',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 188 (PDF 194)',
  'pdf_page': 194,
  'stats': 'Execução: padrão; Alcance: curto; Efeito: elemento escolhido; Duração: instantânea.',
  'description': 'Você cria uma pequena porção de um elemento, a sua escolha. Os elementos criados são '
                 'reais, não mágicos. Elementos físicos devem surgir em uma superfície. Em vez de um cubo, '
                 'pode-se criar objetos simples (sem partes móveis) feitos de gelo, terra ou pedra.\n'
                 'Água: enche um recipiente de tamanho Minúsculo (como um odre) com água potável ou cria um '
                 'cubo de gelo de tamanho Minúsculo.\n'
                 'Ar: cria um vento fraco em um quadrado de 1,5m. Isso purifica a área de qualquer gás ou '
                 'fumaça, ou remove névoa por uma rodada.\n'
                 'Fogo: cria uma chama que ilumina como uma tocha. Você pode segurá-la na palma de sua mão '
                 'sem se queimar, ou fazê-la surgir em um quadrado de 1,5m. Se uma criatura ou objeto '
                 'estiver no quadrado, sofre 1d6 pontos de dano de fogo; se falhar num teste de Reflexos, '
                 'fica em chamas.\n'
                 'Terra: cria um cubo de tamanho Minúsculo feito de terra, argila ou pedra.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta a quantidade do elemento em um passo (uma categoria de tamanho '
                            'para água ou terra, +1 quadrado de 1,5m para ar e fogo).',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o efeito para alvo 1 criatura ou objeto e a resistência para '
                            'Reflexos reduz à metade. Se escolher água ou terra, você arremessa o cubo ou '
                            'objeto criado no alvo, causando 2d4 pontos de dano de impacto. Para cada '
                            'categoria de tamanho acima de Minúsculo, o dano aumenta em um passo. O cubo se '
                            'desfaz em seguida.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+1 PM: se escolheu fogo, aumenta o dano inicial de cada chama em +1d6.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'effect': 'elemento escolhido',
  'duration': 'instantânea',
  'id': 'jda:criar-elementos'},
 {'name': 'Criar Ilusão',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 189 (PDF 195)',
  'pdf_page': 195,
  'stats': 'Execução: padrão; Alcance: médio; Efeito: ilusão que se estende a até 4 cubos de 1,5m; Duração: '
           'cena; Resistência: Vontade desacredita.',
  'description': 'Esta magia cria uma ilusão visual (uma criatura, uma parede...) ou sonora (um grito de '
                 'socorro, um uivo assustador...). A magia cria apenas imagens ou sons simples, com volume '
                 'equivalente ao tom de voz normal para cada cubo de 1,5m no efeito. Não é possível criar '
                 'cheiros, texturas ou temperaturas, nem sons complexos, como uma música ou diálogo. '
                 'Criaturas e objetos atravessam uma ilusão sem sofrer dano, mas a magia pode, por exemplo, '
                 'esconder uma armadilha ou inimigo. A magia é dissipada se você sair do alcance.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda a duração para sustentada. A cada rodada você pode gastar uma ação '
                            'livre para mover a imagem ou alterar levemente o som, como aumentar o volume ou '
                            'fazer com que pareça se afastar ou se aproximar, ainda dentro dos limites do '
                            'efeito. Você pode, por exemplo, criar a ilusão de um fantasma que anda pela '
                            'sala, controlando seus movimentos. Quando você para de sustentar a magia, a '
                            'imagem ou som persistem por mais uma rodada antes de a magia se dissipar.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: aumenta o efeito da ilusão em +1 cubo de 1,5m.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+1 PM: também pode criar ilusões de imagem e sons combinados.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+1 PM: também pode criar sons complexos com volume máximo equivalente ao que '
                            'cinco pessoas podem produzir para cada cubo de 1,5m no efeito. Com uma ação '
                            'livre, você pode alterar o volume do som ou fazê-lo se aproximar ou se afastar '
                            'dentro do alcance.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+2 PM: também pode criar odores e sensações térmicas, que são percebidos a uma '
                            'distância igual ao dobro do tamanho máximo do efeito. Por exemplo, uma miragem '
                            'de uma fogueira com 4 cubos de 1,5m poderia emanar calor e cheiro de queimado a '
                            'até 12m.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e6',
                    'text': '+2 PM: muda o alcance para longo e o efeito para esfera com 30m de raio. Em vez '
                            'do normal, você cria um som muito alto, equivalente a uma multidão. Criaturas '
                            'na área lançam magias como se estivessem em uma condição ruim e a CD de testes '
                            'de Percepção para ouvir aumenta em +10. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e7',
                    'text': '+2 PM: também criar sensações táteis, como texturas; criaturas que não saibam '
                            'que é uma ilusão não conseguem atravessá-la sem passar em um teste de Vontade '
                            '(objetos ainda a atravessam). A ilusão ainda é incapaz de causar ou sofrer '
                            'dano. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e8',
                    'text': '+5 PM: muda a duração para sustentada. Além do normal, você pode gastar uma '
                            'ação livre para modificar livremente a ilusão (mas não pode acrescentar novos '
                            'aprimoramentos após lançá-la). Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'effect': 'ilusão que se estende a até 4 cubos de 1,5m',
  'duration': 'cena',
  'id': 'jda:criar-ilusao'},
 {'name': 'Cúpula de Repulsão',
  'tradition': 'Divina',
  'circle': 4,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 189 (PDF 195)',
  'pdf_page': 195,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: sustentada; Resistência: Vontade anula.',
  'description': 'Uma cúpula de energia invisível o cerca, impedindo a aproximação de certas criaturas. '
                 'Escolha um tipo de cria-\n'
                 'tura (animais, espíritos, monstros...) ou uma raça de humanoides (elfos, goblins, '
                 'minotauros..). Criaturas do grupo escolhido que tentem se aproximar a menos de 3m de você '
                 '(ou seja, que tentem ficar adjacentes a você) devem fazer um teste de Vontade. Se '
                 'falharem, não conseguem, gastam a ação e só podem tentar novamente na rodada seguinte. '
                 'Isso impede ataques corpo a corpo, mas não ataques ou outros efeitos à distância. Se você '
                 'tentar se aproximar além do limite de 3m, rompe a cúpula e a magia é dissipada.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: a cúpula impede criaturas de se aproximarem a menos de 4,5m de você (ou '
                            'seja, deve haver dois quadrados entre você e as criaturas).',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: além do normal, criaturas afetadas também precisam fazer o teste de '
                            'resistência se fizerem um ataque ou efeito à distância você. Se falharem, o '
                            'efeito é desviado pela cúpula. Requer 5º círculo.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'sustentada',
  'id': 'jda:cupula-de-repulsao'},
 {'name': 'Curar Ferimentos',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 189 (PDF 195)',
  'pdf_page': 195,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: instantânea.',
  'description': 'Você canaliza luz que recupera 2d8+2 pontos de vida na criatura tocada.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda o alvo para 1 morto-vivo. Em vez do normal, causa 1d8 pontos de '
                            'dano de luz (Vontade reduz à metade).',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: aumenta a cura em +1d8+1.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: também remove uma condição de fadiga do alvo.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: muda o alcance para curto.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+5 PM: muda o alcance para curto e o alvo para criaturas escolhidas.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:curar-ferimentos'},
 {'name': 'Deflagração de Mana',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 189 (PDF 195)',
  'pdf_page': 195,
  'stats': 'Execução: completa; Alcance: pessoal; Área: esfera com 15m de raio; Duração: instantânea; '
           'Resistência: Fortitude parcial.',
  'description': 'Após concentrar seu mana, você emana energia, como uma estrela em plena terra. Todas as '
                 'criaturas na área sofrem 150 pontos de dano de essência e todos os itens mágicos (exceto '
                 'artefatos) tornam-se mundanos. Você não é afetado pela magia. Alvos que passem no teste de '
                 'Fortitude sofrem metade do dano e seus itens mágicos voltam a funcionar após um dia.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o dano em 10.',
                    'cost': 1,
                    'min_circle': 5,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: afeta apenas criaturas a sua escolha.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'esfera com 15m de raio',
  'duration': 'instantânea',
  'id': 'jda:deflagracao-de-mana'},
 {'name': 'Desejo',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 190 (PDF 196)',
  'pdf_page': 196,
  'stats': 'Execução: completa; Alcance: veja texto; Alvo: veja texto; Duração: veja texto; Resistência: '
           'veja texto.',
  'description': 'Esta é a mais poderosa das magias arcanas, permitindo alterar a realidade a seu '
                 'bel-prazer. Você pode:\n'
                 '• Dissipar os efeitos de qualquer magia de 4º círculo ou menor.\n'
                 '• Transportar até 10 criaturas voluntárias em alcance longo para qualquer outro local, em '
                 'qualquer plano.\n'
                 '• Desfazer um acontecimento recente. A magia permite que um teste realizado por uma '
                 'criatura em alcance longo na última rodada seja realizado novamente. Por exemplo, se um '
                 'aliado morreu na última rodada devido ao ataque de um inimigo, você pode obrigar o inimigo '
                 'a refazer esse ataque.\n'
                 'Você pode desejar por algo ainda mais poderoso. Nesse caso, a magia requer o sacrifício de '
                 '2 PM e pode fazer coisas como:\n'
                 '• Criar um item mundano de até T$ 30.000.\n'
                 '• Duplicar os efeitos de qualquer magia de até 4º círculo. Caso a magia precise de um '
                 'componente material para ser lançada, ainda é necessário providenciar o componente.\n'
                 '• Aumentar um atributo de uma criatura em +1. Cada atributo só pode ser aumentado uma vez '
                 'com Desejo.\n'
                 'Desejo pode gerar efeitos ainda mais poderosos, mas cuidado! Desejar a fortuna de um rei '
                 'pode transportá-lo para a sala de tesouro real, onde você poderá ser preso ou morto; '
                 'desejar ser imortal pode transformá-lo em morto-vivo, e assim por diante. Qualquer efeito '
                 'que não se encaixe na lista acima deve ser decidido pelo mestre.',
  'enhancements': [],
  'range': 'veja texto',
  'target': 'veja texto',
  'duration': 'veja texto',
  'id': 'jda:desejo'},
 {'name': 'Desespero Esmagador',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 190 (PDF 196)',
  'pdf_page': 196,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: cone de 6m; Duração: cena; Resistência: Vontade '
           'parcial.',
  'description': 'Humanoides na área são acometidos de grande tristeza, adquirindo as condições fraco e '
                 'frustrado. Se passarem na resistência, adquirem essas condições por uma rodada.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: em vez do normal, as condições adquiridas são debilitado e esmorecido.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: em vez do normal, afeta qualquer tipo de criatura.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: além do normal, criaturas que falhem na resistência ficam aos prantos '
                            '(pasmos) por 1 rodada (apenas uma vez por cena). Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'cone de 6m',
  'duration': 'cena',
  'id': 'jda:desespero-esmagador'},
 {'name': 'Desintegrar',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 190 (PDF 196)',
  'pdf_page': 196,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 criatura ou objeto; Duração: instantânea; Resistência: '
           'Fortitude parcial.',
  'description': 'Você dispara um raio fino e esverdeado que causa 10d12 pontos de dano de essência. Se o '
                 'alvo passar no teste de resistência, em vez disso sofre 2d12 pontos de dano.\n'
                 'Independentemente do resultado do teste de Fortitude, se os PV do alvo forem reduzidos a 0 '
                 'ou menos, ele será completamente desintegrado, restando apenas pó.',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: aumenta o dano total em +2d12 e o dano mínimo em +1d12.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'target': '1 criatura ou objeto',
  'duration': 'instantânea',
  'id': 'jda:desintegrar'},
 {'name': 'Despedaçar',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 190 (PDF 196)',
  'pdf_page': 196,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura ou objeto mundano Pequeno; Duração: '
           'instantânea; Resistência: Fortitude parcial.',
  'description': 'Esta magia emite um som alto e agudo. O alvo sofre 1d8+2 pontos de dano de impacto (ou o '
                 'dobro disso e ignora RD se for um construto ou objeto mundano) e fica atordoado por uma '
                 'rodada (apenas uma vez por cena). Um teste de Fortitude reduz o dano à metade e evita o '
                 'atordoamento.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em +1d8+2.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alvo para objeto mundano Médio. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda o alvo para objeto mundano Grande. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+9 PM: muda o alvo para objeto mundano Enorme. Requer 4º círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+14 PM: muda o alvo para objeto mundano Colossal. Requer 5º círculo.',
                    'cost': 14,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e6',
                    'text': '+5 PM: muda o alcance para pessoal e a área para esfera com 6m de raio. Todas '
                            'as criaturas e objetos mundanos na área são afetados.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura ou objeto mundano Pequeno',
  'duration': 'instantânea',
  'id': 'jda:despedacar'},
 {'name': 'Despertar Consciência',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 190 (PDF 196)',
  'pdf_page': 196,
  'stats': 'Execução: completa; Alcance: toque; Alvo: 1 animal ou planta; Duração: 1 dia.',
  'description': 'Você desperta a consciência de um animal ou planta. O alvo se torna um parceiro veterano '
                 'de um tipo a sua escolha entre ajudante, combatente, fortão, guardião, médico, perseguidor '
                 'ou vigilante. Se usar esta magia em um parceiro que já possua, o nível de poder de um de '
                 'seus tipos aumenta em um passo (iniciante para veterano, veterano para mestre). Se já for '
                 'um parceiro mestre, recebe o bônus de outro tipo de parceiro iniciante (entre as escolhas '
                 'acima). O alvo se torna uma criatura racional, com Inteligência –1, e pode falar.',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: muda o alvo para 1 escultura mundana inanimada. Além do normal, o alvo '
                            'tem as mesmas características de um construto.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: muda a duração para permanente e adiciona penalidade de –3 PM.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 animal ou planta',
  'duration': '1 dia',
  'id': 'jda:despertar-consciencia'},
 {'name': 'Detectar Ameaças',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 190 (PDF 196)',
  'pdf_page': 196,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: esfera com 18m de raio; Duração: cena, até ser '
           'descarregada.',
  'description': 'Você recebe uma intuição aguçada sobre perigos ao seu redor. Quando uma criatura hostil ou '
                 'armadilha entra na área do efeito, você faz um teste de Percepção (CD determinada pelo '
                 'mestre de acordo com a situação). Se passar, sabe a origem (criatura ou armadilha), '
                 'direção e distância do perigo. Se falhar, sabe apenas que o perigo existe.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: você descobre também a raça ou espécie e o poder da criatura detectada '
                            '(determinado pela aura dela). Criaturas de 1º a 6º nível ou ND geram aura '
                            'tênue, criaturas de 7º a 12º nível ou ND geram aura moderada e criaturas de 13º '
                            'ao 20º nível ou ND geram aura poderosa. Criaturas acima do 20º nível ou ND '
                            'geram aura avassaladora.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: além do normal, você não fica surpreso desprevenido contra perigos '
                            'detectados com sucesso e recebe +5 em testes de resistência contra armadilhas. '
                            'Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'esfera com 18m de raio',
  'duration': 'cena, até ser descarregada',
  'id': 'jda:detectar-ameacas'},
 {'name': 'Dificultar Detecção',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 190 (PDF 196)',
  'pdf_page': 196,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura ou objeto; Duração: 1 dia.',
  'description': 'Esta magia oculta a presença do alvo contra qualquer meio mágico de detecção, inclusive '
                 'detectar magia. Um conjurador que lance uma magia de adivinhação para detectar a presença '
                 'ou localização do alvo deve fazer um teste de Vontade. Se falhar, a magia não funciona, '
                 'mas os PM são gastos mesmo assim. Se for lançada sobre uma criatura, Dificultar Detecção '
                 'protege tanto a criatura quanto seu equipamento.',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: muda o alvo para área de cubo de 9m. Qualquer criatura ou objeto na área '
                            'recebe o efeito da magia enquanto estiver dentro dela.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: muda a duração para 1 semana.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura ou objeto',
  'duration': '1 dia',
  'id': 'jda:dificultar-deteccao'},
 {'name': 'Disfarce Ilusório',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 191 (PDF 197)',
  'pdf_page': 197,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena; Resistência: Vontade desacredita.',
  'description': 'Você muda a aparência do alvo, incluindo seu equipamento. Isso inclui altura, peso, tom de '
                 'pele, cor de cabelo, timbre de voz etc. O alvo recebe +10 em testes de Enganação para '
                 'disfarce. O alvo não recebe novas habilidades (você pode ficar parecido com outra raça, '
                 'mas não ganhará as habilidades dela), nem modifica o equipamento (uma espada longa '
                 'disfarçada de bordão continua funcionando e causando dano como uma espada).',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda o alcance para toque, o alvo para 1 criatura e a duração para 1 '
                            'semana. Em vez do normal, você faz uma pequena alteração na aparência do alvo, '
                            'como deixar o nariz vermelho ou fazer brotar um gerânio no alto da cabeça. A '
                            'mudança é inofensiva, mas persistente — se a flor for arrancada, por exemplo, '
                            'outra nascerá no local.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o alcance para curto e o alvo para 1 objeto. Você pode, por '
                            'exemplo, transformar pedaços de ferro em moedas de ouro. Você recebe +10 em '
                            'testes de Enganação para falsificação.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o alcance para curto e o alvo para 1 criatura. Uma criatura '
                            'involuntária pode anular o efeito com um teste de Vontade.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: a ilusão inclui odores e sensações. Isso muda o bônus em testes de '
                            'Enganação para disfarce para +20.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+3 PM: muda o alcance para curto e o alvo para criaturas escolhidas. Cada '
                            'criatura pode ter uma aparência diferente. Criaturas involuntárias podem anular '
                            'o efeito com um teste de Vontade. Requer 2º círculo.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:disfarce-ilusorio'},
 {'name': 'Dispersar as Trevas',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 191 (PDF 197)',
  'pdf_page': 197,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: esfera com 6m de raio; Duração: veja texto.',
  'description': 'Esta magia cria um forte brilho (multicolorido ou de uma cor que remeta a sua divindade) '
                 'que causa diversos efeitos. Todas as magias de 3º círculo ou menor ativas na área são '
                 'dissipadas se você passar num teste de Religião contra a CD de cada magia. Seus aliados na '
                 'área recebem +4 em testes de resistência e redução de trevas 10 até o fim da cena, '
                 'protegidos por uma aura sutil da mesma cor. Inimigos na área ficam cegos por 1d4 rodadas '
                 '(apenas uma vez por cena). Dispersar as Trevas anula Anular a Luz (este efeito tem duração '
                 'instantânea).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o bônus nas resistências em +1.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: muda o alcance para curto, a área para alvo 1 criatura e a duração para '
                            'cena. O alvo fica imune a efeitos de trevas.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+4 PM: muda o círculo máximo de magias dissipadas para 4º. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+9 PM: muda o círculo máximo de magias dissipadas para 5º. Requer 5º círculo.',
                    'cost': 9,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'esfera com 6m de raio',
  'duration': 'veja texto',
  'id': 'jda:dispersar-as-trevas'},
 {'name': 'Dissipar Magia',
  'tradition': 'Universal',
  'circle': 2,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 191 (PDF 197)',
  'pdf_page': 197,
  'stats': 'Execução: padrão; Alcance: médio; Alvo ou Área: 1 criatura ou 1 objeto mágico ou esfera com 3m '
           'de raio; Duração: instantânea.',
  'description': 'Você dissipa outras magias que estejam ativas, como se sua duração tivesse acabado. Note '
                 'que efeitos de magias instantâneas não podem ser dissipados (não se pode dissipar uma Bola '
                 'de Fogo ou Relâmpago depois que já causaram dano...). Se lançar essa magia em uma criatura '
                 'ou área, faça um teste de Misticismo; você dissipa as magias com CD igual ou menor que o '
                 'resultado do teste. Se lançada contra um item mágico, o transforma em um item mundano por '
                 '1d6 rodadas (Vontade anula).',
  'enhancements': [{'id': 'e1',
                    'text': '+12 PM: muda a área para esfera com 9m de raio. Em vez do normal, cria um '
                            'efeito de disjunção. Todas as magias na área são automaticamente dissipadas e '
                            'todos os itens mágicos na área, exceto aqueles que você estiver carregando, '
                            'viram itens mundanos por uma cena (com direito a um teste de Vontade para '
                            'evitar esse efeito). Requer 5º círculo.',
                    'cost': 12,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'médio',
  'area': '1 criatura ou 1 objeto mágico ou esfera com 3m de raio',
  'duration': 'instantânea',
  'target': '1 criatura',
  'id': 'jda:dissipar-magia'},
 {'name': 'Duplicata Ilusória',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 191 (PDF 197)',
  'pdf_page': 197,
  'stats': 'Execução: padrão; Alcance: médio; Efeito: cópia ilusória; Duração: cena.',
  'description': 'Você cria uma cópia ilusória semirreal de... você mesmo! Ela é idêntica em aparência, som '
                 'e cheiro, mas é intangível. A cada turno, você escolhe se verá e ouvirá através da '
                 'duplicata ou de seu corpo original. A cópia reproduz todas as suas ações, incluindo fala. '
                 'Qualquer magia com alcance de toque ou maior que você lançar pode se originar da '
                 'duplicata, em vez do seu corpo original. As magias afetam outros alvos normalmente, com a '
                 'única diferença de se originarem da cópia, em vez de você. Se quiser que a duplicata faça '
                 'algo diferente de você, você deve gastar uma ação de movimento. Qualquer criatura que '
                 'interagir com a cópia tem direito a um teste de Vontade para perceber que é uma ilusão. As '
                 'magias que se originam dela, no entanto, são reais. A cópia desaparece se sair do alcance.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: cria uma cópia adicional.',
                    'cost': 3,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'effect': 'cópia ilusória',
  'duration': 'cena',
  'id': 'jda:duplicata-ilusoria'},
 {'name': 'Enfeitiçar',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 191 (PDF 197)',
  'pdf_page': 197,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 humanoide; Duração: cena; Resistência: Vontade anula.',
  'description': 'O alvo fica enfeitiçado (veja a página 394). Um alvo hostil ou que esteja envolvido em um '
                 'combate recebe +5 em seu teste de resistência. Se você ou seus aliados tomarem qualquer '
                 'ação hostil contra o alvo, a magia é dissipada e o alvo retorna à atitude que tinha antes '
                 '(ou piorada, de acordo com o mestre).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: em vez do normal, você sugere uma ação para o alvo e ele obedece. A '
                            'sugestão deve ser feita de modo que pareça aceitável, a critério do mestre. '
                            'Pedir ao alvo que pule de um precipício, por exemplo, dissipa a magia. Já '
                            'sugerir a um guarda que descanse um pouco, de modo que você e seus aliados '
                            'passem por ele, é aceitável. Quando o alvo executa a ação, a magia termina. '
                            'Você pode determinar uma condição específica para a sugestão: por exemplo, que '
                            'um rico mercador doe suas moedas para o primeiro mendigo que encontrar.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: muda o alvo para 1 espírito ou monstro. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: afeta todos os alvos dentro do alcance.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 humanoide',
  'duration': 'cena',
  'id': 'jda:enfeiticar'},
 {'name': 'Engenho de Mana',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 192 (PDF 198)',
  'pdf_page': 198,
  'stats': 'Execução: padrão; Alcance: médio; Efeito: disco de energia com 1,5m de diâmetro; Duração: '
           'sustentada.',
  'description': 'Você cria um disco de energia que lembra uma roda de engenho e flutua no ponto em que foi '
                 'conjurado. O disco é imune a dano, não pode ser movido e faz uma contramágica automática '
                 'contra qualquer magia lançada em alcance médio dele (exceto as suas), usando seu teste de '
                 'Misticismo. Caso vença o teste, o engenho não só anula a magia como absorve os PM usados '
                 'para lançá-la, acumulando PM temporários. No seu turno, se estiver ao alcance do disco, '
                 'você pode gastar PM nele para lançar magias.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: em vez de flutuar no ponto em que foi conjurado, o disco flutua atrás de '
                            'você, mantendo-se sempre adjacente.',
                    'cost': 1,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: muda a duração para um dia.',
                    'cost': 4,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'effect': 'disco de energia com 1,5m de diâmetro',
  'duration': 'sustentada',
  'id': 'jda:engenho-de-mana'},
 {'name': 'Enxame de Pestes',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 192 (PDF 198)',
  'pdf_page': 198,
  'stats': 'Execução: completa; Alcance: médio; Efeito: 1 enxame Médio (quadrado de 1,5m); Duração: '
           'sustentada.',
  'description': 'Resistência: Fortitude reduz à metade.\n'
                 'Você conjura um enxame de criaturas a sua escolha, como besouros, gafanhotos, ratos, '
                 'morcegos ou serpentes. O enxame pode passar pelo espaço de outras criaturas e não impede '
                 'que outras criaturas entrem no espaço dele. No final de seus turnos, o enxame causa 2d12 '
                 'pontos de dano de corte a qualquer criatura em seu espaço (Fortitude reduz à metade). Você '
                 'pode gastar uma ação de movimento para mover o enxame 12m.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em +1d12.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda a resistência para Reflexos reduz à metade e o enxame para '
                            'criaturas maiores, como gatos, guaxinins, compsognatos ou kobolds. Ele causa '
                            '3d12 pontos de dano (a sua escolha entre corte, impacto ou perfuração). O resto '
                            'da magia segue normal.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: aumenta o número de enxames em +1. Eles não podem ocupar o mesmo espaço. '
                            'Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+7 PM: muda a resistência para Reflexos reduz à metade e o enxame para '
                            'criaturas elementais. Ele causa 5d12 pontos do dano (a sua escolha entre ácido, '
                            'eletricidade, fogo ou frio). O resto da magia segue normal. Requer 4º círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'effect': '1 enxame Médio (quadrado de 1,5m)',
  'duration': 'sustentada',
  'id': 'jda:enxame-de-pestes'},
 {'name': 'Enxame Rubro de Ichabod',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 192 (PDF 198)',
  'pdf_page': 198,
  'stats': 'Execução: padrão; Alcance: médio; Efeito: 1 enxame Grande (quadrado de 3m); Duração: sustentada; '
           'Resistência: Reflexos reduz à metade.',
  'description': 'Você conjura um enxame de pequenas criaturas da Tormenta. O enxame pode passar pelo espaço '
                 'de outras criaturas e não impede que outras criaturas entrem no espaço dele. No final de '
                 'cada um de seus turnos, o enxame causa 4d12 pontos de dano de ácido a qualquer criatura em '
                 'seu espaço (Reflexos reduz à metade). Você pode gastar uma ação de movimento para mover o '
                 'enxame com deslocamento de 12m.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, uma criatura que falhe no teste de Reflexos fica '
                            'agarrada (o enxame escala e cobre o corpo dela). A criatura pode gastar uma '
                            'ação padrão e fazer um teste de Acrobacia ou Atletismo para escapar. Se você '
                            'mover o enxame, a criatura fica livre.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano em +1d12.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o dano para trevas.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: o enxame vira Enorme (quadrado de 6m de lado).',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+3 PM: o enxame ganha deslocamento de voo 18m e passa a ocupar um cubo ao invés '
                            'de um quadrado.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e6',
                    'text': '+4 PM: o enxame inclui parasitas que explodem e criam novos enxames. No início '
                            'de cada um de seus turnos, role 1d6. Em um resultado 5 ou 6, um novo enxame '
                            'surge adjacente a um já existente à sua escolha. Você pode mover todos os '
                            'enxames com uma única ação de movimento, mas eles não podem ocupar o mesmo '
                            'espaço. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'effect': '1 enxame Grande (quadrado de 3m)',
  'duration': 'sustentada',
  'id': 'jda:enxame-rubro-de-ichabod'},
 {'name': 'Erupção Glacial',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 192 (PDF 198)',
  'pdf_page': 198,
  'stats': 'Execução: padrão; Alcance: médio; Área: quadrado de 6m de lado; Duração: instantânea; '
           'Resistência: Reflexos parcial.',
  'description': 'Estacas de gelo irrompem do chão. Criaturas na área sofrem 4d6 de dano de corte, 4d6 de '
                 'dano de frio e ficam caídas. Passar no teste de Reflexos evita o dano de corte e a queda. '
                 'As estacas duram pela cena, o que torna a área afetada terreno difícil, e concedem '
                 'cobertura leve para criaturas dentro da área ou atrás dela. As estacas são destruídas caso '
                 'sofram qualquer quantidade de dano por fogo mágico.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: aumenta o dano de frio em +2d6 e o dano de corte em +2d6.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: muda a área para cilindro com 6m de raio e 6m de altura e a duração para '
                            'sustentada. Em vez do normal, a magia cria uma tempestade de granizo que causa '
                            '3d6 pontos de dano de impacto e 3d6 pontos de dano de frio em todas as '
                            'criaturas na área (sem teste de resistência). A tempestade fornece camuflagem '
                            'leve às criaturas dentro dela e deixa o piso escorregadio. Piso escorregadio '
                            'conta como terreno difícil e obriga criaturas na área a fazer testes de '
                            'Acrobacia para equilíbrio (veja o Capítulo 2). Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'médio',
  'area': 'quadrado de 6m de lado',
  'duration': 'instantânea',
  'id': 'jda:erupcao-glacial'},
 {'name': 'Escudo da Fé',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 192 (PDF 198)',
  'pdf_page': 198,
  'stats': 'Execução: reação; Alcance: curto; Alvo: 1 criatura; Duração: 1 turno.',
  'description': 'Um escudo místico se manifesta momentaneamente para bloquear um golpe. O alvo recebe +2 na '
                 'Defesa.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda a execução para ação padrão, o alcance para toque e a duração para '
                            'cena.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: também fornece ao alvo camuflagem leve contra ataques à distância.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o bônus na Defesa em +1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: muda a execução para ação padrão, o alcance para toque e a duração para '
                            'cena. A magia cria uma conexão mística entre você e o alvo. Além do efeito '
                            'normal, o alvo sofre metade do dano por ataques e efeitos; a outra metade do '
                            'dano é transferida a você. Se o alvo sair de alcance curto de você, a magia é '
                            'dissipada. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+3 PM: muda a duração para um dia. Requer 2º círculo.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': '1 turno',
  'id': 'jda:escudo-da-fe'},
 {'name': 'Esculpir Sons',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 192 (PDF 198)',
  'pdf_page': 198,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 criatura ou objeto; Duração: cena; Resistência: '
           'Vontade anula.',
  'description': 'Esta magia altera os sons emitidos pelo alvo. Ela não é capaz de criar sons, mas pode '
                 'omiti-los (como fazer uma carroça ficar silenciosa) ou transformá-los (como fazer uma '
                 'pessoa ficar com voz de passarinho). Você não pode criar sons que não conhece (não pode '
                 'fazer uma criatura falar num idioma que não conheça). Uma vez que escolha a alteração, ela '
                 'não pode ser mudada. Um conjurador que tenha a voz modificada drasticamente não poderá '
                 'lançar magias.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de alvos em +1. Todas as criaturas e objetos devem ser '
                            'afetadas da mesma forma.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'target': '1 criatura ou objeto',
  'duration': 'cena',
  'id': 'jda:esculpir-sons'},
 {'name': 'Escuridão',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 193 (PDF 199)',
  'pdf_page': 199,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 objeto; Duração: cena; Resistência: Vontade anula '
           '(veja texto).',
  'description': 'O alvo emana sombras em uma área com 6m de raio. Criaturas dentro da área recebem '
                 'camuflagem leve por escuridão leve. As sombras não podem ser iluminadas por nenhuma fonte '
                 'de luz natural. O objeto pode ser guardado (em um bolso, por exemplo) para interromper a '
                 'escuridão, que voltará a funcionar caso o objeto seja revelado. Se lançar a magia num '
                 'objeto de uma criatura involuntária, ela tem direito a um teste de Vontade para anulá-la. '
                 'Escuridão anula Luz.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta a área da escuridão em +1,5m de raio.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o efeito para fornecer camuflagem total por escuridão total. As '
                            'sombras bloqueiam a visão na área e através dela.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o alvo para 1 criatura e a resistência para Fortitude parcial. Você '
                            'lança a magia nos olhos do alvo, que fica cego pela cena. Se passar na '
                            'resistência, fica cego por 1 rodada. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: muda a duração para um dia.',
                    'cost': 3,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+5 PM: muda o alcance para pessoal e o alvo para você. Em vez do normal, você é '
                            'coberto por sombras, recebendo +10 em testes de Furtividade e camuflagem leve. '
                            'Requer 2º círculo.',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 objeto',
  'duration': 'cena',
  'id': 'jda:escuridao'},
 {'name': 'Explosão Caleidoscópica',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 193 (PDF 199)',
  'pdf_page': 199,
  'stats': 'Execução: padrão; Alcance: curto; Área: esfera com 6m de raio; Duração: instantânea.',
  'description': 'Resistência: Fortitude parcial.\n'
                 'Esta magia cria uma forte explosão de luzes estroboscópicas e sons cacofônicos que '
                 'desorientam as criaturas atingidas. O efeito que cada criatura sofre depende do nível ou '
                 'ND dela.\n'
                 'Nível ou ND 4 ou menor: se falhar no teste de resistência, fica inconsciente. Se passar, '
                 'fica atordoada por 1d4 rodadas e enjoada pelo resto da cena.\n'
                 'Nível ou ND entre 5 e 9: se falhar no teste de resistência, fica atordoada por 1d4 rodadas '
                 'e enjoada pelo resto da cena.\n'
                 'Se passar, fica atordoada por 1 rodada e enjoada por 1d4 rodadas.\n'
                 'Nível ou ND 10 ou maior: se falhar no teste de resistência, fica atordoada por 1 rodada e '
                 'enjoada por 1d4 rodadas. Se passar, fica desprevenida e enjoada por 1 rodada.\n'
                 'Uma criatura só pode ser atordoada por esta magia uma vez por cena.',
  'enhancements': [],
  'range': 'curto',
  'area': 'esfera com 6m de raio',
  'duration': 'instantânea',
  'id': 'jda:explosao-caleidoscopica'},
 {'name': 'Explosão de Chamas',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 193 (PDF 199)',
  'pdf_page': 199,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: cone de 6m; Duração: instantânea; Resistência: '
           'Reflexos reduz à metade.',
  'description': 'Um leque de chamas irrompe de suas mãos, causando 2d6 pontos de dano de fogo às criaturas '
                 'na área.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda o alcance para curto, a área para alvo de 1 objeto e a resistência '
                            'para Reflexos anula. Você gera uma pequena explosão que não causa dano mas pode '
                            'acender uma vela, tocha ou fogueira. Também pode fazer um objeto inflamável com '
                            'RD 0 (como uma corda ou pergaminho) ficar em chamas. Uma criatura em posse de '
                            'um objeto pode evitar esse efeito se passar no teste de resistência.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: aumenta o dano em +1d6.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+1 PM: muda a resistência para Reflexos parcial. Se passar, a criatura reduz o '
                            'dano à metade; se falhar, fica em chamas (veja Condições, na página 394).',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'cone de 6m',
  'duration': 'instantânea',
  'id': 'jda:explosao-de-chamas'},
 {'name': 'Ferver Sangue',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 193 (PDF 199)',
  'pdf_page': 199,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: sustentada; Resistência: Fortitude '
           'parcial.',
  'description': 'O sangue do alvo aquece até entrar em ebulição. Quando a magia é lançada, e no início de '
                 'cada um de seus turnos, o alvo sofre 4d8 pontos de dano de fogo e fica enjoado por uma '
                 'rodada (Fortitude reduz o dano à metade e evita a condição). Se o alvo passar em dois '
                 'testes de Fortitude seguidos, dissipa a magia. Se o alvo for reduzido a 0 PV pelo dano '
                 'desta magia, seu corpo explode, matando-o e causando 6d6 pontos de dano de fogo em todas '
                 'as criaturas a até 3m (Reflexos reduz à metade). Essa magia não afeta criaturas sem '
                 'sangue, como construtos ou mortos-vivos.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em +1d8.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+9 PM: muda alvo para criaturas escolhidas. Requer 5º círculo.',
                    'cost': 9,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'sustentada',
  'id': 'jda:ferver-sangue'},
 {'name': 'Físico Divino',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 193 (PDF 199)',
  'pdf_page': 199,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena.',
  'description': 'Você fortalece o corpo do alvo. Ele recebe +2 em Força, Destreza ou Constituição, a sua '
                 'escolha. Esse aumento não oferece PV ou PM adicionais.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: muda o alcance para curto e o alvo para criaturas escolhidas.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: em vez do normal, o alvo recebe +2 nos três atributos físicos. Requer 3º '
                            'círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: em vez do normal, o alvo recebe +4 no atributo escolhido. Requer 4º '
                            'círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+12 PM: em vez do normal, o alvo recebe +4 nos três atributos físicos. Requer '
                            '5º círculo.',
                    'cost': 12,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:fisico-divino'},
 {'name': 'Flecha Ácida',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 193 (PDF 199)',
  'pdf_page': 199,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 criatura ou objeto; Duração: instantânea; Resistência: '
           'Reflexos parcial.',
  'description': 'Você dispara um projétil que causa 4d6 pontos de dano de ácido. Se falhar no teste de '
                 'resistência, o alvo fica coberto por um muco corrosivo, sofrendo mais 2d6 de dano de ácido '
                 'no início de seus dois próximos turnos. Se lançada contra um objeto que não esteja em '
                 'posse de uma criatura a magia causa dano dobrado e ignora a RD do objeto.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, se o alvo coberto pelo muco ácido estiver usando '
                            'armadura ou escudo, o item é corroído. Isso reduz o bônus na Defesa do item em '
                            '1 ponto permanentemente. O item pode ser consertado, restaurando seu bônus '
                            '(veja Ofício, na página 121).',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta a redução na Defesa em +1.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o dano inicial e o dano por rodada em +1d6.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'target': '1 criatura ou objeto',
  'duration': 'instantânea',
  'id': 'jda:flecha-acida'},
 {'name': 'Forma Etérea',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 193 (PDF 199)',
  'pdf_page': 199,
  'stats': 'Execução: completa; Alcance: pessoal; Alvo: você; Duração: sustentada.',
  'description': 'Você e todo o equipamento que está com você são transportados para o plano etéreo, que '
                 'existe paralelamente ao plano material (o mundo físico). Na prática, é como ser '
                 'transformado em um fantasma (mas você ainda é considerado uma criatura viva). Uma criatura '
                 'etérea é invisível (pode alterar en-\n'
                 'tre visível e invisível como ação livre), incorpórea e capaz de se mover em qualquer '
                 'direção, inclusive para cima e para baixo. Ela enxerga o plano material, mas tudo parece '
                 'cinza e insubstancial, reduzindo o alcance da visão e audição para 18m. Magias de '
                 'abjuração e essência afetam criaturas etéreas, mas outras magias, não. Da mesma forma, uma '
                 'criatura etérea não pode atacar nem lançar magias contra criaturas no plano material. Duas '
                 'criaturas etéreas podem se afetar normalmente. Uma criatura afetada pode se materializar '
                 'como uma ação de movimento, encerrando a magia. Uma criatura etérea que se materialize em '
                 'um espaço ocupado é jogada para o espaço não ocupado mais próximo e sofre 1d6 pontos de '
                 'dano de impacto para cada 1,5m de deslocamento.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: muda o alcance para toque e o alvo para até 5 criaturas voluntárias que '
                            'estejam de mãos dadas. Depois que a magia é lançada, as criaturas podem soltar '
                            'as mãos. Requer 5º círculo.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'sustentada',
  'id': 'jda:forma-eterea'},
 {'name': 'Fúria do Panteão',
  'tradition': 'Divina',
  'circle': 5,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 194 (PDF 200)',
  'pdf_page': 200,
  'stats': 'Execução: completa; Alcance: longo; Área: cubo de 90m; Duração: sustentada; Resistência: veja '
           'texto.',
  'description': 'Você cria uma nuvem de tempestade violenta. Os ventos tornam ataques à distância '
                 'impossíveis e fazem a área contar como condição terrível para lançar magia. Além disso, '
                 'inimigos na área têm a visibilidade reduzida (como a magia Névoa). Uma vez por turno, você '
                 'pode gastar uma ação de movimento para gerar um dos efeitos a seguir.\n'
                 'Nevasca. Inimigos na área sofrem 10d6 pontos de dano de frio (Fortitude reduz à metade). A '
                 'área fica coberta de neve, virando terreno difícil até o fim da cena ou até você usar '
                 'siroco.\n'
                 'Raios. Até 6 inimigos a sua escolha na área sofrem 10d8 pontos de dano de eletricidade '
                 '(Reflexos reduz à metade).\n'
                 'Siroco. Transforma a chuva em uma tempestade de areia escaldante. Inimigos na área sofrem '
                 '10d6 pontos de dano (metade corte, metade fogo) e ficam sangrando (Fortitude reduz o dano '
                 'à metade e evita a condição).\n'
                 'Trovões. Inimigos sofrem 10d6 pontos de dano de impacto e ficam desprevenidos por uma '
                 'rodada (Fortitude reduz o dano à metade e evita a condição).',
  'enhancements': [],
  'range': 'longo',
  'area': 'cubo de 90m',
  'duration': 'sustentada',
  'id': 'jda:furia-do-panteao'},
 {'name': 'Globo da Verdade de Gwen',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 194 (PDF 200)',
  'pdf_page': 200,
  'stats': 'Execução: padrão; Alcance: curto; Efeito: 1 globo; Duração: cena.',
  'description': 'Cria um globo flutuante e intangível, com 50cm de diâmetro. O globo mostra uma cena vista '
                 'até uma semana atrás por você ou por uma criatura que você toque ao lançar a magia '
                 '(mediante uma pergunta; a criatura pode fazer um teste de Vontade para anular o efeito), '
                 'permitindo que outras pessoas a vejam.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: o globo mostra uma cena vista até um mês atrás.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: como acima, até um ano atrás.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: ao lançar a magia, você pode tocar um cadáver. O globo mostra a última '
                            'cena vista por essa criatura.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+4 PM: muda o alcance para longo e o efeito para 10 globos. Todos mostram a '
                            'mesma cena.',
                    'cost': 4,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'effect': '1 globo',
  'duration': 'cena',
  'id': 'jda:globo-da-verdade-de-gwen'},
 {'name': 'Globo de Invulnerabilidade',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 194 (PDF 200)',
  'pdf_page': 200,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: sustentada.',
  'description': 'Você é envolto por uma esfera mágica brilhante com 3m de raio, que detém qualquer magia de '
                 '2º círculo ou menor. Nenhuma magia pode ser lançada contra um alvo dentro do globo e '
                 'magias de área não o penetram. No entanto, magias ainda podem ser lançadas de dentro para '
                 'fora.\n'
                 'Uma magia que dissipe outras magias só dissipa o globo se for usada diretamente sobre '
                 'você, não o afetando se usada em área. Efeitos mágicos não são dissipados quando entram na '
                 'esfera, apenas suprimidos (voltam a funcionar fora do globo, caso sua duração não tenha '
                 'acabado). O globo é imóvel e não tem efeito sobre criaturas ou objetos. Após lançá-lo, '
                 'você pode entrar ou sair livremente.',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: muda o efeito para afetar magias de até 3º círculo. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+9 PM: muda o efeito para afetar magias de até 4º círculo. Requer 5º círculo.',
                    'cost': 9,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'sustentada',
  'id': 'jda:globo-de-invulnerabilidade'},
 {'name': 'Guardião Divino',
  'tradition': 'Divina',
  'circle': 4,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 194 (PDF 200)',
  'pdf_page': 200,
  'stats': 'Execução: padrão; Alcance: curto; Efeito: elemental de luz invocado; Duração: cena ou até ser '
           'descarregado.',
  'description': 'A magia invoca um elemental Pequeno, com a forma de um orbe feito de luz di-\n'
                 'vina. A criatura é incorpórea, imune a dano e ilumina como uma tocha. O elemental tem 100 '
                 'pontos de luz.\n'
                 'Uma vez por rodada, durante o seu turno, o elemental pode se movimentar (deslocamento de '
                 'voo 18m) e gastar quantos pontos de luz quiser para curar dano ou condições de criaturas '
                 'em alcance curto, à taxa de 1 PV por 1 ponto de luz ou uma condição por 3 pontos de luz '
                 '(entre abalado, apavorado, alquebrado, atordoado, cego, confuso, debilitado, enjoado, '
                 'esmorecido, exausto, fascinado, fatigado, fraco, frustrado, ofuscado, pasmo, sangrando, '
                 'surdo ou vulnerável). A magia é encerrada quando o elemental fica sem pontos de luz.',
  'enhancements': [],
  'range': 'curto',
  'effect': 'elemental de luz invocado',
  'duration': 'cena ou até ser descarregado',
  'id': 'jda:guardiao-divino'},
 {'name': 'Heroísmo',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 194 (PDF 200)',
  'pdf_page': 200,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena.',
  'description': 'Esta magia imbui uma criatura com coragem e valentia. O alvo fica imune a medo e recebe 40 '
                 'PV temporários e +4 em testes de ataque e rolagens de dano contra o inimigo de maior ND na '
                 'cena.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o bônus para +6.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:heroismo'},
 {'name': 'Hipnotismo',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 194 (PDF 200)',
  'pdf_page': 200,
  'stats': 'Execução: padrão; Alcance: curto; Alvos: 1 animal ou humanoide; Duração: 1d4 rodadas; '
           'Resistência: Vontade anula.',
  'description': 'Suas palavras e movimentos ritmados deixam o alvo fascinado. Esta magia só afeta criaturas '
                 'que possam perceber você. Se usar esta magia em combate, o alvo recebe +5 em seu teste de '
                 'resistência. Se a criatura passar, fica imune a este efeito por um dia.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda a duração para 1 rodada. Em vez de fascinado, o alvo fica pasmo '
                            '(apenas uma vez por cena).',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: como o normal, mas alvos que passem na resistência não sabem que foram '
                            'vítimas de uma magia.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o alvo para animais ou humanoides escolhidos.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: muda a duração para sustentada.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+2 PM: também afeta espíritos e monstros na área. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e6',
                    'text': '+5 PM: também afeta construtos, espíritos, monstros e mortos-vivos na área. '
                            'Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 animal ou humanoide',
  'duration': '1d4 rodadas',
  'id': 'jda:hipnotismo'},
 {'name': 'Ilusão Lacerante',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 195 (PDF 201)',
  'pdf_page': 201,
  'stats': 'Execução: padrão; Alcance: médio; Área: cubo de 9m; Duração: sustentada; Resistência: Vontade '
           'anula.',
  'description': 'Você cria uma ilusão de algum perigo mortal. Quando a magia é lançada, criaturas na área '
                 'devem fazer um teste de Vontade; uma falha significa que a criatura acredita que a ilusão '
                 'é real e sofre 3d6 pontos de dano psíquico não letal. Sempre que uma criatura iniciar seu '
                 'turno dentro da área, deve repetir o teste de Vontade. Se falhar, sofre o dano novamente. '
                 'Somente criaturas que falham veem a ilusão, e racionalizam o efeito sempre que falham no '
                 'teste (por exemplo, acredita que o mesmo teto pode cair sobre ela várias vezes).',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: aumenta o dano em +2d6.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: muda a área para um cubo de 90m. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'area': 'cubo de 9m',
  'duration': 'sustentada',
  'id': 'jda:ilusao-lacerante'},
 {'name': 'Imagem Espelhada',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 195 (PDF 201)',
  'pdf_page': 201,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Três cópias ilusórias suas aparecem. As duplicatas ficam ao seu redor e imitam suas ações, '
                 'tornando difícil para um inimigo saber quem atacar. Você recebe +6 na Defesa. Cada vez que '
                 'um ataque contra você erra, uma das imagens desaparece e o bônus na Defesa diminui em 2. '
                 'Um oponente deve ver as cópias para ser confundido. Se você estiver invisível, ou o '
                 'atacante fechar os olhos, você não recebe o bônus (mas o atacante ainda sofre penalidades '
                 'normais por não enxergar).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de cópias em +1 (e o bônus na Defesa em +2).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: além do normal, toda vez que uma cópia é destruída, emite um clarão de '
                            'luz. A criatura que destruiu a cópia fica ofuscada por uma rodada. Requer 2º '
                            'círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:imagem-espelhada'},
 {'name': 'Imobilizar',
  'tradition': 'Universal',
  'circle': 3,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 195 (PDF 201)',
  'pdf_page': 201,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 humanoide ou animal; Duração: cena; Resistência: '
           'Vontade parcial.',
  'description': 'O alvo fica paralisado; se passar na resistência, em vez disso fica lento. A cada rodada, '
                 'pode gastar uma ação completa para fazer um novo teste de Vontade. Se passar, se liberta '
                 'do efeito.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alvo para 1 espírito.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o número de alvos em +1.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: muda o alvo para 1 criatura. Requer 4º círculo.',
                    'cost': 3,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 humanoide ou animal',
  'duration': 'cena',
  'id': 'jda:imobilizar'},
 {'name': 'Infligir Ferimentos',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 195 (PDF 201)',
  'pdf_page': 201,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: instantânea; Resistência: Fortitude '
           'reduz à metade.',
  'description': 'Você canaliza energia negativa contra um alvo, causando 2d8+2 pontos de dano de trevas (ou '
                 'curando 2d8+2 PV, se for um morto-vivo). Infligir Ferimentos anula Curar Ferimentos.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, se falhar na resistência, o alvo fica fraco pela cena.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano em 1d8+1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda a resistência para nenhum. Como parte da execução da magia, você '
                            'pode fazer um ataque corpo a corpo contra o alvo. Se acertar, causa o dano do '
                            'ataque e o efeito da magia.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+5 PM: muda o alcance para curto e o alvo para criaturas escolhidas.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:infligir-ferimentos'},
 {'name': 'Intervenção Divina',
  'tradition': 'Divina',
  'circle': 5,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 195 (PDF 201)',
  'pdf_page': 201,
  'stats': 'Execução: completa; Alcance: veja texto; Alvo: veja texto; Duração: veja texto; Resistência: '
           'veja texto.',
  'description': 'Você pede a sua divindade para interceder diretamente. Você pode:\n'
                 '• Curar todos os PV e condições de até 10 criaturas em alcance longo (este efeito cura '
                 'mortos-vivos, em vez de causar dano).\n'
                 '• Dissipar os efeitos de qualquer magia de 4º círculo ou menor.\n'
                 'Você pode implorar por algo ainda mais poderoso. Nesse caso, a magia requer o sacrifício '
                 'de 2 PM e pode fazer coisas como:\n'
                 '• Criar um item mundano de até T$ 30.000.\n'
                 '• Duplicar os efeitos de qualquer magia de até 4º círculo. Caso a magia precise de um '
                 'componente material para ser lançada, ainda é necessário providenciar o componente.\n'
                 '• Proteger uma cidade de um desastre, como uma erupção vulcânica, enchente ou terremoto.\n'
                 '• Ressuscitar uma criatura em alcance longo que tenha morrido há até uma rodada. A '
                 'criatura acorda com 1 PV.\n'
                 '• Qualquer outra coisa que o mestre autorize, conforme os desejos e objetivos da divindade '
                 'do conjurador.',
  'enhancements': [],
  'range': 'veja texto',
  'target': 'veja texto',
  'duration': 'veja texto',
  'id': 'jda:intervencao-divina'},
 {'name': 'Invisibilidade',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 195 (PDF 201)',
  'pdf_page': 201,
  'stats': 'Execução: livre; Alcance: pessoal; Alvo: você; Duração: 1 rodada.',
  'description': 'O alvo fica invisível (incluindo seu equipamento). Um personagem invisível recebe '
                 'camuflagem total, +10 em testes de Furtividade contra ouvir e criaturas que não possam '
                 'vê-lo ficam desprevenidas contra seus ataques.\n'
                 'A magia termina se o alvo faz uma ação hostil contra uma criatura. Ações contra objetos '
                 'livres não dissipam a Invisibilidade (você pode tocar ou apanhar objetos que não estejam '
                 'sendo segurados por outras criaturas). Causar dano indiretamente — por exemplo, acendendo '
                 'o pavio de um barril de pólvora que vai detonar mais tarde — não é considerado um ataque.\n'
                 'Objetos soltos pelo alvo voltam a ser visíveis e objetos apanhados por ele ficam '
                 'invisíveis. Qualquer parte de um item carregado que se estenda além de seu alcance corpo a '
                 'corpo natural se torna visível. Uma luz nunca fica invisível (mesmo que sua fonte seja).',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda a execução para ação padrão, o alcance para toque e o alvo para 1 '
                            'criatura ou 1 objeto Grande ou menor.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda a duração para cena. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: muda a duração para sustentada. Em vez do normal, o alvo gera uma esfera '
                            'de invisibilidade. Não pode ser usado em conjunto com outros aprimoramentos. O '
                            'alvo e todas as criaturas a até 3m dele se tornam invisíveis, como no efeito '
                            'normal da magia (ainda ficam visíveis caso façam uma ação hostial). A esfera se '
                            'move juntamente com o alvo; qualquer coisa que saia da esfera fica visível. '
                            'Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+7 PM: muda a execução para ação padrão, o alcance para toque e o alvo para 1 '
                            'criatura. A magia não é dissipada caso o alvo faça uma ação hostil. Requer 4º '
                            'círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': '1 rodada',
  'id': 'jda:invisibilidade'},
 {'name': 'Invulnerabilidade',
  'tradition': 'Universal',
  'circle': 5,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 195 (PDF 201)',
  'pdf_page': 201,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Esta magia cria uma barreira mágica impenetrável que protege você contra efeitos nocivos '
                 'mentais ou físicos, a sua escolha.\n'
                 'Proteção mental: você fica imune às condições abalado, alquebrado, apavorado, atordoado, '
                 'confuso, esmorecido,\n'
                 'fascinado, frustrado e pasmo, além de efeitos de encantamento e ilusão.\n'
                 'Proteção física: você fica imune às condições atordoado, cego, debilitado, enjoado, '
                 'envenenado, exausto, fatigado, fraco, lento, ofuscado e paralisado, além de acertos '
                 'críticos, ataques furtivos e doenças.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: muda o alcance para curto e o alvo para 1 criatura.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:invulnerabilidade'},
 {'name': 'Lágrimas de Wynna',
  'tradition': 'Divina',
  'circle': 5,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 196 (PDF 202)',
  'pdf_page': 202,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: instantânea; Resistência: Vontade '
           'parcial.',
  'description': 'Se falhar no teste de resistência, o alvo perde a habilidade de lançar magias arcanas até '
                 'o fim da cena. Se passar, perde a habilidade por uma rodada.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda a área para esfera com 6m de raio e o alvo para criaturas '
                            'escolhidas.',
                    'cost': 2,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: muda a execução para um dia e adiciona custo adicional (sacrifício de 1 '
                            'PM). O alvo da magia precisa ser mantido em alcance curto do conjurador durante '
                            'toda a execução. Ao término, faz um teste de Vontade. Se falhar, perde a '
                            'habilidade de lançar magias arcanas permanentemente. Se passar, resiste, mas '
                            'ainda pode ser alvo da magia no dia seguinte. Nenhum poder mortal é capaz de '
                            'reverter essa perda. Os clérigos de Wynna dizem que a deusa chora cada vez que '
                            'este ritual é realizado.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:lagrimas-de-wynna'},
 {'name': 'Lança Ígnea de Aleph',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 196 (PDF 202)',
  'pdf_page': 202,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 criatura; Duração: instantânea; Resistência: Reflexos '
           'parcial.',
  'description': 'Esta magia foi desenvolvida pelo mago imortal Aleph Olhos Vermelhos, um entusiasta dos '
                 'estudos vulcânicos. Ela dispara um projétil de magma contra o alvo, que sofre 4d6 pontos '
                 'de dano de fogo e 4d6 pontos de dano de perfuração e fica em chamas. As chamas causam 2d6 '
                 'pontos de dano por rodada, em vez do dano normal. Se passar no teste de resistência, o '
                 'alvo sofre metade do dano e não fica em chamas.\n'
                 'Respingos de rocha incandescente se espalham com a explosão, atingindo todas as criaturas '
                 'adjacentes ao alvo, que devem fazer um teste de Reflexos. Se falharem, ficam em chamas, '
                 'como descrito acima.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: aumenta o dano inicial em +2d6 e o dano do efeito em chamas em +1d6.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: muda a duração para cena ou até ser descarregada. Em vez do efeito '
                            'normal, a magia cria quatro dardos de lava que flutuam ao lado do conjurador. '
                            'Uma vez por rodada, como uma ação livre, você pode disparar um dos dardos em '
                            'uma criatura, causando o efeito normal da magia. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'médio',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:lanca-ignea-de-aleph'},
 {'name': 'Legião',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 196 (PDF 202)',
  'pdf_page': 202,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: até 10 criaturas na área; Duração: sustentada.',
  'description': 'Resistência: Vontade parcial.\n'
                 'Você domina a mente dos alvos. Os alvos obedecem cegamente a seus comandos, exceto ordens '
                 'claramente suicidas. Um alvo tem direito a um teste no final de cada um de seus turnos '
                 'para se livrar do efeito. Alvos que passarem no teste ficam abalados por 1 rodada enquanto '
                 'recuperam a consciência.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o número de alvos em +1.',
                    'cost': 1,
                    'min_circle': 5,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'duration': 'sustentada',
  'area': 'até 10 criaturas na área',
  'id': 'jda:legiao'},
 {'name': 'Lendas e Histórias',
  'tradition': 'Universal',
  'circle': 3,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 196 (PDF 202)',
  'pdf_page': 202,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura, objeto ou local; Duração: sustentada.',
  'description': 'Você descobre informações sobre uma criatura, objeto ou local que esteja tocando. O que '
                 'exatamente você descobre depende do mestre: talvez você não descubra tudo que há para '
                 'saber, mas ganhe pistas para continuar a investigação. A cada rodada que mantiver a magia, '
                 'você descobre:\n'
                 '• Todas as informações sobre o alvo, como se tivesse passado em todos os testes de '
                 'Conhecimento para tal.\n'
                 '• Todas as habilidades do alvo. Se for uma criatura, você sabe suas estatísticas de jogo '
                 'como raça, classe, nível, atributos, magias, resistências e fraquezas. Se for um item '
                 'mágico, aprende seu efeito e funcionamento.\n'
                 '• Se o alvo está sob influência de alguma magia e todas as informações sobre as magias '
                 'ativas, se houver alguma.',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: muda a execução para um dia, o alcance para ilimitado e adiciona '
                            'componente material (cuba de ouro cheia d’água e ingredientes mágicos, no valor '
                            'de T$ 1.000). Você ainda precisa ter alguma informação sobre o alvo, como um '
                            'nome, descrição ou localização.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura, objeto ou local',
  'duration': 'sustentada',
  'id': 'jda:lendas-e-historias'},
 {'name': 'Leque Cromático',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 196 (PDF 202)',
  'pdf_page': 202,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: cone de 4,5m; Duração: instantânea.',
  'description': 'Resistência: Vontade parcial.\n'
                 'Um cone de luzes brilhantes surge das suas mãos, deixando os animais e humanoides na área '
                 'atordoados por 1 rodada (apenas uma vez por cena, Vontade anula) e ofuscados pela cena.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: além do normal, as criaturas afetadas ficam vulneráveis pela cena.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: também afeta espíritos e monstros na área. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: também afeta construtos, espíritos, monstros e mortos-vivos na área. '
                            'Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'cone de 4,5m',
  'duration': 'instantânea',
  'id': 'jda:leque-cromatico'},
 {'name': 'Libertação',
  'tradition': 'Universal',
  'circle': 4,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 196 (PDF 202)',
  'pdf_page': 202,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: cena.',
  'description': 'O alvo fica imune a efeitos de movimento e ignora qualquer efeito que impeça ou restrinja '
                 'seu deslocamento. Por fim, pode usar habilidades que exigem liberdade de movimentos mesmo '
                 'se estiver usando armadura ou escudo.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: além do normal, o alvo pode caminhar sobre a água ou outros líquidos com '
                            'seu deslocamento normal. Entretanto, isso não protege contra qualquer efeito '
                            'que o líquido possa causar (o alvo pode andar sobre lava, mas ainda vai sofrer '
                            'dano).',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: além do normal, o alvo pode escolher 20 em todos os testes de Atletismo.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: além do normal, o alvo pode escolher 20 em todos os testes de Acrobacia '
                            'e pode fazer todas as manobras desta perícia mesmo sem treinamento.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+5 PM: muda o alcance para curto e o alvo para até 5 criaturas.',
                    'cost': 5,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+5 PM: pode dissipar Aprisionamento.',
                    'cost': 5,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:libertacao'},
 {'name': 'Ligação Sombria',
  'tradition': 'Divina',
  'circle': 4,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 196 (PDF 202)',
  'pdf_page': 202,
  'stats': 'Execução: padrão; Alcance: longo; Alvo: 1 criatura; Duração: 1 dia; Resistência: Fortitude '
           'anula.',
  'description': 'Cria uma conexão entre seu corpo e o da criatura alvo, deixando uma marca idêntica na pele '
                 'de ambos. Enquanto a magia durar, sempre que você sofrer qualquer dano ou condição, o alvo '
                 'desta magia deve fazer um teste de Fortitude; se falhar, sofre o mesmo dano\n'
                 'que você ou adquire a mesma condição. A magia termina se o alvo chegar a 0 pontos de vida.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: a magia não termina se o alvo chegar a 0 PV (o que significa que dano '
                            'causado por essa magia pode matá-lo).',
                    'cost': 5,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'target': '1 criatura',
  'duration': '1 dia',
  'id': 'jda:ligacao-sombria'},
 {'name': 'Ligação Telepática',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 197 (PDF 203)',
  'pdf_page': 203,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 2 criaturas voluntárias; Duração: 1 dia.',
  'description': 'Você cria um elo mental entre duas criaturas com Inteligência 3 ou maior (você pode ser '
                 'uma delas). As criaturas podem se comunicar independente de idioma ou distância, mas não '
                 'em mundos diferentes.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de alvos em +1.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda o alvo para 1 criatura. Em vez do normal, você cria um elo mental '
                            'que permite que você veja e ouça pelos sentidos da criatura, se gastar uma ação '
                            'de movimento. Uma criatura involuntária pode fazer um teste de Vontade para '
                            'suprimir a magia por uma hora. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': '2 criaturas voluntárias',
  'duration': '1 dia',
  'id': 'jda:ligacao-telepatica'},
 {'name': 'Localização',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 197 (PDF 203)',
  'pdf_page': 203,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: esfera com 90m de raio; Duração: cena.',
  'description': 'Esta magia pode encontrar uma criatura ou objeto a sua escolha. Você pode pensar em termos '
                 'gerais (“um elfo”, “algo de metal”) ou específicos (“Gwen, a elfa”, “uma espada longa”). A '
                 'magia indica a direção e distância da criatura ou objeto mais próximo desse tipo, caso '
                 'esteja ao alcance. Você pode movimentar-se para continuar procurando. Procurar algo muito '
                 'específico (“a espada longa encantada do Barão Rulyn”) exige que você tenha em mente uma '
                 'imagem precisa do objeto; caso a imagem não seja muito próxima da verdade, a magia falha, '
                 'mas você gasta os PM mesmo assim. Esta magia pode ser bloqueada por uma fina camada de '
                 'chumbo.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda a área para alvo você. Em vez do normal, você sabe onde fica o '
                            'norte e recebe +5 em testes de Sobrevivência para se orientar.',
                    'cost': 0,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: aumenta a área em um fator de 10 (90m para 900m, 900m para 9km e assim '
                            'por diante).',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'esfera com 90m de raio',
  'duration': 'cena',
  'id': 'jda:localizacao'},
 {'name': 'Luz',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 197 (PDF 203)',
  'pdf_page': 203,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 objeto; Duração: cena; Resistência: Vontade anula '
           '(veja texto).',
  'description': 'O alvo emite luz (mas não produz calor) em uma área com 6m de raio. O objeto pode ser '
                 'guardado (em um bolso, por exemplo) para interromper a luz, que voltará a funcionar caso o '
                 'objeto seja revelado. Se lançar a magia num objeto de uma criatura involuntária, ela tem '
                 'direito a um teste de Vontade para anulá-la. Luz anula Escuridão.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta a área iluminada em +3m de raio.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a duração para um dia.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda a duração para permanente e adiciona componente material (pó de '
                            'rubi no valor de T$ 50). Não pode ser usado em conjunto com outros '
                            'aprimoramentos. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+0 PM (Apenas Arcanos): muda o alvo para 1 criatura. Você lança a magia nos '
                            'olhos do alvo, que fica ofuscado pela cena. Não afeta criaturas cegas.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True},
                   {'id': 'e5',
                    'text': '+2 PM (Apenas Arcanos): muda o alcance para longo e o efeito para cria 4 '
                            'pequenos globos flutuantes de pura luz. Você pode posicionar os globos onde '
                            'quiser dentro do alcance. Você pode enviar um à frente, outra para trás, outra '
                            'para cima e manter um perto de você, por exemplo. Uma vez por rodada, você pode '
                            'mover os globos com uma ação livre. Cada um ilumina como uma tocha, mas não '
                            'produz calor. Se um globo ocupar o espaço de uma criatura, ela fica ofuscada e '
                            'sua silhueta pode ser vista claramente (ela não recebe camuflagem por escuridão '
                            'ou invisibilidade). Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True},
                   {'id': 'e6',
                    'text': '+2 PM (Apenas Divinos): a luz é cálida como a do sol. Criaturas que sofrem '
                            'penalidades e dano pela luz solar sofrem seus efeitos como se estivessem '
                            'expostos à luz solar real. Seus aliados na área estabilizam automaticamente e '
                            'ficam imunes à condição sangrando, e seus inimigos ficam ofuscados. Requer 2º '
                            'círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True},
                   {'id': 'e7',
                    'text': '+5 PM (Apenas Divinos): muda o alcance para toque e o alvo para 1 criatura. Em '
                            'vez do normal, o alvo é envolto por um halo de luz, recebendo +10 em testes de '
                            'Diplomacia e redução de trevas 10. Requer 2º círculo.',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': True}],
  'range': 'curto',
  'target': '1 objeto',
  'duration': 'cena',
  'id': 'jda:luz'},
 {'name': 'Manto de Sombras',
  'tradition': 'Universal',
  'circle': 3,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 197 (PDF 203)',
  'pdf_page': 203,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: sustentada.',
  'description': 'Você fica coberto por um manto de energia sombria. Nesta forma, torna-se incorpóreo '
                 '(inclui seu equipamento): só pode ser afetado por armas e habilidades mágicas, ou por '
                 'outras criaturas incorpóreas, e pode atravessar objetos sólidos, mas não manipulá-los. '
                 'Também não pode atacar criaturas normais (mas ainda pode lançar magias nelas). Além disso, '
                 'se torna vulnerável à luz direta: se exposto a uma fonte de luz, sofre 1 ponto de dano por '
                 'rodada.\n'
                 'Você pode gastar uma ação de movimento e 1 PM para “entrar” em uma sombra do seu tamanho '
                 'ou maior e se teletransportar para outra sombra, também do seu tamanho ou maior, em '
                 'alcance médio.',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: muda o alcance para toque e o alvo para 1 criatura. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'sustentada',
  'id': 'jda:manto-de-sombras'},
 {'name': 'Manto do Cruzado',
  'tradition': 'Divina',
  'circle': 4,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 197 (PDF 203)',
  'pdf_page': 203,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: sustentada.',
  'description': 'Você invoca o poder de sua divindade na forma de um manto de energia que reveste seu '
                 'corpo. Esta magia tem duas versões. Você escolhe qual versão pode lançar quando aprende '
                 'esta magia. Ela não pode ser mudada.\n'
                 'Manto de Luz: um manto dourado e luminoso. No início de cada um de seus turnos, você e '
                 'todos os seus aliados em alcance curto recuperam 2d8 PV. Você recebe imunidade a dano de '
                 'trevas e seus ataques corpo a corpo causam +2d8 pontos de dano de luz.\n'
                 'Manto de Trevas: um manto negro como a noite. No início de cada um de seus turnos, todos '
                 'os inimigos em alcance curto sofrem 4d8 pontos de dano de trevas. Você cura metade de todo '
                 'o dano causado pela magia.',
  'enhancements': [],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'sustentada',
  'id': 'jda:manto-do-cruzado'},
 {'name': 'Mão Poderosa de Talude',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 197 (PDF 203)',
  'pdf_page': 203,
  'stats': 'Execução: padrão; Alcance: médio; Efeito: mão gigante de energia; Duração: sustentada.',
  'description': 'Esta magia cria uma mão flutuante Grande que sempre se posiciona entre você e um oponente '
                 'a sua escolha. A mão fornece cobertura leve (+5 na Defesa) contra esse oponente. Nada é '
                 'capaz de enganar a mão — coisas como escuridão, invisibilidade, metamorfose e disfarces '
                 'mundanos não a impedem de protegê-lo. A mão tem Defesa 20 e PV e resistências iguais aos '
                 'seus. Com\n'
                 'uma ação de movimento, você pode comandar a mão para que o proteja de outro oponente ou '
                 'para que realize uma das ações a seguir.\n'
                 'Agarrar: a mão usa uma manobra agarrar contra o oponente, usando o seu Misticismo com um '
                 'bônus adicional de +10. A mão mantém o oponente agarrado, mas não causa dano.\n'
                 'Esmagar: a mão esmaga um oponente agarrado, causando 2d6+10 pontos de dano de impacto.\n'
                 'Empurrar: a mão afasta o oponente (manobra empurrar usando o seu Misticismo com um bônus '
                 'adicional de +10). A mão acompanha o oponente para empurrá-lo o máximo que conseguir, '
                 'dentro do alcance da magia.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em +1d6+5.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: muda o bônus adicional em Misticismo para +20. Requer 5º círculo.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'effect': 'mão gigante de energia',
  'duration': 'sustentada',
  'id': 'jda:mao-poderosa-de-talude'},
 {'name': 'Mapear',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 198 (PDF 204)',
  'pdf_page': 204,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: superfície ou objeto plano, como uma mesa ou papel; '
           'Duração: cena.',
  'description': 'Uma fagulha percorre a superfície afetada, queimando-a enquanto esboça um mapa da região '
                 'onde o conjurador está. Se você conhece o lugar, o mapa será completo. Caso contrário, '
                 'apresentará apenas um esboço geral, além de um ponto de referência (para possibilitar '
                 'localização) e um lugar de interesse, ambos definidos pelo mestre. A região representada '
                 'no mapa tem tamanho máximo de um quadrado de 10km de lado. Caso você esteja dentro de uma '
                 'construção, o mapa mostrará o andar no qual você se encontra.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: muda o alvo para 1 criatura e a duração para 1 hora. Em vez do normal, a '
                            'criatura tocada descobre o caminho mais direto para entrar ou sair de um lugar. '
                            'Assim, a magia pode ser usada para descobrir a rota até o relicário de uma '
                            'catedral ou a saída mais próxima de uma masmorra (mas não para encontrar a '
                            'localização de uma criatura ou objeto; a magia funciona apenas em relação a '
                            'lugares). Caso a criatura demore mais de uma hora para percorrer o caminho, o '
                            'conhecimento se perde.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': 'superfície ou objeto plano, como uma mesa ou papel',
  'duration': 'cena',
  'id': 'jda:mapear'},
 {'name': 'Marca da Obediência',
  'tradition': 'Universal',
  'circle': 2,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 198 (PDF 204)',
  'pdf_page': 204,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena; Resistência: Vontade anula.',
  'description': 'Você toca uma criatura, gravando uma marca mística no corpo dela enquanto profere uma '
                 'ordem, como “não ataque a mim ou meus aliados”, “siga-me” ou “não saia desta sala”. A '
                 'criatura deve seguir essa ordem, gastando todas as ações de seu turno para isso. A ordem '
                 'não pode ser genérica demais (como “ajude-me”, por exemplo), nem forçar o alvo a atos '
                 'suicidas. A cada rodada, o alvo pode fazer um teste de Vontade. Se passar, a magia é '
                 'dissipada.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: muda a duração para um dia. Se não estiver em combate, a criatura só '
                            'pode fazer o teste de Vontade a cada hora. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: sempre que o alvo fizer o teste de Vontade e falhar, a marca causa 3d6 '
                            'pontos de dano psíquico. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:marca-da-obediencia'},
 {'name': 'Marionete',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 198 (PDF 204)',
  'pdf_page': 204,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 criatura; Duração: sustentada; Resistência: Fortitude '
           'anula.',
  'description': 'Esta magia manipula o sistema nervoso do alvo. Ao sofrer a magia, e no início de cada um '
                 'de seus turnos, a vítima faz um teste de Fortitude. Se passar, a magia é anulada. Se '
                 'falhar, todas as suas ações físicas naquele turno estarão sob controle do conjurador. A '
                 'vítima ainda tem consciência de tudo que acontece à sua volta, podendo ver, ouvir e até '
                 'falar com certo esforço (mas não para lançar magias). Contudo, seu corpo realiza apenas os '
                 'movimentos que o conjurador deseja. A vítima pode ser manipulada para se movimentar, '
                 'lutar, usar habilidades de combate... Enfim, qualquer coisa de que seja fisicamente '
                 'capaz.\n'
                 'Você precisa de linha de efeito para controlar a vítima. Se perder o contato, não poderá '
                 'controlá-la — mas ela estará paralisada até que o conjurador recupere o controle ou a '
                 'magia termine.',
  'enhancements': [],
  'range': 'médio',
  'target': '1 criatura',
  'duration': 'sustentada',
  'id': 'jda:marionete'},
 {'name': 'Mata-Dragão',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 198 (PDF 204)',
  'pdf_page': 204,
  'stats': 'Execução: duas rodadas; Alcance: pessoal; Área: cone de 30m; Duração: instantânea; Resistência: '
           'Reflexos reduz à metade.',
  'description': 'Esta é uma das mais poderosas magias de destruição existentes. Após entoar longos '
                 'cânticos, o conjurador dispara uma carga de energia que varre uma enorme área à sua '
                 'frente, causando 20d12 pontos de dano de essên-\n'
                 'cia em todas as criaturas, construções e objetos livres atingidos. Sempre que rola um '
                 'resultado 12 em um dado de dano, a magia causa +1d12 pontos de dano. Apesar de seu poder '
                 'destrutivo, esta magia é lenta, tornando seu uso difícil em combate.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o dano em 1d12.',
                    'cost': 1,
                    'min_circle': 5,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'cone de 30m',
  'duration': 'instantânea',
  'id': 'jda:mata-dragao'},
 {'name': 'Mente Divina',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 198 (PDF 204)',
  'pdf_page': 204,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena.',
  'description': 'Você fortalece a mente do alvo. Ele recebe +2 em Inteligência, Sabedoria ou Carisma, a sua '
                 'escolha. Esse aumento não oferece PV, PM ou perícias adicionais.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: muda o alcance para curto e o alvo para criaturas escolhidas.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: em vez do normal, o alvo recebe +2 nos três atributos mentais. Requer 3º '
                            'círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: em vez do normal, o alvo recebe +4 no atributo escolhido. Requer 4º '
                            'círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+12 PM: em vez do normal, o alvo recebe +4 nos três atributos mentais. Requer '
                            '5º círculo.',
                    'cost': 12,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:mente-divina'},
 {'name': 'Metamorfose',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 198 (PDF 204)',
  'pdf_page': 204,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Você muda sua aparência e forma — incluindo seu equipamento — para qualquer outra '
                 'criatura, existente ou imaginada. Independentemente da forma escolhida, você recebe +20 em '
                 'testes de Enganação para disfarce. Características não mencionadas não mudam.\n'
                 'Se mudar para uma forma humanoide, pode mudar o tipo de dano (entre corte, impacto e '
                 'perfuração) de suas armas (se usa uma maça e transformá-la em espada longa, ela pode '
                 'causar dano de corte, por exemplo). Se quiser, pode assumir uma forma humanoide com uma '
                 'categoria de tamanho acima ou abaixo da sua; nesse caso aplique os modificadores em '
                 'Furtividade e testes de manobra.\n'
                 'Se mudar para outras formas, você pode escolher uma Forma Selvagem do druida (veja no '
                 'Capítulo 1). Nesse caso você não pode atacar com suas armas, falar ou lançar magias até '
                 'voltar ao normal, mas recebe uma ou mais armas naturais e os bônus da forma selvagem '
                 'escolhida.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: a forma escolhida recebe uma habilidade de sentidos entre faro, visão na '
                            'penumbra e visão no escuro.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: a forma escolhida recebe percepção às cegas. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: muda o alcance para toque, o alvo para 1 criatura e adiciona resistência '
                            '(Vontade anula).',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: muda o alcance para médio, o alvo para 1 criatura e a resistência para '
                            'Vontade anula. Em vez do normal, transforma o alvo em uma criatura ou objeto '
                            'inofensivo (ovelha, sapo, galinha, pudim de ameixa etc.). A criatura não pode '
                            'atacar, falar e lançar magias; seu deslocamento vira 3m e sua Defesa vira 10. '
                            'Suas outras características não mudam. No início de seus turnos, o alvo pode '
                            'fazer um teste de Vontade; se passar, retorna à sua forma normal e a magia '
                            'termina. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+5 PM: se mudar para formas não humanoides, pode escolher uma Forma Selvagem '
                            'Aprimorada. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e6',
                    'text': '+9 PM: se mudar para formas não humanoides, pode escolher uma Forma Selvagem '
                            'Superior. Requer 4º círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e7',
                    'text': '+12 PM: além do normal, no início de seus turnos o alvo pode mudar de forma '
                            'novamente, como uma ação livre, fazendo novas escolhas. Requer 5º círculo.',
                    'cost': 12,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:metamorfose'},
 {'name': 'Miasma Mefítico',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 199 (PDF 205)',
  'pdf_page': 205,
  'stats': 'Execução: padrão; Alcance: médio; Área: nuvem com 6m de raio; Duração: instantânea; Resistência: '
           'Fortitude (veja texto).',
  'description': 'A área é coberta por emanações letais. Criaturas na área sofrem 5d6 pontos de dano de '
                 'ácido e ficam enjoadas por 1 rodada. Se passarem na resistência, sofrem metade do dano e '
                 'não ficam enjoadas.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda o alcance para toque, a área para alvo (1 criatura com 0 PV ou '
                            'menos), a duração para instantânea, a resistência para Fortitude anula e '
                            'adiciona componente material (pó de ônix no valor de T$ 10). Em vez do normal, '
                            'você canaliza o Miasma contra uma vítima. Se falhar na resistência, ela morre e '
                            'você recebe +2 na CD de suas magias por um dia. Se passar, fica imune a este '
                            'truque por um dia.',
                    'cost': 0,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano em +1d6.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: muda o tipo do dano para trevas.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'area': 'nuvem com 6m de raio',
  'duration': 'instantânea',
  'id': 'jda:miasma-mefitico'},
 {'name': 'Miragem',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 199 (PDF 205)',
  'pdf_page': 205,
  'stats': 'Execução: padrão; Alcance: longo; Área: cubo de até 90m de lado; Duração: 1 dia; Resistência: '
           'Vontade desacredita.',
  'description': 'Você faz um terreno parecer outro, incluindo sons e cheiros. Uma planície pode parecer um '
                 'pântano, uma floresta pode parecer uma montanha etc. Esta magia pode ser usada para criar '
                 'armadilhas: areia movediça pode parecer terra firme ou um precipício pode parecer um lago. '
                 'Você pode alterar, incluir e esconder estruturas dentro da área, mas não criaturas (embora '
                 'elas possam se esconder nas estruturas ilusórias).',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: além do normal, pode alterar a aparência de criaturas escolhidas na '
                            'área, como se usando Disfarce Ilusório.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+9 PM: muda a duração para permanente e adiciona componente material (pó de '
                            'diamante no valor de T$ 1.000). Requer 4º círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'area': 'cubo de até 90m de lado',
  'duration': '1 dia',
  'id': 'jda:miragem'},
 {'name': 'Missão Divina',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 199 (PDF 205)',
  'pdf_page': 205,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: 1 semana ou até ser descarregada; '
           'Resistência: Vontade anula (veja texto)',
  'description': 'Esta magia obriga o alvo a cumprir uma tarefa a sua escolha. Ela dura uma semana ou até o '
                 'alvo cumprir a tarefa, o que vier primeiro. O alvo pode recusar a missão — mas, no fim de '
                 'cada dia em que não se esforçar para cumprir a tarefa, deve fazer um teste de Vontade; se '
                 'falhar, sofre uma penalidade cumulativa de –2 em todos os testes e rolagens.\n'
                 'A Missão Divina não pode forçar um ato suicida, nem uma missão impossível (como matar um '
                 'ser que não existe).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para toque, a duração para permanente e adiciona '
                            'penalidade de –1 PM. Em vez do normal, você inscreve uma marca (como uma '
                            'tatuagem) na pele do alvo e escolhe um tipo de ação que ativará a marca. '
                            'Normalmente, será cometer um crime (roubar, matar...) ou outra coisa contrária '
                            'às Obrigações & Restrições de sua divindade. Sempre que a marca é ativada, o '
                            'alvo recebe uma penalidade cumulativa de –2 em todos os testes. Muitas vezes, '
                            'portar essa marca é um estigma por si só, já que esta magia normalmente é '
                            'lançada em criminosos ou traidores. Uma magia que dissipe outras suprime a '
                            'marca e suas penalidades por um dia; elas só podem ser totalmente removidas '
                            'pelo conjurador original ou pela magia Purificação.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: aumenta a duração para 1 ano ou até ser descarregada.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': '1 semana ou até ser descarregada',
  'id': 'jda:missao-divina'},
 {'name': 'Montaria Arcana',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 199 (PDF 205)',
  'pdf_page': 205,
  'stats': 'Execução: padrão; Alcance: curto; Efeito: criatura conjurada; Duração: 1 dia.',
  'description': 'Esta magia convoca um parceiro cavalo (ou pônei) de guerra veterano. Sua aparência é de um '
                 'animal negro com crina e cauda cinzentas e cascos feitos de fumaça, mas você pode mudá-la '
                 'se quiser. Além dos benefícios normais, a Montaria Arcana pode atravessar terreno difícil '
                 'sem redução em seu deslocamento. Você pode usar Misticismo no lugar de Cavalgar para '
                 'efeitos desta montaria (incluindo ser considerado treinado).',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, criaturas do tipo animal em alcance curto da montaria '
                            'devem fazer um teste de Vontade. Se passarem, ficam abaladas pela cena; se '
                            'falharem, ficam apavoradas por 1d4 rodadas, depois abaladas pela cena.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda a duração para permanente e adiciona penalidade de –3 PM.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: aumenta o tamanho da montaria em uma categoria. Isso também aumenta o '
                            'número de criaturas que ela pode carregar — duas para uma criatura Enorme, seis '
                            'para Colossal. Uma única criatura controla a montaria; as outras apenas são '
                            'deslocadas.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: muda o nível do parceiro para mestre. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'effect': 'criatura conjurada',
  'duration': '1 dia',
  'id': 'jda:montaria-arcana'},
 {'name': 'Muralha de Ossos',
  'tradition': 'Universal',
  'circle': 4,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 199 (PDF 205)',
  'pdf_page': 205,
  'stats': 'Execução: padrão; Alcance: médio; Efeito: muro de ossos; Duração: cena.',
  'description': 'Uma parede de ossos se eleva da terra. A parede tem 15m de comprimento, 9m de altura e '
                 '1,5m de espessura. Ela pode ter qualquer forma — não precisa ser uma linha reta —, mas sua '
                 'base precisa estar sempre tocando o solo. Quando a parede surge, criaturas na área ocupada '
                 'ou adjacentes sofrem 4d8 pontos de dano de corte e precisam fazer um teste de Reflexos '
                 'para não ficarem presas no emaranhado de ossos. Uma criatura presa dessa maneira fica '
                 'agarrada, e pode gastar uma ação padrão para fazer um teste de Atletismo para se soltar. '
                 'Se passar no teste, sai da muralha para um dos lados adjacentes. Se falhar, sofre 4d8 '
                 'pontos de dano de corte.\n'
                 'É possível destruir o muro para atravessá-lo ou libertar uma criatura agarrada. Cada '
                 'trecho de 3m do muro tem Defesa 8, 40 PV e redução de corte, frio e perfuração 10. Também '
                 'é possível escalar a parede. Isso exige um teste de Atletismo e causa 4d8 pontos de dano '
                 'de corte para cada 3m escalados.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: aumenta o comprimento em +15m e a altura em +3m.',
                    'cost': 3,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: o muro é feito de uma massa de esqueletos animados. Sempre que uma '
                            'criatura iniciar seu turno adjacente ou escalando a muralha, deve fazer um '
                            'teste de Reflexos. Se falhar fica agarrada, sofrendo os efeitos normais de '
                            'estar agarrada pela magia.',
                    'cost': 5,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'effect': 'muro de ossos',
  'duration': 'cena',
  'id': 'jda:muralha-de-ossos'},
 {'name': 'Muralha Elemental',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 200 (PDF 206)',
  'pdf_page': 206,
  'stats': 'Execução: padrão; Alcance: médio; Efeito: muralha de energia; Duração: cena.',
  'description': 'Resistência: veja texto. Uma muralha de um elemento a sua escolha se eleva da terra. Ela '
                 'pode ser um muro de até 30m de comprimento e 3m de altura (ou o contrário) ou uma cúpula '
                 'de 3m de raio. Os efeitos variam conforme o elemento escolhido. Fogo. Faz surgir uma '
                 'violenta cortina de chamas. Um lado da muralha (a sua escolha) emite ondas de calor, que '
                 'causam 2d6 pontos de dano de fogo em criaturas a até 6m quando você lança a magia e no '
                 'início de seus turnos. Atravessar a muralha causa 8d6 pontos de dano de fogo. Caso seja '
                 'criada em uma área onde existem criaturas, elas sofrem dano como se estivessem '
                 'atravessando a muralha, mas podem fazer um teste de Reflexos para reduzir o dano à metade '
                 'e escapar para um lado (a criatura escolhe, mas se escapar para o lado quente sofrerá mais '
                 '2d6 pontos de dano). Gelo. Evoca uma parede grossa de gelo denso com 15cm de espessura. Na '
                 'forma de cúpula, pode prender uma ou mais criaturas, mas elas têm direito a um teste de '
                 'Reflexos para escapar antes que a cúpula se forme. Cada trecho de 3m da muralha tem Defesa '
                 '8, 40 PV e RD 5. Um trecho da muralha que atinja 0 PV será rompido. Qualquer efeito de '
                 'fogo causa dano dobrado à muralha. Uma criatura que atravesse um trecho rompido da muralha '
                 'sofre 4d6 pontos de dano de frio.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano por atravessar a muralha em +2d6.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o comprimento em +15m e altura em +3m, até 60m de comprimento e '
                            '9m de altura.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+4 PM: muda a duração para sustentada e adiciona uma nova escolha, Essência. A '
                            'muralha é invisível e indestrutível — imune a qualquer forma de dano e não '
                            'afetada por nenhuma magia. Ela não pode ser atravessada nem mesmo por criaturas '
                            'incorpóreas. No entanto, magias que teletransportam criaturas, como Salto '
                            'Dimensional, podem atravessá-la. Magias e efeitos de dano, como Bola de Fogo e '
                            'o sopro de um dragão, não vencem a muralha, mas magias lançadas diretamente '
                            'sobre uma criatura ou área, como Sono, podem ser lançadas contra alvos que '
                            'estejam no outro lado como se tivessem linha de efeito. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'effect': 'muralha de energia',
  'duration': 'cena',
  'id': 'jda:muralha-elemental'},
 {'name': 'Névoa',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 200 (PDF 206)',
  'pdf_page': 206,
  'stats': 'Execução: padrão; Alcance: curto; Efeito: nuvem com 6m de raio e 6m de altura; Duração: cena.',
  'description': 'Uma névoa espessa eleva-se de um ponto a sua escolha, obscurecendo toda a visão — '
                 'criaturas a até 1,5m têm camuflagem leve e criaturas a partir de 3m têm camuflagem total. '
                 'Um vento forte dispersa a névoa em 4 rodadas e um vendaval a dispersa em 1 rodada. Esta '
                 'magia não funciona sob a água.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: a magia também funciona sob a água, criando uma nuvem de tinta.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: você pode escolher criaturas no alcance ao lançar a magia; elas enxergam '
                            'através do efeito. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: a nuvem tem um cheiro horrível. No início de seus turnos, qualquer '
                            'criatura dentro dela, ou qualquer criatura com faro em alcance curto da nuvem, '
                            'deve fazer um teste de Fortitude. Se falhar, fica enjoada por uma rodada.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: a nuvem tem um tom esverdeado e se torna cáustica. No início de seus '
                            'turnos, criaturas dentro dela sofrem 2d4 pontos de dano de ácido.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+3 PM: aumenta o dano de ácido em +2d4.',
                    'cost': 3,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e6',
                    'text': '+5 PM: além do normal, a nuvem fica espessa, quase sólida. Qualquer criatura '
                            'dentro dela tem seu deslocamento reduzido para 3m (independentemente de seu '
                            'deslocamento normal) e sofre –2 em testes de ataque e rolagens de dano.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'effect': 'nuvem com 6m de raio e 6m de altura',
  'duration': 'cena',
  'id': 'jda:nevoa'},
 {'name': 'Oração',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 200 (PDF 206)',
  'pdf_page': 206,
  'stats': 'Execução: padrão; Alcance: curto; Alvos: todas as criaturas (veja texto); Duração: sustentada.',
  'description': 'Você e os seus aliados no alcance recebem +2 em testes de perícia e rolagens de dano, e '
                 'todos os seus inimigos no alcance sofrem –2 em testes de perícia e rolagens de dano. Esse '
                 'efeito é cumulativo com outras magias. Componente material: T$ 25 por PM gasto em incensos '
                 'ou outras oferendas.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta os bônus em +1 (bônus máximo limitado pelo círculo máximo de '
                            'magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta as penalidades em –1 (penalidade máxima limitada pelo círculo '
                            'máximo de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: muda o alcance para médio. Requer 3º círculo.',
                    'cost': 7,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+12 PM: muda a duração para cena. Requer 4º círculo.',
                    'cost': 12,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': 'todas as criaturas (veja texto)',
  'duration': 'sustentada',
  'id': 'jda:oracao'},
 {'name': 'Orientação',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 200 (PDF 206)',
  'pdf_page': 206,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: 1 rodada.',
  'description': 'Em seu próximo teste de perícia, o alvo pode rolar dois dados e ficar com o melhor '
                 'resultado.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda a duração para cena. Em vez do normal, escolha um atributo. Sempre '
                            'que o alvo fizer um teste de perícia baseado no atributo escolhido, pode rolar '
                            'dois dados e ficar com o melhor resultado. Não se aplica a testes de ataque ou '
                            'resistência. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: como acima, mas, em vez de um atributo, escolha entre atributos físicos '
                            '(Força, Destreza e Constituição) ou mentais (Inteligência, Sabedoria e '
                            'Carisma). Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda o alvo para criaturas escolhidas. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': '1 rodada',
  'id': 'jda:orientacao'},
 {'name': 'Palavra Primordial',
  'tradition': 'Universal',
  'circle': 5,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 200 (PDF 206)',
  'pdf_page': 206,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura com menos níveis que você; Duração: '
           'instantânea ou veja texto; Resistência: Vontade parcial.',
  'description': 'Você pronuncia uma palavra do idioma primordial da Criação, que causa um dos efeitos '
                 'abaixo, a sua escolha.\n'
                 'Atordoar: a criatura fica atordoada por 1d4+1 rodadas (apenas uma vez por cena). Se passar '
                 'no teste de resistência, ou se já foi atordoada por esta magia, fica desprevenida por 1d4 '
                 'rodadas.\n'
                 'Cegar: a criatura fica cega. Se passar no teste de resistência, fica ofuscada por 1d4 '
                 'rodadas.\n'
                 'Matar: a criatura morre. Além do teste de Vontade, a criatura tem direito a um teste de '
                 'Fortitude se tiver mais da metade de seus PV. Se passar em qualquer um deles, em vez de '
                 'morrer perde 10d8 pontos de vida e fica sangrando.',
  'enhancements': [],
  'range': 'curto',
  'target': '1 criatura com menos níveis que você',
  'duration': 'instantânea ou veja texto',
  'id': 'jda:palavra-primordial'},
 {'name': 'Pele de Pedra',
  'tradition': 'Universal',
  'circle': 3,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 201 (PDF 207)',
  'pdf_page': 207,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Sua pele ganha aspecto e dureza de rocha. Você recebe redução de dano 5.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para toque e o alvo para 1 criatura.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: muda a duração para um dia.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+4 PM: sua pele ganha aspecto e dureza de aço. Você recebe redução de dano 10. '
                            'Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+4 PM: muda o alcance para toque, o alvo para 1 criatura, a duração para 1d4 '
                            'rodadas e adiciona Resistência: Fortitude anula. Em vez do efeito normal, a '
                            'magia transforma o alvo e seu equipamento em uma estátua inerte e sem '
                            'consciência. A estátua possui os mesmos PV da criatura e redução de dano 8; se '
                            'for quebrada, a criatura morrerá. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+9 PM: como acima, mas com duração permanente. Requer 5º círculo.',
                    'cost': 9,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:pele-de-pedra'},
 {'name': 'Perdição',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 201 (PDF 207)',
  'pdf_page': 207,
  'stats': 'Execução: padrão; Alcance: curto; Alvos: criaturas escolhidas; Duração: cena; Resistência: '
           'nenhuma.',
  'description': 'Amaldiçoa os alvos, que recebem –1 em testes de ataque e rolagens de dano. Perdição anula '
                 'Bênção.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta as penalidades em –1 (bônus máximo limitado pelo círculo máximo '
                            'de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': 'criaturas escolhidas',
  'duration': 'cena',
  'id': 'jda:perdicao'},
 {'name': 'Poeira da Podridão',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 201 (PDF 207)',
  'pdf_page': 207,
  'stats': 'Execução: padrão; Alcance: médio; Área: nuvem com 6m de raio; Duração: cena; Resistência: '
           'Fortitude (veja texto).',
  'description': 'Você manifesta uma nuvem de poeira carregada de energia negativa, que apodrece lentamente '
                 'as criaturas na área. Ao lançar a magia, e no início de seus turnos, criaturas na área '
                 'sofrem 2d8+8 pontos de dano de trevas (Fortitude reduz à metade). Alvos que falharem no '
                 'teste não podem recuperar PV por uma rodada.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em 1d8+4.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'area': 'nuvem com 6m de raio',
  'duration': 'cena',
  'id': 'jda:poeira-da-podridao'},
 {'name': 'Possessão',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 201 (PDF 207)',
  'pdf_page': 207,
  'stats': 'Execução: padrão; Alcance: longo; Alvo: 1 criatura; Duração: 1 dia; Resistência: Vontade anula.',
  'description': 'Você projeta sua consciência no corpo do alvo. Enquanto possuir uma criatura, você assume '
                 'o controle total do corpo dela. O seu próprio corpo fica inconsciente e a consciência do '
                 'alvo fica inerte. Em termos de jogo, você continua usando a sua ficha, mas com os '
                 'atributos físicos e deslocamento da criatura. Se o alvo passar no teste de resistência, '
                 'sabe que você tentou possuí-lo e fica imune a esta magia por um dia. Caso o corpo da '
                 'criatura morra enquanto você a possui, a criatura morre e você deve fazer um teste de '
                 'Vontade contra a CD da sua própria magia. Se passar, sua consciência retorna para o seu '
                 'corpo (contanto que esteja dentro do alcance). Do contrário, você também morre. Retornar '
                 'para o seu corpo voluntariamente é uma ação livre.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: você ganha acesso às habilidades de raça e classe da criatura.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: enquanto a magia durar e você estiver dentro do alcance do seu corpo '
                            'original, pode “saltar” de uma criatura possuída para outra. O novo alvo tem '
                            'direito a um teste de Vontade. Se falhar, você assume o controle do corpo dele '
                            'e o alvo anterior recobra a consciência.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda a duração para permanente, mas destrói seu corpo original no '
                            'processo. Uma criatura possuída pode fazer um teste de Vontade no começo do dia '
                            'para retomar seu corpo. Se passar, recobra a consciência (e a sua própria '
                            'consciência fica inerte). O teste se repete no início de cada dia. Se o corpo '
                            'de uma criatura possuída morrer e houver outra criatura em alcance curto, você '
                            'pode tentar possuí-la. Enquanto houver novos corpos para possuir, você é '
                            'imortal!',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'target': '1 criatura',
  'duration': '1 dia',
  'id': 'jda:possessao'},
 {'name': 'Potência Divina',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 201 (PDF 207)',
  'pdf_page': 207,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: sustentada.',
  'description': 'Você canaliza o poder de sua divindade. Você aumenta uma categoria de tamanho (seu '
                 'equipamento muda de acordo) e recebe Força +4 e RD 10. Você não pode lançar magias '
                 'enquanto estiver sob efeito de Potência Divina.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o bônus de Força em +1.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: aumenta a RD em +5.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o alcance para toque e o alvo para 1 criatura. A magia falha se '
                            'você e o alvo não forem devotos da mesma divindade.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'sustentada',
  'id': 'jda:potencia-divina'},
 {'name': 'Premonição',
  'tradition': 'Divina',
  'circle': 4,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 201 (PDF 207)',
  'pdf_page': 207,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Vislumbres do futuro permitem que você reavalie suas ações. Uma vez por rodada, você pode '
                 'rolar novamente um teste recém realizado, mas deve aceitar o resultado da nova rolagem.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: muda a execução para reação, o alcance para curto, o alvo para 1 '
                            'criatura e a duração para instantânea. Esta magia só pode ser usada em uma '
                            'criatura que tenha acabado de fazer um teste. Obriga a criatura a fazer uma '
                            'nova rolagem de dados e aceitar o novo resultado, seja ele um sucesso ou falha. '
                            'Criaturas involuntárias têm direito a um teste de Vontade para negar o efeito.',
                    'cost': 3,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+10 PM: muda a duração para um dia.',
                    'cost': 10,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:premonicao'},
 {'name': 'Primor Atlético',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 201 (PDF 207)',
  'pdf_page': 207,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena.',
  'description': 'Você modifica os limites físicos do alvo, que recebe deslocamento +9m e +10 em testes de '
                 'Atletismo.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, o alvo recebe um bônus adicional de +20 em testes de '
                            'Atletismo para saltar (para um bônus total de +30).',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: além do normal, o alvo pode escalar paredes e tetos sem precisar fazer '
                            'testes de Atletismo. Para isso, precisa estar com as mãos livres, mas pode usar '
                            'uma única mão se ficar parado no lugar. O alvo não fica desprevenido enquanto '
                            'escala.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+1 PM: muda a execução para ação de movimento, o alcance para pessoal, o alvo '
                            'para você e a duração para instantânea. Você salta muito alto e pousa em '
                            'alcance corpo a corpo de uma criatura em alcance curto. Se fizer um ataque '
                            'corpo a corpo contra essa criatura neste turno, recebe os benefícios e '
                            'penalidades de uma investida e sua arma causa um dado extra de dano do mesmo '
                            'tipo durante este ataque.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: além do normal, ao fazer testes de perícias baseadas em Força, Destreza '
                            'ou Constituição, o alvo pode rolar dois dados e escolher o melhor. Não afeta '
                            'testes de ataque ou resistência. Requer 2º círculo.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:primor-atletico'},
 {'name': 'Profanar',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 202 (PDF 208)',
  'pdf_page': 208,
  'stats': 'Execução: padrão; Alcance: longo; Área: esfera com 9m de raio; Duração: 1 dia.',
  'description': 'Você enche a área com energia negativa. Dano causado por efeitos de trevas é maximizado '
                 'dentro da área. Isso também afeta PV curados em mortos-vivos por esses efeitos. Esta magia '
                 'não pode ser lançada em uma área contendo um símbolo visível dedicado a uma divindade que '
                 'não a sua. Profanar anula Consagrar.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, mortos-vivos na área recebem +2 na Defesa e +2 em todos '
                            'os testes.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta os bônus para mortos-vivos em +1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+9 PM: muda a execução para 1 hora, a duração para permanente e adiciona '
                            'componente material (incenso e óleos no valor de T$ 1.000). Requer 4º círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'area': 'esfera com 9m de raio',
  'duration': '1 dia',
  'id': 'jda:profanar'},
 {'name': 'Projetar Consciência',
  'tradition': 'Universal',
  'circle': 5,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 202 (PDF 208)',
  'pdf_page': 208,
  'stats': 'Execução: padrão; Alcance: ilimitado (veja texto); Alvo: local ou criatura conhecidos; Duração: '
           'sustentada.',
  'description': 'Esta magia faz com que sua consciência deixe seu corpo e se transporte instantaneamente '
                 'para um local ou para perto de uma criatura alvo. Se escolher um local, ele precisa ser '
                 'conhecido por você. Se escolher uma criatura, você transporta sua consciência até onde a '
                 'criatura estiver, contanto que estejam no mesmo plano.\n'
                 'Você adquire uma forma fantasmagórica invisível, mas pode se mostrar usando uma ação de '
                 'movimento. Pode se mover em qualquer direção com deslocamento de voo 18m e, por ser '
                 'incorpóreo, é capaz de atravessar objetos sólidos, mas fica limitado a se mover dentro dos '
                 'limites do local, ou dentro de alcance curto da criatura alvo. Você pode ver e ouvir como '
                 'se estivesse presente no local e pode falar mentalmente com qualquer criatura que possa '
                 'ver, contanto que tenham um idioma em comum.',
  'enhancements': [{'id': 'e1',
                    'text': '+10 PM: além do normal, sua projeção é capaz de lançar magias que não precisem '
                            'de componentes materiais e tenham duração diferente de sustentada. Sua forma '
                            'fantasmagórica funciona como na magia Forma Etérea, sendo afetada por magias de '
                            'abjuração e essência, mas as magias que ela lança podem afetar criaturas '
                            'corpóreas.',
                    'cost': 10,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'ilimitado (veja texto)',
  'target': 'local ou criatura conhecidos',
  'duration': 'sustentada',
  'id': 'jda:projetar-consciencia'},
 {'name': 'Proteção Contra Magia',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 202 (PDF 208)',
  'pdf_page': 208,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena.',
  'description': 'Você protege o alvo contra efeitos mágicos nocivos. O alvo recebe +5 em testes de '
                 'resistência contra magias.',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: muda o bônus para +10. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: em vez do normal, o alvo fica imune a uma escola de magia a sua escolha. '
                            'Requer 4º Círculo.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+9 PM: em vez do normal, o alvo fica imune a duas escolas de magia a sua '
                            'escolha. Requer 5º Círculo.',
                    'cost': 9,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:protecao-contra-magia'},
 {'name': 'Proteção Divina',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 202 (PDF 208)',
  'pdf_page': 208,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena.',
  'description': 'Esta magia cria uma barreira mística invisível que fornece ao alvo +2 em testes de '
                 'resistência.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o bônus concedido em +1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a execução para reação, o alcance para curto e a duração para 1 '
                            'rodada. Em vez do normal, o alvo recebe +5 no próximo teste de resistência que '
                            'fizer (cumulativo com o efeito básico desta magia).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o alvo para área de esfera com 3m de raio. Todos os aliados dentro '
                            'do círculo recebem o bônus da magia. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+5 PM: torna o alvo imune a efeitos mentais e de medo. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:protecao-divina'},
 {'name': 'Purificação',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 202 (PDF 208)',
  'pdf_page': 208,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: instantânea.',
  'description': 'Você purifica a criatura tocada, removendo uma condição dela entre abalado, apavorado, '
                 'alquebrado, atordoado, cego, confuso, debilitado, enjoado, envenenado, esmorecido, '
                 'exausto, fascinado, fatigado, fraco, frustrado, lento, ofuscado, paralisado, pasmo ou '
                 'surdo.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: também recupera todos os PV perdidos por veneno.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: em vez de uma, remove todas as condições listadas.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: também permite que o alvo solte qualquer item amaldiçoado que esteja '
                            'segurando (mas não remove a maldição do item em si).',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+7 PM: também dissipa magias e efeitos prejudiciais de encantamento, '
                            'necromancia e transmutação afetando o alvo. Requer 3º círculo.',
                    'cost': 7,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:purificacao'},
 {'name': 'Queda Suave',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 202 (PDF 208)',
  'pdf_page': 208,
  'stats': 'Execução: reação; Alcance: curto; Alvos: 1 criatura ou objeto Grande ou menor; Duração: até '
           'chegar ao solo ou cena, o que vier primeiro.',
  'description': 'O alvo cai lentamente. A velocidade da queda é reduzida para 18m por rodada — o suficiente '
                 'para não causar dano. Como lançar esta magia é uma reação, você pode lançá-la rápido o '
                 'bastante para salvar a si ou um aliado de quedas inesperadas. Lançada sobre um projétil — '
                 'como uma flecha ou uma rocha largada do alto de um penhasco —, a magia faz com que ele '
                 'cause metade do dano normal, devido à lentidão.\n'
                 'Queda Suave só funciona em criaturas e objetos em queda livre; a magia não vai frear um '
                 'golpe de espada ou o mergulho rasante de um atacante voador.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda o alvo para objeto Minúsculo. Em vez do normal, você pode gastar '
                            'uma ação de movimento para levitar o alvo até 4,5m em qualquer direção.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alvo para até 10 criaturas ou objetos adequados.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta a categoria de tamanho do alvo em uma.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura ou objeto Grande ou menor',
  'duration': 'até chegar ao solo ou cena, o que vier primeiro',
  'id': 'jda:queda-suave'},
 {'name': 'Raio do Enfraquecimento',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 202 (PDF 208)',
  'pdf_page': 208,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: cena; Resistência: Fortitude '
           'parcial.',
  'description': 'Você dispara um raio púrpura que drena as forças do alvo. Se falhar na resistência, o alvo '
                 'fica fatigado. Se passar, fica vulnerável. Note que, como efeitos de magia não acumulam, '
                 'lançar esta magia duas vezes contra o mesmo alvo não irá deixá-lo exausto.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda o alcance para toque e a resistência para Fortitude anula. Em vez '
                            'do normal, sua mão emana um brilho púrpura e, ao tocar o alvo, ele fica '
                            'fatigado.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: em vez do normal, se falhar na resistência o alvo fica exausto. Se '
                            'passar, fica fatigado. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: como acima, mas muda o alvo para criaturas escolhidas. Requer 3º '
                            'círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:raio-do-enfraquecimento'},
 {'name': 'Raio Polar',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 203 (PDF 209)',
  'pdf_page': 209,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 criatura; Duração: instantânea.',
  'description': 'Resistência: Fortitude parcial.\n'
                 'Você dispara um raio azul esbranquiçado de gelo e ar congelante. O alvo sofre 10d8 pontos '
                 'de dano de frio e fica preso em um bloco de gelo (paralisado). Se passar no teste de '
                 'resistência, sofre metade do dano e, em vez de paralisado, fica lento por uma rodada.\n'
                 'É possível quebrar o gelo para libertar uma criatura presa: o bloco tem 20 PV, RD 10 e é '
                 'vulnerável a fogo. Uma criatura presa pode gastar uma ação completa para fazer um teste de '
                 'Atletismo e se libertar do gelo; cada vez que passar no teste causa 10 pontos de dano ao '
                 'bloco, ignorando a RD.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: aumenta o dano em +2d8.',
                    'cost': 3,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: muda o alvo para área de esfera com 6m de raio. Em vez de um raio, você '
                            'dispara uma bola de gelo que explode, causando o efeito da magia em todas as '
                            'criaturas na área.',
                    'cost': 5,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'médio',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:raio-polar'},
 {'name': 'Raio Solar',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 203 (PDF 209)',
  'pdf_page': 209,
  'stats': 'Execução: padrão; Alcance: médio; Área: linha; Duração: instantânea; Resistência: Reflexos (veja '
           'texto).',
  'description': 'Você canaliza uma poderosa rajada de energia positiva que ilumina o campo de batalha. '
                 'Criaturas na área sofrem 4d8 pontos de dano de luz (ou 4d12, se forem mortos-vivos) e '
                 'ficam ofuscadas por uma rodada. Se passarem na resistência, sofrem metade do dano e não '
                 'ficam ofuscadas.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda a duração para cena e a resistência para nenhuma. Em vez do '
                            'normal, cria um facho de luz que ilumina a área da magia. Uma vez por rodada, '
                            'você pode mudar a direção do facho como uma ação livre.',
                    'cost': 0,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano ou cura em +1d8 (ou +1d12 em mortos-vivos).',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: em vez do normal, criaturas vivas a sua escolha na área curam 4d8 pontos '
                            'de vida; o restante sofre o dano normalmente.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: criaturas que falhem na resistência ficam cegas por 1d4 rodadas.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'area': 'linha',
  'duration': 'instantânea',
  'id': 'jda:raio-solar'},
 {'name': 'Reanimação Impura',
  'tradition': 'Divina',
  'circle': 5,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 203 (PDF 209)',
  'pdf_page': 209,
  'stats': 'Execução: completa; Alcance: toque; Alvo: 1 criatura; Duração: cena.',
  'description': 'Você reanima uma criatura morta recentemente (dentro da mesma cena), trazendo sua alma de '
                 'volta ao corpo de forma forçada. O tipo da criatura muda para morto-vivo, mas ela retém '
                 'suas memórias e habilidades de quando estava viva, podendo inclusive lançar magias. A '
                 'criatura pode pensar e falar livremente, mas obedece cegamente a seus comandos. Quando a '
                 'cena termina, a criatura volta a ficar morta, mas muitos clérigos malignos usam meios para '
                 'guardar e preservar o corpo de criaturas poderosas para serem reanimadas dessa forma '
                 'quando necessário. Se for destruída, a criatura não pode ser reanimada novamente com esta '
                 'magia.',
  'enhancements': [],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:reanimacao-impura'},
 {'name': 'Refúgio',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 203 (PDF 209)',
  'pdf_page': 209,
  'stats': 'Execução: completa; Alcance: curto; Efeito: domo com 6m de raio; Duração: 1 dia.',
  'description': 'Esta magia cria um domo imóvel e quase opaco por fora, mas transparente pelo lado de '
                 'dentro. Ele protege contra calor, frio e forças pequenas, mas não contra qualquer coisa '
                 'capaz de causar dano. Assim, o domo protege contra neve e vento comuns, mas não contra uma '
                 'flecha ou Bola de Fogo. Porém, como o domo é quase opaco, qualquer criatura dentro dele '
                 'tem camuflagem total contra ataques vindos de fora. Criaturas podem entrar e sair do domo '
                 'livremente. Descansar dentro do Refúgio concede recuperação normal de PV e PM.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, os limites do domo são envoltos por uma fumaça escura e '
                            'espessa, que impede criaturas do lado de fora de enxergar ou ouvir o que está '
                            'dentro. Criaturas do lado de dentro enxergam e ouvem normalmente o que está do '
                            'lado de fora. A fumaça também bloqueia magias de adivinhação.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: em vez do normal, cria uma cabana que comporta até 10 criaturas Médias. '
                            'Descansar nesse espaço concede recuperação confortável (recupera PV e PM igual '
                            'ao dobro do nível). Para todos os efeitos é uma cabana normal, com paredes de '
                            'madeira, telhado, uma porta, duas janelas e alguma mobília (camas, uma mesa com '
                            'bancos e uma lareira). A porta e as janelas têm 15 PV, RD 5 e são protegidas '
                            'por um efeito idêntico à magia Tranca Arcana. As paredes têm 200 PV e RD 5.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: em vez do normal, cria um espaço extradimensional, similar a uma caverna '
                            'vazia e escura, que comporta até 10 criaturas Médias. A entrada para o espaço '
                            'precisa estar desenhada em um objeto fixo como uma grande pedra ou árvore. '
                            'Qualquer criatura que atravesse a entrada consegue entrar no espaço. Nenhum '
                            'efeito a partir do mundo real afeta o espaço e vice-versa, mas aqueles que '
                            'estiverem dentro podem observar o mundo real como se uma janela de 1m estivesse '
                            'centrada na entrada. Qualquer coisa que esteja no espaço extradimensional surge '
                            'no mundo real na área vazia mais próxima da entrada quando a duração da magia '
                            'acaba. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+9 PM: em vez do normal, cria uma mansão extradimensional que comporta até 100 '
                            'criaturas Médias, com quartos luxuosos, comida e bebida e dez servos '
                            'fantasmagóricos (como na magia Servos Invisíveis). Descansar na mansão concede '
                            'recuperação luxuosa (recupera PV e PM igual ao triplo do nível). A mansão tem '
                            'uma única entrada, uma porta feita de luz. Você pode deixá-la visível ou '
                            'invisível como uma ação livre e apenas criaturas escolhidas por você podem '
                            'passar. Requer 4º círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'curto',
  'effect': 'domo com 6m de raio',
  'duration': '1 dia',
  'id': 'jda:refugio'},
 {'name': 'Relâmpago',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 203 (PDF 209)',
  'pdf_page': 209,
  'stats': 'Execução: padrão; Alcance: médio; Área: linha; Duração: instantânea; Resistência: Reflexos reduz '
           'à metade.',
  'description': 'Você dispara um poderoso raio que causa 6d6 pontos de dano de eletricidade em todas as '
                 'criaturas e objetos livres na área.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em +2d6.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda a área para alvo (criaturas escolhidas). Em vez do normal, você '
                            'dispara vários relâmpagos, um para cada alvo escolhido, causando 6d6 pontos de '
                            'dano de eletricidade. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'médio',
  'area': 'linha',
  'duration': 'instantânea',
  'id': 'jda:relampago'},
 {'name': 'Relâmpago Flamejante de Reynard',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 203 (PDF 209)',
  'pdf_page': 209,
  'stats': 'Execução: duas rodadas; Alcance: médio; Efeito: bolas de fogo e relâmpagos; Duração: sustentada; '
           'Resistência: Reflexos reduz à metade.',
  'description': 'Esta é uma magia poderosa, desenvolvida pelo metódico e impassível arquimago Reynard. Você '
                 'invoca as energias elementais do fogo e do relâmpago, fazendo com que uma de suas mãos '
                 'fi-\n'
                 'que em chamas e a outra mão eletrificada. Pela duração da magia, você pode gastar uma ação '
                 'de movimento para disparar uma bola de fogo (10d6 pontos de dano de fogo numa esfera com '
                 '6m de raio) ou um relâmpago (10d6 pontos de dano de eletricidade numa linha). Você também '
                 'pode, como uma ação padrão, usar as duas mãos num ataque de energia mista (20d12 pontos de '
                 'dano, metade de fogo e metade de eletricidade, numa esfera com 9m de raio). Você precisa '
                 'estar com as duas mãos livres para invocar o efeito misto e isso consome toda a energia da '
                 'magia, terminando-a imediatamente. Por se tratar de um ritual complexo, o tempo de '
                 'execução dessa magia não pode ser reduzido.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano das rajadas em +1d6 e o dano da rajada mista em +2d12.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'effect': 'bolas de fogo e relâmpagos',
  'duration': 'sustentada',
  'id': 'jda:relampago-flamejante-de-reynard'},
 {'name': 'Réquiem',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 204 (PDF 210)',
  'pdf_page': 210,
  'stats': 'Execução: completa; Alcance: curto; Alvo: criaturas escolhidas; Duração: sustentada; '
           'Resistência: Vontade anula.',
  'description': 'Esta magia cria uma ilusão particular para cada uma das criaturas que atingir. Enquanto a '
                 'magia durar, no início de cada um de seus turnos, cada criatura afetada deve fazer um '
                 'teste de Vontade; se falhar, acha que não tomou as ações que realmente fez no turno '
                 'anterior e é obrigada a repetir as mesmas ações neste turno, com uma penalidade cumulativa '
                 'de –5 em todos os testes para cada vez que se repetir (a penalidade não se aplica ao teste '
                 'de Vontade contra esta magia). Por exemplo, se a criatura se aproximou de um alvo e o '
                 'atacou, precisa se aproximar desse mesmo alvo e atacar novamente. A ação repetida consome '
                 'PM e recursos normalmente e, caso exija um teste de resistência, qualquer alvo faz esse '
                 'teste com um bônus igual ao da penalidade desta magia.',
  'enhancements': [],
  'range': 'curto',
  'target': 'criaturas escolhidas',
  'duration': 'sustentada',
  'id': 'jda:requiem'},
 {'name': 'Resistência a Energia',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 204 (PDF 210)',
  'pdf_page': 210,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena.',
  'description': 'Ao lançar esta magia, escolha entre ácido, eletricidade, fogo, frio, luz ou trevas. O alvo '
                 'recebe redução de dano 10 contra o tipo de dano escolhido.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta a redução de dano em +5.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a duração para um dia. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda o alcance para curto e o alvo para criaturas escolhidas. Requer 3º '
                            'círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+5 PM: muda o efeito para redução de dano contra todos os tipos listados na '
                            'magia. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+9 PM: muda o efeito para imunidade a um tipo listado na magia. Requer 4º '
                            'círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:resistencia-a-energia'},
 {'name': 'Rogar Maldição',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 204 (PDF 210)',
  'pdf_page': 210,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: sustentada; Resistência: Fortitude '
           'anula.',
  'description': 'Você entoa cânticos maléficos que amaldiçoam uma vítima, criando efeitos variados. Ao '
                 'lançar a magia, escolha entre os seguintes.\n'
                 'Debilidade: o alvo fica esmorecido e não pode se comunicar ou lançar magias. Ainda '
                 'reconhece seus aliados e pode segui-los e ajudá-los, mas sempre de maneira simplória.\n'
                 'Doença: muda a duração para instantânea. O alvo contrai uma doença a sua escolha, que o '
                 'afeta imediatamente (sem período de incubação).\n'
                 'Fraqueza: o alvo fica debilitado e lento.\n'
                 'Isolamento: o alvo perde o uso de um de seus cinco sentidos a sua escolha. Se perder a '
                 'visão, fica cego. Se perder a audição, fica surdo. Se perder o olfato ou paladar, não pode '
                 'usar a habilidade faro. Se perder o tato, fica caído e não pode se levantar.\n'
                 'Você também pode inventar sua própria maldição, usando esses exemplos como sugestões, mas '
                 'o mestre tem a palavra final sobre o efeito.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: aumenta o número de efeitos que você pode escolher em +1. Requer 3º '
                            'círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+7 PM: muda a duração para permanente e resistência para Fortitude parcial. Se '
                            'passar, a criatura ainda sofre os efeitos da maldição, mas por 1 rodada. Requer '
                            '4º círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'sustentada',
  'id': 'jda:rogar-maldicao'},
 {'name': 'Roubar a Alma',
  'tradition': 'Universal',
  'circle': 5,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 204 (PDF 210)',
  'pdf_page': 210,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: permanente; Resistência: Vontade '
           'parcial.',
  'description': 'Você rouba a alma da vítima, armazenando-a em um objeto. Se o alvo passar no teste de '
                 'resistência, sente o\n'
                 'impacto de sua alma ser puxada para fora do corpo e fica abalado por 1 rodada. Se falhar, '
                 'seu corpo fica caído, inconsciente e inerte, enquanto sua alma é transportada para dentro '
                 'do objeto. O corpo não envelhece nem se decompõe, permanecendo em estase. Ele pode ser '
                 'atacado e destruído normalmente. O objeto escolhido deve custar T$ 1.000 por nível ou ND '
                 'da criatura e não possuir uma alma presa ou se quebrará quando a magia for lançada (embora '
                 'personagens não conheçam o conceito de “nível” dentro do mundo de jogo, podem ter noção do '
                 'poder geral de uma criatura, estimando assim o valor do objeto). Se o objeto for '
                 'destruído, a magia se esvai. Se o corpo ainda estiver disponível, a alma retorna para ele. '
                 'Caso contrário, escapa para os Mundos dos Deuses.\n'
                 'Custo adicional: sacrifício de 1 PM.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: o objeto que abriga a alma detém os mesmos PM totais que o alvo. Se '
                            'estiver empunhando o objeto, você pode usar esses PM para lançar magias no '
                            'lugar dos seus. O objeto recupera PM por dia como se o personagem estivesse em '
                            'descanso normal.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+10 PM: como uma reação ao lançar esta magia, você possui o corpo sem alma do '
                            'alvo, como na magia Possessão (mesmo que não conheça a magia).',
                    'cost': 10,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'permanente',
  'id': 'jda:roubar-a-alma'},
 {'name': 'Runa de Proteção',
  'tradition': 'Universal',
  'circle': 2,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 204 (PDF 210)',
  'pdf_page': 210,
  'stats': 'Execução: 1 hora; Alcance: toque; Alvo: uma área de 6m de raio; Duração: permanente até ser '
           'descarregada.',
  'description': 'Resistência: varia (veja o texto).\n'
                 'Você escreve uma runa pessoal em uma superfície fixa, como uma parede ou o chão, que '
                 'protege uma pequena área ao redor. Quando uma criatura entra na área afetada a runa '
                 'explode, causando 6d6 pontos de dano em todos os alvos a até 6m. A criatura que ativa a '
                 'runa não tem direito a teste de resistência; outras criaturas na área têm direito a um '
                 'teste de Reflexos para reduzir o dano à metade. Quando lança a magia, você escolhe o tipo '
                 'de dano, entre ácido, eletricidade, fogo, frio, luz ou trevas.\n'
                 'Você pode determinar que a runa se ative apenas em condições específicas — por exemplo, '
                 'apenas por goblins ou apenas por mortos-vivos. Você tam bém pode criar uma palavra mágica '
                 'que impeça a runa de se ativar.\n'
                 'Um personagem pode encontrar a runa com um teste de Investigação e desar má-la com um '
                 'teste de Ladinagem.\n'
                 'Componente material: pó de diamante no valor de T$ 200, com o qual o conjura dor desenha a '
                 'runa, que brilha por al guns instantes e depois se torna prati camente invisível.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o dano em +2d6.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o alvo para “você” e o alcance para “pessoal”. Ao invés do normal, '
                            'escolha uma magia de 1º círculo que você conhece e pode lançar, com tempo de '
                            'execução de uma ação padrão ou menor. Você escreve a runa em seu corpo e '
                            'especifica uma condição de ativação como, por exemplo, “quando eu for alvo de '
                            'um ataque” ou “quando for alvo de uma magia”. Quando a condição for cumprida, '
                            'você pode ativar a runa e lançar a magia escolhida como uma reação. Você só '
                            'pode escrever uma runa em seu corpo ao mesmo tempo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: como o aprimoramento anterior, mas você pode escolher magias de 2º '
                            'círculo. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'duration': 'permanente até ser descarregada',
  'area': 'uma área de 6m de raio',
  'id': 'jda:runa-de-protecao'},
 {'name': 'Salto Dimensional',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 205 (PDF 211)',
  'pdf_page': 211,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: você; Duração: instantânea.',
  'description': 'Esta magia transporta você para outro lugar dentro do alcance. Você não precisa perceber '
                 'nem ter linha de efeito ao seu destino, podendo simplesmente imaginá-lo. Por exemplo, pode '
                 'se transportar 3m adiante para ultrapassar uma porta fechada. Uma vez transportadas, '
                 'criaturas não podem agir até a rodada seguinte. Esta magia não permite que você apareça '
                 'dentro de um corpo sólido; se o ponto de chegada não tem espaço livre, você ressurge na '
                 'área vazia mais próxima.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para médio.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o alvo para você e uma criatura voluntária. Você pode escolher este '
                            'aprimoramento mais vezes para aumentar o número de alvos adicionais em +1, mas '
                            'deve estar tocando todos os alvos.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda a execução para reação. Em vez do normal, você recebe +5 na Defesa '
                            'e em testes de Reflexos contra um ataque ou efeito que esteja prestes a '
                            'atingi-lo. Após a resolução do efeito, salta para um espaço adjacente (1,5m).',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: muda o alcance para longo.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': 'você',
  'duration': 'instantânea',
  'id': 'jda:salto-dimensional'},
 {'name': 'Santuário',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 205 (PDF 211)',
  'pdf_page': 211,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena; Resistência: Vontade anula.',
  'description': 'Qualquer criatura que tente fazer uma ação hostil contra o alvo deve fazer um teste de '
                 'Vontade. Se falhar, não consegue, perde a ação e não pode tentar novamente até o fim da '
                 'cena. Santuário não protege o alvo de efeitos de área. Além disso, o próprio alvo também '
                 'não pode fazer ações hostis (incluindo forçar outras criaturas a atacá-lo), ou a magia é '
                 'dissipada — mas pode usar habilidades e magias de cura e suporte, como Curar Ferimentos e '
                 'Bênção.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, escolha um tipo de criatura entre animal, construto ou '
                            'morto-vivo. Você não pode ser percebido por criaturas não inteligentes (Int –4 '
                            'ou menor) do tipo escolhido.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+9 PM: também protege o alvo contra efeitos de área. Uma criatura que tente '
                            'atacar uma área que inclua o alvo deve fazer o teste de Vontade; se falhar, não '
                            'consegue e perde a ação. Ela só pode tentar novamente se o alvo sair da área.',
                    'cost': 9,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:santuario'},
 {'name': 'Segunda Chance',
  'tradition': 'Divina',
  'circle': 5,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 205 (PDF 211)',
  'pdf_page': 211,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: instantânea.',
  'description': 'Um brilho de luz, na forma de asas de fênix, emana do alvo. Ele recupera 200 pontos de '
                 'vida e se cura de qualquer das seguintes condições: abalado, apavorado, alquebrado, '
                 'atordoado, cego, confuso, debilitado, enjoado, envenenado, esmorecido, exausto, fascinado, '
                 'fatigado, fraco, frustrado, lento, ofuscado, paralisado, pasmo ou surdo.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta a cura em +20 PV.',
                    'cost': 1,
                    'min_circle': 5,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alcance para curto e o alvo para até 5 criaturas.',
                    'cost': 2,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda o alvo para uma criatura que tenha morrido há até uma rodada. Esta '
                            'magia pode curá-la.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:segunda-chance'},
 {'name': 'Selo de Mana',
  'tradition': 'Universal',
  'circle': 3,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 205 (PDF 211)',
  'pdf_page': 211,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: cena; Resistência: Vontade parcial.',
  'description': 'Seu toque manifesta um selo mágico na pele do alvo, que atrapalha o fluxo de mana. Pela '
                 'duração da magia, sempre que o alvo realizar qualquer ação que gaste PM, deve fazer um '
                 'teste de Vontade; se passar, faz a ação normal-\n'
                 'mente. Se falhar, a ação não tem efeito (mas os PM são gastos mesmo assim).',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: muda o alcance para curto e o alvo para criaturas escolhidas dentro do '
                            'alcance. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:selo-de-mana'},
 {'name': 'Semiplano',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 205 (PDF 211)',
  'pdf_page': 211,
  'stats': 'Execução: completa; Alcance: curto; Efeito: semiplano com 30m de lado; Duração: 1 dia.',
  'description': 'Você cria uma dimensão particular. Você pode entrar no semiplano gastando uma ação padrão '
                 'e 10 PM, desaparecendo do plano material como se tivesse se teletransportado. Você pode '
                 'levar criaturas voluntárias que esteja tocando, ao custo de 1 PM por criatura extra. Você '
                 'também pode levar objetos que esteja tocando, ao custo de 1 PM por objeto Médio ou menor, '
                 '2 PM por objeto Grande, 5 PM por Enorme e 10 PM por Colossal. Uma vez no semiplano, pode '
                 'gastar uma ação completa para voltar ao plano material, no mesmo local onde estava. Caso '
                 'conheça a magia Viagem Planar, pode lançá-la para voltar ao plano material em outro '
                 'local.\n'
                 'Você escolhe a forma e a aparência do semiplano — uma caverna, um asteroide que singra o '
                 'éter, um palacete de cristal etc. Ele contém ar, luz e calor, mas além disso é vazio. '
                 'Entretanto, você pode levar itens (mobília, ferramentas etc.) a cada viagem.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: adiciona alvo (1 criatura). Você cria uma semiplano labiríntico e '
                            'expulsa o alvo para ele. A cada rodada, a vítima tem direito a um teste de '
                            'Investigação ou Sobrevivência, com bônus cumulativo de +1 para cada teste já '
                            'realizado, para escapar do labirinto. Quando o alvo escapa, a magia termina e o '
                            'alvo reaparece no plano material no mesmo local onde estava quando a magia foi '
                            'lançada. Magias como Salto Dimensional e Teletransporte não ajudam a escapar do '
                            'labirinto, mas Viagem Planar, sim.',
                    'cost': 2,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: muda a duração para permanente e adiciona componente material (maquete '
                            'do semiplano feita de materiais preciosos no valor de T$ 5.000). Você pode '
                            'lançar a magia diversas vezes para aumentar as dimensões do semiplano em +30m '
                            'de lado a cada vez.',
                    'cost': 5,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'effect': 'semiplano com 30m de lado',
  'duration': '1 dia',
  'id': 'jda:semiplano'},
 {'name': 'Servo Divino',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 205 (PDF 211)',
  'pdf_page': 211,
  'stats': 'Execução: padrão; Alcance: curto; Efeito: criatura conjurada; Duração: cena ou até ser '
           'descarregada.',
  'description': 'Você pede a sua divindade que envie um espírito para ajudá-lo. Esse espírito realiza uma '
                 'tarefa a sua escolha que possa ser cumprida em até uma hora — desde algo simples como “use '
                 'suas asas para nos levar até o topo da montanha” até algo complexo como “escolte esses '
                 'camponeses até o castelo”. A magia é descarregada quando a criatura cumpre a tarefa, '
                 'retornando a seu plano natal. O tipo de criatura é escolhido pelo mestre, de acordo com as '
                 'necessidades da tarefa.\n'
                 'Componente material: um pagamento de T$ 100 ao espírito. A forma de pagamento varia — '
                 'doações a um templo, um item mágico ou mesmo dinheiro.',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: muda a duração para um dia ou até ser descarregada. O espírito realiza '
                            'uma tarefa a sua escolha que exija até um dia. O custo do pagamento aumenta '
                            'para T$ 500. O resto segue normal.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+9 PM: muda a duração para 1 semana ou até ser descarregada. O espírito realiza '
                            'uma tarefa que exija até uma semana. O custo do pagamento aumenta para T$ '
                            '1.000. O resto segue normal.',
                    'cost': 9,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'effect': 'criatura conjurada',
  'duration': 'cena ou até ser descarregada',
  'id': 'jda:servo-divino'},
 {'name': 'Servo Morto-Vivo',
  'tradition': 'Universal',
  'circle': 3,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 206 (PDF 212)',
  'pdf_page': 212,
  'stats': 'Execução: completa; Alcance: toque; Alvo: 1 cadáver; Duração: instantânea.',
  'description': 'Esta magia transforma o cadáver de um humanoide, animal ou monstro em um esqueleto ou '
                 'zumbi (conforme o estado de conservação do corpo). O morto-vivo então obedece a todos os '
                 'seus comandos, mesmo suicidas. Se quiser que o morto-vivo o acompanhe, ele funciona como '
                 'um parceiro iniciante, de um tipo a sua escolha entre ajudante, atirador, combatente, '
                 'fortão, guardião ou montaria.\n'
                 'Uma vez por rodada, quando sofre dano, você pode sacrificar um servo morto-vivo e evitar '
                 'esse dano. O servo é destruído no processo e não pode ser reanimado\n'
                 'Componente material: um ônix negro (T$ 100), inserido na boca ou olho do cadáver.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: muda o componente material para pó de ônix negro (T$ 500). Em vez de um '
                            'zumbi ou esqueleto, cria um carniçal. Ele pode funcionar como um parceiro '
                            'veterano, escolhido entre ajudante, atirador, combatente, fortão ou guardião. O '
                            'resto segue normal.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda o componente material para pó de ônix negro (T$ 500). Em vez de um '
                            'zumbi ou esqueleto, cria uma sombra. Ela pode funcionar como um parceiro '
                            'veterano, escolhido entre assassino, combatente ou perseguidor. O restante da '
                            'magia segue normal.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: muda o componente material para ferramentas de embalsamar (T$ 1.000). Em '
                            'vez de um zumbi ou esqueleto, cria uma múmia. Ela pode funcionar como um '
                            'parceiro mestre, escolhido entre ajudante, destruidor, guardião ou médico. O '
                            'restante da magia segue normal. Requer 4º círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 cadáver',
  'duration': 'instantânea',
  'id': 'jda:servo-morto-vivo'},
 {'name': 'Servos Invisíveis',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 206 (PDF 212)',
  'pdf_page': 212,
  'stats': 'Execução: padrão; Alcance: longo; Efeito: criaturas conjuradas; Duração: 1 cena.',
  'description': 'Você cria até três servos invisíveis e silenciosos, capazes de realizar tarefas simples '
                 'como apanhar lenha, colher frutos, varrer o chão ou alimentar um cavalo. Os servos podem '
                 'ser usados para manter arrumada e organizada uma mansão ou pequena torre ou para preparar '
                 'um acampamento nos ermos para você e seus aliados (veja a perícia Sobrevivência, na página '
                 '123).\n'
                 'Eles também podem ajudá-lo em tarefas mais complexas, como fazer uma pesquisa ou preparar '
                 'uma poção, mas isso consome sua energia mágica. Você pode “gastar” um servo para receber '
                 'um bônus não cumulativo de +2 em um teste de perícia (exceto testes de ataque e '
                 'resistência). Os servos não são criaturas reais; não podem lutar, nem resistir a qualquer '
                 'dano ou efeito que exija um teste de resistência ou teste oposto — falharão '
                 'automaticamente no teste e serão destruídos.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de servos conjurados em 1.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: você pode comandar os servos para realizar uma única tarefa no seu '
                            'lugar. Em termos de jogo, eles passam automaticamente em um teste de perícia '
                            'com CD máxima igual ao seu nível, +2 para cada servo conjurado. O tempo '
                            'necessário para realizar a tarefa é o tempo do uso da perícia em questão. '
                            'Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'effect': 'criaturas conjuradas',
  'duration': '1 cena',
  'id': 'jda:servos-invisiveis'},
 {'name': 'Seta Infalível de Talude',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 206 (PDF 212)',
  'pdf_page': 212,
  'stats': 'Execução: padrão; Alcance: médio; Alvos: criaturas escolhidas; Duração: instantânea.',
  'description': 'Favorita entre arcanistas iniciantes, esta magia lança duas setas de energia\n'
                 'que causam 1d4+1 pontos de dano de essência cada. Você pode lançar as setas em alvos '
                 'diferentes ou concentrá-las num mesmo alvo. Caso você possua um bônus no dano de magias, '
                 'como pelo poder Arcano de Batalha, ele é aplicado em apenas uma seta (o bônus vale para a '
                 'magia, não cada alvo).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda as setas para lanças de energia que surgem e caem do céu. Cada '
                            'lança causa 1d8+1 pontos de dano de essência. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o número de setas/lanças para três.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+4 PM: muda o número de setas/lanças para cinco. Requer 2º círculo.',
                    'cost': 4,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+9 PM: muda o número de setas/lanças para dez. Requer 4º círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'target': 'criaturas escolhidas',
  'duration': 'instantânea',
  'id': 'jda:seta-infalivel-de-talude'},
 {'name': 'Silêncio',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 206 (PDF 212)',
  'pdf_page': 212,
  'stats': 'Execução: padrão; Alcance: médio; Área: esfera com 6m de raio; Duração: sustentada.',
  'description': 'Um silêncio sepulcral recai sobre a área e nenhum som é produzido nela. Enquanto estiverem '
                 'na área, todas as criaturas ficam surdas. Além disso, como lançar magias exige palavras '
                 'mágicas, normalmente nenhuma magia pode ser lançada dentro da área.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda a área para alvo de 1 objeto. Em vez do normal, o alvo emana uma '
                            'área de silêncio com 3m de raio. Se lançar a magia num objeto de uma criatura '
                            'involuntária, ela tem direito a um teste de Vontade para anulá-la.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a duração para cena. Em vez do normal, nenhum som pode deixar a '
                            'área, mas criaturas dentro da área podem falar, ouvir e lançar magias com '
                            'palavras mágicas normalmente.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'médio',
  'area': 'esfera com 6m de raio',
  'duration': 'sustentada',
  'id': 'jda:silencio'},
 {'name': 'Soco de Arsenal',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 206 (PDF 212)',
  'pdf_page': 212,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 criatura; Duração: instantânea; Resistência: Fortitude '
           'parcial.',
  'description': 'Ninguém sabe se Mestre Arsenal foi realmente o criador desta magia — mas ele foi o '
                 'primeiro a utilizá-la. Você fecha o punho e gesticula como se estivesse golpeando o alvo, '
                 'causando dano de impacto igual a 4d6 + sua Força. A vítima é empurrada 3m na direção '
                 'oposta à sua. Passar no teste de resistência reduz o dano à metade e evita o empurrão.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para pessoal, o alvo para você, a duração para cena e a '
                            'resistência para nenhuma. Em vez do normal, seus ataques corpo a corpo passam a '
                            'acertar inimigos distantes. Seu alcance natural aumenta em 3m; uma criatura '
                            'Média pode atacar adversários a até 4,5m, por exemplo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano em +1d6.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+4 PM: aumenta o empurrão em +3m.',
                    'cost': 4,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+5 PM: muda o tipo do dano para essência.',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:soco-de-arsenal'},
 {'name': 'Sombra Assassina',
  'tradition': 'Arcana',
  'circle': 5,
  'school': 'Ilusão',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 207 (PDF 213)',
  'pdf_page': 213,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: cena; Resistência: Vontade parcial.',
  'description': 'Esta magia cria uma duplicata ilusória do alvo na forma de uma silhueta, ligada a ele como '
                 'se fosse uma manifestação sólida de sua própria sombra. A duplicata de sombras segue '
                 'automaticamente o alvo. Sempre que o alvo faz uma ação hostil — fazer um ataque, usar uma '
                 'habilidade, lançar uma magia — a sombra imediatamente realiza a mesma ação contra o alvo, '
                 'usando as mesmas estatísticas e rolagens. A sombra pode ser atacada, tem as mesmas '
                 'estatísticas do alvo e é destruída quando chega a 0 PV. Se o alvo passar no teste de '
                 'resistência, a sombra desaparece no final do turno do alvo, depois de copiar sua ação '
                 'dessa rodada.',
  'enhancements': [{'id': 'e1',
                    'text': '+10 PM: muda o alvo para criaturas escolhidas na área.',
                    'cost': 10,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'jda:sombra-assassina'},
 {'name': 'Sonho',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 207 (PDF 213)',
  'pdf_page': 213,
  'stats': 'Execução: 10 minutos; Alcance: ilimitado; Alvo: 1 criatura viva; Duração: veja texto.',
  'description': 'Você entra nos sonhos de uma criatura. Uma vez lá, pode conversar com ela até que ela '
                 'acorde. Se o alvo não estiver dormindo quando você lançar a magia, você pode permanecer em '
                 'transe até que ele adormeça. Durante o transe, você fica indefeso e sem consciência dos '
                 'arredores. Você pode sair do transe quando quiser, mas a magia termina.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: transforma o sonho do alvo em um pesadelo. A vítima deve fazer um teste '
                            'de Vontade. Se falhar, não recupera PV ou PM pela noite, sofre 1d10 pontos de '
                            'dano de trevas e acorda fatigada. A vítima recebe bônus ou penalidades em seu '
                            'teste de resistência, dependendo do conhecimento que você tiver dela. Use os '
                            'mesmos modificadores da magia Vidência.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: aumenta o número de alvos em +1. Todos os alvos compartilham um mesmo '
                            'sonho (ou pesadelo) entre si e com você.',
                    'cost': 1,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'ilimitado',
  'target': '1 criatura viva',
  'duration': 'veja texto',
  'id': 'jda:sonho'},
 {'name': 'Sono',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 207 (PDF 213)',
  'pdf_page': 213,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 humanoide; Duração: cena; Resistência: Vontade '
           'parcial.',
  'description': 'Um cansaço místico recai sobre o alvo. Se falhar na resistência, ele fica inconsciente e '
                 'caído ou, se estiver envolvido em combate ou outra situação perigosa, fica exausto por 1 '
                 'rodada, depois fatigado. Em ambos os casos, se passar, o alvo fica fatigado por 1d4 '
                 'rodadas.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: alvos que falhem na resistência ficam exaustos por 1d4+1 rodadas, em vez '
                            'de apenas 1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alvo para criatura.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: afeta todos os alvos válidos a sua escolha dentro do alcance.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 humanoide',
  'duration': 'cena',
  'id': 'jda:sono'},
 {'name': 'Sopro da Salvação',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 207 (PDF 213)',
  'pdf_page': 213,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: cone de 9m; Duração: instantânea.',
  'description': 'Você enche seus pulmões de luz e energia positiva e sopra um cone de poeira reluzente. O '
                 'sopro afeta apenas seus aliados na área, curando 2d8+4 pontos de vida e removendo uma das '
                 'seguintes condições de todos os alvos: abalado, atordoado, apavorado, alquebrado, cego, '
                 'confuso, debilitado, enfeitiçado, enjoado, esmorecido, exausto, fascinado, fatigado, '
                 'fraco, frustrado, lento, paralisado, pasmo e surdo.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta a cura em +1d8+2.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: além do normal, se um aliado estiver com PV negativos, seus PV são '
                            'levados a 0 e então a cura é aplicada.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+4 PM: remove todas as condições listadas, em vez de apenas uma.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'cone de 9m',
  'duration': 'instantânea',
  'id': 'jda:sopro-da-salvacao'},
 {'name': 'Sopro das Uivantes',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 207 (PDF 213)',
  'pdf_page': 213,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: cone de 9m; Duração: instantânea; Resistência: '
           'Fortitude parcial.',
  'description': 'Você sopra ar gélido que causa 4d6 pontos de dano de frio (Fortitude reduz à metade). '
                 'Criaturas de tamanho Médio ou menor que falhem na resistência ficam caídas e são '
                 'empurradas 6m na direção oposta. Se houver uma parede ou outro objeto sólido (mas\n'
                 'não uma criatura) no caminho, a criatura para de se mover, mas sofre +2d6 pontos de dano '
                 'de impacto.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano de frio em +2d6.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: aumenta o tamanho máximo das criaturas afetadas em uma categoria. Requer '
                            '3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'cone de 9m',
  'duration': 'instantânea',
  'id': 'jda:sopro-das-uivantes'},
 {'name': 'Suporte Ambiental',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 207 (PDF 213)',
  'pdf_page': 213,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: 1 dia.',
  'description': 'Esta magia facilita a sobrevivência em ambientes hostis. O alvo fica imune aos efeitos de '
                 'calor e frio extremos, pode respirar na água se respirar ar (ou vice-versa) e não sufoca '
                 'em fumaça densa.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: muda o alcance para curto e o alvo para criaturas escolhidas.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': '1 dia',
  'id': 'jda:suporte-ambiental'},
 {'name': 'Sussurros Insanos',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 207 (PDF 213)',
  'pdf_page': 213,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 humanoide; Duração: cena; Resistência: Vontade anula.',
  'description': 'Você murmura palavras desconexas que afetam a mente do alvo. O alvo fica confuso.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de alvos em +1.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda o alvo para 1 criatura.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+12 PM: muda o alvo para criaturas escolhidas. Requer 5º círculo.',
                    'cost': 12,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 humanoide',
  'duration': 'cena',
  'id': 'jda:sussurros-insanos'},
 {'name': 'Talho Invisível de Edauros',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 207 (PDF 213)',
  'pdf_page': 213,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: cone de 9m; Duração: instantânea; Resistência: '
           'Fortitude parcial.',
  'description': 'Esta magia cruel foi desenvolvida pelo mago de combate Edauros, quando ainda era um '
                 'bípede. Você faz um gesto rápido e dispara uma lâmina de ar em alta velocidade. Criaturas '
                 'na área sofrem 10d8 pontos de dano de corte e ficam sangrando. Alvos que passem no teste '
                 'de resistência sofrem metade do dano e não ficam sangrando.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em +2d8.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alvo para você, a duração para sustentada e o efeito para uma vez '
                            'por rodada, como uma ação de movimento, você pode disparar uma lâmina de ar '
                            'contra um alvo em alcance médio, causando 6d8 pontos de dano de corte '
                            '(Fortitude reduz à metade).',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'cone de 9m',
  'duration': 'instantânea',
  'id': 'jda:talho-invisivel-de-edauros'},
 {'name': 'Teia',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 208 (PDF 214)',
  'pdf_page': 214,
  'stats': 'Execução: padrão; Alcance: curto; Área: cubo com 6m de lado; Duração: cena; Resistência: '
           'Reflexos anula.',
  'description': 'Teia cria várias camadas de fibras entrelaçadas e pegajosas na área. Qualquer criatura na '
                 'área que falhar na resistência fica enredada. Uma vítima pode se libertar com uma ação '
                 'padrão e um teste de Acrobacia ou Atletismo. A área ocupada por Teia é terreno difícil.\n'
                 'A Teia é inflamável. Qualquer ataque que cause dano de fogo destrói as teias por onde '
                 'passar, libertando as criaturas enredadas mas deixando-as em chamas.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, criaturas que falhem na resistência também ficam '
                            'imóveis.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: além do normal, no início de seus turnos a magia afeta novamente '
                            'qualquer criatura na área, exigindo um novo teste de Reflexos. Requer 2º '
                            'círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta a área em +1 cubo de 1,5m.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'area': 'cubo com 6m de lado',
  'duration': 'cena',
  'id': 'jda:teia'},
 {'name': 'Telecinesia',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 208 (PDF 214)',
  'pdf_page': 214,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: veja texto; Duração: sustentada ou instantânea (veja '
           'texto).',
  'description': 'Você move objetos ou criaturas se concentrando. Ao lançar a magia, escolha uma das opções '
                 'a seguir.\n'
                 'Força Contínua: você move uma criatura Média ou menor, ou objeto de até 10 espaços, a até '
                 '6m por rodada. Uma criatura pode anular o efeito sobre ela, ou sobre um objeto que possua, '
                 'passando num teste de Vontade. O alvo pode ser movido em qualquer direção dentro do '
                 'alcance. Ele cai no chão se sair do alcance ou a magia terminar. Duração: sustentada.\n'
                 'Empurrão Violento: nesta versão a energia mágica é expelida de uma única vez e arremessa '
                 'até 10 objetos (no máximo 10 espaços). Os objetos devem estar a até 3m uns dos outros e '
                 'podem ser arremessados até o alcance da magia.\n'
                 'Objetos arremessados podem atingir criaturas em seu caminho, causando de 1 ponto de dano '
                 'de impacto por espaço (objetos macios, sem pontas ou sem fio) até 1d6 pontos de dano por '
                 'espaço (objetos duros, pontudos ou afiados). Criaturas atingidas têm direito a um teste de '
                 'Reflexos para reduzir o dano à metade.\n'
                 'Criaturas Médias ou menores podem ser arremessadas, mas têm direito a um teste de Vontade '
                 'para evitar o efeito (em si mesmas ou em objetos que estejam segurando). Uma criatura '
                 'arremessada contra uma superfície sólida sofre 1d6 pontos de dano de impacto para cada 3m '
                 'que “voou” no deslocamento (incluindo outras criaturas; nesse caso, ambas sofrem o dano). '
                 'Duração: instantânea.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: aumenta o tamanho máximo da criatura em uma categoria (para Grande, '
                            'Enorme e Colossal) ou dobra a quantidade de espaços do objeto.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'target': 'veja texto',
  'duration': 'sustentada ou instantânea (veja texto)',
  'id': 'jda:telecinesia'},
 {'name': 'Teletransporte',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 208 (PDF 214)',
  'pdf_page': 214,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: até 5 criaturas voluntárias; Duração: instantânea.',
  'description': 'Esta magia transporta os alvos para um lugar a sua escolha a até 1.000km. Você precisa '
                 'fazer um teste de Misticismo, com dificuldade que depende de seu conhecimento sobre o '
                 'local de destino.\n'
                 'CD 20. Um lugar familiar, que você visita com frequência.\n'
                 'CD 30. Um lugar conhecido, que você já visitou pelo menos uma vez.\n'
                 'CD 40. Um lugar que você nunca visitou e só conhece a partir da descrição de outra pessoa '
                 'que esteve lá.\n'
                 'Você não pode se teletransportar para um lugar que nunca visitou sem a descrição de '
                 'alguém. Ou seja, não pode se transportar para a “sala de tesouro do rei” se nunca esteve '
                 'nela nem falou com alguém que esteve.\n'
                 'Se passar no teste, os alvos chegam ao lugar desejado. Se falhar, os alvos surgem 1d10 x '
                 '10km afastados em qualquer direção (se o destino é uma cidade costeira, você pode surgir '
                 'em alto-mar). Se falhar por 5 ou mais, você chega em um lugar parecido, mas errado. E se '
                 'você rolar 1 natural no teste a magia falha (mas você gasta os PM) e fica atordoado por '
                 '1d4 rodadas.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de alvos em +5.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: em vez do normal, a magia teletransporta os alvos para seu santuário — '
                            'um local familiar e previamente preparado. A magia pode ser usada sem limite de '
                            'distância ou necessidade de testes, mas apenas dentro do mesmo plano. Preparar '
                            'um local como seu santuário exige um ritual de um dia e o gasto de T$ 1.000. '
                            'Você só pode ter um santuário por vez.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+9 PM: muda a execução para ação completa, a duração para cena e adiciona '
                            'sacrifício de 1 PM. Em vez do normal, você cria um círculo de 1,5m de diâmetro '
                            'no chão, que transporta qualquer criatura que pisar nele. O destino é escolhido '
                            'quando a magia é lançada e pode ser qualquer lugar, em qualquer mundo, sem a '
                            'necessidade de testes, desde que seja conhecido por você. O círculo é tênue e '
                            'praticamente invisível. Você pode marcá-lo de alguma forma (por exemplo, '
                            'lançando-o sobre uma plataforma elevada). Se não fizer isso, alguém pode pisar '
                            'nele por acidente. Junte isso a um destino hostil e você terá uma armadilha '
                            'bastante eficaz! Requer 5º círculo.',
                    'cost': 9,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': 'até 5 criaturas voluntárias',
  'duration': 'instantânea',
  'id': 'jda:teletransporte'},
 {'name': 'Tempestade Divina',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 208 (PDF 214)',
  'pdf_page': 214,
  'stats': 'Execução: completa; Alcance: longo; Área: cilindro com 15m de raio e 15m de altura; Duração: '
           'sustentada.',
  'description': 'Esta magia só pode ser usada em ambientes abertos. A área fica sujeita a um vendaval — '
                 'ataques à distância sofrem penalidade de –5, chamas são apagadas e névoas são dissipadas. '
                 'Você também pode gerar chuva (–5 em testes de Percepção), neve (como chuva, e a área se '
                 'torna terreno difícil) ou granizo (como chuva, mais 1 ponto de dano de impacto por rodada, '
                 'no início de seus turnos).',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, uma vez por rodada você pode gastar uma ação padrão para '
                            'fazer um raio cair sobre um alvo na área, causando 3d8 pontos de dano de '
                            'eletricidade (Reflexos reduz à metade).',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano de raios (veja acima) em +1d8.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: se escolheu causar chuva, ela se torna mais grossa, revelando a silhueta '
                            'de criaturas invisíveis na área. Criaturas Médias ou menores ficam lentas e '
                            'criaturas voadoras precisam passar num teste de Atletismo por rodada ou caem ao '
                            'solo (mas podem fazer testes de Acrobacia para reduzir o dano de queda, como o '
                            'normal).',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: se escolheu causar granizo, muda o dano para 2d6 por rodada.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+3 PM: se escolheu causar neve, criaturas na área sofrem 2d6 pontos de dano de '
                            'frio no início de seus turnos.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e6',
                    'text': '+3 PM: muda a área para cilindro com 90m de raio e 90m de altura.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'longo',
  'area': 'cilindro com 15m de raio e 15m de altura',
  'duration': 'sustentada',
  'id': 'jda:tempestade-divina'},
 {'name': 'Tentáculos de Trevas',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 209 (PDF 215)',
  'pdf_page': 215,
  'stats': 'Execução: padrão; Alcance: médio; Área: esfera com 6m de raio; Duração: cena.',
  'description': 'Um círculo de energias sombrias se abre no chão, de onde surgem tentáculos feitos de treva '
                 'viscosa. Ao lançar a magia e no início de cada um de seus turnos, você faz um teste da '
                 'manobra agarrar (usando seu bônus de Misticismo) contra cada criatura na área. Se você '
                 'passar, a criatura é agarrada; se a vítima já está agarrada, é esmagada, sofrendo 4d6 '
                 'pontos de dano de trevas. A área conta como terreno difícil. Os tentáculos são imunes a '
                 'dano.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o raio da área em +3m.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano dos tentáculos em +2d6.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'médio',
  'area': 'esfera com 6m de raio',
  'duration': 'cena',
  'id': 'jda:tentaculos-de-trevas'},
 {'name': 'Terremoto',
  'tradition': 'Divina',
  'circle': 4,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 209 (PDF 215)',
  'pdf_page': 215,
  'stats': 'Execução: padrão; Alcance: longo; Área: esfera com 30m de raio; Duração: 1 rodada; Resistência: '
           'veja texto.',
  'description': 'Esta magia cria um tremor de terra que rasga o solo. O terremoto dura uma rodada, durante '
                 'a qual criaturas sobre o solo ficam atordoadas (apenas uma vez por cena). Barreiras '
                 'físicas não interrompem a área de Terremoto.\n'
                 'O efeito exato depende do terreno.\n'
                 'Caverna ou subterrâneo: a magia derruba o teto, causando 12d6 pontos de dano de impacto e '
                 'agarrando todas as criaturas na área. Um teste de Reflexos reduz o dano à metade e evita a '
                 'condição.\n'
                 'Construção: todas as estruturas na área sofrem 200 pontos de dano de impacto, o suficiente '
                 'para derrubar construções de madeira ou alvenaria simples, mas não de alvenaria reforçada. '
                 'Criaturas em uma construção que desmorone sofrem o mesmo efeito de criaturas em uma '
                 'caverna (veja acima).\n'
                 'Espaço aberto: fendas se abrem no chão. Cada criatura na área precisa rolar um dado; em um '
                 'resultado ímpar, uma fenda se abre sob ela e ela precisa fazer um teste de Reflexos; se '
                 'falhar, cai na fenda. A criatura pode escapar gastando uma ação completa e passando em um '
                 'teste de Atletismo. No início do seu próximo turno as fendas se fecham, matando todos que '
                 'estejam dentro delas.\n'
                 'Penhasco: o penhasco racha, criando um desmoronamento que percorre uma distância '
                 'horizontal igual à distância da queda. Por exemplo, um penhasco com 30m de altura '
                 'desmorona em uma área de 30m de comprimento além da base. Qualquer criatura no caminho '
                 'sofre 12d6 pontos de dano de impacto e fica agarrada. Um teste de Reflexos reduz o dano à '
                 'metade e evita ficar agarrado.\n'
                 'Rio, lago ou pântano: fissuras se abrem sob a água, drenando-a e formando um lamaçal. '
                 'Criaturas na área precisam fazer um teste de Reflexos para não afundarem na lama e ficarem '
                 'agarradas. No início do seu próximo turno as fissuras se fecham, possivelmente afogando as '
                 'criaturas que ficaram agarradas.\n'
                 'Criaturas agarradas (efeito possível de caverna, construção, penhasco e rio, lago ou '
                 'pântano) sofrem 1d6 pontos de dano por rodada até serem libertadas, o que exige uma ação '
                 'completa e um teste de Atletismo (por parte da própria criatura ou de um aliado '
                 'adjacente).',
  'enhancements': [],
  'range': 'longo',
  'area': 'esfera com 30m de raio',
  'duration': '1 rodada',
  'id': 'jda:terremoto'},
 {'name': 'Toque Chocante',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Evocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 209 (PDF 215)',
  'pdf_page': 215,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: instantânea; Resistência: Fortitude '
           'reduz à metade.',
  'description': 'Arcos elétricos envolvem sua mão, causando 2d8+2 pontos de dano de eletricidade. Se o alvo '
                 'usa armadura de metal (ou carrega muito metal, a critério do mestre), sofre uma penalidade '
                 'de –5 no teste de resistência.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o dano em 1d8+1.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a resistências para nenhum. Como parte da execução da magia, você '
                            'faz um ataque corpo a corpo contra o alvo. Se acertar, causa o dano do ataque e '
                            'da magia.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o alcance para pessoal e o alvo para área: esfera com 6m de raio. '
                            'Você dispara raios pelas pontas dos dedos que afetam todas as criaturas na '
                            'área.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:toque-chocante'},
 {'name': 'Toque da Morte',
  'tradition': 'Universal',
  'circle': 5,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 209 (PDF 215)',
  'pdf_page': 215,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: instantânea; Resistência: veja '
           'texto.',
  'description': 'Sua mão exala energias letais. A criatura sofre 10d8+10 pontos de dano de trevas. Se '
                 'estiver com menos da metade de seus PV, em vez disso deve fazer um teste de Fortitude. Se '
                 'passar, sofre\n'
                 'o dano normal. Se falhar, seus PV são reduzidos a –10.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para curto. Em vez de tocar no alvo, você dispara um raio '
                            'púrpura da ponta de seu dedo indicador.',
                    'cost': 2,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+10 PM: muda o alcance para curto e o alvo para inimigos no alcance. Em vez de '
                            'tocar no alvo, você dispara raios púrpuras da ponta de seus dedos.',
                    'cost': 10,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:toque-da-morte'},
 {'name': 'Toque Vampírico',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 209 (PDF 215)',
  'pdf_page': 215,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 criatura; Duração: instantânea; Resistência: Fortitude '
           'reduz à metade.',
  'description': 'Sua mão brilha com energia sombria, causando 6d6 pontos de dano de trevas. Você recupera '
                 'pontos de vida iguais à metade do dano causado (se causou algum dano).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda a resistências para nenhum como parte da execução da magia, você '
                            'pode fazer um ataque corpo a corpo contra o alvo. Se acertar, causa o dano do '
                            'ataque e da magia, e recupera pontos de vida iguais à metade do dano da magia.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano em +2d6.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o alcance para pessoal, o alvo para você e a duração para cena. Em '
                            'vez do normal, a cada rodada você pode gastar uma ação padrão para tocar 1 '
                            'criatura e causar 3d6 pontos de dano. Você recupera pontos de vida iguais à '
                            'metade do dano causado. Requer 3º círculo.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'jda:toque-vampirico'},
 {'name': 'Tranca Arcana',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 209 (PDF 215)',
  'pdf_page': 215,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 objeto Grande ou menor; Duração: permanente.',
  'description': 'Esta magia tranca uma porta ou outro item que possa ser aberto ou fechado (como um baú, '
                 'caixa etc.), aumentando a CD de testes de Força ou Ladinagem para abri-lo em +10. Você '
                 'pode abrir livremente sua própria tranca sem problemas.\n'
                 'Componente material: chave de bronze no valor de T$ 25.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda o alcance para curto. Em vez do normal, pode abrir ou fechar um '
                            'objeto de tamanho Médio ou menor, como uma porta ou baú. Não afeta objetos '
                            'trancados.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o alcance para curto e a duração para instantânea. Em vez do '
                            'normal, a magia abre portas, baús e janelas trancadas, presas, barradas ou '
                            'protegidas por Tranca Arcana (o efeito é dissipado) a sua escolha. Ela também '
                            'afrouxa grilhões e solta correntes.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: aumenta a CD para abrir o alvo em +5.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+5 PM: muda o alvo para 1 objeto de qualquer tamanho, podendo afetar até mesmo '
                            'os portões de um castelo. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 objeto Grande ou menor',
  'duration': 'permanente',
  'id': 'jda:tranca-arcana'},
 {'name': 'Tranquilidade',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 210 (PDF 216)',
  'pdf_page': 216,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 animal ou humanoide; Duração: cena; Resistência: '
           'Vontade parcial.',
  'description': 'Você emana ondas de serenidade. Se falhar na resistência, o alvo tem sua atitude mudada '
                 'para indiferente (veja a página 259) e não pode atacar ou realizar qualquer ação '
                 'agressiva. Se passar, sofre –2 em testes de ataque. Qualquer ação hostil contra o alvo ou '
                 'seus aliados dissipa a magia e faz ele retornar à atitude que tinha antes (ou pior, de '
                 'acordo com o mestre).',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alvo para 1 criatura.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: aumenta o número de alvos em +1.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda o alcance para médio e o alvo para criaturas escolhidas. Requer 3º '
                            'círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 animal ou humanoide',
  'duration': 'cena',
  'id': 'jda:tranquilidade'},
 {'name': 'Transformação de Guerra',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 210 (PDF 216)',
  'pdf_page': 216,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: sustentada.',
  'description': 'Você se torna uma máquina de combate, ficando mais forte, rápido e resistente. Você recebe '
                 '+6 na Defesa, testes de ataque e rolagens de dano corpo a corpo, e 30 PV temporários. '
                 'Durante a Transformação de Guerra você não pode lançar magias, mas se torna proficiente em '
                 'todas as armas.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta os bônus na Defesa, testes de ataque e rolagens de dano corpo a '
                            'corpo em +1, e os PV temporários em +10.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: adiciona componente material (barra de adamante no valor de T$ 100). Sua '
                            'forma de combate ganha um aspecto metálico e sem expressões. Além do normal, '
                            'você recebe redução de dano 10 e imunidade a atordoamento e efeitos de cansaço, '
                            'encantamento, metabolismo, trevas e veneno, e não precisa respirar.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'sustentada',
  'id': 'jda:transformacao-de-guerra'},
 {'name': 'Transmutar Objetos',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 210 (PDF 216)',
  'pdf_page': 216,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: matéria-prima, como madeira, rochas, ossos; Duração: '
           'cena.',
  'description': 'A magia transforma matéria bruta para moldar um novo objeto. Você pode usar matéria-prima '
                 'mundana para criar um objeto de tamanho Pequeno ou menor e preço máximo de T$ 25, como um '
                 'balde ou uma espada. O objeto reverte à matéria-prima no final da cena, ou se for tocado '
                 'por um objeto feito de chumbo. Esta magia não pode ser usada para criar objetos '
                 'consumíveis, como alimentos ou itens alquímicos, nem objetos com mecanismos complexos, '
                 'como bestas ou armas de fogo. Transmutar Objetos anula Despedaçar.',
  'enhancements': [{'id': 'e1',
                    'text': 'Truque: muda o alvo para 1 objeto mundano Mínusculo (ou material em quantidade '
                            'equivalente) e a duração para instantânea. Em vez do normal, você pode alterar '
                            'as propriedades físicas do alvo, como colorir, limpar ou sujar itens pequenos '
                            '(incluindo peças de roupa), aquecer, esfriar e/ou temperar (mas não produzir) '
                            'ou curar 1 PV do objeto, consertando pequenas falhas como colar um frasco de '
                            'cerâmica quebrado, unir os elos de uma corrente ou costurar uma roupa rasgada. '
                            'Um objeto só pode ser afetado por este truque uma vez por dia.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o alcance para toque, o alvo para 1 construto e a duração para '
                            'instantânea. Em vez do normal, cura 2d8 PV do alvo. Você pode gastar 2 PM '
                            'adicionais para aumentar a cura em +1d8.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o limite de tamanho do objeto em uma categoria.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: aumenta o preço máximo do objeto criado em um fator de x10 (+3 PM por T$ '
                            '250 de preço, +6 PM por T$ 2.500 de preço e assim por diante).',
                    'cost': 3,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+5 PM: muda o alvo para 1 objeto mundano e a duração para instantânea. Em vez '
                            'do normal, você cura todos os PV do alvo, restaurando o objeto totalmente. Este '
                            'aprimoramento está sujeito aos limites de tamanho e preço do objeto conforme a '
                            'magia original e não funciona se o objeto tiver sido completamente destruído '
                            '(queimado até virar cinzas ou desintegrado, por exemplo). Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e6',
                    'text': '+9 PM: como o aprimoramento anterior, mas passa a afetar itens mágicos.',
                    'cost': 9,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': 'matéria-prima, como madeira, rochas, ossos',
  'duration': 'cena',
  'id': 'jda:transmutar-objetos'},
 {'name': 'Velocidade',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 210 (PDF 216)',
  'pdf_page': 216,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: sustentada.',
  'description': 'O alvo pode realizar uma ação padrão ou de movimento adicional por turno. Esta ação não '
                 'pode ser usada para lançar magias e ativar engenhocas.',
  'enhancements': [{'id': 'e1',
                    'text': '+0 PM: muda a duração para cena. A ação adicional que você pode fazer é apenas '
                            'de movimento. Uma criatura só pode receber uma ação adicional por turno como '
                            'efeito de Velocidade.',
                    'cost': 0,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+7 PM: muda o alvo para criaturas escolhidas no alcance. Requer 4º círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: muda o alcance para pessoal e o alvo para você. Você acelera sua mente, '
                            'além de seu corpo. A ação adicional pode ser usada para lançar magias e ativar '
                            'engenhocas. Requer 4º círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'sustentada',
  'id': 'jda:velocidade'},
 {'name': 'Vestimenta da Fé',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Abjuração',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 210 (PDF 216)',
  'pdf_page': 216,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 armadura, escudo ou vestuário; Duração: 1 dia.',
  'description': 'Você fortalece um item, aumentando o bônus de Defesa de uma armadura ou escudo em +2. No '
                 'caso de um vestuário, ele passa a oferecer +2 na Defesa (não cumulativo com armadura). Os '
                 'efeitos desta magia contam como um bônus de encanto.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: o objeto oferece o mesmo bônus em testes de resistência. Requer 3º '
                            'círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: aumenta o bônus em +1.',
                    'cost': 4,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM: o objeto também oferece redução de dano 5. Requer 4º círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 armadura, escudo ou vestuário',
  'duration': '1 dia',
  'id': 'jda:vestimenta-da-fe'},
 {'name': 'Viagem Arbórea',
  'tradition': 'Divina',
  'circle': 3,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 210 (PDF 216)',
  'pdf_page': 216,
  'stats': 'Execução: completa; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Como parte da execução, você entra em uma árvore adjacente que seja maior do que você. '
                 'Você pode permanecer dentro da árvore, percebendo os arredores de forma normal (mas sem '
                 'poder fazer ações). Você pode gastar uma ação de movimento para sair dessa árvore, ou de '
                 'qualquer outra dentro de 1km. Se estiver dentro de uma árvore que seja destruída, a magia '
                 'termina e você sofre 10d6 pontos de dano de impacto. Enquanto a magia durar você pode '
                 'gastar uma ação de movimento e 1 PM para entrar em outras árvores.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para toque, o alvo para até cinco criaturas e a duração '
                            'para instantânea. Os alvos entram em uma planta (de tamanho Médio ou maior) e '
                            'saem em outra planta do mesmo tamanho a até 100km de distância, especificada em '
                            'direção e distância aproximadas (como “50km ao norte”).',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:viagem-arborea'},
 {'name': 'Viagem Planar',
  'tradition': 'Universal',
  'circle': 4,
  'school': 'Convocação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 211 (PDF 217)',
  'pdf_page': 217,
  'stats': 'Execução: completa; Alcance: toque; Alvo: pessoal; Duração: instantânea.',
  'description': 'Você viaja instantaneamente para outro plano da Criação. Lá, você chega de 10 a 1.000km do '
                 'destino pretendido (role 1d100 e multiplique por 10km).\n'
                 'Componente material: um bastão de metal precioso em forma de forquilha (no valor de T$ '
                 '1.000). O tipo de metal determina para qual plano de existência você será enviado. Os '
                 'metais que levam a dimensões específicas podem ser difíceis de encontrar, de acordo com o '
                 'mestre.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alvo para até cinco criaturas voluntárias que você esteja '
                            'tocando.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': 'pessoal',
  'duration': 'instantânea',
  'id': 'jda:viagem-planar'},
 {'name': 'Vidência',
  'tradition': 'Universal',
  'circle': 3,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 211 (PDF 217)',
  'pdf_page': 217,
  'stats': 'Execução: completa; Alcance: ilimitado; Alvo: 1 criatura; Duração: sustentada; Resistência: '
           'Vontade anula.',
  'description': 'Através de uma superfície reflexiva (bacia de água benta para clérigos, lago para druidas, '
                 'bola de cristal para magos, espelho para feiticeiros etc.) você pode ver e ouvir uma '
                 'criatura escolhida e seus arredores (cerca de 6m em qualquer direção), mesmo que ela se '
                 'mova. O alvo pode estar a qualquer distância, mas se passar em um teste de Vontade, a '
                 'magia falha. A vítima recebe bônus ou penalidades em seu teste de resistência, dependendo '
                 'do conhecimento que você tiver dela.\n'
                 '• Não conhece o alvo: +10.\n'
                 '• Ouviu falar do alvo: +5.\n'
                 '• O alvo está em outro plano ou mundo: +5.\n'
                 '• Já encontrou o alvo pessoalmente: +0.\n'
                 '• Tem uma pintura, escultura ou outra representação do alvo: –2.\n'
                 '• Conhece bem o alvo: –5.\n'
                 '• Tem um pertence pessoal ou peça de roupa do alvo: –5.\n'
                 '• Tem uma parte do corpo do alvo (unhas, cabelos...): –10.',
  'enhancements': [],
  'range': 'ilimitado',
  'target': '1 criatura',
  'duration': 'sustentada',
  'id': 'jda:videncia'},
 {'name': 'Visão da Verdade',
  'tradition': 'Universal',
  'circle': 4,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 211 (PDF 217)',
  'pdf_page': 217,
  'stats': 'Execução: movimento; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Você enxerga a forma real das coisas. Você pode ver através de camuflagem e escuridão '
                 '(normais e mágicas), assim como efeitos de ilusão e transmutação (enxergando a verdade '
                 'como formas translúcidas ou sobrepostas).',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para toque e o alvo para 1 criatura.',
                    'cost': 1,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: além do normal, o alvo fica com sentidos apurados; ele recebe +10 em '
                            'todos os testes de Percepção.',
                    'cost': 1,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: além do normal, o alvo escuta falsidades; ele recebe +10 em todos os '
                            'testes de Intuição.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+4 PM: além do normal, o alvo enxerga através de paredes e barreiras com 30cm '
                            'de espessura ou menos (as paredes e barreiras parecem translúcidas).',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:visao-da-verdade'},
 {'name': 'Visão Mística',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 211 (PDF 217)',
  'pdf_page': 217,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Seus olhos brilham com uma luz azul e passam a enxergar auras mágicas. Este efeito é '
                 'similar ao uso de Misticismo para detectar magia, mas você detecta todas as auras mágicas '
                 'em alcance médio e recebe todas as informações sobre elas sem gastar ações. Além disso, '
                 'você pode gastar uma ação de movimento para descobrir se uma criatura que possa perceber '
                 'em alcance médio é capaz de lançar magias e qual a aura gerada pelas magias de círculo '
                 'mais alto que ela pode lançar.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: recebe visão no escuro.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a duração para um dia.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: também pode enxergar objetos e criaturas invisíveis. Eles aparecem como '
                            'formas translúcidas.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:visao-mistica'},
 {'name': 'Vitalidade Fantasma',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Necromancia',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 211 (PDF 217)',
  'pdf_page': 217,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: instantânea.',
  'description': 'Você suga energia vital da terra, recebendo 2d10 pontos de vida temporários. Os PV '
                 'temporários desaparecem ao final da cena.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta os PV temporários recebidos em +1d10. Caso a magia cause dano, '
                            'em vez disso aumenta o dano causado em +1d10.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: muda o alvo para área: esfera com 6m de raio centrada em você e a '
                            'resistência para Fortitude reduz à metade. Em vez do normal, você suga energia '
                            'das criaturas vivas na área, causando 1d10 pontos de dano de trevas e recebendo '
                            'PV temporários iguais ao dano total causado. Os PV temporários desaparecem ao '
                            'final da cena. Requer 2º círculo.',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'instantânea',
  'id': 'jda:vitalidade-fantasma'},
 {'name': 'Voo',
  'tradition': 'Arcana',
  'circle': 3,
  'school': 'Transmutação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 211 (PDF 217)',
  'pdf_page': 217,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Você recebe deslocamento de voo 12m. Voar por meio desta magia é simples como andar — você '
                 'pode atacar e lançar magias normalmente enquanto voa. Quando a magia termina, você desce '
                 'lentamente até o chão, como se estivesse sob efeito de Queda Suave.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para toque e o alvo para 1 criatura.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: muda a duração para um dia. Requer 4º círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+4 PM: muda o alcance para curto e o alvo para até 10 criaturas. Requer 4° '
                            'círculo.',
                    'cost': 4,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:voo'},
 {'name': 'Voz Divina',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Adivinhação',
  'book': 'jda',
  'source': 'Tormenta20 — Jogo do Ano, p. 211 (PDF 217)',
  'pdf_page': 217,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Você pode conversar com criaturas de qualquer raça e tipo: animal, construto, espírito, '
                 'humanoide, monstro ou morto-vivo. Pode fazer perguntas e entende suas respostas, mesmo sem '
                 'um idioma em comum ou se a criatura não for capaz de falar, mas respeitando os limites da '
                 'Inteligência dela. A atitude dessas criaturas não é alterada, mas você pode usar a perícia '
                 'Diplomacia para tentar mudar sua atitude.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: você concede um pouco de vida a um cadáver, suficiente para que ele '
                            'responda a suas perguntas. O conhecimento do corpo é limitado ao que ele tinha '
                            'enquanto vivo e suas respostas são curtas e enigmáticas. Um corpo só pode ser '
                            'alvo desta magia uma vez. Ela também não funciona em um corpo cuja cabeça tenha '
                            'sido destruída.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: você pode falar com plantas (normais ou monstruosas) e rochas. Plantas e '
                            'rochas têm percepção limitada de seus arredores e normalmente fornecem '
                            'respostas simplórias.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'jda:voz-divina'},
 {'name': 'Armadura Elemental',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Evocação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 252 (PDF 254)',
  'pdf_page': 254,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Escolha um tipo de energia entre ácido, eletricidade, fogo ou frio. Uma aura faiscante '
                 'dessa energia emana de seu corpo — sempre que uma criatura adjacente acertar um ataque '
                 'corpo a corpo em você, ela sofre 2d6 pontos de dano do tipo escolhido.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para toque e o alvo para 1 criatura. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano em +1d6 (total de dados limitado pelo círculo máximo de '
                            'magia que você pode lançar). Requer 3º círculo.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: muda a energia para essência. Requer 2º círculo.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'herois:armadura-elemental'},
 {'name': 'Assobio Perigoso',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Convocação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 252 (PDF 254)',
  'pdf_page': 254,
  'stats': 'Execução: padrão; Alcance: pessoal; Efeito: grupo de criaturas conjuradas; Duração: especial.',
  'description': 'Esta estranha magia conjura um grupo de criaturas agressivas que imediatamente atacam quem '
                 'está por perto… Inclusive o conjurador e seus aliados! As criaturas são feitas de energia '
                 'e representam um encontro, preparado pelo mestre, de ND igual ao nível do conjurador. Elas '
                 'surgem em alcance curto e agem imediatamente após o turno do conjurador, atacando quem '
                 'estiver por perto (decida aleatoriamente). As criaturas lutam até a morte ou até 1 minuto, '
                 'quando então desaparecem, e não deixam corpos nem tesouro.\n'
                 'A função original da magia é incerta. Estudiosos acreditam ser fruto de um experimento '
                 'falho, ou uma tentativa de conjurar alguma criatura específica. De qualquer forma, hoje é '
                 'utilizada para treinar aventureiros ou causar distrações em situações específicas. '
                 'Componente Material: miniaturas em metal de criaturas (T$ 25 por nível do conjurador).',
  'enhancements': [],
  'range': 'pessoal',
  'effect': 'grupo de criaturas conjuradas',
  'duration': 'especial',
  'id': 'herois:assobio-perigoso'},
 {'name': 'Aura de Morte',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Necromancia',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 252 (PDF 254)',
  'pdf_page': 254,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: esfera com 6m de raio; Duração: cena.',
  'description': 'Uma aura de frio necrótico emana a partir do seu corpo, alimentando-se de sua própria '
                 'força vital. Quando você lança a magia, e no início de cada um dos seus turnos, você perde '
                 '1d6 pontos de vida e cada outra criatura na área perde 2d8 pontos de vida.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta a perda de vida para outras criaturas em +1d8 (número de dados '
                            'de perda de vida máximos limitados pelo círculo máximo de magia que você pode '
                            'lançar). Requer 3º círculo.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: adiciona resistência (Fortitude parcial). Além do normal, outras '
                            'criaturas que percam pontos de vida pela magia devem fazer um teste de '
                            'Fortitude. Se falharem, não podem recuperar PV por 1 rodada. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'esfera com 6m de raio',
  'duration': 'cena',
  'id': 'herois:aura-de-morte'},
 {'name': 'Conjurar Armadilha',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Transmutação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 252 (PDF 254)',
  'pdf_page': 254,
  'stats': 'Execução: completa; Alcance: curto; Efeito: 1 armadilha conjurada; Duração: permanente.',
  'description': 'Esta magia modifica o terreno e/ou a arquitetura de um ponto no alcance, transformando-o '
                 'em uma armadilha de caçador (Tormenta20, p. 50) a sua escolha. A armadilha criada segue as '
                 'mesmas regras de armadilhas, mas a CD dos testes para encontrá-la e resistir a ela é a da '
                 'magia.\n'
                 'Embora seja produzida por magia, a armadilha ainda pode ser superada por meios mundanos '
                 'normais. Depois de ativada, seja bem-sucedida ou não, a armadilha não volta a se reativar: '
                 'fica inerte e inofensiva, devendo ser conjurada outra vez.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: seus poderes que afetam armadilhas também afetam a armadilha criada pela '
                            'magia.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: quando lança a magia, você pode escolher qualquer número de criaturas no '
                            'alcance para não serem afetadas pela armadilha. Requer 2° círculo.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda a execução para padrão. A armadilha pode ser conjurada diretamente '
                            'em uma área ocupada por uma criatura, o que a aciona imediatamente. Requer 3º '
                            'círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+1 PM(Apenas Armadilheiros Mestres e Caçadores): reduz o tempo de execução para '
                            'movimento.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True},
                   {'id': 'e5',
                    'text': '+4 PM (Apenas Armadilheiros Mestres): em vez do normal, você pode conjurar uma '
                            'das suas armadilhas de armadilheiro mestre.',
                    'cost': 4,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': True}],
  'range': 'curto',
  'effect': '1 armadilha conjurada',
  'duration': 'permanente',
  'id': 'herois:conjurar-armadilha'},
 {'name': 'Coração Imortal',
  'tradition': 'Universal',
  'circle': 3,
  'school': 'Necromancia',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 252 (PDF 254)',
  'pdf_page': 254,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Manipulando energias necromânticas, você concentra sua força vital em uma parte específica '
                 'do seu corpo. Você recebe fortificação 100% e imunidade a sangramento.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda a duração para 1 dia.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta a cura do aprimoramento abaixo para +10 PV.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+4 PM: adiciona componente material (um coração de pedra no valor de T$ 100). '
                            'Além do normal, quando seus pontos de vida são reduzidos a 0 ou menos, você '
                            'cura 30 PV e a magia se encerra. Você só pode ser curado por este aprimoramento '
                            'uma vez por dia.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'herois:coracao-imortal'},
 {'name': 'Desafio Corajoso',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Encantamento',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 252 (PDF 254)',
  'pdf_page': 254,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura voluntária; Duração: sustentada; Resistência: '
           'Vontade anula.',
  'description': 'Esta magia cria uma aura de influência de 9m ao redor do alvo. Outras criaturas que '
                 'iniciarem seus turnos dentro da aura devem fazer um teste de Vontade. Se falharem, '
                 'quaisquer\n'
                 'ações hostis nesse turno devem ser feitas contra o alvo.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: muda o alvo para 1 criatura ou objeto. Requer 4° círculo.',
                    'cost': 3,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura voluntária',
  'duration': 'sustentada',
  'id': 'herois:desafio-corajoso'},
 {'name': 'Descobrir Fraqueza',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Adivinhação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 253 (PDF 255)',
  'pdf_page': 255,
  'stats': 'Execução: movimento; Alcance: curto; Alvo: 1 criatura; Duração: instantânea; Resistência: '
           'Vontade evita.',
  'description': 'Você analisa uma criatura em busca de pontos fracos e outras características. Para isso, '
                 'como parte do efeito da magia, você faz um teste de Misticismo para identificar criatura '
                 'contra o alvo (independente do tipo dele) com um bônus de +10.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o bônus no teste em +5.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: além do normal, sua próxima rolagem de dano contra a criatura nessa cena '
                            'ignora 10 pontos da redução de dano dela. Requer 2° círculo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: além do normal, você recebe +2 em testes contra a criatura até o fim da '
                            'cena. Requer 2° círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'herois:descobrir-fraqueza'},
 {'name': 'Desfazer Engenhoca',
  'tradition': 'Universal',
  'circle': 2,
  'school': 'Abjuração',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 253 (PDF 255)',
  'pdf_page': 255,
  'stats': 'Execução: padrão; Alcance: médio; Área ou Alvo: esfera com 3m de raio ou 1 criatura ou '
           'engenhoca; Duração: instantânea.',
  'description': 'Você desfaz os efeitos ativos de engenhocas, como se sua duração tivesse acabado (efeitos '
                 'instantâneos não podem ser dissipados). Se lançar esta magia em uma criatura ou área, faça '
                 'um teste de Misticismo; você dissipa os efeitos ativos de engenhocas com CD igual ou menor '
                 'que o resultado do teste. Lançada diretamente contra uma engenhoca, aumenta a CD para '
                 'ativá-la em +10 até o fim da cena. Lançada contra um construto, o teste é oposto à Vontade '
                 'do alvo. Se você vencer, além do normal, o construto fica fraco e vulnerável (mesmo que '
                 'seja imune a essas condições). A critério do mestre, esta magia pode afetar outras '
                 'habilidades e itens similares a engenhocas.\n'
                 'Dizem que Desfazer Engenhoca foi ofertada aos mortais pela própria Wynna, ressentida em '
                 'relação a inventos mundanos que imitam seus milagres má-\n'
                 'gicos. Por outro lado, alguns isentam a deusa, atribuindo sua criação a algum arcanista '
                 'extremamente incomodado com esses inventores do diacho!',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: além do normal, você recebe +5 no seu teste de Misticismo para dissipar '
                            'uma engenhoca para cada vez que a viu ser usada na cena.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: além do normal, a magia ignora qualquer efeito ativo gerado por '
                            'engenhocas (por exemplo, um Campo Antimagia).',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+12 PM: muda a área para esfera com 9m de raio. Em vez do normal, cria um '
                            'efeito de disjunção. Todos os efeitos de engenhocas na área são automaticamente '
                            'dissipados e todas as engenhocas na área, exceto aquelas que você estiver '
                            'carregando, enguiçam por uma cena (o usuário de engenhocas carregadas tem '
                            'direito a um teste de Vontade para evitar isso; engenhocas soltas são itens '
                            'mundanos e por isso não têm direito a testes, como normal). Requer 5º círculo.',
                    'cost': 12,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'médio',
  'target': '1 criatura',
  'duration': 'instantânea',
  'area': 'esfera com 3m de raio ou 1 criatura ou engenhoca',
  'id': 'herois:desfazer-engenhoca'},
 {'name': 'Discrição',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 253 (PDF 255)',
  'pdf_page': 255,
  'stats': 'Execução: padrão; Alcance: pessoal ou toque; Alvo: você ou 1 objeto; Duração: cena; Resistência: '
           'Vontade anula.',
  'description': 'Esta magia torna a aparência do alvo desinteressante, como se ele fosse parte da paisagem, '
                 'algo perdido na bagunça ou mais um na multidão. O alvo não se torna invisível, ainda é '
                 'percebido como uma criatura ou objeto; o encantamento apenas desvia a atenção dos '
                 'observadores para outras pessoas ou elementos ao redor. Testes de Investigação e Percepção '
                 'contra o alvo sofrem uma penalidade de –10.\n'
                 'Em combate, enquanto Discrição estiver ativa, todos os inimigos que iniciarem seus turnos '
                 'a até 9m do alvo devem fazer um teste de Vontade. Se falharem, qualquer ação hostil que '
                 'realizarem ignora a criatura. Esta magia se dissipa se você causar dano a qualquer '
                 'criatura.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alvo para 1 criatura. Requer 2º círculo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta a penalidade em testes para –15. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: além do normal, o alvo não pode ser detectado por magias de adivinhação. '
                            'Requer 4° círculo.',
                    'cost': 3,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal ou toque',
  'target': 'você ou 1 objeto',
  'duration': 'cena',
  'id': 'herois:discricao'},
 {'name': 'Distração Fugaz',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Ilusão',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 253 (PDF 255)',
  'pdf_page': 255,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 humanoide; Duração: instantânea; Resistência: Vontade '
           'anula.',
  'description': 'Esta magia busca algo de grande interesse pessoal (uma pessoa, um item, uma lembrança...) '
                 'na memória do alvo e produz uma breve ilusão disso, visível a todos os presentes. Não é '
                 'necessário que você conheça o interesse do alvo, a própria magia faz essa revelação. A '
                 'magia, entretanto, não é capaz de revelar detalhes minuciosos (como o nome de uma pessoa '
                 'ou item desejado), produzindo uma versão “genérica” do objeto de interesse. Não importando '
                 'a natureza da distração, se falhar em seu teste de Vontade, o alvo fica desprevenido '
                 'durante 1 rodada.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, se falhar no teste de Vontade o alvo também sofre –5 em '
                            'testes de Diplomacia e Intimidação até o fim da cena.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o alvo para 1 criatura. Requer 2º círculo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: em vez de desprevenido, o alvo fica atordoado (apenas uma vez por cena).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: afeta todos os alvos válidos a sua escolha dentro do alcance. Requer 2º '
                            'círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 humanoide',
  'duration': 'instantânea',
  'id': 'herois:distracao-fugaz'},
 {'name': 'Emular Magia',
  'tradition': 'Universal',
  'circle': 2,
  'school': 'Evocação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 253 (PDF 255)',
  'pdf_page': 255,
  'stats': 'Execução: movimento; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Pela duração de Emular Magia, você pode lançar uma única magia que tenha visto ser lançada '
                 'em alcance curto desde sua última rodada. A magia deve ser de um tipo (arcana ou divina) e '
                 'de um círculo a que você tenha acesso.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: a magia emulada pode ser de qualquer tipo, arcana ou divina.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'herois:emular-magia'},
 {'name': 'Espírito Balístico',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Convocação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 253 (PDF 255)',
  'pdf_page': 255,
  'stats': 'Execução: padrão; Alcance: curto; Efeito: 1 criatura conjurada; Duração: sustentada.',
  'description': 'Esta magia invoca um pequeno espírito feito de energia com aparência a sua escolha em um '
                 'espaço desocupado. O espírito é fixo, permanecendo no lugar onde foi invocado. No come-\n'
                 'ço dos seus turnos, o espírito dispara um projétil mágico contra o inimigo mais próximo em '
                 'alcance médio, causando 1d6+1 pontos de dano de perfuração. O espírito não realiza outras '
                 'ações e dispara projéteis a cada rodada, até que a magia termine, não existam mais '
                 'inimigos no alcance ou o espírito seja destruído.\n'
                 'O espírito tem Defesa igual à sua e 20 pontos de vida. Ele é imune a efeitos que pedem um '
                 'teste de Fortitude ou Vontade e falha automaticamente em testes de Reflexos.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano em um dado do mesmo tipo (total de dados limitado pelo '
                            'círculo máximo de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o número de espíritos para dois. Requer 2º círculo',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda o número de espíritos para três. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM (Apenas Golem [energia elemental], Qareen ou Kallyanach): muda o dado de '
                            'dano para d8 e o tipo de dano para o o tipo escolhido para sua habilidade '
                            'racial elemental.',
                    'cost': 3,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'curto',
  'effect': '1 criatura conjurada',
  'duration': 'sustentada',
  'id': 'herois:espirito-balistico'},
 {'name': 'Farejar Fortuna',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Adivinhação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 254 (PDF 256)',
  'pdf_page': 256,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Ao lançar esta magia, você descobre se existe algum tesouro em alcance longo. Para este '
                 'efeito, “tesouro” é qualquer acúmulo de itens valiosos (acima do dinheiro inicial de um '
                 'personagem do seu nível) que não estejam sendo carregados ou vestidos por uma criatura '
                 'inteligente.\n'
                 'Você sabe se há tesouros na área, mas não recebe nenhuma outra informação a respeito, como '
                 'a direção ou localização do tesouro, seu valor exato, obstáculos no caminho... nada disso '
                 'é informado pela magia.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para toque, o alvo para um item recém-encontrado e a '
                            'duração para instantânea. Em vez do normal, você recebe +5 em testes de perícia '
                            'para identificar o item.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: além do normal, você recebe +5 em testes de perícia para localizar o '
                            'tesouro.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: em vez do normal, quando você rola qualquer dado para definir um '
                            'tesouro, pode rolar dois dados e escolher qual resultado usar.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'herois:farejar-fortuna'},
 {'name': 'Maaais Klunc',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 254 (PDF 256)',
  'pdf_page': 256,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Esta magia surgiu com o objetivo de invocar a força estupenda e estapafúrdia de certo '
                 'bárbaro lendário, capaz de alcançar dimensões colossais. Infelizmente (ou talvez '
                 'felizmente) seus efeitos reais são muito mais brandos, pouco se aproximando do poder '
                 'descomunal e descabido do bruto em questão. Melhor assim.\n'
                 'Ao lançar a magia, você adquire uma fantástica Força +10. Um relevante efeito colateral, '
                 'contudo, é que sua Inteligência cai para acachapantes –3. Não, não uma penalidade de –3; '
                 'um valor –3! Penalidades no atributo são aplicadas após isso.\n'
                 'Pela duração de Maaais Klunc, você não pode lançar magias, nem é capaz de interromper esta '
                 'magia de forma voluntária — nem mesmo soletrar essa palavra. O mestre pode (vai) exigir '
                 'testes de Inteligência mesmo para as tarefas mentais mais simplórias, como achar a saída '
                 'de um aposento vazio, diferenciar aliados de inimigos ou determinar qual extremidade da '
                 'arma vai na direção do adversário.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para toque e o alvo para 1 criatura voluntária (por que '
                            'alguém seria voluntário?). Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: muda o alcance para curto e o alvo para 1 criatura involuntária (Vontade '
                            'evita). Requer 3º círculo. Espera, o quê!?',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'herois:maaais-klunc'},
 {'name': 'Máquina de Combate',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Transmutação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 254 (PDF 256)',
  'pdf_page': 256,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 construto; Duração: cena.',
  'description': 'Esta magia energiza a fonte de energia de um golem ou outro construto, sobrecarregando-a '
                 'temporariamente. O alvo recebe +5 em Atletismo e Luta, mas perde 1d4 pontos de vida no fim '
                 'de cada turno em que executar uma ação padrão.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: além do normal, os ataques corpo a corpo do alvo causam +1d6 pontos de '
                            'dano.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: além do normal, o alvo recebe +2 na Defesa.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o bônus na Defesa em +1.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 construto',
  'duration': 'cena',
  'id': 'herois:maquina-de-combate'},
 {'name': 'Ossos de Adamante',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 254 (PDF 256)',
  'pdf_page': 256,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Esta magia confere resistência extraordinária ao esqueleto, evitando ataques que causam '
                 'fraturas graves. O alvo recebe redução de impacto 5 e fortificação 25%.\n'
                 'Devido à rigidez do esqueleto, o corpo do alvo se torna incapaz de mudar de forma (como '
                 'usar ou encerrar a habilidade Forma Selvagem). Se sofrer um efeito de metamorfose, em vez '
                 'de mudar de forma o alvo perde 1d6 PV por PM gasto no efeito e fica lento. Essa condição '
                 'não pode ser re-\n'
                 'movida enquanto Ossos de Adamante estiver em efeito. Esta magia não afeta construtos.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda a redução de impacto para RD 5 e a fortificação para 50%. Requer 2º '
                            'círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alcance para toque e o alvo para 1 criatura viva.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'herois:ossos-de-adamante'},
 {'name': 'Poção Explosiva',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Transmutação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 255 (PDF 257)',
  'pdf_page': 257,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 poção; Duração: cena.',
  'description': 'Esta magia transforma o conteúdo de uma poção em uma substância volátil e explosiva. '
                 'Quando é usada, em vez de ter seu efeito normal, a poção causa 2d6 pontos de dano de '
                 'essência por círculo da magia que ela continha (outras características da magia, como '
                 'alvos, área e testes de resistência, se mantêm). Se a poção for ingerida, ela causa dano '
                 'máximo à criatura que a ingeriu, sem direito a teste de resistência.\n'
                 'Se esta magia for lançada sobre uma poção carregada por uma criatura, a criatura tem '
                 'direito a um teste de Reflexos para evitar esse efeito. Reconhecer uma poção adulterada '
                 'dessa forma exige um teste de Misticismo ou Ofício (alquimista) com CD 25.',
  'enhancements': [{'id': 'e1',
                    'text': '+5 PM: você pode determinar uma palavra-chave que, pronunciada por qualquer '
                            'pessoa em alcance curto, faz a poção explodir. Requer 3° círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+7 PM: muda o alcance para pessoal e o alvo para área (esfera com 9m de raio). '
                            'A magia afeta mesmo poções na área que estejam sendo carregadas. Requer 4° '
                            'círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 poção',
  'duration': 'cena',
  'id': 'herois:pocao-explosiva'},
 {'name': 'Piscar',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Transmutação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 255 (PDF 257)',
  'pdf_page': 257,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Pela duração da magia, você fica “piscando” entre o Plano material e o etéreo. Para quem o '
                 'observa, é como se você ficasse visível e invisível várias vezes por segundo.\n'
                 'Quaisquer ataques e habilidades (incluindo efeitos benéficos) de outras criaturas têm 50% '
                 'de chance de não afetá-lo. Você recebe +2 em testes de ataque, pois é difícil ver de onde '
                 'você está atacando. Contudo, seus próprios ataques e habilidades têm 25%\n'
                 'de chance de não afetar outras criaturas, pois você não tem controle total sobre quando '
                 'está em qual Plano.\n'
                 'Você pode interagir com criaturas etéreas, com as mesmas chances de falha.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para toque e o alvo para 1 criatura voluntária. Requer 3º '
                            'círculo.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'herois:piscar'},
 {'name': 'Punho de Mitral',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 255 (PDF 257)',
  'pdf_page': 257,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Esta magia transforma uma de suas mãos em mitral, tornando-a prateada como esse metal. A '
                 'mão continua capaz de realizar movimentos normais e segurar objetos — mas também pode '
                 'golpear ou esmagar. Se não estiver segurando nada com essa mão, você recebe +1 em testes '
                 'de ataque e na margem de ameaça com ataques desarmados, e pode causar dano letal ou não '
                 'letal com eles. Por fim, você pode manipular venenos com essa mão sem chance de se '
                 'envenenar acidentalmente.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o bônus em testes de ataque e na margem de ameaça para +2.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alcance para toque e o alvo para 1 criatura. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: além do normal, se você estiver empunhando uma arma ou um item esotérico '
                            'com essa mão, ele recebe os benefícios do material especial mitral (mesmo que '
                            'já possua outro material especial). Requer 2° círculo.',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'herois:punho-de-mitral'},
 {'name': 'Toque do Horizonte',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 255 (PDF 257)',
  'pdf_page': 257,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 arma de ataque à distância; Duração: cena.',
  'description': 'A magia melhora a precisão da arma, aumentando seu alcance em um passo (de curto para '
                 'médio e de médio para longo). Se o alcance da arma já é longo, ele é dobrado. Os efeitos '
                 'desta magia contam como um bônus de encanto.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: a arma ignora camuflagem leve e penalidades por cobertura leve.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: além do normal, a arma fornece +1 em testes de ataque e rolagens de dano '
                            'feitos dentro do seu alcance original.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o bônus do aprimoramento acima em +1 (bônus máximo limitado pelo '
                            'círculo máximo de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: a margem de ameaça da arma aumenta em +1. Requer 2° círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+5 PM: muda o alvo para uma arma de arremesso e a duração para sustentada. Em '
                            'vez do normal, a arma recebe o benefício do encanto dançarina. Requer 3° '
                            'círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 arma de ataque à distância',
  'duration': 'cena',
  'id': 'herois:toque-do-horizonte'},
 {'name': 'Transposição',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Convocação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 255 (PDF 257)',
  'pdf_page': 257,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 2 criaturas voluntárias; Duração: instantânea.',
  'description': 'Esta magia teletransporta duas criaturas, incluindo seu equipamento, fazendo com que '
                 'troquem de lugar imediatamente.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de alvos em +2. Você determina com quais criaturas cada '
                            'alvo troca de lugar.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: a troca não exige linha de efeito, mas os alvos ainda devem estar dentro '
                            'do alcance. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda o alvo para 2 criaturas do tipo lacaio e adiciona resistência '
                            '(Vontade anula). Requer 4º círculo.',
                    'cost': 5,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '2 criaturas voluntárias',
  'duration': 'instantânea',
  'id': 'herois:transposicao'},
 {'name': 'Viagem Onírica',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Adivinhação',
  'book': 'herois',
  'source': 'Heróis de Arton v1.1, p. 255 (PDF 257)',
  'pdf_page': 257,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Lançar esta magia faz você adormecer e abandonar seu corpo físico. Você se torna um '
                 'espírito incorpóreo com deslocamento de voo 18m. Você pode ver e ouvir, mas não falar ou '
                 'emitir qualquer som — nem realizar ataques, lançar magias ou interagir de qualquer forma '
                 'com criaturas e objetos materiais. Você ainda pode ser visto, em forma translúcida, e pode '
                 'ser afetado por qualquer efeito que afete criaturas incorpóreas.\n'
                 'Quando a magia acaba, você retorna imediatamente para seu corpo e desperta. A magia também '
                 'é cancelada caso seu corpo físico seja perturbado de qualquer forma. Você sofre uma '
                 'penalidade de –10 em testes de Percepção para notar ruídos próximos de seu corpo '
                 'adormecido.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: você pode falar em sua forma incorpórea. Requer 3º círculo.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: você pode lançar magias em sua forma incorpórea. Requer 4º círculo.',
                    'cost': 5,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'herois:viagem-onirica'},
 {'name': 'Arma de Jade',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 60 (PDF 62)',
  'pdf_page': 62,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 arma; Duração: cena.',
  'description': 'Esta magia ofertada por Lin-Wu transfere temporariamente para uma arma as qualdades '
                 'místicas do jade, um raro material de Tamu-ra. A arma é considerada mágica, pode ser '
                 'sacada e guardada como ação livre e fornece +1 nos testes de ataque e rolagens de dano '
                 '(isso conta como um bônus de encanto). Contra espíritos, os bônus fornecidos pela magia '
                 'são dobrados.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: a arma causa +1d4 de dano de eletricidade.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o bônus de ataque e dano em +1 (bônus máximo limitado pelo '
                            'círculo máximo de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM (Apenas Devotos de LinWu): muda o bônus de dano do aprimoramento acima '
                            'para +2d4.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'toque',
  'target': '1 arma',
  'duration': 'cena',
  'id': 'deuses:arma-de-jade'},
 {'name': 'Arsenal de Allihanna',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 60 (PDF 62)',
  'pdf_page': 62,
  'stats': 'Execução: padrão; Alcance: pessoal; Efeito: arma criada em sua mão; Duração: cena.',
  'description': 'Outrora chamada Armamento de Allihanna, esta magia recentemente recebeu um novo nome — com '
                 'implicações curiosas. Utilizada pela primeira vez por Lisandra de Galrasia, diz-se que a '
                 'verdadeira origem da magia estaria relacionada a seu pai, Arsenal, então mortal.\n'
                 'Você invoca uma arma a sua escolha, em uma versão de madeira mágica que fornece +1 nos '
                 'testes de ataque e rolagens de dano (isso conta como um bônus de encanto) e conta como uma '
                 'arma primitiva para efeitos como a magia Armamento da Natureza. Se for uma arma de '
                 'disparo, ela produz sua própria munição (mas você pode usar munição normal, se quiser). '
                 'Arsenal de Allihanna não cria armas complexas\n'
                 '(como bestas ou armas de fogo) e seus efeitos só funcionam em suas mãos.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o bônus em +1 (bônus máximo limitado pelo círculo máximo de '
                            'magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: a arma, ou sua munição, é recoberta de espinhos. Ela causa +1d6 pontos '
                            'de dano e o alvo do ataque fica sangrando.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM (Apenas Devotos de Allihanna ou Dahllan): muda o alvo para uma planta e o '
                            'alcance para toque. A planta manifesta uma arma corpo a corpo simples de '
                            'madeira Tollon e uma armadura de couro batido reforçada. Se você tiver o '
                            'suplemento Ameaças de Arton, ela pode manifestar uma espada espinhenta ou um '
                            'fruto da espada-mãe (p. 245). Se estiver apto, você empunha/veste os itens como '
                            'ação livre e eles desaparecem quando a magia acaba. Requer 2º círculo.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'effect': 'arma criada em sua mão',
  'duration': 'cena',
  'id': 'deuses:arsenal-de-allihanna'},
 {'name': 'Bofetada de Nimb',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Evocação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 60 (PDF 62)',
  'pdf_page': 62,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 humanoide; Duração: instantânea; Resistência: Vontade '
           'parcial.',
  'description': 'Uma mão mágica surge diante do alvo e o esbofeteia na face, ou em outra parte vulnerável, '
                 'desaparecendo em seguida. O golpe não causa dano, mas é bastante humilhante. Se o alvo '
                 'falhar na resistência, fica desprevenido por 1 rodada e vulnerável; se passar, fica apenas '
                 'vulnerável por 1 rodada.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: alvos que falhem na resistência ficam vulneráveis pela cena.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alvo para 1 criatura.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: em vez do normal, a mão dá leves tapinhas que acalmam os alvos e anulam '
                            'uma condição entre abalado, alquebrado, apavorado e frustrado. Requer 2° '
                            'círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: alvos que falhem na resistência ficam desprevenidos por 1d4+1 rodadas, '
                            'em vez de apenas 1.',
                    'cost': 3,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+5 PM (Apenas Devotos de Nimb): afeta todos os alvos válidos a sua escolha '
                            'dentro do alcance.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'curto',
  'target': '1 humanoide',
  'duration': 'instantânea',
  'id': 'deuses:bofetada-de-nimb'},
 {'name': 'Couraça de Allihanna',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Abjuração',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 60 (PDF 62)',
  'pdf_page': 62,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: 1 armadura ou vestuário; Duração: cena.',
  'description': 'Lisandra de Galrasia foi a primeira a manifestar uma armadura fibrosa, mas hoje outros '
                 'podem fazer o mesmo. Esta magia transforma o alvo em uma couraça arbórea. Se for uma '
                 'armadura, seu bônus na Defesa aumenta em +2 e se for um vestuário, passa a fornecer +2 na '
                 'Defesa (não cumulativo com armadura). Os efeitos desta magia contam como um bônus de '
                 'encanto e ela só pode ser lançada em terrenos naturais. Dahllan recebem 1 PM para usar em '
                 'aprimoramentos ao lançá-la.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta a Defesa em +1 (bônus máximo limitado pelo círculo máximo de '
                            'magia que você pode lançar).',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: além do normal, suas magias de evocação e transmutação custam –1 PM.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: o alvo é recoberto por folhas e galhos. Você recebe +5 em testes de '
                            'Furtividade e pode se esconder mesmo sem camuflagem ou cobertura disponível.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: além do normal, o alvo fornece o mesmo bônus em testes de resistência. '
                            'Requer 3° círculo.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+3 PM: além do normal, o alvo é recoberto esporos de cogumelo. Quando uma '
                            'criatura faz um ataque corpo a corpo contra você, ela deve fazer um teste de '
                            'Fortitude (CD da magia). Se falhar, fica paralisada por 1 rodada (apenas uma '
                            'vez por cena) e lenta. Se passar, fica lenta por 1 rodada. Requer 3° círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': '1 armadura ou vestuário',
  'duration': 'cena',
  'id': 'deuses:couraca-de-allihanna'},
 {'name': 'Escapatória de Hyninn',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 61 (PDF 63)',
  'pdf_page': 63,
  'stats': 'Execução: reação; Alcance: pessoal; Alvo: você; Duração: instantânea.',
  'description': 'Por um breve instante, você adquire uma agilidade espantosa para se esquivar de algum '
                 'perigo súbito. Você recebe +5 em um teste de Ladinagem para desarmar armadilhas ou de '
                 'Reflexos.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para curto e o alvo para 1 criatura. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: muda a execução para padrão e a duração para cena. Em vez do normal, o '
                            'bônus se aplica a todos os testes destas perícias pela duração. Requer 3º '
                            'círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM (Apenas Devotos de Hyninn): além do normal, o alvo pode usar Evasão '
                            '(Tormenta20, p. 73).',
                    'cost': 3,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True},
                   {'id': 'e4',
                    'text': '+7 PM (Apenas Devotos de Hyninn): além do normal, o alvo pode usar Evasão '
                            'Aprimorada (Tormenta20, p. 75). Requer 4° círculo.',
                    'cost': 7,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'instantânea',
  'id': 'deuses:escapatoria-de-hyninn'},
 {'name': 'Euforia de Valkaria',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 61 (PDF 63)',
  'pdf_page': 63,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Esta magia enche o alvo de disposição, apagando o medo (e bom senso) em seu coração e '
                 'impedindo-o de ser intimidado por desafios árduos.\n'
                 'O alvo se torna imune a medo e recebe +1 em testes de ataque quando luta em desvantagem '
                 '(um encontro contra o dobro de inimigos que seu grupo, ou com ND maior que o do grupo).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o bônus em testes de ataque em +1 (bônus máximo limitado pelo '
                            'círculo máximo de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a execução para reação e a duração para 1 rodada. Em vez do normal, '
                            'o alvo recebe imunidade a medo e +5 em Vontade. Requer 2° círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o alvo para área de esfera com 3m de raio. Você e todos os aliados '
                            'na área são afetados pela magia. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+1 PM (Apenas Devotos de Valkaria): muda o alcance para toque e o alvo para 1 '
                            'criatura.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'deuses:euforia-de-valkaria'},
 {'name': 'Execução de Thwor',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Necromancia',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 61 (PDF 63)',
  'pdf_page': 63,
  'stats': 'Execução: movimento; Alcance: curto; Alvo: 1 humanoide sob efeito de uma condição de medo; '
           'Duração: 1 rodada; Resistência: Vontade anula.',
  'description': 'Se acertar seu próximo ataque no alvo, ele se torna um acerto crítico. Se for um crítico '
                 'naturalmente, em vez disso seu multiplicador aumenta em +1.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alvo para 1 criatura. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: em vez do normal, a magia afeta 1 alvo sob efeito de uma condição '
                            'mental. Requer 3º círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+7 PM (Apenas Devotos de Thwor): se o ataque for um acerto crítico '
                            'naturalmente, em vez do normal ele causa o efeito de um golpe de misericórdia '
                            '(Tormenta20, p. 235). Requer 5º círculo.',
                    'cost': 7,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': True}],
  'range': 'curto',
  'target': '1 humanoide sob efeito de uma condição de medo',
  'duration': '1 rodada',
  'id': 'deuses:execucao-de-thwor'},
 {'name': 'Flecha de Luz',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Evocação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 61 (PDF 63)',
  'pdf_page': 63,
  'stats': 'Execução: padrão; Alcance: médio; Alvo: 1 criatura; Duração: instantânea; Resistência: Reflexos '
           'parcial.',
  'description': 'Esta magia lança uma flecha luminosa contra o alvo, que sofre 2d8+2 pontos de dano de luz '
                 'e fica ofuscado por 1 rodada. Passar no teste de resistência reduz o dano à metade e evita '
                 'a condição.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alvo para uma criatura que tenha causado dano a você ou a seus '
                            'aliados na última rodada e os dados de dano da magia para d10.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano em +1d8+1.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o número de alvos em +1 (número de alvos adicionais limitado '
                            'pelo círculo máximo de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM (Apenas Arcanos): alvos que falhem na resistência ficam cegos por 1 '
                            'rodada e então ofuscados. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True},
                   {'id': 'e5',
                    'text': '+3 PM (Apenas Arqueiros de Lenórienn): muda o alcance para pessoal, o alvo para '
                            'seu arco arcano, a duração para sustentada e a resistência para nenhuma. Em vez '
                            'do normal, o alvo emite luz como uma tocha e causa +2d8+2 pontos de dano de '
                            'luz. Criaturas que sofram dano do arco ficam ofuscadas (veja Arqueiro de '
                            'Lenórienn em Heróis de Arton).',
                    'cost': 3,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': True},
                   {'id': 'e6',
                    'text': '+1 PM (Apenas Elfos): muda o alvo para 1 duyshidakk ou 1 devoto de Aharadak, '
                            'Tauron ou Thwor. Muda os dados de dano para d10.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True},
                   {'id': 'e7',
                    'text': '+2 PM (Apenas Divinos): além do normal, para cada alvo que falhar na '
                            'resistência, o próximo aliado que causar dano a ele recebe uma quantidade de PV '
                            'temporários igual à metade do dano causado pela magia. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'médio',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'deuses:flecha-de-luz'},
 {'name': 'Frescor de Lena',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 61 (PDF 63)',
  'pdf_page': 63,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: raio de 9m; Duração: instantânea.',
  'description': 'Você emana uma aura refrescante, que envolve você e aliados na área. A aura purifica o ar '
                 'ao redor, eliminando todo tipo de fumaça, poeira, gás nocivo, nuvem ácida ou veneno de '
                 'inalação, exceto se forem gerados por magias de 2º círculo ou maior.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta em 1 o círculo de magia afetado (limitado pelo círculo máximo de '
                            'magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o alcance para toque, a área para alvo (1 criatura) e a duração '
                            'para 1 dia. Em vez do normal, suprime uma doença do alvo. Requer 2° círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM (Apenas Devotos de Lena): como acima, mas quando faz o teste da doença '
                            'nesse dia, o alvo recebe um bônus de +5. Requer 3° círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True},
                   {'id': 'e4',
                    'text': '+9 PM (Apenas Devotos de Lena): muda o alcance para toque, a área para alvo (1 '
                            'criatura) e adiciona componente material (ervas no valor de T$ 1.000). O alvo '
                            'recupera 1 ponto de atributo perdido por uma doença. Requer 4° círculo.',
                    'cost': 9,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'area': 'raio de 9m',
  'duration': 'instantânea',
  'id': 'deuses:frescor-de-lena'},
 {'name': 'Fúria dos Antepassados',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Evocação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 61 (PDF 63)',
  'pdf_page': 63,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 humanoide; Duração: instantânea; Resistência: Vontade '
           'parcial.',
  'description': 'Para aqueles devotados a Lin-Wu, respeito aos ancestrais é algo levado muito a sério — '
                 'pois no além-vida, eles podem julgar suas ações e trazer fortuna ou desgraça. Esta ma-\n'
                 'gia invoca a alma de um antepassado da vítima para acusá-la de erros passados e trazer '
                 'punição. O alvo sofre 1d6 pontos de dano psíquico e 1d6 pontos de dano de luz e fica pasmo '
                 'por 1 rodada (apenas na primeira vez que é alvo desta magia na cena). Se passar no teste '
                 'de resistência, sofre apenas metade do dano e evita a condição.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o número de alvos em +1. Requer 2° círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+4 PM: aumenta o dano psíquico e de luz em +1d6 cada.',
                    'cost': 4,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+0 PM(Apenas Devotos de LinWu): muda o alvo para 1 criatura inteligente (Int –3 '
                            'ou maior).',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'curto',
  'target': '1 humanoide',
  'duration': 'instantânea',
  'id': 'deuses:furia-dos-antepassados'},
 {'name': 'Futuro Melhor',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Adivinhação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 62 (PDF 64)',
  'pdf_page': 64,
  'stats': 'Execução: reação; Alcance: pessoal; Alvo: você; Duração: instantânea.',
  'description': 'Esta magia permite enxergar todas as possibilidades e consequências de um evento muito '
                 'recente, ainda a tempo de escolher o melhor caminho. O alvo recebe +2 em um teste cujo '
                 'dado já rolou, mas cujo resultado o mestre ainda não tenha declarado.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para curto e o alvo para 1 criatura. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM (Apenas Devotos de Thyatis): muda o bônus para 1d4+2.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'instantânea',
  'id': 'deuses:futuro-melhor'},
 {'name': 'Infortúnio de Sszzaas',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Necromancia',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 62 (PDF 64)',
  'pdf_page': 64,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: cena; Resistência: Vontade anula.',
  'description': 'Esta maldição menor reduz a resiliência da vítima, tornando-a mais suscetível a efeitos '
                 'nocivos. O alvo sofre –2 em testes de sua resistência originalmente mais baixa.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, a vítima perde imunidade a venenos até o fim da próxima '
                            'rodada. Requer 2° círculo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta a penalidade em –1 (penalidade máxima limitada pelo círculo '
                            'máximo de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM (Apenas Devotos de Sszzaas): além do normal, quando o alvo morre, deixa '
                            'para trás um pequeno cristal com memórias e segredos. Ao resolver uma busca '
                            '(Tormenta20, p. 278), um personagem pode quebrar um desses cristais para '
                            'receber +2 em um teste de perícia. Requer 3° círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'cena',
  'id': 'deuses:infortunio-de-sszzaas'},
 {'name': 'Instante Estoico',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 62 (PDF 64)',
  'pdf_page': 64,
  'stats': 'Execução: reação; Alcance: pessoal; Alvo: você; Duração: instantânea.',
  'description': 'Invocando a proteção de Khalmyr, você resiste a agressões potencialmente perigosas. Quando '
                 'sofre dano não mágico, você recebe RD 10 contra esse dano.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda a RD para 20. Requer 2° círculo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: além do normal, para cada 10 pontos de dano que a magia reduzir em um '
                            'turno, sua próxima rolagem de dano feita até a próxima rodada causa +1d6 pontos '
                            'de dano de essência.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+1 PM (Apenas Devotos de Khalmyr): muda a execução para padrão e a duração para '
                            'cena, até ser descarregada. Em vez do normal, quando sofre dano não mágico, '
                            'você pode receber RD 10 contra esse dano. A magia é descarregada após você usar '
                            'este efeito pela terceira vez. Requer 3º círculo.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': True},
                   {'id': 'e4',
                    'text': '+2 PM (Apenas Devotos de Khalmyr): muda o alcance para toque e o alvo para 1 '
                            'criatura.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'instantânea',
  'id': 'deuses:instante-estoico'},
 {'name': 'Magia Dadivosa',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 62 (PDF 64)',
  'pdf_page': 64,
  'stats': 'Execução: movimento; Alcance: pessoal; Alvo: você; Duração: cena, até ser descarregada.',
  'description': 'Não é comum descrever uma divindade maior do Panteão como “maluquinha”. Contudo, há '
                 'ocasiões em que Wynna faz por merecer — como quando oferece estas dádivas caóticas. No '
                 'início de seu turno, role 1d4. Em um resultado 4, você recebe 1 PM temporário que só pode '
                 'ser gasto em aprimoramentos de magias. A magia é descarregada quando você recebe um total '
                 'de 4 PM temporários. Você só pode lançar esta magia uma vez por cena.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para curto e o alvo para 1 criatura. Requer 3° círculo.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+0 PM (Apenas Devotos de Wynna): muda a execução para padrão, o ganho para +2 '
                            'PM temporários e o limite para descarregar para +8 PM.',
                    'cost': 0,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena, até ser descarregada',
  'id': 'deuses:magia-dadivosa'},
 {'name': 'Orbe do Oceano',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 62 (PDF 64)',
  'pdf_page': 64,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: sustentada.',
  'description': 'O suposto desaparecimento do Oceano se mostra particularmente misterioso pelo fato de que '
                 'seus devotos ainda podem lançar magias. Você cria um globo protetor de água salgada que '
                 'ocupa 1 quadrado e o acompanha, fornecendo a você camuflagem leve e cobertura leve.',
  'enhancements': [{'id': 'e1',
                    'text': '+4 PM: muda a duração para cena. Requer 3º círculo.',
                    'cost': 4,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM (Apenas Devotos de Oceano): além do normal, você é considerado submerso. '
                            'Isso exige que você prenda a respiração (a menos que possa respirar debaixo '
                            'd’água), mas faz com que sofra apenas a metade do dano de armas de corte e '
                            'impacto que não sejam armas naturais e é considerado submerso para benefícios '
                            'de suas habilidades que dependam dessa situação.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'sustentada',
  'id': 'deuses:orbe-do-oceano'},
 {'name': 'Paixão de Marah',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 62 (PDF 64)',
  'pdf_page': 64,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Você é cercado por uma aura de magnetismo pessoal que o torna mais interessante e atraente '
                 'aos olhos dos demais. Você recebe +2 em perícias originalmente baseadas em Carisma (exceto '
                 'Intimidação).',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para curto e o alvo para 1 criatura.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM (Apenas Devotos de Marah): além do normal, o alvo recebe +1 em Carisma. '
                            'Esse aumento não oferece PV ou PM adicionais.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True},
                   {'id': 'e3',
                    'text': '+3 PM (Apenas Devotos de Marah): muda a duração para 1 dia. Requer 2º círculo.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'deuses:paixao-de-marah'},
 {'name': 'Percepção Rubra',
  'tradition': 'Universal',
  'circle': 1,
  'school': 'Adivinhação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 63 (PDF 65)',
  'pdf_page': 65,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Esta magia faz o conjurador adquirir, por algum tempo, a estranha percepção de tempo dos '
                 'lefeu — que permite ver alguns momentos no futuro. O alvo recebe +1 em testes de ataque, '
                 'em Reflexos e na Defesa.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alcance para curto e o alvo para 1 criatura.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM (Apenas Devotos de Aharadak): aumenta o bônus em +1 (bônus máximo '
                            'limitado pelo círculo máximo de magia que você pode lançar).',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'deuses:percepcao-rubra'},
 {'name': 'Perturbação Sombria',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Ilusão',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 63 (PDF 65)',
  'pdf_page': 65,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Com a proteção de Tenebra, você emana uma aura de sombras com 6m de raio. As sombras se '
                 'movem de formas estranhas, com rangidos e gemidos sem explicação, vultos fugidios nas '
                 'janelas e faces macabras urrando para sumir no instante seguinte. As demais criaturas na '
                 'área sofrem –5 em testes de Percepção. Medo.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o efeito para aura de 9m.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: muda o alcance para toque e o alvo para 1 criatura ou objeto. O alvo '
                            'emana a aura.',
                    'cost': 5,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: você pode escolher quais criaturas são afetadas pela aura. Requer 2º '
                            'círculo.',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+9 PM: muda o alcance para curto, o alvo para área (esfera de 6m de raio), a '
                            'execução para 1 hora, a duração para permanente e adiciona componente material '
                            '(incenso e óleos no valor de T$ 1.000). Requer 5° círculo.',
                    'cost': 9,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+2 PM (Apenas Devotos de Tenebra): adiciona resistência (Vontade parcial). Além '
                            'do normal, criaturas que comecem seu turno dentro da área ficam abaladas. '
                            'Passar no teste de resistência evita a condição e impede que a criatura seja '
                            'abalada por esta magia até o fim da cena. Requer 2° círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'deuses:perturbacao-sombria'},
 {'name': 'Poder de Kallyadranoch',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Evocação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 63 (PDF 65)',
  'pdf_page': 65,
  'stats': 'Execução: movimento; Alcance: pessoal; Alvo: você; Duração: 1 turno.',
  'description': 'Por um breve momento, você manifesta uma pequena parte da força e majestade das grandes '
                 'feras dracônicas: a capacidade de criar elementos em sua forma mais pura. Até o fim do seu '
                 'turno, a CD para resistir às suas habilidades mágicas que causam dano de ácido, '
                 'eletricidade, fogo ou frio aumenta em +2.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta a CD em +1 (bônus máximo limitado pelo círculo máximo de magias '
                            'que você pode lançar). Requer 3° círculo.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM (Apenas Devotos de Kallyadranoch): além do normal, criaturas que falhem '
                            'nos testes de resistência contra suas habilidades mágicas sofrem uma condição '
                            'baseada no tipo de dano. Ácido: vulnerável até o fim da cena. Eletricidade: '
                            'atordoado por 1 rodada (apenas uma vez por cena). Fogo: em chamas e vulnerável '
                            'enquanto estiver em chamas. Frio: lento até o fim da cena. Requer 2° círculo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': '1 turno',
  'id': 'deuses:poder-de-kallyadranoch'},
 {'name': 'Posse de Arsenal',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Convocação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 63 (PDF 65)',
  'pdf_page': 65,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: 1 item empunhado; Duração: 1 dia.',
  'description': 'Esta magia cria um vínculo poderoso entre você e seus pertences, dificultando sua perda ou '
                 'roubo. Você recebe +5 em testes contra as manobras desarmar e quebrar, e de Percepção '
                 'contra punga (veja Ladinagem) para roubá-lo. Além disso, se tiver o item tirado de você '
                 'involuntariamente e ele estiver em alcance curto, você pode invocá-lo às suas mãos com uma '
                 'ação livre.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM (Apenas Devotos de Arsenal): além do normal, você também pode convocar '
                            'uma arma à sua mão mesmo se ela tiver sido arremessada voluntariamente.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': '1 item empunhado',
  'duration': '1 dia',
  'id': 'deuses:posse-de-arsenal'},
 {'name': 'Proteção de Tauron',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 63 (PDF 65)',
  'pdf_page': 65,
  'stats': 'Execução: movimento; Alcance: curto; Alvo: 1 criatura que não você; Duração: cena.',
  'description': 'Esta antiga magia ofertada pelo Deus da Força ainda pode ser lançada mesmo após sua morte, '
                 'preservada por divindades simpatizantes em honra a seu aspecto como protetor dos fracos. '
                 'Quando a magia é lançada, luz sagrada envolve o alvo, que se torna um “protegido”; ele '
                 'recebe +2 na Defesa e, quando se move em sua direção, o deslocamento dele é dobrado. Além '
                 'disso, você sabe a direção e distância do alvo, e também se ele está ferido ou afetado por '
                 'qualquer condição, independentemente da distância. Você não pode lançar esta magia '
                 'enquanto for o “protegido” de outra criatura.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: além do normal, você pode usar habilidades mágicas com alcance de toque '
                            'no alvo como se elas tivessem alcance curto.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o bônus na Defesa em +2 (bônus máximo limitado ao dobro do '
                            'círculo máximo de magia que você pode lançar). Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM (Apenas Minotauros): além do normal, uma vez por rodada, quando uma '
                            'criatura faz uma ação hostil contra o protegido, você pode gastar 1 PM para '
                            'fazer um ataque corpo a corpo contra ela, desde que ela esteja em seu alcance '
                            'pessoal.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'curto',
  'target': '1 criatura que não você',
  'duration': 'cena',
  'id': 'deuses:protecao-de-tauron'},
 {'name': 'Punição do Profano',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Evocação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 63 (PDF 65)',
  'pdf_page': 65,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 humanoide; Duração: instantânea; Resistência: Vontade '
           'reduz à metade.',
  'description': 'Por meio de um brado poderoso, entoando um dogma de sua religião, você inflige dano a '
                 'devotos de divindades adversárias.\n'
                 'Esta magia causa 6d8 pontos de dano de impacto a devotos de deuses que canalizam energia '
                 'oposta a seu deus. Assim, se sua divindade canaliza energia positiva, a magia afeta '
                 'devotos de deuses que canalizem energia negativa, e vice-versa. Devotos de deuses\n'
                 'que canalizam qualquer energia ou criaturas que não sejam devotas sofrem apenas metade do '
                 'dano.\n'
                 'A magia afeta celestiais e abissais como se fossem devotos, respectivamente, de deuses de '
                 'energia positiva e negativa, enquanto suraggel são afetados conforme sua herança. Nesses '
                 'casos, a natureza planar se sobrepõe à devoção (um aggelus devoto de Tenebra ainda é '
                 'considerado de energia positiva).',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: muda o alvo para 1 espírito ou morto-vivo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o dano em +2d8.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: muda o alvo para 1 criatura.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: muda o alvo para criaturas escolhidas. Requer 3° círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 humanoide',
  'duration': 'instantânea',
  'id': 'deuses:punicao-do-profano'},
 {'name': 'Sigilo de Sszzaas',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Abjuração',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 64 (PDF 66)',
  'pdf_page': 66,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: 1 dia.',
  'description': 'Ofertada pelo Deus dos Segredos, esta magia é utilizada por todos que buscam preservar a '
                 'própria privacidade. Pela duração da magia, quaisquer criaturas que fizerem testes de '
                 'perícia para obter alguma informação a seu respeito sofrem –5 nesses testes. Isso inclui '
                 'testes de Percepção para notá-lo, Conhecimento e Investigação para descobrir algo sobre '
                 'você, Intuição para discernir suas mentiras e disfarces, e assim por diante.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o alcance para toque e o alvo para 1 criatura. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: adiciona resistência (Vontade evita). Além do normal, criaturas que usem '
                            'habilidades mágicas de detecção, como a magia Vidência, devem fazer um teste de '
                            'Vontade. Se falharem, a habilidade não funciona e, pela duração da magia, novas '
                            'tentativas de usar a mesma habilidade feitas pela mesma criatura falham '
                            'automaticamente. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM (Apenas Devotos de Sszzaas): muda a penalidade para –10.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': '1 dia',
  'id': 'deuses:sigilo-de-sszzaas'},
 {'name': 'Siroco de Azgher',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Evocação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 64 (PDF 66)',
  'pdf_page': 66,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: instantânea; Resistência: Reflexos '
           'reduz à metade.',
  'description': 'Invocando a fúria do Deus-Sol, você cria uma breve e focada tempestade de areia, capaz de '
                 'esfolar a carne dos ossos! Criaturas afetadas sofrem dano de corte conforme seu grau de '
                 'proteção: 3d6 se estiverem sem armadura, 2d6 se estiverem com armadura leve e 1d6 se '
                 'estiveren com armadura pesada.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o dano em +1d6.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o tipo de dano para luz.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+1 PM: muda o alcance para pessoal e o alvo para área (cone de 9m). Requer 2° '
                            'círculo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+1 PM (Apenas Devotos de Azgher): além do normal, criaturas que falhem na '
                            'resistência ficam em chamas e sangrando.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'deuses:siroco-de-azgher'},
 {'name': 'Sorriso da Fortuna',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Evocação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 64 (PDF 66)',
  'pdf_page': 66,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: 1 dia, até ser descarregada.',
  'description': 'Variantes desta magia, com diferentes nomes, são concedidas por Nimb, Hyninn, Sszzaas, '
                 'Valkaria e até Thyatis. O objetivo, contudo, é sempre o mesmo: trapacear em jogos. Sorriso '
                 'da Fortuna permite manipular os resultados de um jogo de azar. Quando fizer um teste de '
                 'Jogatina (ou relacionado a algum jogo, a critério do mestre) você pode rolar dois dados e '
                 'usar o melhor resultado. A magia é descarregada após você usar esse efeito três vezes.\n'
                 'Esta magia afeta apenas jogos e itens mundanos, não mágicos. Além disso, embora funcione '
                 'bem em pequenas tavernas, grandes cassinos empregam vigilantes atentos ao uso desta magia '
                 'e suas variações.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta em +1 o total de usos antes de a magia ser descarregada.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda a execução para reação, o alcance para curto e o alvo para 1 '
                            'criatura. Além disso, você lança a magia usando apenas concentração '
                            '(Tormenta20, p. 170). Em vez do normal, a magia confunde um dos jogadores '
                            'presentes, que rola seu teste de Jogatina com dois dados e usa o pior '
                            'resultado.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+3 PM: além do normal, você pode escolher um “número da sorte”. Se o número da '
                            'sorte for rolado em qualquer um dos dados, o resultado conta como um 20 '
                            'natural. Requer 2° círculo. Grande parte das magias neste capítulo trazem o '
                            'nome de um deus no título. Isso significa que a magia é tipicamente ofertada '
                            '(ou foi criada) por aquela divindade. Mas então, sendo devoto de outra fé, '
                            'ainda posso aprendê-la e lançá-la? A resposta é sim. Embora existam rivalidades '
                            'e inimizades, deuses maiores ainda formam um Panteão, são irmãos unidos sob uma '
                            'mesma liderança. Poderes divinos são exclusivos, mas magias não (exceto quando '
                            'sua descrição diz o contrário). Além disso, apesar de suas naturezas díspares, '
                            'deuses são orgulhosos e vaidosos. Ficam satisfeitos quando devotos de outros '
                            'entoam seu nome, recorrem a seus milagres. A divindade padroeira, contudo, '
                            'talvez se aborreça um pouquinho... Como regra opcional, quando você lança uma '
                            'magia com o nome de um deus inimigo ou rival, o mestre pode estabelecer que '
                            'essa transgressão cobra um pequeno preço. Se falhar em um teste de Religião (CD '
                            '20) para conseguir perdão adequado, você sofre –2 em seu próximo teste de '
                            'perícia e recebe uma breve visão de sua divindade, levemente desapontada...',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+1 PM (Apenas Devotos de Hyninn): muda a execução para reação e a duração para '
                            'instantânea. Em vez do normal, quando faz seu primeiro teste de uma perícia em '
                            'uma cena, você pode rolar dois dados e usar o melhor resultado.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': '1 dia, até ser descarregada',
  'id': 'deuses:sorriso-da-fortuna'},
 {'name': 'Toque de Megalokk',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Transmutação',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 65 (PDF 67)',
  'pdf_page': 67,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Criaturas de Allihanna seguem leis naturais. Monstros existem para violar essas leis. Após '
                 'deformações horrendas, você se transforma em uma criatura do tipo monstro. Nessa forma, '
                 'você recebe +5 em Intimidação, mas sofre –5 nas demais perícias baseadas em Carisma. Além '
                 'disso, recebe uma arma natural de um tipo a sua escolha entre chifre, ferrão e mordida '
                 '(dano 1d6, crí-\n'
                 'tico x2, perfuração). Uma vez por rodada, quando usa a ação agredir para atacar com outra '
                 'arma, pode gastar 1 PM para fazer um ataque corpo a corpo extra com essa arma natural.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: a margem de ameaça de suas armas naturais aumenta em +1.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: o dano de suas armas naturais aumenta em um passo. Requer 3° círculo.',
                    'cost': 2,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM (Apenas Devotos de Megalokk): além do normal, você recebe redução de dano '
                            '5.Requer 2º círculo.',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'deuses:toque-de-megalokk'},
 {'name': 'Traição da Lâmina',
  'tradition': 'Divina',
  'circle': 2,
  'school': 'Abjuração',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 65 (PDF 67)',
  'pdf_page': 67,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 arma em posse de uma criatura; Duração: cena, até ser '
           'descarregada; Resistência: Vontade (veja texto).',
  'description': 'Provavelmente ofertada por Sszzaas, esta magia amaldiçoa uma arma contra seu usuário. '
                 'Quando faz um ataque com a arma, o usuário deve passar\n'
                 'em um teste de Vontade.\n'
                 'Se falhar, a arma se re-\n'
                 'torce como\n'
                 'uma serpente, ou muda sua trajetó-\n'
                 'ria em pleno\n'
                 'voo; o agressor se torna o alvo do próprio ataque! Após esse ataque, bem-sucedido ou não, '
                 'a magia descarrega e a arma volta ao normal.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: em vez do usuário, a arma se volta para outra criatura em alcance curto '
                            'que você possa perceber, a sua escolha.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda o alvo para 1 arma e a duração para 1 dia, até ser descarregada. '
                            'Requer 3° círculo.',
                    'cost': 1,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+2 PM: aumenta o número de alvos em +1.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+2 PM: adiciona componente material (uma dose de veneno). Além do normal, o '
                            'ataque envenena o usuário com o veneno utilizado como componente (a CD desse '
                            'veneno é a CD da própria magia).',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 arma em posse de uma criatura',
  'duration': 'cena, até ser descarregada',
  'id': 'deuses:traicao-da-lamina'},
 {'name': 'Traição Mágica',
  'tradition': 'Universal',
  'circle': 2,
  'school': 'Abjuração',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 65 (PDF 67)',
  'pdf_page': 67,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: instantânea; Resistência: Vontade '
           'reduz à metade.',
  'description': 'Esta magia desestabiliza outras magias ativas no alvo, fazendo com que elas causem uma '
                 'súbita descarga de energia mística. Para cada círculo das magias afetando o alvo, ele '
                 'sofre 1d8 pontos de dano de essência. Um alvo sob efeito de Velocidade e Voo (2º e 3º '
                 'círculos) sofre 5d8 pontos de dano.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: muda o alvo para criaturas escolhidas. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+3 PM: muda a resistência para nenhuma. Requer 3º círculo.',
                    'cost': 3,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'deuses:traicao-magica'},
 {'name': 'Voz da Razão',
  'tradition': 'Divina',
  'circle': 1,
  'school': 'Encantamento',
  'book': 'deuses',
  'source': 'Deuses de Arton, p. 65 (PDF 67)',
  'pdf_page': 67,
  'stats': 'Execução: padrão; Alcance: pessoal; Alvo: você; Duração: cena.',
  'description': 'Iluminada por Tanna-Toh, sua mente transborda de argumentos e informações. Você recebe +5 '
                 'em Conhecimento, Diplomacia e\n'
                 'Intimidação.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda o bônus para +10. Requer 2º círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM (Apenas Devotos de Tanna-Toh): além do normal, você recebe +5 em Intuição '
                            'e em testes de Investigação para interrogar.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'cena',
  'id': 'deuses:voz-da-razao'},
 {'name': 'Açoite Flamejante',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Convocação',
  'book': 'ameacas',
  'source': 'Ameaças de Arton v1.0, p. 404 (PDF 406)',
  'pdf_page': 406,
  'stats': 'Execução: padrão; Alcance: pessoal; Efeito: açoite de chamas criado em sua mão (veja texto); '
           'Duração: sustentada; Resistência: Reflexos reduz parcial.',
  'description': 'Um açoite de fogo surge em uma de suas mãos com a qual possa empunhar uma arma (essa mão '
                 'fica ocupada pela duração da magia). Você pode usar uma ação padrão para causar 2d6 pontos '
                 'de dano de fogo com o açoite em uma criatura em alcance curto e deixá-la em chamas e '
                 'enredada enquanto estiver em chamas dessa forma. Passar na resistência reduz o dano à '
                 'metade e evita as chamas.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: muda a execução para movimento.',
                    'cost': 2,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: muda o dano para 4d6. Requer 2° círculo.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM: muda o dano para 6d6. Requer 3° círculo.',
                    'cost': 5,
                    'min_circle': 3,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'effect': 'açoite de chamas criado em sua mão (veja texto)',
  'duration': 'sustentada',
  'id': 'ameacas:acoite-flamejante'},
 {'name': 'Dardo Gélido',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Evocação',
  'book': 'ameacas',
  'source': 'Ameaças de Arton v1.0, p. 404 (PDF 406)',
  'pdf_page': 406,
  'stats': 'Execução: padrão; Alcance: curto; Alvo: 1 criatura; Duração: instantânea; Resistência: Fortitude '
           'parcial.',
  'description': 'Você dispara um dardo de gelo contra o alvo, que sofre 2d6 pontos de dano de frio e fica '
                 'lento por 1 rodada. Passar no teste de resistência reduz o dano à metade e evita a '
                 'condição.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o dano em +1d6.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: aumenta o número de alvos em +1 (total de alvos limitado pelo círculo '
                            'máximo de magia que você pode lançar).',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'curto',
  'target': '1 criatura',
  'duration': 'instantânea',
  'id': 'ameacas:dardo-gelido'},
 {'name': 'Invocar Fagulha Elemental',
  'tradition': 'Arcana',
  'circle': 2,
  'school': 'Convocação',
  'book': 'ameacas',
  'source': 'Ameaças de Arton v1.0, p. 404 (PDF 406)',
  'pdf_page': 406,
  'stats': 'Execução: completa; Alcance: curto; Efeito: familiar elemental; Duração: sustentada.',
  'description': 'Você transforma uma porção de um elemento inerte em uma criatura elemental Pequena do tipo '
                 'do elemento alvo. Por exemplo, lançar esta magia em um copo de água cria um elemental da '
                 'água. Você pode criar elementais do ar, da água, do fogo e da terra com esta magia. O '
                 'elemental obedece a todos os seus comandos e funciona como um familiar comum (veja '
                 'Familiares, em Tormenta20, p. 38) ou elemental (veja Elementais). O elemental auxilia '
                 'apenas você e não conta em seu limite de parceiros.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: além do normal, o elemental fornece redução 10 contra o dano '
                            'correspondente a seu tipo.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: em vez do normal, o elemental recebe a habilidade de dois familiares, um '
                            'comum e um elemental.',
                    'cost': 2,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False}],
  'range': 'curto',
  'effect': 'familiar elemental',
  'duration': 'sustentada',
  'id': 'ameacas:invocar-fagulha-elemental'},
 {'name': 'Jato Corrosivo',
  'tradition': 'Arcana',
  'circle': 1,
  'school': 'Evocação',
  'book': 'ameacas',
  'source': 'Ameaças de Arton v1.0, p. 404 (PDF 406)',
  'pdf_page': 406,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: linha de 9m; Duração: instantânea; Resistência: '
           'Reflexos reduz à metade.',
  'description': 'Você dispara um jato, que causa 2d6 pontos de dano de ácido às criaturas na área. Contra '
                 'construtos e objetos soltos, a magia causa +1 ponto de dano por dado.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o dano em +1d6.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+1 PM: muda a resistência para Reflexos parcial. Se passar, a criatura reduz o '
                            'dano à metade; se falhar, fica vulnerável.',
                    'cost': 1,
                    'min_circle': 1,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'linha de 9m',
  'duration': 'instantânea',
  'id': 'ameacas:jato-corrosivo'},
 {'name': 'Katana Celestial',
  'tradition': 'Divina',
  'circle': 5,
  'school': 'Evocação',
  'book': 'ameacas',
  'source': 'Ameaças de Arton v1.0, p. 404 (PDF 406)',
  'pdf_page': 406,
  'stats': 'Execução: padrão; Alcance: pessoal; Área: linha de 60m ou duas linhas de 30m; Duração: '
           'instantânea; Resistência: Reflexos parcial.',
  'description': 'Um golpe vindo dos céus risca o campo de batalha. Se escolher duas linhas, cada uma deve '
                 'seguir em uma direção diferente, criando um corte em “V”. Criaturas na área sofrem 12d8 '
                 'pontos de dano de luz (ou 12d12, se forem mortos-vivos) e ficam cegas e surdas até o fim '
                 'da cena (Reflexos reduz à metade e evita as condições).',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: aumenta o dano em +2d8 (ou +2d12 contra mortos-vivos).',
                    'cost': 3,
                    'min_circle': 5,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+6 PM: muda a área para uma linha de 120m ou quatro linhas de 30m em direções '
                            'opostas, formando um “X”.',
                    'cost': 6,
                    'min_circle': 5,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'area': 'linha de 60m ou duas linhas de 30m',
  'duration': 'instantânea',
  'id': 'ameacas:katana-celestial'},
 {'name': 'Momento de Tormenta',
  'tradition': 'Universal',
  'circle': 2,
  'school': 'Convocação',
  'book': 'ameacas',
  'source': 'Ameaças de Arton v1.0, p. 404 (PDF 406)',
  'pdf_page': 406,
  'stats': 'Execução: completa; Alcance: pessoal; Área: cubo de 30m; Duração: sustentada; Resistência: veja '
           'texto.',
  'description': 'Uma nuvem rubra surge acima do conjurador. Uma vez por turno, você pode gastar uma ação de '
                 'movimento para fazer a nuvem manifestar um dos fenômenos a seguir.\n'
                 'Chuva ácida. Gotas corrosivas causam 6d4 pontos de dano de ácido em todas as criaturas na '
                 'área.\n'
                 'Neblina venenosa. Uma neblina faz com que todas as criaturas na área percam 2d12 PV por '
                 'veneno (Fortitude evita).\n'
                 'Raios escarlates. Até 6 inimigos aleatórios na área sofrem 6d8 pontos de dano de '
                 'eletricidade (Reflexos reduz à metade).\n'
                 'Pesadelos reais. Cada criatura na área sofre 4d6 pontos de dano psíquico e perde 1d4 PM '
                 '(Vontade reduz o dano à metade e evita a perda de PM).\n'
                 'Esta magia só pode ser aprendida e lançada por conjuradores que tenham observado uma área '
                 'de Tormenta pelo menos uma vez. Sua divulgação é proibida e seu uso é permitido apenas em '
                 'áreas controladas na Academia Arcana e outros lugares restritos, para estudar o fenômeno '
                 'da Tormenta. Usar esta magia em\n'
                 'qualquer outro ponto do Reinado é um crime enquadrado na décima-primeira infração do '
                 'Vigintílogo.',
  'enhancements': [{'id': 'e1',
                    'text': '+3 PM: aumenta o dano em +1 dado do mesmo tipo.',
                    'cost': 3,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+5 PM: além do normal, criaturas na área ficam alquebradas enquanto '
                            'permanecerem na área.',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+5 PM (Apenas Devotos de Aharadak): muda a área para círculo de 1km de raio.',
                    'cost': 5,
                    'min_circle': 2,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': True}],
  'range': 'pessoal',
  'area': 'cubo de 30m',
  'duration': 'sustentada',
  'id': 'ameacas:momento-de-tormenta'},
 {'name': 'Transformação em Dragão',
  'tradition': 'Arcana',
  'circle': 4,
  'school': 'Transmutação',
  'book': 'ameacas',
  'source': 'Ameaças de Arton v1.0, p. 405 (PDF 407)',
  'pdf_page': 407,
  'stats': 'Execução: completa; Alcance: pessoal; Alvo: você; Duração: sustentada.',
  'description': 'Esta magia invoca o poder de um dragão, causando mutações no conjurador que o tornam '
                 'semelhante a uma criatura dracônica. Você recebe +2 em Força, Constituição, Inteligência e '
                 'Carisma (esse aumento não oferece PV, PM ou perícias adicionais), +5 na Defesa e redução '
                 '30 contra o elemento do sopro do dragão cujo componente material você usou. Uma vez por\n'
                 'rodada, você pode gastar uma ação padrão para exalar um sopro que causa 8d6+8 pontos de '
                 'dano do elemento correspondente em um cone de 9m (Reflexos reduz à metade). Componente '
                 'Material: uma peça de couro de dragão ou uma escama de dragão no valor de T$ 1.000.',
  'enhancements': [{'id': 'e1',
                    'text': '+2 PM: aumenta o dano do sopro em +1d6+1.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e2',
                    'text': '+2 PM: aumenta o bônus na Defesa em +1.',
                    'cost': 2,
                    'min_circle': 4,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e3',
                    'text': '+6 PM: além do normal, asas de couro brotam de suas costas. Você recebe '
                            'deslocamento de voo 18m.',
                    'cost': 6,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False},
                   {'id': 'e4',
                    'text': '+3 PM: você recebe uma arma natural de mordida (1d6, crítico x2, corte). Uma '
                            'vez por rodada, quando usa a ação agredir para atacar com outra arma, você pode '
                            'gastar 1 PM para fazer um ataque corpo a corpo extra com a mordida. Se já '
                            'possuir uma mordida, em vez disso seu dano aumenta em dois passos.',
                    'cost': 3,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': True,
                    'restricted': False},
                   {'id': 'e5',
                    'text': '+3 PM: o bônus em atributos se torna +4.',
                    'cost': 3,
                    'min_circle': 4,
                    'repeatable': False,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'pessoal',
  'target': 'você',
  'duration': 'sustentada',
  'id': 'ameacas:transformacao-em-dragao'},
 {'name': 'Preparação de Batalha',
  'tradition': 'Universal',
  'circle': 2,
  'school': 'Convocação',
  'book': 'npcs',
  'source': 'Guia de NPCs, p. 17 (PDF 19)',
  'pdf_page': 19,
  'stats': 'Execução: padrão; Alcance: toque; Alvo: até dois itens que você possua, entre armas, armaduras e '
           'escudos; Duração: permanente até ser descarregada; Custo Adicional: penalidade de 1 PM.',
  'description': 'Esta magia é utilizada por clérigos e bardos que não precisam (ou não podem) estar sempre '
                 'com suas armas ou armaduras. A magia é lançada sobre até dois itens que você possua. A '
                 'partir daí, em qualquer momento, você pode usar uma ação completa para convocar os itens, '
                 'que aparecem sobre seu corpo e em suas mãos (conforme apropriado ao item). O efeito é '
                 'espalhafatoso, sendo praticamente impossível utilizá-lo sem chamar atenção. A magia '
                 'funciona independentemente da distância dos itens, desde que estejam no mesmo Plano, mas '
                 'termina se você perder a posse deles.',
  'enhancements': [{'id': 'e1',
                    'text': '+1 PM: aumenta o número de alvos em dois e o custo adicional em +1 PM.',
                    'cost': 1,
                    'min_circle': 2,
                    'repeatable': True,
                    'exclusive': False,
                    'restricted': False}],
  'range': 'toque',
  'target': 'até dois itens que você possua, entre armas, armaduras e escudos',
  'duration': 'permanente até ser descarregada',
  'id': 'npcs:preparacao-de-batalha'}]
