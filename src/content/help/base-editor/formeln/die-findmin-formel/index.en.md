---
title: 'The Findmin Formula'
date: 2023-02-13
lastmod: '2026-11-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/help/findmin-formula'
aliases:
    - '/help/die-findmin-formel'
seo:
    title: 'Findmin formula in SeaTable – find the smallest linked value'
    description: 'Use the Findmin formula to get the minimum numeric value from linked records in SeaTable. Perfect for cross‑table data analysis.'
---

The **Findmin formula** searches among the entries of the linked column for the **minimum value** and returns it. This is useful if there are **several entries** in the linked table that refer to the same record (e.g. of a person or category) in another table.

## What you can use the Findmin formula for

You can use the Findmin formula with all alphanumeric values to determine the **minimum value**. Let's say you use SeaTable for [budget planning]({{< relref "templates/finance/budget-plan" >}}), where one table stores the expenses and another table stores the categories. You can then link each expense to a category. To find out what **the lowest expense per category** was, you can use the **Findmin formula** to display the smallest value from all linked expenses.

![findmin formula](images/findmin.png)

## How to use the Findmin formula

### Add a table link

See the [article about the link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) for information on how to create a column of the type **Link to other records**. This is a basic requirement to be able to use the Findmin formula.

{{< warning headline="Multiple linked rows required" >}}

Using the Findmin formula only makes sense if the **Limit links to a maximum of one row** option is disabled in the settings of a link column. If the option were enabled, the Findmin formula would always show the same value as in the single linked row.

{{< /warning >}}

### Add a column with Findmin formula

![findmin formula](images/findmin.gif)

1. Create a new column of the type **Link formula**.
2. Set the **Findmin** option as the formula.
3. Select the previously created column of the type **Link to other records** in this table.
4. Now specify the **column in the linked table to look up** whose record with the minimum value should be displayed in the Findmin column.
5. Select the **column in the linked table to be evaluated** in which you want to determine the minimum value.
6. Click **Submit**.
