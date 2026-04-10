---
title: 'Apps in SeaTable'
date: 2023-05-04
lastmod: '2025-02-13'
categories:
    - 'apps'
author: 'nsc2'
url: '/help/apps-in-seatable'
aliases:
    - '/help/universelle-app'
    - '/help/universal-app'
seo:
    title: 'Apps in SeaTable: Features & Guide'
    description: 'Discover SeaTable apps: page types, dashboards, permissions, user & role management, sharing, copying and design tips.'
weight: 1
---

When building an **app**, you can let your creativity run wild. The app has a number of [page types]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) a **custom page**, you can create dashboards with meaningful **statistics** from your data that you can share with other (external) users.

{{< warning  headline="Authorization required in the group"  text="To be able to create, edit, copy or delete an app, you must be the **owner** or **administrator of the group** in which the underlying **base** is located. Simple **group members** can only view and use existing apps." />}}

## Creating the app

In order to use an app in your base, you must first **add** it to your base.

![Create the app](images/universal-app-preview.png)

[Learn how to add an app to your base here.]({{< relref "help/app-builder/app-verwaltung/apps-zu-einer-base-hinzufuegen" >}})

## Design of the app

After you have successfully created your app, you can start designing it. Make sure to always use the **pencil icon** {{< seatable-icon icon="dtable-icon-rename" >}} to enter the [editing mode of]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}) the app.

![Edit apps](images/Apps-bearbeiten.png)

An app consists of several **pages** that you can group into **folders**.

[Learn how to add new pages and folders to your app here]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}).

To prepare the data in your base in an appealing way, the app offers a variety of [page types]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) with different design elements.

![Page Types app](images/Seitentypen-Universal-App.png)

## Preview of an app

When designing an app, you'll want to test how the app looks to users in between. To do this, you can simply [preview]({{< relref "help/app-builder/app-verwaltung/die-vorschau-einer-app-anzeigen-lassen" >}}) in Edit mode.

## Change settings of an app

Within an app, you can make various **global settings**. For example, you can change the **name**, **color**, and **URL of** your app. You can make the desired adjustments with just a few clicks via the **app settings**.

![Opening the app settings of the app](images/global-settings-universal-app.png)

[Learn more about the global settings of the app here.]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}})

## Saving versions of an app

The **version management** of each app offers you the option of saving snapshots of the structure of an app. You can find out how to create an app **snapshot** [here]({{< relref "help/app-builder/einstellungen/versionsverwaltung-und-snapshots-einer-universellen-app" >}}). Please note what an app snapshot saves - and what it does not save.

## Page permissions in an app

To precisely control access to your data, you can set **individual page permissions for** **each page** you have added to an app. Editing page permissions is always done through the **page settings**, which you can access via the gear icon {{< seatable-icon icon="dtable-icon-set-up" >}}.

![Open the page settings](images/page-permissions-universal-app.png)

[Learn more about the different page permissions in the app here.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

## User and role management of an app

Add new users, create and assign roles - in the **user and role management of** an app you can perform various administrative activities.

![User and role management of an app](images/open-user-and-role-management-1.png)

[Learn more about the user and role management of the app here.]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}})

## Share an app

You can also share an app with other users via the [user and role management]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}). To do this, simply generate an individual **invitation link** or use a **QR code**.

## Copy an app

Have you built an app that you would like to use in a similar form for another user group? Then just copy the existing app and customize the copy as you like. You can learn how to copy an app [here]({{< relref "help/app-builder/app-verwaltung/apps-kopieren" >}}).

## Disable an app

If you've created an app that you want to temporarily disable, you can disable it with just a few clicks to revoke access to all user groups. You can find out how to do this [here]({{< relref "help/app-builder/app-verwaltung/apps-zeitweise-deaktivieren" >}}).

## Delete an app

You can **delete** an app that you no longer need at any time. Please note the consequences of the deletion.

[Learn more about deleting an app here.]({{< relref "help/app-builder/app-verwaltung/apps-loeschen" >}})

## No collaborative work in apps

While the app has many advantages over [working in the]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}) base, there is a big difference if you want to work on the data together in a team. In a base, every change made by other users is displayed immediately. The entries change in real time. This type of collaborative work is not supported in the app.

## Comments in apps

Nevertheless, you also have the option of communicating with other team members in an app. To do this, use the [comment function]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) that you already know in the same form from base. Record your feedback or additional information on the data records for the other app users and hold discussions on the spot.

![Comment function in apps](images/Kommentarfunktion-in-Universellen-Apps.png)

{{< warning  headline="Good to know"  text="The comments in the app are completely **independent** of the comments in the base. This means that every comment in the app is only visible where it was posted - not in the base and not in other apps, even if it is the same data record." />}}
