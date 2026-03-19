---
title: 'Ejemplo Python: Crear algunas entradas aleatorias'
date: 2023-03-02
lastmod: '2023-03-22'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/es/ayuda/python-entradas-aleatorias-seatable'
aliases:
  - '/es/ayuda/python-beispiel-ein-paar-zufaellige-eintraege-erstellen'
seo:
    title: 'Python: genera entradas aleatorias en SeaTable'
    description: 'Genera fácilmente múltiples filas de ejemplo en tu base SeaTable con este script Python. Acelera pruebas y prototipos con datos automáticos y opcionales.'

---


A veces quieres generar unas cuantas entradas de muestra en una base. Con este script de Python puedes generar desde unas pocas hasta muchos miles de entradas en poco tiempo.

Este artículo te guiará a través de las diferentes secciones del script para que entiendas cómo funciona y puedas adaptarlo a tus necesidades si es necesario. El script completo se encuentra al final de este artículo.

## 1) Carga de los módulos

Todo script Python comienza cargando los módulos Python utilizados, donde nosotros utilizaremos _base_ y _context_ de la clase _seatable_api_. Sólo necesitas el módulo _random_ en la segunda línea si quieres generar números aleatorios.

```python
from seatable_api import Base, context
import random
```

## 2) Autenticación

Las dos líneas siguientes son necesarias para establecer la conexión con la base actual. Después de esta autenticación, podemos leer, borrar o manipular información a través del _objeto base_.

```python
base = Base(context.api_token, context.server_url)
base.auth()
```

## 3) Definir el contenido de la nueva línea

Ahora que tenemos acceso a la tabla actual, podemos definir los registros a crear. El siguiente código asume que usted tiene columnas con los nombres _Nombre_, _único_, _aleatorio_, _calificación_. Si sus columnas tienen nombres diferentes, deberá ajustar los nombres en consecuencia.

```python
# define the data for two new rows
rows_data = [
  {
    'Name': "I am new Row",
    'single': "new",
    'random': random.randint(0,100000000),
    'rating': random.randint(0,5)
  },
  {
    'Name': "I am second new row",
    'single': "other value",
    'random': random.randint(0,100000000),
    'rating': random.randint(0,5)
  },
]
```

## 4) Escribir nuevas líneas

Con el último bloque de código, el contenido de las nuevas _filas_ estaba definido y almacenado en la variable _filas_datos_, pero aún no estaba escrito en la base. Ahora lo hacemos con la siguiente llamada.

```python
# append the two rows
  base.batch_append_rows(context.current_table, rows_data)
```

## 5) Si quieres más líneas

Por supuesto, también puede escribir más de dos líneas. Puede hacerlo simplemente definiendo contenidos de línea adicionales o haciendo que el proceso de escritura se ejecute varias veces con la ayuda de un bucle.

```python
# execute batch append 10 times
for i in range(10):

  # define the data for two new rows
  ...

  # append the two rows
  ...
```

{{< warning  headline="Nota sangrías en Python"  text="En Python, la sangría de línea se utiliza para estructurar el código. Esto mantiene el código corto y claro, pero al mismo tiempo hay que prestar mucha atención a la sangría porque determina dónde termina el _bucle for_." />}}

## El guión completo

El script completo debería estar listo para ejecutarse inmediatamente sin mayores ajustes. Cambie los nombres de las cuatro columnas y el script debería ser capaz de crear nuevas filas en su tabla.

```python
from seatable_api import Base, context
import random

base = Base(context.api_token, context.server_url)
base.auth()

# execute batch append multiple times
for i in range(10):

  # define the data for two new rows
  rows_data = [
    {
      'Name': "I am new Row",
      'single': "new",
      'random': random.randint(0,100000000),
      'rating': random.randint(0,5)
    },
    {
      'Name': "I am second new row",
      'single': "more than new",
      'random': random.randint(0,100000000),
      'rating': random.randint(0,5)
    },
  ]

  # append the two rows
  base.batch_append_rows(context.current_table, rows_data)
```

El script puede iniciarse manualmente o mediante un botón o automatización. Puede obtener más información al respecto [aquí]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).
