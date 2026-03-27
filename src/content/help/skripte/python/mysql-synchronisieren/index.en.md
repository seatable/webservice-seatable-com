---
title: 'Python example: Sync MySQL data'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/help/python-sync-mysql'
seo:
    title: 'Python: Synchronize MySQL data to SeaTable'
    description: 'Synchronize data from a MySQL database to SeaTable with this Python script. Compares records and adds only new entries.'
---


This script synchronizes data from a MySQL database to a SeaTable table. It compares existing records by name and only adds entries from MySQL that don't yet exist in SeaTable -- perfect for periodic one-way syncs.

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
