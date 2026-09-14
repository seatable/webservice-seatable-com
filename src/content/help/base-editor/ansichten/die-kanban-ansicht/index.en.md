---
title: 'The Kanban view'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/help/the-kanban-view'
aliases:
    - '/help/kanban-plugin-guide'
    - '/help/anleitung-zum-kanban-plugin'
seo:
    title: 'Create and use the Kanban view in SeaTable'
    description: 'Learn how to set up the Kanban view in SeaTable and how to use it optimally for the visualization of processes'
weight: 14
---

A **Kanban view** is predestined to visualize dynamic processes with different phases. In this respect, it allows you to visualize **workflows** and **project progress**, for example. It is particularly helpful for [project planning]({{< relref "templates/projects/project-plan" >}}), [software development]({{< relref "templates/it-engineering/bug-tracker" >}}) or task distribution within a team.

{{< warning type="warning" headline="Requirements" >}}

In order to be able to use the Kanban view sensibly, you need at least one column in your table that allows options to be clearly assigned. The column types [Single select]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) or [Collaborator]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) are suitable for this.

{{< /warning>}}

**In this how-to video, we’ll show you in just a few minutes how to create and import a Kanban view in SeaTable.**
{{< youtube C19DWHZzTbg >}}

## Structure of a Kanban view

A Kanban view consists of **pillars** that stand for different steps or phases in a process. In a workflow, for example, these can be "idea", "planned", "in progress" and "done".

![Kanban view](images/kanban-view.jpg)

You provide the columns with **movable cards** that you can move both within a column and from one column to the next. A Kanban card can represent a work package or a task, for example.

![Kanban moves](images/move-records-in-kanban-view.gif)

## How to create a Kanban view

![Create a Kanban view](images/create-kanban-view.jpg)

1. Click on the **Name of the current view**.
2. Click on **Add view or folder** and select the desired **View type**.

![Name a Kanban view](images/name-kanban-view.jpg)

3. Give the new view a **name**.
4. Activate the slider if the new view should not be visible to everyone but **private**.
5. Confirm with **Submit**.

![Group a Kanban view](images/group-kanban-view.jpg)

6. Click on **Add group** and specify which **column** you want to use for the grouping, i.e. the definition of the columns. The Kanban view is then generated automatically.

![Set up a Kanban view](images/kanban-view-settings.jpg)

7. Go to the **settings** and enter the column with which you want to label the Kanban cards in the **Title field**.
8. Optionally, you can also activate **sliders** to enable certain functions.

If you want to change something later, click on the **gearwheel icon** {{< seatable-icon icon="dtable-icon-set-up" >}} in the top right-hand corner and adjust the settings.

## Settings of the Kanban view

You can use the slider options to change the visual display of the Kanban view.

- You can use the **Don't show empty values** slider to remove grayed-out placeholders on the Kanban cards.
- The **Show field names** slider shows the column names above all activated information.
- The **Wrap text** slider formats texts so that they are fully legible on the Kanban board cards.

![kanban view settings](images/show-other-fields-in-kanban-view.gif)

## View options

You can use the following options in a Kanban view:
- [Lock view]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filter]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) or [sort]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) by any value
- [Group]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) by exactly one column
- [Hide columns]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Share view with others]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Show and hide other columns

![Hide columns in the Kanban view](images/hide-columns-in-kanban-view.jpg) 

If you want to display less information on the cards, click on **Hide columns** and deactivate the **sliders** of the respective columns. Reactivating the sliders makes the entries in these columns visible on the cards again.

{{< warning  headline="Note"  text="If the sliders are **not activated**, you cannot see or edit the values in the hidden columns when you open the **row details** either." />}}

## Add a new record in the Kanban view

![Add a new record in the Kanban view](images/add-record-in-kanban-view.jpg)

Click on **Add record** at the bottom of a column. A new window opens. Create a new data record in the **Row details** and enter the required information. The changes are saved automatically when you close the window.

## Edit data records in the Kanban view

Click on a **Kanban card** and a window with the **Row details** opens. Make the desired adjustments to the data record. The changes are saved automatically when you close the window.
