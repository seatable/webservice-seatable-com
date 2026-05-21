---
title: 'Tips and tricks when importing CSV or XLSX files'
date: 2022-10-15
lastmod: '2023-01-19'
categories:
    - 'import-von-daten'
author: 'nsc2'
url: '/help/tips-tricks-csv-xlsx-import-seatable'
aliases:
    - '/help/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien'
seo:
    title: 'CSV/XLSX import tips for SeaTable – quality and structure'
    description: 'Import data to SeaTable without errors: prepare tables, split imports, ensure data quality and check the results for optimal integration.'
---

In SeaTable you have the possibility to import **CSV** as well as **Excel files (.xlsx)** into your bases. To ensure that everything goes according to plan during the data import and that no data is lost, we have summarized the most important **tips and tricks** for importing CSV or XLSX files for you. If you follow these tips and tricks, you will successfully import your data into SeaTable:

- Import table structures only
- Create the table structure in SeaTable before importing
- Split the import
- Ensure the data quality
- Control the import

## Import table structures only

Problems often occur when importing Excel files if they contain **structures** and contents that do **not belong to the table**. The following graphic shows such a case. The heading, the date and the columns A and D do not belong to the table and must be removed before the import.

![Excel list with bad elements](images/tipps-import.png)

**Graphics** are also not taken into account during an import and should therefore be deleted before the import attempt.

## Create the table structure in SeaTable before the import

When SeaTable imports an Excel list, it tries to determine which **column type** to create based on the **imported data**. Problems inevitably arise whenever SeaTable incorrectly determines the column type and the data is not compatible with the column type. For example, if SeaTable recognizes a number and therefore creates a number column, texts and words in this column can no longer be imported and the cells remain the same.

Even if the column recognition typically works reliably, you can easily avoid a possible occurrence of this problem. Instead of having a new base created via import, first create the base yourself with all table columns and then import only the contents.

## Split the import

SeaTable's import function can import Excel files with **multiple spreadsheets** and **tens of thousands rows.** However, experience shows that the more data you try to import in one go, the more likely you are to encounter problems.

Therefore, whenever possible, try to split the import into **smaller data packages**. Rather import the spreadsheets separately and one after the other and split large tables into small ones. This way you have better control over the import and are happy to have completely imported data in the end.

## Ensure data quality

**Data preparation** is essential for a smooth import. Before importing CSV or XLSX files into a base, you should always make sure that the data is cleaned and meets the requirements for import. You can read about the **limitations of** CSV and Excel data import in the corresponding help article [Limitations of CSV/Excel import]({{< relref "help/startseite/import-von-daten/limitationen-beim-csv-excel-import" >}}).

## Control the import

Every data import always includes a **success check**. Do not rely on the fact that everything worked just because you do not get any error messages. Check the imported data for **completeness** and **freedom from errors** before you start processing.
