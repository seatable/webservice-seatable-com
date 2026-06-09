---
title: 'La columna de selección múltiple'
date: 2023-03-28
lastmod: '2025-07-15'
categories:
    - 'spalten'
author: 'kgr'
url: '/es/ayuda/columna-seleccion-multiple'
aliases:
    - '/es/ayuda/die-mehrfachauswahl-spalte'
seo:
    title: 'Columna de selección múltiple en SeaTable: guía'
    description: 'Gestiona opciones, colores, exportación/importación, orden flexible y diferencias clave de la columna de selección múltiple SeaTable.'
weight: 8
---

Una columna de selección múltiple es ideal si desea asignar a las filas de una columna **varias opciones** de una lista de opciones por definir. Las opciones reciben etiquetas de colores que puede utilizar para etiquetar sus registros y hacer tablas claras, por ejemplo, [filtrando]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) por opciones específicas.

![Ejemplo de tabla con una columna de selección múltiple](images/example-table-multiple-select.png)

## Crear una columna de selección múltiple

Crear una columna de selección múltiple es un juego de niños y se hace con unos pocos clics. Para obtener información detallada, consulte [Añadir una columna]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

1. Haga clic en el **símbolo \[+\]** situado a la derecha de la última columna de la tabla.
2. Dale un **nombre** a la nueva columna.
3. Seleccione **Selección múltiple** como tipo de columna.
4. Confirme con **Enviar**.

## Similitudes con la columna de selección única

### Añadir opciones de selección múltiple

Añadir opciones a una columna de selección múltiple funciona **exactamente igual que con una columna de selección única**. Puede añadir nuevas opciones de varias maneras. Descúbralo todo en el artículo [sobre la columna de selección única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}).

### Exportar e importar opciones de selección múltiple

Puede **exportar** e **importar** las opciones de una columna de selección múltiple del mismo modo que una columna de selección única. Encontrará más información al respecto en el artículo sobre la columna de selección única.

### Colores de las opciones

Al igual que con la columna de selección única, actualmente se dispone de **24 colores** para resaltar visualmente las opciones respectivas.

![Colores de la columna de selección única](images/farben-einfachauswahl.png)

Con una [suscripción Enterprise]({{< relref "help/teamverwaltung/abonnement/abo-pakete" >}}), también tiene la opción de crear [sus propios colores]({{< relref "help/base-editor/weitere-optionen/eigene-farben-in-einer-base-hinzufuegen" >}}) para sus múltiples opciones de selección.

### Cambiar el orden de las opciones de selección múltiple

El orden de las opciones puede ajustarse del mismo modo que para una columna de selección única. Es de vital importancia si desea [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) o [agrupar]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) por la columna de selección múltiple. Esto se debe a que SeaTable **no organiza las opciones alfabéticamente**, sino de forma flexible según el **orden de las opciones**, que usted especifica mediante arrastrar y soltar.

### Fijar valor por defecto

A diferencia de la columna de selección única, usted **no puede** especificar un valor por defecto para una columna de selección múltiple.

## ¿Selección múltiple o enlace a otras entradas?

Si desea poder guardar **información adicional** para cada opción de selección, debería plantearse utilizar una [columna de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) en lugar de una columna de selección múltiple. Para ello, cree registros de datos completos para todas las opciones en una tabla adicional, que podrá vincular a cualquier número de filas de otras tablas.
