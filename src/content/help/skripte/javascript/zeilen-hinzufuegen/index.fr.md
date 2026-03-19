---
title: 'Exemple JavaScript : Ajouter des lignes automatiquement'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/javascript-ajouter-lignes'
---

Ce script ajoute automatiquement des entrées de dépenses dans une table. Il vérifie si une entrée existe déjà pour le mois en cours avant d'en créer une nouvelle.

## How it works

The script gets the current month, checks the existing rows for duplicates, and only adds new entries if none exist yet for this month. Unlike the Python version, JavaScript scripts require that select options already exist in the column before running the script.

## The complete script

```js
// Configuration
const tableName = 'Ledger';
const viewName = 'Default View';

const today = new Date();
const year = today.getFullYear();
const month = today.getMonth();
const firstOfMonth = new Date(year, month, 1).toISOString().split('T')[0];

const table = base.getTableByName(tableName);
const view = base.getViewByName(table, viewName);
const rows = base.getRows(table, view);

// Check if office supplies entry exists this month
let officeSuppliesExists = false;
rows.forEach(row => {
    if (row['Category'] === 'Office supplies' && row['Month'] && row['Month'].startsWith(firstOfMonth)) {
        officeSuppliesExists = true;
    }
});

if (!officeSuppliesExists) {
    base.addRow(table, {
        'Category': 'Office supplies',
        'Description': 'Monthly office supplies',
        'Amount': 150,
        'Month': firstOfMonth,
        'Type': 'Expense'
    });
    output.text('Office supplies entry added.');
} else {
    output.text('Office supplies entry already exists.');
}
```

Adjust the column names (`Category`, `Description`, `Amount`, `Month`, `Type`) to match your table structure.

The script can be started manually or via a button. Learn more about execution methods [here]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/javascript/scripting/).
