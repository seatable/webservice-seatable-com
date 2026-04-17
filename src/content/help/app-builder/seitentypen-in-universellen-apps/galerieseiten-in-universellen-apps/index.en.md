---
title: 'Gallery pages in SeaTable apps'
date: 2023-12-04
lastmod: '2024-08-02'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/help/gallery-pages-in-seatable-apps'
aliases:
    - '/help/galerieseiten-in-universellen-apps'
    - '/help/gallery-pages-in-universal-apps'
seo:
    title: 'Gallery Pages in SeaTable Apps: SeaTable Guide'
    description: 'Create gallery pages in SeaTable Apps to show images & data, set filters, manage permissions & leverage flexible linking options.'
weight: 4
---

You can use this page type to display **images** and other data that you have saved in your spreadsheet in the form of a **gallery** within an app. You could use a gallery page for clear **profiles of your employees**, for example.

![Representation of your employees in a gallery page](images/page-type-gallery-example.png)

## Page settings

If you want to change the settings of a page, click on the corresponding {{< seatable-icon icon="dtable-icon-set-up" >}} **cogwheel symbol** in the navigation bar.

![Change gallery page settings](images/Einstellungen-der-Galerieseite-aendern.png)

In the **page settings**, you can select the **table**, the **image column** and the **title column** from which the gallery is fed.

![Page settings of the gallery page in SeaTable apps](images/Seiteneinstellungen-der-Galerieseite-in-Universellen-Apps.png)

## Preset filters, sorting and hidden columns

You can also define preset filters, sorting and hidden columns to limit and organize the data displayed for users. To filter or sort, click on **Add filter** or **Add sorting**, select the desired **column** and **condition** and confirm with **Submit**.

![Add filter on gallery pages in SeaTable Apps](images/Add-filter-on-gallery-pages-in-Universal-Apps.png)

Users can view more information about an index card in the gallery by clicking on an entry.

![Open entry on the gallery page](images/Eintrag-auf-der-Galerieseite-oeffnen.gif)

Therefore, decide which data should be **visible** and show or hide the corresponding columns using the **sliders**.

![Hide columns on gallery pages in SeaTable Apps](images/Hide-columns-on-gallery-pages-in-Universal-Apps-1.png)

{{< warning  headline="Important note"  text="App users **cannot change preset filters**, **sorting** and **hidden columns**. You will therefore only see the filtered entries in a fixed order, as you wish." />}}

## Link column settings

In the **settings for the link column**, you can define which data is visible and which operations are permitted for each linked table.

![Link column settings on table pages in SeaTable Apps](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Field settings**: Here you can define exactly which columns the following authorizations apply to.
- **Allow adding new entries**: If you activate this slider, users can add new entries to the linked table. You can use the field settings to define which columns are **visible** and which columns are **required**, i.e. must be filled in.
- **Allow linking of existing entries**: If you activate this slider, users can link existing entries in the linked table. You can use the field settings to define which columns are **visible**.
- Limit **links to a maximum of one row :** If you activate this slider, users can only link to one row of the linked table in the cells of the link column.
- **Preset filters**: If you add a filter here, only options that fulfill the filter conditions will be displayed when linking entries.
- **Activate big data** function: If the big data function is activated, users can search through more than 20,000 data records, provided there are this many entries in the linked table.
- **Modify linked records**: If you activate this slider, users can edit existing records in the linked table. You can use the field settings to define which columns are **editable**.

## Page authorizations

You can define the following [page authorizations]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) for gallery pages:

![Page authorizations of gallery pages](images/Seitenberechtigungen-von-Galerieseiten.png)

Decide who can view, add, edit and delete the gallery page rows . Thanks to the differentiated authorization options of this page type, you can set this precisely.
