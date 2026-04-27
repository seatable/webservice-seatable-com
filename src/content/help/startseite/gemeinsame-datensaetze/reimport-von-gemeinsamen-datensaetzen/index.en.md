---
title: 'Reimport of common datasets'
date: 2024-06-11
lastmod: '2024-06-11'
categories:
    - 'gemeinsame-datensaetze'
author: 'kgr'
url: '/help/reimport-common-datasets'
aliases:
    - '/help/reimport-von-gemeinsamen-datensaetzen'
    - '/help/reimport-shared-datasets'
seo:
    title: 'Reimport comkon datasets in SeaTable tables'
    description: 'Learn how to reconnect and synchronize common records in SeaTable after copying or restoring a base and how to check possible impacts.'
---

If you [copy]({{< relref "help/startseite/bases/eine-base-in-eine-gruppe-kopieren" >}}) **bases** into which common datasets are integrated or [restore them]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}}), the **connection to the common datasets** is lost. Although the data is then available in a normal table, it can no longer be synchronized. You can therefore **reimport** common datasets back into existing tables and thus enable **synchronization** with the data there.

## How to link a table to a common dataset again

![Reimport common dataset](images/Reimport-common-dataset.gif)

1. Open a **base** and select the **tab of the table** into which you want to reimport a common dataset.
2. Click on the triangular **drop-down icon** to the right of the table name.
3. Select the **Link to common dataset** option.
4. Select the **common dataset** to which you want to link the table.
5. Confirm with **Link**.

{{< warning  headline="Beware of data loss"  text="Please note the consequences of reimporting listed below before you accidentally delete or overwrite data." />}}

You can tell that the table is linked to the common dataset again by the **stack symbol** in the table tab.

![Icon in front of the name of tables of a common dataset.](images/icon-table-common-dataset.png)

## Consequences of reimportation

- Entries that are contained in the table but not in the common dataset are **deleted** from the table.
- Entries that are contained in both the table and the common dataset are **overwritten** in the table if changes have been made since the last synchronization.
- Entries that are not contained in the table but are contained in the common dataset are **added** to the table.
- Entries in added columns that are contained in the table but not in the common dataset remain **unchanged**.
