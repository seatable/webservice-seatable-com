---
title: 'Adjust row height in table views'
date: 2022-10-26
lastmod: '2023-03-28'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/help/adjust-row-height'
aliases:
    - '/help/zeilenhoehe-anpassen'
seo:
    title: 'Adjust Row Height in Table Views and See More Data'
    description: 'Learn how to change row height in SeaTable table views and display more data. Step-by-step guide for all settings and best practices.'
weight: 29
---

By default, SeaTable displays all rows in table views with a compact row height to show as many records as possible. However, with this **default row height**, among other things, [text]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}), [link]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})and [multiple select columns]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}) are truncated and only small **thumbnails** of images are displayed.

![Truncated cell contents](images/small-row-height-cut-cells.png)

This row height may be suitable for most of your use cases, but there may be situations when you want to see more content of the respective rows. That's why SeaTable allows you to adjust the row height in table views.

Specifically, four different row heights are available for this purpose:

- Default (the default value for new table views)
- Double
- Triple
- Quadruple

## Adjust row height

![Adjust row height](images/set-row-height-new.gif)

1. Click the **row height** icon in the view options above the table.
2. **Set** the desired row height.

{{< warning  headline="One row height for all rows"  text="The row height is always adjusted for **all** rows of a table view. Individual row heights within a view are not possible." />}}
