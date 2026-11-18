---
title: 'The Rollup Formula'
date: 2023-01-24
lastmod: '2026-11-12'
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

With the help of the rollup formula of the column type **Link formula** you can set several numerical values of a linked column in relation to each other and perform simple statistical calculations.

## Scope of the rollup formula

With the **rollup formula** it is possible to determine relations between numerical values. For example, in [budget planning]({{< relref "templates/finance/budget-plan" >}}), you can **sum up** the expenses of a category, calculate the **maximum** or **minimum value** spent, or even the **average**.

First of all, you need a column of the type [Link to other records]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Make sure that the option **Limit links to a maximum of one row** is disabled, because only then can you link multiple rows.

The [Link formula]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}}) column then uses the rollup formula to show you the selected relation of the numerical values within the link column. In this example, we have chosen the **Sum** evaluation method:

![The rollup formula](images/rollup-formel.png)

## Create a column with the rollup formula

Read in the [article about the link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) how to create a column of the type **Link to other records**. This is a basic requirement to be able to use the rollup formula.

{{< warning headline="Multiple linked rows required" >}}

Using the rollup formula only makes sense if the **Limit links to a maximum of one row** option is disabled in the settings of a link column. If the option were enabled, the rollup formula would always show the same value as in the single linked row.

{{< /warning >}}

![The rollup formula](images/rollup-formel.gif)

1. Create a new column of the type **Link formula**.
2. Set the **Rollup** option as the formula.
3. Select the **link column** that links to the desired table.
4. Now decide which column from the desired table you want to link and evaluate in the **Select column in the linked table to be summarized** field.
5. Set the **evaluation method**. You have average, minimum, maximum, sum and concatenation to choose from.
6. Click **Submit**.

## Format settings

You can precisely define the **format** in which the numerical values are displayed. To do this, click on the triangular **drop-down icon** of the rollup column and select the **Format settings** option. Besides numbers, you can also choose **currencies**, **percentages** and **durations** as the format. You can also specify **decimal and thousands separators** as well as the number of **decimal places**.

## Making changes later

Of course, you can adjust the rollup formula later, for example by changing the evaluation method from sum to average. Click on the triangular **drop-down icon** to the right of the column name and then on **Customize column type**. This takes you to the same settings as when you created the column.
