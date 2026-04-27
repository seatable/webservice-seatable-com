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
    description: 'Use this Python script to automatically add recurring entries to your SeaTable base with duplicate checking.'
---


This script automatically creates recurring monthly entries in a table. It uses an SQL query to check whether entries for the current month already exist and only creates missing ones. This way you can set it up as a scheduled automation (e.g. on the 1st of each month) without creating duplicates.

![Monthly Expenses in SeaTable](monthly-expenses.png)

{{< dtable-download name="Monthly Expenses" file="/downloads/python-examples/monthly-expenses.dtable" text="Base with sample data and ready-made script to try out directly." />}}

## Prerequisites

The table requires at least the following columns:

- **Category** (Single select) — type of entry
- **Description** (Text) — description
- **Amount** (Number) — amount
- **Month** (Date) — billing month
- **Type** (Single select) — e.g. Expense or Income

## The script

Adjust `TABLE_NAME` and the entries in `ENTRIES` to match your table structure. Values for single-select columns are automatically created as new options if they do not yet exist.

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

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
