---
title: 'Python-Beispiel: PDF-Dateien zusammenführen'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/de/hilfe/python-pdf-dateien-zusammenfuehren'
seo:
    title: 'Python: PDF-Dateien in SeaTable zusammenführen'
    description: 'Führen Sie mehrere PDF-Dateien aus einer SeaTable-Zeile zu einem einzigen Dokument zusammen mit diesem Python-Skript.'
---


Dieses Skript führt mehrere PDF-Dateien aus einer Dateispalte zu einem einzigen PDF-Dokument zusammen und speichert das Ergebnis zurück in die Zeile. Nützlich für das Zusammenführen von Rechnungen, Berichten oder anderen Dokumenten.

{{< warning headline="Python Runner Version" text="Dieses Skript erfordert Python Runner Version 4.1.1 oder höher." />}}

## Das vollständige Skript

```python
from seatable_api import Base, context
import pdfmerge
from io import BytesIO
import os

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Documents"
FILES_COLUMN = "PDF Files"
RESULT_COLUMN = "Merged PDF"

rows = base.list_rows(TABLE_NAME)
for row in rows:
    files = row.get(FILES_COLUMN, [])
    if not files or len(files) < 2:
        continue
    if row.get(RESULT_COLUMN):
        continue

    # Download all PDFs
    tmp_files = []
    for i, f in enumerate(files):
        url = f if isinstance(f, str) else f.get('url', '')
        content = base.download_file(url)
        tmp_path = f"/tmp/pdf_{i}.pdf"
        with open(tmp_path, 'wb') as fh:
            fh.write(content)
        tmp_files.append(tmp_path)

    # Merge
    output_path = "/tmp/merged.pdf"
    pdfmerge.merge(tmp_files, output_path)

    # Upload
    with open(output_path, 'rb') as fh:
        info = base.upload_bytes_file("merged.pdf", fh.read())
    base.update_row(TABLE_NAME, row['_id'], {RESULT_COLUMN: [info.get('url')]})

    # Cleanup
    for f in tmp_files:
        os.remove(f)
    os.remove(output_path)

print("PDFs merged.")
```

Das Skript überspringt Zeilen, die bereits ein zusammengeführtes PDF haben oder weniger als zwei Dateien enthalten. Passen Sie die Spaltennamen an Ihre Tabellenstruktur an.

Die vollständige Funktionsreferenz finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
