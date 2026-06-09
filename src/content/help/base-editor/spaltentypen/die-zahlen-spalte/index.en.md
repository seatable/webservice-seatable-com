---
title: 'The number column'
date: 2023-01-08
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'ssc'
url: '/help/number-column'
aliases:
    - '/help/die-zahlen-spalte'
seo:
    title: 'Number column in SeaTable – formats, settings & tips'
    description: 'Easily track, format and validate numbers, percentages, and currencies in SeaTable. Everything about number columns at a glance.'
weight: 3
---

In SeaTable you can use the **Number column** in many ways to work with numbers of any kind (e.g. number of items, percentages, or prices in different currencies).

## Application area of the number column

The use of **number columns** allows you, for example, to **calculate values** with formulas and create clear **diagrams and statistics**. However, it is not suitable for saving strings of any length (e.g. account numbers), as rounding occurs with more than 15 digits. In this case, you should use the [text column]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

In addition, SeaTable offers other column types that sometimes better match the values to be stored:

- Duration and periods = [duration column]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})
- Date and times = [date column]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- Scores = [rating column]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})
- Serial numbers = [Auto Number]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- Phone numbers = [phone number column]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})
- Geo information = [geolocation column]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}})

## Adding a number column

![Adding a column of numbers](images/hinzufuegen-einer-zahlenspalte.gif)

1. Click the **plus icon** to the right of the last column.
2. Give the column a **name**.
3. Select **Number** as the column type.
4. Decide on a **format** (e.g. number, percentage or currency).
5. With a click on **More settings** you can also set details.
6. Add the column with **Submit**.

## Format settings

You can also edit and fine-tune the **number format** afterwards. To do this, first open the drop-down menu with the **column options** via the triangle {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} in the column header and then click on {{< seatable-icon icon="dtable-icon-set-up" color="grey" >}} **Format settings**.

You can now select a different **format**, set **decimal** and **thousands separators**, and change the number of **decimal places**.

### Available formats of the numbers column

The following number formats are available:

- **Number**

    Use a simple number, for example, for the number of items.

- **Percent**

    Use percentages, for example, for progress in completing tasks.

- **Currencies (Yuan, Dollar & Euro)**

    Use different currencies, for example, for the prices of products.

- **Custom currency**

    Use a custom currency where the currency symbol can be entered individually.

## Set default value and validate input

You can [define]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) for each number column, which is automatically entered in every row that you add to your table.

To identify **errors** and **extreme values** directly, you can also **validate** the **input**. To do this, define a **numerical range** in which the values of the column should lie; cells with a higher or lower value are then highlighted in color.

You can make these settings when creating the number column or afterwards:

1. Open the drop-down menu with the **column options** via the triangle {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} in the column header.
2. Then click on **Customize column type**.
3. Click on **Further settings** and activate the corresponding **sliders** at the bottom.

![Format settings of number columns](images/Format-settings-of-number-columns.png)
