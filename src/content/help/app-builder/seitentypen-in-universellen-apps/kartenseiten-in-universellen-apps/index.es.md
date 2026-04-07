---
title: 'Páginas de mapas en aplicaciones'
date: 2026-04-07
lastmod: '2026-04-07'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/es/ayuda/paginas-de-mapas-en-aplicaciones'
seo:
    title: 'Páginas de mapas en las apps: visualice las ubicaciones en un mapa'
    description: 'Cree páginas de mapas en SeaTable Apps: visualice datos de geolocalización y direcciones en un mapa del mundo.'
weight: 9
---

Puede utilizar este tipo de página para mostrar **ubicaciones** que haya guardado en su tabla utilizando **datos de geoposición o direcciones** en un **mapa mundial** dentro de la aplicación.

![visualización de ubicaciones en un mapa](images/map-page-app-builder.png)

## Configuración de la página

Si desea cambiar los ajustes de una página, haga clic en el **icono de la rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondiente de la barra de navegación.

![cambiar los ajustes de la página del mapa](images/access-page-settings.png)

En los **ajustes de la página** puede seleccionar el **tipo de mapa** (estándar o imágenes), la **tabla** y una columna para la **dirección** y el **color de la chincheta**. Tenga en cuenta que sólo se pueden utilizar determinados tipos de columnas para esta información.

![Configuración de la página del mapa en aplicaciones](images/map-page-settings.png)

Si especifica una **columna para mostrar**, los lugares se etiquetarán permanentemente en el mapa.

![Columna a visualizar en la página del mapa en apps](images/map-page-display-field.png)

Sin embargo, también puede definir columnas para mostrar de forma flexible, que sólo se harán visibles mediante un **efecto hover**. Active los controles deslizantes de las columnas que deben ser visibles al pasar el ratón por encima de una chincheta.

![efecto hover de las columnas que se mostrarán en la página del mapa](images/map-page-hover-display.gif)

## Filtros preestablecidos y columnas ocultas

También puede definir filtros preestablecidos y columnas ocultas para limitar los datos mostrados. Para filtrar, haga clic en **Añadir filtro**, seleccione la **Columna** y la **Condición** deseadas y confirme con **Enviar**.

![filtro en páginas de mapas](images/map-page-filters.png)

Oculte las columnas que no deben estar disponibles para la página de mapa utilizando el **deslizador**.

![ocultar columnas en páginas de mapas](images/hide-columns-on-map-pages.png)

{{< warning type="warning" headline="Nota importante" text="**Los filtros preestablecidos** y las columnas ocultas **no pueden ser modificados por los usuarios de la aplicación**. Por lo tanto, sólo verán las entradas filtradas que desee." />}}

## Autorizaciones de página

Para las páginas de mapa, sólo puede definir un [permiso de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) – a saber, quién tiene permiso para ver la página de mapa. Esto se debe a que **no se pueden añadir, editar o borrar filas** en las páginas de mapas.
