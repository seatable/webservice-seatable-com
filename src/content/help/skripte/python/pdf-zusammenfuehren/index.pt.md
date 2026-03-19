---
title: 'Exemplo Python: Fundir ficheiros PDF'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-fundir-pdf'
---

Este script funde vários ficheiros PDF armazenados numa coluna de ficheiros num único documento PDF e guarda o resultado de volta na linha.

## The complete script

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

The script skips rows that already have a merged PDF or have fewer than two files. Adjust the column names to match your table structure.

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
