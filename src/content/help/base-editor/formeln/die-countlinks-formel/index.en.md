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
    description: 'Use the Countlinks formula to count linked entries in any column. Perfect for project tracking, attendance, or cross-referencing records.'

---

The Countlinks formula counts the number of linked entries of the column type **Link to other entries** in the respective row.

{{< warning  headline="Table linking is a basic requirement" >}}

You can create a column with the Countlinks formula only if you have linked two tables. Read [here how to create such a link]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

{{< /warning >}}

## Scope of the Countlinks Formula

The **Countlinks formula** should be used whenever you want to display the **number of entries of** another table as a cross-reference.

For example, you can use this to map the number of registered participants from a separate table when planning a workshop. The [link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) would thus hold the names of all participants.

![The Countlinks Formula.](images/countlinks-2.png)

Using the Countlinks formula makes sense only if you enable the **Allow link to multiple rows** option when creating a column of the **Link to other entries** type. If the option were turned off, there would always be a one in the Countlinks formula field.

## Create a Countlinks formula

![The Countlinks Formula.](images/countlink.gif)

1. Create a new column of the type **Formula for links**.
2. Give the column an appropriate **name**.
3. Set the **Countlinks** option as the formula.
4. Now select the **link column** whose entries you want to count in the **Select** link column in **this table** field.
5. Click **Submit**.
