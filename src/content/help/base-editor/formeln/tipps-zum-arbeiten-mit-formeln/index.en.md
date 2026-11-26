---
title: 'Tips for working with formulas'
date: 2023-05-03
lastmod: '2023-09-21'
categories:
    - 'formeln'
author: 'nsc2'
url: '/help/formula-tips-working-seatable'
aliases:
    - '/help/tipps-zum-arbeiten-mit-formeln'
seo:
    title: 'Formula Tips for Working in SeaTable'
    description: 'Helpful SeaTable formula tips: line breaks, syntax, color highlights, bracket matching, planning formulas, and avoiding errors.'

---

Here you will find help and tips to facilitate your work with Seatable formulas. A list of all available formulas can be found [here]({{< relref "help/base-editor/formeln/formelreferenz" >}}).

## Use spaces and line breaks

Don't be afraid to use **spaces** and **line breaks** when creating formulas. These help you keep an overview of the individual functions and other elements, especially in more complex formulas.

You can set spaces and line breaks almost arbitrarily in the **formula editor**. Caution is only required when using **functions**. Directly **after** a function, for example _lower()_, **no** space must be set.

### Application example

![Spaces and line breaks can be set almost arbitrarily in the formula wizard. The only exception are functions.](images/benutzen-Sie-leerzeichen-und-spaltenumbrueche.png)

## Using syntax in the formula editor

When you click on an **element** in the formula editor that you want to add to your formula, helpful information is displayed. Directly under the name of the selected element, in addition to a brief description of how it **works**, you'll also see a possible **syntax** and a concrete **example** of how it might look in a formula. When writing more complex formulas, this **information** can be useful to avoid mistakes or uncertainties.

![Information about an element in the formula wizard](images/Informationen-zu-einem-Element.png)

## Note the color scheme of the various formula elements

To be able to distinguish the different elements of your formula from each other, they are marked in a different **color** depending on their type. You can find out which elements are displayed in which color [here]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}#klare-farbsprache-zur-orientierung).

Use the different **colors** as a guide to get a better overview of your formula. In addition, the color highlighting of the formula elements can also act as a kind of **self-check** in two cases:

- **Text elements** are not marked in **red** in your formula until they are enclosed in **quotation marks**.
- **References to columns** are not marked in **purple** in your formula until they are surrounded by **curly braces**.

If the mentioned formula elements are **not** marked in the corresponding **color** in your formula, you have entered them **incorrectly**. To correct this, use the syntax.

## Note the highlighting of matching parentheses

**Matching parentheses** are **highlighted** in the formula editor as soon as you click an opening or closing parenthesis. This makes it easier to spot **missing** or **incorrect** parentheses.

![Opening and closing parentheses are always highlighted in the formula editor](images/example-brackets.png)

## Plan formulas

The logic and construction of a formula can sometimes be challenging. A helpful exercise here is to write down in simple language what specific goal you want to achieve.

For example, an optimal way to plan a formula might look like this:

1. First write down in your own words what **goal** you want to achieve with the formula (e.g. calculate remaining days until an event).
2. Search for a suitable **function** in the formula editor (e.g. dateDif).
3. Use the **syntax** of the function to check the correct spelling – e.g. dateDif(start date, end date, unit).
4. Write the **formula** in the provided text field in the formula editor. Use **line breaks** and **spaces** to make the logic of your formula more visible. Especially at the beginning, it can be helpful to write only parts of a formula and then gradually add more elements to it.
5. Pay attention to possible **error messages**. If any appear, first try to fix them on your own by checking the formula against the syntax. If you need further help, feel free to use our help article [Typical errors when working with formulas]({{< relref "help/base-editor/formeln/typische-fehler-beim-arbeiten-mit-formeln" >}}).
