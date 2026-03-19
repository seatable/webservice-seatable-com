---
title: 'Python-Beispiel: Anwesenheitsstatistik berechnen'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-anwesenheitsstatistik-berechnen'
seo:
    title: 'Python: Anwesenheitsstatistik in SeaTable berechnen'
    description: 'Verarbeiten Sie Stempelzeiten und erzeugen Sie tägliche Kommen-/Gehen-Statistiken pro Mitarbeiter mit diesem SeaTable Python-Skript.'
---


Dieses Skript verarbeitet Zeiterfassungsdaten und erstellt eine tägliche Anwesenheitsstatistik. Für jeden Mitarbeiter und Tag wird der früheste Eintrag (Kommen) und der späteste Eintrag (Gehen) ermittelt und in eine separate Statistik-Tabelle geschrieben.

## Voraussetzungen

Sie benötigen zwei Tabellen:
- **Time records**: Enthält die Spalten `Name`, `Date` und `Time` mit den Rohdaten der Zeiterfassung.
- **Statistics**: Enthält die Spalten `Name`, `Date`, `Clock in` und `Clock out` für die Ergebnisse.

## Das vollständige Skript

```python
from seatable_api import Base, context

base = Base(context.api_token, context.server_url)
base.auth()

TIME_RECORDS_TABLE = "Time records"
STATISTICS_TABLE = "Statistics"

rows = base.list_rows(TIME_RECORDS_TABLE)
groups = {}
for row in rows:
    name = row.get('Name', '')
    date = row.get('Date', '')
    time = row.get('Time', '')
    if not name or not date or not time:
        continue
    key = f"{date}_{name}"
    if key not in groups:
        groups[key] = {'name': name, 'date': date, 'times': []}
    groups[key]['times'].append(time)

for key, group in groups.items():
    times = sorted(group['times'])
    clock_in = times[0]
    clock_out = times[-1]
    base.append_row(STATISTICS_TABLE, {
        'Name': group['name'],
        'Date': group['date'],
        'Clock in': clock_in,
        'Clock out': clock_out
    })
```

Passen Sie die Tabellen- und Spaltennamen an Ihre Struktur an. Das Skript fügt immer neue Zeilen hinzu -- wenn Sie es mehrfach ausführen, leeren Sie vorher die Statistik-Tabelle, um Duplikate zu vermeiden.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
