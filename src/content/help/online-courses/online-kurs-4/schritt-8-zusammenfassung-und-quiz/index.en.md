---
title: 'Step 8: Summary and quiz'
date: 2026-07-02
lastmod: '2026-07-23'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-8-summary-and-quiz'
aliases:
    - '/help/schritt-9-zusammenfassung-und-quiz'
    - '/help/step-9-summary-and-quiz'
seo:
    title: 'Step 8 of SeaTable course 4: summary and quiz'
    description: 'Recap what you have learned — automations, scripts, webhooks, n8n, AI and the API — along the three directions of information, then check your knowledge with the quiz.'
---

Here you are at the end of the journey. Look back for a moment: you took a warehouse that received its deliveries by hand, and turned it into a process that triggers itself, checks itself, updates the stock and raises the alert all on its own. Let's take the time to name what you have learned — because behind the warehouse scenario are skills that hold true for any project.

## Three directions

Everything you have built falls into three directions, depending on where the information comes from and where it goes.

**Inside SeaTable.** The no-code automations — linking by comparison the instant a line appears, then sweeping your deliveries on a schedule to assign whoever must settle a dispute — and the Python scripts — updating a stock, creating rows — act on your data without ever leaving the base. This is the backbone: the most accessible one, and the one everything else leans on.

**To the outside.** Webhooks and n8n send information *out*: a notification on your phone, a file archived in another service. SeaTable tells the world, or hands it a task.

**From the outside.** The API lets other systems *write* into your base: your management software drops its purchase orders there. SeaTable doesn't live in a bubble, it hooks into what already exists.

And, cutting across all of this, **artificial intelligence**: it read a delivery note for you. A powerful accelerator — provided, as you saw, that you always keep the human in the loop.

## The quiz

All that's left is to put your knowledge to the test. The quiz actually takes the shape of a **SeaTable form** — one last nod to what you have just learned. It mixes questions about the features you came across and questions about the base you have equipped throughout the course.

When you're ready, open the [Course 4 quiz](https://cloud.seatable.io/dtable/forms/custom/seatable-quiz-level-4). If you pass, you receive a badge for your profile on the forum, which makes your skills visible. <!-- TODO: forum badge URL -->

## What's next?

The process you have built was deliberately kept simple to get to the point, but it already opens up a thousand next steps: automatically enriching a product sheet from a public database, plugging a third service into your workflow, refining each automation as your needs grow… You now have the building blocks; it's up to you to assemble them for your own needs.

And here is one challenge to stand on your own feet. All along you worked in a single direction — deliveries arriving from your suppliers, adding to the stock. But your base carries a second `Movement type` for the opposite direction: the `Customer order`, where goods leave your shelves. Point the same building blocks the other way — when a customer order comes in, check the stock is there, record what goes out, subtract it from `Stock`, and alert whoever needs to know. It is the patterns you already know, running in reverse — and this time, no one walks you through it.

Thank you for taking this course, and well done for the road you have travelled.
