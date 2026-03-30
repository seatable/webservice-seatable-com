---
title: 'Passo 6: Criar vistas'
date: 2024-08-30
lastmod: '2024-09-19'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/pt/ajuda/etapa-6-visoes'
aliases:
    - '/pt/ajuda/schritt-6-ansichten'
seo:
    title: 'Etapa 6: Crie e filtre visualizações e organize seus dados SeaTable'
    description: 'Saiba como criar, filtrar, ordenar e agrupar visualizações em SeaTable para acessar as informações certas e manter seus dados organizados.'
---

Criou um sistema de gestão de despesas sólido que já calcula automaticamente o total de despesas por categoria. Agora vai ficar a conhecer outra função do SeaTable: **as visualizações**.

As vistas permitem-lhe utilizar filtros, ordenação, agrupamento e ocultação de informações para determinar os dados que são apresentados numa tabela. As vistas aplicam-se sempre por tabela e pode criar tantas vistas quantas quiser. Isto significa que o utilizador recebe sempre as informações que lhe interessam.

Por exemplo, pode criar uma vista que mostre apenas as despesas superiores a 100 euros e as ordene por data. Isto permite-lhe acompanhar as despesas maiores.

{{< warning  headline="As alterações aos dados afectam todas as visualizações"  text="É importante perceber que uma vista é apenas uma representação diferente dos mesmos dados. As alterações aos registos de dados de uma vista afectam todas as vistas da mesma tabela, uma vez que todas acedem ao mesmo registo de dados." />}}

## Criar uma vista adicional com um agrupamento

Mudar para a tabela `Expenses` e criar uma nova vista. Escolha um nome que indique claramente o objetivo da vista, como por exemplo `Group by date and category`.

Cada vista recém-criada não contém inicialmente quaisquer agrupamentos, ordenação ou filtros. Agora queremos mudar isso:

1. Agrupar os dados na coluna `Date` por ano.
2. Em seguida, agrupe os dados de acordo com `Category-Link`.

![Vista «Group by date and category» agrupada por ano e por ligação de categoria](images/lvl1-view-groups.png)

## Criar uma vista com filtro e agrupamento

Agora que já domina o agrupamento de dados, é altura de filtrar os dados utilizando uma vista.

Criar uma nova vista com o nome `Clothing Expenses by Year`para mostrar as despesas anuais com vestuário:

1. Adicionar um filtro: `Category-Link` contém `Clothing`para apresentar apenas as entradas desta categoria.
2. Agrupar os dados filtrados por ano.

Agora, com apenas alguns cliques, criou uma vista que apresenta claramente as suas despesas de vestuário, agrupadas por ano.

## Experimentar outras vistas

Isto conclui este curso online, que é também o início da sua viagem com o SeaTable. Reserve alguns minutos para experimentar outras vistas - compreendê-las é um dos aspectos mais importantes da utilização do SeaTable.

Encorajo-o a conhecer melhor o SeaTable. Já criou uma ferramenta poderosa, mas há muito mais para descobrir!

Quando já tiveres experimentado o suficiente, tenta completar o questionário e ganha o teu prémio no nosso fórum da comunidade.

## Artigo de ajuda com mais informações

- [O que é um ponto de vista?]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}})
- [Agrupamento, classificação e filtragem]({{< relref "help/base-editor/ansichten/gruppierung-sortierung-und-filter" >}})
- [Criar uma nova visão]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}})
- [Visualizações de pinos]({{< relref "help/base-editor/ansichten/ansichten-pinnen" >}})
- [A barra de estado e as suas funções]({{< relref "help/base-editor/ansichten/die-status-zeile-und-ihre-funktionen" >}})
