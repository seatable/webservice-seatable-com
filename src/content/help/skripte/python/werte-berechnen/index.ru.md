---
title: 'Пример Python: Вычисление накопленных значений'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-nakoplennye-znacheniya'
seo:
    title: 'Python: Вычисление накопленных значений в SeaTable'
    description: 'Вычисляйте накопленные значения по строкам SeaTable с помощью этого скрипта Python.'
---

Этот скрипт вычисляет накопленные итоги по строкам таблицы. Для каждой строки он прибавляет текущее значение к сумме всех предыдущих строк и записывает результат в столбец "Accumulated". Автоматически обрабатывает группированные и негруппированные представления.

## The complete script

```python
from seatable_api import Base, context

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Table1"
VIEW_NAME = "Default View"
COLUMN_CURRENT = "Value"
COLUMN_ACCUMULATED = "Accumulated"

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

    if view.get('groupbys') and len(view['groupbys']) > 0:
        # Grouped view: reset accumulated value per group
        group_col_key = view['groupbys'][0]['column_key']
        group_col_name = col_key_to_name.get(group_col_key, '')
        groups = {}
        for row in rows:
            group_val = str(row.get(group_col_name, ''))
            if group_val not in groups:
                groups[group_val] = []
            groups[group_val].append(row)
        for group_val, group_rows in groups.items():
            accumulated = 0
            for row in group_rows:
                value = row.get(COLUMN_CURRENT, 0) or 0
                accumulated += value
                base.update_row(TABLE_NAME, row['_id'], {COLUMN_ACCUMULATED: accumulated})
    else:
        # Non-grouped view
        accumulated = 0
        for row in rows:
            value = row.get(COLUMN_CURRENT, 0) or 0
            accumulated += value
            base.update_row(TABLE_NAME, row['_id'], {COLUMN_ACCUMULATED: accumulated})
```

Adjust the four variables at the top to match your table. If your view is grouped, the accumulated value resets for each group.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
