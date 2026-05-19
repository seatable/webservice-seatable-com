---
title: 'Links within a table'
date: 2025-02-28
lastmod: '2025-02-28'
categories:
    - 'verknuepfungen'
author: 'kgr'
url: '/help/linking-records-within-table'
aliases:
    - '/help/verknuepfungen-innerhalb-einer-tabelle'
seo:
    title: 'Linking Records Within a Table: SeaTable Guide'
    description: 'How to link rows in the same table: hierarchy, parent-child relations, double link columns, and clear tips for table connections.'

---

With the help of a **link column**, you can not only link several tables with each other, but also **relate data records in one and the same table to each other**.

This is particularly useful if the data in your table has a **hierarchy**.

## Add a link within a table

![Adding a link within a table](images/Verlinkung-innerhalb-einer-Tabelle-hinzufuegen.gif)

1. Click on the **plus symbol** to the right of the last column header.
2. Enter the **name for the parent column** in the input field.
3. Select **Link to other entries** as the column type.
4. Select **the current table** as the table to be linked.
5. Confirm with **Submit**.
6. SeaTable automatically adds a **second column for the subordinate entries**.

{{< warning  headline="Attention" >}}

The two link columns are **inextricably** linked. If you **delete** one of the two columns, the other also disappears immediately. However, if you only want to see one of the two columns in your table, you can [hide]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}}) the other one.

{{< /warning >}}

## Linking data records in a table

![Parent-child relationships in a table](images/Eltern-Kind-Beziehungen-in-einer-Tabelle.gif)

1. Click in a **cell in the link column** and then on the **plus symbol** that appears.
2. The available **rows in the table** are now listed. Click on the row(s) that you would like to link to the selected row .
3. **The linked entry** is immediately displayed in both link columns.

{{< warning  headline="Tip"  text="You can use the **integrated search function** in the link dialog to search through the entries in the table to quickly find the desired row ." />}}

## Why are there two columns for the same link?

If you create a link column that links entries in one and the same table, SeaTable automatically creates a second link column.

- In the **first** link column, you can see the data records that are**superordinate to** a row .
- In the **second** link column, you can see the data records that are**subordinate to** a row .

The **parents and children** of a parent-child relationship are therefore recorded and displayed in separate columns. In this way, SeaTable ensures that there is a parent and a child data record for each relationship.

{{< warning  headline="Note"  text="When you **remove** a **link**, you also delete the entry in the parent or child link column." />}}

## Related articles

- If you want to **visualize** hierarchical links clearly, we can warmly recommend the [organization chart plugin]({{< relref "help/base-editor/plugins/anleitung-zum-organigramm-plugin" >}}).
- For all other questions about handling link columns, please consult the article about the [link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).
