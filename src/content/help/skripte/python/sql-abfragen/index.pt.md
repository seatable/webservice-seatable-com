---
title: 'Exemplo Python: Analisar dados com SQL'
date: 2026-03-27
lastmod: '2026-03-27'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-consultas-sql'
seo:
    title: 'Python: Analisar dados com consultas SQL no SeaTable'
    description: 'Use consultas SQL em scripts Python do SeaTable para filtrar, agrupar e agregar dados.'
weight: 3
---

Este script mostra como executar consultas SQL no SeaTable com `base.query()`. Ao contrário de `base.list_rows()`, com SQL pode filtrar, agrupar e agregar dados de forma direcionada, sem precisar de carregar todas as linhas. O script é adequado para execução manual ou como automação.

![SQL Queries Base no SeaTable](sql-queries-base.png)

{{< dtable-download name="SQL Queries" file="/downloads/python-examples/sql-queries.dtable" text="Base com dados de exemplo e script pronto para experimentar." />}}

## Vantagens das consultas SQL

| | `base.list_rows()` | `base.query()` |
|---|---|---|
| **Filtragem** | Apenas através de filtros de vista | Cláusula WHERE |
| **Agrupamento** | Não é possível | GROUP BY |
| **Agregação** | Não é possível | SUM, COUNT, AVG, MIN, MAX |
| **Limite padrão** | 100 linhas | 100 linhas |
| **Limite máximo** | 1.000 linhas | 10.000 linhas |

## O script

O script executa várias consultas SQL contra uma tabela de encomendas e apresenta os resultados. Ajuste `TABLE` à estrutura da sua tabela.

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

## Exemplo de saída

![Saída SQL Queries](sql-queries-output.png)

## Sintaxe SQL no SeaTable

O SeaTable suporta as operações SQL mais importantes:

- **WHERE** — Filtrar com `=`, `!=`, `LIKE`, `IN`, `BETWEEN`, `IS NULL`
- **GROUP BY** — Agrupar com `SUM`, `COUNT`, `AVG`, `MIN`, `MAX`
- **ORDER BY** — Ordenar (ASC/DESC)
- **LIMIT / OFFSET** — Limitar resultados (máx. 10.000)
- **DISTINCT** — Apenas valores únicos

A referência SQL completa encontra-se no [SeaTable Developer Manual](https://developer.seatable.com/sql/select/).
