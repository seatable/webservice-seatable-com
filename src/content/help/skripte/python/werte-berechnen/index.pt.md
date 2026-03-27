---
title: 'Exemplo Python: Calcular valores acumulados'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-valores-acumulados'
seo:
    title: 'Python: Calcular totais acumulados no SeaTable'
    description: 'Calcule valores acumulados nas linhas do SeaTable com este script Python.'
---

Este script calcula totais acumulados nas linhas de uma tabela. Para cada linha, soma o valor atual à soma de todas as linhas anteriores e escreve o resultado numa coluna "Accumulated". Gere automaticamente vistas agrupadas e não agrupadas.

## The complete script

```python
from seatable_api import Base, context

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Table1"
VIEW_NAME = "Default View"
COLUMN_CURRENT = "Value"
COLUMN_ACCUMULATED = "Accumulated"

# Look up view and table metadata
metadata = base.get_metadata()
table = None
view = None
for t in metadata['tables']:
    if t['name'] == TABLE_NAME:
        table = t
        for v in t['views']:
            if v['name'] == VIEW_NAME:
                view = v
                break
        break

if not table:
    print(f"Table '{TABLE_NAME}' not found.")
elif not view:
    print(f"View '{VIEW_NAME}' not found.")
else:
    rows = base.list_rows(TABLE_NAME, view_name=VIEW_NAME)

    # Build a mapping from column key to column name
    col_key_to_name = {col['key']: col['name'] for col in table['columns']}
    updated = 0

    if view.get('groupbys') and len(view['groupbys']) > 0:
        # Grouped view: reset accumulated value per group
        group_col_key = view['groupbys'][0]['column_key']
        group_col_name = col_key_to_name.get(group_col_key, '')
        groups = {}
        for row in rows:
            group_val = row.get(group_col_name)
            if not group_val:
                continue
            group_val = str(group_val)
            if group_val not in groups:
                groups[group_val] = []
            groups[group_val].append(row)
        for group_val, group_rows in groups.items():
            accumulated = 0
            for row in group_rows:
                value = row.get(COLUMN_CURRENT, 0) or 0
                accumulated += value
                base.update_row(TABLE_NAME, row['_id'], {COLUMN_ACCUMULATED: accumulated})
                updated += 1
    else:
        # Non-grouped view
        accumulated = 0
        for row in rows:
            value = row.get(COLUMN_CURRENT, 0) or 0
            accumulated += value
            base.update_row(TABLE_NAME, row['_id'], {COLUMN_ACCUMULATED: accumulated})
            updated += 1

    print(f"{updated} rows updated.")
```

Adjust the four variables at the top to match your table. If your view is grouped, the accumulated value resets for each group.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
