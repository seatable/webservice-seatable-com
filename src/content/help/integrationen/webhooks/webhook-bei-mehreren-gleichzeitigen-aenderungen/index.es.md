---
title: 'Webhook para múltiples cambios simultáneos'
date: 2024-02-13
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/es/ayuda/webhook-cambios-simultaneos'
aliases:
    - '/es/ayuda/webhook-bei-mehreren-gleichzeitigen-aenderungen'
seo:
    title: 'Webhooks por cambios simultáneos en SeaTable'
    description: 'Descubra cómo SeaTable agrupa los webhooks en cambios simultáneos, qué significa el parámetro row_count y cómo consultar todas las filas modificadas.'

---

SeaTable suele enviar un webhook por cada cambio en una fila. Sin embargo, si una operación modifica varias filas al mismo tiempo, solo se genera un webhook con el parámetro adicional _row\_count_. Esto también se aplica a la API: una llamada a la API genera un webhook, independientemente de si modifica una o varias filas.

En el editor web, esto ocurre, por ejemplo, si copia un valor al portapapeles con {{< key "CTRL" >}}+{{< key "C" >}} y luego lo pega en varias otras filas con {{< key "CTRL" >}}+{{< key "V" >}}. Este proceso solo genera un webhook. El siguiente gráfico muestra el webhook correspondiente.

![Múltiples cambios simultáneos a través de webhook.](images/webhook_multiple_changes.jpg)

## Qué contiene el webhook

El parámetro _row\_count_ indica el número de filas afectadas. Los demás datos, como _row\_id_, _row\_name_ y _row\_data_, se refieren solo a una fila, normalmente la primera de la operación. _op\_type_ también permanece en singular, es decir, _insert\_row_, _modify\_row_ o _delete\_row_.

Actualmente no existe la opción de crear un webhook distinto para cada fila. El webhook tampoco contiene una lista de todas las filas afectadas.

## Consultar las filas modificadas después de un webhook

{{< warning headline="Los webhooks no están pensados para la sincronización" text="Si desea sincronizar datos con otro sistema, el webhook solo debe ser el desencadenante de la sincronización. No contiene todos los cambios y su entrega no está garantizada." />}}

Después del webhook, consulte las filas modificadas a través de la [interfaz SQL](https://developer.seatable.com/sql/select/):

```sql
SELECT * FROM Table1 WHERE _mtime >= '2026-11-05T18:30:00+01:00' ORDER BY _mtime, _id LIMIT 1000 OFFSET 0
```

Tenga en cuenta los siguientes puntos:

- **Comparar con `>=`:** La columna _\_mtime_ suele tener una precisión de solo un segundo. Con `>` pasaría por alto los cambios realizados en el mismo segundo que su última sincronización. Como `>=` devuelve algunas filas de nuevo, su sistema debe poder gestionar duplicados.
- **Indicar la zona horaria:** Una hora sin zona horaria no se interpreta como UTC. Por lo tanto, indique siempre el desfase, por ejemplo, `+01:00`.
- **Obtener los resultados por páginas:** Sin `LIMIT`, una consulta SQL devuelve como máximo 100 filas, y el máximo por consulta es de 10.000 filas. Aumente `OFFSET` hasta que una consulta devuelva menos filas que el `LIMIT` indicado.
- **Filas eliminadas y enlaces:** Las filas eliminadas no aparecen en esta consulta, y añadir un enlace no modifica _\_mtime_. Por lo tanto, compare de vez en cuando los ID de las filas y las columnas de enlace en ambos sistemas.

## Sincronizar además con regularidad

Los webhooks no garantizan una entrega completa: las entregas fallidas no se reintentan, un webhook puede [desactivarse tras errores]({{< relref "help/integrationen/webhooks/deaktivierung-eines-webhooks-bei-fehlern" >}}) y, en casos aislados, puede no enviarse en absoluto. Por lo tanto, ejecute también la sincronización según un calendario fijo y compruebe periódicamente que el webhook sigue activo.
