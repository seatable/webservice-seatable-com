---
title: 'Пример Python: Синхронизация данных MySQL'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-sinkhronizatsiya-mysql'
---

Этот скрипт синхронизирует данные из базы данных MySQL в таблицу SeaTable. Сравнивает существующие записи по имени и добавляет только те, которых ещё нет в SeaTable.

## The complete script

```python
from seatable_api import Base, context
import mysql.connector

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Contacts"

# MySQL connection
db = mysql.connector.connect(
    host="your-mysql-host",
    user="your-user",
    password="your-password",
    database="your-database"
)
cursor = db.cursor(dictionary=True)
cursor.execute("SELECT * FROM contacts")
mysql_rows = cursor.fetchall()

# Get existing SeaTable rows
seatable_rows = base.query(f"SELECT Name FROM `{TABLE_NAME}` LIMIT 10000")
existing_names = [row.get('Name') for row in seatable_rows]

# Add new entries
new_rows = []
for mysql_row in mysql_rows:
    if mysql_row['name'] not in existing_names:
        new_rows.append({
            'Name': mysql_row['name'],
            'Email': mysql_row['email'],
            'Phone': mysql_row.get('phone', '')
        })

if new_rows:
    base.batch_append_rows(TABLE_NAME, new_rows)
    print(f"{len(new_rows)} new rows added.")
else:
    print("No new entries found.")

cursor.close()
db.close()
```

{{< warning headline="MySQL connector availability" text="The `mysql.connector` library is available in the SeaTable Cloud Python environment. For self-hosted installations, ensure it is installed in your Python Runner." />}}

Adjust the MySQL connection parameters, SQL query, and column mappings to match your setup.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
