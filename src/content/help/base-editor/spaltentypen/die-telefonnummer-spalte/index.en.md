---
title: 'The phone number column'
date: 2025-12-17
lastmod: '2025-12-17'
categories:
    - 'text-und-zahlen'
author: 'kgr'
url: '/help/the-phone-number-column'
seo:
    title: 'The phone number column type in SeaTable'
    description: 'Use this column type to validate telephone numbers and start calls with a mouse click.'
weight: 16
---

There is a separate column type in SeaTable for entering **phone numbers**. Compared to a normal text column, the phone number column offers the advantage that you can **call a phone number** with a mouse click.

## Create a phone number column

![Create phone number column](images/column-type-phone-number.gif)

1. Click on the **Plus symbol** to the right of the last column in the table header.
2. Give the column a **name**.
3. Select the **column type Phone number**.
4. Confirm with **Submit**.

### Set default value

You can define a preset [default value]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) for each phone number column. This is automatically entered in each new row of the table.

### Validate input

As with text columns, you have the option of validating entries in the telephone number column. By performing a **format check**, you can highlight telephone numbers that deviate from the valid format. You can also use [regular expressions]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}) for validation.

![Check the format of a telephone number](images/format-check-phone-number.png)

## Start calls

The phone number column type makes your daily communication even easier. A click on the **phone icon in a cell** transfers the phone number to your telephony application. On cell phones, this works without any further configuration. The same applies on the desktop if a shortcut to telephony software has been set up in the browser.

![Call phone number](images/call-phone-number.png)