---
title: 'Retrieve rows from the big data storage'
date: 2023-05-11
lastmod: '2024-05-13'
categories:
    - 'big-data'
author: 'nsc2'
url: '/help/restore-rows-big-data-storage'
aliases:
    - '/help/zeilen-aus-dem-big-data-backend-zurueckholen'
seo:
    title: 'Restore Rows from Big Data Storage: SeaTable Guide'
    description: 'Learn how to restore archived rows from SeaTable’s Big Data storage back to normal views quickly and effectively.'

---

To retrieve rows from the big data storage, you need a [big data view]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}). In this view, you can [select the desired rows]({{< relref "help/base-editor/zeilen/mehrere-zeilen-selektieren" >}}) and move them back to a **normal view**.

1. Open a **big data view**.
2. Make a **right click on an archived row**.
3. Select the option **Unarchive row**.

![Retrieve entries from the Big Data backend](images/unarchive-rows-out-of-the-big-data-backend.png)

Within a few seconds, the selected rows are written back from the big data memory to the normal view and thus lose their **gray triangle** , which identifies the rows as big data entries.
