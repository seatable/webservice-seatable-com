---
title: 'El botón'
date: 2023-01-07
lastmod: '2023-08-23'
categories:
    - 'andere-spalten'
author: 'nsc2'
url: '/es/ayuda/la-columna-boton'
aliases:
    - '/es/ayuda/die-schaltflaeche'
seo:
    title: 'La columna de botón en SeaTable – automatiza procesos'
    description: 'Aprende cómo la columna de botón en SeaTable permite automatizar acciones y ejecutar scripts o emails directamente desde tus filas.'
weight: 25
---

La columna de botones tiene una función similar a [las automatizaciones]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}}), en las que siempre hay que accionar los botones **manualmente**. Con la ayuda del **botón** que puede añadir a sus **filas en** esta columna, desencadena **acciones** definidas de antemano. Por esta razón, este tipo de columna es especialmente adecuado para automatizar los pasos del proceso.

## Crear el botón

En primer lugar, asigne un nombre a la **columna** y defina la **etiqueta** y el **color del botón** que desea añadir a las filas.

![Crear un botón](images/create-button-column.png)

En el paso siguiente, defina el número de **acciones** que se desencadenarán al activar el botón. Tiene la posibilidad de cambiar **varias** acciones sucesivamente.

![Panel con nueve botones de acción](images/New-button-action-modal.png)

Puedes elegir entre un total de **nueve** acciones diferentes:

- Línea de bloqueo
- Editar línea
- Copiar fila a otra tabla
- Abrir URL
- Abrir plugin (sólo es posible si ha activado al menos un [plugin]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}}) )
- Guardar archivo PDF en columna (sólo es posible si está activado el [plug-in de diseño de página]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}) )
- Enviar notificación
- Enviar correo electrónico
- Ejecutar el script

## Ejemplo de aplicación

En este ejemplo de aplicación, utilizamos el botón para asignar el estado "pagado" a las facturas pagadas con un clic del ratón. Para ello utilizamos la acción **Editar fila**.

![Selección de la acción que se desencadena al activar el botón](images/modify-row.png)

En la **configuración de la columna**, especificamos que las entradas de la columna de selección única **"estado** " pasen de **"pendiente"** a **"pagado** " al activar el botón.

![Definición del botón en el ejemplo de aplicación](images/settings-of-the-button-column-in-the-example.png)

Tras hacer clic en el botón, el **estado de** la factura seleccionada cambia a **pagada.**

![Acción desencadenada en el ejemplo de aplicación de botón](images/example-button-column.gif)

### Posibilidad adicional

Para ampliar la automatización de los pasos del proceso, también puede utilizar botones en combinación con [automatizaciones]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) las **líneas** con las facturas respectivas que se hayan configurado como pagadas para su procesamiento.

![Ejemplo de aplicación del botón en combinación con automatismos](images/use-the-button-cplumn-with-automations.gif)
