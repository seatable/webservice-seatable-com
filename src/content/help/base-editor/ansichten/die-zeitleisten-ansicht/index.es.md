---
title: 'La vista de la línea de tiempo'
date: 2026-03-31
lastmod: '2026-03-31'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/es/ayuda/la-vista-linea-de-tiempo'
seo:
    title: 'Vista de la línea de tiempo: Visualice periodos de tiempo en SeaTable'
    description: 'La vista de la línea de tiempo le ofrece una visión clara de los periodos de tiempo y sus solapamientos.'
weight: 15
---

La vista **Línea de tiempo** le permite visualizar diferentes lapsos de tiempo en una línea de tiempo. Esto resulta muy útil, por ejemplo, si desea visualizar la secuencia de procesos o ver si los periodos de tiempo **se solapan**. Así, puede utilizar la vista de línea de tiempo para la [planificación de vacaciones]({{< relref "templates/human-resources/holiday-request-management" >}}), [planes de proyecto]({{< relref "templates/projects/project-plan" >}}) o la reserva de salas de conferencias, entre otras cosas.

![la vista de la línea de tiempo](images/timeline-view.jpg)

{{< warning type="warning" headline="Requisitos" >}}

Este tipo de vista muestra **tramos de tiempo**. Por lo tanto, necesita **dos** [columnas de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) en una tabla que definan el **inicio** y el **final** de los periodos de tiempo. El resultado es un **gráfico Gantt**.

{{< /warning >}}

## Crear una vista de la línea de tiempo

1. Haga clic en el **nombre de la vista actual**.
2. Haga clic en **Añadir vista o carpeta** y seleccione el **Tipo de vista** deseado.

![crear una vista de línea de tiempo](images/create-timeline-view.png)

3. Asigne un **nombre** a la nueva vista.
4. Active el control deslizante si la nueva vista no debe ser visible para todos sino **privada**.
5. Confirme con **Submitir**.
6. A continuación, especifique la **fecha de inicio y de finalización** en los ajustes y el **periodo de tiempo** que debe abarcar la línea de tiempo. La nueva vista se genera entonces automáticamente.
7. En el campo de entrada superior, introduzca la columna de la que depende el **etiquetado de los bloques**.

![crear una vista de línea de tiempo](images/create-timeline-view.gif)

## Opciones de vista

Puede utilizar las siguientes opciones en una vista de línea de tiempo:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) u [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por cualquier valor
- [Color de las líneas]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Compartir vista con otros]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Imprimir vista]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})

## Opciones de visualización

Hay un total de 5 opciones de visualización para la escala de la línea de tiempo: **Año**, **Trimestre**, **Mes**, **Semana** y **Día**. Puede cambiar fácilmente entre estas opciones. Sólo tiene que hacer clic en la opción correspondiente del **menú desplegable** situado encima de la línea de tiempo.

![Opciones de visualización de la vista de la línea de tiempo](images/display-options-timeline-view.jpg)

## Mostrar y ocultar información

Haga clic en **Mostrar columnas** para mostrar más o menos información mostrando u ocultando columnas. Active el **deslizador** de las respectivas columnas para mostrar más información de los registros de datos en la línea de tiempo.

![mostrar información de otras columnas en la línea de tiempo](images/other-fields-shown-in-timeline-view.gif)

## Editar registros de datos en la vista de línea de tiempo

Haga doble clic en un registro y se abrirá una ventana con los **detalles de la fila**. Realice los ajustes deseados en el registro de datos. Los cambios se guardan automáticamente al cerrar la ventana.

## Ampliar, acortar o mover periodos de tiempo

Para ampliar o acortar un periodo de tiempo, mantenga pulsado el botón del ratón y arrastre **sobre el borde izquierdo o derecho de una entrada**. Si desea mover un periodo de tiempo, mantenga pulsado el botón izquierdo del ratón y mueva la entrada **arrastrando y soltando** en la dirección deseada. Los valores correspondientes en las columnas de fechas se ajustarán automáticamente.

![Cambiar periodos de tiempo en la vista de línea de tiempo](images/change-records-in-timeline-view.gif)