---
title: 'Ejemplo Python: Agregar filas automáticamente'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/python-agregar-filas'
seo:
    title: 'Python: Agregar filas automáticamente en SeaTable'
    description: 'Use este script Python para agregar automáticamente entradas recurrentes en su base SeaTable con verificación de duplicados.'
---


Este script crea automáticamente entradas mensuales recurrentes en una tabla. Verifica mediante una consulta SQL si ya existen entradas para el mes actual y solo crea las que faltan. De este modo puede configurarlo como automatización programada (por ej. el 1 de cada mes) sin crear duplicados.

![Monthly Expenses in SeaTable](monthly-expenses.png)

{{< dtable-download name="Monthly Expenses" file="/downloads/python-examples/monthly-expenses.dtable" text="Base con datos de ejemplo y script listo para probar directamente." />}}

## Requisitos

La tabla necesita al menos las siguientes columnas:

- **Category** (Selección simple) — tipo de entrada
- **Description** (Texto) — descripción
- **Amount** (Número) — importe
- **Month** (Fecha) — mes de facturación
- **Type** (Selección simple) — por ej. Expense o Income

## El script

Adapte `TABLE_NAME` y las entradas en `ENTRIES` a la estructura de su tabla. Los valores de las columnas de selección simple se crean automáticamente como nuevas opciones si aún no existen.

```python
from seatable_api import Base, context, dateutils
from datetime import datetime

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Ledger"

today = datetime.today()
this_month = today.month
this_year = today.year
first_of_this_month = dateutils.date(this_year, this_month, 1)

# Define recurring monthly entries
ENTRIES = [
    {"Category": "Office supplies", "Description": "Monthly office supplies", "Amount": 150.00, "Type": "Expense"},
    {"Category": "Software licenses", "Description": "Monthly software licenses", "Amount": 500.00, "Type": "Expense"},
]

for entry in ENTRIES:
    rows = base.query(f"SELECT _id FROM `{TABLE_NAME}` WHERE `Month` = '{first_of_this_month}' AND `Category` = '{entry['Category']}'")
    if len(rows) == 0:
        entry['Month'] = first_of_this_month
        base.append_row(TABLE_NAME, entry)
        print(f"Added: {entry['Category']}")
    else:
        print(f"Skipped (already exists): {entry['Category']}")
```

Para la referencia completa de funciones, visite el [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
