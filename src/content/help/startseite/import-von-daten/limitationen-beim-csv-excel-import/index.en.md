---
title: 'Limitations of CSV/Excel import'
date: 2022-10-15
lastmod: '2024-05-10'
categories:
    - 'import-von-daten'
author: 'nsc2'
url: '/help/csv-excel-import-limitations'
aliases:
    - '/help/limitationen-beim-csv-excel-import'
seo:
    title: 'CSV/Excel Import Limitations in SeaTable Fully Explained'
    description: 'Learn all about row count and file size limits when importing CSV or Excel files in SeaTable Cloud and Server. Detailed info on supported formats and tips.'

---

SeaTable has a powerful import function to make it as easy as possible for you to **import data records from XLSX or CSV files**. In most cases, importing works without any difficulties. If you try to import too many records at once, SeaTable will warn you of the limit. While you can freely choose the **limits for file size and number of rows** on self-hosted SeaTable servers, SeaTable Cloud imposes certain limits on you.

## Maximum file size and number of lines for SeaTable Cloud

When importing Excel files, SeaTable supports this for files up to a maximum size of **100 MB** and up to **50,000 rows**. Due to these generous limits, you should never have problems with the file size. If you have a file that is larger or has more rows , you will need to split it into two **Excel files** and perform the import in two steps.

{{< warning  headline="Memory limit for rows" >}}

The normal SeaTable backend can hold a maximum of 100,000 rows per table. If you want to import an Excel or CSV file that contains more than 100,000 rows , you must first [activate the big data backend]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) in order to be able to [import]({{< relref "help/base-editor/big-data/eine-excel-tabelle-ins-big-data-backend-importieren" >}}).

{{< /warning >}}

## Embedded graphics and files

Importing graphics and files via XLSX file is **not** possible. For such import you need to use SeaTable API, which allows you to import images and files without difficulties.

## Links to other records

There is no way to import data into the column type **Link to other records**. Since SeaTable is a [relational database]({{< relref "posts/relationale-datenbank" >}}), links also work differently from cross-references in Excel.

Everything about handling the link column in SeaTable can be found [here]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

{{< warning headline="Note" >}}
After the import, you can also use the data processing operation [Compare and link]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}}) to create links between specific records.
{{< /warning >}}

## Different file formats

The import function of SeaTable has been tested with files from **LibreOffice** as well as current files from **Microsoft Excel.** Other office programs (such as from the company Softmaker) are **not** actively tested, which may lead to different import results. If in doubt, use Microsoft Excel or the free LibreOffice to get the best results.

{{< warning  headline="Use Excel or Libre Office" >}}

If you still have problems importing data, we recommend that you take a look at the article [Tips and tricks for importing CSV or XLSX files]({{< relref "help/startseite/import-von-daten/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien" >}}). It describes typical pitfalls.

{{< /warning >}}
