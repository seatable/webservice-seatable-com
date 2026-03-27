---
title: 'General information about bases in SeaTable'
date: 2022-08-25
lastmod: '2023-05-03'
categories:
    - 'arbeiten-mit-bases'
author: 'cdb'
url: '/help/manage-bases-overview-seatable'
aliases:
    - '/help/bases'
seo:
    title: 'SeaTable Bases: Overview, Features and Administration Guide'
    description: 'Find out all about SeaTable bases: organizing, permissions, sharing, exporting, deleting, restoring, and working productively with your data.'
star: true
weight: 1
---

Bases are of central importance in SeaTable. Whenever you collect, analyze, edit or share data in SeaTable, you are in a base.

At first glance, a base is just a **container** for one or more **tables**. From this perspective it is obvious to compare a base with a workbook in Excel. However, this comparison does not do justice to a base. Bases in SeaTable are far superior to the workbooks known from conventional spreadsheets, because they offer:

- [Relational database]({{< relref "posts/relationale-datenbank" >}}) functions and the [linking of tables]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})
- [Over 20 column types]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) covering all common data formats
- Various [sharing options for]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}})
- Real-time [collaboration]({{< relref "help/erste-schritte/einfuehrung-funktionen/zusammenarbeit" >}}) with other users and real-time transmission of all changes
- A [comment function for]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) each record in a row
- Complete [versioning]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) all changes
- An integrated [web form editor]({{< relref "help/base-editor/webformulare/webformulare" >}}) and graphical [plugins]({{< relref "help/base-editor/ansichten" >}})
- Simple integration options thanks to REST API

Bases are therefore much more than "table containers" on the web. You will appreciate these advantages very quickly and never want to miss them again!

## Bases owner

Each base has one (and only one) **owner**. However, transferring ownership of a base from one user to another user is possible.

The owner of a base is either a **user** or a **group**. If a user is the owner of a base, then only this user has full power of disposal. If the base belongs to a group, then all administrators of the group have full access to it. Here you can learn more about the [permissions of individual group members]({{< relref "help/startseite/gruppen/gruppenmitglieder-und-ihre-berechtigungen" >}}).

Direct transfer of ownership from one user to another is currently (as of 3/20/2023) not possible. However, you can **change** ownership indirectly by exporting a base and having the new owner import it. For more information on importing and exporting bases, see the article [Data import and export]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}).

## Creation of bases

You create **new bases** from the home page. You are always on the start page when you log in to SeaTable. If you are currently working in a base, you can return to the start page by clicking on the **base icon** {{< seatable-icon icon="dtable-icon-dtable-logo" >}} in the upper left corner.

In the **My bases** section and in each **group** where you are an administrator, you will find the **Add a base or Folder** button. By clicking this button you create a new base wherever you want.

You have **three options** when creating a new base. You can read more about them in the respective articles:

- [Create empty base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Import base from a file]({{< relref "help/startseite/import-von-daten/welche-import-formate-unterstuetzt-seatable" >}})
- [Create base from template]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}})

## Base management

You manage bases via the **context menu** on the start page. When you move the mouse pointer over one of your bases, a **pencil icon** appears to the right of the name {{< seatable-icon icon="dtable-icon-rename" >}} and a **three-dot icon** {{< seatable-icon icon="dtable-icon-more-vertical" >}} for the advanced options. You will need these regularly to manage your bases.

You cannot **manage** bases shared with you. In the advanced functions of such bases you have only two options: **Exit shared base** and **Copy**.

## Rename bases

You can **rename** bases of which you are the owner or administrator afterwards. Move the mouse pointer to the name of the base you want to rename and click on the **pencil icon** {{< seatable-icon icon="dtable-icon-rename" >}}. You can now change the name and save it by clicking the **Enter key**. Read [here]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}}) what you should consider when naming a base.

## Change icon and color of a base

You can give a new look to the bases you are the owner or administrator of. You can learn how to do it [here]({{< relref "help/startseite/bases/aussehen-einer-base-anpassen-icon-und-farbe" >}}). To bring a breath of fresh air to your bases, you have **more than 10 colors** and **more than 25 icons** at your disposal.

## Add base Description

You can add a description to your bases to give other users an "instruction manual" or to record supplementary information about a base. Learn how to use this feature [here]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}}).

## Share bases

You can **share** bases that you own or administer with other **users and groups**, giving them access to the data. Sharing is done with different permissions, so you always have control over changes in your bases.

For more information on this important and extremely helpful feature, see the article [Base and view shares]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) at a glance.

## Copy a base

You can **copy** all the bases you have access to. Depending on where the base came from and where you want to copy the base to, either the [Duplicating a]({{< relref "help/startseite/bases/eine-base-in-eine-gruppe-kopieren" >}}) article will help you.

## Move bases to folder or add to favorites

If a large number of bases have accumulated on your Home page, it may be useful for clarity to [group several bases together in folders]({{< relref "help/startseite/bases/eine-base-zu-den-favoriten-hinzufuegen" >}}).

## Export base

For backup, transfer to another user or transfer to another SeaTable server you can export bases. Basically, the export is done to a [DTABLE file]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}).

For more information on exporting bases, see the article [Saving a base as a DTABLE File]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}})

## Delete and restore bases

You can [delete]({{< relref "help/startseite/papierkorb/loeschen-einer-base" >}}) and [restore]({{< relref "help/startseite/papierkorb/eine-geloeschte-base-wiederherstellen" >}}) bases that you own or administer as needed for up to 30 days. To do this, follow the instructions in the linked articles.

### Restore base from Snapshot

You can view and restore snapshots of the bases you own or administer. You can learn everything you need to know about snapshots in SeaTable in the articles

- [Saving the current base as a snapshot]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}})
- [Restoring a snapshot]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}})

## Set up email account in a base

If you want to send emails from a base, you need to connect your email account to the base. We will show you how to make use of this useful feature in SeaTable in the article [Setting up an email account in a base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).
