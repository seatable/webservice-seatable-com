---
title: 'The specifics of the first column'
date: 2022-10-13
lastmod: '2024-03-15'
categories:
    - 'arbeiten-mit-spalten'
author: 'nsc2'
url: '/help/first-column-features'
aliases:
  - '/help/die-besonderheiten-der-ersten-spalte'
seo:
    title: 'First Column in SeaTable – Features and Specifics Explained'
    description: 'Learn all the unique attributes of the first column in SeaTable, including supported types, restrictions, and step-by-step adjustability.'
---

The **first column** of a table in SeaTable has several special features and restrictions compared to the other columns. Here you can find out how to customize the first column in SeaTable.

## The peculiarities of the first column in SeaTable

- Unlike the other columns, you **cannot hide** the first column of a table.
- Unlike the other columns, you **cannot move** the first column of a table.
- Unlike the other columns, you **cannot delete** the first column of a table.
- In contrast to the other columns, however, you can **freeze** the first column individually.
- There are only **six column types** to choose from for the **first column**:
  - [Text]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})
  - [Number]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
  - [Date]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
  - [Single select]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
  - [Auto number]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
  - [Formula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

## How to customize the type of the first column

![Customize the first column](images/change-the-first-column.gif)

1. Click on the triangular **drop-down icon** to the right of the name of the first column.
2. Go to **Customize column type**.
3. Click in the **field of** the current column type.
4. Select a **new column type** for the first column.
5. Make **format settings** if necessary.
6. Click **Submit**.
7. Confirm the adjustment by clicking **Convert**.

## Formulas in the first column

If you define a **formula** as the **first column** of a table, you can use the simple formula **{column name}**, for example, to **quote** the entries from almost all other columns in your table. This even works if the other column type is **not** supported in the first column.

![Possibilities with the Formula column type in the first column of a table](images/formular-in-the-first-column-1.png)

## Frequently asked questions

{{< faq "What are the limitations of the first column?" >}}The first column cannot be **hidden**, **moved** or **deleted**.
{{< /faq >}}
{{< faq "Is it possible to change the type of the first column afterwards?" >}}Yes, this is possible. However, in some cases information may be **lost** when [changing the column type]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}}), for example from text to number. Therefore, after a conversion, check whether all information has been transferred correctly and completely.
{{< /faq >}}
{{< faq "What is an automatic number?" >}}If you want your rows to have a **unique identification number**, the [Auto number]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}}) column type could serve you well. Examples include invoice numbers, test cases or employee IDs. The number can also be supplemented with any prefix.

{{< /faq >}}
