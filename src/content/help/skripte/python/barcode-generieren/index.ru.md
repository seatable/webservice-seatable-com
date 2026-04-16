---
title: 'Пример Python: Генерация штрих-кодов'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-generatsiya-shtrikh-kodov'
seo:
    title: 'Python: Генерация штрих-кодов в SeaTable'
    description: 'Конвертируйте текст в изображения штрих-кодов (Code 128) и сохраняйте их в SeaTable с помощью этого скрипта Python.'
---


Этот скрипт преобразует текстовые значения (например, идентификаторы продуктов, серийные номера) в изображения штрих-кодов формата Code 128 и сохраняет их как изображения в SeaTable. Скрипт обрабатывает все строки и пропускает те, которые уже содержат штрих-код. Он подходит для ручного запуска или как автоматизация.

![Barcode Generator in SeaTable](barcode-generator.png)

{{< dtable-download name="Barcode Generator" file="/downloads/python-examples/barcode-generator.dtable" text="База с примерами данных и готовым скриптом для непосредственного тестирования." />}}

## Предварительные требования

Таблица должна содержать минимум два столбца:

- **Текстовый столбец** со значением, которое будет закодировано как штрих-код (например, «Product ID»)
- **Столбец изображений**, в который будет сохранён сгенерированный штрих-код (например, «Barcode»)

## Скрипт

Адаптируйте три переменные в начале под структуру вашей таблицы. Внешний вид штрих-кода можно настроить через `options` (ширина, высота, размер шрифта и т.д.).

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

## Запуск

Скрипт можно запустить тремя способами:

- **Вручную** в Python-редакторе базы
- **Через автоматизацию** (например, по расписанию или при создании новых строк)
- **Через кнопку** — для этого скрипт нужно адаптировать для обработки только текущей строки

Подробнее об этом [здесь]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Полный справочник функций доступен в [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
