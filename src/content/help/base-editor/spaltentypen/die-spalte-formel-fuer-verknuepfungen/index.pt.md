---
title: 'A coluna Fórmula para ligações'
date: 2025-07-18
lastmod: '2025-07-18'
categories:
    - 'formeln'
author: 'kgr'
url: '/pt/ajuda/coluna-de-formula-de-ligacoes'
aliases:
    - '/pt/ajuda/die-spalte-formel-fuer-verknuepfungen'
seo:
    title: 'Coluna de fórmula de ligações no SeaTable'
    description: 'Saiba como usar a coluna de fórmula de ligações no SeaTable para combinar e resumir dados entre tabelas relacionadas.'

---

Com uma fórmula para ligações, pode **exibir, resumir ou relacionar dados de tabelas ligadas** na sua tabela atual. É aqui que SeaTable mostra as suas vantagens como [base de dados relacional]({{< relref "posts/relationale-datenbank" >}}).

Está disponível um total de **cinco fórmulas diferentes** para o tipo de coluna. O pré-requisito para utilizar a coluna é a existência de pelo menos uma coluna do tipo [Ligação a outras entradas]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) na sua tabela.

## Crie uma coluna de fórmula para ligações

Para aplicar uma fórmula, tem primeiro de adicionar uma nova coluna Fórmula para ligações à sua tabela.

![Seleção de uma fórmula para as ligações](images/add-a-link-formula.png)

1. Clique no símbolo **Mais** à direita da última coluna.
2. Atribua um **Nome** à coluna.
3. Selecione **Fórmula para ligações** como o tipo de coluna.
4. Escolha uma **Fórmula** (por exemplo, Rollup).
5. Selecione a **Coluna de ligação** da tabela a partir da qual pretende utilizar os dados.
6. Especifique a **Coluna na tabela ligada** à qual a fórmula deve fazer referência.
7. Dependendo da fórmula selecionada, pode fazer **outras opções**.
8. Crie a coluna com **Enviar**.

## 5 Fórmulas para ligações

Pode encontrar mais informações e exemplos das cinco fórmulas diferentes nos artigos seguintes, que ilustram as vantagens e a utilização das fórmulas:
- [Lookup]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}})
- [Countlinks]({{< relref "help/base-editor/formeln/die-countlinks-formel" >}})
- [Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}})
- [Findmax]({{< relref "help/base-editor/formeln/die-findmax-formel" >}})
- [Findmin]({{< relref "help/base-editor/formeln/die-findmin-formel" >}})

## Formatação dos resultados

Cada fórmula no SeaTable tem um **número**, uma **data** ou um **texto/corda** como resultado. Os resultados numa coluna de fórmula para ligações são automaticamente atribuídos a um **formato** específico. Se não estiver satisfeito com isso, pode **redetectá-lo**. Para o fazer, clique na **seta pendente** à direita do nome da coluna e depois em **Editar definições de formato**.

![Formatação dos resultados da fórmula](images/format-settings-of-the-link-formula-column.png)

Também estão disponíveis diferentes definições de **formato para números** para colunas de countlinks e rollup: Percentagem, moedas ou duração, bem como separadores decimais, separadores de milhares e precisão.