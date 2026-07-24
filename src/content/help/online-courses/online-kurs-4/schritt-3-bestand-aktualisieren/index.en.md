---
title: 'Step 3: Receive the delivery'
date: 2026-07-02
lastmod: '2026-07-23'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-3-receive-the-delivery'
aliases:
    - '/help/schritt-3-bestand-aktualisieren'
    - '/help/step-3-receive-and-update-stock'
    - '/help/schritt-4-abschliessen-und-zuweisen'
    - '/help/step-4-close-and-alert'
seo:
    title: 'Step 3 of SeaTable course 4: receive a delivery, update the stock, raise a dispute'
    description: 'Record what you actually received, write your first Python script to move the stock, then let a scheduled automation assign a reviewer whenever a delivery does not match.'
---

Your line items are in the base and linked to their products. Now for the receiving itself: recording what actually came off the truck, passing it on to your stock, and making sure somebody picks it up when the delivery does not match. Three jobs — and you will use two different tools, which is the whole point of this step.

## Receiving on the dock

In the field, you don't receive goods from a spreadsheet grid. Your base ships with a small app: a page that shows only the line items still waiting to be received, designed for a tablet or phone screen. Open it and, for each line, fill in two things:

- `Received qty`: the quantity you actually count.
- `Status`: the state of the batch — `As expected` if it's fine, otherwise `Too many`, `Too few`, `Missing` or `Damaged`.

Mark at least one line as something other than `As expected` — you will need a delivery with a problem later in this step.

![The receiving app showing the line items to check, with the received quantity and status fields](images/lvl4-receiving-app.png)

{{< warning headline="The status is a human call" text="The status is not calculated automatically, and that is on purpose: a box can arrive complete but damaged. No quantity reconciliation could ever guess that. It is you, on the dock, who decides — and the rest of the course builds on that call." />}}

## Your first script

What is left is moving the stock: adding what you received to the `Stock` of the product concerned. You could go at this with automations — but look at the rule you would have to express. A batch marked `Damaged` or `Missing` adds nothing to what you can sell. `Too many` and `Too few` add what you actually counted, not what was ordered. That is one behaviour per status, and no-code would have you write one rule per case.

A script says it in three lines. This is the arbitration you will make again and again: the built-in actions are quicker to set up, code is better at expressing a rule that branches. Neither is the *advanced* option — they are two tools, and the interesting skill is knowing which one a given job calls for.

SeaTable lets you write scripts in two languages: Python and JavaScript. Throughout this course, we use Python — one of the most widespread languages for automation and data processing, known for its readability, and therefore a good entry point if you're just starting out. What you learn here carries over easily to JavaScript if you prefer it.

The editor is built into your base: nothing to install. And a script there enjoys a precious asset, the `context` object, which gives it access to the base and to the row it was started from, without you handling a single key.

First, the connection to the base. Thanks to `context`, there is no token to paste: SeaTable provides the credentials on the fly.

```python
from seatable_api import Base, context

base = Base(context.api_token, context.server_url)
base.auth()
```

Then the row that launched the script, and the small piece of judgement that no-code made expensive — how much of what arrived is actually sellable:

```python
row = context.current_row

if row.get('Validated'):
    print('This line has already been validated. Nothing to do.')
else:
    status = row.get('Status')
    if status in ('Damaged', 'Missing'):
        delta = 0
    else:
        delta = row.get('Received qty') or 0
```

Notice the first two lines: before anything else, the script checks whether this line has already been validated, and stops if it has. Adding to a stock is not a replayable gesture — run it twice and you have credited yourself goods that never arrived. A guard like this one costs two lines and saves you a wrong stock.

Finally, find the product this line refers to, add the delta to its `Stock`, and mark the line as done:

```python
    products = base.list_rows('Products')
    product = next(p for p in products if p.get('Reference') == row.get('Product reference'))

    base.update_row('Products', product['_id'], {'Stock': (product.get('Stock') or 0) + delta})
    base.update_row('Line items', row['_id'], {'Validated': True})

    print('Stock updated by', delta)
```

{{< warning headline="Keep your credentials out of the code" text="In a SeaTable script, never hard-code a token. Going through context.api_token and context.server_url means the secret never exists in the file itself, so it cannot escape through an export, a screenshot or a snippet you paste somewhere. That is not the same as hiding it from whoever opens the script — anyone allowed to run it could print the token. Where the secret lives, and who may run the code, are two separate questions, and the second one is answered by access rights, not by the code." />}}

## Run it at the right moment

A script can be started in several ways; here you tie it to a button — the `Validate` column of your line items. The operator checks a line, clicks `Validate`, and the stock follows.

Before you press it, open the **online-courses plugin** in your base and select **Step 3**. It notes the current stock first, so it can tell you exactly what your script moved — then it asks you to click `Validate` on a compliant line, and to click it a second time. The stock rises once and stays put: the guard you wrote is doing its job.

## When something is off

A compliant delivery needs nobody. A delivery that came up short, or arrived damaged, needs someone to take it up with the supplier — and that someone should not have to go looking for it.

The criterion is already in your base. On `Documents`, `Lines to review` counts the line items of that delivery whose status is anything other than `As expected`. Greater than zero means there is something to settle.

Now, the thing worth learning here. You cannot start an automation from that column. `Lines to review` is calculated: SeaTable recomputes it whenever the linked lines change, and a recalculation is not an event a trigger can watch. This is not a quirk of this particular base — it is true of every formula and every link-formula column you will ever build.

So you do not react. You **sweep**: a scheduled automation that passes over your documents, keeps the ones matching a condition, and acts on those.

> Trigger: At a given time, for the records that match a condition
>
> Condition: `Lines to review` is greater than 0
>
> Action: Assign a `Reviewer`

Build it exactly like that, then use `Run now` in the automation editor rather than waiting for the night: the delivery you flagged earlier gets its reviewer.

Now press `Run now` again. You are notified a second time, for a dispute that is already assigned — and it would happen again every single night. Nothing in your rule says the document has been dealt with. Add a second condition, `Reviewer` is empty, and run it once more: silence. The document has left the set.

{{< warning headline="A scheduled rule needs a way out" text="An event-driven rule runs once, when something happens. A scheduled rule goes over your records again and again, so it has to know what takes a record out of the set — otherwise it keeps acting on work that is already done. For every scheduled automation you write, ask the question the other way round: what makes a record stop matching?" />}}

On your own base you are alone, so you assign the delivery to yourself. In a real team — as you saw in [Online Course 3 – Collaboration]({{< relref "help/online-courses/online-kurs-3/level-drei-einfuehrung/" >}}) — this would be the buyer who placed the order, the one person who calls the supplier once and settles every line of that delivery in a single conversation.

Back in the plugin, it checks the rule you built, both conditions included. Then it does something itself: it puts a discrepancy on another line and asks you for a `Run now`. What it verifies afterwards is not only that a reviewer is there, but that the automation is the one that put it there.

## Try it yourself

Replay the receiving with a batch marked `Damaged`: fill in a received quantity — you normally would not bother, and here you do it precisely to watch what happens — then validate, and open the product record. The stock has not moved. Your script correctly kept damaged goods out of what you can sell, which is exactly the branch that would have cost you a separate automation.

Then look at the two rules you now own side by side: one fires the instant a line appears, the other passes by on a schedule. Ask yourself which of the two your next idea calls for.

## Help article with further information

- [Python scripts in SeaTable]({{< relref "help/skripte/python/" >}})
- [Run a script from a button or an automation]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren/" >}})
- [The collaborator column]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte/" >}})
- [Online Course 3 – Collaboration]({{< relref "help/online-courses/online-kurs-3/level-drei-einfuehrung/" >}})
