---
title: 'Grouping, sorting, and filtering'
date: 2022-08-25
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'cdb'
url: '/help/grouping-sorting-filter'
aliases:
    - '/help/gruppierung-sortierung-und-filter'
seo:
    title: 'Group, sort & filter data in SeaTable step by step'
    description: 'Learn how to group, sort and filter tables efficiently in SeaTable. Organize your data to get exactly the information you need – with just a few clicks.'
weight: 20
---

SeaTable offers various methods for evaluating and preparing data. **Filters, sorting and grouping** are simple tools with which you can structure your data in just a few clicks and quickly obtain the desired information. Used correctly, filters, sorting and grouping offer a wide range of evaluation options.

Data records are filtered, sorted and grouped using **rules**. A rule always consists of an instruction and the column to which it is applied. In the case of sorting and grouping, the instruction is the order (ascending or descending) in which the data records are listed, regardless of the column type. A filter instruction has further components that depend on the column type.

Sounds complicated? Not at all – grouping, sorting and filtering is child's play in SeaTable!

## Grouping

The grouping function allows you to **group the rows of a table** and calculate simple descriptive statistics such as the number of rows in a group or the sum and average value of number-based columns. Grouping is done using **identical values in the column selected for grouping**. For example, organize the tasks in your team by using a grouping via the employee column to bundle the pending tasks for each team member.

If you want to display your data even more precisely, use **nested groupings**. You can select up to three grouping characteristics to create subordinate groupings. For example, you can group tasks first by the person responsible, then by priority and then by date. This opens up new possibilities for structuring data.

[Find out more about the grouping function here]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})

## Sorting

You can use the sort function to display the unordered entries in a table **in an ordered sequence**.

Create a rule to sort the data records in ascending or descending order according to the values in a column. **Multiple sorting rules** can also be used for large data records. If several sorting rules are used, the rows are first sorted according to the first rule. Rows with identical values according to the first sorting rule are then sorted according to the second rule.

[Learn more about the sorting function here]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})

## Filtering

With SeaTable's filter function, you can use filter rules to **filter out certain data records from a table** and only display the rows that fulfill a desired criterion or criteria. This allows you to reduce the rows in the view to the minimum you need and always maintain an overview.

Unlike grouping and sorting rules, the instruction for filter rules usually consists of two components:
- **Filter criterion**: Relationship between filtered column and filter value (e.g. "is", "contains", "is empty")
- **Filter value**: The value to filter by (e.g. "123", "done")

Filter rules can also be linked with the two Boolean operators AND and OR. With an **AND** link, only the entries that fulfill all defined conditions are displayed. The **OR link** can be used to filter the view so that all rows that fulfill at least one of the defined conditions are displayed. The AND and OR operators can also be used together using **filter groups**.

[Learn more about the filter function here]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})

## Locking filter, sorting and grouping settings

The settings you have made using filters, grouping and sorting are saved in the current view. If you want to save them for future use, you can lock the [view]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}}) so that no one changes the view.

{{< warning headline="Important note" text="With filters, groupings and sorting, you only change how the data is displayed in your view! The data basis remains unchanged. So if data records have disappeared, check whether you are in the correct view or whether you have hidden data records with a filter." />}}

## Differences depending on view type

Not all [view types]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) allow grouping, sorting and filtering in the same way. Get an overview with the help of this table:

| View type | Filter | Sort | Group |
| ------------------ | ------------------------------ | ------------------------------ | -------------------------- |
| **Table** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Kanban** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Calendar** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Gallery** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Timeline** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Tree** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Big Data** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |