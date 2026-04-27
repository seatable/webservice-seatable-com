---
title: 'Query pages in SeaTable apps'
date: 2023-12-08
lastmod: '2025-02-27'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/help/query-pages-seatable-apps'
aliases:
    - '/help/abfrageseiten-in-universellen-apps'
    - '/help/query-pages-universal-apps'
seo:
    title: 'Use query pages in SeaTable Apps'
    description: 'Search and filter large datasets in SeaTable Apps by values: define filters, sorting and query fields for custom results.'
weight: 9
---

Using this page type, you can search your data records for specific values across certain fields. The page type is particularly useful for **extensive data records** such as product catalogs or libraries. A specific use case could be, for example, querying an employee directory.

![Query pages in SeaTable apps](images/Abfrageseiten-in-Universellen-Apps.png)

## Page settings

If you want to change the settings of a page, click on the corresponding {{< seatable-icon icon="dtable-icon-set-up" >}} **cogwheel symbol** in the navigation bar.

![Change query page settings](images/Einstellungen-der-Abfrageseite-aendern.png)

## Preset filters, sorting and hidden columns

In the **page settings**, first define the **table** to be searched.

You can then define preset **filters**, **sorting** and **hidden columns** to limit and organize the data displayed for users. To filter or sort, click on **Add filter** or **Add sorting**, select the desired **column** and **condition** and confirm with **Submit**.

![Add filter on query pages](images/Add-filter-on-query-pages-in-Universal-Apps.png)

Users can see all the information of the applicable data records in the **query results** if you do not restrict them. Therefore, decide which data should be **visible** and show or hide the corresponding columns using the **sliders**.

![Hide columns on query pages](images/Hide-columns-on-query-pages-in-Universal-Apps.png)

{{< warning  headline="Important note"  text="App users **cannot change preset filters** and **hidden columns**. You will therefore only see the filtered entries, as you wish. However, users can customize the **row height** and **sorting** of the queried data records." />}}

## Add query fields

**Query fields** are of central importance for this type of page. They allow users to search the selected table columns for specific values and thus **find data records**. Click on {{< seatable-icon icon="dtable-icon-enlarge" >}} **Add field** in the page settings to define a query field.

![Add fields to query pages](images/Felder-auf-Abfrageseiten-hinzufuegen.png)

You can then select the desired **column** and set whether the query field should be **required**, whether a **fuzzy search** is possible and whether **upper and lower case** are taken into account when making entries.

## Add note

You can add an introductory **note** to your query page, which can contain explanations on how to fill in the query fields, for example. To do this, simply activate the **slider** in the page settings and write the note in the text box that appears.

![Add note to query pages](images/Hinweis-auf-Abfrageseiten-der-Universellen-App-hinzufuegen.png)

## Edit query results

To be able to use this function, you must **activate** the slider in the page settings under **Is the query result editable**.

![Make query result editable](images/Abfrageergebnis-bearbeitbar-machen.png)

All users with access to the query page can then **edit** the **data records** they are looking for.

![Edit query results on query pages of the app](images/Abfrageergebnisse-bearbeiten-auf-Abfrageseiten-der-App.gif)

- Carry out a **successful data query**.
- Move your mouse to the **row numbering** of the hit list and click on the **double arrow symbol** in front of the data record you want to edit.
- Make the desired changes in the open **row details**.
- Click on the **x symbol** to close the window and save your changes.

{{< warning  type="warning" headline="Read-only columns" text="You can define columns in advance that cannot be edited. To do this, go to the page settings and click on the boxes of the columns that should be **read-only** for users. You can recognize read-only columns by the fact that the fields in the row details are highlighted in grey." />}}

## Page authorizations

At the bottom of the page settings, you can restrict who can see the query page.

![Authorization for query pages](images/Berechtigung-fuer-individuelle-Seiten-der-Universellen-App.png)

This is the only [page authorization]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) you can select here. You cannot add or delete rows in the table via query pages.

However, after a successful data query, app users can click on [buttons]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) in the displayed hit list to **perform** certain **actions**.

![Execute buttons on query pages](images/Schaltflaechen-auf-Abfrageseiten-ausfuehren.gif)

One application example is an internal job board: the query page allows you to quickly search for relevant positions. If an interesting position is found, a click on the button in the search results is enough to apply for the position directly.

{{< warning  headline="Attention with buttons" >}}

[Buttons]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) can **always** be pressed regardless of the page authorizations. This means that every app user can make certain changes to the data records that you have previously defined, even if the affected columns are otherwise locked for them or the user is not authorized to edit the query results.

{{< /warning >}}
