---
title: 'Limitations in the use of Big Data'
date: 2023-05-11
lastmod: '2024-12-16'
categories:
    - 'big-data'
author: 'nsc2'
url: '/help/big-data-limitations-seatable'
aliases:
    - '/help/einschraenkungen-in-der-nutzung-von-big-data'
seo:
    title: 'SeaTable Big Data: All limitations at a glance'
    description: 'Find out key limitations of SeaTable Big Data: real-time sync, editing, sharing, operations, and practical tips. Optimize your data management and collaboration.'

---

A normal view in SeaTable allows **collaborative** work **in real time** for **up to 100,000 rows**. Big Data allows you to **store unlimited** rows, but reduces your ability to collaborate. Before using Big Data, be sure to take a look at this help article to find out what limitations you should expect when using Big Data.

## Limitations of Big Data

Big data storage offers you largely **unlimited storage of rows**, but also comes with certain restrictions. You can find an overview of the **restrictions** below:

- Changes to a Big Data entry are **not** **synchronized** in **real time** in another user's browser. The changes are only visible to other users after a **reload** of the page.
- You **cannot share** Big Data views - neither individually nor with [user-defined sharing authorizations]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}).
- You **cannot create new rows** in a big data view. This must always be done in a [normal view]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) .
- In a Big Data view, you cannot [customize]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}) edit columns.
- You **cannot change**[linked entries]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) in big data entries. Links to rows in the big data storage are **not displayed** in normal views - but are displayed in a big data view.
- Conditional formatting ([highlightrows in color]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}).
- [Data processing operations]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) are **not** available for big data. The only exception is [compare and join]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}}). This operation can link entries in the big data store with rows in any other table, regardless of whether the rows are stored in the base or in the big data store.
- The [Find and Replace]({{< relref "help/base-editor/tabellen/suchen-und-ersetzen-von-werten-in-seatable" >}}) function is **not** available.

{{< warning  headline="Many of these limitations of big data do not apply to the app" >}}

Most users of big data storage do not feel that their work is affected by these restrictions. However, if you are affected, you can take a look at the [app]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). Some of the restrictions mentioned do not apply there.

{{< /warning >}}
