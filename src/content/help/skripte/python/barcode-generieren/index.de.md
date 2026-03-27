---
title: 'Python-Beispiel: Barcodes generieren'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-barcodes-generieren'
seo:
    title: 'Python: Barcodes in SeaTable generieren'
    description: 'Konvertieren Sie Text in Barcode-Bilder (Code 128) und speichern Sie diese in SeaTable mit diesem Python-Skript.'
---


Dieses Skript wandelt Textwerte (z.B. Produkt-IDs, Seriennummern) in Barcode-Bilder im Code-128-Format um und speichert sie als Bilder in SeaTable. Es werden nur Zeilen verarbeitet, die noch keinen Barcode haben.

## Das vollständige Skript

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

Passen Sie `TEXT_COLUMN` und `IMAGE_COLUMN` an Ihre Spaltennamen an. Das Erscheinungsbild des Barcodes können Sie über die Optionen (module_width, module_height, font_size, etc.) anpassen.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
