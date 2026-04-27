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


Dieses Skript wandelt Textwerte (z.B. Produkt-IDs, Seriennummern) in Barcode-Bilder im Code-128-Format um und speichert sie als Bilder in SeaTable. Das Skript durchläuft alle Zeilen und überspringt solche, die bereits einen Barcode haben. Es eignet sich für die manuelle Ausführung oder als Automation.

![Barcode Generator in SeaTable](barcode-generator.png)

{{< dtable-download name="Barcode Generator" file="/downloads/python-examples/barcode-generator.dtable" text="Base mit Beispieldaten und fertigem Skript zum direkten Ausprobieren." />}}

## Voraussetzungen

Die Tabelle benötigt mindestens zwei Spalten:

- Eine **Text-Spalte** mit dem Wert, der als Barcode kodiert werden soll (z.B. "Product ID")
- Eine **Bild-Spalte**, in die der erzeugte Barcode gespeichert wird (z.B. "Barcode")

## Das Skript

Passen Sie die drei Variablen am Anfang an Ihre Tabellenstruktur an. Das Erscheinungsbild des Barcodes können Sie über die `options` anpassen (Breite, Höhe, Schriftgröße, etc.).

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

## Ausführung

Das Skript kann auf drei Arten gestartet werden:

- **Manuell** im Python-Editor der Base
- **Per Automation** (z.B. zeitgesteuert oder bei neuen Zeilen)
- **Per Schaltfläche** — dafür müsste das Skript so angepasst werden, dass es nur die aktuelle Zeile verarbeitet

Mehr dazu erfahren Sie [hier]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
