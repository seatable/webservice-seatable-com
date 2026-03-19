---
title: 'Ejemplo JavaScript: Calcular estadísticas de asistencia'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/javascript-estadisticas-asistencia'
---

Este script procesa registros de tiempo y genera estadísticas diarias de asistencia con tiempos de entrada y salida por empleado.

## Prerequisites

You need two tables:
- **Time records**: Contains columns `Name`, `Date`, and `Time` with the raw clocking data.
- **Statistics**: Contains columns `Name`, `Date`, `Clock in`, and `Clock out` for the results.

## The complete script

```js
const timeRecordsTable = base.getTableByName('Time records');
const statisticsTable = base.getTableByName('Statistics');
const view = base.getViewByName(timeRecordsTable, 'Default View');
const rows = base.getRows(timeRecordsTable, view);

// Group by date and name
const groups = {};
rows.forEach(row => {
    const name = row['Name'] || '';
    const date = row['Date'] || '';
    const time = row['Time'] || '';
    if (!name || !date || !time) return;

    const key = date + '_' + name;
    if (!groups[key]) {
        groups[key] = {name: name, date: date, times: []};
    }
    groups[key].times.push(time);
});

// Create statistics entries
Object.keys(groups).forEach(key => {
    const group = groups[key];
    const sortedTimes = group.times.sort();
    const clockIn = sortedTimes[0];
    const clockOut = sortedTimes[sortedTimes.length - 1];

    base.addRow(statisticsTable, {
        'Name': group.name,
        'Date': group.date,
        'Clock in': clockIn,
        'Clock out': clockOut
    });
});

output.text('Attendance statistics computed.');
```

Adjust the table and column names to match your setup. The script always appends new rows to the statistics table -- if you run it multiple times, you may want to clear the statistics table first.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/javascript/scripting/).
