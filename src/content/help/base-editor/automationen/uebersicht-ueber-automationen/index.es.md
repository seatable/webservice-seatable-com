---
title: 'Visión general de las automatizaciones'
date: 2023-01-31
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/es/ayuda/automatizaciones-guia-seatable'
aliases:
    - '/es/ayuda/uebersicht-ueber-automationen'
    - '/es/ayuda/automatizaciones-no-disponibles-seatable'
    - '/es/ayuda/warum-finde-ich-in-meiner-base-die-automationen-nicht'
seo:
    title: 'Automatizaciones en SeaTable: guía y casos de uso'
    description: 'Descubra cómo crear y gestionar automatizaciones en SeaTable: disparadores, acciones, historial y ejemplos prácticos para optimizar operaciones.'
star: true
weight: 1
---

Las automatizaciones son una función útil de SeaTable que le ayuda a **automatizar los procesos de trabajo**. Con la ayuda de las automatizaciones, no sólo puede **ahorrar tiempo**, sino también **minimizar** el número de **errores humanos** en el mantenimiento de sus datos, ya que los pasos del proceso completados automáticamente ya no tienen que ser realizados manualmente por un usuario.

En consecuencia, las automatizaciones tienen un efecto especialmente grande en los **grandes conjuntos de datos**, en los que pueden gestionar un elevado número de procesos de trabajo.

El siguiente artículo pretende darle una visión general del tema de las automatizaciones en SeaTable y contiene enlaces a los distintos artículos de ayuda en torno a esta característica.

## El editor de automatización

Puede acceder al editor de automatización de una base a través del icono correspondiente en la cabecera de la base.

![acceso al editor de automatización](images/access-automation-editor.jpg)

El editor de automatismos se extiende por toda la anchura de la ventana y, por tanto, permite una disposición clara: la **lista de todas las reglas de automatización existentes** se encuentra en la parte izquierda. Pasar de una regla a otra es, por tanto, cuestión de un solo clic. Aquí también puede añadir nuevas reglas y gestionar las existentes.

![editor de automatización en acción](images/automation-editor-in-action.gif)

En la zona central, puede ver la configuración de la automatización seleccionada en ese momento. Ésta consta de un **disparador** y una o varias **acciones**. La configuración del disparador o de las acciones se muestra dinámicamente en la parte derecha, en función del elemento sobre el que acabe de hacer clic.

También puede contraer la lista de reglas de automatización para crear más espacio en la zona central. Otro factor de comodidad es la **altura variable del panel del editor**. Esto le permite ver la vista, los nombres de las columnas y los registros de datos mientras trabaja en una automatización.

## Crear una automatización

El primer paso hacia los procesos de trabajo automatizados es la creación de una automatización. Para asegurarnos de que todo va según lo previsto y de que las reglas de automatización creadas tienen el efecto deseado, hemos resumido la información más importante para usted en este artículo.

Aprenda a crear una automatización [aquí]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}}).

## Gestionar automatizaciones

Por supuesto, puede gestionar posteriormente las automatizaciones ya creadas y activas. En este artículo le mostraremos qué ajustes puede realizar al automatizar sus procesos de trabajo.

Obtenga más información sobre la gestión de automatizaciones [aquí]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}}).

## Cómo funcionan las automatizaciones

Este artículo explica los fundamentos del funcionamiento de las automatizaciones en SeaTable y, por lo tanto, es adecuado como **introducción al tema de las automatizaciones**.

Obtenga más información sobre el funcionamiento de las automatizaciones [aquí]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}}).

## Disparadores de automatización

Los disparadores de automatización son el primero de los dos componentes esenciales de las automatizaciones. Los disparadores, que puedes configurar individualmente para cada automatización, activan distintos tipos de acciones automatizadas.

Obtenga más información sobre los disparadores de automatización [aquí]({{< relref "help/base-editor/automationen/automations-trigger" >}}).

## Acciones de automatización

Las acciones automatizadas representan el segundo de los dos componentes esenciales de las automatizaciones. Las acciones se desencadenan por los eventos desencadenantes definidos. Dependiendo del disparador, SeaTable puede realizar diferentes acciones de automatización.

Obtenga más información sobre las acciones de automatización [aquí]({{< relref "help/base-editor/automationen/automations-aktionen" >}}).

## Visualizar el registro de ejecución de una automatización

Para comprobar la ejecución de las automatizaciones, tiene la opción de visualizar el registro de ejecución de cada regla de automatización. Aquí puede ver información sobre cada ejecución de automatización.

Obtenga más información sobre el registro de ejecución de una automatización [aquí]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}}).

## Pausar automatizaciones

Las automatizaciones activas que ya no necesite durante un determinado periodo de tiempo pueden simplemente pausarse y reactivarse cuando sea necesario.

Aprenda a detener las automatizaciones [aquí]({{< relref "help/base-editor/automationen/automationen-stoppen" >}}).

## Borrar automatizaciones

También puede eliminar las automatizaciones que ya no necesite. Tenga en cuenta que no puede restaurar las automatizaciones eliminadas.

Aprenda a eliminar automatizaciones [aquí]({{< relref "help/base-editor/automationen/automationen-loeschen" >}}).

## Bloquear filas mediante automatización

Con la ayuda de las automatizaciones, ya no tendrá que bloquear manualmente las filas de sus tablas, sino que podrá hacer que este bloqueo se realice automáticamente. Esto es muy útil si siempre quiere evitar que una fila se siga editando después de un determinado momento (por ejemplo, cuando se ha completado un proceso).

Aprenda [aquí]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}) cómo bloquear filas con una automatización.

## Añadir filas mediante automatización

Con la ayuda de las automatizaciones, ya no tendrá que añadir manualmente filas con determinadas entradas a sus tablas, sino que podrá hacer que estos pasos se lleven a cabo automáticamente. Esto es especialmente ventajoso si desea automatizar varios pasos del proceso en sus tablas.

Aprenda a añadir filas mediante automatización [aquí]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}}).

## Añadir filas a otras tablas mediante automatización

Con la ayuda de las automatizaciones, ya no tendrá que realizar entradas en otras tablas manualmente, sino que podrá hacer que estos pasos se lleven a cabo automáticamente. La gran ventaja de esto es que el desencadenante no tiene que estar en la misma tabla que la acción desencadenada. Esta automatización es especialmente ventajosa si utiliza tablas diferentes cuyo contenido está relacionado entre sí.

Aprenda [aquí]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) cómo añadir entradas a otras tablas mediante la automatización.

## Envío automatizado de correos electrónicos

Con la ayuda de las automatizaciones, ya no tiene que enviar correos electrónicos manualmente a los usuarios seleccionados, sino que puede hacer que se envíen automáticamente. Esto resulta especialmente útil si, por ejemplo, desea informar inmediatamente a los usuarios sobre cambios en los datos de determinadas tablas.

Descubra [aquí]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}) cómo puede enviar correos electrónicos de forma automatizada.

## Vinculación de entradas mediante automatización

Con la ayuda de las automatizaciones, ya no tendrá que vincular manualmente las entradas de sus tablas, sino que podrá hacer que estos pasos se realicen automáticamente. Esto es útil si necesita determinados datos en varias tablas.

Aprenda [aquí]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}}) cómo vincular entradas mediante automatización.
