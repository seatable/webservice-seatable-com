---
title: 'Python-Beispiel: Kumulierte Werte berechnen'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-kumulierte-werte-berechnen'
seo:
    title: 'Python: Kumulierte Werte in SeaTable berechnen'
    description: 'Berechnen Sie mit diesem Python-Skript kumulierte Werte über Zeilen hinweg – mit Unterstützung für gruppierte und nicht-gruppierte Ansichten.'
---

{{< required-version "Enterprise" >}}

Dieses Skript berechnet kumulierte Werte (laufende Summen) über die Zeilen einer Tabelle. Für jede Zeile wird der aktuelle Wert zur Summe aller vorherigen Zeilen addiert und das Ergebnis in eine "Accumulated"-Spalte geschrieben. Gruppierte und nicht-gruppierte Ansichten werden automatisch behandelt.

## Das vollständige Skript

```python
from seatable_api import Base, context

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Table1"
VIEW_NAME = "Default View"
COLUMN_CURRENT = "Value"
COLUMN_ACCUMULATED = "Accumulated"

metadata = base.get_metadata()
table = None
view = None
for t in metadata['tables']:
    if t['name'] == TABLE_NAME:
        table = t
        for v in t['views']:
            if v['name'] == VIEW_NAME:
                view = v
                break
        break

if view.get('groupbys') and len(view['groupbys']) > 0:
    # Grouped view: reset accumulated value per group
    rows = base.list_rows(TABLE_NAME, view_name=VIEW_NAME)
    groups = {}
    group_col = view['groupbys'][0]['column_key']
    for row in rows:
        group_val = str(row.get(group_col, ''))
        if group_val not in groups:
            groups[group_val] = []
        groups[group_val].append(row)
    for group_val, group_rows in groups.items():
        accumulated = 0
        for row in group_rows:
            value = row.get(COLUMN_CURRENT, 0) or 0
            accumulated += value
            base.update_row(TABLE_NAME, row['_id'], {COLUMN_ACCUMULATED: accumulated})
else:
    # Non-grouped view
    rows = base.list_rows(TABLE_NAME, view_name=VIEW_NAME)
    accumulated = 0
    for row in rows:
        value = row.get(COLUMN_CURRENT, 0) or 0
        accumulated += value
        base.update_row(TABLE_NAME, row['_id'], {COLUMN_ACCUMULATED: accumulated})
```

Passen Sie die vier Variablen am Anfang an Ihre Tabelle an. Bei gruppierten Ansichten wird der kumulierte Wert für jede Gruppe separat berechnet.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
