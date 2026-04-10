---
title: 'The collaborator column'
date: 2023-01-07
lastmod: '2024-02-14'
categories:
    - 'datum-dauer-und-personen'
author: 'ssc'
url: '/help/collaborator-column-seatable'
aliases:
    - '/help/die-spalte-mitarbeiter'
seo:
    title: 'The Collaborator Column in SeaTable: Assign People, Notify and Filter Data'
    description: 'SeaTable Collaborator Column: Assign tasks, activate notifications and use flexibly for filters & automations.'
---

In the **collaborator column**, you can assign one or more **people** to row . SeaTable allows you to select people who currently have **access** to the **base** as well as all other team members without access.

![The collaborator column in SeaTable](images/employee-column.png)

## Select persons with access to the base

If you **double-click** in a cell of an collaborator column, a list appears with all users who currently have access to the base. Select one or more of these **people**. You can also use the **search field** to find a specific user.

![Select persons with access to a base in the collaborator column](images/Personen-mit-Zugriff-auf-eine-Base-in-der-Mitarbeiter-Spalte-auswaehlen.png)

{{< warning  headline="Note"  text="If an collaborator's access to a base is **withdrawn** but they are entered in an collaborator column, the value remains in the column until you delete it manually. After removal, the collaborator is no longer available for selection in the list." />}}

## Select team members without access to the base

If you cannot find a user via the search field in the collaborator column, they do **not** currently have **access** to the base. However, if they are a **member of your team**, you can still enter them in the collaborator column.

Click on the {{< seatable-icon icon="dtable-icon-add\_members" >}} icon to add team members without access. Enter the name of the user in the **search field**, select the desired **team member** and confirm with **Add**.

![Enter team members without access to a base in the collaborator column](images/Teammitglieder-ohne-Zugriff-auf-eine-Base-in-die-Mitarbeiter-Spalte-eintragen.gif)

## Notification of the collaborator when adding

When creating an collaborator column, you can **activate** the **slider** so that collaborators receive a [notification]({{< relref "help/startseite/benachrichtigungen/sinn-und-zweck-von-benachrichtigungen-in-seatable" >}}) when others enter them in the column and thus assign them to row .

![Enable notifications to collaborators added to an collaborator column.](images/turn-on-notification-for-collaborateur-1.png)

Collaborators then receive a corresponding notification in base, which they can access via the {{< seatable-icon icon="dtable-icon-notice" >}} **bell symbol** in the top right-hand corner.

![Notification when an collaborator is added](images/Benachrichtigung-wenn-Mitarbeiter-hinzugefuegt-wird.png)

## Set default value

You can set one or more collaborators as the [default value]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) in an collaborator column. You can choose between the options **Current user** or **Specific users**. Whenever someone adds a new row to the table, either the creator of the row or the selected persons are automatically entered in the collaborator column.

![Set default values in collaborator columns](images/Set-default-values-in-collaborator-columns.png)

## Select collaborators as recipients of automated notifications

When sending notifications via [automations]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}), you can select all persons entered in the collaborator column as recipients of the message.

![Collaborator column for automated notifications](images/Collaborator-column-for-automated-notifications.gif)

## The collaborator column in apps

The collaborator column is also an advantage in the [app]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). You can activate the option for team members to be visible to all users in the drop-down list in the app [settings]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}).

If you do not want the app users to be able to see the data records of other users, define **preset filters**: If a page is filtered by collaborator column with the condition "includes current user", each user of the app only sees the entries that are assigned to them in the table.

![Collaborator column in the app](images/Mitarbeiter-Spalte-in-der-Universellen-App.gif)
