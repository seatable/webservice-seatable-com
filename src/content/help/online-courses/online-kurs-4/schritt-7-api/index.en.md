---
title: 'Step 7: Connect the existing with the API'
date: 2026-07-02
lastmod: '2026-07-23'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-7-connect-the-existing-with-the-api'
aliases:
    - '/help/schritt-8-api'
    - '/help/step-8-connect-the-existing-with-the-api'
seo:
    title: 'Step 7 of SeaTable course 4: bringing data in through the API'
    description: 'Learn how an existing piece of software pushes data into SeaTable through its API: the api.seatable.com explorer, the append_rows operation, and the matching Python code.'
---

From the very start, your delivery lines have been arriving, linking up, and getting validated. But one question has stayed open: the **purchase-order** lines — the ones that say what you had ordered from your suppliers — where do they come from? You never entered them yourself. That is the subject of this last technical building block, and it reverses the direction of everything we have seen so far: instead of taking information out of SeaTable, we are going to bring it in, from the outside.

## Connecting the existing system, not replacing it

In a real company, orders are not born in SeaTable: they already live in a management or accounting software. When you enter a supplier invoice there, that software already knows the ordered lines. So the idea is not to re-enter everything in SeaTable, nor to rebuild that software here: it is to **connect the one that already exists**.

Concretely, when the invoice is entered, that system calls the **SeaTable API** to drop the order lines into it — all at once, in a single request. That is how the order lines in your base appeared without you touching them: pushed from the outside, by the tool that holds them.

{{< warning headline="You connect, you do not replace" text="This is an important matter of posture. SeaTable is not trying to replace your management software: it plugs into it. The API is the meeting point between what you build here and the systems already in place in the company — each keeps its role, and the data flows between them." />}}

## The API in practice

You do not have a management software at hand, but you can play its role. Head to the API explorer, [api.seatable.com](https://api.seatable.com): it lists every operation possible on a base and lets you try them out directly, with your own API token. The one we are interested in adds several rows in a single call: `append_rows`.

<!-- TODO (spine open point #9): resolve what document the pushed order lines hang from. Links are now made on the raw Delivery reference, and the course is delivery-only (Line items no longer carries a movement type). A line whose Document reference matches no document stays unlinked — yet the whole payoff here is watching it link itself. Provisional plan: push the lines with the Delivery reference of note B ("your existing system records what was ordered for this delivery"), which also gives Documents.PO reference a visible job. Confirm before finalizing this section; the append_rows fields below assume it. -->

Point it at your base and the `Line items` table, describe a few order lines — each carrying the `Delivery reference` of a delivery already in your base, so your linking automation can attach it — then fire the request. Go back into your base: the rows are there, already tied to their product and their document, because the automation you built in step 2 caught them the instant they appeared. You have just done, by hand, what the management software does automatically for every invoice. Open the **online-courses plugin**, select **Step 7**, and let it confirm that your pushed line arrived and linked itself.

![The api.seatable.com explorer: the append_rows operation and the generated Python code alongside it](images/lvl4-api-explorer.png)

Look at what the explorer shows next to the request: the **matching code**, in Python, with the `requests` library you already came across at the webhooks step. The loop closes: the API, the scripts, the webhooks — everywhere the same gesture, an HTTP request. What you have just run by hand, a management software runs behind the scenes for every invoice.

One last thing worth a thought before you leave it: what would happen if that software fired the same request twice for the same invoice? You would find, at the scale of a whole system, the very question of idempotence you met with the validation button in step 3 — the same precaution applies, whether you click a button or wire two pieces of software together.

{{< warning headline="An API token opens your base" text="The explorer asks you for an API token, the one for your base. Handy for trying things out, but keep in mind what it represents: the access key to your data. In production, it is the calling software that holds it — it must keep it on the server side, never expose it in a page nor send it to a browser." />}}

## Try it yourself

You have played the outside system writing *in*; now do the smallest version of it with your own hands. Off to the side of your base sits a **webform** with a single `Reference` field and **barcode scanning turned on**. Take a real product from your desk — a bag of coffee, anything with a barcode — open that form on your phone and **scan it**. A new row lands in `Products`, carrying nothing but its barcode. You have just fed your base from the physical world, in one gesture.

## Going further: enrich from Open Food Facts

That freshly scanned row holds a barcode and nothing else — so let a script fill in the rest. The API you used above pulls data in from a system *you* own; a script can travel the other way just as easily, out to a public service on the open web.

Every barcode in your `Products` catalog is described in [Open Food Facts](https://world.openfoodfacts.org), a free, community-run database of food products. So rather than typing a product's `Description`, `Brand` and `Qty` by hand, you let a script look them up from the barcode alone.

On the `Products` table, create a **button column** named `🌐 Open Food Facts` and attach the script below — the same button-and-script pattern you built in step 3. Click it on your freshly scanned row and watch `Description`, `Brand` and `Qty` appear on their own.

```python
import requests
from seatable_api import Base, context

base = Base(context.api_token, context.server_url)
base.auth()

def get_product(barcode: str):
    url = f"https://world.openfoodfacts.org/api/v3/product/{barcode}.json"
    headers = {"User-Agent": "SeaTableOnlineCourseLevel4/1.0 (https://seatable.com)"}
    params = {"fields": "product_name,brands,code,quantity"}

    resp = requests.get(url, headers=headers, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    if data.get("status") == "success":
        return data["product"]
    print(f"Product {barcode} can't be found")
    return None

p = get_product(context.current_row.get('Reference'))
if p:
    base.update_row('Products', context.current_row['_id'], {
        'Description': p.get("product_name"),
        'Brand': p.get("brands") or "–",
        'Qty': p.get("quantity") or "–",
    })
```

The script reads the row's `Reference`, asks Open Food Facts about that barcode (`GET /product/{barcode}.json` — no key needed to read), and writes three of the fields it returns back onto the row: `product_name` into `Description`, `brands` into `Brand`, `quantity` into `Qty`. It is the mirror image of what you did above — there, an outside system wrote into your base; here, your base reaches outside and brings something back.

{{< warning headline="Identify the app you are calling from" text="Open Food Facts is free and run by a non-profit, and it asks every program that calls its API to send a User-Agent header naming the app that is calling — so real applications are not mistaken for anonymous bots, and so the traffic can be traced back to whoever is behind it. The script already does this: it announces itself as the SeaTable course and points to seatable.com, so you have nothing to fill in. If one day you turn a script like this into a tool of your own, that identity is what you would make yours — politely saying who you are is simply part of being a good citizen of the open web." />}}

## Help article with further information

- [Using the SeaTable API]({{< relref "help/integrationen/seatable-api/" >}})
- [Creating an API token]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens/" >}})
- [The interactive API explorer](https://api.seatable.com)
