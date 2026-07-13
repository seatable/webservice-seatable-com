---
title: 'Step 2: Import and link the lines'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-2-import-and-link-lines'
aliases:
    - '/help/schritt-2-zeilen-verknuepfen'
seo:
    title: 'Step 2 in SeaTable Course 4: link lines automatically'
    description: 'Import the lines of a delivery from a spreadsheet and build your first automation: link each line to its product and its document by comparing references.'
---

A new delivery arrives at the warehouse. Its header is already in the `Documents` table, but the detail — which products, in what quantities — still has to be entered. In this step you import those lines, then build your first automation: the one that links them, all on its own, to the right product and the right document.

## Preparing the automation that links

Let's start with the automation, before we even have the data: that way, the moment the lines arrive, they will link themselves.

A SeaTable automation always follows the same pattern: a **trigger** — the event that sets it off — followed by one or more **actions**. Here, the trigger is a new line arriving in `Line items`, and the action will attach it to its product record.

The action to choose is called *link by comparison*. Rather than picking a record by hand, it searches another table for the one whose column matches a value from the line. This is how you link the `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Product` column by comparing the line's `Product ref` to the products' `Reference`; then, in the same way, you link the `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Document` column by comparing its `Document reference` to the documents' `Identifier`.

![The configuration of the "link by comparison" action, matching the line's Product ref to the products' Reference](images/lvl4-link-by-comparison.png)

{{< warning headline="An action to keep in your back pocket" text="Link by comparison saves you from choosing the linked record one by one: the automation finds it thanks to a shared value. This is exactly what you need when data arrives from the outside — an import, a form, or artificial intelligence later in this course — with no link already established, but with a shared reference." />}}

## Importing the delivery lines

The supplier sent you the detail of the delivery as a spreadsheet — a very common case. Rather than retyping everything, import that file straight into the `Line items` table: SeaTable creates one line per entry in the file and matches its columns to yours.

<!-- TODO: provide the sample CSV/XLSX file and drop it at this path -->
[SeaTable Course 4 - Delivery lines.csv](/SeaTable-Course-4-Delivery-lines.csv)

The instant each line is created, your automation fires: the `Product` and `Document` columns, absent from the file, fill themselves in. Your lines are now attached to the catalog and to their delivery, without a single link entered by hand. This is a good moment to have your work checked by the plugin — it verifies that each imported line has indeed found its product.

One note for later: here, you imported these lines yourself from a nicely organized spreadsheet. But a delivery note, to begin with, is a PDF document, not a ready-to-use file. How do you get from one to the other? You'll find out a little further along in the course.

## Try it yourself

Open a freshly imported line and follow its `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Product` link to the catalog: the same reference, now a real connection. This is precisely the link you will use in the next step to update the stock — without it, SeaTable would not know which product to credit.

## Help article with further information

- [Import data into SeaTable]({{< relref "help/startseite/import-von-daten/" >}})
- [Create and configure an automation]({{< relref "help/base-editor/automationen/" >}})
- [The link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte/" >}})
