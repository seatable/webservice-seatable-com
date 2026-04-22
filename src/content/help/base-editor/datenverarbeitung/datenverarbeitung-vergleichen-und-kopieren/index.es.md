---
title: 'Tratamiento de datos: Comparar y copiar'
date: 2023-03-17
lastmod: '2023-11-27'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/es/ayuda/datos-comparar-copiar-seatable'
aliases:
    - '/es/ayuda/datenverarbeitung-vergleichen-und-kopieren'
seo:
    title: 'Compare y copie datos con SeaTable de forma sencilla'
    description: 'Copie valores entre tablas SeaTable automáticamente cuando existan coincidencias en los campos elegidos.'
---

Puede utilizar la función de tratamiento de datos para realizar diversas operaciones en una columna. **Comparar y copiar** es una operación con la que puede copiar los valores de una columna de una tabla a la columna de otra tabla, siempre que un determinado valor de comparación sea idéntico en ambos registros de datos.

## Puesta en marcha de la operación

![Crear una acción de tratamiento de datos](images/create-an-data-processing-action-1.jpg)

1. Abra cualquier **tabla** y haga clic en los **tres puntos** de las opciones de vista.
2. Haga clic en **Proceso de datos** y luego en **Añadir operación de proceso de** datos.
3. Asigne un **nombre** a la operación y seleccione **Comparar y copiar**.

![Denominación de la acción de tratamiento de datos y selección del tipo de operación](images/name-operation-and-select-operation-type-exmaple-copy.jpg)

5. Defina de **qué tabla** proceden los datos y **en qué tabla** desea copiarlos.
6. Establezca una o varias **condiciones** en las que dos columnas de las tablas comparadas deben tener un valor idéntico para que se realice la operación.
7. Seleccione una o varias **columnas de origen** desde las que se copiarán valores en **columnas de resultado** que también deben definirse, siempre que se cumplan las condiciones de coincidencia establecidas.

![Definición de la acción de tratamiento de datos](images/name-operation-and-define-columns-example-copy-1.png)

{{< warning  headline="Nota"  text="Con un clic en **Añadir**, puede seleccionar tantas columnas como desee para otras **condiciones** o **procesos de copia**." />}}

11. Haga clic en **Guardar para** guardar la acción y ejecutarla más tarde, o en **Ejecutar** para ejecutar la acción directamente.

La primera vez que se ejecuta con éxito, un pequeño **garrapata verde**.  
![Si la acción de tratamiento de datos se ejecuta correctamente por primera vez, aparece una marca verde](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Caso práctico

Un caso de uso concreto para esta operación de tratamiento de datos podría darse, por ejemplo, si mantiene los **datos de los** empleados de los miembros de su equipo en una tabla y desea crear las **tareas de su equipo** que aún deben completarse en una nueva tabla. Al añadir una columna con los **nombres de** los empleados responsables de las respectivas tareas, desea crear una correspondencia entre las tablas.

Posteriormente, desea que determinados datos de los empleados, que ya existen en la tabla de empleados, se copien en la tabla de tareas. Por ejemplo, es posible que también necesite allí la **dirección de correo electrónico** para poder ponerse en contacto directamente con el responsable.

Para realizar esta operación de tratamiento de datos, se necesitan **dos tablas en la misma base**. En la primera tabla se actualizan los **datos del** personal, que incluyen, entre otras cosas, las **direcciones de correo electrónico** del personal.

![Ejemplo de tabla para el mantenimiento de los datos personales de los empleados](images/example-table-employees-and-personal-data-1.png)

En la segunda tabla se introducen las **tareas pendientes**, para las que se introduce el empleado responsable correspondiente en otra columna. Además, se crea una nueva columna del tipo [correo electrónico]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}), en la que se copiarán posteriormente las direcciones de correo electrónico.

![Tabla de destino que incluye la columna de resultados antes de la ejecución de la acción de tratamiento de datos](images/table-open-tasks-before-data-processing-operation-1.png)

Para crear la operación de tratamiento de datos, siga los pasos descritos anteriormente. Para el caso de uso específico, seleccione como **condición** que el **nombre** de un empleado en la columna nombre de la tabla **empleados** debe coincidir con el nombre en la columna **responsable** de la tabla **tareas abiertas**. Este paso es esencial para que durante la operación de tratamiento de datos se copien los datos correctos de los empleados correspondientes.

![Definición de la condición de coincidencia para la acción de tratamiento de datos](images/define-condition-for-data-operation-compare-and-copy.png)

{{< warning  headline="Nota importante"  text="En esta operación de tratamiento de datos, las columnas a comparar deben tener **el mismo tipo de columna** para que SeaTable pueda reconocer con fiabilidad valores idénticos." />}}

En el siguiente paso, puede seleccionar cualquier número de columnas de origen de la tabla de **empleados**, cuyo contenido se copiará en las columnas de resultado seleccionadas de la tabla de **tareas abierta** cuando se ejecute la operación y la condición de coincidencia recién definida sea verdadera.

![Selección de las columnas de la tabla de origen cuyo contenido se copia en la tabla de destino si se cumple la condición de coincidencia.](images/select-columns-to-copy.png)

{{< warning  headline="Cuidado con la pérdida de datos" >}}

Las columnas de origen y de resultado deben tener **el mismo tipo de columna** para que no se pierdan datos al copiar. Por ejemplo, puede copiar datos de una [columna de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) en [una columna de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}), pero entonces ya no servirán para [calendarios]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}). Por lo tanto, antes de realizar la operación, cree una columna de **resultado** del mismo tipo en la tabla de destino para cada columna de **origen** que desee copiar.

{{< /warning >}}

Si la operación se ejecuta correctamente, se comprueba si las tablas **empleados** y **tareas** abiertas coinciden en las columnas definidas **nombre** y **responsable**. Si los **nombres** de las columnas de ambas tablas coinciden, la **dirección de correo electrónico** del empleado correspondiente se copia automáticamente de la columna definida **correo electrónico** a la columna resultante **contacto**.

![Contenido copiado en la tabla de destino tras activarse la acción de tratamiento de datos.](images/table-after-data-processing-operation-2.png)

{{< warning  headline="Nota"  text="Para facilitar la comprensión, en el caso de uso hemos decidido copiar sólo **una columna** mediante la operación de tratamiento de datos. Para aumentar el efecto, por supuesto también puede seleccionar un mayor número de columnas de origen y de resultado." />}}

## Tipos de columna no compatibles

Los siguientes tipos de columnas **no pueden** copiarse mediante la operación _Comparar y copiar_ y, por lo tanto, **no** están disponibles al definir las columnas de origen y de resultado.

- [Columna de selección múltiple]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}})
- [La columna Creado]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})
- [La columna del Último Editor]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})
- [Botón]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
