---
title: 'The multiple select column'
date: 2023-03-28
lastmod: '2025-07-15'
categories:
    - 'spalten'
author: 'kgr'
url: '/help/multiple-select-column'
aliases:
    - '/help/die-mehrfachauswahl-spalte'
seo:
    title: 'Multiple Select Column in SeaTable: Options & Colors'
    description: 'Use the multiple select column in SeaTable: colorful labels, flexible sorting, export/import, custom colors, and key differences to single select.'

---

A multiple select column is ideal if you want to assign your rows in a column **several options** from a list of options to be defined. The options are given colorful labels that you can use to label your records and make tables clear, for example, by [filtering]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) for specific options.

![Example table with one multiple select column](images/example-table-multiple-select.png)

## Create a multiple select column

Creating a multiple select column is easy as pie and done with just a few clicks. For detailed information, see [Add a column]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

1. Click the **\[+\] icon** to the right of the last column of any table.
2. Give the new column a **name**.
3. Select **Multiple select** as the column type.
4. Confirm with **Submit**.

## Similarities with the single select column

### Add multiple select options

Adding options to a multi-select column works **in exactly the same way as with a single-select column**. You can add new options in several ways. Find out all about this in the help article on [the single select column]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}).

### Exporting and importing multiple select options

You can **export** and **import** the options of a multi-select column in the same way as a single-select column. You can find more information on this in the article on the single select column.

### Colors of the options

As with the single select column, **24 colors** are currently available to visually highlight the selection options.


![Colors of the single select column](images/farben-einfachauswahl.png)

With an [Enterprise subscription]({{< relref "help/teamverwaltung/abonnement/abo-pakete" >}}), you also have the ability to create [custom colors]({{< relref "help/base-editor/weitere-optionen/eigene-farben-in-einer-base-hinzufuegen" >}}) for your multiple select options.

### Change the order of multiple select options

The order of the options can be adjusted in the same way as for a single select column. It is of crucial importance if you want to [sort]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) or [group]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) by the multi-select column. This is because SeaTable does **not arrange the options alphabetically**, but flexibly according to the **order of the options**, which you define using drag-and-drop.

### Set default value

In contrast to the single select column, you **cannot** set a default value for a multiple select column.

## Multiple select or link to other records?

If you want to be able to save **additional information** for each selection option, you should consider using a [link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) instead of a multiple select column. To do this, create complete data records for all options in a separate table, which you can link to any number of rows in other tables.
