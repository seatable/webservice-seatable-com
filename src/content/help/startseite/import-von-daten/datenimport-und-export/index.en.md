---
title: 'Data import and export'
date: 2022-08-25
lastmod: '2024-03-11'
categories:
    - 'import-von-daten'
author: 'cdb'
url: '/help/data-import-export-seatable'
aliases:
    - '/help/datenimport-und-export'
seo:
    title: 'SeaTable Data Import and Export: Bases, Tables, CSV and Excel'
    description: 'Learn how to import and export bases and tables in SeaTable using DTABLE, Excel, and CSV formats—complete guide with tips and troubleshooting.'
star: true
weight: 1
---

SeaTable's import features make it possible to switch from other solutions to SeaTable with little effort. The same is true when moving from one SeaTable system to another, for example, when migrating from SeaTable Cloud to a self-hosted system. You can seamlessly continue working on a base that you have imported from another SeaTable instance.

How to export bases and tables from SeaTable and import them into SeaTable is the topic of this article.

## Export base

You can export the current status of your bases including all tables, [views]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}), [web forms]({{< relref "help/base-editor/webformulare/webformulare" >}}) and plugins. [Comments]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), [automations]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}) and the [change history]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) as well as [data in the big data backend]({{< relref "help/base-editor/big-data/potenzial-big-data" >}}) are **not exported**.

![Bases export](images/export-bases.png)

For exporting bases, SeaTable uses the [DTABLE file format]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}). For more information, see the article [Saving a base as a DTABLE File]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}).

## Export table

You can **export** individual **tables to Excel files** from any base to which you have access. The contents of text and number-based columns are copied as values to the destination file. [Comments]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), [automations]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}) and the [change history]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) are **not exported**.

![Export tables](images/export-tables.jpg)

You start the export of a table from base. Click on the drop-down arrow to the right of the name of the table you want to export. Now select **Export table to XLSX**.

![Confirm table export](images/confirm-view-export.png)

Decide whether you want to **include images in the export file** by toggling the switch. Confirm with **Export** to start the download. Once the export is complete, you will find the XLSX file in the selected location on your device.

## Export view

You don't want to export all data in a table? Then narrow down the [view]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) using **filters** and **hidden columns**! If you want to export a table view, click the **three dots** in the view options above the table and then **Export view to XLSX**. 

![Export view](images/export-view.png)

Decide whether you want to **include images in the export file** by toggling the switch. 

![Confirm view export](images/confirm-view-export.png)

As soon as you click **Export**, the download starts. Afterwards you will find the XLSX file in the selected location on your device.

## Import base

SeaTable supports importing bases from its own [DTABLE format]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}), from **Excel files**, and from the generic **CSV format**. You can also import bases from Airtable into SeaTable.

When importing a **DTABLE file**, the base is restored exactly as it looked at the time of export. When importing CSV or Excel, the values from the CSV/XLSX file are copied into table columns of a new base, and SeaTable tries to interpret the column types based on the data.

![Importing data into a base](images/import-data-into-your-base.png)

What you need to do when importing a base depends on the type of import file. However, the procedure is the same for all file types: go to the **Home page** and click **Add a base or Folder** in the area or group where you want the new base. You can get more detailed information in the following articles:

- [Creating a base from a DTABLE File]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei" >}})
- [Import Excel files into SeaTable]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}})
- [Data import using CSV in SeaTable]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}})
- [Migration of Airtable bases to SeaTable]({{< relref "help/startseite/import-von-daten/migration-von-airtable-bases-zu-seatable" >}})

## Import table

In existing bases you can **fill** individual **tables via CSV or Excel import**. You have the following options: You can import the data into an **existing table**

![Import data into an existing table](images/Daten-in-eine-bestehende-Tabelle-importieren.png)

or import the data into a **new table**.

![Filling of existing tables via data import](images/import-data-in-table.jpg)

The import is done as a [CSV file]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}}) or [Excel file]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}}) into the table. For more information, see the linked articles.

If you have already created a table in **SeaTable** and need it in **another base**, you can simply copy it over. To learn how to import tables from another base, [click here]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}}).

{{< warning  headline="Memory limit for rows" >}}

SeaTable's normal backend can hold a maximum of 100,000 rows per table. If you want to import an Excel or CSV file that contains more than 100,000 rows , you must first [enable the Big Data backend]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) to import it.

{{< /warning >}}

## More helpful articles about data import

- [Tips and tricks when importing CSV or XLSX files]({{< relref "help/startseite/import-von-daten/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien" >}})
- [Limitations with CSV/Excel import]({{< relref "help/startseite/import-von-daten/limitationen-beim-csv-excel-import" >}})
- [Import of CSV data records into an existing base]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}})
