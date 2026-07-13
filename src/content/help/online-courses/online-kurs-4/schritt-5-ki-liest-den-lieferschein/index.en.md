---
title: 'Step 5: Let AI read the delivery note'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/help/step-5-let-ai-read-the-delivery-note'
aliases:
    - '/help/schritt-5-ki-liest-den-lieferschein'
seo:
    title: 'Step 5 of SeaTable course 4: extract line items from a PDF with AI'
    description: 'Let SeaTable read a PDF delivery note and create its line items automatically — text recognition, AI extraction, script — without ever making AI a critical link.'
---

Remember step 2: you imported the line items of a delivery from a neatly organized spreadsheet. But a real delivery note, to begin with, is a PDF document, not a ready-to-use file. Now you are going to let SeaTable do that work for you: read the PDF and pull out the line items, all on its own. This is the most spectacular moment of the course — and also the one where you need to stay clear-eyed about what AI can, and cannot, do.

It all happens in an automation triggered when a new document arrives, in three steps: **read**, **extract**, **create**.

## Read the document

The delivery note arrives in the `File` column of your document, as a PDF. First action: a **text recognition** AI action. It requires no instructions — you only tell it which column to read, `File`, and the column where to drop the result, `OCR text`. SeaTable extracts all the text from it: references, quantities, whatever is on the paper — but raw, as-is.

![The result of text recognition dropped into the OCR text column from the PDF](images/lvl4-ai-extraction.png)

## Extract the line items

This raw text needs to be structured: isolating each product and its quantity. That is the job of a **custom AI action**, to which you give a precise instruction this time. Here it is, to paste as-is:

```
From {OCR text}, extract the purchase order reference (look for "purchase order", "PO" or "P.O.") and the delivery reference and, for each product, its product reference and quantity. Write valid JSON (double quotes) into the {JSON} column, as plain text, no code block, with this exact shape:
{
    "delivery": "delivery reference",
    "order": "purchase order reference",
    "products": [
        { "ref": "product reference", "qty": product quantity as a number }
    ]
}
```

<!-- TODO: verify that the placeholder syntax {OCR text} / {JSON} matches the column referencing of the Custom AI action in the base. -->

The instruction asks the AI to answer in **JSON** — a format your script will read back unambiguously. The result lands in the `JSON` column.

## Create the line items

You already know, from step 3, what a script can do. This one reads the JSON produced by the AI and creates one line per product in `Line items`. It is provided to you:

```python
from seatable_api import Base, context
import json

base = Base(context.api_token, context.server_url)
base.auth()

data = json.loads(context.current_row.get('JSON'))
base.update_row(context.current_table, context.current_row['_id'], {
    'PO reference': data['order'],
    'Delivery reference': data['delivery'],
})
lines = [{
    'Product ref': p['ref'],
    'Qty': int(p['qty']),
    'Document reference': 'DN' + data['delivery'],
} for p in data['products']]
if lines:
    base.batch_append_rows('Line items', lines)
```

And here is the elegance of the whole thing: each line created triggers, as in step 2, your "link by comparison" automation. The new lines attach themselves to their product and their document. From the PDF to the linked line items, without a single manual entry — chain these three actions in an automation triggered by the arrival of a document, drop a new note, and watch it work.

## AI proposes, you validate

An essential word before going further. AI is impressive, but it is not infallible: depending on the scan quality or the supplier's layout, it can get a quantity wrong, miss a line, or simply choke. That is in its nature, and no setting changes that one hundred percent.

That is precisely why the next step in your process is the human verification you already know. The lines proposed by the AI are not set in stone: they go through the receiving of step 3, where you compare what was announced against what is real. The AI's imperfection is not a flaw to work around, it is the very reason for this validation.

And what if the AI goes completely off the rails on your example? The plugin offers you a "Load the example" button that lays down the correct lines directly. Your progress is never blocked by a whim of the model — and the plugin checks that the lines are there and validated, not that the AI succeeded on the first try.

{{< warning headline="Never make AI a critical link" text="AI speeds things up and proposes, but a process that must run reliably cannot depend on its success. Always keep, behind it, a human validation and a fallback path. Here, that safety net is the receiving of step 3 and the load-the-example button — AI saves time, it never decides on its own." />}}

## Try it yourself

Open the `OCR text` column of a document already processed and read what the recognition actually produced: raw text, sometimes approximate. Measure the distance travelled between that mess and the clean, linked and verified line items of your base — that is all the work the OCR, AI and script chain did for you, and it is also why a human review remains in order.

## Help article with further information

- [Artificial intelligence actions]({{< relref "help/ai/ai-automations/" >}})
- [Python scripts in SeaTable]({{< relref "help/skripte/python/" >}})
