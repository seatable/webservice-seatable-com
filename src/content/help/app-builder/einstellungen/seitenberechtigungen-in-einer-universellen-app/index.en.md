---
title: 'Page permissions in an app'
date: 2023-05-03
lastmod: '2023-11-30'
categories:
    - 'universelle-apps'
author: 'nsc2'
url: '/help/page-permissions-in-a-universal-app'
aliases:
    - '/help/seitenberechtigungen-in-einer-universellen-app'
seo:
    title: 'Page permissions in app – SeaTable guide'
    description: 'Learn how to set and manage page permissions in SeaTable’s app, control user access, roles and data editing rights.'
---

{{< required-version "Enterprise" >}}

To precisely control **access to your data**, you can set **individual page permissions for** each page you have created in an app. You edit the permissions through the page settings.

{{< warning type="warning" headline="Default page permissions" text="When you create **new pages** in your app, they initially grant all available permissions to all users. However, if you want to restrict the usage rights, you will need to adjust the page permissions." />}}

## Set and edit page permissions

1. Open a **base** to which you have already added an app.
2. Click **Apps** in the base header.
![Click Apps in the base header](images/click-apps-in-the-base-header.jpg)
3. Hover your mouse over the app and click the **pencil icon** {{< seatable-icon icon="dtable-icon-rename" >}}.
![Click on the edit icon](images/add-page-to-universal-app-1.png)
4. Select the desired **page** from the navigation on the left side of the page and click on the **gear icon** {{< seatable-icon icon="dtable-icon-set-up" >}}.
![Click on the edit icon](images/page-permissions-universal-app.png)
5. Set the desired **permissions** in the **page settings** that appeared on the right side of the page.
![Setting the page permissions](images/page-permissions.png)
6. The defined page permissions are **automatically** saved and **immediately** applied.

## Which page authorizations are available

You can set the following page permissions:

- Who may add rows ?
- Who may edit rows ?
- Who may delete rows ?
- Who can see the page?

Not all page permissions are available for all [page types]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}). Take a look at this overview:

| Page type                             | Add records                                                     | Modify records                                                  | Delete records                                                  | View page                                                       |
| ------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------| --------------------------------------------------------------- | --------------------------------------------------------------- |
| Table page                            | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Form page                             | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Gallery page                          | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Calendar page                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Custom page                           | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Kanban page                           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Timeline page                         | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Query page                            | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Single record page                    | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## Which user groups you can authorize

For each permission, you can choose from the following options to narrow down the group of people: **Nobody**, **Administrators**, **Specific Roles** and **Everyone**.

![Available page permission options Who can see the page?](images/page-permission-who-can-add-records.png)

Select the **Specific roles** option to define your own roles. To do this, create new **roles** for individual user groups in the [User and Role Management]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}) beforehand, to which you can assign permissions individually on each page of the app.

![Definition of specific roles that have the appropriate authorization](images/define-roles.png)
