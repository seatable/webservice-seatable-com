---
title: 'Estructura de los datos Webhook'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/es/ayuda/estructura-de-datos-del-webhook'
aliases:
  - '/es/ayuda/struktur-der-webhook-daten'
seo:
    title: 'Estructura de los datos del webhook en SeaTable – ejemplos'
    description: 'Aprende cómo SeaTable envía webhooks con formato JSON: campos, eventos de activación y ejemplos de inserción, edición o eliminación.'
---

Un webhook de SeaTable tiene una estructura claramente definida. Esto permite que el evento sea procesado fácilmente por cualquier lenguaje de programación. Este artículo presenta la estructura general y los valores posibles.

## ¿Qué cambios provoca un webhook?

Si se configura un webhook para una base, se envía una petición HTTP por cada cambio en el contenido de la base. Así, por ejemplo, los siguientes cambios activan un webhook:

- Se añade o duplica una nueva fila.
- Se borra una línea.
- Se modifica el contenido de una línea.
- Se añade o se elimina un enlace.

Si una operación modifica varias filas al mismo tiempo, solo se envía [un webhook para todas las filas]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).

{{< warning headline="Esto no activa un webhook" text="Los cambios estructurales en una base, como la adición de una nueva columna, un comentario de columna, la creación de una nueva vista o el bloqueo de una fila **, no activan un webhook**." />}}

## Ejemplos de webhooks enviados por SeaTable

### Ejemplo 1: se ha añadido una nueva fila (por ejemplo, en la interfaz web de SeaTable, a través de un formulario web o mediante una llamada a la API)

```
{
  "event": "update",
  "data": {
    "dtable_uuid": "fae0a3a42ba94df88e8303fd385e37de",
    "row_id": "Fk-i7xZGS5iA5aSvaG5HAA",
    "op_user": "4bc9a7c79c5942c5b6238413f2132bea@auth.local",
    "op_type": "insert_row",
    "op_time": 1649922777.279,
    "table_id": "9g8f",
    "table_name": "Opportunities",
    "row_name": "",
    "row_data": []
  }
}

```

En este ejemplo, la nueva fila está vacía. Si ya contiene valores, estos aparecen en _row\_data_.

### Ejemplo 2: se ha seleccionado un valor de selección única

```
{
  "event": "update",
  "data": {
    "dtable_uuid": "fae0a3a42ba94df88e8303fd385e37de",
    "row_id": "QoNno3QiTF26sxmG1sl3_g",
    "op_user": "4bc9a7c79c5942c5b6238413f2132bea@auth.local",
    "op_type": "modify_row",
    "op_time": 1649929622.589,
    "table_id": "9g8f",
    "table_name": "Opportunities",
    "row_name": "",
    "row_data": [{
      "column_key": "589r",
      "column_name": "Prio",
      "column_type": "single-select",
      "column_data": {
        "options": [{
          "name": "++",
          "color": "#F4667C",
          "textColor": "#FFFFFF",
          "id": "381992"
        },
        {
          "name": "+",
          "color": "#FBD44A",
          "textColor": "#FFFFFF",
          "id": "830278"
        }
      ]},
      "value": "381992",
      "old_value": ""
    }]
  }
}

```

### Ejemplo 3: se ha borrado una línea

```
{
  "event": "update",
  "data": {
    "dtable_uuid": "fae0a3a42ba94df88e8303fd385e37de",
    "row_id": "QoNno3QiTF26sxmG1sl3_g",
    "op_user": "4bc9a7c79c5942c5b6238413f2132bea@auth.local",
    "op_type": "delete_row",
    "op_time": 1649929650.668,
    "table_id": "9g8f",
    "table_name": "Opportunities",
    "row_name": "",
    "row_data": []
  }
}

```

### Ejemplo 4: se han modificado varias filas al mismo tiempo

```
{
  "event": "update",
  "data": {
    "dtable_uuid": "fae0a3a42ba94df88e8303fd385e37de",
    "row_id": "QoNno3QiTF26sxmG1sl3_g",
    "op_user": "4bc9a7c79c5942c5b6238413f2132bea@auth.local",
    "op_type": "modify_row",
    "op_time": 1649929700.125,
    "table_id": "9g8f",
    "table_name": "Opportunities",
    "row_count": 5,
    "row_name": "",
    "row_data": [{
      "column_key": "0000",
      "column_name": "Name",
      "column_type": "text",
      "column_data": {},
      "value": "Valor nuevo",
      "old_value": "Valor anterior"
    }]
  }
}

```

### Ejemplo 5: se ha añadido un enlace

Los enlaces tienen una estructura propia sin _row\_id_ ni _row\_data_. En su lugar, el webhook contiene los datos de las dos filas enlazadas:

```
{
  "event": "update",
  "data": {
    "dtable_uuid": "fae0a3a42ba94df88e8303fd385e37de",
    "op_user": "4bc9a7c79c5942c5b6238413f2132bea@auth.local",
    "op_type": "add_link",
    "op_time": 1649929800.512,
    "link_id": "x9Tq",
    "table1_id": "9g8f",
    "table1_name": "Opportunities",
    "table1_row_id": "QoNno3QiTF26sxmG1sl3_g",
    "table1_row_name": "",
    "table2_id": "0000",
    "table2_name": "Contactos",
    "table2_row_id": "Fk-i7xZGS5iA5aSvaG5HAA",
    "table2_row_name": "",
    "row_data1": [{ ... }],
    "row_data2": [{ ... }]
  }
}

```

## Posibles valores que puede tomar un webhook

La petición enviada por un webhook contiene siempre los valores "event" y "data". Actualmente, el valor "event" es siempre "update". En el futuro, es posible que se añadan aquí otros valores.

El valor "data" contiene un objeto con más elementos. Para los cambios en filas, estos se enumeran en la siguiente tabla:

| Valor               | Tipo                               | Ejemplo                                     |
| ------------------- | ---------------------------------- | ------------------------------------------- |
| **dtable_uuid**     | Cadena (32)                        | fae0a3a42ba94df88e8303fd385e37de            |
| **row_id**          | Cadena (22)                        | QoNno3QiTF26sxmG1sl3_g                      |
| **op_user**         | Cadena (32) + "auth.local"         | 4bc9a7c79c5942c5b6238413f2132bea@auth.local |
| **op_type**         | insert_row, delete_row, modify_row | insert_row                                  |
| **op_time**         | Marca de tiempo                    | 1649929650.668                              |
| **table_id**        | Cadena (4)                         | 9g8f                                        |
| **table_name**      | Cadena                             | Tareas                                      |
| **row_count**       | Número                             | 5                                           |
| **row_name**        | Cadena                             |                                             |
| **row_name_option** | Objeto o cadena vacía              | { "name": "++", "id": "381992", ... }       |
| **row_data**        | Array                              | [ { ... } ]                                 |
| **op_app**          | Cadena                             | Nombre del token de API                     |

El valor _row\_count_ solo se incluye si una operación se [ejecuta como operación por lotes]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}). Esto también puede ocurrir en llamadas a la API para una sola fila, en cuyo caso el valor es 1. El valor _row\_name\_option_ contiene la opción seleccionada si la primera columna de la tabla es de selección única.

En los enlaces, _op\_type_ toma los valores _add\_link_, _remove\_link_, _update\_links_ o _update\_rows\_links_. Con _update\_rows\_links_, el webhook contiene además los valores _row\_id\_list_ y _other\_rows\_ids\_map_ con las filas afectadas.

## Contenido truncado

Un webhook no contiene una copia completa de la fila, sino que trunca el contenido:

- En las filas modificadas, _row\_data_ contiene como máximo 10 columnas.
- Los textos se cortan a partir de 1.000 caracteres.
- Las listas, como los valores de una selección múltiple o las opciones de _column\_data_, se cortan a partir de 10 entradas.

Si necesita los datos completos, lea después la fila a través de la API.

Equipado con esta estructura, ahora puede desarrollar su propia interfaz Webhook.
