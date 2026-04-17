---
title: 'Páginas da linha de tempo em aplicações de SeaTable'
date: 2023-12-04
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/pt/ajuda/paginas-de-linha-do-tempo-em-apps-seatable'
aliases:
    - '/pt/ajuda/zeitstrahlseiten-in-universellen-apps'
    - '/pt/ajuda/paginas-de-linha-do-tempo-em-apps-universais'
seo:
    title: 'Páginas de linha do tempo em SeaTable Apps'
    description: 'No SeaTable, organize projetos, prazos e férias em timelines dinâmicas nas SeaTable Apps.'
weight: 8
---

Este tipo de página permite-lhe apresentar diferentes períodos de tempo sob a forma de uma **linha cronológica**. Como esta visualização de dados revela datas sobrepostas, **o planeamento de férias numa empresa**, por exemplo, pode ser um caso de utilização específico.

![Página da linha de tempo nas aplicações](images/Timeline-page-in-Universal-Apps.png)

## Definições da página

Se pretender alterar as definições de uma página, clique no **símbolo da roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondente na barra de navegação.

![Alterar as definições da página da linha de tempo](images/Einstellungen-der-Zeitstrahlseite-aendern.png)

Nas **definições da página**, pode começar por definir a representação gráfica das linhas cronológicas. Para tal, selecionar a [cor da linha]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}) ou uma [coluna de seleção individual]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}), que determina a **cor dos blocos**. Também é possível definir uma coluna para a **etiquetagem dos blocos**.

![Definição gráfica das linhas de tempo em aplicações](images/Grafische-Einstellung-der-Zeitleisten.png)

Para definir o período das entradas, você precisa de uma [coluna de data]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) para a **data de início**. Para a **data de término**, você pode usar outra coluna de data ou uma coluna numérica diferente – [número]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}), [duração]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}}) ou [fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) – que indique o número de dias. Além disso, é possível selecionar o **período de tempo**, ou seja, quantos anos a cronologia deve abranger.

![Definições de página da página da linha de tempo em aplicações](images/Seiteneinstellungen-der-Zeitstrahlseite-in-Universellen-Apps.png)

## Filtros predefinidos e colunas ocultas

É possível definir **filtros predefinidos** e **colunas ocultas** para limitar os dados apresentados aos utilizadores. Para tal, clique em **Adicionar filtro**, seleccione a **coluna** e a **condição** pretendidas e confirme com **Enviar**.

![Adicionar filtro nas páginas da linha do tempo em apps](images/Add-filter-on-timeline-pages-in-Universal-Apps.png)

Os utilizadores podem ver mais informações sobre uma entrada clicando num bloco na linha cronológica. Por conseguinte, decida quais os dados que devem ser **visíveis** e mostre ou oculte as colunas correspondentes utilizando os **cursores**.

![Ocultar colunas nas páginas da linha do tempo em apps](images/Hide-columns-on-timeline-pages-in-Universal-Apps.png)

{{< warning  headline="Nota importante"  text="Os utilizadores da aplicação **não podem alterar os filtros predefinidos** e **as colunas ocultas**. Por conseguinte, o utilizador só verá os dados filtrados que desejar." />}}

Se for adicionado um **agrupamento**, as barras também podem ser exibidas em **raias**. Para actividades que não se sobrepõem, esta opção de visualização resulta numa exibição compacta e clara.

![Agrupamento em páginas da linha do tempo](images/Grouping-on-timeline-pages.png)

## Editar ou mover uma entrada na linha de tempo

Pode editar facilmente as entradas clicando numa **barra** e fazendo as alterações desejadas nos **detalhes da linha** que se abrem.

![Alterar entradas nas páginas da linha do tempo](images/Eintraege-auf-Zeitstrahlseiten-aendern.gif)

Também pode **aumentar** ou **diminuir** o **período de tempo** diretamente na linha de tempo. Para o fazer, agarre a **extremidade** direita ou esquerda **da barra** e arraste-a para a data pretendida.

![Mover entradas para páginas da linha do tempo](images/Eintraege-auf-Zeitstrahlseiten-verschieben.gif)

Também pode **mover** convenientemente entradas na linha de tempo **utilizando a função arrastar e largar**. O SeaTable ajusta automaticamente os respectivos **valores de data**.

## Definições da coluna de ligações

Nas **opções da coluna de ligação**, é possível especificar quais os dados visíveis e quais as operações permitidas para cada tabela ligada.

![Ligar definições de coluna em páginas de linha do tempo nas aplicações](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Definições de campo**: Aqui pode definir exatamente a que colunas se aplicam as seguintes autorizações.
- **Adicionar e ligar novos registos**: Se ativar este seletor, os utilizadores podem adicionar novas entradas à tabela ligada. Pode utilizar as definições de campo para definir as colunas que são **visíveis** e as que são **obrigatórias**, ou seja, que têm de ser preenchidas.
- **Ligar registos existentes**: Se ativar esta barra deslizante, os utilizadores podem ligar entradas existentes na tabela ligada. Pode utilizar as definições de campo para definir as colunas que são **visíveis**.
- **Limitar as ligações a um registro máximo**: Se ativar esta barra deslizante, os utilizadores só podem ligar uma linha da tabela ligada nas células da coluna de ligação.
- **Filtros predefinidos**: Se adicionar um filtro aqui, apenas as opções que satisfazem as condições do filtro serão apresentadas ao ligar as entradas.
- **Ativar** a função de grandes volumes de dados: Se a função de grandes volumes de dados estiver activada, os utilizadores podem pesquisar mais de 20.000 registos de dados, desde que existam este número de entradas na tabela ligada.
- **Modificar registos ligados**: Se ativar esta barra deslizante, os utilizadores podem editar as entradas existentes na tabela ligada. Pode utilizar as definições de campo para definir quais as colunas que são **editáveis**.

## Autorizações de páginas

Na parte inferior das definições da página, pode restringir quem pode **ver** a página da linha do tempo e **editar** entradas. Não é possível adicionar ou eliminar linhas através das páginas da linha do tempo.

![Autorizações de páginas para páginas de cronologia](images/Seitenberechtigungen-von-Kalenderseiten.png)
