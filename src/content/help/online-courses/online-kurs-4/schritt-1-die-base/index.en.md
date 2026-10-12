---
title: 'Step 1: The starting base'
date: 2026-07-02
lastmod: '2026-10-01'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-1-the-starting-base'
aliases:
    - '/help/schritt-1-die-base'
seo:
    title: 'Step 1 in SeaTable Course 4: the warehouse base'
    description: 'Import the Warehouse base and get to know its three tables — the products, the incoming documents and their lines — before you automate the receiving of deliveries.'
---

Before you automate anything, you need a base to work on. In this course you run a warehouse: you receive goods, you check what arrives, and you keep your stock up to date. So we start from a base that is already prepared — as in the previous courses — to spend our time on automation rather than on data entry.

Download the following file and import it as a new base:

[SeaTable Course 4 - Warehouse.dtable](/SeaTable-Course-4-Warehouse.dtable)

Then add the online courses plugin to this base. You keep following the course here, on the site; the plugin is the companion you switch over to now and then to put things into practice and have your work checked. If you have never used it, start with its built-in Welcome course: a short tour of how a course works with it, including two small exercises to try it out.

Even though you did not build the base yourself, take the time to get to know it well: the course refers back to it at every step, and a few of the column types may be new to you.

## The components of the base

The `Warehouse` base is organized around three tables: your product catalog, the documents that move goods in and out, and the lines that detail each of those documents.

### The catalog: `Products`

The `Products` table is your catalog. Each row is one product, identified by its `Reference` — the barcode printed on the packaging. A few descriptive columns — `Description`, `Brand` and `Qty` (the pack size, such as `250 g`) — say what the product actually is. The `Stock` column shows the quantity you have in reserve: it is the number the rest of the course will work to keep up to date, without you having to touch it by hand. Keep an eye on `Reference`: it is what everything else in the base will use to point at a product.

You will not always have to fill those descriptive fields by hand — a script can go and look them up from the barcode alone. For now, just note they are there.

{{< warning headline="Stock is a number, not a formula" text="The Stock column is a plain number, not an automatic calculation. That is a deliberate choice for this course: you will learn to move it yourself, with a script you write in step 3. In a real base, stock can also be calculated from the movements — but writing it ourselves is exactly what makes the next steps meaningful." />}}

### The documents: `Documents`

Each record in the `Documents` table is a piece of paperwork that moves stock. Its `{{< seatable-icon icon="dtable-icon-single-election" >}} Movement type` marks which way the goods go — a `Delivery` brings them in, a `Customer order` sends them out — and `{{< seatable-icon icon="dtable-icon-file" >}} File` holds the document itself: the delivery note, for example. Two text columns carry the numbers printed on that paperwork: `{{< seatable-icon icon="dtable-icon-single-line-text" >}}Delivery reference`, the number the supplier gave this delivery, and `{{< seatable-icon icon="dtable-icon-single-line-text" >}}PO reference`, the number of your own order it answers.

{{< warning headline="Deliveries only" text="Throughout this course, every document is a Delivery — goods coming in that add to your stock. We leave the Customer order direction aside." />}}

The other columns in this table — those that will hold the text extracted from the document, the archive link or the assignment of an issue to a colleague — will fill up as the course goes on, as you put them into service. No need to detail them now; each one arrives at its own step. One of them is worth spotting straight away, though: `{{< seatable-icon icon="dtable-icon-link-formulas" >}} Lines to review` counts, on its own, how many lines of that delivery came in with something wrong. Nobody fills it in — SeaTable recalculates it — and step 3 turns on that very fact.

### The lines: `Line items`

A document on its own does not say much: it is its lines that count. The `Line items` table details each document, one line per product. Each line ties a product from the catalog to two quantities: `Qty`, what the document **announces**, and `Received qty`, what you **actually find** on receiving. It is the comparison of these two numbers that sits at the heart of the course. Two more columns record how the receiving went — `Status` and `Validated` — and you put them to work in step 3. Each line also carries, as plain text, the two references it belongs to: `{{< seatable-icon icon="dtable-icon-single-line-text" >}}Product reference` and `{{< seatable-icon icon="dtable-icon-single-line-text" >}}Document reference`. They are the whole subject of step 2.

## How it all fits together

The `Documents` and `Line items` tables are linked: on the document side, the `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Line items` column gathers all of its lines; on the line side, `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Document` points to the document it belongs to. A header and its lines is a very common way to organize a commercial document, whether it is an invoice or a delivery note. Each line also links its `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Product` to the catalog, which lets it show the product's `{{< seatable-icon icon="dtable-icon-link-formulas" >}} Description` without retyping it.

In a well-run warehouse, the same goods pass through three states, and your base holds the two that this course is about:

- **Ordered**: your purchase order — what you asked the supplier for. Those lines live in whatever software places your orders, and they stay there. All your base ever sees of them is the order's reference, printed on the delivery note.
- **Delivered**: what the delivery note announces on arrival, in the `Qty` column.
- **Received**: what you actually count on the dock, in the `Received qty` column.

The course's through-line compares the last two. The supplier announces three boxes, you receive only two: the gap has to jump out, be tracked, and trigger what is needed — a stock update, a notification, or a colleague stepping in. That is exactly what you are going to build, one brick after another.

## Try it yourself

Open the `Documents` table and find the delivery note already there. Its header is filled in — you can have a look at the original note in the `File` column, but you will see it has no lines yet: the detail of what the supplier sent — which products, in what quantities — is still missing. Supplying that detail is exactly where the next step begins.

## Help article with further information

- [Activating a plugin in a base]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base/" >}})
- [Creating a base from a DTABLE file]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei/" >}})
- [The link column]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte/" >}})
- [The link formula column]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen/" >}})
