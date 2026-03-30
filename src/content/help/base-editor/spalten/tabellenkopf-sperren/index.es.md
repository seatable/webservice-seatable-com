---
title: 'Bloquear cabecera de tabla'
date: 2023-03-03
lastmod: '2023-03-03'
categories:
    - 'arbeiten-mit-spalten'
author: 'nsc2'
url: '/es/ayuda/bloquear-encabezado-seatable'
aliases:
    - '/es/ayuda/tabellenkopf-sperren'
seo:
    title: 'Bloquee el encabezado de la tabla en SeaTable'
    description: 'Controle su estructura: Bloquee el encabezado y evite cambios en columnas de SeaTable por otros usuarios fácilmente.'
---

Si dispone de la autorización necesaria, puede bloquear la **cabecera de** cada tabla para impedir que se añadan, muevan y editen columnas en la tabla. La gran ventaja es que puedes bloquear **todas las columnas al mismo** tiempo con un solo clic.

Esto puede ser útil, por ejemplo, si trabajas con otros usuarios en una tabla y no quieres que se realicen cambios en la **estructura de columnas**.

{{< warning  headline="Consejo" >}}

Si sólo desea bloquear **columnas individuales de** su tabla para su edición, puede hacerlo a través de los [permisos de columna]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}).

{{< /warning >}}

## Bloquear cabecera de tabla

1. Abra la **tabla** en la que desea bloquear la cabecera de la tabla.
2. Haga clic en el **candado negro abierto de** la cabecera de la tabla.

![Bloqueo de la cabecera de la tabla](images/lock-the-table-head.jpg)

4. Si el bloqueo aparece en **rojo**, significa que ha bloqueado correctamente la cabecera de la tabla.

![Símbolo de bloqueo para una cabecera de tabla bloqueada correctamente](images/locked-table-head.jpg)

{{< warning  headline="Nota importante" >}}

No confunda esta función con la función **Icono de bloqueo en las opciones de vista**Puede utilizarlo para cambiar la configuración de un [Vista de la tabla de bloqueo]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}}) puede.

{{< /warning >}}

![Icono de bloqueo para bloquear las vistas en las opciones de vista](images/Bildschirmfoto-2022-10-28-um-15.22.16.png)

## Efectos del cierre

Una vez bloqueada la cabecera de la tabla, ya no se pueden **añadir columnas** a la tabla correspondiente hasta que se vuelva a cancelar el bloqueo. El **+-símbolo** para [añadir una columna]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}) por lo tanto **no** se muestra en tablas con una cabecera de tabla bloqueada.

![Falta el icono para añadir columnas en tablas con la cabecera bloqueada](images/tables-with-locked-table-head.png)

Tampoco se pueden mover las columnas, lo que significa que la **estructura de columnas** sigue siendo la misma en cualquier caso hasta que finalice el bloqueo.

Además, una vez bloqueada la cabecera de una tabla, ya no se pueden realizar **configuraciones** diversas en las columnas de la tabla. Esto afecta a las siguientes configuraciones de columna:

- Renombrar columna
- Añadir descripción de columna
- Personalizar el tipo de columna
- Duplicar columna
- Insertar columna izquierda
- Insertar columna derecha
- Borrar columna

Cuando la cabecera de la tabla está bloqueada, las opciones correspondientes aparecen **en gris** en la configuración de la columna.

![Opciones de columna atenuadas y, por tanto, no disponibles cuando la cabecera de la tabla está bloqueada](images/ausgegraute-spalten-einstellungen.png)

Sin embargo, el resto de **configuraciones de columna** no se ven afectadas por el bloqueo y pueden seguir editándose aunque la cabecera de la tabla esté bloqueada. Esto incluye las siguientes opciones:

- Ajustes de formato
- Editar autorizaciones de columna
- Formatear celdas de columna
- Ocultar
- Orden ascendente
- Ordenar de forma descendente

## Desbloquear

Para desbloquear una cabecera de tabla, basta con volver a hacer clic en el **bloqueo (rojo)** de la cabecera de la tabla.

![Desbloquear una cabecera de tabla](images/unlock-the-table-head.jpg)

Si el desbloqueo se ha realizado correctamente, aparecerá de nuevo un **cerrojo negro abierto**. A continuación, puede volver a añadir columnas a la tabla y editar las columnas existentes.

Tenga en cuenta que la cabecera bloqueada de las tablas que pertenecen a un grupo sólo puede ser desbloqueada de nuevo por **propietarios** y **administradores** del grupo. Los simples miembros del grupo **no** están autorizados a desbloquear y verán el siguiente mensaje cuando hagan clic en el símbolo del candado:

![Nota para los miembros de grupos simples que no están autorizados a desbloquear la cabecera de una tabla](images/no-permission-to-unlock-head-of-a-table.png)
