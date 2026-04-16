---
title: 'Ejemplo Python: Analizar datos con SQL'
date: 2026-03-27
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/python-consultas-sql'
seo:
    title: 'Python: Analizar datos con consultas SQL en SeaTable'
    description: 'Use consultas SQL en scripts Python de SeaTable para filtrar, agrupar y agregar datos.'
weight: 3
---

Este script muestra cómo ejecutar consultas SQL en SeaTable con `base.query()`. A diferencia de `base.list_rows()`, con SQL puede filtrar, agrupar y agregar datos de forma selectiva, sin necesidad de cargar todas las filas. El script es adecuado para la ejecución manual o como automatización.

![SQL Queries Base en SeaTable](sql-queries-base.png)

{{< dtable-download name="SQL Queries" file="/downloads/python-examples/sql-queries.dtable" text="Base con datos de ejemplo y script listo para probar." />}}

## Ventajas de las consultas SQL

| | `base.list_rows()` | `base.query()` |
|---|---|---|
| **Filtrado** | Solo mediante filtros de vista | Cláusula WHERE |
| **Agrupación** | No es posible | GROUP BY |
| **Agregación** | No es posible | SUM, COUNT, AVG, MIN, MAX |
| **Límite estándar** | 100 filas | 100 filas |
| **Límite máximo** | 1.000 filas | 10.000 filas |

## El script

El script ejecuta varias consultas SQL contra una tabla de pedidos y muestra los resultados. Ajuste `TABLE` a la estructura de su tabla.

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

## Salida de ejemplo

![Salida SQL Queries](sql-queries-output.png)

## Sintaxis SQL en SeaTable

SeaTable soporta las operaciones SQL más importantes:

- **WHERE** — Filtrar con `=`, `!=`, `LIKE`, `IN`, `BETWEEN`, `IS NULL`
- **GROUP BY** — Agrupar con `SUM`, `COUNT`, `AVG`, `MIN`, `MAX`
- **ORDER BY** — Ordenar (ASC/DESC)
- **LIMIT / OFFSET** — Limitar resultados (máx. 10.000)
- **DISTINCT** — Solo valores únicos

La referencia SQL completa se encuentra en el [SeaTable Developer Manual](https://developer.seatable.com/sql/select/).
