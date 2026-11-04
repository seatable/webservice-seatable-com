---
title: 'Guide to the organization chart plugin'
date: 2024-07-18
lastmod: '2025-02-28'
categories:
    - 'plugins'
author: 'kgr'
url: '/help/guide-to-org-chart-plugin'
aliases:
    - '/help/anleitung-zum-organigramm-plugin'
seo:
    title: 'Org Chart Plugin: Visualize Hierarchies & Teams'
    description: 'Org Chart Plugin: Visualize teams, company roles, or project structures as a concise chart in SeaTable. Simple setup & customization.'
---

You can use the organization chart plugin to display **hierarchies** between the data records in a table. This is useful, for example, to visualize the positions in a company or [superordinate and subordinate tasks in a project]({{< relref "templates/projects/work-breakdown-structure" >}}).

{{< youtube OD71y5CJ7vo >}}

You can find out how to activate the plugin in a base [here]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

![Organizational chart plugin](images/Organigramm-Plugin.png)

## Requirements and functionality of the organization chart plugin

To define which data records are dependent on each other, you need a [link that refers to one and the same table]({{< relref "help/base-editor/tabellen/verknuepfungen-innerhalb-einer-tabelle" >}}). The entry that you link in this column to another row in the same table is displayed as a **superordinate data record**.

![Link column for an organization chart](images/Verknuepfungsspalte-fuer-ein-Organigramm.png)

> In the application example with the positions in a company, you would therefore link the employee's respective manager in the link column. This results in the levels of the organizational chart: The department heads would be in the second level and the managing director at the top.

If you want to illustrate the data records in the organization chart with images, you also need an [image column]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) in the table where you can upload photos and graphics.

## Setting options for an organizational chart

By default, an empty organization chart is already created when you first open the organization chart plugin. If you would like to create another organization chart, click on {{< seatable-icon icon="dtable-icon-add-table" >}} **Add organization chart**. This opens an input field in which you can enter the desired **name**.

![Options for organizational charts](images/Optionen-fuer-Organigramme.png)

To **change** the **order of the organigrams**, hold down the left mouse button on the {{< seatable-icon icon="dtable-icon-drag" >}} **grab area** and **drag and drop** the organigram to the desired position. You can also **rename**, **duplicate** or **delete** organization charts.

{{< warning  headline="Note"  text="If only a single organization chart is created in the plugin, you **cannot delete** it." />}}

Via the **settings**, which you can access by clicking on the **cogwheel symbol** {{< seatable-icon icon="dtable-icon-set-up" >}}, you can define the following for the organization chart:

- **Table**: Select the table from which SeaTable should generate the organization chart.
- **View**: Select the view with the data records to be displayed in the organization chart.
- **Relationship**: Select the relationship column on which the hierarchy is based.
- **Title**: Select a column whose values are to be displayed as a title.
- **Cover picture**: Select a picture column to illustrate the data records.
- **Further columns**: Select additional columns whose values are to be displayed.

![Organizational chart settings](images/Einstellungen-eines-Organigramms.png)

{{< warning  headline="Note"  text="Currently, the organization chart can only have **one head** at the top level of the hierarchy. If your company has several managing directors, for example, you should place the company name at the top." />}}
