---
title: 'JavaScript-Beispiel: Anwesenheitsstatistik berechnen'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/javascript-anwesenheitsstatistik-berechnen'
seo:
    title: 'JavaScript: Anwesenheitsstatistik in SeaTable berechnen'
    description: 'Verarbeiten Sie Stempelzeiten und erzeugen Sie tägliche Kommen-/Gehen-Statistiken pro Mitarbeiter mit diesem SeaTable JavaScript-Skript.'
---

Dieses Skript verarbeitet Zeiterfassungsdaten (Stempelzeiten) und erstellt eine tägliche Anwesenheitsstatistik. Für jeden Mitarbeiter und Tag wird der früheste Eintrag (Kommen) und der späteste Eintrag (Gehen) ermittelt und in eine Statistik-Tabelle geschrieben.

## Voraussetzungen

Sie benötigen zwei Tabellen:
- **Time records**: Enthält die Spalten `Name`, `Date` und `Time` mit den Rohdaten der Zeiterfassung.
- **Statistics**: Enthält die Spalten `Name`, `Date`, `Clock in` und `Clock out` für die Ergebnisse.

## Das vollständige Skript

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

Passen Sie die Tabellen- und Spaltennamen an Ihre Struktur an. Das Skript fügt immer neue Zeilen in die Statistik-Tabelle ein -- wenn Sie es mehrfach ausführen, sollten Sie die Statistik-Tabelle vorher leeren.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/javascript/scripting/).
