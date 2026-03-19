---
title: 'Пример Python: Генерация штрих-кодов'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-generatsiya-shtrikh-kodov'
---

Этот скрипт преобразует текстовые значения в изображения штрих-кодов формата Code 128 и сохраняет их как изображения в SeaTable.

## The complete script

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

    info = base.upload_bytes_file(str(text) + '.png', buf.read())
    base.update_row(TABLE_NAME, row['_id'], {IMAGE_COLUMN: [info.get('url')]})

print("Barcodes generated.")
```

Adjust `TEXT_COLUMN` and `IMAGE_COLUMN` to match your column names. You can customize the barcode appearance by modifying the options (module_width, module_height, font_size, etc.).

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
