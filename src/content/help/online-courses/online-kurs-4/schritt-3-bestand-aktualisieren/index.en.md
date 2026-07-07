---
title: 'Step 3: Receive and update the stock'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-3-receive-and-update-stock'
aliases:
    - '/help/schritt-3-bestand-aktualisieren'
seo:
    title: 'Step 3 of SeaTable course 4: a script to update the stock'
    description: 'Receive a delivery, record the quantities you got, then meet SeaTable''s Python script to update the stock — right where no-code reaches its limit.'
---

Your line items are in the base and linked to their products. Now for the receiving itself: recording what you actually received, then passing that on to your stock. This is where you meet a new tool — the script — because you are about to run into a limit of no-code.

## Receiving on the dock

In the field, you don't receive goods from a spreadsheet grid. Your base ships with a small app: a page that shows only the line items still waiting to be received, designed for a tablet or phone screen. Open it and, for each line, fill in two things:

- `Received qty`: the quantity you actually count.
- `Status`: the state of the batch — `As expected` if it's fine, otherwise `Too many`, `Too few`, `Missing` or `Damaged`.

![The receiving app showing the line items to check, with the received quantity and status fields](images/lvl4-receiving-app.png)

{{< warning headline="The status is a human call" text="The status is not calculated automatically, and that is on purpose: a box can arrive complete but damaged. No quantity reconciliation could ever guess that. It's you, on the dock, who decides — and the rest of the course builds on that call." />}}

## Where no-code stops today

You have recorded the receipt. What's left is updating the stock: adding the received quantities to the `Stock` of the product concerned. And here, the no-code automation you just learned hits a wall.

An automation acts on the row that triggers it, here a row of `Line items`. But the stock lives in **another** table, `Products`, on the `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Product` record it is *linked* to. Writing into a linked record from an automation is, as of today, not possible without code — and it's actually a planned SeaTable improvement.

Never mind: this is the perfect chance to meet the tool that doesn't have this limit — the script. A script lets you go beyond the built-in functions, for this need and plenty of others. And even the day no-code can write into a linked record, this little script will remain an excellent first playground: you're not learning to bring out the heavy artillery for a trifle, but a tool that will serve you everywhere the built-ins stop.

## Your first script

SeaTable lets you write scripts in two languages: Python and JavaScript. Throughout this course, we use Python — one of the most widespread languages for automation and data processing, known for its readability, and therefore a good entry point if you're just starting out. What you learn here carries over easily to JavaScript if you prefer it.

The editor is built into your base: nothing to install. And a script there enjoys a precious asset, the `context` object, which gives it access to the base and the current row without you handling a single key.

Let's write it together — it's short. (In a hurry, or already comfortable with Python? The complete script is right below, ready to copy and paste.)

First, the connection to the base. Thanks to `context`, there's no token to paste: SeaTable provides the credentials on the fly.

```python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
```

Next, the row that launched the script — `context.current_row` — and computing what to add to the stock, based on the status recorded:

```python
row = context.current_row
status = row.get('Status')
if status == 'As expected':
    delta = row.get('Qty') or 0
elif status in ('Missing', 'Damaged'):
    delta = 0                       # nothing sellable enters the stock
else:                               # Too many / Too few
    delta = row.get('Received qty') or 0
```

Finally, we go from the line up to the linked product and add this `delta` to its `Stock`.

<!-- TODO: coller ici le script complet et testé (récupération du Product lié via son row_id + base.update_row sur Products), et le proposer en bloc à copier-coller. -->

{{< warning headline="Keep your credentials out of the code" text="In a SeaTable script, never hard-code a token. Always go through context.api_token and context.server_url: the secret doesn't appear in the code and is never sent to a browser. Bear this in mind: this protects the secret because only the people allowed to run the script have access to it — it isn't the code that hides it, it's the control over who can run it." />}}

## Run the script at the right moment

A script can be triggered in several ways; here, you tie it to a button — the `Validate` column of your line items. The operator checks a line, clicks `Validate`, and the stock updates.

Why a button rather than an automation that would react to data entry? Because adding to the stock is not a replayable operation. An automation that fired again on every change to the row would add the quantities twice. The button, on the other hand, is a deliberate gesture, made once — and the line then leaves the to-do list, which rules out any risk of double counting.

Click `Validate` for a conforming line, then open its product record: the `Stock` has gone up. This is the right moment to have your work checked by the plugin.

## Try it yourself

Replay the receiving with a batch marked `Damaged`: fill in a received quantity, validate, then check the product's stock. It doesn't move — the script has correctly handled this special case. This small test shows you why the status was worth entering by hand rather than deducing it from a simple quantity gap.

## Help article with further information

- [Python scripts in SeaTable]({{< relref "help/skripte/python/" >}})
- [Run a script from a button or an automation]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren/" >}})
- [Developer documentation: getting started with Python](https://developer.seatable.com/)
- [Get started with Python by automating tasks (Automate the Boring Stuff, free)](https://automatetheboringstuff.com/)
