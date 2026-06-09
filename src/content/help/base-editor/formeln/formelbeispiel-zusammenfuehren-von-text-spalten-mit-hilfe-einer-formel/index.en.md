---
title: 'Formula example: Merging text columns with the help of a formula'
date: 2023-01-28
lastmod: '2023-09-18'
categories:
    - 'formeln'
author: 'nsc2'
url: '/help/formula-example-merge-text-columns'
aliases:
    - '/help/formelbeispiel-zusammenfuehren-von-text-spalten-mit-hilfe-einer-formel'
seo:
    title: 'Formula example: merge text columns in SeaTable'
    description: 'See how to use SeaTable formulas to combine text from multiple columns into one field for full names or other strings.'
---

SeaTable formulas offer you several ways to work with the data in your tables. One of them is merging content from different [text columns]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}). Using an appropriate formula, you can merge any number of contents from different columns into one formula column.

## Merging text columns

In the concrete example, the goal is to use a formula to merge the contents (last name, first name, and title) of the first three columns into a **complete name**.

![Example table for merging different contents into one formula column](images/example-table-zusammenfuehren-von-inhalten-mit-Formel.png)

To do this, you first add a **formula column** to the table, in whose editor you can then insert the formula.

![Adding a formula in the text field provided for this purpose](images/insert-formular-example-1.png)

To merge content from different text columns into one column, you must always refer to the **names of the columns** where the corresponding content can be found in your table. It is especially important that the column names are framed with **curly brackets**, otherwise SeaTable **cannot** recognize which contents are to be merged.

{{< warning  headline="Tip"  text="The **column names** in the opened table are displayed on the left side of the **formula editor** and can be inserted into the formula with a **double-click**." />}}

![When you refer to column names in your tables, always surround them with curly braces](images/verweis-auf-spaltennamen-in-formel-beispiel-2.png)

To merge the contents of the text columns into a formula column, first arrange the column names in the desired **order** in the formula and separate each of them with an **& symbol**, which you will find in the formula editor near the **operands**.

![Arrange the different column names in the desired order in the formula and separate them with a & symbol](images/insert-symbols.png)

To separate the different contents by a **space**, add an **& symbol** and **two quotation marks (above)** **after the** first two column names.

![Adding an additional & symbol and two quotation marks after the first two column names](images/insert-and-22-22-to-the-formular.png)

After confirming the entered formula, the contents of the text columns are automatically merged and the **result** appears automatically in the formula column.

![Formula column after confirming the entered formula.](images/table-example-2-after-formular.png)

{{< warning  headline="Professional tip" >}}

Whenever you use text columns in a formula and these columns can also be empty, it is recommended to use the _trim( )_ function. This function removes blanks at the beginning and end of a text. The complete formula is then e.g.

```
trim( {Title} & " " & {Surname} & " " & {Name} )
```

{{< /warning >}}
