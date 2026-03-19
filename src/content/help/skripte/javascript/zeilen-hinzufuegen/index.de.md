---
title: 'JavaScript-Beispiel: Zeilen automatisch hinzufügen'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/javascript-zeilen-automatisch-hinzufuegen'
seo:
    title: 'JavaScript: Automatisch Zeilen in SeaTable hinzufügen'
    description: 'Mit diesem JavaScript-Skript fügen Sie automatisch wiederkehrende Einträge in Ihre SeaTable-Base ein – mit Duplikat-Prüfung und Datumsbehandlung.'
---

Dieses Skript fügt automatisch Ausgabeneinträge in eine Ledger-Tabelle ein. Es prüft, ob bereits ein Eintrag für den aktuellen Monat existiert, bevor ein neuer angelegt wird -- ideal für wiederkehrende monatliche Einträge wie Büromaterial oder Softwarelizenzen.

## So funktioniert es

Das Skript ermittelt den aktuellen Monat, prüft die vorhandenen Zeilen auf Duplikate und fügt nur dann neue Einträge hinzu, wenn für diesen Monat noch keine vorhanden sind. Im Gegensatz zur Python-Variante müssen bei JavaScript-Skripten die Einfachauswahl-Optionen bereits in der Spalte existieren.

## Das vollständige Skript

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

Passen Sie die Spaltennamen (`Category`, `Description`, `Amount`, `Month`, `Type`) an Ihre Tabellenstruktur an.

Das Skript kann manuell oder über eine Schaltfläche gestartet werden. Mehr zu den Ausführungsmethoden erfahren Sie [hier]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/javascript/scripting/).
