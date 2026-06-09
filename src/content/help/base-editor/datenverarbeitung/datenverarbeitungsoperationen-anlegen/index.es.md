---
title: 'Crear operaciones de tratamiento de datos'
date: 2023-03-03
lastmod: '2023-03-13'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/es/ayuda/crear-operaciones-procesamiento-datos'
aliases:
    - '/es/ayuda/datenverarbeitungsoperationen-anlegen'
seo:
    title: 'Crear operaciones de procesamiento de datos en SeaTable'
    description: 'Descubre cómo realizar operaciones matemáticas y vincular tablas en SeaTable: guía paso a paso para automatizar y comparar datos.'

---

Con la ayuda de la función de tratamiento de datos, puede realizar diversas **operaciones**. Puede realizar cálculos matemáticos en todos los valores de una columna, así como correlacionar valores cuando las entradas de dos tablas diferentes son idénticas.

Puede crear operaciones de tratamiento de datos en sus tablas en cualquier momento utilizando las opciones de vista. Basta con almacenar los resultados de una operación en una columna adicional.

## Crear una operación de tratamiento de datos

![Crear una acción de tratamiento de datos](images/create-an-data-processing-action-1.jpg)

1. Abra cualquier **tabla** para la que desee crear una operación de tratamiento de datos.
2. Haga clic en los **tres puntos** de las opciones de visualización.
3. Haga clic en **Proceso de datos** y luego en **Añadir operación de proceso de** datos.
4. Dé un **nombre** a la operación.
5. Seleccione una **operación**.
6. En función de la operación, defina la **tabla**, la **vista**, la columna de **origen** y la **columna de resultado** o las tablas y columnas que se van a comparar.
7. Haga clic en **Guardar para** guardar la operación y ejecutarla más tarde, o en **Ejecutar** para iniciar la operación directamente.

![Definición de la acción de tratamiento de datos](images/define-data-processing-action.jpg)

## Operaciones de tratamiento de datos

Actualmente están disponibles las siguientes operaciones:

- Calcular valores acumulados
- Calcular la clasificación
- Calcular los cambios
- Calcular el porcentaje
- Comparar y enlazar
- Comparar y copiar
- Transferir nombres de usuario

## Requisitos

Existen **diferentes requisitos para** crear una operación de tratamiento de datos en función de la operación.

Para los cálculos matemáticos, es decir, para las operaciones **Calcular valores acumulados**, Calcular **clasificación**, Calcular **cambios** y Calcular **porcentaje**, se necesitan al menos **dos** [columnas numéricas]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}) en la vista de tabla seleccionada. Normalmente, la **columna de origen** ya existe y se rellena con datos, mientras que la **columna de** resultado se crea y se rellena con valores mediante la operación.

Para las demás operaciones, necesitará en parte columnas de [enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}})**(comparar y enlazar** y **comparar y copiar**) o [columnas de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})**(transferir nombre de usuario**).
