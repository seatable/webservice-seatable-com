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

A new delivery has just arrived at the warehouse. Its header is already in the `Documents` table, but the detail — which products, in what quantities — still has to be entered. In this step you import those lines and build your first automation: the one that links them, all on its own, to the right product and the right document.

## Building the automation that links

Your base does not ship with this automation — you are going to create it yourself, before importing the data, so that the moment the lines arrive they link themselves. It is your first automation of the course, so we lay it out one piece at a time — and the plugin comes along beside you, whether you want to be walked through each piece or simply have the finished result checked.

A SeaTable automation always follows the same pattern: a trigger — the event that sets it off — followed by one or more actions. For the one you need here, that comes down to:

> Trigger: New row in the `Line items` table
>
> First action: Add links between `Line items` and `Products` — by comparing `{{< seatable-icon icon="dtable-icon-single-line-text" >}}Product reference` (`Line items`) and `{{< seatable-icon icon="dtable-icon-single-line-text" >}}Reference` (`Products`)
>
> Second action: Add links between `Line items` and `Documents` — by comparing `{{< seatable-icon icon="dtable-icon-single-line-text" >}}Document reference` (`Line items`) and `{{< seatable-icon icon="dtable-icon-single-line-text" >}}Delivery reference` (`Documents`)

You build it in your base, with the plugin as your companion. In your base, open the **online-courses plugin** and select **Step 2**.

It starts by asking whether you would like a hand. Go it alone and it sends you straight to a check of your finished automation, matched against the summary above. Choose the guided path and it walks you through the stages below, one page at a time, confirming each before you move to the next — the very stages laid out here, so you can follow along on the course as well.

1. **Create the automation.** Open the `Automations editor` and add a new one. Name it and leave it there for a moment: the plugin confirms that a fresh automation now exists and remembers it for the checks that follow.

2. **Set the trigger — and guard it.** Choose `When a row is added`, so every line appearing in `Line items` — typed by hand or imported — sets the automation off. Then add two conditions, so it only runs on lines it can actually link: `Product reference` is not empty and `Document reference` is not empty. A line missing one of them would send the next actions searching for nothing; the conditions keep that from happening. The plugin checks the trigger and both conditions.

3. **Link the product.** Add a first action, `Add links`. Instead of you picking a record by hand, it searches another table for the one whose column matches a value from your line. Point it at the `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Product` column: the line's `Product reference` should equal a product's `Reference`. The plugin checks this first action.

4. **Link the document.** Add a second `Add links` action, built the same way, this time filling the `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Document` column: the line's `Document reference` should equal a document's `Delivery reference`. The plugin checks this last action — and your automation is complete.

{{< warning headline="An action to keep in your back pocket" text="Add links saves you from choosing the linked record one by one: the automation finds it thanks to a shared value. This is exactly what you need when data arrives from the outside — an import, a form, or artificial intelligence later in this course — with no link already established, but with a shared reference." />}}

## Try it yourself

Your automation is built — but nothing has set it off yet. Time to give it something to work on. Rather than retyping every line, import the detail of the delivery from a spreadsheet: drop this file straight into the `Line items` table, and SeaTable creates one line per entry, matching its columns to yours.

<!-- TODO: provide the sample CSV/XLSX file and drop it at this path -->
[SeaTable Course 4 - Delivery lines.csv](/SeaTable-Course-4-Delivery-lines.csv)

The instant each line is created, your automation fires: the `Product` and `Document` columns, absent from the file, fill themselves in — your lines are now attached to the catalog and to their delivery, without a single link entered by hand. Open one of the fresh lines and follow its `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Product` link to the catalog: the same reference, now a real connection your automation built. This is precisely the link you will use in the next step to update the stock — without it, SeaTable would not know which product to credit.

This is a good moment to have your work checked by the plugin — it verifies that each imported line has indeed found its product and its delivery, proof that the automation you built is doing its job.

One note for later: here, you imported these lines yourself from a nicely organized spreadsheet. But a delivery note, to begin with, is just a document — not a ready-to-use file. How do you get from one to the other? You'll find out a little further along in the course.

## Help article with further information

- [Import data into SeaTable]({{< relref "help/startseite/import-von-daten/" >}})
- [Automation overview]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [The link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte/" >}})
