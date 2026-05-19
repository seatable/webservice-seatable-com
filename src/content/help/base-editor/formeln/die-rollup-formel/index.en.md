---
title: 'The Rollup Formula'
date: 2023-01-24
lastmod: '2023-01-24'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/help/rollup-formula'
aliases:
    - '/help/die-rollup-formel'
seo:
    title: 'Rollup Formula in SeaTable: Stats & Aggregation Guide'
    description: 'Learn to use SeaTable rollup formulas: sum, average, min, max or join values from linked records, plus formatting and setup for number relations.'
---

With the help of the rollup formula of the column type **Formula for links** you can set several numerical values of a linked column in relation to each other and perform simple statistical calculations.

## Scope of the rollup formula

With the **rollup formula** it is possible to determine relations between numerical values. For example, in budgeting, you can **sum up** the expenses of a category, calculate the **maximum** or **minimum value** spent, or even the **average**.

First of all, you need a column of the type [Link to other records]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Make sure that the option **Allow links to several rows** is activated, because only then you can determine relations between numbers.

![The roll-up formula](images/rollup-1.png)

The **Formula for Link** column then uses the rollup formula to show you the selected relation of the numerical values within the link column. In this example, we have chosen the **Sum** evaluation method:

![The roll-up formula](images/rollup-2-1.png)

## Add a table link

Read in the [article about the link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) how to create a column of the type **Link to other records**. This is a basic requirement to be able to use the rollup formula.

Using the rollup formula only makes sense if you enable the **Allow link to multiple rows** option when creating a link column. If the option were disabled, the field of the rollup formula would always contain the same value of the link column.

## Create a column with the rollup formula

![The Rollup Formula.](images/rollup-Formel.gif)

1. Create a new column of the type **Formula for links**.
2. Set the **Rollup** option as the formula.
3. Select the **link column** that links to the desired table.
4. Now decide which column from the desired **table** you want to link and evaluate in the **Select column to be merged** field in the **linked** table.
5. Set the **evaluation method**. You have average, minimum, maximum, sum and concatenation to choose from.
6. Click **Submit**.

## Format settings

You can precisely define the **format** in which the numerical values are displayed. To do this, click on the triangular **drop-down icon of** the "Formula for links" column and select the **Format settings** option. Besides numbers, you can also take **currencies**, **percentages** and **durations** as the format.
