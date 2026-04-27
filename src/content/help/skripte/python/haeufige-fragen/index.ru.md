---
title: 'Скрипты Python: Частые вопросы'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-chastye-voprosy'
seo:
    title: 'Скрипты Python в SeaTable: Часто задаваемые вопросы'
    description: 'Ответы на частые вопросы о скриптах Python в SeaTable: поддерживаемые библиотеки, пакетные операции, локальный запуск и советы по отладке.'
weight: 2
star: true
---

## Как запустить скрипт и локально, и в SeaTable?

Вы можете написать скрипт так, чтобы он работал в обоих окружениях без изменений. Трюк в том, чтобы проверить, доступен ли объект `context`:

```python
from seatable_api import Base

try:
    from seatable_api import context
    base = Base(context.api_token, context.server_url)
except:
    base = Base('your-api-token', 'https://cloud.seatable.io')

base.auth()
```

## Какие библиотеки доступны?

Полный список всех предустановленных библиотек находится в статье [Поддерживаемые библиотеки Python]({{< relref "help/skripte/python/unterstuetzte-python-bibliotheken" >}}). Там же вы узнаете, как добавить собственные библиотеки на самостоятельно размещённом сервере.

## Как обработать более 1 000 строк?

Метод `base.list_rows()` по умолчанию возвращает максимум 1 000 строк. Для обработки большего количества строк используйте один из этих подходов:

**Вариант 1: Цикл с offset**
```python
all_rows = []
offset = 0
while True:
    rows = base.list_rows(TABLE_NAME, start=offset, limit=1000)
    if not rows:
        break
    all_rows.extend(rows)
    offset += 1000
```

**Вариант 2: SQL-запрос**
```python
rows = base.query("SELECT * FROM `Table1` LIMIT 10000")
```

SQL-запросы поддерживают до 10 000 строк за один запрос.

## Как отладить сложные структуры данных?

Используйте `json.dumps()` с отступами для форматированного вывода словарей и списков:

```python
import json
metadata = base.get_metadata()
print(json.dumps(metadata, indent=2))
```

Полный справочник функций доступен в [SeaTable Developer Manual](https://developer.seatable.com/python/).
