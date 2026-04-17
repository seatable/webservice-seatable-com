---
title: 'Agrupar, ordenar y filtrar'
date: 2022-08-25
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'cdb'
url: '/es/ayuda/agrupar-ordenar-filtrar'
aliases:
    - '/es/ayuda/gruppierung-sortierung-und-filter'
seo:
    title: 'Agrupar, ordenar y filtrar datos en SeaTable fácilmente '
    description: 'Descubra cómo agrupar, ordenar y filtrar sus datos en SeaTable. Organice sus tablas y encuentre la información que necesita con simples clics.'
weight: 20
---

SeaTable ofrece varios métodos para analizar y preparar los datos. **Los filtros, la ordenación y la agrupación** son herramientas sencillas con las que puede estructurar sus datos en unos pocos clics y obtener rápidamente la información deseada. Utilizados correctamente, los filtros, la ordenación y la agrupación ofrecen una amplia gama de opciones de análisis.

Los registros de datos se filtran, ordenan y agrupan mediante **reglas**. Una regla consta siempre de una instrucción y de la columna a la que se aplica. En el caso de la ordenación y la agrupación, la instrucción es el orden (ascendente o descendente) en el que se listan los registros de datos, independientemente del tipo de columna. Una instrucción de filtro tiene otros componentes que dependen del tipo de columna.

¿Suena complicado? En absoluto: ¡agrupar, ordenar y filtrar es un juego de niños en SeaTable!

## Agrupación

La función de agrupación le permite **agrupar las filas de una tabla en grupos** y calcular estadísticas descriptivas sencillas como el número de filas de un grupo o la suma y el valor medio de columnas basadas en números. La agrupación se realiza utilizando **valores idénticos en la columna seleccionada para la agrupación**. Por ejemplo, organice las tareas de su equipo agrupando las tareas pendientes de cada miembro del equipo utilizando la columna de empleados.

Si desea visualizar sus datos de forma aún más precisa, utilice **agrupaciones anidadas**. Puede seleccionar hasta tres características de agrupación para crear agrupaciones subordinadas. Por ejemplo, puede agrupar las tareas primero por la persona responsable, luego por prioridad y después por fecha. Esto abre nuevas posibilidades para estructurar los datos.

[Más información sobre la función de agrupación aquí]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})

## Ordenación

Puede utilizar la función de ordenación para mostrar las entradas desordenadas de una tabla **en una secuencia ordenada**.

Cree una regla para ordenar los registros de datos en orden ascendente o descendente según los valores de una columna. También se pueden utilizar **varias reglas de ordenación** para registros de datos de gran tamaño. Si se utilizan varias reglas de ordenación, las filas se ordenan primero según la primera regla. Las filas con valores idénticos según la primera regla de ordenación se ordenan a continuación según la segunda regla.

[Más información sobre la función de ordenación aquí]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})

## Filtro

Con la función de filtrado de SeaTable, puede utilizar reglas de filtrado para **filtrar** determinados registros de datos de una tabla y mostrar sólo las filas que cumplan un criterio o criterios deseados. Esto le permite reducir las filas de la vista al mínimo que necesite y mantener siempre una visión de conjunto.

A diferencia de las reglas de agrupación y ordenación, la instrucción de las reglas de filtrado suele constar de dos componentes:
- **Criterio de filtrado**: Relación entre la columna filtrada y el valor del filtro (por ejemplo, "es", "contiene", "está vacío")
- **Valor del filtro**: El valor por el que se va a filtrar (por ejemplo, "123", "hecho")

Las reglas de filtrado también pueden vincularse con los dos operadores booleanos AND y OR. Con un enlace **AND**, sólo se muestran las entradas que cumplen todas las condiciones definidas. Con el enlace **OR** se puede filtrar la vista de forma que se muestren todas las filas que cumplan al menos una de las condiciones definidas. Los operadores AND y OR también pueden utilizarse conjuntamente utilizando **grupos de filtros**.

[Más información sobre la función de filtro aquí]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})

## Bloqueo de los ajustes de filtrado, ordenación y agrupación

Los ajustes que haya realizado con los filtros, la agrupación y la clasificación siempre se guardan en la vista actual. Si desea guardarlos para utilizarlos en el futuro, puede [bloquear la vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}}) para que nadie pueda cambiar la vista.

{{< warning headline="Nota importante" text="Con los filtros, agrupaciones y ordenaciones, ¡sólo cambia cómo se muestran los datos en su vista! La base de datos permanece inalterada. Por lo tanto, si han desaparecido registros de datos, compruebe si se encuentra en la vista correcta o si ha ocultado registros de datos con un filtro." />}}

## Diferencias según el tipo de vista

No todos los [tipos de vista]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) permiten agrupar, ordenar y filtrar de la misma manera. Obtenga una visión general con la ayuda de esta tabla:

| Tipo de vista | Filtrar | Ordenar | Agrupar |
| ------------------ | ------------------------------ | ------------------------------ | -------------------------- |
| **Tabla** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Kanban** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Calendario** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Galería** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Línea de tiempo** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| **Árbol** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}  |
| **Big Data** | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |