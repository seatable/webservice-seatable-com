---
title: 'Validation of input for text fields with regular expressions'
date: 2023-05-03
lastmod: '2024-03-11'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/help/validate-textfield-regex-seatable'
aliases:
    - '/help/validierung-der-eingabe-bei-textfeldern'
seo:
    title: 'Validate text fields in SeaTable using regular expressions'
    description: 'Use regular expressions to check and highlight values in SeaTable text fields. Automatically detect and prevent incorrect formats for high data quality.'

---

When using text columns in your tables, you have the option to validate inputs. Using validation that supports regular expressions, you can validate cell values and highlight cells with content that deviates from the valid format.

{{< warning  headline="Note" >}}

Basically, there are two different ways to validate entries in text columns. Validation can be performed both when **adding a new** [text column]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) that have **already been created**.

{{< /warning >}}

## Validate inputs

![Activation of the validation of the input of text columns](images/activate-validation-1.png)

1. If you want to validate the entries in an already created text column, first click on the **triangle icon** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} of the corresponding column.
2. Select **Customize Column Type** from the drop-down menu.
3. Activate the **Validate input** slider
4. Define a **target format**.
5. Confirm with **Submit**.

![Definition of the target format](images/define-specific-format-2.png)

## Consequence of validation

After successful validation, the **cells** with **content different** from the target format will be highlighted in red.

![Cells highlighted in red with content different from the target format](images/marked-entries-which-not-match-the-format.png)

## Regular expressions

SeaTable supports **regular expressions** for validating your entries in text columns.  
You can find some examples in the following table:

| Regular expression              | Function                                                                 |
| ------------------------------- | ------------------------------------------------------------------------ |
| \[123456\]                      | Check whether an input corresponds to a school grade from 1 to 6.        |
| \[1-9\]\[0-9\]?\[0-9\]?\[a-z\]? | Check format of a German house number (3 digits + 1 letter)              |
| \[0-9\]{5}                      | Checking the format of German postal codes (5x a number between 0 and 9) |
| \[0-9/. \\-\]+                  | Checking the format of a phone number                                    |
| Max.\*Mustermann                | Search for a possible middle name of an author                           |

{{< warning  headline="Tip"  text="A detailed **tutorial** for using regular expressions to check strings can be found [here (German)](https://danielfett.de/2006/03/20/regulaere-ausdruecke-tutorial/) and [here (English](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285))." />}}
