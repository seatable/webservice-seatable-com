---
title: 'Páginas Kanban en aplicaciones de SeaTable'
date: 2023-12-07
lastmod: '2023-12-07'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/es/ayuda/paginas-kanban-apps-seatable'
aliases:
    - '/es/ayuda/kanbanseiten-in-universellen-apps'
    - '/es/ayuda/paginas-kanban-apps-universales'
seo:
    title: 'Páginas Kanban en SeaTable Apps: Gestiona tareas y flujos visualmente'
    description: 'Descubre cómo usar páginas Kanban en SeaTable para organizar tareas, configurar tarjetas, aplicar filtros y gestionar permisos en tus apps.'
weight: 7
---

Este tipo de página le ofrece la opción de mostrar las entradas como fichas en un **tablero Kanban**. Un caso de uso específico podría ser la **visualización de los flujos de trabajo y el progreso de los proyectos**, por ejemplo.

![Páginas Kanban en aplicaciones](images/Kanbanseiten-in-Universellen-Apps.png)

## Cambiar la configuración de la página

Si desea cambiar la configuración de una página, haga clic en el **símbolo de rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondiente en la barra de navegación.

![Cambiar la configuración de la página Kanban](images/Einstellungen-der-Kanbanseite-aendern.png)

En la **configuración de la página**, especifique en qué **tabla** se basa la tabla Kanban, por qué columna se **agrupan** las entradas y de qué columna proceden los **títulos**.

![Configuración de la página Kanban en aplicaciones](images/Seiteneinstellungen-der-Kanbanseite-in-Universellen-Apps.png)

## Filtros preestablecidos, clasificación y columnas ocultas

También puede definir filtros preestablecidos, clasificaciones y columnas ocultas para limitar y organizar los datos que se muestran a los usuarios. Para filtrar u ordenar, haga clic en **Añadir filtro** o **Añadir ordenación**, seleccione la **columna** y la **condición** deseadas y confirme con **Enviar**.

![Añadir filtro en páginas kanban](images/Add-filter-on-kanban-pages-in-Universal-Apps.png)

Los usuarios pueden ver más información sobre una entrada haciendo clic en una pestaña. Por lo tanto, decida qué datos deben ser **visibles** y muestre u oculte las columnas correspondientes utilizando los **controles deslizantes**.

![Ocultar columnas en páginas de galerías](images/Hide-columns-on-gallery-pages-in-Universal-Apps-1.png)

{{< warning  headline="Nota importante"  text="Los usuarios de la aplicación **no pueden cambiar** los **filtros preestablecidos**, la **ordenación** ni las **columnas ocultas**. Por tanto, solo verán las entradas filtradas en un orden fijo, como deseen." />}}

## Configuración de la columna de enlaces

En **la configuración de la columna de enlace**, puede especificar qué datos son visibles y qué operaciones están permitidas para cada tabla enlazada.

![Configuración de columnas de enlace en páginas de tablas](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Configuración de campos**: Aquí puede definir exactamente a qué columnas se aplican las siguientes autorizaciones.
- **Añadir y vincular nuevos registros**: Si activa este control deslizante, los usuarios podrán añadir nuevas entradas a la tabla vinculada. Puede utilizar la configuración de campos para definir qué columnas son **visibles** y qué columnas son **obligatorias**, es decir, deben rellenarse.
- **Vincular registros existentes**: Si activa este control deslizante, los usuarios podrán vincular entradas existentes en la tabla vinculada. Puede utilizar los ajustes de campo para definir qué columnas son **visibles**.
- **Limitar los enlaces a máximo un registro**: Si activa este control deslizante, los usuarios sólo podrán enlazar una fila de la tabla enlazada en las celdas de la columna de enlace.
- **Filtros preestablecidos**: si añade un filtro aquí, al enlazar las entradas sólo se mostrarán las opciones que cumplan las condiciones del filtro.
- **Activar la función de big data**: Si la función big data está activada, los usuarios pueden buscar en más de 20.000 registros de datos, siempre que haya este número de entradas en la tabla vinculada.
- **Modificar registros enlazados**: Si activa este control deslizante, los usuarios podrán editar las entradas existentes en la tabla vinculada. Puede utilizar los ajustes de campo para definir qué columnas son **editables**.

## Otros ajustes de página

Con otros tres deslizadores puede configurar SeaTable para **que no muestre filas vacías**, para que muestre los **nombres de las columnas** en las fichas y para que **ajuste el texto**.

![Otros ajustes de página para la página Kanban en aplicaciones](images/Weitere-Seiteneinstellungen-der-Kanbanseite-in-Universellen-Apps.png)

También puede mostrar otros **datos** de la tabla subyacente en las fichas: Active el número de campos que **desee visualizar**.

## Autorizaciones de páginas

Puede definir las siguientes [autorizaciones de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) para las páginas Kanban:

![Autorizaciones para las páginas de la galería](images/Seitenberechtigungen-von-Galerieseiten.png)

Decida quién está autorizado a ver la página Kanban, añadir, editar y eliminar filas. Gracias a las opciones de autorización diferenciadas de este tipo de página, puede establecerlo con precisión.
