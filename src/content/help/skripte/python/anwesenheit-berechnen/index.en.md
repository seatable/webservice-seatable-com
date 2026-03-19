---
title: 'Python example: Compute attendance statistics'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/help/python-attendance-statistics'
seo:
    title: 'Python: Compute attendance statistics in SeaTable'
    description: 'Process clocking times to generate daily clock-in and clock-out statistics per employee with this SeaTable Python script.'
---


This script processes time records and generates daily attendance statistics. For each employee and day, it determines the earliest entry (clock-in) and the latest entry (clock-out) and writes the results to a separate statistics table.

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
