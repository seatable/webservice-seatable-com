---
title: 'Table pages in SeaTable apps'
date: 2023-12-01
lastmod: '2025-07-04'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/help/table-pages-seatable-apps'
aliases:
    - '/help/tabellenseiten-in-universellen-apps'
    - '/help/table-pages-universal-apps'
seo:
    title: 'Design table pages in SeaTable Apps'
    description: 'Add tables as pages in SeaTable Apps, set filters, sorting, grouping and column visibility. Manage editing rights and export the page to Excel with one click.'
weight: 2
---

You can use this page type to [add a table from your base to your app]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}).

![Table page in app](images/Table-page-in-Universal-App.png)

## Change page settings

If you want to change the settings of a page, click on the corresponding {{< seatable-icon icon="dtable-icon-set-up" >}} **cogwheel symbol** in the navigation bar.

![Open the page settings](images/page-permissions-universal-app.png)

When editing table pages, you can make numerous **page settings** to tailor the displayed data from the underlying table precisely to a user group.

![Page settings on table pages](images/Page-settings-on-table-pages.png)

## Preset filters, sorting and grouping

You can define **preset filters**, **sorting** and **grouping** in the page settings to limit and organize the displayed data for a user group.

![Add filter on table page in SeaTable Apps](images/Add-filter-on-table-page-in-Universal-Apps.png)

To do this, click on **Add filter**, **Add sort** or **Add group**, select the desired **column** and **condition** and confirm with **Submit**.

{{< warning  headline="Important note"  text="App users **cannot change preset filters**. They are therefore only shown the filtered data, as you wish. Preset sorting and grouping, on the other hand, only define a **standard view** that users can change individually." />}}

![Default view grouped by one column on a table page in SeaTable Apps](images/Default-view-grouped-by-one-column-on-a-table-page-in-Universal-Apps.png)

{{< warning  headline="Filter by number or duration columns"  text="If you want to filter by number or duration columns, there are certain format specifications to observe. **Decimal numbers** must be written with a dot as a separator, **percentage values** must be entered as decimal numbers (e.g. 99% = 0.99) and the **duration** must be converted into seconds (e.g. 1 hour = 3600 seconds)." />}}

## Hidden and read-only columns

In addition to the preset filters, you can also define **hidden and read-only columns** to further restrict the visibility and editability of certain data.

![Preset hidden columns in App Builder](images/Preset-hidden-columns-in-Universal-App-Builder.png)

Simply click on the **sliders** or **boxes** of the columns that should be **hidden** or **read-only** for the users.

![Read-only columns on table pages in SeaTable Apps](images/Read-only-columns-on-table-pages-in-Universal-Apps.png)

You can recognize read-only columns by the fact that they are highlighted in **grey** in the table and marked with a **lock symbol**.

{{< warning  headline="No inheritance of view settings from the base"  text="Please note that **hidden and locked columns** in the underlying table have **no** effect on the app. When you create a new table page in the app, all columns are initially displayed and can be edited." />}}

## View options of the user

With the **view options** above the table, app users can make their own additional settings, which work in exactly the same way as in the base. These include

- [Filter]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})
- [Sort]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})
- [Group]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})
- [Hide columns]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Set row height]({{< relref "help/base-editor/ansichten/zeilenhoehe-anpassen" >}})
- [Adjust the number of frozen columns]({{< relref "help/base-editor/spalten/anzahl-der-fixierten-spalten-anpassen" >}})

![User view options on table pages in SeaTable Apps](images/user-view-options-on-table-pages-in-apps.png)

As mentioned above, the user's individual view settings **have no effect on the standard settings** you have predefined for the table page. For example, the user can hide additional columns or additionally filter a view that you have pre-filtered, but they cannot display any rows that you have filtered out or columns that you have hidden or even make them visible to others.

## Link column settings

In the **settings for the link column**, you can define which data is visible and which operations are permitted for each linked table.

![Link column settings on table pages in SeaTable Apps](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Field settings**: Here you can define exactly which columns the following authorizations apply to.
- **Add and link new records**: If you activate this slider, users can add new records to the linked table. You can use the field settings to specify which columns are **required**, i.e. must be filled in.
- **Link existing records**: If you activate this slider, users can link existing records in the linked table. You can use the field settings to define which columns are **visible**.
- **Preset filter**: If you add a filter here, only options that fulfill the filter conditions will be displayed when linking records.
- **Enable big data feature**: When the Big Data feature is enabled, users can search more than 20,000 records if there are that many records in the linked table.
- **Limit linking to max one record**: If you activate this slider, users can only link one row of the linked table at a time in the cells of the link column.
- **Modify linked records**: If you activate this slider, users can edit existing records in the linked table. You can use the field settings to define which columns are **editable**.

## Prevent duplicates from being added

On table pages where different users can make new entries in a base, it is easy for **identical rows** to be created. You can prevent this by preventing duplicates from being added. To do this, activate the corresponding **slider** and select the **columns** in which the values must match for an row to be considered a **duplicate**. If the addition of an row is blocked, a corresponding error message appears.

![Prevent the addition of duplicates in SeaTable apps](images/Prevent-adding-duplicate-records-in-Universal-Apps.gif)

## Format check for new entries

You can activate another **slider** to [validate entries in text columns]({{< relref "help/base-editor/spaltentypen/validierung-der-eingabe-bei-textfeldern" >}}). As soon as the **format check** is switched on, the row details always open when someone wants to add a new entry to the table page - and this is only possible if the entries correspond to the defined format. An **error message** appears for entries with a different format.

![Format check on table page](images/Format-check-on-table-page.png)

For example, you can minimize **typing errors** for clearly defined character strings such as zip codes or account numbers. You define the [regular expressions]({{< relref "help/base-editor/spaltentypen/validierung-der-eingabe-bei-textfeldern" >}}) for validating the entries when you create a text column in the base.

## Show cell formatting

If you use the [coloring of cells]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}) in the underlying table, you can activate the option to display the cell formatting on the table page with one click.

![Show cell coloring on table pages in SeaTable Apps](images/Show-cell-coloring-on-table-pages-in-Universal-Apps.gif)

## Export table page as Excel file

This function is disabled by default. If you want to enable Excel export, activate the corresponding slider in the table page settings. All app users who have access to the table page can then export the visible data as an Excel file. To do this, click on the **three dots** in the view options and then on **Export to Excel**.

![Enable Excel export of a table page](images/Enable-Excel-export-of-a-table-page.png)

The data exported from the table page is independent of the current **view**. Even if you **filter or hide columns**, all data is included in the export.

## Page authorizations

In the [page authorizations]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}), you can set exactly who is allowed to view and edit the table.

{{< warning  headline="Attention with buttons" >}}

[Buttons]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) can **always** be activated regardless of the page authorizations. This means that every app user can make certain changes to the data records that you have previously defined, even if the affected columns are otherwise locked for them or the user is not authorized to edit the page.

{{< /warning >}}

![Setting the page permissions](images/page-permissions.png)
