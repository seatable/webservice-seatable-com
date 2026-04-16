---
title: 'Python example: Analyze data with SQL'
date: 2026-03-27
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/help/python-sql-queries'
seo:
    title: 'Python: Analyze data with SQL queries in SeaTable'
    description: 'Use SQL queries in SeaTable Python scripts to filter, group, and aggregate data.'
weight: 3
---

This script demonstrates how to run SQL queries in SeaTable using `base.query()`. Unlike `base.list_rows()`, SQL lets you filter, group, and aggregate data without loading all rows. The script is suitable for manual execution or as an automation.

![SQL Queries Base in SeaTable](sql-queries-base.png)

{{< dtable-download name="SQL Queries" file="/downloads/python-examples/sql-queries.dtable" text="Base with sample data and ready-to-use script." />}}

## Advantages of SQL queries

| | `base.list_rows()` | `base.query()` |
|---|---|---|
| **Filtering** | Only via view filters | WHERE clause |
| **Grouping** | Not possible | GROUP BY |
| **Aggregation** | Not possible | SUM, COUNT, AVG, MIN, MAX |
| **Default limit** | 100 rows | 100 rows |
| **Maximum limit** | 1,000 rows | 10,000 rows |

## The script

The script runs various SQL queries against an orders table and prints the results. Adjust `TABLE` to match your table structure.

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

## Example output

![SQL Queries output](sql-queries-output.png)

## SQL syntax in SeaTable

SeaTable supports the most important SQL operations:

- **WHERE** — Filter with `=`, `!=`, `LIKE`, `IN`, `BETWEEN`, `IS NULL`
- **GROUP BY** — Group with `SUM`, `COUNT`, `AVG`, `MIN`, `MAX`
- **ORDER BY** — Sort (ASC/DESC)
- **LIMIT / OFFSET** — Limit results (max 10,000)
- **DISTINCT** — Unique values only

The full SQL reference can be found in the [SeaTable Developer Manual](https://developer.seatable.com/sql/select/).
