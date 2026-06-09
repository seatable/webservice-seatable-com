---
title: 'Last Modifier and Last Modified Time columns'
date: 2023-01-20
lastmod: '2023-08-04'
categories:
    - 'datum-dauer-und-personen'
author: 'nsc2'
url: '/help/last-editor-modified-date-seatable'
aliases:
    - '/help/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum'
seo:
    title: 'Last editor and modified date columns in SeaTable'
    description: 'SeaTable’s system columns show exactly who changed each row and when. They are vital for tracking, auditing and efficient team processes.'
weight: 23
---

The columns **Last modifier** and **Last modified time** are exclusively filled **automatically** by SeaTable and therefore represent special column types. They prove to be extremely useful if you want to track **when** and **by whom** an entry was **last edited**.

Since the two columns automatically capture changes to entries, they are well suited, for example, as triggers for [automations]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) and [sorting]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}).

## The columns Last modifier and Last modified time

While SeaTable fills the **Last modifier** column with the name of the user who last edited the row, the **Last modified time** column records the moment (date and time) when the last edit occurred.

![The columns Last modifier and Last modified time after being created by a user](images/last-modifiere-and-last-modified-time.png)

## Special features of the two column types

- You **cannot** manually change the automatically entered values in the Last modifier and Last modified time columns. The values update themselves as soon as a change is made to a row.
- When creating the two types of columns, apart from the column name, **no** options are available.
- Only **one** column of each type can be created per table. If you try to create another column of the same type, the message "Another column has this column type." appears.

![Error message for another last modifier column](images/Fehlermeldung-bei-weiterer-Letzter-Bearbeiter-Spalte.png)

- For this reason, you **cannot duplicate** Last modifier and Last modified time columns **and customize their column type**.
