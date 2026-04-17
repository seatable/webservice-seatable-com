---
title: 'Timeline pages in SeaTable apps'
date: 2023-12-04
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/help/timeline-pages-in-seatable-apps'
aliases:
    - '/help/zeitstrahlseiten-in-universellen-apps'
    - '/help/timeline-pages-in-universal-apps'
seo:
    title: 'Timeline Pages in SeaTable Apps: Projects & Planning'
    description: 'SeaTable Apps: visualize and manage project schedules and periods on an interactive timeline.'
weight: 8
---

This page type allows you to display different time spans in the form of a **timeline**. As this data view reveals overlapping dates, **vacation planning in a company**, for example, could be a specific use case.

![Timeline page in SeaTable Apps](images/Timeline-page-in-Universal-Apps.png)

## Page settings

If you want to change the settings of a page, click on the corresponding {{< seatable-icon icon="dtable-icon-set-up" >}} **cogwheel symbol** in the navigation bar.

![Changing the settings of the timeline page](images/Einstellungen-der-Zeitstrahlseite-aendern.png)

In the **page settings**, you can first set the graphic display of the timelines. To do this, select the [row color]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}) or a [single selection column]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}), which determines the **color of the blocks**. You can also define a column for the **labeling of the blocks**.

![Graphical setting of the timelines in SeaTable apps](images/Grafische-Einstellung-der-Zeitleisten.png)

To define the period of the entries, you need a [date column]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) for the **start date**. For the **end date**, you can use another date column or a different numerical column – [number]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}), [duration]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}}), or [formula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) – that specifies the number of days. You can also select the **time span**, indicating how many years the timeline should cover.

![Page settings of the timeline page in SeaTable apps](images/Seiteneinstellungen-der-Zeitstrahlseite-in-Universellen-Apps.png)

## Preset filters and hidden columns

You can define **preset filters** and **hidden columns** to limit the data displayed for users. To do this, click on **Add filter**, select the desired **column** and **condition** and confirm with **Submit**.

![Add filter on timeline pages in SeaTable Apps](images/Add-filter-on-timeline-pages-in-Universal-Apps.png)

Users can view more information about an entry by clicking on a block on the timeline. Therefore, decide which data should be **visible** and show or hide the corresponding columns using the **sliders**.

![Hide columns on timeline pages in SeaTable Apps](images/Hide-columns-on-timeline-pages-in-Universal-Apps.png)

{{< warning  headline="Important note"  text="App users **cannot change preset filters** and **hidden columns**. You will therefore only see the filtered data as you wish." />}}

If you add a **grouping**, the bars can also be displayed in **swimlanes**. For non-overlapping activities, this view option results in a compact, clear display.

![Grouping on timeline pages](images/Grouping-on-timeline-pages.png)

## Edit or move an entry on the timeline

You can easily edit entries by clicking on a **bar** and making the desired changes in the **row details** that open.

![Change entries on timeline pages](images/Eintraege-auf-Zeitstrahlseiten-aendern.gif)

You can also **extend** or **shorten** the **time span** directly on the timeline. To do this, grab the right or left **edge of the bar** and drag it to the desired date.

![Move entries to timeline pages](images/Eintraege-auf-Zeitstrahlseiten-verschieben.gif)

You can also conveniently **move** entries on the timeline **using drag-and-drop**. SeaTable automatically adjusts the respective **date values**.

## Link column settings

In the **settings for the link column**, you can define which data is visible and which operations are permitted for each linked table.

![Link column settings on timeline pages in SeaTable Apps](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Field settings**: Here you can define exactly which columns the following authorizations apply to.
- **Allow adding new entries**: If you activate this slider, users can add new entries to the linked table. You can use the field settings to define which columns are **visible** and which columns are **required**, i.e. must be filled in.
- **Allow linking of existing entries**: If you activate this slider, users can link existing entries in the linked table. You can use the field settings to define which columns are **visible**.
- Limit **links to a maximum of one row :** If you activate this slider, users can only link to one row of the linked table in the cells of the link column.
- **Preset filters**: If you add a filter here, only options that fulfill the filter conditions will be displayed when linking entries.
- **Activate big data** function: If the big data function is activated, users can search through more than 20,000 data records, provided there are this many entries in the linked table.
- **Modify linked records**: If you activate this slider, users can edit existing records in the linked table. You can use the field settings to define which columns are **editable**.

## Page authorizations

At the bottom of the page settings, you can restrict who can **see** the timeline page and **edit** entries. You cannot add or delete rows via timeline pages.

![Page authorizations of timeline pages](images/Seitenberechtigungen-von-Kalenderseiten.png)
