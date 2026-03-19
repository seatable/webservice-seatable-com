---
title: 'Exemplo Python: Consultar cotações de ações'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-cotacoes-acoes'
---

Este script obtém cotações de ações atuais da API Twelve Data e atualiza as linhas correspondentes numa tabela do SeaTable.

## Prerequisites

You need a free API key from [Twelve Data](https://twelvedata.com/) and a table with columns `Symbol` (text) and `Price` (number).

## The complete script

```python
from seatable_api import Base, context
import requests

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Stocks"
API_KEY = "your-api-key"

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

print("Stock prices updated.")
```

You can replace the Twelve Data API with any other financial data provider. Adjust the URL and response parsing accordingly.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
