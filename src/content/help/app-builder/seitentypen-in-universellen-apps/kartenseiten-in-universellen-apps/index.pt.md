---
title: 'Páginas de mapas em aplicações'
date: 2026-04-07
lastmod: '2026-04-07'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/pt/ajuda/paginas-de-mapas-em-aplicacoes'
seo:
    title: 'Páginas de mapas em aplicações: visualize localizações num mapa'
    description: 'Crie páginas de mapas nas SeaTable Apps: visualize dados de geolocalização e endereços de forma flexível num mapa mundial.'
weight: 9
---

Pode utilizar este tipo de página para apresentar **localizações** que tenha guardado na sua tabela utilizando **dados de geoposição ou endereços** num **mapa do mundo** dentro da aplicação.

![Mostrar localizações num mapa](images/map-page-app-builder.png)

## Definições da página

Se pretender alterar as definições de uma página, clique no ícone de roda dentada correspondente {{< seatable-icon icon="dtable-icon-set-up" >}} na barra de navegação.

![Alterar as definições da página do mapa](images/access-page-settings.png)

Nas **configurações da página** pode selecionar o **tipo de mapa** (padrão ou imagens), a **tabela** e uma coluna para o **endereço** e a **cor do pino**. Tenha em atenção que apenas determinados tipos de colunas podem ser utilizados para estas informações.

![definições da página do mapa em aplicações](images/map-page-settings.png)

Se especificar uma **coluna a ser apresentada**, as localizações serão permanentemente identificadas no mapa.

![Coluna a apresentar na página do mapa em aplicações](images/map-page-display-field.png)

No entanto, também pode definir colunas a serem apresentadas de forma flexível, que só se tornam visíveis através de um **efeito de ponte**. Active os cursores para as colunas que devem ser visíveis quando passa o rato sobre um pin.

![efeito de pairar das colunas a serem apresentadas na página do mapa](images/map-page-hover-display.gif)

## Filtros predefinidos e colunas ocultas

Também pode definir filtros predefinidos e colunas ocultas para limitar os dados apresentados. Para filtrar, clique em **Adicionar filtro**, selecione a **Coluna** e a **Condição** pretendidas e confirme com **Enviar**.

![Filtro nas páginas do mapa](images/map-page-filters.png)

Oculte as colunas que não devem estar disponíveis para a página do mapa utilizando o **deslizador**.

![Ocultar colunas nas páginas do mapa](images/hide-columns-on-map-pages.png)

{{< warning type="warning" headline="Nota importante" text="Os filtros predefinidos e as colunas ocultas **não podem ser alterados pelos utilizadores da aplicação**. Por conseguinte, só verá as entradas filtradas como desejar." />}}

## Autorizações de página

Para as páginas de mapa, só pode definir uma [permissão de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) – nomeadamente quem tem permissão para ver a página de mapa. Isto deve-se ao facto de você **não poder adicionar, editar ou apagar linhas** nas páginas de mapas.
