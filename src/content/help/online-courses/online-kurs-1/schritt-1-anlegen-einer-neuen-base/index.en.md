---
title: 'Step 1: Creating a new base'
date: 2024-08-30
lastmod: '2024-09-04'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/help/step1-create-new-base-seatable'
aliases:
    - '/help/schritt-1-anlegen-einer-neuen-base'
seo:
    title: 'Step 1 in SeaTable Course 1: create your expenses base'
    description: 'Begin your online course: Set up a new SeaTable base, customize fields and categories, and build the perfect structure for personal expense tracking.'
---

In this course we will create a simple tool to record and manage your personal or professional expenses. When you're done, you'll be able to record expenses at any time, either on your computer or on your cell phone. Every time you pull out your wallet, you should then document this expense. The reward for this effort is that you can see at a glance what you have spent how much money on.

So let's start this online course by creating the necessary structure to be able to save these outputs. To do this, you will create an initial base and then some columns. You will see that the following steps are almost self-explanatory.

{{< warning  headline="A little tip for working efficiently with this online course"  text="I would like to recommend that you have two browser windows open on your monitor and place them next to each other. Open this article in one browser window and open your SeaTable in the other. This will make it much easier for you to follow the steps in this course without having to constantly switch windows." />}}

![](images/level1-browser-window-setup.png)

## Create new base

We start on the SeaTable start page. Create a new base with the name `Expense Tracking` button. Then click on this base to go to the base Editor.

## Change the name of the first table

By default, each base contains a table with the name `Table 1`which has a column with three rows .

- Delete the three rows
- Then change the name of the table to `Expenses`

{{< warning  headline="Help if you get stuck"  text="The operation of SeaTable should be intuitive in most cases. For example, you can delete rows in the same way as you are used to from many other software solutions: Select the rows and right-click. If you still need assistance, please refer to the help articles we have compiled for you at the bottom of the page. There you will find instructions for every step of this online course." />}}

## Customize the columns of the table and add new ones

Next, we turn to the columns of the table so that our base can record the desired data.

- Change the name of the first column from `Name` on `Reason`
- Now add three more columns

**Column 1:**

> Name: `Date`
>
> Column type: `{{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} Date`
>
> Format: any
>
> To the minute: `Yes`

**Note:** Instead of the column type `{{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} Date` the column type `{{< seatable-icon icon="dtable-icon-creation-time" >}} Created time` can be used. While you have to fill in the date column manually, this would be filled in automatically with the current date. This of course saves time. However, the disadvantage would be that you would no longer be able to change the date value and, for example, could no longer retroactively enter expenses for other days.

---

**Column 2:**

> Name: `Amount`
>
> Column type: `{{< seatable-icon icon="dtable-icon-number" >}} Number`
>
> Format: `Euro`

---

**Column 3:**

> Name: `Category`
>
> Column type: `{{< seatable-icon icon="dtable-icon-single-election" >}} Single select`

---

{{< warning  headline="26 column types"  text="So far you have only seen a fraction of the possible column types. One of SeaTable's greatest strengths is that you can really store any type of information thanks to the 26 column types currently available." />}}

## Add single selection options

Your single selection currently has no selection options. Therefore, next create a new selection for the `Category` the following four options:

- Clothing
- Groceries
- Leisure
- Travel

## Short quality check

Fantastic. If you have followed the instructions exactly, your base should now look like this:

![](images/level1-expenses-table.png)

Let's briefly recap what you have just created with just a few mouse clicks: **You now have a base in which you can record all your future expenses.**

At the same time, by selecting the column types, you have ensured that only the appropriate information can be entered in the columns.

That was step 1 of this online course. Scroll to the end of this article and jump to **Step 2: Creating a form**.

## Help article with further information

- [Create a new base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [How to customize the column type]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}})
- [Delete a row]({{< relref "help/base-editor/zeilen/das-loeschen-von-zeilen" >}})
- [Adding a column]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}})
- [Adding options to a single-selection column]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
- [Special features of the first column]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}})
- [Customize the appearance of a base (icon and color)]({{< relref "help/startseite/bases/aussehen-einer-base-anpassen-icon-und-farbe" >}})
