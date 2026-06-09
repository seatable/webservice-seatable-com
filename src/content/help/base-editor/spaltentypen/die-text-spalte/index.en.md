---
title: 'The text column'
date: 2023-05-03
lastmod: '2024-03-11'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/help/text-column'
aliases:
    - '/help/validierung-der-eingabe-bei-textfeldern'
    - '/help/validate-textfield-regex-seatable'
seo:
    title: 'The text column in SeaTable'
    description: 'Use the text column for short alphanumeric strings such as terms, names, passwords or IBANs, set default values and validate input with regular expressions.'
weight: 1
---

The text column is one of the most basic **column types** in SeaTable and is also displayed first in the column type selection menu.

![The regular text column](images/select-regular-text-column.png)

By default, SeaTable automatically adds a **text column** as the first column to every newly created table. In addition, you can manually add as many text columns to your table as you like. You can find out how to do this [here]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![The text column](images/text-column-new.png)

The **first column** of a table has several [peculiarities]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}), as you can read in the linked article.

## Using the text column

The text column is particularly suitable for collecting and [sorting]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) short alphanumeric strings, for example **terms**, **names**, **passwords**, **license plates** or **IBANs**.

![Application example of the regular text column](images/regular-text-example.png)

{{< warning  headline="UTF-8"  text="SeaTable supports all characters according to the UTF-8 standard, since UTF-8 is the most widely used character encoding for the internet worldwide." />}}

When using the column, it makes sense to keep the entries as **short** as possible, since only a **limited number of characters** can be displayed without having to increase the column width.

![Entries that are too long cannot be displayed in their entirety in a text column without increasing the column width](images/use-short-entries.png)

## Other text-based column types

Please note that **no formatting options** are available for entries in the text column. If you want to capture structured texts with line breaks, lists, images, etc., you should use the [Formatted Text]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) column.

There are three other text-based column types in SeaTable for special use cases:
- the [email column]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}})
- the [URL column]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})
- the [phone number column]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

{{< warning  headline="Note" >}}
There are numerous text functions for [formula columns]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}), which behave like text columns when the results are **strings**.
{{< /warning >}}

## Set default value

You can define a preset [default value]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) for each text column. This is automatically entered in every new row of the table.

If you set the **{creator.name}** or **{creator.id}** reference as the default value, the **name** or **ID of the user** who added the row is automatically entered.

![Referencing the user name with a default value](images/Set-creator-name-as-default-value.png)

## Validate inputs

When using text columns in your tables, you have the option to validate inputs. Using validation that supports regular expressions, you can validate **cell values** and highlight cells with content that deviates from the valid format.

You can set up the format check as early as when creating a text column by activating the slider.

![Activation of the validation of the input of text columns](images/activate-validation-1.png)

If you want to validate the entries in an already created text column, first click on the **triangle icon** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} of the corresponding column and select **Customize Column Type** from the drop-down menu.

1. Activate the **Validate input** slider
2. Define a **target format**.
![Definition of the target format](images/define-specific-format-2.png)
3. Confirm with **Submit**.

### Consequence of validation

After successful validation, the **cells** with **content different** from the target format will be highlighted in red.

![Cells highlighted in red with content different from the target format](images/marked-entries-which-not-match-the-format.png)

### Regular expressions

SeaTable supports **regular expressions** for validating your entries in text columns. You can find some examples in the following table:

| Regular expression              | Function                                                                 |
| ------------------------------- | ------------------------------------------------------------------------ |
| \[123456\]                      | Check whether an input corresponds to a school grade from 1 to 6.        |
| \[1-9\]\[0-9\]?\[0-9\]?\[a-z\]? | Check format of a German house number (3 digits + 1 letter)              |
| \[0-9\]{5}                      | Checking the format of German postal codes (5x a number between 0 and 9) |
| \[0-9/. \\-\]+                  | Checking the format of a phone number                                    |
| Max.\*Mustermann                | Search for a possible middle name of an author                           |

{{< warning  headline="Tip"  text="A detailed **tutorial** for using regular expressions to check strings can be found [here (German)](https://danielfett.de/2006/03/20/regulaere-ausdruecke-tutorial/) and [here (English)](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)." />}}
