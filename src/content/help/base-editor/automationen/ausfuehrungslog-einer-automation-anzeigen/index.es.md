---
title: 'Mostrar registro de ejecución de una automatización'
date: 2023-01-26
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/es/ayuda/registro-ejecucion-automatizacion'
aliases:
    - '/es/ayuda/ausfuehrungslog-einer-automation-anzeigen'
seo:
    title: 'Registro de ejecución de automatizaciones SeaTable: controla tiempos y alertas'
    description: 'Descubre cómo ver y analizar el log de las automatizaciones en SeaTable: revisa tiempos, condiciones, éxito y advertencias en los procesos empresariales.'
weight: 8
---

Para comprobar la **correcta ejecución de una automatización**, tiene la opción de ver el **registro de ejecución**. SeaTable registra la siguiente información para cada ejecución de automatización: tiempo de ejecución, condición de ejecución, estado y cualquier advertencia. También hay completas **estadísticas** para todas las ejecuciones de automatización.

{{< warning  headline="Nota importante"  text="Cada ejecución de una automatización se denomina **ejecución de automatización**." />}}

## Para echar un vistazo al registro de ejecución

![Mostrar registro de ejecución](images/open-automation-log.jpg)

1. Haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} en la cabecera Base y luego en **Reglas de automatización**.
2. Mueva el puntero del ratón sobre la **regla de automatización** cuyo registro desea ver.
3. Haga clic en los **tres puntos** y después en {{< seatable-icon icon="dtable-icon-journal" >}} **Abrir registro**.

## Estructura del registro de ejecución

![Estructura de un registro de ejecución](images/structure-of-an-automation-log.jpg)

Puede ver la siguiente información en el registro de ejecución de una automatización:

**Tiempo de ejecución**  
Aquí SeaTable almacena la hora exacta en la que el disparador inició la automatización.

**Condición de ejecución**  
Si la automatización se activa por la modificación o adición de una entrada, aparece el mensaje **per_update**. Si, por el contrario, la automatización se activa periódicamente, aparece el mensaje **por_día/semana/mes**.

**Estado**  
El estado indica si la automatización se ha ejecutado correctamente. Si es así, aquí aparece el mensaje **Éxito**.

**Advertencias**  
Si se produjeron problemas durante la ejecución de una automatización, aparece aquí el correspondiente mensaje de advertencia.

## Estadística de todas las ejecuciones de automatización

También puede consultar las estadísticas sobre **cuántas ejecuciones de automatización se han producido en total dentro de la base**, independientemente de las reglas de automatización individuales. Esto le permite saber con qué frecuencia se activan sus reglas de automatización y cuántas de las ejecuciones de automatización de que dispone en su suscripción mensual ha agotado ya.

1. Haga clic en **Estadística** en la esquina superior derecha del editor de automatización abierto.
![abrir las estadísticas de las ejecuciones de automatización](images/open-automation-statistic.png)
2. Esto abre una ventana en la que puede ver el **número de todas las automatizaciones ejecutadas por día**.
![Estadísticas de ejecución de automatizaciones](images/automation-statistic.png)