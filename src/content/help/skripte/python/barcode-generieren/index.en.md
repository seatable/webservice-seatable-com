---
title: 'Python example: Generate barcodes'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/help/python-generate-barcodes'
seo:
    title: 'Python: Generate barcodes in SeaTable'
    description: 'Convert text to barcode images (Code 128) and store them in SeaTable with this Python script.'
---


This script converts text values (e.g. product IDs, serial numbers) into barcode images in Code 128 format and stores them as images in SeaTable. The script iterates through all rows and skips those that already have a barcode. It is suitable for manual execution or as an automation.

![Barcode Generator in SeaTable](barcode-generator.png)

{{< dtable-download name="Barcode Generator" file="/downloads/python-examples/barcode-generator.dtable" text="Base with sample data and ready-made script to try out directly." />}}

## Prerequisites

The table requires at least two columns:

- A **text column** with the value to be encoded as a barcode (e.g. "Product ID")
- An **image column** where the generated barcode will be stored (e.g. "Barcode")

## The script

Adjust the three variables at the beginning to match your table structure. You can customize the barcode appearance via the `options` (width, height, font size, etc.).

```python
from seatable_api import Base, context
import barcode
from barcode.writer import ImageWriter
from io import BytesIO

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Table1"
TEXT_COLUMN = "Product ID"
IMAGE_COLUMN = "Barcode"

rows = base.list_rows(TABLE_NAME)
for row in rows:
    text = row.get(TEXT_COLUMN)
    existing = row.get(IMAGE_COLUMN)
    if not text or existing:
        continue

    code128 = barcode.get_barcode_class('code128')
    rv = code128(str(text), writer=ImageWriter())

    buf = BytesIO()
    rv.write(buf, options={"module_width": 0.4, "module_height": 10, "quiet_zone": 1, "font_size": 10, "text_distance": 2})
    buf.seek(0)

    info = base.upload_bytes_file(str(text) + '.png', buf.read(), file_type='image')
    base.update_row(TABLE_NAME, row['_id'], {IMAGE_COLUMN: [info.get('url')]})

print("Barcodes generated.")
```

## Execution

The script can be started in three ways:

- **Manually** in the Python editor of the base
- **Via automation** (e.g. scheduled or on new rows)
- **Via button** — for this the script would need to be adapted to process only the current row

Learn more about this [here]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
