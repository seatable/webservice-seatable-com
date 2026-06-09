---
title: 'The Long Text column'
date: 2023-02-21
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'kgr'
url: '/help/long-text-column'
aliases:
    - '/help/die-spalten-text-und-formatierter-text'
    - '/help/text-formatted-text-columns-seatable'
seo:
    title: 'The Long Text column in SeaTable'
    description: 'Use the Long Text column to capture structured texts of any length with line breaks, lists, tables and images, and set a default value.'
weight: 2
---

For **capturing structured texts of any length**, SeaTable provides the *Long Text* column type. In this article, learn what the differences to the text column are and in which cases it makes sense to use the Long text column.

## Using the Long Text column

In contrast to the text column, the **Long Text** column type does not capture unstructured strings, but Long texts with line breaks, lists, images, etc.

![The Long Text column](images/formatted-text-column.png)

Long text columns are particularly suitable for holding **longer texts**, for example product descriptions, checklists or social media posts.

{{< warning  headline="UTF-8"  text="SeaTable supports all characters according to the UTF-8 standard, since UTF-8 is the most widely used character encoding for the internet worldwide." />}}

You do **not** write your entries directly in the cell, but in an **editor** that can be called up with a click, which offers various **formatting options**. In contrast to the text column, you can also structure longer texts.

![Application example of a Long text column](images/long-text-example.png)

Among other things, you can choose a **paragraph format**, italicize or bold the **font**, and insert **links**, **quotes**, **lists**, **tables**, and **images**.

{{< warning  type="warning" headline="Character limit"  text="A limit of 100,000 characters applies to individual cells of the Long Text type. This corresponds to approximately 25 A4 pages of text. The character limit should therefore only have an effect on your work in exceptional cases." />}}

## Other text-based column types

If you want to capture **short strings without formatting** (e.g. names, passwords, license plates), you should use the [text column]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

In addition to the Long text column, there are three other text-based column types in SeaTable for special use cases:
- the [email column]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}})
- the [URL column]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})
- the [phone number column]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

## Set default value

You can define a preset [default value]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) for each Long text column. This text is automatically entered into the cell of every newly created row.

1. Click on the **drop-down arrow** to the right of the column name.
2. Go to **Set default value**.
3. When you click on **Edit text**, the editor opens, where you can write the text that is to serve as the default value.

## Limitations with filters, sorting and grouping

It is not possible to sort or group the entries in a table by Long text columns. With filters, you only have the options "is empty" and "is not empty" available.
