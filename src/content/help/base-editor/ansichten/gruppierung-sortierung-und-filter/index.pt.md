---
title: 'Agrupamento, ordenação e filtragem'
date: 2022-08-25
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'cdb'
url: '/pt/ajuda/agrupar-ordenar-filtrar'
aliases:
    - '/pt/ajuda/gruppierung-sortierung-und-filter'
seo:
    title: 'Agrupar, ordenar e filtrar dados no SeaTable passo a passo'
    description: 'Saiba como agrupar, ordenar e filtrar dados no SeaTable. Organize suas tabelas e encontre as informações que precisa com poucos cliques.'
weight: 20
---

SeaTable oferece-lhe vários métodos de análise e preparação de dados. **Os filtros, a ordenação e o agrupamento** são ferramentas simples com as quais pode estruturar os seus dados com apenas alguns cliques e obter rapidamente a informação desejada. Utilizados corretamente, os filtros, a ordenação e o agrupamento oferecem-lhe uma vasta gama de opções de análise.

Os registos de dados são filtrados, ordenados e agrupados através de **regras**. Uma regra é sempre constituída por uma instrução e pela coluna à qual é aplicada. No caso da ordenação e do agrupamento, a instrução é a ordem (ascendente ou descendente) pela qual os registos de dados são listados, independentemente do tipo de coluna. Uma instrução de filtro tem outros componentes que dependem do tipo de coluna.

Parece-lhe complicado? De modo algum – agrupar, ordenar e filtrar é uma brincadeira de crianças no SeaTable!

## Agrupamento

A função de agrupamento permite-lhe **agregar as linhas de uma tabela em grupos** e calcular estatísticas descritivas simples, tais como o número de linhas num grupo ou a soma e o valor médio de colunas baseadas em números. O agrupamento é feito utilizando **valores idênticos na coluna selecionada para agrupamento**. Por exemplo, organize as tarefas da sua equipa agrupando as tarefas pendentes de cada membro da equipa utilizando a coluna do empregado.

Se pretender apresentar os seus dados de forma ainda mais precisa, utilize **agrupamentos aninhados**. Pode selecionar até três caraterísticas de agrupamento para criar agrupamentos subordinados. Por exemplo, pode agrupar tarefas primeiro pela pessoa responsável, depois por prioridade e depois por data. Isto abre-lhe novas possibilidades de estruturação de dados.

[Saiba mais sobre a função de agrupamento aqui]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})

## Ordenação

Pode utilizar a função de ordenação para apresentar as entradas não ordenadas de uma tabela **numa sequência ordenada**.

Crie uma regra para ordenar os registos de dados por ordem ascendente ou descendente de acordo com os valores de uma coluna. Também podem ser utilizadas **várias regras de ordenação** para registos de dados grandes. Se forem utilizadas várias regras de ordenação, as linhas são ordenadas primeiro de acordo com a primeira regra. As linhas com valores idênticos de acordo com a primeira regra de ordenação são depois ordenadas de acordo com a segunda regra.

[Saiba mais sobre a função de ordenação aqui]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})

## Filtrar

Com a função de filtro do SeaTable, pode utilizar regras de filtro para **filtrar** determinados registos de dados de uma tabela e apresentar apenas as linhas que satisfazem um critério ou critérios desejados. Isto permite-lhe reduzir as linhas da vista ao mínimo necessário e manter sempre uma visão geral.

Ao contrário das regras de agrupamento e ordenação, a instrução para as regras de filtragem é normalmente constituída por dois componentes:
- **Critério de filtragem**: Relação entre a coluna filtrada e o valor do filtro (por exemplo, "é", "contém", "está vazio")
- **Valor do filtro**: O valor a ser filtrado (por exemplo, "123", "feito")

As regras de filtragem também podem ser ligadas com os dois operadores booleanos AND e OR. Com uma ligação **AND**, apenas são apresentadas as entradas que satisfazem todas as condições definidas. A ligação **OU** pode ser utilizada para filtrar a vista de modo a que sejam apresentadas todas as linhas que satisfaçam pelo menos uma das condições definidas. Os operadores AND e OR também podem ser utilizados em conjunto através de **grupos de filtros**.

[Saiba mais sobre a função de filtro aqui]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})

## Bloquear definições de filtro, ordenação e agrupamento

As definições que efectuou utilizando filtros, agrupamento e ordenação são sempre guardadas na vista atual. Se as quiser guardar para utilização futura, pode [bloquear a vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}}) para que ninguém possa alterar a vista.

{{< warning headline="Nota importante" text="Com filtros, agrupamentos e ordenação, apenas altera a forma como os dados são apresentados na sua vista! A base de dados permanece inalterada. Assim, se os registos de dados tiverem desaparecido, verifique se está na vista correta ou se ocultou registos de dados com um filtro." />}}

## Diferenças consoante o tipo de vista

Nem todos os [tipos de vista]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) permitem agrupamento, ordenação e filtragem da mesma forma. Obtenha uma visão geral com a ajuda desta tabela:

| Tipo de vista | Filtrar | Ordenar | Agrupar |
| ------------------ | ------------------------------ | ------------------------------ | -------------------------- |
| **Tabela** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Kanban** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Calendário** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Galeria** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Linha de tempo** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Árvore** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Big Data** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |