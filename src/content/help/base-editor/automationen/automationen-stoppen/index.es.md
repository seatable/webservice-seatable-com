---
title: 'Pausar automatizaciones'
date: 2023-01-27
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/es/ayuda/pausar-automatizaciones-seatable'
aliases:
    - '/es/ayuda/automationen-stoppen'
seo:
    title: 'Pausar y reactivar las automatizaciones SeaTable: gestión sencilla para empresas'
    description: 'Descubre cómo pausar y volver a activar las automatizaciones en SeaTable Enterprise para controlar flujos sin perder configuraciones ni datos importantes.'
weight: 9
---

Si ya no desea ejecutar automatizaciones durante un determinado periodo de tiempo, puede **pausarlas** en lugar de [eliminarlas]({{< relref "help/base-editor/automationen/automationen-loeschen" >}}). Esto tiene la ventaja de que puede **reactivar** simplemente las automatizaciones en pausa, mientras que tiene que crear desde cero las automatizaciones eliminadas.

## Detener temporalmente las automatizaciones

1. Abra una **Base** en la que desee pausar una automatización activa.
2. En la cabecera de la base, haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} y después en **Reglas de automatización**.
3. Mueva el puntero del ratón sobre la regla de automatización correspondiente, haga clic en los tres puntos y, a continuación, en {{< seatable-icon icon="dtable-icon-paused" >}} **Pausar regla** .

![Pausar regla de automatización](images/pause-automation-rule.gif)

La regla de automatización seleccionada queda **pausada**. Puede reconocerlo por la nota **(pausado)**, que se añade al nombre de la automatización en rojo.

{{< warning type="warning" headline="Nota importante" text="Las automatizaciones pausadas **dejan de estar activas** hasta que se reinician. Esto significa que los eventos de activación definidos **ya no** desencadenan acciones automatizadas." />}}

## Reiniciar automatizaciones

Para **activar** de nuevo las automatizaciones pausadas, sólo tiene que seguir los pasos descritos anteriormente y hacer clic en {{< seatable-icon icon="dtable-icon-implement" >}} **Iniciar regla** .

![Reiniciar regla de automatización](images/start-automation-rule.gif)

El aviso **(pausado)** a la derecha del nombre de la automatización vuelve a desaparecer.
