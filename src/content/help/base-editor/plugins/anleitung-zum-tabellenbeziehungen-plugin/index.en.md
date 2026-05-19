---
title: 'Instructions for the table relationships plugin'
date: 2024-07-29
lastmod: '2024-08-01'
categories:
    - 'plugins'
author: 'kgr'
url: '/help/table-relationships-plugin-guide'
aliases:
    - '/help/anleitung-zum-tabellenbeziehungen-plugin'
seo:
    title: 'Guide to Table Relationships Plugin in SeaTable'
    description: 'Learn how to use the Table Relationships Plugin in SeaTable to visualize and manage table links clearly within your bases.'

---

Especially when there are many tables with dozens of columns in a base, it is easy to lose track of how they relate to each other. Using the table relationships plugin, you can visualize which tables are linked to each other via which columns.

You can find out how to activate the plugin in a base [here]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

![Table relations plugin](images/Table-Relationships-Plugin.png)

## How the plugin works

Once you have set up and opened the table relationships plugin, you will first see **all the tables** in the base. **All columns** that are created in the respective tables are listed under the colored table names.

To visualize the table relationships, you will not only see **solid lines** for _direct_ links via [link columns]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), but also **dashed lines** for _indirect_ links via link formula columns (e.g. [lookups]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}).

## Setting options for a table relationships graphic

By default, a graphic with all table relationships is already created when the table relationships plugin is opened for the first time. If you would like to create another graphic, click on {{< seatable-icon icon="dtable-icon-add-table" >}} **Add new table relationship**. This opens an input field in which you can enter the desired **name**.

![Options of a table relationships graphic](images/Options-of-Table-Relationship-Chart.png)

To **change** the **order of the graphics**, hold down the left mouse button on the **gripping surface** {{< seatable-icon icon="dtable-icon-drag" >}} and **drag and drop** a graphic to the desired position. You can also **rename**, **duplicate** or **delete** the graphics.

{{< warning  headline="Note"  text="If only a single graphic is created in the plugin, you **cannot delete** it." />}}

In the **settings**, which you can access by clicking on the **cogwheel symbol** {{< seatable-icon icon="dtable-icon-set-up" >}}, you can define the following for the graphic by **(de)activating** the **sliders**:

- Would you like to display **links to other entries** (direct connections)?
- Would you like to display **formulas for links** (indirect links)?
- Do you want to display **two-level formulas for links** (e.g. a lookup formula that takes values from the lookup column of another table)?
- Would you like to display **tables without links**?

![Setting options for a table relationships graphic](images/Settings-of-Table-Relationship-Chart.png)

## Move tables in a graphic

You can move the various tables in the graphic as required **using drag and drop**. To do this, hold down the left mouse button, drag the table to the desired position and release.

![Move tables in a table relationships graphic using drag-and-drop](images/Move-tables-in-a-Table-Relationship-Chart.gif)
