---
title: 'Typical mistakes when working with formulas'
date: 2023-05-03
lastmod: '2023-05-03'
categories:
    - 'formeln'
author: 'nsc2'
url: '/help/formula-errors-seatable'
aliases:
    - '/help/typische-fehler-beim-arbeiten-mit-formeln'
seo:
    title: 'Common formula errors in SeaTable: avoid pitfalls'
    description: 'Identify and fix common errors in SeaTable formulas: correctly place quotation marks, brackets, commas and column references.'

---

The [formula column]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) opens up many possibilities for working with your data. For example, you can use formulas to relate values from different columns to each other and perform calculations with them. However, since working with more complex formulas can be difficult, especially at the beginning, this article provides you with **solutions to the most common problems**.

## Quotation marks around text elements are missing

Each text element in your formulas **must** be enclosed in quotation marks in order to be recognized by the formula editor. If a text is **not** enclosed in quotation marks, the following **error message** may appear:

![Error message that appears when quotation marks are missing around text elements](images/Fehlermeldung-fehlende-Anfuehrungszeichen-bei-Textelementen.png)

#### Incorrect input:

![Incorrect input of text elements](images/fehlerhafte-eingabe-anfuehrungszeichen.png)

#### Correct input:

![Correct input of text elements](images/richtige-eingabe-anfuehrungszeichen.png)

{{< warning  headline="Tip"  text="Text elements are always marked in **red** in a formula and can thus be distinguished from other elements. If a text element is **not** marked in **red** in the formula editor, this means that it was entered **incorrectly**." />}}

## Parentheses for functions are missing or set incorrectly

In the formula editor, **each function** must first be followed by an **opening parenthesis** before you add further elements. Once you have added all elements of a function to the formula, it must also end with a **closing parenthesis**. If **no** parentheses are set, the formula editor **cannot** recognize the function and the following error messages may appear:

![Error message that appears if no opening parenthesis is set after a function](images/Fehlermeldung-bei-fehlender-Klammer-nach-einer-Funktion.png)

![Error message that appears when the parentheses are set incorrectly for a function](images/fehlermeldung-klammern-bei-funktion-falsch-gesetzt.png)

#### Incorrect input:

![Incorrect input of a function](images/fehlerhafte-eingabe-funktion-1.png)

#### Correct input:

![Correct input of a function](images/korrekte-eingabe-funktion-1.png)

{{< warning  headline="Tip"  text="Functions are always marked in **blue** in a formula. If you click an opening or closing parenthesis in the formula editor, **the matching parenthesis is highlighted**. This makes it easier to spot missing or incorrect parentheses when entering functions." />}}

## Incorrect use of brackets in general

Setting brackets correctly is one of the biggest challenges when entering formulas. Whether **parentheses or curly brackets** – they must always be set in the **right place** in a formula so that it is recognized by the formula editor.

### Parentheses

How to set parentheses correctly when entering functions is explained in the **previous section** of this article.

### Curly brackets

You use curly brackets when you want to refer to specific **table columns**. The **name** of the desired column must always be surrounded by **two curly brackets**. If **no** brackets or **incorrect** brackets are set, the formula editor **cannot** recognize the column reference and the following error messages may appear:

![Error message that appears if no curly brackets are set when referring to column names](images/fehlermeldung-keine-geschweiften-klammern.png)

![Error message that appears when curly brackets are set incorrectly when referring to column names](images/fehlermeldung-geschweifte-klammern-falsch-gesetzt-1.png)

#### Incorrect input:

![Incorrect input of curly brackets when referring to column names](images/fehlerhafte-eingabe-geschweifte-klammern-1.png)

#### Correct input:

![Correct input of curly brackets when referring to column names](images/korrekte-eingabe.geschweifte-klammern.png)

### Column references within functions

If you want to refer to column names within a function, you must pay special attention to setting the brackets correctly. Observe the individual rules for brackets in functions and column references. If you are unsure whether a pair of brackets is complete, remember that the second bracket is always highlighted when you click a bracket in the formula editor.

#### Incorrect input:

![Incorrect input of a function with a column reference](images/fehlerhafte-eingabe-einer-funktion-mit-spaltenverweis.png)

#### Correct input:

![Correct input of a function with a column reference](images/korrekte-eingabe-einer-funktion-mit-spaltenverweis.png)

## Chaining multiple functions

If you want to include **multiple functions** in your formula, you must make sure to always separate the individual functions with a **comma**.

In addition, you must end formulas that contain multiple functions with **multiple closing parentheses**. For example, if your formula contains three functions, it must also end with three closing parentheses in the formula editor.

If these points are **not** observed, the formula editor **cannot** recognize the entered formula and the following error messages may appear:

![Error message that appears when a formula containing multiple functions does not end with the required number of closing parentheses](images/fehlermeldung-zu-weinge-klammern-am-ende-der-formel.png)

![Error message that appears if commas between the different functions of a formula are missing or set incorrectly](images/fehlermeldung-falsche-kommasetzung.png)

#### Incorrect input:

![Incorrect input of a formula in which multiple functions were chained](images/fehlerhafte-eingabe-einer-formel-mit-mehreren-funktionen.png)

#### Correct input:

![Correct input of a formula in which multiple functions were chained](images/korrekte-eingabe-formel-mit-mehreren-funktionen.png)

{{< warning  headline="Tip"  text="For more complex formulas, always work with **spaces and line breaks** so that you can view the individual functions of your formula separately and spot errors more easily." />}}

## Concatenating multiple text elements in a formula

To concatenate multiple text elements in your formula, you must separate the individual text elements from each other with an **& symbol**. If **no & symbols** are added between the text elements, the formula editor **cannot** recognize the entered formula and the following error message appears:

![Error message that appears when multiple text elements in a formula are not separated by &.](images/Fehlermeldung-bei-fehlendenen-zwischen-Textelementen.png)

#### Incorrect input:

![Incorrect input of multiple text elements in a formula](images/fehlerhafte-Eingabe-mehrere-Textelemente.png)

#### Correct input:

![Correct input of multiple text elements in a formula](images/korrekte-Eingabe-mehrere-Textelemente.png)

{{< warning headline="Tip" text="To separate the various text elements with a space, insert **two & symbols** and **two quotation marks (at the top)** between each of the text elements." />}}

![Editing the formula so that the text elements are each separated by a space](images/Leerzeichen-zwischen-Textelementen.png)
