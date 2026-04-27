---
title: 'Exemplo Python: Converter HEIC para PNG'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-converter-heic-png'
---

Este script converte ficheiros de imagem HEIC (comumente usados por dispositivos Apple) para o formato PNG.

## The complete script

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

The script skips rows that already have a PNG file. Adjust the table and column names to match your setup.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
