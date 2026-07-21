---
title: 'SeaTable 6.2: O código encontra o no-code'
description: 'O SeaTable 6.2 introduz um tipo de página HTML extremamente flexível e outras melhorias no App Builder. Além disso, há novas funções nas colunas de fórmula e nas ligações externas.'
date: 2026-07-13
author: 'rdb'
url: '/pt/seatable-release-6-2'
color: '#dc6165'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 6.2: O código encontra o no-code'
    description: 'SeaTable 6.2: novo tipo de página HTML e outras melhorias no App Builder, bem como novas funções nas colunas de fórmula e nas ligações externas.'
register:
    show: true
---

Com o SeaTable 6.2, o [App Builder]({{< relref "help/app-builder" >}}) ganha um novo tipo de página: as **páginas HTML** permitem criar páginas totalmente personalizadas com base em HTML, JavaScript e CSS. Com isso, deixam de existir praticamente todas as limitações no que toca à visualização de dados. Também os formulários web podem ser concebidos exatamente de acordo com as suas necessidades e mesmo interações complexas se podem implementar sem problemas. O impossível deixou de existir!

De resto, o App Builder também está em destaque na versão 6.2. O tipo de página [Registo único]({{< relref "help/app-builder/seitentypen-in-universellen-apps/seiten-vom-typ-einzelner-datensatz-in-universellen-apps" >}}) recebe de uma só vez uma tripla melhoria: agora todos os valores de coluna podem ser apresentados de forma uniforme como texto, formatados de maneira universal e – um desejo manifestado com frequência – editados diretamente «inline» na página.

Outros [tipos de página]({{< relref "help/app-builder/seitentypen-in-universellen-apps" >}}) beneficiam de uma gestão de permissões alargada para as colunas de ligação. Além disso, pequenos ajustes de design proporcionam maior clareza: as aplicações sem páginas são assinaladas como tal para evitar mal-entendidos e o avatar, incluindo as notificações da aplicação, encontrou um novo lugar.

As [colunas de fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) recebem com o SeaTable 6.2 duas novas capacidades de uma só vez: a nova função **datetimeFormat()** converte valores de data em cadeias de texto com um formato de livre definição. Se o seu formato de data preferido não era oferecido pelo SeaTable até agora, isso passa a ser coisa do passado. Além disso, as fórmulas de texto suportam agora **quebras de linha**, o que torna muito mais flexível a composição de textos a partir de diferentes colunas.

Por último, o SeaTable 6.2 melhora a colaboração: as [ligações externas]({{< relref "help/startseite/freigaben/externer-link-erklaert" >}}) e as [ligações de convite]({{< relref "help/startseite/freigaben/einladungs-link-erklaert" >}}) podem agora ser acompanhadas de uma descrição, de modo que a finalidade e os destinatários previstos possam ser anotados diretamente na ligação. Além disso, o friso para bases e vistas abertas através de ligações externas foi reformulado e tornado mais claro.

O [changelog](https://cloud.seatable.io/dtable/view-external-links/c9124bcd934b47bc8f30/) regista – como sempre – todas as alterações relevantes.

Para o [SeaTable Server]({{< relref "pages/product/seatable-server" >}}), a versão 6.2 está disponível para download a partir de hoje no [repositório Docker do SeaTable](https://hub.docker.com/r/seatable/seatable-enterprise).

A atualização do [SeaTable Cloud]({{< relref "pages/product/seatable-cloud" >}}) ocorre **a 4 de agosto**. Com a atualização, a quota mensal para a [execução de scripts Python]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}) passa a ser dinâmica. À semelhança das chamadas à API ou das automatizações, a quota total de scripts Python fica associada à dimensão de uma equipa. Uma equipa Plus recebe 250 execuções de scripts Python e uma equipa Enterprise 1000 execuções de Python por utilizador e por mês. Na subscrição Free continua a aplicar-se um limite fixo de 100 execuções por mês.

{{< warning headline="Breaking Changes nos scripts Python" >}}

Os valores de retorno do objeto de contexto e do método de consulta para os tipos de coluna Data, Fórmula e Fórmula para ligações são harmonizados na versão 6.2. Isto pode fazer com que a execução dos seus scripts resulte em erros. Por favor, verifique e atualize os seus scripts Python.

{{< /warning >}}

## Novo tipo de página de aplicação: a página HTML

Com o **App Builder do SeaTable** é possível criar aplicações poderosas – sem qualquer programação. Graças aos tipos de página predefinidos, em pouco tempo surge uma aplicação web totalmente funcional. No entanto, esta eficiência tem o seu preço: embora os **10 tipos de página** ofereçam inúmeras possibilidades de configuração, predeterminam a estrutura e o comportamento de uma página. Personalizações individuais que fossem além disso não eram possíveis até agora.

Pretende utilizar um tipo de gráfico que o SeaTable não suporta? Criar um formulário web altamente personalizado? Incorporar um diagrama interativo com elementos clicáveis? Ou combinar várias representações – por exemplo, uma tabela e um registo único – numa só página? Com o novo tipo de página **página HTML**, estes e muitos outros requisitos podem ser concretizados.

![Novo tipo de página de aplicação: a página HTML](HTMLPage.png)

As páginas HTML podem apresentar **conteúdos estáticos**, mas revelam todo o seu potencial em conjugação com os **dados de uma base**. Tal como outros tipos de página do App Builder, podem obter dados de uma base e alterar registos numa base. Já na **conceção da interface do utilizador**, dispõe de uma liberdade quase total. O que se consegue realizar com HTML, CSS e JavaScript pode, em princípio, ser implementado também como página HTML no App Builder.

Não se deixe confundir pelo nome. As páginas HTML suportam não só **HTML**, mas igualmente **JavaScript e CSS**. Todo o código da página é carregado na aplicação como um pacote (bundle). O modo de funcionamento, as possíveis abordagens de desenvolvimento e a referência do respetivo Software Development Kit (SDK) encontram-se no [Manual do programador do SeaTable](https://developer.seatable.com/html-pages/ 'SeaTable Developer Manual'). Aí encontra também um exemplo de página.

Atualmente, este tipo de página destina-se, sobretudo, a **utilizadores com experiência em programação**. Já está em desenvolvimento uma função de IA com a qual, no futuro, as páginas HTML também poderão ser criadas em linguagem natural e sem conhecimentos de programação.

## Tipo de página de aplicação melhorado: Registo único

O tipo de página **Registo único** recebe no SeaTable 6.2 várias melhorias de uma só vez. Até agora, só podia editar registos através dos detalhes da linha, que tinha de abrir primeiro com o botão «Editar entrada». Isto implicava cliques adicionais e uma rutura desnecessária na experiência do utilizador durante o fluxo de edição.

Com o SeaTable 6.2, este passo intermédio fica para trás. Se um utilizador dispuser das permissões de edição necessárias, os campos podem agora ser editados diretamente na página. **Um clique num campo ativa o modo de edição**, as entradas são validadas como habitualmente e as alterações são guardadas de imediato. Isto proporciona um fluxo de trabalho nitidamente mais fluido e intuitivo.

![Edição inline nas páginas de registo único](SingleRecordPage_InlineEditing.png)

Também a apresentação foi alargada. Os **tipos de coluna** com uma representação visual própria – por exemplo, as etiquetas das colunas de [seleção única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) ou de [colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) – podem agora, opcionalmente, ser apresentados como texto simples. Além disso, para todos os valores apresentados como texto está disponível um conjunto uniforme de **opções de formatação**: o tamanho do tipo de letra, a cor do tipo de letra, o alinhamento e o fundo podem ser ajustados de forma coerente, independentemente do tipo de coluna original. Assim, pode conceber páginas com um aspeto uniforme e organizado.

## Permissões alargadas para as ligações na aplicação

O SeaTable 6.2 colmata uma lacuna na gestão de permissões das [colunas de ligação]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) no App Builder. Com a nova permissão **Remover entradas existentes** é possível definir de forma específica se os utilizadores podem eliminar ligações existentes.

Até agora, qualquer utilizador com permissão de edição podia remover ligações existentes. Este comportamento pode agora ser controlado para a coluna de ligação independentemente das restantes [permissões de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}).

![Nova permissão na aplicação: eliminar ligações existentes](AppBuilder_RemoveExistingRecords.png)

Agora pode gerir de forma abrangente os direitos de acesso às colunas de ligação: consoante a configuração, os utilizadores podem criar novos registos na tabela ligada, bem como ligar, alterar e remover registos existentes – cada um com as suas próprias permissões. Isto permite um **controlo nitidamente mais preciso dos direitos de edição nas aplicações**.

## Nova função na coluna de fórmula

A nova função **datetimeFormat()** ajuda-o a apresentar os valores de data exatamente como deles precisa. O primeiro parâmetro contém a data a formatar ou a referência à coluna que contém o valor. No segundo parâmetro, define o formato de destino.

![Fórmula para valores de data formatados](FormulaColumn_datetimeFormat.png)

Nas fórmulas de texto pode agora inserir uma **quebra de linha** com «\n» ou '\n'. Isto é especialmente útil quando concatena várias colunas mas não pretende escrever os valores numa só linha. O exemplo por excelência é um endereço:

![Quebras de linha em fórmulas de texto](FormulaColumn_LineBreak.png)

## Melhorias nas ligações externas e nas ligações de convite

Por último, o SeaTable 6.2 reserva uma otimização para as **ligações externas e as ligações de convite**. Pode agora acompanhá-las de uma **descrição**. Assim, por exemplo, a finalidade e os destinatários previstos podem ser anotados diretamente na ligação. Além disso, reformulámos e tornámos mais claro o friso para bases e vistas abertas através de ligações externas.

## E ainda muito mais

- **Registo da base melhorado**:​ O [registo da base]({{< relref "help/base-editor/historie-und-versionen/aenderungen-ueber-die-logs-rueckgaengig-machen" >}}) foi reformulado em vários pontos. Os campos de pesquisa facilitam a seleção em bases grandes, os menus pendentes apresentam-se com um design uniforme e agora também pode filtrar as ações em tabelas eliminadas.

- **Widget de data melhorado​**: O widget de data foi otimizado no que respeita à utilização e à apresentação e oferece um trabalho ainda mais cómodo com os [valores de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}).

- **Emojis nos comentários​**: Os [comentários]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) suportam agora emojis. Isto torna os retornos, as reações e a colaboração ainda mais expressivos.

## Adaptação dos valores de retorno nos scripts Python

Com o objetivo de harmonizar os formatos, no SeaTable 6.2 são atualizados os valores de retorno de alguns tipos de coluna para o objeto de contexto e o método de consulta. Isto pode exigir a adaptação dos seus scripts Python.

Encontra uma comparação dos valores de retorno no SeaTable 6.1 e no SeaTable 6.2 no [Fórum SeaTable](https://forum.seatable.com/t/important-changes-related-to-python-client-in-seatable-6-2/7435).

Para os scripts executados manualmente, ou seja, os scripts que executa através de um botão ou no editor Python do SeaTable, tem de ter em conta todas as alterações aí mencionadas. Os scripts que são executados por automatização só tem de os adaptar no que respeita às alterações relacionadas com o método de consulta.
