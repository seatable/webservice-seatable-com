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

Este script agrega automáticamente entradas de gastos mensuales en una tabla de libro mayor. Verifica si ya existen entradas para el mes actual y solo crea nuevas si es necesario. También crea automáticamente las opciones de selección faltantes.

## How it works

1. The script calculates the first day of the current month
2. It checks if entries for "Office supplies" and "Software licenses" already exist
3. If a select option doesn't exist yet, it creates it
4. Only then does it add the new row

## The complete script

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

# Check and add office supplies
rows = base.filter("Ledger", "Month = '" + str(first_of_this_month) + "' and Category = 'Office supplies'")
if len(rows) == 0:
    options = base.list_column_options("Ledger", "Category")
    found = False
    for option in options:
        if option['name'] == 'Office supplies':
            found = True
            break
    if not found:
        base.add_column_options("Ledger", "Category", [{"name": "Office supplies", "color": "#FF8000", "textColor": "#FFFFFF"}])

    base.append_row(TABLE_NAME, {
        "Category": "Office supplies",
        "Description": "Monthly office supplies",
        "Amount": 150.00,
        "Month": first_of_this_month,
        "Type": "Expense"
    })

# Check and add software licenses
rows = base.filter("Ledger", "Month = '" + str(first_of_this_month) + "' and Category = 'Software licenses'")
if len(rows) == 0:
    base.append_row(TABLE_NAME, {
        "Category": "Software licenses",
        "Description": "Monthly software licenses",
        "Amount": 500.00,
        "Month": first_of_this_month,
        "Type": "Expense"
    })
```

Adjust the column names and values to match your table structure. The script can be started manually, via a button, or via automation. Learn more [here]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
