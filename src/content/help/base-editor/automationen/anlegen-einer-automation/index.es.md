---
title: 'Creación de una automatización'
date: 2022-12-06
lastmod: '2025-11-04'
categories:
    - 'automationen'
author: 'kgr'
url: '/es/ayuda/crear-automatizacion'
aliases:
    - '/es/ayuda/anlegen-einer-automation'
seo:
    title: 'Crear automatización en SeaTable – guía paso a paso'
    description: 'Aprende a crear automatizaciones en SeaTable: define eventos, acciones y condiciones para flujos de trabajo automáticos y eficientes.'
weight: 2
---

Con la ayuda de las automatizaciones, puede **automatizar procesos** de modo que no sólo ahorre tiempo, sino que también minimice el número de errores humanos. El primer paso hacia los flujos de trabajo automatizados es crear una automatización.

## Crear una regla de automatización

1. Abra la **Base** en la que desea crear una automatización.

![crear automatizaciones](images/how-to-use-automations.jpg)

2. En la cabecera de la base, haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} y después en **Reglas de automatización**.

3. Haga clic en **Añadir regla o carpeta** y después en **Regla**.

![crear automatización](images/add-automation.jpg)

4. Dé un **nombre** a la regla de automatización.

5. Cree la automatización deseada definiendo un **disparador** y varias **acciones**.

{{< warning headline="Consejo" text="Si aún no existen reglas en la base, también puede seleccionar directamente un disparador **para la primera automatización** – y SeaTable creará automáticamente una regla." />}}

![Acceso directo para la primera automatización](images/shortcut-add-first-automation.gif)

### Crear una regla de automatización en una carpeta

Si ya ha creado una carpeta para las reglas de automatización, también puede crear una regla directamente en la carpeta. Para ello, mueva el puntero del ratón sobre la carpeta, haga clic en los **tres puntos** y en **Añadir regla**.

![crear regla de automatización en una carpeta](images/add-automation-in-folder.jpg)

## Más pasos de automatización

### Administración

En primer lugar, puede administrar la nueva regla de automatización, por ejemplo **renombrar**, **borrar** o **mover a una carpeta**.

{{< button label="Más información sobre la gestión de reglas de automatización" link="help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}}

### Disparadores

En el siguiente paso, usted define un evento que sirve como disparador e inicia la automatización. Aquí también se especifica en qué **tabla** y en qué **vista** debe tener efecto la automatización. El **disparador** puede ser que se añada una fila o que se cumplan determinadas condiciones tras una modificación. También puede configurar la automatización para que se active diaria, semanal o mensualmente a una hora determinada.

![ajustes del disparador](images/trigger-settings.jpg)

{{< button label="Más información sobre los disparadores de automatización" link="help/base-editor/automationen/automations-trigger" >}}

### Acciones

Por último, defina una o varias **acciones** que se desencadenen por el evento desencadenante previamente definido. Dependiendo del tipo de disparador, las acciones posibles pueden incluir el envío de notificaciones y correos electrónicos, la adición o bloqueo de entradas o la ejecución de una función de AI.

![más pasos de automatización](images/steps-for-automation.jpg)

{{< button label="Más información sobre las acciones de automatización" link="help/base-editor/automationen/automations-aktionen" >}}