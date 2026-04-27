---
title: 'Exemplo Python: Calcular estatísticas de presença'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-estatisticas-presenca'
seo:
    title: 'Python: Estatísticas de presença no SeaTable'
    description: 'Processe tempos de ponto e gere estatísticas diárias de entrada e saída por funcionário.'
---

Este script processa registos de tempo e gera estatísticas diárias de presença. Para cada funcionário e dia, determina a entrada mais cedo (chegada) e a mais tardia (saída) e escreve os resultados numa tabela de estatísticas separada.

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

# Clear statistics table to avoid duplicates on re-run
for row in base.list_rows(STATISTICS_TABLE):
    base.delete_row(STATISTICS_TABLE, row['_id'])

# Group time records by date and name
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
    print(f"{group['name']} ({group['date']}): {clock_in} - {clock_out}")

print(f"---
{len(groups)} entries created.")
```

Adjust the table and column names to match your setup. The script always appends new rows -- if you run it multiple times, clear the statistics table first to avoid duplicates.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
