---
title: 'Páginas de galería en aplicaciones de SeaTable'
date: 2023-12-04
lastmod: '2024-08-02'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/es/ayuda/paginas-galeria-apps-seatable'
aliases:
    - '/es/ayuda/galerieseiten-in-universellen-apps'
    - '/es/ayuda/paginas-galeria-apps-universales'
seo:
    title: 'Páginas de galería en SeaTable Apps: guía'
    description: 'Muestre imágenes y datos en galerías dentro de SeaTable: controle filtros, permisos y enlaces de tablas según sus necesidades.'
weight: 4
---

Puede utilizar este tipo de página para mostrar **imágenes** y otros datos que haya guardado en su hoja de cálculo en forma de **galería** dentro de una aplicación. Podría utilizar una página de galería para **perfiles claros de sus empleados**, por ejemplo.

![Representación de sus empleados en una página de galería](images/page-type-gallery-example.png)

## Configuración de página

Si desea cambiar la configuración de una página, haga clic en el **símbolo de rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondiente en la barra de navegación.

![Cambiar la configuración de la página de la galería](images/Einstellungen-der-Galerieseite-aendern.png)

En la **configuración de la página**, puede seleccionar la **tabla**, la **columna de imágenes** y la **columna de título** desde las que se alimenta la galería.

![Configuración de la página de la galería en las aplicaciones](images/Seiteneinstellungen-der-Galerieseite-in-Universellen-Apps.png)

## Filtros preestablecidos, clasificación y columnas ocultas

También puede definir filtros preestablecidos, clasificaciones y columnas ocultas para limitar y organizar los datos que se muestran a los usuarios. Para filtrar u ordenar, haga clic en **Añadir filtro** o **Añadir ordenación**, seleccione la **columna** y la **condición** deseadas y confirme con **Enviar**.

![Añadir filtro en páginas de galería](images/Add-filter-on-gallery-pages-in-Universal-Apps.png)

Los usuarios pueden ver más información sobre una ficha en la galería haciendo clic en una entrada.

![Abrir entrada en la página de la galería](images/Eintrag-auf-der-Galerieseite-oeffnen.gif)

Por lo tanto, decida qué datos deben ser **visibles** y muestre u oculte las columnas correspondientes utilizando los **controles deslizantes**.

![Ocultar columnas en páginas de galerías](images/Hide-columns-on-gallery-pages-in-Universal-Apps-1.png)

{{< warning  headline="Nota importante"  text="Los usuarios de la aplicación **no pueden cambiar** los **filtros preestablecidos**, la **ordenación** ni las **columnas ocultas**. Por tanto, solo verán las entradas filtradas en un orden fijo, como deseen." />}}

## Configuración de la columna de enlaces

En **la configuración de la columna de enlace**, puede especificar qué datos son visibles y qué operaciones están permitidas para cada tabla enlazada.

![Configuración de columnas de enlace en páginas de tablas](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Permitir añadir nuevas entradas**: Si activa este control deslizante, los usuarios podrán añadir nuevas entradas a la tabla vinculada. Puede utilizar la configuración de campos para definir qué columnas son **visibles** y qué columnas son **obligatorias**, es decir, deben rellenarse.
- **Permitir la vinculación de entradas existentes**: Si activa este control deslizante, los usuarios podrán vincular entradas existentes en la tabla vinculada. Puede utilizar los ajustes de campo para definir qué columnas son **visibles**.
- **Limitar** los enlaces a una fila como máximo: Si activa este control deslizante, los usuarios sólo podrán enlazar una fila de la tabla enlazada en las celdas de la columna de enlace.
- **Filtros preestablecidos**: si añade un filtro aquí, al enlazar las entradas sólo se mostrarán las opciones que cumplan las condiciones del filtro.
- **Activar** la función big data: Si la función big data está activada, los usuarios pueden buscar en más de 20.000 registros de datos, siempre que haya este número de entradas en la tabla vinculada.

## Autorizaciones de páginas

Puede definir las siguientes [autorizaciones de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) para las páginas de la galería:

![Autorizaciones para las páginas de la galería](images/Seitenberechtigungen-von-Galerieseiten.png)

Decida quién está autorizado a ver, añadir, editar y eliminar la página de la galería. Gracias a las opciones de autorización diferenciadas de este tipo de página, puede establecerlo con precisión.
