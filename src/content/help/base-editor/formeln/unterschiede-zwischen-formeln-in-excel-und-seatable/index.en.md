---
title: 'Differences between formulas in Excel and SeaTable'
date: 2023-02-03
lastmod: '2023-02-03'
categories:
    - 'formeln'
author: 'ssc'
url: '/help/excel-vs-seatable-formulas-differences'
aliases:
    - '/help/unterschiede-zwischen-formeln-in-excel-und-seatable'
seo:
    title: 'Excel vs. SeaTable formulas – what’s different?'
    description: 'Learn the key differences between Excel and SeaTable formulas: column vs. cell references, tabular logic, and practical tips for experts.'
---

Are you an Excel user who is familiar with writing formulas and just getting started with SeaTable? If so, this article is for you! Although the principles of the formula functions in SeaTable are similar, there are some important differences that you need to learn at the beginning that will pay off if you want to become an expert in SeaTable formulas.

## Central difference

The most important difference in the formula function of SeaTable and Excel is the **scope of the formulas**.

While in **Excel** you can enter a formula in any cell and it can subsequently refer to any other cell in the spreadsheet, formulas in **SeaTable** refer to **entire columns** and not to specific cells.

Since SeaTable acts as a [relational database]({{< relref "posts/relationale-datenbank" >}}) in this context, formulas are applied to the entire column of a table so that the same formula applies to each entry in that column.

## Line referencing

### Excel

Any particular cell can be referenced in another cell. For example, to determine the source of each purchase in a table, you would write a formula that references each  
cell - like A3 - to check the type of source.

The formula used below is:  
**\= IF(A3 = "Online", "Web", "Store")**

![Cell referencing in Excel](images/table-excel-vs.-seatable-1.png)

The formula refers to specific _cells_, such as A3.

### SeaTable

A formula is always applied to an entire _column_ and **not** to specific cells. For example, to identify the source of each purchase, you would write a formula that references the {Purchase Type} column, and the formula will check that column for each entry in the table.

The formula used for this below is:

**IF({Purchase Type}= "Online", "Web", "Store")**

![Column referencing in SeaTable](images/table-excel-vs-seatable-2.png)

The formula refers to whole _columns_, such as {Purchase Type}.

## Values from other tables

SeaTable formulas work within _tables_, not across _bases_.  
Similar to above, by default SeaTable formulas only refer to _columns_ within the same _table_. However, there are also ways to take a value from another table to reference it in a formula field. This approach uses linked records, which are discussed in more detail [here]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}).

### Excel

To refer to a record in another table, you must write specific references to the other table in a format such as the following:

**\=IF(Tasks!B1='Home improvements',Tasks!A1,0).**

Then you need to apply this formula to each cell where you want to run the formula (changing the cell references for each cell where you want to run the formula).

![Reference to other data set in Excel](images/table-excel-vs-seatable-3.png)

### SeaTable

To reference a record in another table, you can first link it using the **"Link to other records"** column type. Once a record in one table, such as Projects, is linked to a record in another table, such as Tasks, you can reference any row in both tables by using a **lookup**, **rollup**, or **count column**.

In the following example, a **rollup column** is used to easily reference the cost of each task associated with a project and sum the expenses to determine the total project cost.

![Rollup column to reference the cost of each task associated with a project and total the expenses to determine the total project cost.](images/reference-to-other-bases.gif)

The function thereby creates a number of possibilities to write both simple and complex formulas to reference data between tables.
