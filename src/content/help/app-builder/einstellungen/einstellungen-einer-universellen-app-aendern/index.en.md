---
title: 'Change global settings of an app'
date: 2023-05-03
lastmod: '2025-07-03'
categories:
    - 'universelle-apps'
author: 'kgr'
url: '/help/change-universal-app-global-settings'
aliases:
    - '/help/einstellungen-einer-universellen-app-aendern'
seo:
    title: 'Change global settings in an app'
    description: 'Learn how to customize global settings, URLs, navigation and access control in your SeaTable app.'
---

Within an **app**, you can make various **global settings** that affect the configuration and appearance of the entire app with just a few clicks.

## Change the settings of an app

1. Open a **base** in which you want to edit an existing app.
2. Click **Apps** in the base header.
![Click Apps in the base header](images/click-apps-in-the-base-header.jpg)
3. Hover your mouse over the app and click the **pencil icon** {{< seatable-icon icon="dtable-icon-rename" >}}.
![Edit apps](images/Apps-bearbeiten.png)
4. Click the **gear icon** at the top left of the page.
![Gear icon for app settings](images/Zahnrad-Symbol-fuer-App-Einstellungen.png)
5. Make the desired adjustments to the **settings** of the app.

{{< warning  headline="Authorization required in the group"  text="To be able to edit an app, you must be the **owner** or **administrator of the group** in which the underlying **base** is located. Simple **group members** can only view and use the apps." />}}

## Edit the name of the app

In the first section of the app settings you can customize the **name of** the app and save it by clicking **Submit**.

![Change app name](images/Change-app-name.png)

## User-defined URL

In the second section, you can customize part of the **URL** that you can use to access and link to your app. Simply enter your desired URL in the **text field** and note the **requirements** below when entering it. You can then **save** and **copy** the URL you have entered.

![Edit custom URL](images/Edit-custom-URL.png)

**Requirements:** The user-defined part of the URL must be between 5 and 30 characters long and may only contain **letters (a-z), numbers (0-9) and hyphens**.

## Show and hide navigation

In the third section, you can decide whether the **navigation bar** should be shown or hidden by default when the app is opened. The navigation bar is the area on the left-hand side that all users use to navigate to the app's [pages and folders]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}).

![Hide app navigation by default](images/Hide-app-navigation-by-default.png)

This is only a default setting when the app is opened for the first time. Every app user can show and hide the navigation bar as required using the corresponding **icons** or **key combinations**.

![Show and hide navigation](images/Hide-and-show-navigation.gif)

## Collaboration settings

In the fourth section, you can decide whether your **collaborator list** should be visible to all users in the app. You can then enter people in [Collaborator columns]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) or add them to [comments]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}). If you want your collaborators to remain invisible to others, you should deactivate this function.

![Load collaborator list in apps](images/Load-collaborator-list-in-apps.png)

You can also set whether you want to **enable loading comments from the underlying base**. By default, only comments written in the app are visible in the app. If you do not want app users to see the comments from the base, you should deactivate this function.

{{< warning type="warning" headline="Comments are possible on these page types" text="The app comment function can currently be found on table, gallery, kanban, calendar and timeline pages." />}}

## Big Data Management

This section is only relevant if you have activated the [big data storage]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) in your base. Apps can then access data in the big data storage and save entries created via the app directly there. However, new entries are saved in the base by default. To set the Big Data storage as the **storage location for new entries**, simply activate the slider. As the screenshot shows, you can specify for each table whether new rows should be written to the base (empty box) or to the big data storage (checked box).

![Big data management in apps](images/Big-data-management-in-apps.png)

## Open access

In the last section, you can **allow anonymous access**, i.e. make your app publicly accessible. To do this, you must activate the slider. Anyone who calls up the link (even unregistered users) can then see (but not change) the data in the app.

![Open access to an app](images/Open-access-to-an-app.png)

You can also **allow file and image download**. However, if you do not want everyone to be able to use your app without restriction, you can also **enable password protection**. When accessing the app URL, users must then enter the correct password in order to view the data.

However, you can also activate that **any logged-in user who visits the app is automatically registered as app user**. In doing so, you determine which **role** is assigned to the users during registration. Depending on their [authorization]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) on the pages, users with this role can also add, edit or delete rows.

## Edit settings of individual pages

The settings mentioned so far affect an **entire app**. If you want to change the settings of a **single page**, click the **gear icon** {{< seatable-icon icon="dtable-icon-set-up" >}} of the corresponding page in the navigation.

![Open the page settings](images/page-permissions-universal-app.png)
