---
title: 'Python example: Add rows automatically'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/help/python-auto-add-rows'
seo:
    title: 'Python: Automatically add rows to SeaTable'
    description: 'Use this Python script to automatically add recurring entries to your SeaTable base with duplicate checking, date handling and select option management.'
---


This script automatically adds monthly expense entries to a ledger table. It checks whether entries for the current month already exist and only creates new ones if needed. It also creates missing select options automatically.

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

Adjust the column names and values to match your table structure. The script can be started manually, via a button, or via automation. Learn more [here]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
