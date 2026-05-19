---
title: 'The Findmin Formula'
date: 2023-02-13
lastmod: '2023-02-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/help/findmin-formula'
aliases:
    - '/help/die-findmin-formel'
seo:
    title: 'Findmin formula in SeaTable – find the smallest value'
    description: 'Use the Findmin formula to get the minimum numeric value from linked records in SeaTable. Perfect for cross‑table data analysis.'
---

The **Findmin formula** searches among the entries of a linked column for the **minimum value** and returns it. This is useful if there are **several entries** in the linked table that refer to the same record (e.g. of a person) in another table.

The Findmin formula works exclusively with **numerical values**, which is why the content of the linked column must also consist of numerical values. In addition, the use of the Findmin formula only makes sense if the **Allow link to multiple rows** slider is enabled when creating the **Link to other records** column. If the option were off, the Findmin formula would always contain the same number as in the linked column.

## What you need the Findmin formula for

The **Findmin function** should be used when you want to **cross-reference** numerical values stored in different tables. Let's say you use SeaTable to collect the **working hours of** your employees, where one table stores the employees and another table stores the daily activity. You can then link each employee record to the working hours entered.

![findmin formula](images/findmax-1.png)

To determine when an employee logged in for the first time, you can use the **Findmin formula** to display the **smallest value** - in this case the first login - from the total login times in a column.

![findmin formula](images/findmin.png)

You can use the Findmin formula with all numeric values to represent the **minimum value**.

## How to use the Findmin formula

### Add a table link

See the [article about the link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) for information on how to create a column of the type **Link to other records**. This is a basic requirement to be able to use the Findmin formula.

### Add a column with Findmin formula

![findmin formula](images/findmin.gif)

1. Create a new column of the type **Formula for links**.
2. Set the **Findmin** option as the formula.
3. Select the previously created column of the type **Link to other records** in this table.
4. Now, in the **Select lookup column** field **in the linked table "..."**, specify the column from the other table that you want to link to the column here.
5. Click **Submit**.

{{< warning  headline="Attention"  text="The Findmin formula works exclusively with **numeric values** which is why the linked column must contain numerical values." />}}
