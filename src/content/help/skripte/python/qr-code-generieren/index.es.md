---
title: 'Ejemplo Python: Generar códigos QR'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/python-generar-qr'
seo:
    title: 'Python: Generar códigos QR en SeaTable'
    description: 'Genere códigos QR a partir de texto o URLs y guárdelos como imágenes directamente en SeaTable con este script Python.'
---


Este script lee contenido de texto (por ej. URLs, IDs de producto) de una columna, genera imágenes de códigos QR y las guarda en una columna de imagen. El script recorre todas las filas de la tabla y por lo tanto es adecuado para la ejecución manual o como automatización — no como script de botón.

![QR Code Generator in SeaTable](qr-code-generator.png)

{{< dtable-download name="QR Code Generator" file="/downloads/python-examples/qr-code.dtable" text="Base con datos de ejemplo y script listo para probar directamente." />}}

## Requisitos

La tabla necesita al menos dos columnas:

- Una **columna de texto** o **URL** con el contenido a codificar como código QR.
- Una **columna de imagen** donde se guardará el código QR generado.

## El script

Adapte las cuatro variables del inicio a la estructura de su tabla. El script omite las filas que no tienen valor de texto o que ya contienen un código QR. Establezca `OVERWRITE = True` para regenerar los códigos QR existentes.

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

## Ejecución

El script se puede iniciar de tres formas:

- **Manualmente** en el editor Python de la base
- **Por automatización** (por ej. programada o al crear nuevas filas)
- **Por botón** — para ello el script debería adaptarse para procesar solo la fila actual

Más información [aquí]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Para la referencia completa de funciones, visite el [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
