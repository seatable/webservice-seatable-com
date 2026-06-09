---
title: 'SeaTable 3.5: Fórmulas na primeira coluna, novas acções de automatização e todo o tipo de guloseimas - SeaTable'
description: 'Use fórmulas na chave, automatize links e processing, acione botões/lookups com condições, sequência lógica garantida. Monte apps sem programação, pinte com cores próprias, importe de outras bases: mais potência, flexibilidade e visual para equipes competitivas.'
date: 2023-04-12
lastmod: '2023-09-04'
author: 'kgr'
url: '/pt/seatable-release-3-5'
color: '#f3fa61'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 3.5: fórmulas, automações, app builder'
    description: 'Fórmulas na primeira coluna, automações avançadas, botões e lookups condicionais, App Builder beta—SeaTable 3.5 evoluiu!'
---

Abril faz o que quer - mas SeaTable faz o que você quer! A versão 3.5 responde a alguns desejos há muito acalentados dos nossos utilizadores: a primeira coluna agora também suporta [fórmulas]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) e através da [automatização]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}) pode ter duas acções adicionais executadas periodicamente. Ganha mais flexibilidade para casos de utilização mais exigentes com a execução condicional de [acções de botões]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) e a [procura]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}) condicional. A seguir, apresentamos estas melhorias em detalhe.

Com este lançamento, estamos também a publicar um novo App Builder como um beta. Com o Universal App Builder, as aplicações podem ser construídas para uma grande variedade de casos de utilização e grupos de utilizadores sem qualquer conhecimento de programação. Neste momento, a nossa equipa de desenvolvimento ainda está a afiná-lo, mas mesmo o antegosto faz-nos querer mais. Aguardamos o seu feedback!

Esta manhã actualizámos a SeaTable Cloud para a versão 3.5. Todos os auto-gestores podem fazer o mesmo: A imagem SeaTable 3.5 está disponível para download a partir do conhecido [repositórioDocker](https://hub.docker.com/r/seatable/seatable-enterprise) . Como sempre, é possível encontrar a lista completa de alterações no [changelog]({{< relref "pages/changelog" >}}).

## Fórmulas na primeira coluna

A SeaTable 3.5 proporciona mais flexibilidade na primeira coluna da tabela: Até agora, apenas os [tipos de coluna]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) texto, número, data, selecção única e número automático eram aí permitidos. O [tipo de coluna de fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}), que agora também é suportado, torna possível "calcular" a sua própria referência de linha. Uma vez que a [primeira coluna]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}) de uma tabela não pode ser escondida e é também sempre exibida no diálogo da ligação, é particularmente adequada para este fim.

No editor de fórmulas, basta introduzir a coluna a referenciar entre parênteses rectos. _por exemplo, _{número do produto}** obtém o valor da coluna "Número do produto". Pode concatenar vários valores de coluna com **&**. Naturalmente, também pode utilizar funções de texto como **left()\*\* para truncar valores. Por exemplo, se gerir facturas numa tabela, uma referência de linha que consista na data da fatura, nome do cliente e número da fatura pode ter o seguinte aspeto _20230412-CustomerZ-INV202302347_.

![SeaTable 3.5 - Fórmulas de suporte da primeira coluna](SeaTable-3.5-FirstColumn.png)

## Duas acções adicionais para automatizações periódicas

As [automatizações]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}}) no SeaTable tornam a sua vida mais fácil, aliviando-o de muitos cliques manuais. Consequentemente, as automatizações não só lhe poupam tempo, como também minimizam o número de erros humanos. SeaTable tem quatro [automatismos]({{< relref "help/base-editor/automationen/automations-trigger" >}}) que lhe permitem realizar várias [acções de automatização]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) com base num evento (por exemplo, é adicionada uma nova entrada) ou periodicamente (por exemplo, todas as segundas-feiras às 10 da manhã). O SeaTable 3.5 torna as automatizações periódicas muito mais potentes, acrescentando mais duas acções.

Pode agora seleccionar as acções "Adicionar ligações" e "Executar operação de processamento de dados" para o disparo periódico, para além das acções "Enviar notificação", "Enviar e-mail", "Adicionar linha" e "Executar script Python". Estas duas acções podem ser utilizadas para executar automaticamente todas as operações de processamento de dados que anteriormente só podiam ser executadas manualmente.

Veja por si próprio o que é possível com [operações de processamento de dados em SeaTable]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}).

## Execução condicional de acções de botão

Com um [botão]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) pode executar uma ou mais acções com um clique, por exemplo, [enviar um e-mail]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) e depois editar a linha. Não foi possível ligar a execução de uma acção a uma condição. Fechámos esta lacuna funcional com o SeaTable 3.5.

![SeaTable 3.5 - As acções dos botões podem ser ligadas a regras](SeaTable-3.5-ConditionalExecution.png)

A nova execução condicional permite definir uma regra para cada acção de botão. Uma regra pode consistir em uma ou mais condições. Apenas se a regra for cumprida, a acção será executada quando o botão for clicado. Se uma condição não se aplicar, o SeaTable salta para a acção seguinte e exibe a acção não executada numa mensagem.

Imagine que quer enviar e-mails aos seus clientes em diferentes línguas. Por exemplo, a versão inglesa só deve ser enviada se o inglês for definido como a língua do cliente numa coluna. Até agora, precisava de um botão separado para isso. Graças à execução condicional, um único botão é agora suficiente para qualquer número de línguas. Basta adicionar ao botão tantas acções de "Enviar correio electrónico" quantas as que desejar utilizar idiomas e fornecer-lhes as regras apropriadas. Uma vez definidas as regras, SeaTable só enviará o e-mail na língua do respectivo cliente quando o botão for clicado.

A partir da versão 3.5, SeaTable executa todas as acções definidas de forma estritamente sequencial. Enquanto uma acção não for concluída, a acção seguinte não é iniciada. Isto assegura que uma acção demorada (por exemplo, a criação de um PDF) é concluída antes de se iniciar outra acção (por exemplo, o envio de um e-mail ao qual o PDF deve ser anexado).

## Pesquisa condicional na coluna Fórmula para links

O tipo de coluna Fórmula para ligações permite a avaliação de entradas ligadas. Estão disponíveis um total de cinco métodos de avaliação: [Findmin]({{< relref "help/base-editor/formeln/die-findmin-formel" >}}), [Findmax]({{< relref "help/base-editor/formeln/die-findmax-formel" >}}), [Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}}), [Countlinks]({{< relref "help/base-editor/formeln/die-countlinks-formel" >}}) e [Lookup]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}). A fórmula de Lookup permite exibir valores adicionais de linhas já ligadas na sua tabela actual. Desta forma, pode ler e exibir tanta informação quanto desejar a partir da tabela ligada.

![SeaTable 3.5 - Colunas de fórmula de ligação suportam pesquisas condicionais](SeaTable-3.5-ConditionalLookup.png)

No SeaTable 3.5 melhorámos a fórmula de pesquisa e implementámos uma função que já existe há algum tempo nas outras fórmulas: uma avaliação condicional. Se a avaliação condicional for activada para pesquisas, apenas são exibidos os valores que preenchem a(s) condição(ões) definida(s). Desta forma, obtém-se a informação exacta de que necessita a partir da tabela ligada.

## Construtor universal de aplicações (Beta)

Sempre quis construir as suas próprias aplicações? SeaTable torna agora este sonho realidade: Com o Universal App Builder, pode criar aplicações individuais para grupos de utilizadores com diferentes necessidades de informação (por exemplo, empregados, chefes de departamento, gestores) a partir de uma base. Como backend, basta utilizar a estrutura e os dados numa base, na qual pode colocar tantas frentes quantas desejar para cada grupo de utilizadores.

Na interface gráfica do utilizador, é possível criar páginas, tabelas, formulários web, quadros Kanban, calendários e galerias individualmente adaptados aos grupos de utilizadores. Estas funcionam como na Base, mas com algumas características especiais, tais como opções de visualização predefinidas e imutáveis.

O acesso é através de URL (personalizado) com ou sem login. Ao definir o acesso aberto, pode também tornar os dados acessíveis a terceiros externos sem uma conta SeaTable (por exemplo, clientes, parceiros comerciais) através da aplicação. Actualmente, a nossa equipa de desenvolvimento ainda está a afinar a versão beta, mas a estrutura básica da aplicação universal está em vigor. Experimente-a agora mesmo!

## E muito mais

Para simplificar a transferência de dados de uma base para outra, o SeaTable 3.5 oferece agora a opção conveniente de importar tabelas directamente de outra base e assim transferir dados através dos limites da base.

SeaTable fornece 24 cores para opções de selecção, botões e formatação condicional. Para satisfazer desejos individuais ou requisitos de IC, SeaTable 3.5 permite definir qualquer número de cores adicionais em cada base. Os auto-gerentes também têm a opção de definir cores individuais no SeaTable globalmente através do ficheiro de configuração.

![SeaTable 3.5 - Novo layout para detalhes da linha](SeaTable-3.5-RowDetails.png)

A disposição de uma coluna dos detalhes da linha é substituída por um desenho de duas colunas na nova versão. Isto torna o visor mais curto e claro, especialmente para tabelas com muitas colunas. O registo de base, no qual se pode acompanhar todas as alterações dentro de uma base, também recebe um novo visual. Se clicar em Logs no histórico da base {{< seatable-icon icon="dtable-icon-history" >}}, abre-se uma janela separada com entradas de log claras.

Fizemos as alterações mais importantes à interface do utilizador nos diálogos das colunas de ligação. Para além da largura das colunas, o tamanho das caixas de diálogo também pode ser alterado. Se se quiser esconder colunas irrelevantes, isto também é agora possível. Tal como nas opções de visualização, existe a partir de agora uma opção para ocultar, bem como ordenar as colunas no diálogo "Entradas Ligadas".

## Dois novos limites

Como anunciado nas [últimas Notas de Lançamento]({{< relref "posts/seatable-releases/seatable-release-3-4" >}}), SeaTable 3.5 introduz um limite de 100.000 caracteres para células individuais do tipo [Texto Formatado]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}). Se o texto numa célula exceder 100.000 caracteres (o que corresponde a cerca de 25 páginas A4 de texto), aparecerá uma mensagem de aviso. Se não encurtar o texto e fechar o editor, o SeaTable guarda apenas 100.000 caracteres.

Com a versão 3.5, reduzimos o número máximo de linhas devolvidas numa chamada API de 10.000 para 1.000 para o SeaTable Cloud. Por favor, verifique se isto resulta numa necessidade de ajustamento nas suas integrações.
