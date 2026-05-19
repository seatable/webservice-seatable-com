---
title: 'SeaTable 4.4: Universal App, Excel Import & Common Datasets'
description: 'Buttons enabled on query pages, fill handle for columns, flexible appointments in app calendars, employee fields for forms, more dashboard/chart options, hide title bars on custom pages. Gallery and data query apps consolidated into Universal App, fast/robust Excel import, new dataset sync & copying options.'
date: 2024-05-15
lastmod: '2024-05-15'
author: 'kgr'
url: '/seatable-release-4-4'
color: '#96b228'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 4.4: Universal App, Excel Import, Common Datasets'
    description: 'Universal App now with actionable queries, drag-and-drop calendar, better Excel import, improved datasets and universal default values.'
---

In SeaTable 4.4, we continue the development of the Universal App Builder with verve. Many new functions enable even more powerful and convenient web applications. We have also polished up the import function and the common datasets. The practical default values now apply universally.

This morning we updated SeaTable Cloud to version 4.4. All self-hosters can do the same: The image of SeaTable 4.4 is available for download in the well-known [Docker repository](https://hub.docker.com/r/seatable/seatable-enterprise). As always, you can find the complete list of changes in the [changelog]({{< relref "pages/changelog" >}}).

## More flexible, more powerful App Builder

In SeaTable 4.4 we have again made a lot of improvements and bug fixes to the [Universal App]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}), which benefit almost all [page types]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}). The end of the beta phase is now within reach.

### Buttons on query pages

[Query pages]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}) now support the execution of button actions: After a successful data query, you can press [buttons]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) in the displayed hit list to execute actions. This is a special new feature, as it was previously not possible to interact with queried rows anywhere in SeaTable.

![Execute buttons on query pages](Schaltflaechen-auf-Abfrageseiten-ausfuehren.gif)

One application example is an internal job board: the query page allows you to quickly search for relevant positions. If an interesting position is found, a click on the button in the search results is enough to apply for the position directly.

### Drag and drop in the calendar

Until now, it was not possible to change appointments on the [calendar page]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kalenderseiten-in-universellen-apps" >}}). SeaTable 4.4 gives you more flexibility here. You can now conveniently move your appointments in the calendar using drag and drop. You can also edit the values in the corresponding [date columns]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) via the row details, provided you have the necessary [permission]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}).

### Simplified data handling on the table page

As in Base, you can now [select all entries in a column]({{< relref "help/base-editor/tabellen/hinzufuegen-von-daten-per-copy-and-paste" >}}) on the [table pages]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}) of your apps with just one click on the column header. The practical [fill handle]({{< relref "help/base-editor/zeilen/duplizieren-einer-zeile" >}}) is now also possible: drag the small square in the bottom right-hand corner of a cell downwards to transfer the value to all the rows below it.

![Mark column entries](Spalteneintraege-markieren-und-Fuellgriff-in-App.gif)

### Collaborator column available on form pages

If you use an [employee column]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) in your table, it is **not** available in [web forms]({{< relref "help/base-editor/webformulare" >}}). However, as of SeaTable 4.4, you can add employee columns to [form pages]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}) in the Universal App. For example, your team members can select themselves for a vacation request and no longer have to enter their names manually. You must first activate the option to display the employee list in the [app settings]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern/" >}}).

### More customizing options for custom pages

In version 4.4, you can hide the **title bar** on the [individual page]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}). This allows you to create visually appealing landing pages. For the image and map elements, drop-down menus allow you to quickly **link** to other pages in the app. For the **statistics**, we have added further chart types and additional configuration options to make the creation of dashboards even more convenient. In order to present the many style options clearly, we have divided the chart style and the general style into two different tabs.

## Gallery and data query apps

As announced in the last release notes, we have **removed** the **Gallery App Builder** in SeaTable 4.4. If you want to create a new app with a [gallery]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}), the Universal App Builder offers you an alternative with higher functionality.

{{< warning headline="Good to know" text="**Existing gallery apps will continue to work**. However, we recommend switching existing gallery apps to universal apps in order to benefit from further developments and improvements." />}}

![Create app dialog](Create-app-dialog-.png)

There have also been some changes to the [data query app]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}). The old App Builder for data queries has been removed and replaced by a new one based on the Universal App Builder. This means that you can of course still create public apps for querying your bases, but the interface now looks like the Universal App Builder. The same applies to existing query apps as for gallery apps: you don't have to do anything and can continue to use them.

{{< warning headline="Efficiency gain" text="The changes described allow us to focus on the further development of the Universal App Builder and thus achieve a higher development speed for upcoming features." />}}

## More pleasant user experience when importing Excel files

SeaTable 4.4 makes the [import of Excel tables]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}}) faster, more flexible and more stable: Tables with many thousands rows are now made available in SeaTable in just a few moments. In the significantly enlarged preview window, you can now choose which tables of a workbook – all or only some – you want to import from the XLSX file. While special characters in column names and other special cases led to undesired results in the past, these are now reliably taken into account. Improved error messages provide clear indications of conflicts, especially when [importing into the Big Data Storage]({{< relref "help/base-editor/big-data/eine-excel-tabelle-ins-big-data-backend-importieren" >}}).

![Excel import](Excel-Import.png)

{{< warning headline="A little foretaste" text="With SeaTable 5.0 we make the import even more flexible! You can now also select individual columns of a table and exclude them from the import." />}}

## More functions for common datasets

[Common datasets]({{< relref "help/startseite/gemeinsame-datensaetze/funktionsweise-von-gemeinsamen-datensaetzen" >}}) are very useful if you and your team members need certain tables (e.g. an employee list) across different [groups]({{< relref "help/startseite/gruppen/einfuehrung-in-die-arbeit-mit-gruppen" >}}) in your bases. SeaTable 4.4 adds three new functions to the existing ones:

1. If you  
   [Copy a base
   ]({{< relref "help/startseite/bases/eine-base-in-eine-gruppe-kopieren" >}})to a group in which common datasets are included, you can decide whether you want to retain the connection to these datasets. The group to which you copy the base must of course have access to the common datasets.

    ![Retain link to common dataset when copying a base](Retain-link-to-common-dataset-when-copying-a-base.gif)

2. After  
   [restoring bases from snapshots]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}}) or  
   [creating a base from a template]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}}) you can link existing tables to a common dataset and thus enable synchronization with the data there. Previously, common datasets could not be reimported, but only integrated into new tables.

    ![Reimport common dataset](Reimport-common-dataset.gif)

3. The creator of a common dataset can now force the  
   [synchronization]({{< relref "help/startseite/gemeinsame-datensaetze/synchronisation-eines-gemeinsamen-datensatzes" >}}) of all dependent tables with the data set and thus ensure that the other users use the current status of the data in their bases. In the past, you had to rely on users setting up automatic synchronization or triggering synchronization manually.

    ![Force sync of common dataset](Force-sync-of-common-dataset.png)

## Default values apply everywhere

With version 4.4, SeaTable generalizes the effect of [default values]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}). When you create a new row, whether in the table of a base or app, via a [link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), [web form]({{< relref "help/base-editor/webformulare" >}}), [button]({{< relref "help/base-editor/schaltflaechen/zeilen-per-schaltflaeche-in-eine-andere-tabelle-kopieren" >}}) or [automation]({{< relref "help/base-editor/automationen/automations-aktionen" >}}), the default values are applied everywhere when creating the row. Previously, the default values only applied if a new row was created manually in a table.

As the scope of the default values has increased considerably, we have also created a prominent menu item in the column options, which you can use to conveniently set the default values.

![Default value applies everywhere for new rows](Standardwert-greift-ueberall-bei-neuen-Zeilen.gif)

{{< warning headline="Note" text="If a default value is defined both in the table and in the web form, the value from the form applies to all rows that are created via the form." />}}

By the way: You can even activate the default values with the corresponding parameter when creating a new rows via API.

## And much more

You already know the **editor for formatted text** from various places in SeaTable, e.g. from the [base description]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}}), the [column type for long texts]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) or [e-mail messages]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}). With SeaTable 4.4 we have improved usability and fixed some bugs. Here are just two: Previously, multiple line breaks were removed when closing the editor and existing text was overwritten when typing in the cell. In the new editor, multiple line breaks are retained and can be used to structure the text more clearly. We have also eliminated the risk of unintentional deletions: When typing, the new text is placed in front of the existing text.

In the new version, we have also improved the **notification center** {{< seatable-icon icon="dtable-icon-notice" >}} on the start page. Now you can see all [notifications]({{< relref "help/startseite/benachrichtigungen/sinn-und-zweck-von-benachrichtigungen-in-seatable" >}}) in the system in one place, track the source of the notification and go to the relevant page with one click.

Last but not least, we have optimized the dialog for **resetting the SeaTable password**. To do this, we have standardized the design and added more functions. If you [change]({{< relref "help/startseite/persoenliche-einstellungen/eigenes-passwort-aendern" >}}) the [password]({{< relref "help/startseite/persoenliche-einstellungen/eigenes-passwort-aendern" >}}) in your personal settings, you can now have it displayed in plain text by clicking on the eye symbol. You are also automatically shown the strength of your new password.
