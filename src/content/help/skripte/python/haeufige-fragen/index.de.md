---
title: 'Python-Skripte: Häufige Fragen'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-skripte-haeufige-fragen'
seo:
    title: 'Python-Skripte in SeaTable: Häufig gestellte Fragen'
    description: 'Antworten auf häufige Fragen zu Python-Skripten in SeaTable: unterstützte Bibliotheken, Batch-Operationen, lokale Ausführung und Debugging-Tipps.'
weight: 2
star: true
---

## Wie kann ich ein Skript sowohl lokal als auch in SeaTable ausführen?

Sie können Ihr Skript so schreiben, dass es in beiden Umgebungen ohne Änderungen funktioniert. Der Trick ist, zu prüfen, ob das `context`-Objekt verfügbar ist:

```python
from seatable_api import Base

try:
    from seatable_api import context
    base = Base(context.api_token, context.server_url)
except:
    base = Base('your-api-token', 'https://cloud.seatable.io')

base.auth()
```

## Welche Bibliotheken sind verfügbar?

Eine vollständige Liste aller vorinstallierten Bibliotheken finden Sie im Artikel [Unterstützte Python Bibliotheken]({{< relref "help/skripte/python/unterstuetzte-python-bibliotheken" >}}). Dort erfahren Sie auch, wie Sie auf einem selbst gehosteten Server eigene Bibliotheken hinzufügen können.

## Wie verarbeite ich mehr als 1.000 Zeilen?

Die Methode `base.list_rows()` liefert standardmäßig maximal 1.000 Zeilen. Für mehr Zeilen nutzen Sie einen dieser Ansätze:

**Option 1: Schleife mit Offset**
```python
all_rows = []
offset = 0
while True:
    rows = base.list_rows(TABLE_NAME, start=offset, limit=1000)
    if not rows:
        break
    all_rows.extend(rows)
    offset += 1000
```

**Option 2: SQL-Abfrage**
```python
rows = base.query("SELECT * FROM `Table1` LIMIT 10000")
```

SQL-Abfragen unterstützen bis zu 10.000 Zeilen pro Anfrage.

## Wie debugge ich komplexe Datenstrukturen?

Verwenden Sie `json.dumps()` mit Einrückung, um Dictionaries und Listen formatiert auszugeben:

```python
import json
metadata = base.get_metadata()
print(json.dumps(metadata, indent=2))
```

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/).
