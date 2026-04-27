---
title: 'Color marking of rows'
date: 2022-11-16
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'vge'
url: '/help/color-highlight-rows-seatable'
aliases:
  - '/help/farbliche-markierung-von-zeilen'
seo:
    title: 'Color highlight rows in SeaTable: easy rules & options'
    description: 'Assign colors to rows: use single select, custom rules or highlight duplicates for better table organization, status tracking or quick overviews in SeaTable.'
weight: 27
---

The **color marking of rows** serves the quick identification of certain data sets. This is not to be confused with [coloring cells]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}), which allows you to highlight individual cells.

## The row color tool

In the view options above a table you will find the following icon:

![Color Marking Tool](images/Farbliche-Markierung-von-Zellen-1.png)

After clicking on the row color tool, you can choose between **three options** for color highlighting:

- Use single selection column
- Use rules
- Highlight duplicates

![Color marking of cells](images/Farbliche-Markierung-von-Zellen-2.png)

The row color tool is available not only in table views, but also in [calendar]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}) and [timeline views]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}). However, for the latter you can only use single select columns to define the row color.

## Use single select column

For the **Use single selection column** option, you need a column of this type in your table. This allows you to mark each row at the beginning with the color of the respective option that is entered in this column.

![Color marking of cells](images/Farbliche-Markierung-von-Zellen-3.png)

{{< warning  headline="Creating a single selection column" >}}

Find out [here]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) how to create new single selection columns.

{{< /warning >}}

## Use rules

The **Use rules** option allows you to set conditions for color highlighting.

- Click on the **colored triangle symbol**to change the color of the marker.
  ![Color marking of cells](images/Farbliche-Markierung-von-Zellen-5.png)
- Specify to which of your **Columns** the condition should refer to.
  ![Color marking of cells](images/Farbliche-Markierung-von-Zellen-6.png)
- Decide for the **Condition type**.
  ![Color marking of cells](images/Farbliche-Markierung-von-Zellen-7.png)

{{< warning  headline="Selection of condition types depending on the column type"  text="Please note that what options you have to choose from in the conditions depends on the type of the selected column." />}}

### Use rule example

In this example, all rows in an editorial plan that are marked as completed in the [checkbox column]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}}) are to be marked. To do this, the **"Published" column** was selected, the condition **"is"** was used and it was specified that the rows **with a checkmark** should be marked.

![Color marking of rows](images/Farbliche-Markierung-von-Zellen-9.png)

### Example of a rule with multiple conditions

In this example, we only want to highlight rows the editorial plan in color if the **status** of the post is not "finished", the **publication date** is in the future and an **image** already exists.

![Rule with several conditions for the colored row marking](images/Regel-mit-mehreren-Bedingungen-fuer-die-farbliche-Zeilenmarkierung.png)

## Highlight duplicates

rows with one or more identical column values can be highlighted using the **Highlight Duplicates** option. To do this, select the column you want to check for duplicates. This way you can easily identify duplicates in your table and correct or delete them if necessary.

![Highlight duplicate cells in color](images/Farbliche-Markierung-von-Zellen-9-1.png)
