---
title: 'The first base'
date: 2022-08-25
lastmod: '2023-05-15'
categories:
    - 'kurzanleitungen'
author: 'cdb'
url: '/help/create-first-base-guide-seatable'
aliases:
    - '/help/die-erste-base'
seo:
    title: 'How to Create Your First SeaTable Base: Full Guide'
    description: 'Start with SeaTable: add your first base, set up tables, manage columns and use relations for smarter data organization and collaboration.'
---

In SeaTable you organize your data in [bases]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}). A base is a container for one or more tables. The tables of a base can stand independently next to each other or - as in a database - be linked to each other via relations.

You can also [share]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) with other team members or [invite]({{< relref "help/startseite/freigaben/unterschiede-zwischen-einladungs-links-und-externen-links" >}}) external third parties to work on them together.

SeaTable maintains a [history]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) for each base in the background, allowing you to undo changes and restore previous states if you need to.

## The home page

After logging in, you will find yourself on the **start** page. Here you manage your bases. If you have selected [templates]({{< relref "templates" >}}) during registration, they will be displayed here.

By clicking on the **avatar image** in the upper right corner, you can switch to the [personal settings]({{< relref "help/startseite/persoenliche-einstellungen" >}}) to adjust the system language, for example.

Click on **Add base** to create your first base. Give it a **name**, press **Enter** and the base will be placed on the start page. When you move the mouse pointer over the base name, a **pencil icon** {{< seatable-icon icon="dtable-icon-rename" >}} and the three-dot icon {{< seatable-icon icon="dtable-icon-more-vertical" >}} for the advanced functions appear on the right.

Using the pencil icon, you can rename the base and assign a different icon and color to it. The advanced functions include, for example, [sharing]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) a base or [exporting]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}) it. You open the base by clicking on its name.

## Table view

The new base contains a [table]({{< relref "help/erste-schritte/einfuehrung-funktionen/einfuehrung-in-die-arbeit-mit-bases-und-tabellen" >}}) from the beginning. The Table view is the central, but not the only view of SeaTable. In the Table view you manage the tables of the base, define their column structure and enter or analyze your data.

SeaTable offers a total of [over 20 column types]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}). From conventional spreadsheets you probably already know text, number and date columns. Of course, SeaTable knows these as well. In addition, SeaTable offers columns for images and files, buttons and checkboxes as well as single and multiple select fields.

You want to add images to an entry? Just drag the image into an image column and SeaTable saves it directly into the table. In SeaTable you have all your data in one place!

Another column type that you are not familiar with from a spreadsheet is the [link to other entries]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). With links you create relations between rows of different tables. This procedure, which corresponds to the way relational databases work, avoids double entries, ensures data consistency and creates an overview.

Here is an application example: A property management company records the managed objects in a table and links them to tenants who are managed in another table. If something changes in the object properties, the manager only has to change the adjustment in the object table. By linking, the changed information is automatically updated for all assigned tenants.

[You create additional tables via the table tabs]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}}). Each table has an individual layout: design the columns according to your own wishes and needs.
