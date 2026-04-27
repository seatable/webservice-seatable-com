---
title: 'Scripts Python: Preguntas frecuentes'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/python-preguntas-frecuentes'
seo:
    title: 'Scripts Python en SeaTable: Preguntas frecuentes'
    description: 'Respuestas a preguntas frecuentes sobre scripts Python en SeaTable: bibliotecas compatibles, operaciones por lotes, ejecución local y consejos de depuración.'
weight: 2
star: true
---

## ¿Cómo puedo ejecutar un script tanto localmente como en SeaTable?

Puede escribir su script de forma que funcione en ambos entornos sin cambios. El truco es comprobar si el objeto `context` está disponible:

```python
from seatable_api import Base

try:
    from seatable_api import context
    base = Base(context.api_token, context.server_url)
except:
    base = Base('your-api-token', 'https://cloud.seatable.io')

base.auth()
```

## ¿Qué bibliotecas están disponibles?

Una lista completa de todas las bibliotecas preinstaladas se encuentra en el artículo [Bibliotecas Python compatibles]({{< relref "help/skripte/python/unterstuetzte-python-bibliotheken" >}}). Allí también aprenderá cómo añadir bibliotecas personalizadas en un servidor autoalojado.

## ¿Cómo proceso más de 1.000 filas?

El método `base.list_rows()` devuelve por defecto un máximo de 1.000 filas. Para procesar más filas, utilice uno de estos enfoques:

**Opción 1: Bucle con offset**
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

**Opción 2: Consulta SQL**
```python
rows = base.query("SELECT * FROM `Table1` LIMIT 10000")
```

Las consultas SQL admiten hasta 10.000 filas por solicitud.

## ¿Cómo depuro estructuras de datos complejas?

Utilice `json.dumps()` con sangría para mostrar diccionarios y listas de forma formateada:

```python
import json
metadata = base.get_metadata()
print(json.dumps(metadata, indent=2))
```

Para la referencia completa de funciones, visite el [SeaTable Developer Manual](https://developer.seatable.com/python/).
