---
title: 'The Calendar view'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/help/the-calendar-view'
aliases:
    - '/help/calendar-plugin-guide-seatable'
    - '/help/anleitung-zum-kalender-plugin'
    - '/help/create-multiple-calendars-base-seatable'
    - '/help/mehrere-kalender-fuer-eine-base-anlegen'
    - '/help/add-calendar-entries-calendar-plugin-seatable'
    - '/help/neue-kalendereintraege-im-kalender-plugin-anlegen'
seo:
    title: 'Calendar view in SeaTable – use chronological overview'
    description: 'The Calendar view in SeaTable displays your appointments per year, month, week, day or in the agenda. Complete setup and tips.'
weight: 13
---

The calendar view shows you data from a table in **calendar form**. You can get an overview of **different time periods (year, month, week, day)** or display appointments as **agenda** in list form.

One example is the monthly overview in a vacation calendar:

![The calendar view](images/calendar-view.jpg)

{{< warning type="warning" headline="Requirements" >}}

To be able to use the calendar view sensibly, you need at least one [date column]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) in your table.

{{< /warning >}}

## To create a calendar view

![Create a calendar view](images/create-calendar-view.jpg)

1. Click on the **Name of the current view**.
2. Click on **Add view or folder** and select the desired **view type**.

![Name a calendar view](images/name-calendar-view.jpg)

3. Give the new view a **name**.
4. Activate the slider if the new view should not be visible to everyone but **private**.
5. Confirm with **Submit**.

![create a calendar view](images/calendar-view-settings.jpg)

6. In the **Title field**, enter the column with which you want to label the calendar entries.
7. Specify which date column should be used for the **Start date**. The calendar view is then generated automatically.
8. Optionally, you can specify a date or duration column for the **End date**, which defines the period of the calendar entries.
9. Finally, select which day of the week should be used as the **first day of the week**.

If you want to change something later, click on the **gearwheel icon** {{< seatable-icon icon="dtable-icon-set-up" >}} in the top right-hand corner and adjust the **settings**.

## View options

You can use the following options in a calendar view:
- [Lock view]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filter]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) or [sort]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) by any value
- [Row color]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Share view with others]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Print view]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})

## The display options in detail

There are a total of 5 display options: You can display appointments in a calendar **yearly**, **monthly** or **weekly** overview, in the **daily planner** or as **agenda** in list form.

You can easily switch between the five display options of the calendar view. Simply click on the corresponding option on the **button** above the calendar.

![Calendar view display options](images/display-options-calendar-view.png)

### Yearly overview

Here you can see the **year** at a glance. The **dot** under a date shows you that there is an entry on that day. You also have the option of clicking on the date to call up the **row details**.

![Year overview in calendar view](images/year-overview-calendar-view.png)

### Monthly overview

This view gives you an overview of all the days in a **month**. You can also call up the **row details** here by clicking on one of the calendar entries.

### Weekly overview

This display shows you the **times** on the vertical axis and the seven days of a **week** from left to right. You can also open the **row details** here by clicking on one of the dates.

### Daily planner

The daily planner is particularly suitable if you want to have several appointments on one **day** on the screen. Just like the weekly overview, it shows you the **times** on the vertical axis. You can also open the **row details** here by clicking on one of the appointments.

### Agenda display

The **Agenda** lists all appointments within a **month** and offers you the option of viewing certain **information** on the appointments at a glance.

To do this, simply show the desired **columns** of the table in the **settings** of the calendar view – for example, topic, status and type of publication.

![Agenda in the calendar view](images/calendar-view-agenda.jpg)

## Add a new record in the calendar view

To add **new records** in the calendar view, you have various options.

### 1. Via the large plus symbol

![Add a new record in the calendar view](images/add-new-record-in-calendar-view.jpg)

Click on the **orange circle with the plus symbol** in the bottom right-hand corner. A new window will open. Create a new data record in the **Row details** and enter the desired data. The changes are saved automatically when you close the window.

{{< warning type="warning" headline="Note" text="This function is available for **all** display options in the calendar." />}}

### 2. Via a calendar field

![Create new calendar entry in the calendar view](images/add-record-in-monthly-calendar-view.jpg)

Move the mouse pointer over a **field** in the calendar and click on the **Plus symbol** that appears in the top right-hand corner. Create a new data record in the **row details** and enter the desired data. The changes are automatically saved when you close the window.

{{< warning type="warning" headline="Note" text="This function only exists for the **month** and **week** display options." />}}

### 3. Double-click

If you **double-click** on a position in the calendar, the **row details** will also open. Otherwise, create the entry in the same way as with the other options.

{{< warning type="warning" headline="Note" text="The double-click only works with the **month**, **week** and **day** display options." />}}

### 4. Pull up dates

For this function, you need **two date columns** that can record **times**.

1. Create two date columns for the **start and end time** and switch on the **accurate to the minute** option in each case.
2. Open the **Calendar view** and select the **Weekly or daily overview**.
3. In the **Settings** (accessible via the cogwheel icon {{< seatable-icon icon="dtable-icon-set-up" >}}), select the two date columns for the calendar.
4. In the calendar, click on the time at which the appointment should start, hold down the **left mouse button** and drag the box to the time at which the appointment should end.

![pull up appointments in the weekly and daily overview](images/add-record-in-weekly-calendar-view.gif)

{{< warning type="warning" headline="Note" text="You can only add appointments in the **weekly or daily overview**." />}}

## Move appointments using drag-and-drop

You can easily move the entries in the calendar view **by drag-and-drop**. This automatically changes the corresponding values in the date columns of your table. This function is available for the **monthly**, **weekly** and **daily** overview.

![Move calendar entries](images/move-record-in-weekly-calendar-view.gif)
