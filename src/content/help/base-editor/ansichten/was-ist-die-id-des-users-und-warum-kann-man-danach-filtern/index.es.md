---
title: '¿Qué es el ID de usuario y cómo se puede filtrar con él?'
date: 2023-04-25
lastmod: '2023-05-12'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/es/ayuda/filtrar-por-id-usuario'
aliases:
    - '/es/ayuda/was-ist-die-id-des-users-und-warum-kann-man-danach-filtern'
seo:
    title: 'Filtra por ID de usuario en SeaTable'
    description: 'Aproveche la ID del usuario para filtrar registros y asignar tareas en SeaTable. Más práctico que los filtros clásicos.'
weight: 23
---

El ID de usuario se describe mejor como un **número de identificación personal**. El ID de usuario es único dentro del equipo y siempre pertenece a un miembro del equipo.

Con la ayuda del ID de usuario, puede establecer **filtros dinámicos** en SeaTable, que en determinadas situaciones son más adecuados que un filtro según la [columna del creador]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) o [colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}). En este artículo presentamos las ventajas y desventajas de los filtros con el ID de usuario.

Si quieres saber cómo cambiar el ID de usuario de un miembro del equipo, [encontrarás la respuesta en este artículo de ayuda]({{< relref "help/teamverwaltung/team/aenderung-der-id-des-users-in-der-teamverwaltung" >}}).

{{< warning  headline="Uso típico de la identificación de usuario"  text="El ID de usuario lo establece el **administrador del equipo** para los miembros y suele seguir una lógica determinada. En las empresas, a menudo se utiliza como ID de usuario el **número** individual **del empleado o del personal**." />}}

## Filtro con el ID de usuario

En SeaTable puede utilizar el filtro **"es el ID del usuario actual"** para cada columna de texto. Esto crea un **filtro dinámico** que sólo muestra las entradas en las que el **propio ID** del usuario está almacenado en la [columna]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) de texto correspondiente.

![Ejemplo de filtro por ID de usuario](images/filter-user-ID-example-1.png)

### Ejemplo de aplicación

Suponga que tiene **tres empleados** y que tienen los siguientes **identificadores**:

- Markus con el ID **20**
- Helmut con el ID **23**
- Sven con el DNI **56**

Por ejemplo, si ahora mantiene una tabla en la que introduce las tareas pendientes de sus tres empleados y define un **filtro** de este tipo, ...

![Filtro definido según el ID de usuario en el caso de uso](images/filter-user-ID-in-the-example-case.png)

... se ...

-  ... Markus **sólo** verá las entradas para las que se haya introducido su **ID de usuario** individual **20** en la columna correspondiente.

![Vista de la tabla de Markus en el caso de uso concreto](images/example-table-markus.png)

-  ... Helmut **sólo** verá las entradas en las que se haya introducido su **ID de usuario** individual **23** en la columna correspondiente.
-  ... Sven **sólo** verá las entradas en las que se haya introducido su **ID de usuario** individual **56** en la columna correspondiente.

## ¿Cuándo tiene sentido un filtro de este tipo?

La alternativa sería filtrar por la columna [Creador]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) o [Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), que también ofrecen opciones de filtrado dinámico. Sin embargo, estas dos columnas presentan las siguientes desventajas:

- El valor de **la columna del creador** _no puede_ **modificarse** posteriormente. Una vez establecido, el valor siempre es el mismo. Esto sería problemático en el ejemplo anterior porque el creador de las tareas _no_ es el empleado.
- La **columna de colaborador** sólo puede rellenarse si un miembro del equipo tiene al menos **acceso de lectura** a la base. Esto puede _no_ ser deseable, especialmente cuando se utiliza la [aplicación]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}).
- La columna de colaborador _no_ se puede **rellenar automáticamente a través del formulario web**. El ID del usuario, sin embargo, puede establecerse como valor por defecto asignando _{creator.id}_.

Puede ajustar el ID de **usuario** introducido en la columna de texto en cualquier momento. Por lo tanto, si **posteriormente** desea cambiar la asignación de una fila, filtrar por el ID de usuario resulta muy útil.

### Ejemplo: Asignación de tareas

Imagine una lista de tareas con la que se introducen tareas en SeaTable. La columna del **creador** está _descartada_ para asignar al responsable, porque entonces los miembros del equipo sólo podrían crear tareas ellos mismos y asignárselas a sí mismos. La columna del **colaborador** es la solución más obvia, pero sólo si todos los miembros del equipo tienen al menos acceso de lectura a la base. Si los miembros del equipo no deben ver las tareas de sus colegas bajo ninguna circunstancia, se recomienda utilizar el ID de usuario para asignar al responsable.

Si asigna la tarea abierta _"planificar la próxima reunión"_ de _Markus_ a otro miembro del personal, es decir, cambia el **ID del usuario** de esta fila de _20 (Markus_ ) a _23 (Helmut_ ), por ejemplo, la fila correspondiente se **filtra** automáticamente de la vista de tabla de Markus y se añade a la vista de tabla de Helmut.

![Cambio posterior del identificador de usuario y consiguiente eliminación de la entrada de la tabla del empleado.](images/record-gets-deleted-after-user-ID-was-changed.gif)

Si la tarea debe mostrarse no sólo al usuario con el ID correspondiente, sino también al creador de la fila, puede establecer **dos reglas de filtrado** con un [enlace "o" o "o"]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}}).

![La alternativa: El filtro según la columna Creador](images/filter-creator.png)

## ID del usuario en formularios web

En los [formularios web]({{< relref "help/base-editor/webformulare/webformulare" >}}), puede registrar automáticamente la **identidad de los usuarios registrados**. Para ello, establezca **{creator.id}** o **{creator.name}** en la configuración de página de su formulario web como **valor predeterminado** y active la opción de que _no se pueda_ modificar. Una vez realizada esta configuración, el **ID del usuario conectado** se utilizará **automáticamente** en el formulario web y ya no podrá introducirse ni modificarse manualmente.

![Definición del ID de usuario como valor por defecto en formularios web](images/set-default-value-user-ID-in-webformulars.png)
