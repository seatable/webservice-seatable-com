---
title: 'La vista Kanban'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/es/ayuda/la-vista-kanban'
aliases:
    - '/es/ayuda/guia-plugin-kanban'
    - '/es/ayuda/anleitung-zum-kanban-plugin'
seo:
    title: 'Cree y utilice la vista Kanban en SeaTable'
    description: 'Aprenda a configurar la vista Kanban en SeaTable y a utilizarla de forma óptima para la visualización de procesos'
weight: 14
---

Una **vista Kanban** está predestinada a visualizar procesos dinámicos con diferentes fases. En este sentido, permite visualizar **flujos de trabajo** y **progresos de proyectos**, por ejemplo. Es especialmente útil para la [planificación de proyectos]({{< relref "templates/projects/project-plan" >}}), el [desarrollo de software]({{< relref "templates/software-development/bug-tracker" >}}) o la distribución de tareas dentro de un equipo.

{{< warning type="warning" headline="Requisitos" >}}

Para utilizar la vista Kanban de forma eficaz, necesita al menos una columna en su tabla que permita asignar opciones de forma clara. Los tipos de columna [Selección única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) o [Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) son adecuados para ello.

{{< /warning >}}

## Estructura de una vista Kanban

Una vista Kanban consta de **pilares** que representan diferentes pasos o fases de un proceso. En un flujo de trabajo, por ejemplo, pueden ser "idea", "planificado", "en curso" y "completado".

![Vista Kanban](images/kanban-view.jpg)

Las columnas están etiquetadas con **tarjetas móviles**, que puede mover tanto dentro de una columna como de una columna a la siguiente. Una tarjeta Kanban puede representar un paquete de trabajo o una tarea, por ejemplo.

![movimientos Kanban](images/move-records-in-kanban-view.gif)

## Cómo crear una vista Kanban

![Crear una vista Kanban](images/create-kanban-view.jpg)

1. Haga clic en el **nombre de la vista actual**.
2. Haga clic en **Añadir vista o carpeta** y seleccione el **Tipo de vista** deseado.

![Nombrar una vista Kanban](images/name-kanban-view.jpg)

3. Asigne un **nombre** a la nueva vista.
4. Active el control deslizante si la nueva vista no debe ser visible para todos sino **privada**.
5. Confirme con **Submitir**.

![crear una vista Kanban](images/kanban-view-settings.jpg)

6. Especifique qué columna desea utilizar para la **agrupación**, es decir, la definición de las columnas. A continuación, la vista Kanban se genera automáticamente.
7. En el campo **Título**, introduzca la columna con la que desea etiquetar las tarjetas Kanban.
8. Opcionalmente, también puede activar los **controladores** para activar determinadas funciones o visualizar más columnas.

Si desea cambiar algo más adelante, haga clic en el **icono de la rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} de la esquina superior derecha y ajuste la **configuración**.

## Ajustes de la vista Kanban

Puede utilizar las opciones de la rueda dentada para cambiar la presentación visual de la vista Kanban.

- Puede utilizar el control deslizante **No mostrar valores vacíos** para eliminar los marcadores de posición en gris de las tarjetas Kanban.
- El deslizador **Mostrar nombres de columnas** muestra los nombres de las columnas por encima de toda la información activada.
- El deslizador **Envolver texto** formatea los textos para que sean totalmente legibles en las tarjetas del tablero Kanban.

![configuración de la vista Kanban](images/show-other-fields-in-kanban-view.gif)

## Mostrar y ocultar otras columnas

Todas las **columnas** que haya creado en su tabla aparecen en la sección inferior. Al activar los **controladores** individuales, las entradas de las columnas respectivas se hacen visibles como notas informativas en las fichas.

{{< warning headline="Nota" text="Abra los **detalles de las filas** haciendo clic en una tarjeta para ver toda la información de una fila, aunque los controles deslizantes no estén activados." />}}

## Opciones de vista

Puede utilizar las siguientes opciones en una vista Kanban:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) u [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por cualquier valor
- [Compartir vista con otros]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Añadir un nuevo registro en la vista Kanban

![añadir un nuevo registro en la vista Kanban](images/add-record-in-kanban-view.jpg)

Haga clic en **Añadir fila** en la parte inferior de una columna. Se abrirá una nueva ventana. Cree un nuevo registro de datos en **detalles de la línea** e introduzca la información necesaria. Los cambios se guardan automáticamente al cerrar la ventana.

## Editar registros de datos en la vista Kanban

Haga clic en una **tarjeta Kanban** y se abrirá una ventana con los **detalles de la línea**. Realice los ajustes deseados en el registro de datos. Los cambios se guardan automáticamente al cerrar la ventana.
