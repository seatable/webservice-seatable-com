---
title: 'Instructions for the statistics module'
date: 2023-02-06
lastmod: '2024-03-18'
categories:
    - 'statistiken-und-datenanalyse'
author: 'vge'
url: '/help/stats-module-guide-seatable'
aliases:
    - '/help/anleitung-zum-statistik-modul'
seo:
    title: 'Statistics and charts with SeaTable’s stats module'
    description: 'Visualize data in SeaTable: create charts, build dashboards and analyze trends. Use flexible configuration and real-time updates to present results impressively.'
weight: 1
---

With the **statistics module**, you can display the data from your table visually in the form of various **graphs** and **charts**. This is extremely useful for your work in SeaTable: thanks to the **dashboards**, you always have an overview of the figures and statistical developments in your base.

![Statistics module](images/erweitertes-statistik-plugin-release-notes.gif)

## Open the statistics module

The statistics module is set up by default in every base. You can always access it via the "Statistics" button in the **base header**.

![Statistics module in the base header](images/statistic-plugin-in-base-header.jpg)

## Create a graphic

1. Open the statistics module and click on the button {{< seatable-icon icon="dtable-icon-add-table" >}} **Add chart** in the top right-hand corner.

You have the option to choose from different **types of** graphs and charts. Scroll through the selection or click on the labeled icons in the options bar to jump directly to the desired location.

![Navigate in the statistics module.](images/Navigieren-im-Statistik-Plugin-1.png)

2. Select the appropriate **type** for your statistics and click **Submit**.

### Data settings

3. Specify from which **table** and **view** the graphic should obtain the data.
4. Depending on the graph, you can make different **data settings** – for a bar chart, for example, which values you want to display on the **X and Y axes**.

![Create new graphic in the statistics module.](images/Dateneinstellungen.png)

You start the detailed work on a column chart by selecting the column that will provide the **values for the X-axis**. Click on the corresponding drop-down field and select the **column**. You can use a slider to set whether you want to include **empty rows** in the chart.

Then choose how you want the **values** to be displayed on the **Y-axis**. You can choose between the **number of** entries that have a certain value in the selected column and the **Sum field** option, where you can evaluate either the sum, average, number of unique values, maximum or minimum in **numeric columns**. For **grouped** or **stacked** charts, you can specify a column with options by which you want to group.

All setting changes are executed **in real time**, i.e. the diagram is **updated** immediately with every setting change. This allows you to see directly whether you have achieved the desired result or need to readjust.

### Style settings

5. Give the graphic a **title**. To do this, click on the **Chart style** tab and enter the desired name.
6. If the graphic you selected allows **style settings**, you can configure **X- and Y-axis titles**, **colors** or **data labels**, for example.

![Settings when adding a new graphic in the statistics module.](images/Stileinstellungen.png)

## Graphics on the dashboard

7. After you close the settings window, the saved graphic will appear on your **dashboard**.

You can create **multiple dashboards** and create as many graphics as you want on each dashboard. To change the **order of the graphics**, drag **and drop** them to the desired location. To do this, hover the mouse pointer over the **title of** a graphic until an **arrow cross** appears and hold down the mouse **button**.

![Move graphics in the statistics module.](images/Dashboard_Sortierung_Statistik-Plugin.gif)

## Options for a graphic

When you hover over a graphic, a **double-arrow icon** {{< seatable-icon icon="dtable-icon-open" >}} and a **three-dot icon** {{< seatable-icon icon="dtable-icon-more-level" >}} appear in the upper right corner. Select the double arrow to display a graphic in **full screen mode**. You can access all other options using the three dots:

- Edit graphic
- Copy graphic
- Export as image
- Delete graphic

![Statistics module Graphic options](images/Statistik-Plugin-Grafik-Optionen.gif)

## More display options

By clicking on {{< seatable-icon icon="dtable-icon-full-screen" >}} you can display the entire window of the statistics module in **full screen mode**.

![Statistics module full screen mode](images/Statistik-Plugin-Vollbildmodus.gif)

You can switch between **light and dark mode** using the {{< seatable-icon icon="dtable-icon-night-mode" >}} and {{< seatable-icon icon="dtable-icon-day-mode" >}} icons.

![Night mode statistics module](images/Statistik-Plugin-dark-mode.png)
