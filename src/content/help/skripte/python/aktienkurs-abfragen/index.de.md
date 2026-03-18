---
title: 'Python-Beispiel: Aktienkurse abfragen'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-aktienkurse-abfragen'
seo:
    title: 'Python: Aktienkurse in SeaTable abrufen'
    description: 'Rufen Sie aktuelle Aktienkurse von einer externen API ab und aktualisieren Sie Ihre SeaTable-Tabelle mit diesem Python-Skript.'
---

{{< required-version "Enterprise" >}}

Dieses Skript ruft aktuelle Aktienkurse von der Twelve Data API ab und aktualisiert die entsprechenden Zeilen in einer SeaTable-Tabelle. Es zeigt, wie Sie externe APIs aus einem SeaTable Python-Skript aufrufen können.

## Voraussetzungen

Sie benötigen einen kostenlosen API-Schlüssel von [Twelve Data](https://twelvedata.com/) und eine Tabelle mit den Spalten `Symbol` (Text) und `Price` (Zahl).

## Das vollständige Skript

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

Sie können die Twelve Data API durch einen anderen Finanzdatenanbieter ersetzen. Passen Sie die URL und die Antwortverarbeitung entsprechend an.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
