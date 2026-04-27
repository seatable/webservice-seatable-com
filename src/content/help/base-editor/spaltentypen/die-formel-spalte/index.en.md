---
title: 'The formula column'
date: 2023-01-28
lastmod: '2023-09-14'
categories:
    - 'formeln'
author: 'ssc'
url: '/help/formula-column-seatable'
aliases: 
    - '/help/grundlagen-von-seatable-formeln'
    - '/help/die-formel-spalte'
seo:
    title: 'Make the most of the formula column in SeaTable'
    description: 'Use formula columns to calculate, merge or manipulate row values flexibly in SeaTable – simple for math and string ops.'

---

SeaTable offers you many different functions that you can add to your table. One of them is the so-called **formula column**. Using formulas you can link values from different columns and create different functions based on the data types of these columns. Among other things, you can calculate with values in a row , merge them or relate them to each other.

{{< warning  headline="SeaTable does not allow free referencing as in Excel"  text="In Excel you can address any cell in a formula. In SeaTable this is **not** possible. A formula can only work with the **values from the same row**." />}}

## Create a formula column

To apply a formula, you must first add a new formula column to your table. You can learn how to do that [here]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![Selection of a formula column](images/select-formula-column.png)

SeaTable provides you with a **formula editor** to help you enter formulas.

![Formula wizard to simplify the input of especially complex formulas](images/Formula.wizard.png)

## Write a first formula

Once your formula column is created, you can start writing the formula. The following figure shows a simple formula to calculate the average of five numbers.

![Entering any formula in the text field](images/input-formular.jpg)

This formula always writes the static value _13.2_ into the formula column as the result. However, the true power of the formula column only comes into its own when you use the values of other columns for your formula. With the **{column name}** in curly brackets you can reference existing columns in your table.

{{< warning headline="Add columns to the formula" text="The column names in the opened table are displayed on the left side of the formula editor and can be edited with a **Double click** must be inserted into the formula." />}}

![Columns available for selection in the formula editor](images/columns-in-the-formula-editor.jpg)

Then you can insert certain **constants**, **operands** and **functions** into your formula to calculate with, merge or relate the values of the different columns.

## Clear color language

To be able to distinguish the different elements of your formula from each other, they are marked in a different **color** depending on their type:

| Object            | Example                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| Functions         | ![Functions are always marked blue in a formula](images/example-function.png)                       |
| Text / String     | ![Texts and strings are always marked in red in the formula editor](images/example-text.png)        |
| Numbers           | ![Numbers are always highlighted in green in the formula editor](images/example-number.png)         |
| Column references | ![Column references are always marked purple in a formula ](images/example-reference-to-column.png) |

{{< warning headline="Brackets that belong together are highlighted" text="When you click an opening or closing parenthesis in the formula editor, the associated parenthesis is also highlighted. This makes it easier to spot missing or incorrect bracket replacements." />}}

![Opening and closing parentheses are always highlighted in the formula editor](images/example-brackets.png)

## Formula examples

Below are a few examples that illustrate the utility and use of formulas.

- [Formula example: Simple multiplication with a formula]({{< relref "help/base-editor/formeln/formelbeispiel-einfache-multiplikation-mit-einer-formel" >}})
- [Formula example: Merging text columns using a formula]({{< relref "help/base-editor/formeln/formelbeispiel-zusammenfuehren-von-text-spalten-mit-hilfe-einer-formel" >}})
- [Formula example: Logical if operators for comparing values]({{< relref "help/base-editor/formeln/formelbeispiel-logische-if-operatoren-zum-vergleichen-von-werten" >}})
- [Formula example: Calculate the duration of a vacation]({{< relref "help/base-editor/formeln/formelbeispiel-berechne-die-dauer-eines-urlaubs" >}})
- [Formula example: Calculate days until an event]({{< relref "help/base-editor/formeln/formelbeispiel-berechne-tage-bis-zu-einem-event" >}})
- [Formula example: Search for a word in a text]({{< relref "help/base-editor/formeln/formelbeispiel-nach-einem-wort-in-einem-text-suchen" >}})

## Mathematical conventions also apply in SeaTable

Of course you can rely on the fact that mathematical conventions also find their application in the formulas of SeaTable. Here are the most important examples:

- You can **nest functions** within each other using parentheses. Example: (( 1 + 2 ) \* 3)
- **Dot before dash**, the **order of parentheses** and other **mathematical rules** are taken into account in SeaTable.

## Formula column formatting

You can format the results in the formula column. Each formula in SeaTable has a **number**, a **date** or a **text/string** as result. Therefore, depending on this, you have different **format settings** available.

![Formatting formula results](images/Formatierung-von-Formelergebnissen.jpg)
