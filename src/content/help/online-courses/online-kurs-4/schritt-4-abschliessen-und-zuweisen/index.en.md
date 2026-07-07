---
title: 'Step 4: Close and alert'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-4-close-and-alert'
aliases:
    - '/help/schritt-4-abschliessen-und-zuweisen'
seo:
    title: 'Step 4 of SeaTable course 4: close a delivery and assign a dispute'
    description: 'Close a delivery by dating it, then build an automation that assigns a colleague when something is off — discovering along the way why trigger conditions matter so much.'
---

The line items are validated, the stock is up to date. What remains is to close the receipt of the document and, if not everything was in order, to escalate the problem to the right person. You are going to build a second automation — and, along the way, meet the single most important reflex there is when you automate.

## Close the receipt

Until now you have worked line by line. Take a step back now: open the document record. The same app as in the previous step gives you an overview of it — one page per delivery, where you see at a glance how many line items are still to be checked and whether any discrepancy has been reported.

When you have finished processing the delivery, date it: fill in `Operator validation`. This simple gesture — a date set by hand — means "this document is processed", and it is what will trigger the next step.

![A document record in the app, with the delivery summary and the validation field](images/lvl4-close-document.png)

## Alert when there is a problem

A compliant delivery calls for no particular action. But if items are missing, or if a batch arrived damaged, someone has to deal with it — file a claim with the supplier, adjust an order. Let's automate that alert.

The trigger, this time, is not the arrival of a new line but the **modification** of a document: the exact moment you fill in `Operator validation`. The action: assign a `Reviewer`, the person in charge of settling the dispute.

On your base, you are on your own: assign the document to yourself. In a real team — as you saw in the [level 3 course, dedicated to collaboration]({{< relref "help/online-courses/online-kurs-3/level-drei-einfuehrung/" >}}) — it would be a colleague, the purchasing team for example, who would receive the notification and take over.

## The condition that changes everything

Build the automation just like that — trigger: `Operator validation` filled in; action: assign the reviewer — then try it on a **perfectly compliant** delivery. Surprise: a reviewer is assigned all the same, even though there is nothing to settle.

This is the most common trap of automations: a trigger that is too broad. Your rule fires for *every* validated document, whether it is a problem or not. It is missing a **condition**.

Add it: the action should only run if `Review needed` is true — in other words if at least one line item deviates from compliant. Play it again: a delivery without issues no longer bothers anyone, while a delivery with a discrepancy assigns its reviewer just fine.

{{< warning headline="Always ask -- only if?" text="A trigger decides when an automation runs; a condition decides in which cases only. Forgetting the condition is the most frequent mistake: the rule fires too often, or at the wrong moment. The right reflex, for every automation, is to ask not only when it should run, but also when it must absolutely not." />}}

This is a good moment to have your work checked by the plugin: it looks that a reviewer has indeed been assigned on the document that needed one.

## Try it yourself

Open the record of a delivery you closed without any discrepancy, and confirm that no reviewer is assigned to it: your condition is doing its job. Then imagine the next rule you would add in a real warehouse — alerting the team when a delivery arrives late, for example. What would its trigger be, and above all: what condition would keep it from firing when it shouldn't?

## Help article with further information

- [The collaborator column]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte/" >}})
- [Create and configure an automation]({{< relref "help/base-editor/automationen/" >}})
- [The level 3 course: collaborating on shared data]({{< relref "help/online-courses/online-kurs-3/level-drei-einfuehrung/" >}})
