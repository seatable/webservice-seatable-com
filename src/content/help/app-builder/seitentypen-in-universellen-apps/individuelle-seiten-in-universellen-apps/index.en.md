---
title: 'Custom pages in SeaTable apps'
date: 2023-12-08
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/help/custom-pages-seatable-apps'
aliases:    
    - '/help/individuelle-seiten-in-universellen-apps'
    - '/help/custom-pages-universal-apps'
seo:
    title: 'Build and Design Custom Pages in SeaTable Apps'
    description: 'Design custom pages flexibly with text, images & stats, configure elements and easily implement your own designs.'
weight: 6
---

With this page type, you can give free rein to your creativity and build a **customized page** according to your wishes. Add **text** and **images** to your page or use **statistics** to create meaningful **dashboards** with the data from your base.

![Management dashboard in the working time recording app](images/Dashboard_2.gif)

## Create custom pages

If you want to change the settings of a page, click on the corresponding {{< seatable-icon icon="dtable-icon-set-up" >}} **cogwheel symbol** in the navigation bar.

![Change the settings of the custom page](images/Einstellungen-der-individuellen-Seite-aendern.png)

You can use the **page settings** to add various **elements** to your page using drag-and-drop.

![Drag and drop elements on custom pages](images/Drag-and-drop-elements-on-custom-pages.gif)

## Copy, move or delete elements

If you want to copy, move or delete an existing element on your custom page, simply use the three corresponding **symbols** in the top right-hand corner of the frame.

![Copy, move and delete elements on custom pages](images/Copy-move-and-delete-elements-on-custom-pages.gif)

## Element settings

There are additional settings for each **element** of the custom page, which mainly affect the formatting and graphic configuration.

### Text

Text elements are particularly suitable for **headings** or **short texts** that you want to place on your custom page.

![Add texts to custom pages](images/Texte-auf-individuellen-Seiten-hinzufuegen.png)

You can define numerous parameters in the element settings:

- **Font type, size, thickness and color**
- **Line spacing and text alignment**
- **Background and framework**

![Element settings for texts on custom pages](images/Elementeinstellungen-fuer-Texte-auf-individuellen-Seiten.png)

### Formatted text

As the name suggests, you can use formatted text elements to **format longer texts**. This opens the text editor that you already know from the [formatted text]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) column type.

![Formatted texts on custom pages](images/Formatierte-Texte-auf-individuellen-Seiten.png)

As you already have a wide range of formatting options in the text editor, you can only set the **background color** and the **frame of** the text box in the element settings.

![Element settings for formatted texts on custom pages](images/Elementeinstellungen-fuer-formatierte-Texte-auf-individuellen-Seiten.png)

### Horizontal line

To separate different areas on your custom page, you can draw a **horizontal line**. You can specify a **color**, a **background** and a **frame**.

![Element settings for lines on custom pages](images/Elementeinstellungen-fuer-Linien-auf-individuellen-Seiten.png)

### Images

You can easily add **pictures** to make your custom page more attractive. To do this, click on the picture frame that you have previously embedded in the page using drag-and-drop and upload the desired picture from your device.

![Add image to custom page](images/Bild-auf-individueller-Seite-hinzufuegen.gif)

In the element settings, you can define the **fill mode**, the **background** and the **frame** of the image. You can also use **hyperlinks** to link other pages of the app or external resources on an image.

![Element settings for images on custom pages](images/Elementeinstellungen-fuer-Bilder-auf-individuellen-Seiten.png)

### Container

A container provides a **grid** with which you can arrange other elements (e.g. texts, images, statistics) more easily and group them together. First of all, you therefore define **how many rows and columns** this grid should have. This results in the individual boxes into which you can insert other elements using drag-and-drop.

![Container element on custom page in SeaTable 4.3](images/Container-element-on-custom-page.png)

In the element settings, you can add a **title** to the container, the font size, font weight and alignment of which you can adjust. You also have the option of setting the **background color** and the **frame** of the container.

![Element settings for containers on custom pages](images/Elementeinstellungen-fuer-Container-auf-individuellen-Seiten.png)

### Card (design template)

The **card**, which combines an image, a headline and a text into a design template, also ensures a beautiful page layout.

![Card element on custom page in SeaTable 4.3](images/Card-element-on-custom-page.png)

You can insert an **image**, a **title** and **card content** (text) into this template. You can also use a **hyperlink** to link to another page of the app or an external resource.

![Element settings for cards on custom pages](images/Elementeinstellungen-fuer-Karten-auf-individuellen-Seiten.png)

As far as the design of the card is concerned, you first have the option of changing the **fill mode** of the image. Next, you can adjust the **font size, weight and color of** both the title and the card content. Finally, you can set the **background color** and the **border** of the card.

![Style settings for cards on custom pages](images/Stileinstellungen-fuer-Karten-auf-individuellen-Seiten.png)

## Statistics

On a custom page of your app, you can visualize the data from the underlying base using various **graphics** and **diagrams**.

![Add statistics to custom pages](images/Statistiken-auf-individuellen-Seiten-hinzufuegen.gif)

### Data settings

The **configuration of statistics** is very similar to the [statistics module]({{< relref "help/base-editor/statistiken/statistiken" >}}) in the base. First select the **table** from which the statistics should display data. You can change the **chart type** by clicking on the **opposite arrows**.

![](images/Elementeinstellungen-fuer-Statistiken-auf-individuellen-Seiten.png)

You can filter the entries to narrow down the data displayed in the statistics. To do this, click on **Add filter**, select the desired **column** and **condition** and confirm with **Submit**.

![Filter displayed data from statistics](images/Angezeigte-Daten-von-Statistiken-filtern.png)

You can also activate the **drill-down function** and specify exactly for which columns the data should be displayed when you click on the statistics. If the function is deactivated, the chart does not allow any deeper insights into the underlying data. The user only sees the chart itself.

![Drill-down function for statistics](images/Drill-down-Funktion-fuer-Statistiken.gif)

For a bar chart, you must specify the column that is to provide the **values for the x-axis**. Click on the corresponding drop-down field and select the column. You can use a slider to set whether you want to include **empty rows** in the chart.

![Data settings of statistics on custom pages](images/Dateneinstellungen-von-Statistiken-auf-individuellen-Seiten.png)

Then decide how the **values** should be displayed **on the Y-axis**. You can choose between the **number of entries** that have a specific value in the selected column and the **Summarize field** option, where you can evaluate either the sum, the average, the number of unique values, the maximum or the minimum in **numerical columns**.

![Data settings Y-axis of statistics on custom pages](images/Dateneinstellungen-Y-Achse-von-Statistiken-auf-individuellen-Seiten.png)

For **grouped charts**, you can specify a column with options by which you want to group. For some chart types, you can also **sort** the data in ascending or descending order.

### Style settings

Depending on the chart type, you have different style settings to choose from.

For example, you can make the following settings for a **bar chart**:

- Title, font size, font weight and alignment
- Display the title of the X and Y axis
- Automatic limits or minimum and maximum of the Y-axis
- Color and data labeling of the columns
- Frame (shade, color, thickness and radius)

![Style settings for bar charts on custom pages](images/Stileinstellungen-bei-Saeulendiagrammen-auf-individuellen-Seiten.gif)

You can make the following settings for a **pie chart**:

- Title, font size, font weight and alignment
- Show legend and labeling
- Position, format and font size of the labels
- Minimum share of a sector
- Frame (shade, color, thickness and radius)

![Style settings for pie charts on custom pages](images/Stileinstellungen-bei-Kuchendiagrammen-auf-individuellen-Seiten.gif)

All setting changes are carried out **in real time**, i.e. the diagram is updated immediately each time a setting is changed. This allows you to see immediately whether you have achieved the desired result or need to make adjustments.

### Simple table

There is a special type of statistics on custom pages: Similar to [table pages]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}), the **simple table** allows the tabular display of a data set that has been pre-filtered and pre-sorted by the app admin. Unlike on the table page, it is therefore possible to combine **several tables** on one dashboard.

![New chart type "Basic table"](images/BasicTable.png)

## Set the background color of the page

In addition to the colors of the custom page elements, you can also set the **background color** of an entire custom page.

![Set the background color of the custom page](images/Hintergrundfarbe-der-individuellen-Seite.png)

Choose between white, grey and your own color, which you can enter using a hexadecimal code or specify freely in the color selector.

## Hide top bar

If you want to **hide the top bar** on a custom page, you can do this by **activating** the corresponding **slider**.

![Hide top bar](images/hide-top-bar-on-dashboard-pages.png)

## Enable printing the page

If you allow the page to be printed by activating the corresponding **slider**, an icon will be displayed to app users in the top right-hand corner. Using this print function, app users can print the dashboard including all elements (texts, images, statistics, etc.) or export it as a PDF.

![Print dashboard pages](images/print-custom-pages.png)

## Page authorizations

Last but not least, you can limit who can see the page in the page settings.

![Authorization for custom pages](images/Berechtigung-fuer-individuelle-Seiten-der-Universellen-App.png)

This is the only [page authorization]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) you have to choose from for custom pages - because custom pages cannot be used to add, change or delete rows in the table.
