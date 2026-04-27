---
title: 'Exemple Python : Analyser des données avec SQL'
date: 2026-03-27
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/python-requetes-sql'
seo:
    title: 'Python : Analyser des données avec des requêtes SQL dans SeaTable'
    description: 'Utilisez des requêtes SQL dans les scripts Python de SeaTable pour filtrer, grouper et agréger des données.'
weight: 3
---

Ce script montre comment exécuter des requêtes SQL dans SeaTable avec `base.query()`. Contrairement à `base.list_rows()`, SQL vous permet de filtrer, grouper et agréger les données de manière ciblée, sans avoir à charger toutes les lignes. Le script convient à l'exécution manuelle ou en tant qu'automation.

![SQL Queries Base dans SeaTable](sql-queries-base.png)

{{< dtable-download name="SQL Queries" file="/downloads/python-examples/sql-queries.dtable" text="Base avec données d'exemple et script prêt à l'emploi." />}}

## Avantages des requêtes SQL

| | `base.list_rows()` | `base.query()` |
|---|---|---|
| **Filtrage** | Uniquement via les filtres de vue | Clause WHERE |
| **Regroupement** | Pas possible | GROUP BY |
| **Agrégation** | Pas possible | SUM, COUNT, AVG, MIN, MAX |
| **Limite standard** | 100 lignes | 100 lignes |
| **Limite maximale** | 1 000 lignes | 10 000 lignes |

## Le script

Le script exécute différentes requêtes SQL sur une table de commandes et affiche les résultats. Adaptez `TABLE` à la structure de votre table.

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

## Exemple de sortie

![Sortie SQL Queries](sql-queries-output.png)

## Syntaxe SQL dans SeaTable

SeaTable prend en charge les opérations SQL les plus importantes :

- **WHERE** — Filtrer avec `=`, `!=`, `LIKE`, `IN`, `BETWEEN`, `IS NULL`
- **GROUP BY** — Grouper avec `SUM`, `COUNT`, `AVG`, `MIN`, `MAX`
- **ORDER BY** — Trier (ASC/DESC)
- **LIMIT / OFFSET** — Limiter les résultats (max. 10 000)
- **DISTINCT** — Valeurs uniques uniquement

La référence SQL complète se trouve dans le [SeaTable Developer Manual](https://developer.seatable.com/sql/select/).
