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
    description: 'Mit diesem Python-Skript fügen Sie automatisch wiederkehrende Einträge in Ihre SeaTable-Base ein – mit Duplikat-Prüfung und Verwaltung von Auswahloptionen.'
---


Dieses Skript fügt automatisch monatliche Ausgabeneinträge in eine Ledger-Tabelle ein. Es prüft, ob Einträge für den aktuellen Monat bereits existieren, und legt nur dann neue an, wenn nötig. Fehlende Auswahloptionen werden dabei automatisch erstellt.

## So funktioniert es

1. Das Skript berechnet den ersten Tag des aktuellen Monats
2. Es prüft, ob Einträge für "Office supplies" und "Software licenses" bereits existieren
3. Falls eine Auswahloption noch nicht existiert, wird sie angelegt
4. Erst dann wird die neue Zeile hinzugefügt

## Das vollständige Skript

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

Passen Sie die Spaltennamen und Werte an Ihre Tabellenstruktur an. Das Skript kann manuell, per Schaltfläche oder per Automation gestartet werden. Mehr dazu erfahren Sie [hier]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
