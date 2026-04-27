---
title: 'Sorting records in a view'
date: 2022-10-26
lastmod: '2025-12-05'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/help/sort-entries-view-seatable'
aliases:
    - '/help/sortieren-von-eintraegen-in-einer-ansicht'
seo:
    title: 'Sort records in a SeaTable view: multi-level sorting'
    description: 'Sort records in SeaTable by column and order, apply several sorts at once and keep data tidy for best overview — works in all views.'
weight: 24
---

The sort function allows you to display the unordered records in a table in an **ordered sequence**.

## Sort records in a view

![Entry sorting](images/Sortierung-von-Eintraegen-2.gif)

1. Create a [new view]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}}) or select the view you want to sort.
2. Click the **Sort** option in the view options above the table.
3. Go to **Add sort**.
4. In the empty field, select the **column** you want to sort by.
5. In the second field, decide whether the data should be listed in **ascending** or **descending** order.

Repeat the process for **multi-level sorting**. To **change the hierarchy of the sorting rules**, hold down the left mouse button on the six-point gripping area and drag the rule to the desired position.

The sorting is carried out **in real time**, i.e. the data records are sorted before the window is closed. This allows you to see immediately whether you have achieved the desired result and make any necessary adjustments.

## Sorting behavior according to column type

SeaTable supports sorting by all [column types]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) with the exception of the column types **Long text, File, Image, Geolocation, Creator, Last modifier, Button and Digital signature**.

Sorting is based on the following sorting principles:

- Text, Collaborator, E-mail, URL, Phone number: alphabetical or alphanumerical
- Number, Duration, Rating, Autonumber: numerical
- Date, Created, Last modified: chronological
- Single and multiple select: according to the order of the options
- Checkbox: dichotomous
- Formula: depending on the data type of the result
- Link: depending on the data type of the referenced column

All rows **with empty cells in the sorting column** are displayed at the bottom of the view.

## Remove a sort

You can delete a created sort by clicking the **x icon**.

![Delete sorting of records of a view](images/Sortieren-von-Eintraegen-in-einer-Ansicht.png)

## Subsequent addition of rows

An activated sorting is automatically applied to newly added rows.

![Entry sorting](images/Sortierung-von-Eintraegen-1-1.gif)

## Apply multiple sorts

By applying multiple sorts, you can order records that have the **same entry** in a previous sort. For example, you can first sort a list of employees by the options "female", "male", "miscellaneous" via a single selection column and then sort the names of the females, males and miscellaneous each alphabetically via a text column.

![Multiple sorting](images/Mehrere-Sortierungen.png)
