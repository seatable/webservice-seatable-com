---
title: 'Python-Beispiel: QR-Codes generieren'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-qr-codes-generieren'
seo:
    title: 'Python: QR-Codes in SeaTable generieren'
    description: 'Generieren Sie QR-Codes aus Text oder URLs und speichern Sie diese als Bilder direkt in SeaTable mit diesem Python-Skript.'
---


Dieses Skript liest Textinhalte (z.B. URLs, Produkt-IDs) aus einer Spalte, erzeugt daraus QR-Code-Bilder und speichert diese in einer Bildspalte. Das Skript durchläuft alle Zeilen der Tabelle und eignet sich daher für die manuelle Ausführung oder als Automation — nicht als Button-Skript.

![QR Code Generator in SeaTable](qr-code-generator.png)

{{< dtable-download name="QR Code Generator" file="/downloads/python-examples/qr-code.dtable" text="Base mit Beispieldaten und fertigem Skript zum direkten Ausprobieren." />}}

## Voraussetzungen

Die Tabelle benötigt mindestens zwei Spalten:

- Eine **Text-** oder **URL-Spalte** mit dem Inhalt, der als QR-Code kodiert werden soll.
- Eine **Bild-Spalte**, in die der erzeugte QR-Code gespeichert wird.

## Das Skript

Passen Sie die vier Variablen am Anfang an Ihre Tabellenstruktur an. Das Skript überspringt Zeilen, die keinen Textwert haben oder bereits einen QR-Code enthalten. Mit `OVERWRITE = True` können Sie vorhandene QR-Codes neu generieren lassen.

```python
from seatable_api import Base, context
import qrcode
from io import BytesIO

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Table1"
TEXT_COLUMN = "URL"
IMAGE_COLUMN = "QR Code"
OVERWRITE = False

rows = base.list_rows(TABLE_NAME)
for row in rows:
    text = row.get(TEXT_COLUMN)
    existing = row.get(IMAGE_COLUMN)
    if not text or (existing and not OVERWRITE):
        continue

    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    info = base.upload_bytes_file(str(text) + '.png', buf.read(), file_type='image')
    base.update_row(TABLE_NAME, row['_id'], {IMAGE_COLUMN: [info.get('url')]})

print("QR codes generated.")
```

## Ausführung

Das Skript kann auf drei Arten gestartet werden:

- **Manuell** im Python-Editor der Base
- **Per Automation** (z.B. zeitgesteuert oder bei neuen Zeilen)
- **Per Schaltfläche** — dafür müsste das Skript so angepasst werden, dass es nur die aktuelle Zeile verarbeitet

Mehr dazu erfahren Sie [hier]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
