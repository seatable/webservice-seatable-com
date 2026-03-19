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

Passen Sie die Spaltennamen und Werte an Ihre Tabellenstruktur an. Das Skript kann manuell, per Schaltfläche oder per Automation gestartet werden. Mehr dazu erfahren Sie [hier]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
