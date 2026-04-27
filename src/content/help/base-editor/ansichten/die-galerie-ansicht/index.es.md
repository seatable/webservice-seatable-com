---
title: 'La vista de galería'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/es/ayuda/la-vista-de-galeria'
aliases:
    - '/es/ayuda/guia-plugin-galeria-seatable'
    - '/es/ayuda/anleitung-zum-galerie-plugin'
    - '/es/ayuda/anadir-nueva-fila-plugin-galeria'
    - '/es/ayuda/eine-neue-zeile-ueber-das-galerie-plugin-hinzufuegen'
seo:
    title: 'Vista de galería: Mostrar imágenes claramente en SeaTable'
    description: 'Con la vista de galería se obtiene una visión general de todos los registros de datos que contienen imágenes'
weight: 12
---

La **vista de galería** utiliza imágenes de vista previa de una [columna de imágenes]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) para organizar los registros de datos claramente en mosaicos. Varias imágenes se resumen en un **álbum**. Esta visualización es adecuada para diversos casos de uso, por ejemplo [perfiles de empleados]({{< relref "templates/human-resources/employee-directory" >}}), [bibliotecas de productos]({{< relref "templates/product-design/product-library" >}}), [listas de inventario]({{< relref "templates/operations/inventory-list" >}}) o [gestión de colecciones]({{< relref "templates/operations/art-gallery-management" >}}).

![la vista de galería](images/gallery-view.jpg)

## Cómo crear una vista de galería

1. Haga clic en el **nombre de la vista actual**.
2. Haga clic en **Añadir vista o carpeta** y seleccione el **tipo de vista** deseado.

![crear una vista de galería](images/create-gallery-view.jpg)

3. Asigne un **nombre** a la nueva vista.
4. Active el control deslizante si la nueva vista no debe ser visible para todos, sino **privada**.
5. Confirme con **Submitir**.
6. A continuación, especifique en la configuración de qué **columna de imágenes** deben proceder las imágenes. La nueva vista se genera automáticamente.
7. En el campo **Título**, introduzca la columna cuyas entradas desea utilizar como título del álbum.

![crear una vista de galería](images/create-gallery-view.gif)

## Opciones de vista

Puede utilizar las siguientes opciones en una vista de galería:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) u [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por cualquier valor
- [Compartir vista con otros]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Mostrar y ocultar información

En los **ajustes de la galería**, a los que puede acceder a través del **icono de la rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}}, puede mostrar más o menos información mostrando u ocultando columnas. Active los **deslizadores** de las respectivas columnas para mostrar más información de los registros de datos de la galería.

![mostrar información de otras columnas en la galería](images/other-fields-shown-in-gallery-view.jpg)

## Varias imágenes en un álbum

El **número de imágenes** por álbum se muestra en la galería con un **número gris**. Lógicamente, el número sólo se muestra si hay más de una imagen en un álbum.

![Número de imágenes gris](images/image-number.jpg)

Haga clic en la imagen de previsualización para abrir el álbum en modo **pantalla completa**, en el que puede ampliar y reducir las imágenes con las **lupas** y pasar de una imagen a otra con las **flechas**.

![Modo de pantalla completa en la vista de galería](images/gallery-image-preview.gif)

## Añadir un nuevo registro en la vista de galería

![Añadir un nuevo registro en la vista de galería](images/add-new-record-in-gallery-view.jpg)

Haga clic en el **círculo morado con el símbolo más** en la esquina inferior derecha. Se abrirá una nueva ventana. Cree un nuevo registro de datos en **detalles del registro** e introduzca la información y las imágenes deseadas. Los cambios se guardan automáticamente al cerrar la ventana.

## Editar registros de datos en la vista de galería

![Editar registros en vista galería](images/modify-records-in-gallery-view.jpg)

Haga clic en el **título** de un registro y se abrirá una ventana con los **detalles del registro**. Realice los ajustes que desee en el registro. Los cambios se guardan automáticamente al cerrar la ventana.