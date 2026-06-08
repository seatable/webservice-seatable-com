---
title: 'Data processing operations in SeaTable'
date: 2023-03-20
lastmod: '2023-04-28'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/help/data-processing-operations-seatable'
aliases:
    - '/help/datenverarbeitungsoperationen-in-seatable'
seo:
    title: 'Data processing in SeaTable: cross-row operations'
    description: 'Perform mathematical and relational operations in SeaTable, analyze data and link values across tables for advanced workflows.'
star: true
weight: 1
---

The data processing function is a useful feature of SeaTable that allows you to perform **operations** on a column across multiple rows . By defining an operation, you can either perform various **mathematical calculations** or establish **relationships between values** in different tables. Data processing operations have a particularly great effect in large data sets where you can handle a high number of computational processes.

## Sense behind data processing operations

SeaTable often thinks in rows. For example, a [formula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) can exclusively relate the values in a row and also [links between tables]({{< relref "help/base-editor/tabellen/tabellen-miteinander-verlinken" >}}) are only ever done from rows to rows.

Data processing, in contrast, is a function to perform operations in a column across multiple rows . Basically, a distinction is made between two different types of data processing operations:

- **Mathematical calculations** across all values in a column. Example: Access numbers to a web page.
- Relate **values** if they are identical in two tables. Example: assign payments received to an invoice.

## Mathematical and relationship operations

The following **mathematical operations** can currently be performed using the data processing function:

- [Calculate cumulative values]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}})
- [Calculate ranking]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Calculate changes]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calculate percentage]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})

The following **relationship operations** can currently be performed using the data processing function:

- [Compare and link]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}})
- [Compare and copy]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})
- [Transfer user name]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})

## Requirements for the definition of operations

The two types of data processing operations each have different **requirements** that must be met in order to create a corresponding operation.

- **Mathematical operations** require the presence of **two columns of numbers** in your table.
- For the **relation operations**, you need very specific column types depending on the use case, e.g. an [employee column]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) and a [text column]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}) when transferring user names.

## Execution notes

Data processing operations can currently be performed [manually]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-ausfuehren" >}}) or [via automation]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) in the future.

Each time the data processing operation is executed, the **results** are written to the **results column** regardless. If you do not want to overwrite any data, you should [create]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}) for the results in advance.

Unlike **formula** columns that permanently monitor the columns involved, **result columns** do _not_ update themselves. Changes to the values in the source column do _not_ affect the values in the result column without [automation]({{< relref "help/base-editor/automationen/beispiel-datenverarbeitungsoperation-per-automation-ausfuehren" >}}) or re-execution. Therefore, you can also manually overwrite the calculated or related values.

## Protection against changes

To prevent misunderstandings, we recommend **not to** make **manual changes to** the columns involved and to [lock]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}) after execution for safety (requires Plus or Enterprise subscription).

![Result columns of data processing actions locked for processing ](images/locked-score-columns.jpg)

Be aware that the calculated or related values are a **snapshot at** the time of execution. If you do not execute the operation again, the results may be outdated if the values in the source column have changed in the meantime.
