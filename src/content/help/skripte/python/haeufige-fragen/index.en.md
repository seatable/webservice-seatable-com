---
title: 'Python scripts: Common questions'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/help/python-scripts-common-questions'
seo:
    title: 'Python Scripts in SeaTable: Frequently Asked Questions'
    description: 'Answers to common questions about Python scripts in SeaTable: supported libraries, batch operations, local execution, and debugging tips.'
weight: 2
star: true
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

## Which libraries are available?

A complete list of all pre-installed libraries can be found in the article [Supported Python Libraries]({{< relref "help/skripte/python/unterstuetzte-python-bibliotheken" >}}). There you will also learn how to add custom libraries on a self-hosted server.

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

**Option 2: SQL query**
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

For the complete function reference, visit the [SeaTable Developer Manual](https://developer.seatable.com/python/).
