---
title: 'Overview of all column types'
date: 2022-08-25
lastmod: '2024-03-18'
categories:
    - 'arbeiten-mit-spalten'
author: 'cdb'
url: '/help/overview-all-column-types'
aliases:
    - '/help/uebersicht-alle-spaltentypen'
seo:
    title: 'Overview of All Column Types in SeaTable – Functions Explained'
    description: 'Discover all 26 column types in SeaTable: text, number, file, selection fields, formulas, relations and more. Key features and best use cases included.'
star: true
weight: 1
---

In SeaTable you can store information and data in a wide variety of formats.

- In addition to simple, text-based information (e.g. words, numbers, monetary amounts), SeaTable also supports the storage of complex information (e.g. files, images, long text including inserted elements).
- Select fields allow you to divide your data into defined categories, and integrated validation functions (e.g. URL, position data) ensure that your entries are in a consistent, directly analyzable format.
- With formulas you can perform arithmetic operations and with links you create relations between records of different tables that allow powerful database operations.

Get to know SeaTables 26 different column types here!

## Columns types with manual data entry

Each table column is assigned a type. The column type determines what data you can enter in the cells of the column. For example, you cannot insert files into a text field. The date column, on the other hand, forces you to enter a date in the selected format.

### Text

Icon: {{< seatable-icon icon="dtable-icon-single-line-text" >}} **Text**

This column type stores **text** without formatting and is one of the most basic column types in SeaTable. Text contents consist of **letters**, **numbers** and **special characters** as well as **spaces**. That's why text columns are often used for names and (short) descriptions.

[More about the text column]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})

### Long text

Icon: {{< seatable-icon icon="dtable-icon-long-text" >}} **Long text**

In this column type you can save **longer texts** with inserted elements such as **images** and **tables**. You also have various formatting and structuring options for your texts using the Markdown markup language. Therefore, the _Long Text_ column is often used for descriptions and documentation. If it is helpful for information gathering that texts contain structuring elements and/or text and images are close to each other, then this column type is ideal.

[More about the Long Text column]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})

### Number

Icon: {{< seatable-icon icon="dtable-icon-number" >}} **Number**

Number columns store **numeric information** and can be used in many ways to work with numbers of any kind. A numeric information can be a **number**, a **percentage** or a **monetary amount**. Furthermore, number columns allow you to **calculate values** that you can visualize with formulas and [statistics]({{< relref "help/base-editor/statistiken" >}}). However, number columns are not suitable for storing strings of any length, and SeaTable refuses to allow you to enter letters in this type of column.

[More about the numbers column]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})

### Date

Icon: {{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} **Date**

You can use the date column to enter **times** and **dates** in your tables down to the minute. Note that date columns always interpret the information entered as a date, so entries that cannot be interpreted as dates are always discarded as invalid.

[More about the date column]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})

### Duration

Icon: {{< seatable-icon icon="dtable-icon-duration" >}} **Duration**

The duration column is a specialized number column type for storing **time measurements, spans and intervals,** and can thereby record a period of time to the minute or even to the second. For this reason, the column is particularly suitable for recording the duration of various events, among other things. When using the column, however, note that non-numeric entries are always discarded as invalid.

[More about the duration column]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})

### Single select

Icon: {{< seatable-icon icon="dtable-icon-single-election" >}} **Single select**

In a cell of a single-select column you can select a **value** from a list of defined options. You create the list of defined options per single select column yourself and can adapt it to changing circumstances at any time. The single select is thus particularly suitable for categorizing and grouping your data.

[More about the single select column]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})

### Multiple select

Icon: {{< seatable-icon icon="dtable-icon-multiple-selection" >}} **Multiple select**

With a multiple select, you can choose **any number of values** from a list of defined options. As with the single select, you create the list of possible values yourself and adapt it to your individual requirements. The multiple select is therefore ideal for keywording - also called tagging.

[More about the multiple select column]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}})

### Image

Icon: {{< seatable-icon icon="dtable-icon-picture" >}} **Image**

The Image column type stores any number of **image files** in **BMP**, **GIF**, **ICO**, **JPG**, **PNG**, **SVG** and **TIF** file formats. The Image column is thus a file column restricted to image file formats.

[More about the image column]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}})

### File

Icon: {{< seatable-icon icon="dtable-icon-file" >}} **File**

The File column type stores any number of files of **any file type**. For numerous image file formats SeaTable offers a preview function.

[More about the file column]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}})

### E-mail

Icon: {{< seatable-icon icon="dtable-icon-email" >}} **E-mail**

Email columns are specialized text columns for capturing and storing **email addresses** and allow direct use with a mouse click. The email column is especially handy for web forms. Using an email field in place of a text column ensures that the input has the syntax of a valid email address. In addition, email columns can be used to send emails via [buttons]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) and [automations]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}).

If you need more detailed information about the email column, take a look at this [article]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}).

### URL

Icon: {{< seatable-icon icon="dtable-icon-url" >}} **URL**

URL columns interpret the entered information as a **resource** in the local network or on the Internet and allow it to be called up directly by clicking. Since entries in this column type are not validated, an Internet address (e.g. https://seatable.com) or an IP address (e.g. 192.168.178.1) can be stored in a cell.

[More about the URL column]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})

### Checkbox

Icon: {{< seatable-icon icon="dtable-icon-check-square-solid" >}} **Checkbox**

Checkboxes allow the collection of **binary information**: Yes or No or _Checked_ vs. _Unchecked_. Further entries are not possible. Therefore, they are good for marking tasks as done, for example - that is, for keeping track of whether rows meets a certain yes/no condition. For this reason, you can also make excellent use of checkbox columns for [filtering]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}), [sorting]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) or [grouping]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}).

[More about the checkbox column]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}})

### Rating

Icon: {{< seatable-icon icon="dtable-icon-rate" >}} **Rating**

A rating column allows you to **classify** your records in order to **rank** them or give them a **quality score**. You can select a rating scale from 1 to 10 and choose between different colors and shapes. This allows data to be assessed and rated quickly and easily for everyone to understand.

[More about the rating column]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})

### Phone number

Icon: {{< seatable-icon icon="dtable-icon-telephone" >}} **Phone number**

SeaTable has its own column type for phone numbers. Compared to a regular text column, the phone number column offers the advantage that you can **call a phone number** with a mouse click.

[More about the phone number column]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

### Formula

Icon: {{< seatable-icon icon="dtable-icon-formula" >}} **Formula**

Using formulas you can**link** different column values of a row and create different **functions** based on the content of these columns. Among other things, you can calculate with values in your tables, change values or relate values from the same row.

You need more info about the formula column? Then take a look at this [article]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}). Since formulas are a very complex feature, you can find numerous other help articles in our manual. Click [here]({{< relref "help/base-editor/formeln" >}}) and you will be redirected to the overview page.

### Link to other records

Icon: {{< seatable-icon icon="dtable-icon-link-other-record" >}} **Link to other records**

In cells of this column type you can enter any number of **references to records in other tables** of the base. The link column is intended for mapping relations between records of different tables. The link column can be used to map 1:n and n:1 relations as well as n:m relations.

More information about the column type Link to other records can be found [here.]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})

### Link formula

Icon: {{< seatable-icon icon="dtable-icon-link-formulas" >}} **Link formula**

With the Link formula you can **display** data from **linked tables** in your current table and **relate** them to each other. A total of five different formulas are subsequently available for the column type, which you can also use to perform statistical calculations. The prerequisite for using the column is the existence of at least one column of the type **Link to other records** in your table.

[More about the link formula column]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}})

### Collaborator

Icon: {{< seatable-icon icon="dtable-icon-collaborator" >}} **Collaborator**

In a collaborator column you can record any number of **users** who have at least read access to the base. SeaTable users without access cannot be entered in the column as collaborators. Other entries are also not allowed. The collaborator column is especially useful for project management. For example, if you enter tasks to be completed in a table, you can record the persons performing the tasks and the responsibles in columns of the Collaborator type.

[More about the collaborator column]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}})

### Button

Icon: {{< seatable-icon icon="dtable-icon-button" >}} **Button**

Buttons allow you to **automate** the processing of data or the execution of certain actions. However, keep in mind that you always have to operate buttons **manually**. Using the button that you can add to your rows in this column, you trigger certain actions defined in advance. For this reason, this column type is particularly suitable for automating process steps.

For more information about the button and the actions that can be triggered in columns of this type, see this [article]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}).

### Geolocation

Icon: {{< seatable-icon icon="dtable-icon-location" >}} **Geolocation**

In this column you can record **locations** and visualize them later with the [map plugin]({{< relref "help/base-editor/plugins/anleitung-zum-karten-plugin" >}}). For this you can either select the entry with country and region or with latitude and longitude. Additionally, you have the possibility to find a country or region using the search function and add it as an entry.

[More about the geolocation column]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}})

### Digital signature

Icon: {{< seatable-icon icon="dtable-icon-rename" >}} **Digital signature**

You can store **digital signatures** in a signature column, which are automatically saved in the file management of your base. Digital signatures are very well suited for data capture using **web forms**, for example to have applications conveniently signed online.

[More about the signature column]({{< relref "help/base-editor/spaltentypen/die-signatur-spalte" >}})

## Column types with automatic data capture

In addition to the column types in which you as a user enter data, SeaTable has five other column types whose contents SeaTable generates automatically. These columns cannot be edited manually by users. They are primarily used for documentation purposes.

### Creator

Icon: {{< seatable-icon icon="dtable-icon-creator" >}} **Creator**

SeaTable automatically documents the **name of the user** who created the row in the creator column.

[More about the creator column]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})

### Created time

Icon: {{< seatable-icon icon="dtable-icon-creation-time" >}} **Created time**

SeaTable automatically documents the **date and time of creation of the row** in the Created time column. The date and time are displayed in the format YYYY-MM-DD HH:MM.

[More about the Created time column]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})

### Last modifier

Icon: {{< seatable-icon icon="dtable-icon-creator" >}} **Last modifier**

SeaTable automatically documents the **name of the user** who made the **last change to** an entry in the Last modifier column. Since the column automatically records changes to records, it is well suited, for example, as a trigger for automations as well as for filters and sorts.

[More about the Last modifier column]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})

### Last modified time

Icon: {{< seatable-icon icon="dtable-icon-creation-time" >}} **Last modified time**

SeaTable documents the **date and time of the last modification of an entry** in the Last modified time column. Date and time are displayed in the format YYYY-MM-DD HH:MM. Since the column automatically records changes to records, it is well suited as a trigger for automations as well as for filters and sorts.

[More about the Last modified time column]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})

### Automatic number

Icon: {{< seatable-icon icon="dtable-icon-autonumber" >}} **Auto number**

The Auto number column type generates an **automatically increasing number** for each new row. This column type is used whenever you need a unique identifier for each record.

[More about the Auto number column]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}}).
