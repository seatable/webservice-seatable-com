---
title: 'The status bar and its functions'
date: 2023-02-21
lastmod: '2023-02-21'
categories:
    - 'ansichtsoptionen'
author: 'nsc2'
url: '/help/status-bar-and-its-functions'
aliases:
    - '/help/die-status-zeile-und-ihre-funktionen'
seo:
    title: 'Status bar in SeaTable – count & calculate values easily'
    description: 'Learn how the SeaTable status bar works: count rows, calculate sums, averages, medians and numeric results directly in your view.'
weight: 30
---

The **status bar** is located at the bottom of your tables and basically fulfills two different functions, which are explained in more detail in this article:

- **Function 1**: Counting the rows in a view
- **Function 2**: Specify a value calculated from all records (e.g. sum, average, etc.) for number-based columns.

Thanks to the status bar you always have these **statistical basic values** in view as soon as you have opened a table.

## Counting the rows in a view

The status bar indicates at the lower left margin the number of all **rows** that are in the currently opened **table view**. If you [filter in a view]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}), the status bar counts only the remaining table records.

![The status row always indicates the number of rows in the currently opened table view.](images/status-cell-function-1.jpg)

In addition, you can [select rows]({{< relref "help/base-editor/zeilen/mehrere-zeilen-selektieren" >}}) – then it refers only to the selected records.

## Specification of a value calculated from all records

For **number-based columns**, the status bar for each column gives a **value** calculated from all records.

![Calculated values in the statusrows](images/the-status-cell-function-2-1.png)

## Calculation options

For number-based columns, the following **calculation options** are available in the status bar :

- Calculation of the **sum** of all records of the column
- Calculation of the **average value** from all records of the column
- Calculation of the **median** from all records of the column
- Determination of the **maximum value** from all records of the column
- Determination of the **minimum value** from all records of the column
- No calculation

![Calculation options of the statusrow](images/berechnungsoptionen-status-zeile.png)

## Compatible column types and formats

For the following column types, the statusrow reflects a calculated value:

- [Number columns]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
    - Number
    - Percent
    - Currency
- [Duration columns]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})
- [Rating columns]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})
- Numerical values in [formula columns]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

For the following column types, the status bar **does not** reflect a calculated value, although they (may) contain numbers:

- [Date columns]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- [Created time]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) and [Last modified time]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})
- [Automatic number]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- Numbers in [text columns]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})
