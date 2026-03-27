---
title: 'Python-Beispiel: Daten auswerten mit SQL'
date: 2026-03-27
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-sql-abfragen'
seo:
    title: 'Python: Daten mit SQL-Abfragen in SeaTable auswerten'
    description: 'Nutzen Sie SQL-Abfragen in SeaTable Python-Skripten, um Daten zu filtern, zu gruppieren und zu aggregieren.'
weight: 3
---

Dieses Skript zeigt, wie Sie mit `base.query()` SQL-Abfragen in SeaTable ausführen. Im Gegensatz zu `base.list_rows()` können Sie mit SQL gezielt filtern, gruppieren und aggregieren — ohne alle Zeilen laden zu müssen. Das Skript eignet sich für die manuelle Ausführung oder als Automation.

![SQL Queries Base in SeaTable](sql-queries-base.png)

{{< dtable-download name="SQL Queries" file="/downloads/python-examples/sql-queries.dtable" text="Base mit Beispieldaten und fertigem Skript zum direkten Ausprobieren." />}}

## Vorteile von SQL-Abfragen

| | `base.list_rows()` | `base.query()` |
|---|---|---|
| **Filterung** | Nur über View-Filter | WHERE-Klausel |
| **Gruppierung** | Nicht möglich | GROUP BY |
| **Aggregation** | Nicht möglich | SUM, COUNT, AVG, MIN, MAX |
| **Standard-Limit** | 100 Zeilen | 100 Zeilen |
| **Maximales Limit** | 1.000 Zeilen | 10.000 Zeilen |

## Das Skript

Das Skript führt verschiedene SQL-Abfragen gegen eine Bestelltabelle aus und gibt die Ergebnisse aus. Passen Sie `TABLE` an Ihre Tabellenstruktur an.

```python
from seatable_api import Base, context

base = Base(context.api_token, context.server_url)
base.auth()

TABLE = "Orders"

# 1. Filter: unpaid orders
print("=== Unpaid orders ===")
rows = base.query(f"SELECT Product, Customer, Amount FROM `{TABLE}` WHERE `Paid` = false")
for row in rows:
    print(f"  {row['Product']} - {row['Customer']} - {row['Amount']}")

# 2. Aggregate: total revenue per category
print(".")
print("=== Revenue per category ===")
rows = base.query(f"SELECT Category, SUM(Amount) AS total FROM `{TABLE}` GROUP BY Category")
for row in rows:
    print(f"  {row['Category']}: {row['total']}")

# 3. Aggregate: orders per customer
print(".")
print("=== Orders per customer ===")
rows = base.query(f"SELECT Customer, COUNT(*) AS orders, SUM(Amount) AS total FROM `{TABLE}` GROUP BY Customer ORDER BY total DESC")
for row in rows:
    print(f"  {row['Customer']}: {row['orders']} orders, {row['total']} total")

# 4. Filter with date range
print(".")
print("=== Orders in March 2026 ===")
rows = base.query(f"SELECT Product, Customer, Date, Amount FROM `{TABLE}` WHERE `Date` BETWEEN '2026-03-01' AND '2026-03-31'")
for row in rows:
    print(f"  {row['Date']} - {row['Product']} ({row['Customer']}): {row['Amount']}")

# 5. Summary
print(".")
print("=== Summary ===")
rows = base.query(f"SELECT COUNT(*) AS count, SUM(Amount) AS revenue, AVG(Amount) AS avg_order FROM `{TABLE}`")
r = rows[0]
print(f"  {r['count']} orders, {r['revenue']} total revenue, {r['avg_order']:.2f} avg order value")
```

## Beispielausgabe

![SQL Queries Ausgabe](sql-queries-output.png)

## SQL-Syntax in SeaTable

SeaTable unterstützt die wichtigsten SQL-Operationen:

- **WHERE** — Filtern mit `=`, `!=`, `LIKE`, `IN`, `BETWEEN`, `IS NULL`
- **GROUP BY** — Gruppieren mit `SUM`, `COUNT`, `AVG`, `MIN`, `MAX`
- **ORDER BY** — Sortieren (ASC/DESC)
- **LIMIT / OFFSET** — Ergebnisse begrenzen (max. 10.000)
- **DISTINCT** — Nur eindeutige Werte

Die vollständige SQL-Referenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/sql/select/).
