---
title: 'Tratamiento de datos: Comparar y enlazar'
date: 2023-03-20
lastmod: '2023-03-20'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/es/ayuda/datos-comparar-vincular-seatable'
aliases:
    - '/es/ayuda/datenverarbeitung-vergleichen-und-verknuepfen'
seo:
    title: 'Compare y vincule datos en tablas de SeaTable'
    description: 'Relacione registros de varias tablas en SeaTable automáticamente cuando los valores coincidan, sin esfuerzo manual.'
---

Mediante la función de tratamiento de datos, puede realizar diversas operaciones con una columna. **Comparar y vincular** es una operación que permite vincular registros de dos tablas diferentes si el valor de una columna de ambas tablas es idéntico.

## Puesta en marcha de la operación

![Crear una acción de tratamiento de datos](images/create-an-data-processing-action-1.jpg)

1. Abra cualquier **tabla** y haga clic en los **tres puntos** de las opciones de vista.
2. Haga clic en **Proceso de datos** y luego en **Añadir operación de proceso de** datos.
3. Asigne un **nombre** a la operación y seleccione **Comparar y vincular**.

![Denominación de la acción de tratamiento de datos y selección del tipo de operación](images/select-operation-type-example-compare-and-link.jpg)

5. Defina **dos tablas** que desee comparar y vincular, y en qué **columnas** deben coincidir los valores para que SeaTable vincule los registros.

![Definición de la acción de tratamiento de datos](images/name-and-define-data-operation-compare-and-link-1.png)

{{< warning  headline="Nota"  text="Haciendo clic en **Añadir**, puede definir **cualquier número de columnas** en las que los valores deben coincidir." />}}

9. Haga clic en **Guardar para** guardar la acción y ejecutarla más tarde, o en **Ejecutar** para ejecutar la acción directamente.

La primera vez que se ejecuta con éxito, un pequeño **garrapata verde**.  
![Si la acción de tratamiento de datos se ejecuta correctamente por primera vez, aparece una marca verde](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Caso práctico

Un caso de uso concreto de esta operación de tratamiento de datos podría darse, por ejemplo, si trabajas en el departamento de contabilidad de una empresa y registras en dos tablas por un lado las **facturas** y por otro las **transacciones** realizadas.

Aquí desea **que** se cree un enlace entre estas tablas cuando el importe de la factura en una tabla coincida con el importe de la transferencia en la otra tabla. Con la vinculación puede vincular fácilmente los registros relacionados de forma que las facturas se asignen a las transferencias y las transferencias se asignen a las facturas.

Para la implementación, primero necesita dos tablas: una tabla en la que se registren los números de factura (**Invoice Nr**) y los importes, y una tabla con los números de transacción (**Transaction Nr**) y los importes (**Amount**).

![Ejemplo de facturas de tabla](images/table-invoices.png)

![Ejemplo de transacciones de tablas](images/table-transactions.png)

{{< warning  headline="Nota importante" >}}

Con esta operación de tratamiento de datos, **no** es necesario añadir **columnas** a las tablas manualmente, ya que se crea automáticamente una [columna de enlace]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) en ambas tablas la primera vez que se ejecuta.

{{< /warning >}}

Para crear la operación de tratamiento de datos, siga los pasos descritos anteriormente. Para el caso de uso específico, seleccione las **tablas** _Transacciones_ y _Facturas_ y las _columnas_**Importe** con los importes respectivos que deben coincidir para que los registros se vinculen.

![Definición de la acción de tratamiento de datos](images/name-and-define-data-operation-compare-and-link-1.png)

Si se ejecuta correctamente, se comprueba si las tablas _Transacciones_ y _Facturas_ coinciden en las _columnas_ de importe definidas. Si los **importes** de estas columnas coinciden, se crea un **enlace** entre las dos **tablas**.

En este caso, se añade un enlace a la **transacción** correspondiente de la tabla _Transacciones_ a un lado de la **factura** correspondiente en la tabla _Facturas_.

![Añadido enlace en la tabla Facturas](images/table-invoices-after-operation.png)

Por otra parte, se añade al mismo tiempo un enlace a la **factura** correspondiente de la tabla _Facturas_ a la **transacción** correspondiente de la tabla _Transacciones_.

![Añadido enlace en la tabla de Transacciones](images/table-transactions-after-operation.png)
