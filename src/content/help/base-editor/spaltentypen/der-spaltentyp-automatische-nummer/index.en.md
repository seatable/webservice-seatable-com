---
title: 'The Auto Number column type'
date: 2023-01-07
lastmod: '2023-02-10'
categories:
    - 'text-und-zahlen'
author: 'ssc'
url: '/help/auto-number-column-type'
aliases:
    - '/help/der-spaltentyp-automatische-nummer'
seo:
    title: 'Auto Number column type in SeaTable – all formats & tips'
    description: 'Learn how to use the auto number column in SeaTable: unique record IDs, formatting, resetting, and common pitfalls with numbering gaps.'
weight: 24
---

The **Auto number** column type generates an automatically increasing number for each new row. This column type is used whenever you need a unique identifier for each record.

Note that this column is **not** intended to count the number of records in a table. If you [delete a row]({{< relref "help/base-editor/zeilen/das-loeschen-von-zeilen" >}}), the remaining records will **not** be renumbered. This can lead to **gaps** in the numbering.

To **renumber** your records (for example, to eliminate gaps), you can either delete the _Auto Number_ column and recreate it, or change the column type and then convert it to _Auto Number_ again.

![rows with an automatic number](images/auto-number.gif)

## Three formats are available

When you create the _Auto number_ column, you specify what **format** the values in this column should take. You can choose a **number** with a certain number of digits and prefix this number with a **string of** letters or digits (for example, the current **date**).

![SeaTable Formal Options for the Automatic Number Column](images/Formatmoeglichkeiten-spalten.png)

## Frequently asked questions

Even though the _Auto Number_ column type seems comparatively simple, there are a few special features that need to be considered.

{{< faq "Is it possible to influence the next value used?" >}}Yes. The column offers the possibility in the column options to **reset** the **automatic number** to a certain value, which will then be given to the next row .
{{< /faq >}}
{{< faq "Can values in the column be duplicated?" >}}Yes, this can happen. If you reset the automatic number, values can also occur twice. Thus, the values of this column are not unique.
{{< /faq >}}
{{< faq "Can the column also contain only unique values?" >}}Yes. If you use a Plus or Enterprise subscription of SeaTable, you can **lock** the **column for editing**. This way no one can reset the number and each value remains unique.

{{< /faq >}}
