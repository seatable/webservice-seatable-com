---
title: 'Instrucciones para el plug-in de línea de tiempo'
date: 2023-02-06
lastmod: '2023-08-14'
categories:
    - 'plugins'
author: 'vge'
url: '/es/ayuda/guia-plugin-timeline'
aliases:
    - '/es/ayuda/anleitung-zum-timeline-plugin'
seo:
    title: 'Guía del plugin Timeline en SeaTable: visualiza periodos y gestiona solapamientos'
    description: 'Use el complemento Timeline de SeaTable para mostrar periodos en un cronograma y planificar citas y recursos claramente.'
---

El **plugin de línea** de tiempo permite mostrar distintos intervalos de tiempo en forma de **línea de tiempo**. Esto es muy útil, por ejemplo, si desea ver si las citas **se solapan**. En consecuencia, puede utilizar el plugin de cronograma para planificar vacaciones y proyectos o reservar salas (de reuniones), entre otras cosas.

Lea el artículo [Activación de un plugin en una base]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}) para saber cómo activar el plugin Timeline.

## Función del complemento de línea de tiempo

El complemento de la línea de tiempo muestra **intervalos de tiempo**. Por lo tanto, para esta representación se necesitan **dos** [columnas de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) en una tabla que definan el **principio** y el **final de** un marco temporal.

## Cómo utilizar el plug-in de la línea de tiempo

1. Active y abra el **plug-in de la línea de tiempo**.
2. Coloque el **Ajustes** {{< seatable-icon icon="dtable-icon-set-up" >}} de la línea de tiempo:
    - Tabla y vista
    - Color de los bloques y etiquetado
    - Fecha de inicio y fin
    - El período de tiempo que abarcará la representación
3. Haga doble clic en una de las entradas para abrir **los detalles de** la **fila**.

![Plugin de cronología con barras de colores y detalles de registro al hacer doble clic](images/timeline-plugin.gif)

## Efecto de la agrupación y la clasificación

Dado que el complemento de la línea de tiempo se basa en las vistas de la tabla, la [ordenación]({{< relref "help/base-editor/ansichten/ansichten-in-ordnern-gruppieren" >}}) las entradas también afectan a la visualización en la línea de tiempo. Para las vistas agrupadas, tiene la opción de mostrar los datos en un diagrama de **línea de n** ado activando el control deslizante **Mostrar como modo de línea de nado**.

![Plugin de cronología en modo swimlane con entradas agrupadas por categoría o usuario](images/timeline-plugingroup-3.gif)

## Crear varias líneas de tiempo

Como se puede ver en el vídeo anterior, también puedes crear **varias líneas de tiempo** en una base. Para ello, proceda del siguiente modo:

1. Haga clic en el **signo más** situado a la derecha del título de la primera línea de tiempo.
2. Asigne un **nombre** a la línea de tiempo y confirme con **Enviar**.
3. En la **configuración** {{< seatable-icon icon="dtable-icon-set-up" >}}, defina a qué [vista de tabla]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) y a qué [columnas de]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) fecha debe referirse la nueva línea de tiempo.
