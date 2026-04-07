---
title: 'Map pages in apps'
date: 2026-04-07
lastmod: '2026-04-07'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/help/map-pages-in-apps'
seo:
    title: 'Map pages in apps: visualize places on a map'
    description: 'Create map pages in SeaTable apps: flexibly visualize geolocation data and addresses on a world map.'
weight: 9
---

This page type allows you to display **locations**, using **geoposition or address data** from a table, on a **world map** within the app.

![Displaying locations on a map](images/map-page-app-builder.png)

## Page settings

If you want to change the settings of a page, click on the corresponding **gearwheel icon** {{< seatable-icon icon="dtable-icon-set-up" >}} in the navigation bar.

![Change map page settings](images/access-page-settings.png)

In the **page settings** you can select the **map type** (standard or images), the **table**, and a column for the **address field** and the **marker color**. Please note that only certain column types can be used to provide this information.

![Page settings of the map page in apps](images/map-page-settings.png)

If you specify a column for the **display field**, a label for the locations will be permanently displayed on the map.

![Column to be displayed on the map page in apps](images/map-page-display-field.png)

However, you can also define columns to be displayed flexibly, which only become visible through a **hover effect**. Activate the sliders for the columns that should be visible when you move the mouse over a marker.

![hover effect of the columns to be displayed on the map page](images/map-page-hover-display.gif)

## Preset filters and hidden columns

You can also define preset filters and hidden columns to limit the data displayed. To filter, click on **Add filter**, select the desired **Column** and **Condition** and confirm with **Submit**.

![Filter on map pages](images/map-page-filters.png)

Hide the columns that should not be available for the map page using the **slider**.

![Hide columns on map pages](images/hide-columns-on-map-pages.png)

{{< warning type="warning" headline="Important note" text="**Preset filters** and hidden columns **cannot be changed by app users**. They will therefore only see the filtered entries, as you wish." />}}

## Page permissions

For map pages, you can only set one [page permission]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) – namely who is allowed to see the map page. This is because you **cannot add, edit or delete rows** on map pages.