---
title: 'Пример Python: Генерация QR-кодов'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-generatsiya-qr'
seo:
    title: 'Python: Генерация QR-кодов в SeaTable'
    description: 'Генерируйте QR-коды из текста или URL и сохраняйте их как изображения прямо в SeaTable с помощью этого скрипта Python.'
---


Этот скрипт читает текстовое содержимое (например, URL, идентификаторы продуктов) из столбца, генерирует изображения QR-кодов и сохраняет их в столбец изображений. Скрипт обрабатывает все строки таблицы и поэтому подходит для ручного запуска или как автоматизация — не как скрипт-кнопка.

![QR Code Generator in SeaTable](qr-code-generator.png)

{{< dtable-download name="QR Code Generator" file="/downloads/python-examples/qr-code.dtable" text="База с примерами данных и готовым скриптом для непосредственного тестирования." />}}

## Предварительные требования

Таблица должна содержать минимум два столбца:

- **Текстовый столбец** или **столбец URL** с содержимым, которое будет закодировано в QR-код.
- **Столбец изображений**, в который будет сохранён сгенерированный QR-код.

## Скрипт

Адаптируйте четыре переменные в начале под структуру вашей таблицы. Скрипт пропускает строки без текстового значения или уже содержащие QR-код. Установите `OVERWRITE = True`, чтобы перегенерировать существующие QR-коды.

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

## Запуск

Скрипт можно запустить тремя способами:

- **Вручную** в Python-редакторе базы
- **Через автоматизацию** (например, по расписанию или при создании новых строк)
- **Через кнопку** — для этого скрипт нужно адаптировать для обработки только текущей строки

Подробнее об этом [здесь]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Полный справочник функций доступен в [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
