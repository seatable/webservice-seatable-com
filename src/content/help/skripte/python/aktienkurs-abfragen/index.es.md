---
title: 'Ejemplo Python: Consultar cotizaciones bursátiles'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/python-cotizaciones-bursatiles'
seo:
    title: 'Python: Consultar cotizaciones bursátiles en SeaTable'
    description: 'Obtenga cotizaciones bursátiles actuales desde una API externa y actualice su tabla SeaTable con este script Python.'
---


Este script obtiene cotizaciones bursátiles actuales de la API Twelve Data y escribe los precios en una tabla SeaTable. Muestra cómo llamar a APIs externas desde un script Python de SeaTable. El script recorre todas las filas y es adecuado para la ejecución manual o como automatización programada.

![Stock Prices in SeaTable](stock-prices.png)

{{< dtable-download name="Stock Prices" file="/downloads/python-examples/stock-prices.dtable" text="Base con datos de ejemplo y script listo para probar directamente." />}}

## Requisitos

- Una clave API gratuita de [Twelve Data](https://twelvedata.com/)
- Una tabla con las columnas `Symbol` (texto) y `Price` (número)

## El script

Introduzca su clave API en `API_KEY`. El script verifica si se ha definido una clave válida y se detiene inmediatamente en caso de error de la API.

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

Puede reemplazar la API de Twelve Data por cualquier otro proveedor de datos financieros. Adapte la URL y el procesamiento de la respuesta en consecuencia.

Para la referencia completa de funciones, visite el [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
