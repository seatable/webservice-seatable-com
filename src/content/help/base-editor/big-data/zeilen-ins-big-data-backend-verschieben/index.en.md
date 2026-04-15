---
title: 'Move rows to big data storage'
date: 2022-09-23
lastmod: '2024-05-13'
categories:
    - 'big-data'
author: 'cdb'
url: '/help/move-rows-big-data-backend'
aliases:
    - '/help/zeilen-ins-big-data-backend-verschieben'
seo:
    title: 'Move Rows to SeaTable Big Data Storage – Complete Guide'
    description: 'Learn how to move rows to SeaTable’s big data backend, archive data, restore entries, and activate big data features. Step-by-step guide for Enterprise.'

---

{{< required-version "Enterprise" >}}

You can only create **new rows** in normal SeaTable views. You can then move the rows of the view **manually or automatically** to the big data storage.

{{< warning  headline="Prerequisite" >}}

You can only move rows to the big data storage if [it is already activated]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) within the base.

{{< /warning >}}

## Move rows manually to the big data storage

![move rows manually to the big data storage](images/move-rows-to-big-data.gif)

1. Click the **three dots** in the view options.
2. Select the **Archive View** option.
3. **Confirm** the move of all visible rows to the big data storage.

{{< warning  headline="Tip" >}}

For example, if you want to **archive outdated records**, you can filter the view beforehand using the [Created]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) or [Last modified]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}) time column types.

{{< /warning >}}

The rows are then transferred to the big data storage. As a result, they are no longer visible in the normal view. [Create a big data view]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}) to display data in the big data storage.

## Automated archiving

You can also create an **automation rule with the action "Archive"** so that SeaTable automatically moves the rows in a view to the big data storage at a certain time.

You can find out more about this under [Automation actions]({{< relref "help/base-editor/automationen/automations-aktionen" >}}).

## How can you tell whether data is stored in big data storage or not?

Rows that are archived in the Big Data storage have a small **gray triangle in the numbering column**.

**Good to know:**

- In a [normal view]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}}), you will **not see rows from the big data storage**.
- **All rows** can be displayed in a [big data view]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}), regardless of where they are currently stored.

## Retrieve records from the big data storage

You can find out how to retrieve records from the big data storage [in this article]({{< relref "help/base-editor/big-data/zeilen-aus-dem-big-data-backend-zurueckholen" >}}).
