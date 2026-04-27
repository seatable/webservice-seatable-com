---
title: 'The Gallery view'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/help/the-gallery-view'
aliases:
    - '/help/gallery-plugin-guide-seatable'
    - '/help/anleitung-zum-galerie-plugin'
    - '/help/add-new-row-via-gallery-plugin'
    - '/help/eine-neue-zeile-ueber-das-galerie-plugin-hinzufuegen'
seo:
    title: 'Gallery view: Display images clearly in SeaTable'
    description: 'With the Gallery view you get a vivid overview of all data records that contain images.'
weight: 12
---

The **Gallery view** uses preview images from an [image column]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) to arrange data records clearly in tiles. Several images are combined in an **album**. This display is suitable for a variety of use cases, for example [employee profiles]({{< relref "templates/human-resources/employee-directory" >}}), [product libraries]({{< relref "templates/product-design/product-library" >}}), [inventory lists]({{< relref "templates/operations/inventory-list" >}}) or [the management of collections]({{< relref "templates/operations/art-gallery-management" >}}).

![The Gallery view](images/gallery-view.jpg)

## How to create a Gallery view

1. Click on the **name of the current view**.
2. Click on **Add view or folder** and select the desired **view type**.

![Create a Gallery view](images/create-gallery-view.jpg)

3. Give the new view a **name**.
4. Activate the slider if the new view should not be visible to everyone but **private**.
5. Confirm with **Submit**.
6. Then specify in the settings which **image column** the images should come from. The new view is then generated automatically.
7. In the **Title field**, enter the column whose entries you want to use as the album title.

![Create a Gallery view](images/create-gallery-view.gif)

## View options

You can use the following options in a Gallery view:
- [Lock view]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filter]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) or [sort]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) by any value
- [Share view with others]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Show and hide information

In the **Gallery settings**, which you can access via the **gearwheel icon** {{< seatable-icon icon="dtable-icon-set-up" >}}, you can display more or less information by showing or hiding columns. Activate the **sliders** of the respective columns to display more information from the data records in the gallery.

![Show information from other columns in the Gallery](images/other-fields-shown-in-gallery-view.jpg)

## Multiple images in one album

The **number of images** per album is displayed in the gallery with a **grey highlighted number**. Logically, the number is only displayed if there is more than one image in an album.

![Number of images gray number](images/image-number.jpg)

Click on the preview image to open the album in **full screen mode**, in which you can enlarge and reduce the images using the **magnifying glasses** and switch between the images using the **arrows**.

![Full screen mode in Gallery view](images/gallery-image-preview.gif)

## Add a new record in the Gallery view

![Add a new record in the Gallery view](images/add-new-record-in-gallery-view.jpg)

Click on the **purple circle with the plus symbol** in the bottom right corner. A new window will open. Create a new data record in the **row details** and enter the desired information and images. The changes are automatically saved when you close the window.

## Edit data records in the Gallery view

![Edit records in Gallery view](images/modify-records-in-gallery-view.jpg)

Click on the **title** of an album and a window with the **row details** will open. Make the desired adjustments to the record. The changes are saved automatically when you close the window.