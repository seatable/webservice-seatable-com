---
title: 'Ejemplo Python: Lectura de la metaestructura de una base'
date: 2023-03-22
lastmod: '2023-07-25'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/ejemplo-python-leer-metadatos-base'
aliases:
    - '/es/ayuda/python-beispiel-die-metastruktur-einer-base-auslesen'
seo:
    title: 'Ejemplo Python: leer metadatos de base en SeaTable'
    description: 'Descubre cómo extraer y estructurar los metadatos de una base SeaTable con Python—script, resultados y columnas de enlace claras.'
weight: 4
---

Este artículo presenta un script en Python que muestra la metaestructura completa de una base. Esto es útil, por ejemplo, si tienes una pregunta sobre una base en el [foro de la comunidad](https://forum.seatable.com/) y quieres describir la estructura de tu base rápida y fácilmente sin capturas de pantalla.

![Salida de metaestructura en SeaTable](base-metadata.png)

{{< dtable-download name="Base Metadata" file="/downloads/python-examples/base-metadata.dtable" text="Base con varias tablas y enlaces para probar." />}}

## La metaestructura de una base

La metaestructura de una base describe las tablas, columnas y vistas de una base. Las entradas y registros de las filas no se incluyen en la metaestructura. La siguiente estructura JSON describe una base comparativamente sencilla con una sola tabla, dos columnas y una vista.

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

Por supuesto, este código es poco práctico cuando se pide ayuda en el foro de la comunidad, por lo que la estructura de esta tabla se reducirá a las siguientes líneas.

```bash
--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---
Table: Table1 (ID: 0000)
--> Name (text)
```

Descubra cómo funciona exactamente en este artículo.

{{< warning  headline="Si quiere saber más sobre Python"  text="En Internet hay innumerables instrucciones, tutoriales y ayuda sobre Python. Sin embargo, un buen primer puerto de escala es sin duda el [sitio web](https://www.python.org/about/gettingstarted/) oficial de [Python](https://www.python.org/about/gettingstarted/), que también ofrece una colección de [tutoriales para principiantes](https://wiki.python.org/moin/BeginnersGuide/Programmers)." />}}

## El código Python para leer la metaestructura

En SeaTable, sólo unas pocas líneas de código Python son suficientes para obtener la metaestructura de una base. En concreto, unas pocas líneas son suficientes para la autenticación y una línea para la metaestructura.

```
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
metadata = base.get_metadata()
print(metadata)

```

Sin embargo, el resultado o la salida de la metaestructura es cualquier cosa menos fácil de usar.

```
{'tables': [{'_id': '0000', 'name': 'Table1', 'columns': [{'key': '0000', 'name': 'Name', 'type': 'text', 'width': 200, 'editable': True, 'resizable': True}], 'views': [{'_id': '0000', 'name': 'Default View', 'type': 'table', 'is_locked': False, 'rows': [], 'formula_rows': {}, 'summaries': [], 'filter_conjunction': 'And', 'filters': [], 'sorts': [], 'hidden_columns': [], 'groupbys': [], 'groups': []}]}], 'version': 13, 'format_version': 9, 'scripts': [{'name': 'Untitled', 'url': '/scripts/zkon.py', '_id': 'zkon', 'type': 'Python'}]}
```

## Transformar la metaestructura en otra forma

Los **metadatos** variables almacenan ahora toda la metaestructura con todos sus elementos en formato JSON. SeaTable y Python ofrecen, por supuesto, posibilidades para recorrer estas estructuras e interactuar con ellas.  
Con las siguientes líneas, la metaestructura se puede poner en la forma deseada.

```
print("--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---")
for table in metadata['tables']:
  print('.')
  print("Table: "+table['name']+" (ID: "+table['_id']+")")
  for column in table['columns']:
    print("  --> "+column['name']+" ("+column['type']+")")
```

¿Qué ocurre exactamente? En primer lugar, se ordena a Python que cree todas las tablas con una directiva **for**\-bucle. A continuación, introduzca el número con **print** el nombre de la tabla y su ID. Aquí también puedes ver cómo acceder a los elementos individuales con los corchetes.

Repite lo mismo con las columnas. A través del **for**\-loop, se muestran todas las columnas de la tabla correspondiente.

{{< warning  headline="Nota sangrías en Python"  text="En Python, la sangría de línea se utiliza para estructurar el código. Esto mantiene el código corto y claro. Por lo tanto, debe prestar mucha atención a las sangrías, ya que determinan dónde termina el _bucle for_." />}}

## Adición de enlaces

Ahora ya casi está. Ya podría utilizar la metaestructura tan bien, pero un punto débil del script anterior es que con las columnas de enlace no es obvio a dónde enlazan exactamente. Por lo tanto, sustituye las dos últimas columnas por el siguiente código:

```
  for column in table['columns']:
    link_target = ""
    if column['type'] == "link":
      link_target = " --> "+column['data']['other_table_id']
      if column['data']['other_table_id'] == table['_id']:
        link_target = " --> "+column['data']['table_id']
    print("  --> "+column['name']+" ("+column['type']+")")
```

## El guión completo

El script completo puede ejecutarse directamente en cualquier base SeaTable sin necesidad de realizar ningún ajuste. Te servirá si quieres describir la estructura de tu base en el foro de la comunidad.

```
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
