---
title: 'Filtering records in a view'
date: 2022-11-16
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/help/filter-records-in-view'
aliases:
    - '/help/filtern-von-eintraegen-in-einer-ansicht'
seo:
    title: 'Filter Records in a SeaTable View: How-To, Options, and Pro Tips'
    description: 'Discover how to use filters in SeaTable views: apply and combine filter rules, target columns by type, and keep your table relevant with custom conditions.'
weight: 21
---

SeaTable's filter function allows you to use **filter rules** to filter out the desired records from a table and display only those records that meet certain criteria. The set filter refers only to the **active view**.

{{< warning headline="Important note" text="Filtering only changes how many data records are displayed in your view! The data basis remains unchanged by filtering and the invisible rows are not deleted. So if data records have disappeared, check whether you are in the correct view or whether you have hidden data records with a filter." />}}

## Filter records in a view

![Filter records](images/Filtern-von-Eintraegen-1.gif)

1. Select the **view** in which you want to set a filter.
2. Click **Filter** in the view options above the table.
3. Go to **Add filter** or **Add filter group**.
4. In the first field, select the **column** for which you want to define a filter rule.
5. In the middle field, specify the **condition** according to which the records are to be filtered.
6. In the last field, decide which **option** or **value** the condition should refer to.

## The different conditions when filtering

SeaTable supports filtering by all [column types]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) except buttons.

Depending on the **column type** you want to filter by, the conditions you can select will also adjust.

### Here are some examples

You have these condition options with a [Text column]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}): 

![Filter text column](images/filtern-von-eintraegen-5.png)

You have these condition options with a [Single selection column]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}): 

![Filter single selection column](images/filtern-von-eintraegen-6.png)

You have these condition options with a [Image column]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}): 

![Filter image column](images/filtern-von-eintraegen-7.png)

Rows **with empty cells** in the filter column are generally not displayed unless "is empty" is explicitly searched for.

## Remove a filter

You can **delete** created filters by clicking on the **x symbol**.

![Removing a filter of a view](images/filtern-von-eintraegen.png)

## Apply multiple filters

You can create one or more filters that further restrict the first condition. Read more about this in the article [Linking filter rules with AND and OR.]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}})

## Rearrange filters

You can move and rearrange filters by moving the mouse on the **six-dot gripping surface**, press and hold, pull and release.

![Filter records sort](images/Filtern-von-Eintraegen-2.gif)
