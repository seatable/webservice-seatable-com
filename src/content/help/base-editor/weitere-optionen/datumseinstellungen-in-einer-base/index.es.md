---
title: 'Configuración de la fecha en una base'
date: 2025-07-02
lastmod: '2025-07-02'
categories:
    - 'arbeiten-mit-bases'
author: 'kgr'
url: '/es/ayuda/configuracion-fechas-base'
aliases:
    - '/es/ayuda/datumseinstellungen-in-einer-base'
seo:
    title: 'Configuración de fechas personalizada en tu base'
    description: 'Cambia el primer día de la semana en tu base SeaTable. Elige lunes, sábado o domingo según tu región y ajusta la visualización del calendario fácilmente.'

---

Como es habitual en Europa y en muchas otras regiones, SeaTable utiliza por defecto el **lunes** como primer día de la semana. Sin embargo, dependiendo del país en el que viva, el sábado o el domingo pueden ser el **primer día de la semana**. Por lo tanto, puede adaptar SeaTable a sus circunstancias regionales: En los ajustes de fecha, el primer día de la semana puede fijarse individualmente para cada base.

{{< warning type="warning" headline="Nota importante" >}}
Sólo los **propietarios** y **administradores** pueden editar los ajustes de fecha de una base que pertenezca a un grupo. Los simples miembros del grupo **no** verán los ajustes de fecha.
{{< /warning >}}

## Cambiar el primer día de la semana en una base

![Ajustes de fecha en una base](images/date-settings-of-a-base.gif)

1. Abra la **base** cuyos ajustes de fecha desea editar.
2. Haga clic en los **tres puntos** de la cabecera de la base.
3. Vaya a **Configuración** y después a **Configuración de la fecha**.
4. En la nueva ventana, seleccione qué día de la semana debe ser el **primer día de la semana**.
5. A continuación **cierre** la ventana. Los ajustes que haya realizado se **guardarán** automáticamente.

## Alcance de los ajustes de fecha

Un ajuste en la configuración de la fecha hace que el día seleccionado pase a la primera columna en el control de calendario de [Columnas de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}). Esto se aplica a la base actualmente abierta y a todas las aplicaciones basadas en ella.

En [la vista de calendario]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}) y en [la página de calendario en aplicaciones]{{< relref "help/app-builder/seitentypen-in-universellen-apps/kalenderseiten-in-universellen-apps" >}}), sin embargo, aún puede configurar el primer día de la semana de forma individual e independiente de la configuración en la base.