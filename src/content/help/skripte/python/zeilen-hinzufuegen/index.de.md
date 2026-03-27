---
title: 'Python-Beispiel: Zeilen automatisch hinzufügen'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-zeilen-automatisch-hinzufuegen'
seo:
    title: 'Python: Automatisch Zeilen in SeaTable hinzufügen'
    description: 'Mit diesem Python-Skript fügen Sie automatisch wiederkehrende Einträge in Ihre SeaTable-Base ein – mit Duplikat-Prüfung.'
---


Dieses Skript legt automatisch wiederkehrende monatliche Einträge in einer Tabelle an. Es prüft per SQL-Abfrage, ob für den aktuellen Monat bereits Einträge existieren, und erstellt nur fehlende. So können Sie es als zeitgesteuerte Automation (z.B. am 1. jeden Monats) einrichten, ohne Duplikate zu erzeugen.

![Monthly Expenses in SeaTable](monthly-expenses.png)

{{< dtable-download name="Monthly Expenses" file="/downloads/python-examples/monthly-expenses.dtable" text="Base mit Beispieldaten und fertigem Skript zum direkten Ausprobieren." />}}

## Voraussetzungen

Die Tabelle benötigt mindestens folgende Spalten:

- **Category** (Einfachauswahl) — Art des Eintrags
- **Description** (Text) — Beschreibung
- **Amount** (Zahl) — Betrag
- **Month** (Datum) — Abrechnungsmonat
- **Type** (Einfachauswahl) — z.B. Expense oder Income

## Das Skript

Passen Sie `TABLE_NAME` und die Einträge in `ENTRIES` an Ihre Tabellenstruktur an. Die Werte für Einfachauswahl-Spalten werden automatisch als neue Optionen angelegt, falls sie noch nicht existieren.

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

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
