---
title: 'Data processing: compare and link'
date: 2023-03-20
lastmod: '2023-03-20'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/help/data-processing-compare-link'
aliases:
    - '/help/datenverarbeitung-vergleichen-und-verknuepfen'
seo:
    title: 'Compare and link data automatically in SeaTable'
    description: 'Link records across tables in SeaTable when values match. Automate relations easily with the compare and link operation.'
---

Using the data processing function, you can perform various operations across a column. **Compare and link** is an operation that allows you to link records in two different tables when a column value in both tables is identical.

## Putting on the operation

![Create a data processing action](images/create-an-data-processing-action-1.jpg)

1. Open any **table** and click the **three dots** in the view options.
2. Click **Data Processing**, and then click **Add Data Processing Operation**.
3. Give the operation a **name** and select **Compare and Link**.

![Naming the data processing action and selecting the operation type](images/select-operation-type-example-compare-and-link.jpg)

5. Define **two tables** you want to compare and link, and in which **columns** the values must match for SeaTable to link the records.

![Definition of the data processing action](images/name-and-define-data-operation-compare-and-link-1.png)

{{< warning  headline="Note"  text="By clicking **Add you** can define **any number of columns** where the values must match." />}}

9. Click **Save to** save the action and execute it later, or **Execute** to execute the action directly.

On the first successful execution, a small **Green hook**.  
![If the data processing action is successfully executed for the first time, a green tick appears](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Use case

A concrete use case for this data processing operation could occur, for example, if you work in the accounting department of a company and record in two tables, on the one hand, the **invoices** and, on the other hand, the **transactions** performed.

Here you want a **link to** be created between these tables when the invoice amount in one table matches the remittance amount in the other table. Using the linking you can easily link the related records so that the invoices are assigned to the remittances and the remittances are assigned to the invoices.

For the implementation, you first need two tables: a table in which the invoice numbers**(Invoice Nr**) and amounts are recorded, and a table with the transaction numbers**(Transaction Nr**) and amounts**(Amount**).

![Example table invoices](images/table-invoices.png)

![Example table transactions](images/table-transactions.png)

{{< warning  headline="Important note" >}}

This data processing operation does **not** require you to add **columns** to your tables manually, as a [join column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) is automatically created in both tables when it is first executed.

{{< /warning >}}

To create the data processing operation, follow the steps described above. For the specific use case, select the _Transactions_ and _Invoices_ **tables** and the **Amount** \_columns_with the respective amounts that must match in order to link the records.

![Definition of the data processing action](images/name-and-define-data-operation-compare-and-link-1.png)

If executed successfully, the _Transactions_ and _Invoices_ tables are checked for matches in the defined _Amount columns_. If the **amounts** in these columns match, a **link** is created between the two **tables**.

In this case, a link to the corresponding **transaction** from the _Transactions_ table is added to one side of the corresponding **invoice** in the _Invoices_ table.

![Added link in the Invoices table](images/table-invoices-after-operation.png)

On the other hand, a link to the corresponding **invoice** from the _Invoices_ table is added to the corresponding **transaction** in the _Transactions_ table at the same time.

![Added link in the Transactions table](images/table-transactions-after-operation.png)
