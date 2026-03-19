---
title: 'Скрипты Python: Частые вопросы'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-chastye-voprosy'
---

## How can I run a script both locally and in SeaTable?

You can write your script so it works in both environments without changes. The trick is to check whether the `context` object is available:

```python
from seatable_api import Base

try:
    from seatable_api import context
    base = Base(context.api_token, context.server_url)
except:
    base = Base('your-api-token', 'https://cloud.seatable.io')

base.auth()
```

## Which libraries are available in the cloud environment?

SeaTable Cloud runs Python 3.12 with the following third-party libraries pre-installed:

- **seatable-api** -- SeaTable API client
- **requests** -- HTTP requests
- **Pillow** -- Image processing
- **pandas** -- Data analysis
- **numpy** -- Numerical computing
- **scipy** -- Scientific computing
- **openai** -- OpenAI API
- **beautifulsoup4** -- HTML/XML parsing
- **python-dateutil** -- Date utilities
- **PyPDF** -- PDF processing
- **pdfmerge** -- PDF merging
- **qrcode** -- QR code generation
- **python-barcode** -- Barcode generation
- **pillow-heif** -- HEIC image support
- **ldap3** -- LDAP operations
- **markdown** -- Markdown conversion

For the complete and up-to-date list, check the [SeaTable Developer Manual](https://developer.seatable.com/python/getting-started/).

## Can I install custom libraries?

On **SeaTable Cloud**, you are limited to the pre-installed libraries listed above.

On a **self-hosted SeaTable Server**, you can install additional libraries in your Python Runner. See the [Admin Manual](https://admin.seatable.com) for details.

## How do I handle more than 1,000 rows?

The `base.list_rows()` method returns a maximum of 1,000 rows by default. To process more rows, use one of these approaches:

**Option 1: Loop with offset**
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

**Option 2: Use SQL query**
```python
rows = base.query("SELECT * FROM `Table1` LIMIT 10000")
```

SQL queries support up to 10,000 rows per request.

## How do I debug complex data structures?

Use `json.dumps()` with indentation to pretty-print dictionaries and lists:

```python
import json
metadata = base.get_metadata()
print(json.dumps(metadata, indent=2))
```

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
