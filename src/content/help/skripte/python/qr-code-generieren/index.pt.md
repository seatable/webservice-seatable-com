---
title: 'Exemplo Python: Gerar códigos QR'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-gerar-qr'
---

Este script gera códigos QR a partir de conteúdo de texto armazenado numa coluna do SeaTable e guarda as imagens resultantes numa coluna de imagem.

## The complete script

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

    info = base.upload_bytes_file(row['Name'] + '.png', buf.read())
    base.update_row(TABLE_NAME, row['_id'], {IMAGE_COLUMN: [info.get('url')]})

print("QR codes generated.")
```

Set `OVERWRITE = True` if you want to regenerate existing QR codes. Adjust `TEXT_COLUMN` and `IMAGE_COLUMN` to match your column names.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
