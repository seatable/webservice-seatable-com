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


Dieses Skript ruft aktuelle Aktienkurse von der Twelve Data API ab und schreibt die Preise in eine SeaTable-Tabelle. Es zeigt, wie Sie externe APIs aus einem SeaTable Python-Skript aufrufen können. Das Skript durchläuft alle Zeilen und eignet sich für die manuelle Ausführung oder als zeitgesteuerte Automation.

![Stock Prices in SeaTable](stock-prices.png)

{{< dtable-download name="Stock Prices" file="/downloads/python-examples/stock-prices.dtable" text="Base mit Beispieldaten und fertigem Skript zum direkten Ausprobieren." />}}

## Voraussetzungen

- Ein kostenloser API-Schlüssel von [Twelve Data](https://twelvedata.com/)
- Eine Tabelle mit den Spalten `Symbol` (Text) und `Price` (Zahl)

## Das Skript

Tragen Sie Ihren API-Schlüssel in `API_KEY` ein. Das Skript prüft, ob ein gültiger Schlüssel hinterlegt ist, und bricht bei einem API-Fehler sofort ab.

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

Sie können die Twelve Data API durch einen anderen Finanzdatenanbieter ersetzen. Passen Sie die URL und die Antwortverarbeitung entsprechend an.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
