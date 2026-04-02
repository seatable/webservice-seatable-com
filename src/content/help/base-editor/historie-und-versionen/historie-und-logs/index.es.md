---
title: 'Historia y registros'
date: 2023-03-20
lastmod: '2024-12-16'
categories:
    - 'historie-und-versionen'
author: 'nsc2'
url: '/es/ayuda/historial-logs'
aliases:
    - '/es/ayuda/historie-und-logs'
seo:
    title: 'Historial y logs en SeaTable: seguimiento de cambios'
    description: 'Gestione historial y logs en SeaTable: actividades, logs de base, logs de fila, ejecuciones de automatización y registro de scripts fácil.'

---

Para que pueda controlar quién ha realizado qué **cambios** en los datos de sus bases y cuándo, el **historial** se almacena temporalmente en varios lugares de SeaTable. Hay un **registro de actividad** general en la página de inicio, un **registro** para cada base y para cada fila. Además, puede comprobar las automatizaciones y scripts que han tenido lugar en un registro **de ejecución**.

## Registro de actividades

Puede acceder al registro de actividades en cualquier momento desde la página **de inicio** de SeaTable.

![Contenido de un registro de actividades](images/activities-protocol.png)

En esta vista general encontrará todos los **cambios** que se han realizado en sus **bases**. Tenga en cuenta que el registro de actividad muestra todas las ediciones realizadas por usted, los miembros de su equipo, otros usuarios y automatizaciones.

Sin embargo, sólo se muestran los cambios que se han producido en sus bases **en los últimos 7 días**. Los cambios que se produjeron hace más de una semana se **eliminan** automáticamente del registro y ya **no** se pueden ver aquí.

Haciendo clic en el **nombre de** una **base** del protocolo, puede abrirla en una nueva ventana.

Para saber más sobre los cambios realizados en una base, basta con hacer clic en los **cambios** junto al nombre de una base en el registro de actividades.

![Más información sobre los cambios realizados en una base en el registro de actividades](images/details-of-a-edit.png)

A continuación, se abre una ventana en la que puede ver diversa información sobre los cambios realizados en la base correspondiente, por ejemplo, las **entradas** que se han añadido o eliminado de una base, una **descripción de** los cambios y la **hora exacta en** que se produjo la edición.

Tenga en cuenta que las **entradas añadidas** siempre se marcan **en verde**, mientras que **las eliminadas** aparecen **en rojo** en el registro.

![Entradas añadidas a una base (marcadas en verde) y entradas eliminadas de una base (marcadas en rojo) en el registro de actividades](images/red-or-green-marked-entries.png)

Haga clic en **Detalles** para visualizar los cambios correspondientes en una ventana aparte.

![Vista detallada de las entradas añadidas o eliminadas de una base en el registro de actividades.](images/activity-details.png)

## Registro de la base

Puede consultar todas las actividades realizadas en una base en el denominado **registro de la base**, al que puede acceder a través de la cabecera de la base.

![Abrir registros en Base](images/Logs-in-der-Base-oeffnen.png)

En el registro de una base, encontrará los cambios más recientes que se han realizado en la base correspondiente. Cada entrada de registro contiene la siguiente información:

- Nombre del editor
- Naturaleza del cambio
- Tabla correspondiente
- Fecha del cambio
- Descripción del cambio

![Cambios en los registros](images/Aenderungen-in-den-Logs.png)

Para más información sobre el registro base e **instrucciones** detalladas sobre cómo deshacer cambios sobre él, consulte este [artículo de ayuda]({{< relref "help/base-editor/historie-und-versionen/aenderungen-ueber-die-logs-rueckgaengig-machen" >}}).

Para aumentar la trazabilidad de los cambios en las filas de la [memoria de big data]({{< relref "help/base-editor/big-data/potenzial-big-data" >}}), SeaTable ofrece un **registro de big data** independiente. Sin embargo, este registro solo aparece en cuanto se activa la memoria de big data en la base.

![Registro de Big Data](images/Big-Data-Log.png)

{{< warning  headline="Explicado de forma sencilla"  text="Si quiere ver no sólo los cambios en **una** base, sino también una visión general de lo que está pasando en **todas sus bases**, entonces mira el registro de **actividad** en la página de inicio. Si le interesan los cambios en un **registro** exactamente, mire el **registro de filas**." />}}

## Registro de filas

Puede ver todos los cambios realizados en una fila en el denominado **registro de filas**, al que puede acceder haciendo clic en el **símbolo de la doble flecha** situado en la columna de numeración de una fila.

![Abrir el registro de filas](images/how-to-open-the-cell-log.jpg)

El registro de **fila** le permite ver cuándo qué usuario realizó qué cambio en el registro de una **fila**. Si en cambio desea ver todos los cambios en una base, debe utilizar el registro de **base**.

![Visualización de los cambios en una fila por registros.](images/Logs.png)

Si necesita más información sobre el registro de filas, consulte el [artículo de ayuda]({{< relref "help/base-editor/zeilen/anzeige-der-veraenderungen-auf-einer-zeile" >}}) correspondiente.

## Registro de ejecución de automatizaciones

Para comprobar la correcta ejecución de una **automatización**, tiene la posibilidad de ver el **registro de ejecución**, al que puede acceder a través de las opciones de la base.

![Mostrar registro de ejecución](images/open-an-automation-log.png)

SeaTable registra la siguiente información para cada ejecución de automatización: tiempo de ejecución, condición de ejecución, estado y cualquier advertencia.

![Estructura de un Auführungslog](images/structure-of-an-automation-log-newest.png)

Puede encontrar más información sobre el registro de ejecución de una automatización [aquí]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}}).

## Registro de ejecución de scripts

Los scripts creados en sus bases también tienen un **registro de ejecución al que** puede acceder a través de las opciones de la base.

![Abrir el registro de ejecución](images/Anlegen-eines-Skriptes.jpg)

En el registro de ejecución encontrará diversa información útil, como la hora de inicio, la hora de finalización, la duración total y el estado de la ejecución de un script.

![Información que se encuentra en el registro de ejecución de un script](images/information-in-a-script-log.png)

Si necesita más información sobre el registro de ejecución de scripts, no dude en echar un vistazo a este [artículo de ayuda]({{< relref "help/skripte/allgemein/das-ausfuehrungslog-von-skripten" >}}).
