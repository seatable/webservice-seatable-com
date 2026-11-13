---
title: 'The Countlinks Formula'
date: 2023-01-11
lastmod: '2023-01-24'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/help/countlinks-formula-seatable'
aliases:
    - '/help/die-countlinks-formel'
seo:
    title: 'Countlinks formula in SeaTable: count linked records'
    description: 'Use the Countlinks formula to automatically count the records linked to a row. Perfect for attendee lists, evaluations or any kind of multiple linking.'

---

The Countlinks formula counts the number of linked records of the column type **Link to other records** in the respective row.

{{< warning  headline="Table linking is a basic requirement" >}}

You can create a column with the Countlinks formula only if you have linked two tables. Read [here how to create such a link]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

{{< /warning >}}

## Scope of the Countlinks Formula

The **Countlinks formula** should be used whenever you want to display the **number of records linked to a row**.

For example, when planning a workshop, you can display the number of registered participants from a separate table. The [link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) would thus hold the names of all participants.

![The Countlinks Formula.](images/countlinks-2.png)

Using the Countlinks formula makes sense only if the **Limit links to a maximum of one row** option is disabled in the settings of a link column. If the option were enabled, the Countlinks formula field would always show a one (= a single linked row).

## Create a Countlinks formula

![The Countlinks Formula.](images/countlink.gif)

1. Create a new column of the type **Link formula**.
2. Give the column an appropriate **name**.
3. Set the **Countlinks** option as the formula.
4. Now select the **link column** whose records you want to count in the **Select link column in this table** field.
5. Click **Submit**.
