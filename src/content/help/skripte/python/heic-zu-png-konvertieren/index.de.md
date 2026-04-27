---
title: 'Python-Beispiel: HEIC in PNG konvertieren'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-heic-in-png-konvertieren'
seo:
    title: 'Python: HEIC-Bilder in PNG konvertieren in SeaTable'
    description: 'Konvertieren Sie HEIC-Bilddateien automatisch in das PNG-Format und speichern Sie diese in SeaTable mit diesem Python-Skript.'
---


Dieses Skript konvertiert HEIC-Bilddateien (häufig von Apple-Geräten verwendet) in das PNG-Format. Es liest HEIC-Dateien aus einer Spalte, konvertiert sie und speichert die erzeugten PNG-Dateien in einer anderen Spalte.

{{< warning headline="Python Runner Version" text="Dieses Skript erfordert Python Runner Version 4.1.1 oder höher." />}}

## Das vollständige Skript

```python
from seatable_api import Base, context
from PIL import Image
from pillow_heif import register_heif_opener
from io import BytesIO

register_heif_opener()

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Photos"
HEIC_COLUMN = "HEIC File"
PNG_COLUMN = "PNG File"

rows = base.list_rows(TABLE_NAME)
for row in rows:
    heic_files = row.get(HEIC_COLUMN, [])
    if not heic_files or row.get(PNG_COLUMN):
        continue

    url = heic_files[0] if isinstance(heic_files[0], str) else heic_files[0].get('url', '')
    content = base.download_file(url)

    img = Image.open(BytesIO(content))
    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    info = base.upload_bytes_file(row.get('Name', 'image') + '.png', buf.read(), file_type='image')
    base.update_row(TABLE_NAME, row['_id'], {PNG_COLUMN: [info.get('url')]})

print("HEIC files converted to PNG.")
```

Das Skript überspringt Zeilen, die bereits eine PNG-Datei haben. Passen Sie die Tabellen- und Spaltennamen an Ihre Struktur an.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
