---
title: '¿Qué es una vista?'
date: 2023-01-13
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/es/ayuda/que-es-una-vista'
aliases:
    - '/es/ayuda/was-ist-eine-ansicht'
seo:
    title: '¿Qué es una vista en SeaTable?'
    description: 'Descubra qué es una vista en SeaTable y cómo usarla para mostrar y filtrar sus datos de forma personalizada.'
star: true
weight: 1
---

Siempre que visualiza sus datos en una tabla, lo hace a través de una **vista**. Incluso si ha creado una tabla completamente nueva, ya la está visualizando en la **"Vista por defecto"** suministrada de serie.

## ¿Para qué se utilizan las vistas?

En una tabla convencional, usted siempre ve los datos de la misma manera. Aunque puede añadir o eliminar filas y columnas, no puede ver los mismos datos desde distintos ángulos.

En SeaTable, puede crear vistas y **utilizar filtros, ordenar, agrupar, ocultar, resaltar con colores y ajustar la altura de las filas** para determinar qué sección de sus datos desea ver y cómo. Esto le permite visualizar exactamente los datos que son relevantes para usted sin tener que cambiar o borrar registros de datos.

También puede seleccionar determinados formatos de visualización para visualizar los datos de forma atractiva. Aquí tiene ejemplos de **tipos de vistas** que puede crear:

![tipos de vista](images/create-table-view.jpg)

- Vista de tabla
- Vista Kanban
- Vista de calendario
- Vista de galería
- Vista de línea de tiempo
- Vista de árbol
- Vista de big data

Es importante comprender que una vista no es más que otra forma de ver **los mismos datos subyacentes**. Esto significa que si edita los datos de una tabla en una vista, estos datos cambian en todas las vistas de la tabla, ya que todas las vistas representan el mismo conjunto de datos.

{{< warning type="warning" headline="Nota" >}}

Puede utilizar otros formatos de visualización como organigramas o mapas en forma de [plugins]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}}).

{{< /warning >}}

## La vista de tabla

La **vista de tabla** es el formato de visualización estándar en una base SeaTable. Es muy similar a una hoja de cálculo, ya que los registros de datos se organizan en filas y columnas.

![vista de tabla](images/table-view.jpg)

Si crea una vista filtrada u oculta columnas, sólo verá la cantidad de datos que necesite. También puede organizar la vista de forma más clara clasificando o agrupando según determinados principios de ordenación.

## La vista Kanban

Si tiene **columnas con un número limitado de opciones** en su tabla, puede resumir sus filas en grupos. Una forma especial de visualización de esto es la **vista Kanban**. Es especialmente adecuada para visualizar **procesos con distintas fases**.

![la vista Kanban](images/kanban-view.jpg)

Puede obtener más información en el artículo sobre la [vista Kanban]({{< relref "help/base-editor/ansichten/die-kanban-ansicht" >}}).

## La vista de calendario

Si tiene una tabla con **columnas de fecha**, puede crear una vista de calendario que organice todos sus registros de datos **cronológicamente**.

![la vista de calendario](images/calendar-view.jpg)

Encontrará más información al respecto en el artículo sobre la [vista de calendario]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}).

## La vista de galería

Si tiene una tabla con una **columna de imágenes**, puede crear una vista de galería para ilustrar los registros de datos con imágenes de vista previa.

![la vista de galería](images/gallery-view.jpg)

Encontrará más información al respecto en el artículo sobre la [vista de galería]({{< relref "help/base-editor/ansichten/die-galerie-ansicht" >}}).

## La vista de línea de tiempo

Si tiene una tabla con **dos columnas de fecha**, puede crear una vista de línea de tiempo que visualice distintos períodos de tiempo en una **línea cronológica**. Es especialmente adecuada para representar la secuencia de procesos o comprobar si los períodos de tiempo se **solapan** – por ejemplo en la planificación de vacaciones, los planes de proyectos o la reserva de salas.

![la vista de línea de tiempo](images/timeline-view.jpg)

Puede obtener más información en el artículo sobre la [vista de línea de tiempo]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}).

## La vista de árbol

Si tiene una base con **al menos dos tablas vinculadas**, puede crear una vista de árbol para representar los registros vinculados de forma **jerárquica**. Es especialmente adecuada para visualizar estructuras complejas como carteras de proyectos o jerarquías organizativas – con hasta tres niveles en el diagrama de árbol.

![la vista de árbol](images/tree-view.jpg)

Puede obtener más información en el artículo sobre la [vista de árbol]({{< relref "help/base-editor/ansichten/die-baum-ansicht" >}}).

## La vista de big data

Si ha activado el **almacenamiento de big data** en su Base, puede archivar **grandes cantidades de datos** que no son visibles inmediatamente para todos los usuarios. Se necesita una vista especial de big data para acceder a los datos del almacenamiento de big data.

![la vista de big data](images/create-big-data-view.jpg)

Puede encontrar más información al respecto en el artículo sobre la [vista de big data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}).

## Más artículos sobre el tema de las vistas

- [Crear una nueva vista]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}})
- [Cambiar el nombre de una vista]({{< relref "help/base-editor/ansichten/umbenennen-einer-ansicht" >}})
- [Borrar una vista]({{< relref "help/base-editor/ansichten/loeschen-einer-ansicht" >}})
- [Duplicación de vistas]({{< relref "help/base-editor/ansichten/das-duplizieren-von-ansichten" >}})
- [Diferencias entre las vistas privadas y las normales]({{< relref "help/base-editor/ansichten/unterschiede-zwischen-privaten-und-normalen-ansichten" >}})
- [Imprimir una vista]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})
- [Cambiar el orden de las vistas]({{< relref "help/base-editor/ansichten/die-reihenfolge-von-ansichten-aendern" >}})
- [Agrupar las vistas en carpetas]({{< relref "help/base-editor/ansichten/ansichten-in-ordnern-gruppieren" >}})
- [Filtrar entradas en una vista]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})
- [Vinculación de reglas de filtrado con AND y OR]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}})
- [Ordenar las entradas en una vista]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})
- [Agrupación de entradas en una vista]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})
- [Colorear las células]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}})
- [Marcación por colores de las filas]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Ajustar la altura de la fila]({{< relref "help/base-editor/ansichten/zeilenhoehe-anpassen" >}})
- [Ajustar el número de columnas fijas]({{< relref "help/base-editor/spalten/anzahl-der-fixierten-spalten-anpassen" >}})
- [Ocultar y mover columnas]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Bloquear las vistas]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Compartir una vista con un miembro del equipo]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Crear un enlace externo para una vista]({{< relref "help/startseite/freigaben/externen-link-fuer-eine-ansicht-erstellen" >}})
