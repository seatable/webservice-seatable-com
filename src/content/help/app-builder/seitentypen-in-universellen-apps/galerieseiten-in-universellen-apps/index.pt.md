---
title: 'Páginas de galeria em aplicações de SeaTable'
date: 2023-12-04
lastmod: '2024-08-02'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/pt/ajuda/paginas-galeria-apps-seatable'
aliases:
    - '/pt/ajuda/galerieseiten-in-universellen-apps'
    - '/pt/ajuda/paginas-galeria-apps-universais'
seo:
    title: 'Páginas de galeria em SeaTable Apps: guia'
    description: 'Exiba imagens e dados em galeria nas SeaTable Apps: defina filtros, permissões e integrações de tabelas com flexibilidade.'
weight: 4
---

Pode utilizar este tipo de página para apresentar **imagens** e outros dados que tenha guardado na sua folha de cálculo sob a forma de uma **galeria** numa aplicação. Pode utilizar uma página de galeria para **perfis** claros **dos seus empregados**, por exemplo.

![Representação dos seus empregados numa página de galeria](images/page-type-gallery-example.png)

## Definições da página

Se pretender alterar as definições de uma página, clique no **símbolo da roda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondente na barra de navegação.

![Alterar as definições da página da galeria](images/Einstellungen-der-Galerieseite-aendern.png)

Nas **definições da página**, pode selecionar a **tabela**, a **coluna da imagem** e a **coluna do título** a partir das quais a galeria é alimentada.

![Definições de página da página da galeria em aplicações](images/Seiteneinstellungen-der-Galerieseite-in-Universellen-Apps.png)

## Filtros predefinidos, ordenação e colunas ocultas

Também é possível definir filtros predefinidos, ordenação e colunas ocultas para limitar e organizar os dados apresentados aos utilizadores. Para filtrar ou ordenar, clique em **Adicionar filtro** ou **Adicionar ordenação**, seleccione a **coluna** e a **condição** pretendidas e confirme com **Enviar**.

![Adicionar filtro nas páginas da galeria em aplicações](images/Add-filter-on-gallery-pages-in-Universal-Apps.png)

Os utilizadores podem ver mais informações sobre um cartão de índice na galeria, clicando numa entrada.

![Abrir entrada na página da galeria](images/Eintrag-auf-der-Galerieseite-oeffnen.gif)

Por conseguinte, decida quais os dados que devem ser **visíveis** e mostre ou oculte as colunas correspondentes utilizando os **cursores**.

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

## Autorizações de páginas

Pode definir as seguintes [autorizações de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) para as páginas da galeria:

![Autorizações de páginas para páginas de galerias](images/Seitenberechtigungen-von-Galerieseiten.png)

Decida quem está autorizado a ver, adicionar, editar e eliminar a página da galeria. Graças às opções de autorização diferenciadas deste tipo de página, pode definir isto com precisão.
