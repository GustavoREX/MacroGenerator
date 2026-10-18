# Macro x Token — 0.02.2.0

Macro Generator e TokenForge em um único aplicativo Windows.

Nesta versão: gerenciamento de inventário com o SHOPING e criação de armas,
armaduras e escudos com melhorias, materiais e encantamentos.

A maior aposta, juntei um programa que fiz a uns 6 meses atras e desenterrei com esse que estava a um tempo arrumando.

Sim usei IA pra me ajudar, os dois programas originais eram meus então eu faço o que eu bem entender.
Dito isso, as versões dos programas originais ainda estão no git. podem ser utilizadas. e se quiser pode mecher a vontade.

Esse aqui é a maior mudança do Macro Generator, onde tambem vai trazer uma edição de token em tempo real, com bordas e estilos customisados. E eu devo dizer, estou feliz com o que foi criado.

Em **Componentes → Armas**, o catálogo contém as 144 armas das cinco abas do
compilado Tormenta20: simples, marciais, exóticas, de fogo e mágicas. O ícone ⓘ
mostra preço, dano, crítico, multiplicador, descrição e fonte. A busca ignora
acentos; armas híbridas e adaptáveis permitem escolher o modo antes de preencher
a macro. Armas duplas preenchem um ataque de uma ponta.

Nas armas mágicas, os valores aplicados são os da arma-base identificada na
descrição. Melhorias, materiais, encantos e efeitos condicionais devem ser
ajustados no editor. Dados ausentes permanecem vazios para preenchimento manual.
O catálogo acompanha o programa e dispensa Excel. Para atualizá-lo a partir de
outra versão da mesma planilha, execute
`python tools/import_weapon_catalog.py "caminho/Compilado-de Itens_Tormenta20.xlsx"`.
Para verificar catálogo e integração com o editor, execute
`python -m unittest discover -s tests -v`.

O botão **⚡ Iniciativa** copia a macro de iniciativa com envio ao rastreador
de turnos. A engrenagem permite personalizar o título, Orgulho e o efeito de
pergunta, como nos botões de Perícias e Resistências. Os bônus são inseridos
antes de `&{tracker}`.

Em **Inventário → 🗡️ Crie sua arma**, escolha uma das 103 armas não mágicas e
monte sua configuração final nas abas de melhorias, material e encantamentos.
Os catálogos da planilha oferecem 24 melhorias de armas, 14 materiais e 51
encantamentos, com descrições no ⓘ. A construção da parte que causa dano é
informada para validar materiais de metal ou madeira; opções incompatíveis
indicam o motivo. Melhorias e encantamentos dependentes aparecem recuados logo
abaixo de seus pré-requisitos, ficando cinza até que eles sejam selecionados.
Remover o pré-requisito também desmarca suas opções dependentes.
Há limite de quatro melhorias (material incluso), três
encantamentos e um único material, inclusive para Prata.

Para modificar uma arma que já possui, marque **Já possuo esta arma**, informe
as quantidades anteriores e selecione a configuração final **incluindo as
melhorias e encantos anteriores**. O orçamento mostra o preço final e o valor
a pagar agora: desconta a progressão anterior, não cobra a arma-base de novo e
mostra os acréscimos às CDs de melhorias e encantamentos separadamente. Na troca
de material, cobra todo o valor do novo material sem reembolsar o anterior;
manter o mesmo material não o cobra outra vez. Preços-base ausentes e materiais
sem preço de mercado exigem um valor informado pelo usuário, inclusive zero
quando o item ou as peças forem gratuitos.

Pequena, padrão, aumentada e colossal alteram o dano em −1, 0, +1 e +2 passos.
Adamante e demais efeitos suportados usam as mesmas trilhas do calculador de
passos. Casos fora dessas trilhas permitem informar o dano final manualmente.
**Gerar macro de arma** retorna ao Macro Generator com os bônus, dano, crítico,
tipos e descrição preenchidos. Danos elementais passivos ficam em Efeito extra,
somente com o dado ou valor, sem rótulos de elemento, e não recebem o
multiplicador do crítico. Os elementos continuam no campo de tipo de dano.
A descrição da macro contém apenas o total de RD ignorada e lembretes curtos
com nome, custo e efeito das ativações por PM. As descrições completas ficam
nos ícones de informação do catálogo.
A configuração é preservada ao trocar entre telas durante a sessão.

Para reimportar os catálogos de customização, execute
`python tools/import_crafting_catalog.py "caminho/Compilado-de Itens_Tormenta20.xlsx"`.

**Inventário → 🛡 Crie sua Armadura** abre o criador com 30 armaduras e escudos
da tabela, sem os itens mágicos específicos. Mostra Defesa, penalidade, espaços,
proteções e orçamento. Os materiais usam os adicionais da categoria correta:
armadura leve, pesada ou escudo. Mantém os descontos de progressão para um item
já possuído e a cobrança integral do novo material em uma substituição.

Escudos compartilham **um único limite de quatro melhorias e três encantamentos**
entre defesa e ataque, incluindo o material. Opções ofensivas ficam disponíveis
nos escudos que podem atacar; opções exclusivas de armadura ficam bloqueadas.
Escudos de vime e torre não atacam. Broquel usa o ataque de escudo leve e sagna
o de escudo pesado. Defesa e dano são calculados separadamente; Espinhoso,
Esmagador, materiais e tamanhos modificam o ataque, enquanto as proteções
permanecem na ficha do escudo. Balístico e o dano de Cáustica exigem marcar a
ativação correspondente, pois consomem bala ou PM. Encantos explicitamente
marcados na tabela como dois encantos ocupam dois espaços do limite de três.

Armaduras e escudos sem ataque exibem suas informações, efeitos e preços na
própria tela, sem ações de copiar ficha ou gerar macro. Para escudos que atacam,
**Gerar macro de ataque do escudo** retorna ao editor com o escudo customizado.
Os criadores de arma e armadura preservam configurações
independentes ao navegar entre as telas durante a sessão.

**Inventário → 🛒 SHOPING** reúne 842 itens em 27 catálogos, com botões por
categoria, busca sem acentos, páginas e informações completas nos ícones ⓘ.
Os botões **Armas**, **Armaduras e escudos** e **Esotéricos** expandem suas
subcategorias, incluindo as versões mágicas. As demais categorias continuam
acessíveis diretamente.
Inclui armas, armaduras, escudos, munições, consumíveis, itens mágicos, animais,
veículos, serviços e os itens especiais sem preço. Melhorias, materiais usados
como modificadores, encantamentos e maldições ficam nos criadores; o fardo de
matéria-prima comercial continua disponível nas compras.

Clique no nome, no preço ou no cartão do item, ou use **+**, para adicionar uma
unidade ou pacote (por exemplo, Virotes (20)). O ⓘ abre apenas as informações. Em
**Meu inventário**, ajuste a quantidade, use +1/−1 ou remova o item. O resumo
mostra gasto, valor dos itens e carga em **espaços**, conforme a tabela. Itens
sem preço fixo aparecem em vermelho como especiais. Preços variáveis e cargas
ausentes ficam pendentes e deixam os totais explicitamente parciais; selecione
o item e preencha preço/carga por unidade para completar o orçamento. Zero é
aceito quando não houver custo ou carga. Animais, serviços e outros itens
marcados com travessão na coluna de espaços não acrescentam carga transportada.
O SHOPING soma os espaços dos itens; não calcula capacidade do personagem ou
redistribuição entre mochilas, montarias e veículos.

Os dois criadores oferecem **Adicionar no inventário**, inclusive para
armaduras sem ataque. Cada configuração é preservada com seus efeitos,
proteções, dano, preço completo e **valor a pagar agora**. O gasto usa esse
último valor para respeitar os descontos de itens já possuídos; o valor completo
aparece separadamente. Configurações iguais aumentam a quantidade, enquanto
configurações diferentes, mesmo com o mesmo nome, são itens separados.
Elas também ficam no catálogo **Customizados** para adicionar novas unidades.

**Limpar**, disponível no catálogo e ao lado de **Remover**, esvazia as compras.
Se houver customizados, pergunta se devem ser excluídos também: **Sim** remove
todas as compras e os modelos salvos no catálogo Customizados; **Não** remove
apenas os itens comuns e preserva os customizados; **Cancelar** mantém tudo.
As configurações que estiverem abertas nos criadores continuam disponíveis.
A roda do mouse rola os painéis dos criadores e do SHOPING sobre seus textos,
cartões e controles, mesmo com a página da macro oculta no aplicativo integrado.

O inventário é salvo automaticamente em
`%LOCALAPPDATA%\MacroGenerator\inventory.json` e restaurado ao abrir o SHOPING.
Para atualizar seus catálogos a partir da mesma estrutura de planilha, execute
`python tools/import_shopping_catalog.py "caminho/Compilado-de Itens_Tormenta20.xlsx"`.
O programa usa os dados incluídos e não depende de Excel nem altera a planilha.

Para compilar, execute `setup.bat` uma vez e depois `build_macro_generator.bat`
(ou `build_macro_generator.bat clean` para refazer o cache do PyInstaller).
O script valida os fontes, executa os testes, compila o atualizador e o aplicativo
com os catálogos incluídos e verifica o executável antes de preparar a release.
O resultado desta versão fica em `release\MacroXToken.V0.02.2.0.exe`.
Caches, ambientes locais, relatórios e executáveis gerados não entram no Git.
