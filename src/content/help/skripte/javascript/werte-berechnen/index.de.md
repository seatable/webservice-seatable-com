---
title: 'JavaScript-Beispiel: Kumulierte Werte berechnen'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/javascript-kumulierte-werte-berechnen'
seo:
    title: 'JavaScript: Kumulierte Werte in SeaTable berechnen'
    description: 'Berechnen Sie mit diesem JavaScript-Skript kumulierte Werte über Zeilen hinweg – mit Unterstützung für gruppierte und nicht-gruppierte Ansichten.'
---

Dieses Skript berechnet kumulierte Werte (laufende Summen) über die Zeilen einer Tabelle. Für jede Zeile wird der aktuelle Wert zur Summe aller vorherigen Zeilen addiert und das Ergebnis in eine "Accumulated"-Spalte geschrieben. Gruppierte und nicht-gruppierte Ansichten werden unterstützt.

## Das vollständige Skript

```js
const tableName = 'Table1';
const viewName = 'Default View';
const valueColumn = 'Value';
const accumulatedColumn = 'Accumulated';

const table = base.getTableByName(tableName);
const view = base.getViewByName(table, viewName);

// Check if view is grouped
if (view.groupbys && view.groupbys.length > 0) {
    const groupedRows = base.getGroupedRows(table, view);
    groupedRows.forEach(group => {
        let accumulated = 0;
        group.rows.forEach(row => {
            const value = row[valueColumn] || 0;
            accumulated += value;
            base.modifyRow(table, row, {[accumulatedColumn]: accumulated});
        });
    });
} else {
    const rows = base.getRows(table, view);
    let accumulated = 0;
    rows.forEach(row => {
        const value = row[valueColumn] || 0;
        accumulated += value;
        base.modifyRow(table, row, {[accumulatedColumn]: accumulated});
    });
}

output.text('Accumulated values calculated.');
```

Passen Sie `tableName`, `viewName`, `valueColumn` und `accumulatedColumn` an Ihre Tabelle an. Bei gruppierten Ansichten wird der kumulierte Wert für jede Gruppe separat berechnet.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/javascript/scripting/).
