---
title: 'The image column'
date: 2023-06-29
lastmod: '2024-08-02'
categories:
    - 'dateien-und-bilder'
author: 'nsc2'
url: '/help/image-column'
aliases:
    - '/help/die-bild-spalte'
seo:
    title: 'Image column: Manage photos in your SeaTable tables'
    description: 'SeaTable Image Column: Upload, manage and preview images. Add via upload, URL, drag-and-drop and file manager.'
weight: 9
---

With the help of an **image column** you can upload, save and manage new images in your tables with just a few clicks.

## How to create an image column

![Create an image column](images/create-image-column.gif)

1. Click the **\[+\] symbol** to the right of the last column in your table.
2. Give the column a **name** in the upper field.
3. Select the **Image** column type from the drop-down menu.
4. Confirm with **Submit**.

## Add images

In an image column, you have several options for **adding** images. Here's how:

![First double-click in any row of an image column or click on the blue arrow](images/open-image-column.png)

1. Click in the **cell of** an image column.
2. Click on the **plus icon** that appears.
3. A new window will open. Here you can upload **images from your device**, embed them via **URL** or add them from the [file manager]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}).

### Local images

In the **Local Images** section you can click in the field with the Add Documents icon, select one or more **image files on your device** and upload them to the Image column.

![The "Local Images" area of an image column](images/image-column-local-images.png)

{{< warning  headline="Tip"  text="In addition, you can select as many images as you want on your device and **drag** and drop them into the field." />}}

### Image link

In the **Image Link** section you can add images to the image column by entering the image **URL**. To do this, paste the URL into the empty field and click the **link icon** {{< seatable-icon icon="dtable-icon-url" >}}.

![Add images to an image column using the image address ](images/image-link-image-column.png)

{{< warning  headline="Image URL"  text="You can get an image URL, for example, by uploading your images to an image upload service like Postimage or embedding them in your website using a content management system like WordPress." />}}

### Last uploaded

In the **Recently uploaded** section, you have access to the [file management]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) of the base. Images that you have already uploaded to **image** or **file columns** or to **your own folders** are saved there. Select an image and insert it into the image column by clicking **Submit**.

![The "Last Uploaded" area of an image column](images/recently-uploaded-images-image-column.png)

### By drag and drop

You can also **insert** images **directly into a table**. To do this, select any number of **images on your device** and drag them into the **cell of** an image column while holding down the mouse button.

![Drag and drop multiple images from a device into an image column](images/drag-and-drop-files-into-file-column.gif)

## Preview image files

As soon as you insert an image file into the **image column**, the uploaded image is displayed as a **reduced thumb** nail. You can **enlarge** this **thumbnail** by **double-clicking** on the displayed image.

![Preview image files](images/Vorschau-von-Bilddateien.gif)

In **full screen mode**, you can zoom in and out of the images using the **magnifying glasses** and switch between multiple images in a row or column using the **arrows**. You can also **delete** or **download** the displayed image file using the {{< seatable-icon icon="dtable-icon-delete" >}} and {{< seatable-icon icon="dtable-icon-download" >}} icons.

## Image management

In addition to uploading images, you also have various options for managing your images in an image column.

### Download images

You can **download** images stored in an image column with just a few clicks. To do this, first **double-click** in a cell that already contains images _or_ on the **blue double arrow icon**.

Then select the desired **image** and click on the **download icon** {{< seatable-icon icon="dtable-icon-download" >}} in the image.

![Download images from an image column](images/Dana-White.jpg)

If you want to download **all images in a column**, open the drop-down menu above the column header and select **Download all**.

![Download all images in one column](images/Download-all-images.png)

You can then specify **your own file name** and the **number of files** contained in the export will be displayed.

![Dialog box to download all files](images/Download-all-files-dialog.png)

If you click on the **three dots**, you have two options for saving the file: A **download** will save a zip file on your device from which you can extract all the images. You can also save the images **in Seafile**. To do this, you must first [connect a Seafile library to your base]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/eine-seafile-bibliothek-an-seatable-anbinden" >}}).

### Delete images

You can also **delete** all images that are stored in an image column. To do this, first **double-click** in a cell that already contains images _or_ on the **blue double arrow symbol**.

Then select the desired **image** and click on the {{< seatable-icon icon="dtable-icon-x" color="grey" >}} **icon**. Confirm the process by clicking **Delete**.

![Confirmation of deletion](images/confirm-delete.jpg)

{{< warning  headline="Attention" >}}

Images deleted from an image column are still part of base and thus **not** permanently deleted. For more information, read the articles [Accessing deleted files and images]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}}) and [How to permanently remove files]({{< relref "help/base-editor/dateien/wie-man-dateien-dauerhaft-entfernt" >}}).

{{< /warning >}}
