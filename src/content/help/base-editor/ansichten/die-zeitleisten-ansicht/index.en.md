---
title: 'The Timeline View'
date: 2026-03-31
lastmod: '2026-03-31'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/help/the-timeline-view'
seo:
    title: 'Timeline view: visualize time periods in SeaTable'
    description: 'With the Timeline view you get a clear overview of time periods and their overlaps.'
weight: 15
---

The **Timeline view** allows you to visualize different time periods on a **timeline**. This is very useful, for example, if you want to visualize the sequence of processes or see whether time periods **overlap**. Accordingly, you can use the timeline view for [vacation planning]({{< relref "templates/human-resources/holiday-request-management" >}}), [project plans]({{< relref "templates/projects/project-plan" >}}) or booking conference rooms, among other things.

![The timeline view](images/timeline-view.jpg)

{{< warning type="warning" headline="Requirements" >}}

This view type displays **time spans**. Therefore, you need **two** [date columns]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) in a table that define the **start** and **end** of the time periods. The result is a **Gantt chart**.

{{< /warning >}}

## How to create a timeline view

1. Click on the **name of the current view**.
2. Click on **Add view or folder** and select the desired **View type**.

![Create a timeline view](images/create-timeline-view.png)

3. Give the new view a **name**.
4. Activate the slider if the new view should not be visible to everyone but **private**.
5. Confirm with **Submit**.
6. Then specify the **Start and End date** and the **Date range** that the timeline should cover in the settings. The new view is then generated automatically.
7. In the top input field, select the column on which the **block label** depends.

![Create a timeline view](images/create-timeline-view.gif)

## View options

You can use the following options in a timeline view:
- [Lock view]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filter]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) or [sort]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) by any value
- [Row color]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Share view with others]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Print view]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})

## Display options

There are a total of 5 display options for the scale of the timeline: **Year**, **Quarter**, **Month**, **Week** and **Day**. You can easily switch between these options. Simply click on the corresponding option in the **drop-down menu** above the timeline.

![Display options of the timeline view](images/display-options-timeline-view.jpg)

## Show and hide information

Click on **Show columns** to display more or less information by showing or hiding columns. Activate the **slider** of the respective columns to display more information from the data records in the timeline.

![Show information from other columns in the timeline](images/other-fields-shown-in-timeline-view.gif)

## Edit data records in the timeline view

Double-click on a record and a window with the **Row details** will open. Make the desired adjustments to the data record. The changes are saved automatically when you close the window.

## Extend, shorten or move time periods

To extend or shorten a period, hold down the mouse button and drag **on the left or right edge of a record**. If you want to move a period, hold down the left mouse button and move the entry **by drag and drop** in the desired direction. The corresponding values in the date columns will adjust automatically.

![Change time periods in the timeline view](images/change-records-in-timeline-view.gif)