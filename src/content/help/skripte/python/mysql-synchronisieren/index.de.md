---
title: 'Python-Beispiel: MySQL-Daten synchronisieren'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-mysql-daten-synchronisieren'
seo:
    title: 'Python: MySQL-Daten nach SeaTable synchronisieren'
    description: 'Synchronisieren Sie Daten aus einer MySQL-Datenbank nach SeaTable mit diesem Python-Skript. Vergleicht Datensätze und fügt nur neue Einträge hinzu.'
---

{{< required-version "Enterprise" >}}

Dieses Skript synchronisiert Daten aus einer MySQL-Datenbank in eine SeaTable-Tabelle. Es vergleicht bestehende Datensätze anhand des Namens und fügt nur Einträge aus MySQL hinzu, die in SeaTable noch nicht existieren -- ideal für periodische Einweg-Synchronisierungen.

## Das vollständige Skript

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
seatable_rows = base.list_rows(TABLE_NAME)
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

{{< warning headline="Verfügbarkeit des MySQL-Connectors" text="Die `mysql.connector`-Bibliothek ist in der SeaTable Cloud Python-Umgebung verfügbar. Bei selbst gehosteten Installationen stellen Sie sicher, dass sie in Ihrem Python Runner installiert ist." />}}

Passen Sie die MySQL-Verbindungsparameter, die SQL-Abfrage und die Spaltenzuordnungen an Ihre Konfiguration an.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
