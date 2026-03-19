---
title: 'Ejemplo Python: Calcular estadísticas de asistencia'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/python-estadisticas-asistencia'
seo:
    title: 'Python: Estadísticas de asistencia en SeaTable'
    description: 'Procese tiempos de fichaje y genere estadísticas diarias de entrada y salida por empleado.'
---

Este script procesa registros de tiempo y genera estadísticas diarias de asistencia. Para cada empleado y día, determina la entrada más temprana (llegada) y la más tardía (salida) y escribe los resultados en una tabla de estadísticas separada.

## Prerequisites

You need two tables:
- **Time records**: Contains columns `Name`, `Date`, and `Time` with the raw clocking data.
- **Statistics**: Contains columns `Name`, `Date`, `Clock in`, and `Clock out` for the results.

## The complete script

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

Adjust the table and column names to match your setup. The script always appends new rows -- if you run it multiple times, clear the statistics table first to avoid duplicates.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
