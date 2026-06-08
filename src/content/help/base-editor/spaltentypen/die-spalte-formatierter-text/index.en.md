---
title: 'The Text and Formatted Text columns'
date: 2023-02-21
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/help/text-formatted-text-columns-seatable'
aliases:
    - '/help/die-spalten-text-und-formatierter-text'
seo:
    title: 'Text vs formatted text columns in SeaTable'
    description: 'Use text columns for short entries, formatted text columns for longer, structured data with markdown and more formatting.'

---

For capturing **strings** and **texts of** any kind, SeaTable provides you with two different column types: **Text** and **Formatted Text**. But what exactly is the difference between the two column types? And in which cases does it make sense to use the formatted text column?

## The text column

The text column is one of the most basic **column types** in SeaTable and is also displayed first in the column type selection menu.

![The regular text column](images/select-regular-text-column.png)

In addition, SeaTable automatically adds a **text column** as the first column to each newly created table.

![The "regular" text column ](images/text-column-new.png)

The **first column of** a table has several [peculiarities]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}), as you can read in the linked article.

### Using the text column

The text column is particularly suitable for collecting short entries, such as **terms**, **names**, **words** or other **character strings** that do not have a calculable numerical value, e.g. addresses and telephone numbers.

![Application example of the regular text column](images/regular-text-example.png)

When using the column, it makes sense to keep the entries **short**, since only a **limited number of characters** can be displayed without having to increase the column width.

![Entries that are too long cannot be displayed in their entirety in a text column without increasing the column width](images/use-short-entries.png)

{{< warning  headline="Important note"  text="Please note that **no formatting options** are available for entries in the regular text column." />}}

There are two other text-based column types in SeaTable for special use cases: the [email column]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}) and the [URL column]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}}).

### Set default value

You can define a preset [default value]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) for each text column. This is automatically entered in every new row of the table.

If you set the **{creator.name}** or **{creator.id}** reference as the default value, the **name** or **ID of the user** who added the row is automatically entered.

![Referencing the user name with a default value](images/Set-creator-name-as-default-value.png)

## The Formatted Text column

The **Formatted Text** column type is one of the more specific column types and is displayed second when you select the column type.

![The Formatted Text column](images/formatted-text-column.png)

### Using the Formatted Text column

Formatted text columns are particularly suitable for holding **longer texts**, for example product descriptions, checklists or social media posts.

You do **not** write your entries directly in the cell, but in an **editor** that can be called up with a click, which offers various **formatting options**. In contrast to the text column, you can also structure longer texts.

![Application example of a formatted text column](images/long-text-example.png)

Among other things, you can choose a **paragraph format**, italicize or bold the **font**, and insert **links**, **quotes**, **lists**, **tables**, and **images**.

{{< warning  headline="Character limit"  text="A limit of 100,000 characters applies to individual cells of the Formatted Text type. This corresponds to approximately 25 A4 pages of text. The character limit should therefore only have an effect on your work in exceptional cases." />}}
