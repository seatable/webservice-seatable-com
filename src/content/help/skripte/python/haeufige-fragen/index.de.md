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

## Welche Bibliotheken sind in der Cloud-Umgebung verfügbar?

SeaTable Cloud nutzt Python 3.12 mit folgenden vorinstallierten Drittanbieter-Bibliotheken:

- **seatable-api** -- SeaTable API-Client
- **requests** -- HTTP-Anfragen
- **Pillow** -- Bildverarbeitung
- **pandas** -- Datenanalyse
- **numpy** -- Numerische Berechnungen
- **scipy** -- Wissenschaftliche Berechnungen
- **openai** -- OpenAI API
- **beautifulsoup4** -- HTML/XML-Parsing
- **python-dateutil** -- Datums-Hilfsfunktionen
- **PyPDF** -- PDF-Verarbeitung
- **pdfmerge** -- PDF-Zusammenführung
- **qrcode** -- QR-Code-Erzeugung
- **python-barcode** -- Barcode-Erzeugung
- **pillow-heif** -- HEIC-Bildunterstützung
- **ldap3** -- LDAP-Operationen
- **markdown** -- Markdown-Konvertierung

Die vollständige und aktuelle Liste finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/getting-started/).

## Kann ich eigene Bibliotheken installieren?

In **SeaTable Cloud** sind Sie auf die oben aufgelisteten vorinstallierten Bibliotheken beschränkt.

Auf einem **selbst gehosteten SeaTable-Server** können Sie zusätzliche Bibliotheken in Ihrem Python Runner installieren. Details finden Sie im [Admin Manual](https://admin.seatable.com).

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

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
