---
title: 'Coloring cells in table views'
date: 2022-10-26
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'vge'
url: '/help/color-cells'
aliases:
    - '/help/einfaerben-von-zellen'
seo:
    title: 'Color Cells in Table Views in SeaTable Based on Rules and Values'
    description: 'Learn to color cells in SeaTable using custom rules or values for easy data analysis and visual highlights. Step-by-step instructions included.'
weight: 28
---

Unlike Excel, you can't just color cells arbitrarily in table views in SeaTable, you have to color them either by **rules** you set or based on the **values** in a **column**. Sounds complicated? But it isn't.

{{< warning  headline="Note" >}}

In addition to the **Color cells** option, there is also the possibility to [mark rows]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}) in color. In this case, however, the cells are not colored, but colored marks are set at the beginning of the rows.

{{< /warning >}}

## Coloring by rules or by values

Each column of a table view offers the option **Color column cells**:  
![Column formatting option shown in SeaTable](images/color-cells.png)

SeaTable will behave differently depending on the **column type** for which you call this option. For [number columns]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}), you can use both rules and values for coloring. For all other column types, only the rules for coloring are available.

![Overview of coloring cells by rules or values](images/color-cells-rules-values.png)

## To color cells by a rule

![Example: Coloring cells using a rule](images/einfaerben-von-zellen-beispiel-1-1.gif)

1. Click the **triangle icon** in the table header of a column.
2. Select the **Color column cells** option.
3. Go to **Use rules**.
4. Click **Add Rule**.
5. Click on the newly appeared row to define the rule.
6. Select a **column** and decide on a **condition** in the middle field.
7. Enter the **value** to which the condition is attached.
8. Click the **colored triangle icon** in front of the rule to open the color picker and change the color of the cells to which your rule applies.

By a rule you color **all cells** in a column to which a rule **applies**. For example, such a rule could be: "Color all cells with a rating of three or more stars yellow."

![Result: One rule colors matching cells yellow](images/Einfaerben-von-Zellen-mit-einer-Regel.png)

You can create **several rules with different colors** per column.

![Multiple rules with different colors in one column](images/Einfaerben-von-Zellen-mit-mehreren-Regeln.png)

You can also define **several conditions** per rule, which can apply to all columns in the table. For example, color the [text column]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) with the headline of an article if the **status** is not "finished", the **publication date** is in the future and an **image** is already available.

![Rule with multiple conditions for cell coloring](images/Regel-mit-mehreren-Bedingungen-fuer-die-farbliche-Zeilenmarkierung.png)

{{< warning  headline="Different options depending on the column type"  text="The **selection** of possible conditions adapts dynamically to the column type." />}}

## To color cells by values

![Example: Coloring cells based on values in SeaTable](images/einfaerben-von-zellen-beispiel-2-1.gif)

1. Click the **triangle icon** in the table header of a column.
2. Select the **Color column cells** option.
3. Go to **Use values**.
4. Click on the **color selector** to choose from more colors
5. Decide from which and up to which **value** you want to format the cells.
6. Click **Submit**.

**Use values** option colors the entire column. The larger a value is in the entire spectrum, the darker or lighter the color of the cell.

![Gradient from light to dark based on cell values](images/einfaerben-von-zellen-2.png)

This type of coloring helps you to quickly and easily make **outliers** (i.e. particularly small or particularly large values) visible in a column.

## Locate duplicates

![Example: Highlight duplicate values in a column](images/einfaerben-von-zellen-beispiel-3.gif)

1. Click the **triangle icon** in the table header of a column.
2. Select the **Color column cells** option.
3. Go to **Highlight Duplicates**.

Using the **Highlight Duplicates** option, you can quickly find identical values in a column.

## Frequently asked questions

### Fill all cells with the same color

To do this, define a rule that applies to all the desired cells. For example, you can color all **filled** cells of a column by selecting the condition **is not empty.**

![FAQ example: Coloring all filled cells](images/einfaerben-von-zellen-6.png)

### Colorize upcoming appointments

Here you have two options to color the respective cells of a date column. Either you select the condition **is on or after** and an **exact date** - or you select the option **is within** and a period in the future.

![Example: Highlight upcoming dates with colors](images/einfaerben-von-zellen-7.png)

### Color a specific date

Select the option **is equal to** and specify the respective date.

![Example: Coloring a specific date](images/einfaerben-von-zellen-8.png)
