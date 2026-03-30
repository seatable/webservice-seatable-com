---
title: 'How common datasets work'
date: 2022-12-15
lastmod: '2024-06-12'
categories:
    - 'gemeinsame-datensaetze'
author: 'nsc2'
url: '/help/common-datasets-how-they-work-seatable'
aliases:
    - '/help/funktionsweise-von-gemeinsamen-datensaetzen'
    - '/help/shared-datasets-how-they-work-seatable'
seo:
    title: 'How common datasets work in SeaTable: full guide'
    description: 'Learn how to use, sync and share datasets across teams and bases in SeaTable, including templates, updates and top workflow scenarios.'
star: true
weight: 1
---

Using common datasets, it is possible to make a pre-defined table view available to other groups and users so that they can access specific data in a variety of contexts and departments. Common datasets are a powerful and extremely useful feature in SeaTable, as they can facilitate the workflow in your team.

## Advantages of a common dataset

Compared to a [view]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}}) share, a common dataset offers further possibilities, which are illustrated by the following example:

- An employee list that is relevant to multiple user groups (e.g., HR, Accounting, and Internal Communications) can be made available to your team members via common datasets as a **template for new tables**.
- After your team members import the common dataset into a base, they can add columns to the table as they wish and customize it to their specific use cases (e.g., vacation scheduling, payroll, distribution list for internal newsletters).
- The tables accessing a common dataset can be **synchronized** at any time, i.e. compared with the latest version of the data record (e.g. when new employees join or leave).
- There is a top-down relationship here: changes to the common dataset are transferred to the dependent tables during synchronization. However, changes in these tables have **no** effect on the underlying data set.

{{< warning headline="Common datasets and Big Data storage" text="At this time, it is not possible to use common datasets within a Big Data view." />}}

In the following overview you will also find the links to the various help articles in the common datasets section.

## Create a common dataset

First, publish any table view along with its specific filtering and sorting conditions as a common dataset.

[Learn more about creating a common dataset.]({{< relref "help/startseite/gemeinsame-datensaetze/anlegen-eines-gemeinsamen-datensatzes" >}})

## Management of a common dataset

Would you like to change the name of a common dataset or know which bases are linked to the data set?

[Find out more about managing a common dataset.]({{< relref "help/startseite/gemeinsame-datensaetze/verwaltung-eines-gemeinsamen-datensatzes" >}})

## Share a common dataset with another group

To be able to use a common dataset in other groups, you can share it with any group.

[Learn more about sharing a common dataset.]({{< relref "help/startseite/gemeinsame-datensaetze/freigabe-eines-gemeinsamen-datensatzes-an-eine-andere-gruppe" >}})

## Synchronization of a common dataset

Any table that you have created with a common dataset can be synchronized. When you do this, SeaTable matches the data in the table with that in the common dataset. These are overwritten if you or your group members have made changes to the common dataset since the last synchronization.

[Learn more about synchronization of a common dataset.]({{< relref "help/startseite/gemeinsame-datensaetze/synchronisation-eines-gemeinsamen-datensatzes" >}})

## Create a new table with a common dataset

If you or your team members want to use a common dataset, you can import it into a base. To do this, you create a new table with the common dataset.

[Learn more about creating a new table with a common dataset.]({{< relref "help/startseite/gemeinsame-datensaetze/mit-einem-gemeinsamen-datensatz-eine-neue-tabelle-anlegen" >}})

## Add columns to a table created with a common dataset

After importing a common dataset as a new table into a desired base, you can add your own columns to the table as you wish.

[Learn how to add columns to a table created with a common dataset.]({{< relref "help/startseite/gemeinsame-datensaetze/eine-mit-einem-gemeinsamen-datensatz-erstellte-tabelle-um-spalten-erweitern" >}})

## Reimport of common datasets

If you copy bases into which common datasets are integrated or restore them from snapshots, the connection to the common datasets is lost. Although the data is then available in a normal table, it can no longer be synchronized.

[Here you can find out how to re-import common datasets into existing tables.]({{< relref "help/startseite/gemeinsame-datensaetze/reimport-von-gemeinsamen-datensaetzen" >}})

## Delete a common dataset

Common datasets can, of course, also be deleted. However, be aware of the effects that a deletion has both on the data of the common dataset and on the tables that you and your group members have created with the common dataset.

[Learn more about deleting a common dataset.]({{< relref "help/startseite/gemeinsame-datensaetze/loeschen-eines-gemeinsamen-datensatzes" >}})

### More helpful articles in the common datasets section

- [Why do common datasets only work in groups?]({{< relref "help/startseite/gemeinsame-datensaetze/warum-funktionieren-gemeinsame-datensaetze-nur-in-gruppen" >}})
