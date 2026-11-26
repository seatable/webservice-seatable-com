---
title: 'Bloquear filas mediante automatización'
date: 2023-01-27
lastmod: '2023-03-31'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/es/ayuda/bloquear-filas-automatizacion'
aliases:
    - '/es/ayuda/zeilen-per-automation-sperren'
seo:
    title: 'Bloquear filas automáticamente en SeaTable: tutorial'
    description: 'Automatice el bloqueo de filas en SeaTable: defina disparadores, establezca condiciones y gestione el acceso a los datos fácilmente.'
---

Con la ayuda de las automatizaciones, ya no tendrá que bloquear manualmente las filas de sus tablas, sino que podrá hacer que el [bloqueo de filas]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) se ejecute automáticamente. Esto es muy útil si siempre quiere evitar que una fila se siga editando después de un determinado momento (por ejemplo, cuando finaliza una operación).

![Bloquear una fila con una automatización](images/lock-row-with-an-automation.png)

{{< warning  headline="Desbloqueo solo posible manualmente"  text="Las filas bloqueadas con una automatización **no** se pueden **desbloquear** del mismo modo. Esto solo es posible manualmente y con los **derechos de administrador** necesarios." />}}

## Creación de la automatización

1. En las opciones de la base, haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} y luego en **Reglas de automatización**.
2. Haga clic en **Añadir regla**.
3. **Asigne un nombre** a la automatización y defina la **tabla** y la **vista** en las que debe surtir efecto.
4. Defina un **evento desencadenante** que active la automatización.
5. Haga clic en **Añadir acción** y seleccione **Bloquear registro** como acción automatizada.

![Selección de la acción automatizada: "Bloquear registro"](images/lock-record.png)

6. Confirme con **Enviar**.

{{< warning headline="Nota importante" >}}

La acción automatizada **Bloquear registro** solo está disponible para los siguientes eventos desencadenantes:

- Cuando se modifica una fila
- Cuando se añade una fila
- A una hora programada para las entradas que cumplan determinadas condiciones

{{< /warning >}}

## Ejemplo de aplicación

Si, por ejemplo, desea **bloquear** todas las filas de una de sus tablas en las que una determinada entrada alcance un **valor** específico, defina el evento **Cuando se modifica una fila** como desencadenante de la automatización.

![Definición del evento desencadenante de la automatización](images/trigger-example-1.png)

A continuación, establezca el **valor** y la **columna** en la que debe alcanzarse.

![Definición del evento desencadenante de la automatización](images/trigger-example-2.png)

Por último, establezca **Bloquear registro** como acción automatizada.

![Definición de la acción automatizada](images/automated-action-example.png)

A partir de este momento, la automatización creada bloqueará **todas las filas** en las que las **entradas** cambien de forma que cumplan la regla de automatización.

![Acción automatizada definida: "Bloquear registro"](images/automated-action-example-2.png)

{{< warning  headline="Atención"  text="Con una automatización, solo puede bloquear las filas en las que se ha producido el evento desencadenante de la automatización. Una regla de automatización según el patrón **Un evento en la fila X desencadena el bloqueo de la fila Y** no es posible." />}}

## Bloquear varias filas al mismo tiempo

Las automatizaciones son extremadamente útiles si desea bloquear varias filas al mismo tiempo. Para ello, seleccione el disparador **A una hora programada para las entradas que cumplan determinadas condiciones** y establezca las condiciones correspondientes. En lugar de establecer la frecuencia y la hora de ejecución, haga clic en **Ejecutar ahora** en la parte inferior para bloquear inmediatamente todas las filas deseadas.

Para obtener más información sobre el bloqueo de filas, consulte el artículo [Bloquear una fila]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}).

### Más artículos útiles en la sección Automatizaciones:

- [Visión general de las automatizaciones]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [Cómo funcionan las automatizaciones]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Crear una automatización]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Gestionar y agrupar automatizaciones]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Pausar automatizaciones]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Borrar automatizaciones]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Mostrar el registro de ejecución de una automatización]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Disparadores de automatización]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Acciones de automatización]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Vinculación de entradas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

### Otros ejemplos interesantes de automatizaciones:

- [Vinculación de entradas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Añadir filas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Añadir entradas a otras tablas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Enviar notificaciones mediante automatización]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Envío automatizado de correos electrónicos]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
