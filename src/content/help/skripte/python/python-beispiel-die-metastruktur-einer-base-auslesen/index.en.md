---
title: 'Python example: Reading the metastructure of a base'
date: 2023-03-22
lastmod: '2023-07-25'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/help/python-example-read-base-metadata'
aliases:
    - '/help/python-beispiel-die-metastruktur-einer-base-auslesen'
seo:
    title: 'Python Example: Reading SeaTable Base Metadata'
    description: 'Learn to extract and format full SeaTable base metadata with an easy Python script—structured output and link columns explained.'
weight: 4
---

This article introduces you to a Python script that outputs the complete metastructure of a base. This is useful, for example, if you have a question about a base in the [community forum](https://forum.seatable.com/) and want to describe the structure of your base easily and quickly without screenshots.

![Metadata output in SeaTable](base-metadata.png)

{{< dtable-download name="Base Metadata" file="/downloads/python-examples/base-metadata.dtable" text="Base with multiple tables and links to try out." />}}

## The metastructure of a base

The metastructure of a base describes the tables, columns and views of a base. The entries and records in the rows are not included in the metastructure. The following JSON structure describes a comparatively simple base with only one table, two columns and one view.

```json
{
    "metadata": {
        "tables": [
            {
                "_id": "0000",
                "name": "Table1",
                "columns": [
                    {
                        "key": "0000",
                        "name": "Name",
                        "type": "text",
                        "width": 200,
                        "editable": true,
                        "resizable": true
                    },
                    {
                        "key": "BydO",
                        "type": "date",
                        "name": "Date",
                        "editable": true,
                        "width": 200,
                        "resizable": true,
                        "draggable": true,
                        "data": {
                            "format": "YYYY-MM-DD"
                        },
                        "permission_type": "",
                        "permitted_users": []
                    }
                ],
                "views": [
                    {
                        "_id": "0000",
                        "name": "Default View",
                        "type": "table",
                        "is_locked": false,
                        "rows": [],
                        "formula_rows": {},
                        "summaries": [],
                        "filters": [],
                        "sorts": [],
                        "hidden_columns": [],
                        "groupbys": [],
                        "groups": []
                    }
                ]
            }
        ],
        "version": 482,
        "format_version": 7,
        "settings": {
            "securities": {
                "table_settings": {
                    "can_copy": false,
                    "can_export": false,
                    "can_print": false
                },
                "share_user_settings": {
                    "can_copy": false,
                    "can_export": false,
                    "can_print": false
                }
            }
        }
    }
}
```

This code is obviously impractical if you ask for help in the community forum, so the structure of this table should be reduced to the following rows .

```bash
--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---
Table: Table1 (ID: 0000)
--> Name (text)
```

You can find out exactly how this works in this article.

{{< warning  headline="If you want to learn more about Python"  text="On the Internet there are countless instructions, tutorials and help around Python. However, a good first place to start is definitely the official [Python website](https://www.python.org/about/gettingstarted/), which also offers a collection of [beginner tutor](https://wiki.python.org/moin/BeginnersGuide/Programmers) ials." />}}

## The Python code for reading the metastructure

In SeaTable, only a few rows of Python code are enough to get the metastructure of a base. Specifically, a few rows are enough for authentication and one row for the metastructure.

```python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
metadata = base.get_metadata()
print(metadata)
```

However, the result or the output of the metastructure is anything but user-friendly.

```python
{'tables': [{'_id': '0000', 'name': 'Table1', 'columns': [{'key': '0000', 'name': 'Name', 'type': 'text', 'width': 200, 'editable': True, 'resizable': True}], 'views': [{'_id': '0000', 'name': 'Default View', 'type': 'table', 'is_locked': False, 'rows': [], 'formula_rows': {}, 'summaries': [], 'filter_conjunction': 'And', 'filters': [], 'sorts': [], 'hidden_columns': [], 'groupbys': [], 'groups': []}]}], 'version': 13, 'format_version': 9, 'scripts': [{'name': 'Untitled', 'url': '/scripts/zkon.py', '_id': 'zkon', 'type': 'Python'}]}
```

## Putting the metastructure into a different form

The variable **metadata** now stores the entire metastructure with all its elements in JSON format. SeaTable or Python, respectively, of course offer possibilities to traverse these structures and interact with them.  
With the following rows the metastructure can be put into the desired form.

```python
print("--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---")
for table in metadata['tables']:
  print('.')
  print("Table: "+table['name']+" (ID: "+table['_id']+")")
  for column in table['columns']:
    print("  --> "+column['name']+" ("+column['type']+")")
```

What exactly happens here? First, you instruct Python to create all tables with a **for**\-loop. Next, you enter a value with **print** the name of the table and its ID. Here you can also see how to access the individual elements with the square brackets.

Repeat the same for the columns. Through the **for**\-loop, all columns of the respective table are output.

{{< warning  headline="Note indentations in Python"  text="In Python, the indentation of rows is used to structure the code. This keeps the code short and clear. Therefore, you must pay close attention to the indentations, as they determine where the _for loop_ ends." />}}

## Addition of links

Now you are almost there. You could already use the metastructure so well, but one weakness of the previous script is that when you have linking columns, it is not obvious where exactly they link to. Therefore replace the last two columns with the following code:

```python
  for column in table['columns']:
    link_target = ""
    if column['type'] == "link":
      link_target = " --> "+column['data']['other_table_id']
      if column['data']['other_table_id'] == table['_id']:
        link_target = " --> "+column['data']['table_id']
    print("  --> "+column['name']+" ("+column['type']+")")
```

## The complete script

The complete script is immediately executable in any SeaTable base without any adjustments. It will serve you well if you want to describe the structure of your base in the community forum.

```python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()

metadata = base.get_metadata()

print("--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---")
for table in metadata['tables']:
  print('.')
  print("Table: "+table['name']+" (ID: "+table['_id']+")")
  for column in table['columns']:
    link_target = ""
    if column['type'] == "link":
      link_target = " --> "+column['data']['other_table_id']
      if column['data']['other_table_id'] == table['_id']:
        link_target = " --> "+column['data']['table_id']
    print("  --> "+column['name']+" ("+column['type']+link_target+")")
```
