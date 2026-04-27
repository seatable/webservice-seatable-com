---
title: 'Пример Python: Чтение метаструктуры базы'
date: 2023-03-22
lastmod: '2023-07-25'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/ru/pomoshch/python-primer-chitat-metastrukturu-bazy'
aliases:
    - '/ru/pomoshch/python-beispiel-die-metastruktur-einer-base-auslesen'
seo:
    title: 'Пример Python: чтение метаструктуры базы SeaTable'
    description: 'Как считать метаструктуру базы SeaTable с помощью Python: готовый скрипт, структурированный вывод, обработка столбцов-ссылок.'
weight: 4
---

Эта статья знакомит вас с Python-скриптом, который выводит полную метаструктуру базы. Это полезно, например, если у вас возник вопрос о базе на [форуме сообщества](https://forum.seatable.com/) и вы хотите быстро и просто описать структуру базы без скриншотов.

![Вывод метаструктуры в SeaTable](base-metadata.png)

{{< dtable-download name="Base Metadata" file="/downloads/python-examples/base-metadata.dtable" text="База с несколькими таблицами и связями для тестирования." />}}

## Метаструктура базы

Метаструктура базы описывает таблицы, колонки и представления базы. Записи в строках в метаструктуру не входят. Следующая JSON-структура описывает сравнительно простую базу, содержащую только одну таблицу, два столбца и одно представление.

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

Такой код, конечно, нецелесообразен при обращении за помощью на форум сообщества, поэтому структура этой таблицы должна быть сведена к следующим строкам.

```bash
--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---
Table: Table1 (ID: 0000)
--> Name (text)
```

Как именно это работает, вы можете узнать из этой статьи.

{{< warning  headline="Если вы хотите узнать больше о Python"  text="В Интернете можно найти бесчисленное количество инструкций, учебников и справочных материалов по Python. Однако первым делом, конечно же, стоит обратиться к официальному [сайту Python](https://www.python.org/about/gettingstarted/), на котором также представлена коллекция [обучающих материалов для начинающих](https://wiki.python.org/moin/BeginnersGuide/Programmers)." />}}

## Код Python для считывания метаструктуры

В SeaTable для получения метаструктуры базы достаточно всего нескольких строк кода Python. В частности, нескольких строк достаточно для аутентификации и одной строки для метаструктуры.

```python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
metadata = base.get_metadata()
print(metadata)

```

Однако результат или выход метаструктуры не является удобным для пользователя.

```python
{'tables': [{'_id': '0000', 'name': 'Table1', 'columns': [{'key': '0000', 'name': 'Name', 'type': 'text', 'width': 200, 'editable': True, 'resizable': True}], 'views': [{'_id': '0000', 'name': 'Default View', 'type': 'table', 'is_locked': False, 'rows': [], 'formula_rows': {}, 'summaries': [], 'filter_conjunction': 'And', 'filters': [], 'sorts': [], 'hidden_columns': [], 'groupbys': [], 'groups': []}]}], 'version': 13, 'format_version': 9, 'scripts': [{'name': 'Untitled', 'url': '/scripts/zkon.py', '_id': 'zkon', 'type': 'Python'}]}
```

## Преобразование метаструктуры в другую форму

Переменная **метаданных** теперь хранит всю метаструктуру со всеми ее элементами в формате JSON. SeaTable и Python, конечно, предоставляют возможности для обхода этих структур и взаимодействия с ними.  
С помощью следующих строк метаструктура может быть приведена к нужному виду.

```python
print("--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---")
for table in metadata['tables']:
  print('.')
  print("Table: "+table['name']+" (ID: "+table['_id']+")")
  for column in table['columns']:
    print("  --> "+column['name']+" ("+column['type']+")")
```

Что именно здесь происходит? Во-первых, вы инструктируете Python создать все таблицы с помощью команды **for**\-петля. Далее вводится число с помощью **print** имя таблицы и ее идентификатор. Здесь же показан доступ к отдельным элементам с помощью квадратных скобок.

Повторите то же самое для колонн. Через **for**\-loop, выводятся все столбцы соответствующей таблицы.

{{< warning  headline="Отступы для заметок в Python"  text="В Python для структурирования кода используются отступы строк. Это позволяет сделать код коротким и понятным. Поэтому необходимо обращать пристальное внимание на отступы, так как они определяют, где заканчивается _цикл for_." />}}

## Добавление ссылок

Теперь вы почти у цели. Вы уже могли бы использовать эту метаструктуру, но недостатком предыдущего скрипта является то, что при связывании столбцов не очевидно, на что именно они ссылаются. Поэтому замените два последних столбца следующим кодом:

```python
  for column in table['columns']:
    link_target = ""
    if column['type'] == "link":
      link_target = " --> "+column['data']['other_table_id']
      if column['data']['other_table_id'] == table['_id']:
        link_target = " --> "+column['data']['table_id']
    print("  --> "+column['name']+" ("+column['type']+")")
```

## Полный сценарий

Весь скрипт может быть запущен непосредственно в любой базе SeaTable без каких-либо настроек. Он пригодится вам, если вы захотите описать структуру своей базы на форуме сообщества.

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
