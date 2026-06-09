---
title: 'The file column'
date: 2022-11-16
lastmod: '2024-08-02'
categories:
    - 'dateien-und-bilder'
author: 'vge'
url: '/help/file-column-seatable'
aliases:
    - '/help/die-datei-spalte'
seo:
    title: 'File column in SeaTable – manage and share all files'
    description: 'Learn how to use the file column in SeaTable to upload, share, rename, delete and manage multiple documents directly in your table.'
weight: 10
---

In a **file column** you can save one or more files and thus add documents to the respective row .

## How to create a file column

![Create a column.](images/Wie-man-eine-Spalte-anlegt.gif)

1. Click the **\[+\] symbol** to the right of the last column in your table.
2. Give the column a **name** in the upper field.
3. Select the **File** column type from the drop-down menu.

## Upload new files

You can **upload files** in the file column by clicking on a **cell** with the mouse and selecting the **plus icon** that appears. In the newly opened window you can **drag and drop** files or click with the mouse to upload files from your device.

![Upload attachments to a file column](images/upload-files-into-file-column.gif)

{{< warning  headline="Note"  text="SeaTable supports individual files **up to 200 MB** in size. You can upload **any file** type to a file column, but only certain Office documents and images can be viewed and edited directly in SeaTable." />}}

### Upload multiple new files at the same time

![Upload multiple attachments at the same time](images/upload-multiple-files-into-file-column.gif)

1. Click in the **cell of** a file column.
2. Click on the **plus icon** that appears.
3. A new window will open. Here you can **drag and drop** or **click to** upload files from your device.
4. Select multiple files at once by selecting all the documents you want to upload and uploading them together.

{{< warning  headline="Connected to file management" >}}

Files that you upload locally to a file column are saved in a **system folder** that you can access via the [file management]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) of your base.

{{< /warning >}}

## Adding existing files

Besides new files that you upload locally to the cell of a file column, you can also add existing files, which can come from **three sources**:

- **Last uploaded**: Here you will find the most recently uploaded files saved in the base [file manager]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}).
- **My folders**: Here you have access to files in your own folders, which you can create and fill in the [file manager]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}).
- **Seafile**: Here you can select files from [Seafile libraries]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/eine-seafile-bibliothek-an-seatable-anbinden" >}}) that are attached to your base.

![Add existing files to a file column](images/Add-existing-files-to-a-file-column.png)

1. Click in the **cell of** a file column and then on the **plus icon** that appeared.
2. A new window will open. In the navigation on the left, select the **source** from which you want to add a file.
3. Click through the **folder structure to** the desired file.
4. Select the **file** and paste it into the cell by clicking **Submit**.

## Download files

![Download files.](images/Herunterladen-von-Dateien.gif)

1. In the File column, **double-click** the cell that contains the documents you want to download.
2. A new window opens. Here are listed **all the files** that are stored in the cell.
3. So you can create a **single file** download
    - Hover the mouse cursor over the document and click the **download icon** {{< seatable-icon icon="dtable-icon-download" >}}.
4. So you can **Multiple files** download
    - Click **Select.**
    - Select the **Select all** option or put check **marks** in the boxes in front of the files.
    - Then click **Download**.

If you want to download all files in a column, open the drop-down menu above the column header and select **Download all**.

![Download all files in one column](images/Download-all-files.png)

You can then specify **your own file name** and the **number of files** contained in the export will be displayed.

![Dialog box to download all files](images/Download-all-files-dialog.png)

If you click on the **three dots**, you have two options for saving the file: When **downloading**, a zip file is saved on your device from which you can extract all files. You can also save the files **in Seafile**. To do this, you must first [connect a Seafile library to your base]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/eine-seafile-bibliothek-an-seatable-anbinden" >}}).

## Rename files

![Rename attachments of a file column.](images/Datei-Spalte-Anhaenge-umbenennen.gif)

1. Open the **All Files** window by **double-clicking** on a cell in the Files column.
2. Hover the mouse cursor over the file you want to rename and click the **three dots**.
3. Select the **Rename** option and enter a new **file name**.

## Delete files

![Delete attachments.](images/Loeschen-von-Anhaengen.gif)

1. Open the **All Files** window by **double-clicking** on a cell in the Files column.
2. So you can create a **single file** Delete
    - Hover the mouse cursor over the file you want to delete and click the **three dots**.
    - Select the **Delete** option.
3. So you can **Multiple files** Delete
    - Click **Select.**
    - Select the **Select all** option or put check **marks** in the boxes in front of the files.
    - Click **Delete**.

{{< warning  headline="Note" >}}

The files are **not** permanently deleted in this way. Only when you delete the files in the base [file manager]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) are they [permanently removed]({{< relref "help/base-editor/dateien/wie-man-dateien-dauerhaft-entfernt" >}}).

{{< /warning >}}

## Frequently asked questions

{{< faq "Can a file be downloaded on a read share?" >}}Yes. Even if a user has **read-only permission**, he or she can download files.
{{< /faq >}}
{{< faq "Can audio files be played in SeaTable?" >}}No. To play **audio files**, you need to download them first.
{{< /faq >}}
{{< faq "Is it possible to change the order of files in a file column?" >}}No, the order **cannot** be changed within a file column. The first uploaded document comes first. By the order in which you upload the documents, you can determine the order within the file column.

{{< /faq >}}
