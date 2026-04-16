---
title: 'The Lookup Formula'
date: 2022-10-13
lastmod: '2023-04-06'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/help/lookup-column-seatable'
aliases:
    - '/help/die-lookup-funktion'
seo:
    title: 'Lookup column: show values from linked tables in SeaTable'
    description: 'SeaTable’s lookup lets you display data from linked tables, eliminate double entry and connect project info quickly and accurately.'

---

The Lookup function allows you to display additional values from an already linked table in your current table. This prevents you from having to enter the data twice and allows you to relate the data at the same time. In Excel this function is known as _VLOOKUP_ or _SVERWEIS_.

## When do you need the lookup formula?

The Lookup function should be used whenever you want to cross-reference information stored in different tables. Let's say you are using SeaTable for [project management]({{< relref "pages/landing-pages/industry-solutions/project-management" >}}), where the projects are stored in one table and the tasks associated with the project are stored in another table. Each project is then linked to a set of tasks.

![Linking project tasks to a project](images/linked-tables-seatable.png)

As a project manager, you may want to view information about the tasks associated with each project. The Lookup formula can be used to select a column in the linked table and display its values. For example, you can automatically display the project team members who are responsible for each task.

![Lookup Column](images/lookup-columns.png)

This can be useful for easy access to cross-table information, setting up automations, formulas, etc. Below you will learn more about using the Lookup function.

## To use the Lookup column

### Add a table link

The lookup function can only be used if a column of the type _Link to other entries_ already exists. If you don't have such a column yet, create one first. You can find out how this works [here]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}).

### Add a lookup formula

At first, the Lookup formula may confuse you. But you'll see that before long you'll love this incredibly versatile and powerful column feature. Here's how to add a column with the Lookup formula:

![Set up a lookup column](images/setup-of-lookup-column.gif)

1. Create a new column of the type **Formula for links**.
2. Set the **Lookup** option as the formula.
3. Select a **link column**. This field is automatically filled in correctly if you have only one link column.
4. With the **lookup column in the linked table** you define from which column of the other table the values should be taken.
5. Click **Submit**.

## Frequently asked questions about the Lookup column

{{< faq "Is it possible to get multiple values into one table via lookup?" >}}Definitely. Just create another column and use the lookup function again. This way you can read and display as much information as you want from the linked table.
{{< /faq >}}
{{< faq "Can lookups be changed afterwards?" >}}Of course, this is possible. Click the **triangle icon to** the right of the column name and then click **Customize Column Type**. Adjust the settings of the column and immediately the desired information will be displayed.
{{< /faq >}}
{{< faq "Do lookups work with multiple links?" >}}Each lookup formula can only fetch the information from **one** column of your linked tables. But of course you can link multiple tables via link columns and create more lookup columns to read and display even more information.
{{< /faq >}}
{{< faq "Can entries looked up by lookup be filtered?" >}}Yes, you can filter the entries as you wish. To do this, activate the corresponding **Controller** in the _Column settings_ and select the **Column(s)** whose entries are to be looked up. You can select any number of **Filter conditions** define.

{{< /faq >}}
