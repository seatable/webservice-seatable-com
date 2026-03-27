---
title: 'The link formula column'
date: 2025-07-18
lastmod: '2025-07-18'
categories:
    - 'formeln'
author: 'kgr'
url: '/help/linked-formula-column'
aliases:
    - '/help/die-spalte-formel-fuer-verknuepfungen'
seo:
    title: 'Using the Linked Formula Column in SeaTable'
    description: 'Discover how to use the linked formula column in SeaTable to connect and summarize data across related tables efficiently.'

---

With a link formula, you can **display, summarize or relate data from linked tables** in your current table. This is where SeaTable shows its advantages as a [relational database]({{< relref "posts/relationale-datenbank" >}}).

A total of **five different formulas** are available for the column type. The prerequisite for using the column is the existence of at least one column of the type [Link to other records]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) in your table.

## Create a link formula column

To apply a formula, you must first add a new link formula column to your table.

![Selection of a Link formula](images/add-a-link-formula.png)

1. Click on the **Plus symbol** to the right of the last column.
2. Give the column a **Name**.
3. Select **Link formula** as the column type.
4. Decide on a **Formula** (e.g. Rollup).
5. Select the **Link column** of the table from which you want to use data.
6. Specify the **column in the linked table** to which the formula should refer.
7. Depending on the formula selected, you can make **further settings**.
8. Create the column with **Submit**.

## 5 link formulas

Further information and examples of the five different formulas can be found in the following articles, which illustrate the benefits and use of the formulas:
- [Lookup]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}})
- [Countlinks]({{< relref "help/base-editor/formeln/die-countlinks-formel" >}})
- [Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}})
- [Findmax]({{< relref "help/base-editor/formeln/die-findmax-formel" >}})
- [Findmin]({{< relref "help/base-editor/formeln/die-findmin-formel" >}})

## Formatting the results

Each formula in SeaTable has a **number**, a **date** or a **text/string** as a result. The results in a link formula column are automatically assigned a specific **format**. If you are not satisfied with this, you can **re-detect** it. To do this, click on the **drop-down arrow** to the right of the column name and then on **Edit format settings**.

![Formatting the formula results](images/format-settings-of-the-link-formula-column.png)

For countlinks and rollup columns, different **format settings for numbers** are available: percent, currencies or duration as well as decimal separators, thousands separators and precision.