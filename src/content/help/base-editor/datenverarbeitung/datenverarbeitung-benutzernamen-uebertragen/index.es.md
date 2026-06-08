---
title: 'Tratamiento de datos: Transferencia de nombres de usuario'
date: 2023-03-17
lastmod: '2023-03-17'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/es/ayuda/transferir-nombres-usuario-seatable'
aliases:
    - '/es/ayuda/datenverarbeitung-benutzernamen-uebertragen'
seo:
    title: 'Transfiera nombres de usuario con SeaTable fácilmente'
    description: 'Transfiera nombres de usuario entre columnas en SeaTable con procesamiento de datos: perfecto para informes, listas y automatización.'
---

Mediante la función de tratamiento de datos, puede realizar diversas operaciones en una columna. La **transferencia de nombres de usuario** es una operación que permite copiar datos de columnas del tipo [Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), [Creador]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) o [Último modificador]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}) en una [columna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

## Puesta en marcha de la operación

![Crear una acción de tratamiento de datos](images/create-an-data-processing-action-1.jpg)

1. Abra cualquier **tabla** y haga clic en los **tres puntos** de las opciones de vista.
2. Haga clic en **Proceso de datos** y luego en **Añadir operación de proceso de** datos.
3. Asigne un **nombre** a la operación y seleccione **Transferir** nombre de usuario.

![Denominación de la acción de tratamiento de datos y selección del tipo de operación](images/select-operation-and-name-example-name.jpg)

5. Definir **tabla**, **vista**, **columna origen** y **columna resultado**.

![Definición de tabla, vista, columna origen y columna resultado de la operación](images/define-table-view-and-columns-example-name.png)

7. Haga clic en **Guardar para** guardar la acción y ejecutarla más tarde, o en **Ejecutar** para ejecutar la acción directamente.

La primera vez que se ejecuta con éxito, un pequeño **garrapata verde**.  
![Si la acción de tratamiento de datos se ejecuta correctamente por primera vez, aparece una marca verde](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Ejecución de la operación

Si, por ejemplo, mantiene una tabla con tareas pendientes en la que **los miembros de** su equipo están registrados como personas de contacto responsables en una [columna de personal]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), puede simplemente copiar los nombres de usuario en una [columna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}), por ejemplo, para utilizarlos en una lista de personal.

Para ello, siga los pasos descritos anteriormente y seleccione la columna de personal como columna de **origen** y la columna de texto como columna de **resultado**.

![Definición de la acción de tratamiento de datos](images/name-operation-and-define-columns-example-name-1.png)

Si la operación se ejecuta correctamente, los **nombres de usuario seleccionados** se extraen de la columna de personal y se transfieren a la columna de texto separados por una coma.

![Nombres de usuario transferidos a una columna de texto o de resultados](images/table-after-operation-example-user-name.png)

{{< warning  headline="Nota importante"  text="Tenga en cuenta que con cada nueva ejecución de esta operación se **sobrescriben** las entradas existentes en la columna de resultados, siempre que hayan cambiado los nombres de usuario de la columna de origen." />}}
