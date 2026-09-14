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

Una **vista Kanban** está predestinada a visualizar procesos dinámicos con diferentes fases. En este sentido, permite visualizar **flujos de trabajo** y **progresos de proyectos**, por ejemplo. Es especialmente útil para la [planificación de proyectos]({{< relref "templates/projects/project-plan" >}}), el [desarrollo de software]({{< relref "templates/it-engineering/bug-tracker" >}}) o la distribución de tareas dentro de un equipo.

{{< warning type="warning" headline="Requisitos" >}}

Para utilizar la vista Kanban de forma eficaz, necesita al menos una columna en su tabla que permita asignar opciones de forma clara. Los tipos de columna [Selección única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) o [Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) son adecuados para ello.

{{< /warning >}}

**En este vídeo tutorial, te mostraremos en solo unos minutos cómo crear una vista Kanban en SeaTable (con subtítulos en español).**
{{< youtube C19DWHZzTbg >}}


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

![Agrupar una vista Kanban](images/group-kanban-view.jpg)

6. Haga clic en **Añadir agrupación** y especifique qué **columna** desea utilizar para la agrupación, es decir, la definición de las columnas. A continuación, la vista Kanban se genera automáticamente.

![Configurar una vista Kanban](images/kanban-view-settings.jpg)

7. Vaya a la **configuración** e introduzca en el campo **Título** la columna con la que desea etiquetar las tarjetas Kanban.
8. Opcionalmente, también puede activar los **controladores** para activar determinadas funciones.

Si desea cambiar algo más adelante, haga clic en el **icono de la rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} de la esquina superior derecha y ajuste la configuración.

## Ajustes de la vista Kanban

Puede utilizar las opciones de la rueda dentada para cambiar la presentación visual de la vista Kanban.

- Puede utilizar el control deslizante **No mostrar valores vacíos** para eliminar los marcadores de posición en gris de las tarjetas Kanban.
- El deslizador **Mostrar nombres de columnas** muestra los nombres de las columnas por encima de toda la información activada.
- El deslizador **Envolver texto** formatea los textos para que sean totalmente legibles en las tarjetas del tablero Kanban.

![configuración de la vista Kanban](images/show-other-fields-in-kanban-view.gif)

## Opciones de vista

Puede utilizar las siguientes opciones en una vista Kanban:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) u [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por cualquier valor
- [Agrupar]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) por una sola columna
- [Ocultar columnas]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Compartir vista con otros]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Mostrar y ocultar otras columnas

![Ocultar columnas en la vista Kanban](images/hide-columns-in-kanban-view.jpg) 

Si desea mostrar menos información en las tarjetas, haga clic en **Ocultar** y desactive los **controladores** de las columnas correspondientes. Al reactivar los controladores, las entradas de esas columnas vuelven a ser visibles en las tarjetas.

{{< warning  headline="Nota"  text="Si los controladores **no están activados**, tampoco podrá ver ni editar los valores de las columnas ocultas al abrir los **detalles de la fila**." />}}

## Añadir un nuevo registro en la vista Kanban

![añadir un nuevo registro en la vista Kanban](images/add-record-in-kanban-view.jpg)

Haga clic en **Añadir fila** en la parte inferior de una columna. Se abrirá una nueva ventana. Cree un nuevo registro de datos en **detalles de la línea** e introduzca la información necesaria. Los cambios se guardan automáticamente al cerrar la ventana.

## Editar registros de datos en la vista Kanban

Haga clic en una **tarjeta Kanban** y se abrirá una ventana con los **detalles de la línea**. Realice los ajustes deseados en el registro de datos. Los cambios se guardan automáticamente al cerrar la ventana.
