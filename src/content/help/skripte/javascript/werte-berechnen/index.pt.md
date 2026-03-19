---
title: 'Exemplo JavaScript: Calcular valores acumulados'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/javascript-valores-acumulados'
---

Este script calcula totais acumulados nas linhas de uma tabela. Suporta vistas agrupadas e não agrupadas.

## The complete script

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

Adjust `tableName`, `viewName`, `valueColumn` and `accumulatedColumn` to match your table. If your view is grouped, the accumulated value resets for each group.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/javascript/scripting/).
