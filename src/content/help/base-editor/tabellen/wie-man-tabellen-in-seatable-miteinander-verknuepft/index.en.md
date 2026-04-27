---
title: 'How to link tables in SeaTable'
date: 2022-10-11
lastmod: '2023-11-29'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/help/how-to-link-tables-seatable'
aliases:
    - '/help/wie-man-tabellen-in-seatable-miteinander-verknuepft'
seo:
    title: 'How to link tables in SeaTable for powerful relations'
    description: 'Link tables in SeaTable for cross-references and data integration. Step-by-step guide to connect and manage related tables.'

---

Use the [relational database]({{< relref "posts/relationale-datenbank" >}}) functions of SeaTable by linking information from different tables. To do this, use the **Link to other records** column type.

## How to link two tables with each other

![Create link between two tables](images/how-to-link-different-tables.gif)

1. Create a new column and select the column type **Link to other records**.
2. Give the column a **name**.
3. Under **Select table for linking**, select the table whose records you want to link to the current table.
4. Click **Submit**.
5. The content of the new column is still empty. To fill it, you can **link existing records** or **add record** .

As soon as tables are linked, you can call up the information of the linked records via the **link dialog**. To do this, click on the **double arrow symbol** in a **cell of the link column** or **double-click**. The **linked records** are listed in the link dialog that opens. Click on an record to view the **row details** in an additional window.

![Row detail view for linked records](images/Zeilendetailansicht-bei-verknuepften-Eintraegen-711x225.png)

## Link existing records

![Link existing records](images/link-existing-entries.gif)

1. Click in a **cell of the link column** and then on the **plus icon** that appeared.
2. Now the available **rows of the linked table** are listed. Select the row(s) you want to link to the row of your current table.
3. In the link column, each row is immediately displayed **as a linked record**.

{{< warning  headline="Detour via the link dialog"  text="Alternatively, you can open the link dialog first. Click on a **cell in the link column** and then on the blue **double arrow symbol** or make a **double click**. Then click **Link existing records** and select the row(s) as above." />}}

Using the **integrated search function** in the link dialog, you can search the records of the linked table to quickly find the desired row .

{{< warning  headline="Multiple links per cell"  text="You can link **several records of** the linked table in **one cell** of the link column. To do this, repeat the instructions described above." />}}

## Add record

You can even add a **new row** to a **linked table** via the link dialog without having to switch to this table. Subsequently, the row is added to the linked table among the existing records and displayed as a linked record in the link column of the opened table.

1. **Double-click** on the **cell of a link column** or click on the blue **double arrow icon** to open the link dialog.
   ![Double-click in a link column](images/click-in-linked-column.png)
2. Click **Add record**.
   ![Click to add row](images/click-add-record.jpg)
3. In the window that opens, fill in the various **table columns**.
   ![Filling in the table columns](images/fill-columns.png)
4. Click **Submit** to create the new row .
   ![Click submit](images/click-submit.png)
5. The **new row** is automatically added to the **linked table** and displayed in the currently opened table as a **linked record** in the link column.

## Edit existing records of a linked table

![Edit existing records of a linked table](images/edit-linked-entries.gif)

1. Click in a **cell of the link column**.
2. Click on the **linked record** you want to edit.
3. The **row details** open. Make the desired **changes** there.
4. **Close** the window to **save** the changes.

## Remove links

You can remove records linked in a link column with just a few clicks. To do this, simply open the **link dialog** of the corresponding link column and click on the **X symbol** to the right of the desired record.

![Remove links](images/delete-links.png)

{{< warning  headline="Important note"  text="Only the **linked record** is **deleted** from the corresponding link column. The **row in the linked table**, however, remains **intact**." />}}

## Link column settings

A link column allows you to make and change various settings very easily. To do this, click the triangular **drop-down icon of** the link column in the table header and then click **Settings**.

![Open settings of a link column](images/Einstellungen-einer-Link-Spalte-oeffnen-350x200.png)

### Selection of the linked column from the linked table

In the drop-down menu you can first select the **column of the linked table** whose **entries** are to be displayed in the link column.

![Selection of the linked column from the linked table](images/select-column-of-linked-table-to-display.png)

### Limit linking to max one row

By activating the corresponding slider you can limit the linking to a **maximum of one row**. If this setting is active, only **one linked record** can be added in each cell of the link column.

![Restrict links](images/limit-linking-to-max-one-row.png)

If you have already added a linked record to a cell, the options to add more records are **no** longer displayed.

![If the link is limited to a maximum of one row , the options for adding links in the link dialog are no longer available for selection once a link has been added](images/not-visibble-options-to-add-linked-records.png)

This setting can be useful, for example, if an invoice is to be linked to the corresponding purchase order from another table - i.e. if the linked records form logical **pairs**. In this case, adding more links could lead to confusion and negatively affect work processes.

### Limit row selection to a view

By activating this setting you can restrict links to **one view of the linked table**. To do this, you specify a previously defined **view** of the linked table. In the link column, you can then link **only** the records of this view. Linking records from other views is then **no** longer possible.

![Restrict links to one view](images/Verknuepfungen-auf-eine-Ansicht-einschraenken.png)

This setting is especially useful for **filtered views** and can be helpful if you want to specifically link **certain records** in your tables.

### Prevent linking existing records

In the settings of a link column you can also prevent the linking of existing records by activating a corresponding slider. If the slider is **activated**, the corresponding link column supports **only** the addition of **new rows** or records.

Existing records in the linked table can then **no** longer be linked in the column. Records that have already been linked in the column, however, remain **unaffected** by the setting.

![Setting to prevent linking of existing records](images/setting-avoid-linking-existing-records.png)

### Limit row selection using a filter rule

If you activate this option, the selection of linkable rows can be restricted on the basis of filter rules. The filters themselves can be static or dynamic:
- With a **static filter**, you use a uniform value to filter the rows in the linked table (e.g. only rows that do not have the value "archived" are linkable). The effect is therefore similar to the **Limit row selection to a view** option.
- With a **dynamic filter**, the value used for filtering the rows in the linked table is a column value of the active row (e.g. only rows whose status is identical to the status of the active row can be linked). **Rows with different filter values** therefore have different linkable rows.

![restrict links with a filter rule](images/limit-row-selection-using-a-filter-rule.png)

## View options of the link dialog

The link dialog of a link column also provides you with various view options.

### Adjust the size of the window

To have all linked records at a glance, you can adjust the **size of** the link dialog window. To do this, simply move the mouse over one of the outer borders until the cursor turns into a **double arrow**, and drag the border in the desired direction while holding down the mouse button.

![Adjust window size of the link dialog](images/adjust-size-of-the-link-dialogue.gif)

### Adjust column width

To fit more column records of the linked rows into the window, you can also adjust the **width of** the displayed **columns** in the link dialog. To do this, move the mouse over the **area between two column names** until the cursor turns into a **double arrow**, and drag the invisible boundary line to the left or right while holding down the mouse button until you reach the desired **column width**.

![Adjust column width](images/adjust-size-of-columns-in-link-dialog.gif)

### Hide columns

To make the link dialog even clearer, you can hide any number of columns of the linked records by clicking on the **eye symbol**. A window opens in which you can **(de)activate** the individual columns with sliders. Accordingly, the columns are hidden or displayed in the overview of the linked records.

![Hiding certain columns in the linked records view in the dialog box of a linked column](images/hide-columns.in-link-dialog.jpg)

### Sort records

You can **sort** the linked records in the link dialog by clicking on the **arrow icons**. Use this function, for example, to display linked records in alphabetical order based on a text column or to sort them by another column.

![Sorting records in the link dialog of a link column](images/sort-entries-link-dialog.jpg)

{{< warning  headline="Tip"  text="In **combination**, the **view options** have an even greater effect and can help you find specific linked records even faster and more conveniently." />}}

## Frequently asked questions

{{< faq "I can't find this column type. Can't I create a link?" >}}The Link column is available in every SeaTable subscription. However, you are probably trying to change the column type of an existing column. When [changing the]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}}) column type, the **Link to other records** column type is actually _not_ available to you. Instead, create a **new column** and you will be offered the column type you want.

{{< /faq >}}
