---
title: 'Disparadores de automatización'
date: 2023-01-27
lastmod: '2026-11-25'
categories:
    - 'automationen'
author: 'kgr'
url: '/es/ayuda/automations-triggers-seatable'
aliases:
    - '/es/ayuda/automations-trigger'
seo:
    title: 'Disparadores de automatización: opciones en SeaTable'
    description: 'Conozca los disparadores disponibles para automatizaciones en SeaTable y las acciones configurables para cada evento.'
weight: 5
---

Los **eventos desencadenantes** son uno de los dos componentes esenciales de las automatizaciones. Los eventos desencadenan diferentes tipos de [acciones]({{< relref "help/base-editor/automationen/automations-aktionen" >}}), que puede definir individualmente para cada automatización. Este artículo le ofrece una **visión general** de los diferentes tipos de disparadores.

## Disparadores de automatización disponibles

En la última versión de SeaTable, hay un total de **cuatro** disparadores diferentes entre los que elegir:

![Eventos desencadenantes actualmente disponibles](images/automation-triggers.jpg)

- Cuando se modifica una fila
- Cuando se añade una fila
- A una hora programada
- A una hora programada para las entradas que cumplan determinadas condiciones

## Ajustes del disparador

Para crear o editar un disparador, haga clic en la casilla correspondiente de la zona central del editor de automatización. Los ajustes del disparador aparecerán entonces a la derecha.

![Ajustes del disparador](images/automation-trigger-settings.jpg)

- Primero puede cambiar el **disparador** utilizando el menú desplegable. Para ello, seleccione el evento desencadenante deseado.
- A continuación, defina la **tabla** y la **vista** en las que debe tener efecto la automatización.
- En función del tipo de disparador, puede realizar más ajustes, por ejemplo, las **columnas supervisadas**, las **condiciones** para la activación o la **hora** de activación.

![Ajustes del disparador en detalle](images/automation-trigger-settings.gif)

{{< warning headline="Guardar cambios" text="¡No olvide **guardar** los ajustes del disparador! De lo contrario, todos los cambios se perderán cuando cierre la ventana." />}}

## Disparador de automatización: Cuando se modifica una fila

Si selecciona este evento como disparador, la automatización correspondiente se activará cada vez que se modifique un valor en una de las columnas supervisadas y una fila de la vista seleccionada cumpla determinadas condiciones tras la edición. Si desea que el disparador se active cada vez que se produzca un cambio, no añada ninguna condición.

En las **condiciones**, puede definir individualmente para cada columna cómo debe ser el valor correspondiente tras la edición para que se inicie la automatización. Como parte de esto, puede decidir si se deben supervisar todas las columnas de la vista o solo las seleccionadas para detectar el evento desencadenante.

![Ajustes del disparador cuando se modifica una fila](images/automation-trigger-when-a-row-is-updated.jpg)

Si selecciona este evento como disparador de una automatización, puede elegir entre las siguientes **acciones automáticas**:

- Enviar notificación
- Enviar notificación de aplicación
- Enviar correo electrónico
- Añadir registro
- Bloquear registro
- Modificar registro
- Añadir enlaces
- Añadir registro a otra tabla
- Añadir registro a una tabla vinculada
- Modificar registro vinculado en otra tabla
- Ejecutar script Python
- Llamar a la IA
- Gestionar citas en Google Calendar
- Convertir página a PDF

## Disparador de automatización: Cuando se añade una fila

Si selecciona este evento como disparador, la automatización correspondiente se activará cada vez que se añada una **nueva fila** en la vista seleccionada. Además, puede restringir aún más la aparición del evento definiendo **condiciones** que debe cumplir la nueva fila.

![Ajustes del disparador cuando se añade una fila](images/automation-trigger-when-a-row-is-added.jpg)

En las condiciones, puede especificar individualmente para cada columna cuál debe ser el valor correspondiente para que se inicie la automatización. Si desea que cada nueva fila active la automatización, no añada ninguna condición.

{{< warning headline="Consejo" text="Este disparador es especialmente útil, por ejemplo, cuando se importan nuevos registros de datos o se introducen a través de formularios." />}}

Si selecciona este evento como disparador de una automatización, podrá elegir entre las siguientes **acciones automáticas**:

- Enviar notificación
- Enviar notificación de aplicación
- Enviar correo electrónico
- Añadir registro
- Bloquear registro
- Modificar registro
- Añadir enlaces
- Añadir registro a otra tabla
- Ejecutar script Python
- Llamar a la IA
- Gestionar citas en Google Calendar
- Convertir página a PDF

## Disparador de automatización: A una hora programada

Si selecciona este disparador, podrá definir una **hora** a la que se ejecutará la automatización **diaria**, **semanal** o **mensualmente**.

![Opciones de configuración para un disparador diario a una hora programada](images/automation-trigger-at-scheduled-time.jpg)

Mientras que solo puede especificar la **hora** para una automatización diaria, también puede especificar el **día de la semana** para una automatización semanal o el **día del calendario** para una automatización mensual.

![Opciones de configuración para un disparador semanal a una hora programada](images/automation-trigger-at-scheduled-time-weekly.jpg)

Si configura este disparador para una automatización, podrá elegir entre las siguientes **acciones automáticas**:

- Enviar notificación
- Enviar notificación de aplicación
- Enviar correo electrónico
- Añadir registro
- Añadir enlaces
- Ejecutar script Python
- Ejecutar procesado de datos
- Generar PDF a partir de un documento y enviarlo
- Archivar

## Disparador de automatización: A una hora programada para las entradas que cumplan determinadas condiciones

Con este disparador, usted especifica una **hora**, al igual que con el disparador anterior, a la que se activa la automatización **diaria**, **semanal** o **mensualmente**. También puede limitar las filas que se ven afectadas por este evento desencadenante.

Para las **condiciones**, puede especificar individualmente para cada columna cómo debe ser el valor correspondiente para que la automatización se ejecute en el momento especificado.

![Disparador a una hora programada para los registros que cumplan determinadas condiciones](images/automation-trigger-at-scheduled-time-for-records-that-match-condition.jpg)

Si selecciona este disparador para una automatización, podrá elegir entre las siguientes **acciones automáticas**:

- Enviar notificación
- Enviar notificación de aplicación
- Enviar correo electrónico
- Bloquear registro
- Modificar registro
- Convertir página a PDF
- Archivar
