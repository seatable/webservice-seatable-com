---
title: 'Step 8: Connect the existing with the API'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-8-connect-the-existing-with-the-api'
aliases:
    - '/help/schritt-8-api'
seo:
    title: 'Step 8 of SeaTable course 4: bringing data in through the API'
    description: 'Learn how an existing piece of software pushes data into SeaTable through its API: the api.seatable.com explorer, the append_rows operation, and the matching Python code.'
---

From the very start, your delivery lines have been arriving, linking up, and getting validated. But one question has stayed open: the **order** lines — the ones that say what you had ordered — where do they come from? You never entered them yourself. That is the subject of this last technical building block, and it reverses the direction of everything we have seen so far: instead of taking information out of SeaTable, we are going to bring it in, from the outside.

## Connecting the existing system, not replacing it

In a real company, orders are not born in SeaTable: they already live in a management or accounting software. When you enter a supplier invoice there, that software already knows the ordered lines. So the idea is not to re-enter everything in SeaTable, nor to rebuild that software here: it is to **connect the one that already exists**.

Concretely, when the invoice is entered, that system calls the **SeaTable API** to drop the order lines into it — all at once, in a single request. That is how the order lines in your base appeared without you touching them: pushed from the outside, by the tool that holds them.

{{< warning headline="You connect, you do not replace" text="This is an important matter of posture. SeaTable is not trying to replace your management software: it plugs into it. The API is the meeting point between what you build here and the systems already in place in the company — each keeps its role, and the data flows between them." />}}

## The API in practice

You do not have a management software at hand, but you can play its role. Head to the API explorer, [api.seatable.com](https://api.seatable.com): it lists every operation possible on a base and lets you try them out directly, with your own API token. The one we are interested in adds several rows in a single call: `append_rows`.

Point it at your base and the `Line items` table, describe a few order lines, then fire the request. Go back into your base: the rows are there. You have just done, by hand, what the management software would do automatically for every invoice — and this is the moment to have the plugin confirm it.

![The api.seatable.com explorer: the append_rows operation and the generated Python code alongside it](images/lvl4-api-explorer.png)

Look at what the explorer shows next to the request: the **matching code**, in Python, with the `requests` library you already came across at the webhooks step. The loop closes: the API, the scripts, the webhooks — everywhere the same gesture, an HTTP request. What you have just run by hand, a management software runs behind the scenes for every invoice.

{{< warning headline="An API token opens your base" text="The explorer asks you for an API token, the one for your base. Handy for trying things out, but keep in mind what it represents: the access key to your data. In production, it is the calling software that holds it — it must keep it on the server side, never expose it in a page nor send it to a browser." />}}

## Going further

Your ordered lines and your delivered lines now coexist in the same table, each tied to its own document — an order on one side, a delivery on the other, for the same supplier. Nothing stops you from comparing them automatically: was everything that was ordered actually delivered? The principle picks up the announced / received comparison from step 3, applied this time from one document to another. We leave that exploration to you.

## Try it yourself

Before firing your `append_rows` request, think about what makes it reliable on the management software's side: what happens if it sends it twice for the same invoice? You run into, at the scale of a whole system, the question of idempotence you met with the validation button at step 3 — a reminder that the same precautions apply, whether you click a button or wire two pieces of software together.

## Help article with further information

- [Using the SeaTable API]({{< relref "help/integrationen/seatable-api/" >}})
- [Creating an API token]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens/" >}})
- [The interactive API explorer](https://api.seatable.com)
