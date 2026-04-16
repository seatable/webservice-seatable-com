---
title: 'Пример Python: Запрос биржевых котировок'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-birzevye-kotirovki'
seo:
    title: 'Python: Получение биржевых котировок в SeaTable'
    description: 'Получайте актуальные биржевые котировки из внешнего API и обновляйте таблицу SeaTable с помощью этого скрипта Python.'
---


Этот скрипт получает актуальные биржевые котировки через API Twelve Data и записывает цены в таблицу SeaTable. Он демонстрирует, как вызывать внешние API из скрипта Python в SeaTable. Скрипт обрабатывает все строки и подходит для ручного запуска или как запланированная автоматизация.

![Stock Prices in SeaTable](stock-prices.png)

{{< dtable-download name="Stock Prices" file="/downloads/python-examples/stock-prices.dtable" text="База с примерами данных и готовым скриптом для непосредственного тестирования." />}}

## Предварительные требования

- Бесплатный API-ключ от [Twelve Data](https://twelvedata.com/)
- Таблица со столбцами `Symbol` (текст) и `Price` (число)

## Скрипт

Введите свой API-ключ в `API_KEY`. Скрипт проверяет, установлен ли действительный ключ, и немедленно прерывается при ошибке API.

```python
from seatable_api import Base, context
import requests

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Stocks"
API_KEY = "your-api-key"

if API_KEY == "your-api-key":
    print("ERROR: Please set your Twelve Data API key first.")
    print("Get a free key at https://twelvedata.com/")
else:
    rows = base.list_rows(TABLE_NAME)
    for row in rows:
        symbol = row.get('Symbol')
        if not symbol:
            continue

        url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if 'price' in data:
            base.update_row(TABLE_NAME, row['_id'], {
                'Price': float(data['price'])
            })
            print(f"{symbol}: {data['price']}")
        else:
            print(f"API error: {data.get('message', 'unknown error')}")
            break

    print("---")
    print("Stock prices updated.")
```

Вы можете заменить API Twelve Data на любого другого поставщика финансовых данных. Адаптируйте URL и обработку ответа соответственно.

Полный справочник функций доступен в [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
