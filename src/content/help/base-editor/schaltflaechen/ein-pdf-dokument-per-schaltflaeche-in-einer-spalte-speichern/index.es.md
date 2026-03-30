---
title: 'Guardar un documento PDF por botón en una columna'
date: 2023-01-23
lastmod: '2023-05-04'
categories:
    - 'andere-spalten'
author: 'nsc2'
url: '/es/ayuda/guardar-pdf-en-columna-por-boton'
aliases:
    - '/es/ayuda/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern'
seo:
    title: 'Guardar PDF en columna con botón – tutorial SeaTable'
    description: 'Descubre cómo guardar PDF automáticamente en una columna de archivo usando un botón en SeaTable, con lógica condicional para idiomas.'
---

Con la ayuda de un **botón** puedes guardar documentos PDF en columnas de archivos. El requisito previo para ello es la configuración del **complemento de diseño de página** a través de las opciones básicas.

## Guardar documentos PDF mediante un botón en una columna

Los botones permiten guardar documentos PDF en las [columnas de archivo]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) de las tablas. La acción está disponible al crear un botón en cuanto haya configurado el [complemento de diseño de página]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}) en la tabla correspondiente.

En el primer paso, nombre la **columna** y establezca la **etiqueta** y el **color** del botón que quiere añadir a sus filas.

![Nombrar la línea, etiquetar y seleccionar el color del botón](images/name-button-and-select-colour.png)

A continuación, configure la acción como **"Guardar archivo PDF en columna"**.

![Seleccionar la acción: Guardar archivo PDF en columna](images/create-pdf-design-and-save-to-column.png)

A continuación, seleccione una **página** del complemento de diseño de páginas para guardarla como archivo PDF. Puede elegir entre las páginas existentes o [añadir]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}) primero una nueva.

![Selección de la página del plug-in de diseño de página que debe guardarse como PDF en la columna.](images/select-file-to-create-PDF-with.png)

{{< warning  headline="Nota importante"  text="También puede utilizar las páginas para visualizar la **información de una tabla** en forma de cartas, tarjetas de visita y boletines, entre otras cosas." />}}

Seleccione ahora la **columna de archivos** en la que desea guardar la página como PDF.

![Seleccione la columna de archivo en la que se guardará el archivo PDF.](images/select-column-to-put-PDF.png)

Por último, **asigne un nombre a** los archivos PDF que se añadirán a la tabla. Utilice **{nombre de columna}**, es decir, el nombre de una columna entre llaves, para dar al fichero el nombre del valor de esa columna.

![Nombre de los archivos](images/PDF-file-name.png)

Tras pulsar el botón, el **archivo PDF** seleccionado se añade a la línea correspondiente.

![Desencadenar la acción activando el botón](images/pdf-example.gif)

## Ejecución condicional de las acciones de los botones

Tiene la opción de definir la acción **Guardar archivo PDF en** columna **varias veces** en un botón. Para cada acción individual, puede definir una **condición** específica que debe cumplirse para que se guarde un archivo PDF en la columna al hacer clic en el botón. Además, puede seleccionar una **página** diferente del complemento de diseño de páginas para guardarla como PDF en cada acción.

![Definición de varias acciones para un botón y adición de condiciones específicas para ejecutar la acción](images/add-several-actions-and-conditions-to-button.jpg)

Con ayuda de esta función podrá, por ejemplo, guardar un documento en diferentes idiomas con un solo botón. Cree varias acciones, para cada una de las cuales seleccione una plantilla en distintos **idiomas**, y defina la condición de que, en función del idioma del cliente, se guarde la **plantilla adecuada** como PDF en la columna.

Esta sería la acción para adjuntar un documento alemán:

![Definición de diferentes plantillas en diferentes idiomas para cada acción, de forma que se guarde la plantilla adecuada en la columna en función del origen del cliente y de la condición de filtro que se aplique.](images/create-pdf-via-button-condition-1.png)

Y esta la acción para adjuntar un documento en inglés:

![Definición de diferentes plantillas en diferentes idiomas para cada acción, de forma que se guarde la plantilla adecuada en la columna en función del origen del cliente y de la condición de filtro que se aplique.](images/create-pdf-via-button-condition-2.png)
