---
title: 'Páginas Kanban em aplicações de SeaTable'
date: 2023-12-07
lastmod: '2023-12-07'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/pt/ajuda/paginas-kanban-apps-seatable'
aliases:
    - '/pt/ajuda/kanbanseiten-in-universellen-apps'
    - '/pt/ajuda/paginas-kanban-apps-universais'
seo:
    title: 'Páginas Kanban em apps de SeaTable: Visualize fluxos e organize projetos'
    description: 'Aprenda a usar as páginas Kanban no SeaTable para visualização de tarefas, gestão de permissões, configuração de filtros e personalização de cartões.'
weight: 7
---

Este tipo de página oferece-lhe a opção de apresentar entradas como cartões de índice num **quadro Kanban**. Um caso de utilização específico poderia ser a **visualização de fluxos de trabalho e do progresso de um projeto**, por exemplo.

![Páginas Kanban em aplicações](images/Kanbanseiten-in-Universellen-Apps.png)

## Alterar as definições da página

Se pretender alterar as definições de uma página, clique no **símbolo da roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondente na barra de navegação.

![Alterar as definições da página Kanban](images/Einstellungen-der-Kanbanseite-aendern.png)

Nas **definições da página**, especificar o **quadro** em que se baseia o quadro Kanban, a coluna em que as entradas são **agrupadas** e a coluna de onde provêm os **títulos**.

![Definições de página da página Kanban em aplicações](images/Seiteneinstellungen-der-Kanbanseite-in-Universellen-Apps.png)

## Filtros predefinidos, ordenação e colunas ocultas

Também é possível definir filtros predefinidos, ordenação e colunas ocultas para limitar e organizar os dados apresentados aos utilizadores. Para filtrar ou ordenar, clique em **Adicionar filtro** ou **Adicionar ordenação**, seleccione a **coluna** e a **condição** pretendidas e confirme com **Enviar**.

![Adicionar filtro às páginas kanban nas aplicações](images/Add-filter-on-kanban-pages-in-Universal-Apps.png)

Os utilizadores podem ver mais informações sobre uma entrada clicando num separador. Por conseguinte, decida quais os dados que devem ser **visíveis** e mostre ou oculte as colunas correspondentes utilizando os **cursores**.

![Ocultar colunas nas páginas da galeria em aplicações](images/Hide-columns-on-gallery-pages-in-Universal-Apps-1.png)

{{< warning  headline="Nota importante"  text="Os utilizadores da aplicação **não podem alterar os filtros predefinidos**, **a ordenação** e **as colunas ocultas**. Por conseguinte, só verá as entradas filtradas numa ordem fixa, como desejar." />}}

## Definições da coluna de ligações

Nas **opções da coluna de ligação**, é possível especificar quais os dados visíveis e quais as operações permitidas para cada tabela ligada.

![Ligar definições de coluna em páginas de tabela nas aplicações](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Permitir adicionar novas entradas**: Se ativar este seletor, os utilizadores podem adicionar novas entradas à tabela ligada. Pode utilizar as definições de campo para definir as colunas que são **visíveis** e as que são **obrigatórias**, ou seja, que têm de ser preenchidas.
- **Permitir a ligação de entradas existentes**: Se ativar esta barra deslizante, os utilizadores podem ligar entradas existentes na tabela ligada. Pode utilizar as definições de campo para definir as colunas que são **visíveis**.
- **Limitar as ligações a um máximo de uma linha**: Se ativar esta barra deslizante, os utilizadores só podem ligar uma linha da tabela ligada nas células da coluna de ligação.
- **Filtros predefinidos**: Se adicionar um filtro aqui, apenas as opções que satisfazem as condições do filtro serão apresentadas ao ligar as entradas.
- **Ativar** a função de grandes volumes de dados: Se a função de grandes volumes de dados estiver activada, os utilizadores podem pesquisar mais de 20.000 registos de dados, desde que existam este número de entradas na tabela ligada.

## Outras definições da página

Com três outros selectores, pode definir o SeaTable **para não apresentar linhas vazias**, para apresentar os **nomes das colunas** nos cartões de índice e para **envolver o texto**.

![Outras definições de página para a página Kanban em aplicações](images/Weitere-Seiteneinstellungen-der-Kanbanseite-in-Universellen-Apps.png)

Também é possível apresentar outros **dados** da tabela subjacente nos cartões de índice: Ativar qualquer número de **campos a serem apresentados**.

## Autorizações de páginas

É possível definir as seguintes [autorizações de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) para páginas Kanban:

![Autorizações de páginas para páginas de galerias](images/Seitenberechtigungen-von-Galerieseiten.png)

Decida quem está autorizado a ver a página Kanban, adicionar, editar e eliminar linhas. Graças às opções de autorização diferenciadas deste tipo de página, pode definir isto com precisão.
