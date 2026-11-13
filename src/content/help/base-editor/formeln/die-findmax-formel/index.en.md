---
title: 'The Findmax formula'
date: 2023-02-13
lastmod: '2026-11-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/help/findmax-formula'
aliases:
    - '/help/die-findmax-formel'
seo:
    title: 'SeaTable Findmax Formula: Determine Maximums from Linked Records'
    description: 'Learn how to use the Findmax formula in SeaTable to get the largest value from multiple linked records – with practical examples & more.'
---

The **Findmax formula** searches among the entries of the linked column for the **maximum value** and returns it. This is useful if there are **several entries** in the linked table that refer to the same record (e.g. of a person or category) in another table.

## What you can use the Findmax formula for

You can use the Findmax formula with all alphanumeric values to determine the **maximum value**. Let's say you use SeaTable for [budget planning]({{< relref "templates/finance/budget-plan" >}}), where one table stores the expenses and another table stores the categories. You can then link each expense to a category. To find out what **the highest expense per category** was, you can use the **Findmax formula** to display the largest value from all linked expenses.

![findmax formula](images/findmax.png)

## How to use the Findmax formula

### Add a table link

See the [article about the link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) for information on how to create a column of the type **Link to other records**. This is a basic requirement to be able to use the Findmax formula.

{{< warning headline="Multiple linked rows required" >}}

Using the Findmax formula only makes sense if the **Limit links to a maximum of one row** option is disabled in the settings of a link column. If the option were enabled, the Findmax formula would always show the same value as in the single linked row.

{{< /warning >}}

### Add a column with Findmax formula

![findmax formula](images/findmax.gif)

1. Create a new column of the type **Link formula**.
2. Set the **Findmax** option as the formula.
3. Select the previously created column of the type **Link to other records** in this table.
4. Now specify the **column in the linked table to look up** whose record with the maximum value should be displayed in the Findmax column.
5. Select the **column in the linked table to be evaluated** in which you want to determine the maximum value.
6. Click **Submit**.
