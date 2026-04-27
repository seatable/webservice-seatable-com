---
title: 'Añadir filas mediante automatización'
date: 2023-03-02
lastmod: '2023-03-31'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/es/ayuda/anadir-filas-automaticas-seatable'
aliases:
    - '/es/ayuda/zeilen-per-automation-hinzufuegen'
seo:
    title: 'Añada filas automáticamente con la automatización'
    description: 'Añada filas nuevas en tablas SeaTable según condiciones o calendario, con automations y sin tareas manuales repetitivas.'
---

Con la ayuda de las automatizaciones, ya no tendrá que añadir manualmente filas con determinadas entradas a sus tablas, sino que podrá hacer que estos pasos se realicen automáticamente. Basta con definir una automatización correspondiente para cualquier vista de tabla.

## Cómo añadir líneas con una automatización

![Añadir entradas mediante automatización](images/how-to-use-automations-for-locking-rows-3.png)

1. Haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} en la cabecera Base y luego en **Reglas de automatización**.
2. Haga clic en **Añadir Regla**.
3. **Asigne un nombre a la** automatización y defina la **tabla** y la **vista en las** que debe funcionar.
4. Defina un **evento desencadenante que active** la automatización.
5. Haga clic en **Añadir Acción** y seleccione **Añadir Fila** como acción automatizada.
6. Confirme con **Enviar**.

## Creación de la automatización

En primer lugar, defina un **evento desencadenante** para la automatización.

![Eventos desencadenantes básicamente disponibles para su selección](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Nota importante" >}}

La acción automatizada **Añadir línea** está a su disposición **exclusivamente** disponible tras los siguientes eventos desencadenantes:

- Se añade una nueva entrada
- Las entradas cumplen determinadas condiciones tras el tratamiento
- Activador periódico

{{< /warning >}}

A continuación, seleccione **Añadir fila** como acción automatizada.

![Añadir la acción automatizada](images/add-an-action.png) ![Selección de la acción automatizada](images/action-add-records.png)

En el siguiente paso, defina las **entradas** que deberán aparecer en una fila tras activarse la automatización. Con un clic en **Añadir campo** puede definir cualquier entrada.

![Haga clic en Añadir campo para definir entradas](images/add-field.png)

En primer lugar, seleccione la **columna** en la que debe insertarse la entrada.

![Selección de la columna en la que se añade la entrada](images/select-column-to-add-record.jpg)

A continuación, puede definir la **entrada**. Dependiendo del [tipo de columna]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}
) seleccionado, dispone de distintas **opciones**.

![Defina la entrada que desea añadir a la tabla](images/define-record-to-add.png)

Por último, active la automatización haciendo clic en **Enviar**.

![Confirmación de la automatización](images/confirm-the-automation.jpg)

## Ejemplo de aplicación

Un **caso de uso** concreto de este tipo de automatización podría darse, por ejemplo, si registra sus reuniones semanales de equipo en una tabla. Desea que cada semana, antes de que comience la reunión, se cree automáticamente una fila con ciertas entradas, de modo que sólo tenga que introducir manualmente la información restante.

En este contexto, podría predefinir, entre otras cosas, la **fecha** de la reunión, la **sala de reuniones** y los **temas** fijos.

![Tabla de ejemplo para el caso de uso concreto](images/example-table-case-record-to-table.png)

### Creación de la automatización

En primer lugar, asigne un **nombre** a la automatización y seleccione tanto la **tabla** (aquí: Team Meetings) como la **vista** (aquí: Weekly Team Meeting) en la que debe actuar la automatización.

![Asignación de nombre a la automatización y selección de la tabla y la vista en las que debe actuar](images/basic-settings-automation-example.png)

Como **evento desencadenante** de la automatización, seleccione la opción **Activador periódico**.

![Selección del evento desencadenante](images/select-trigger.png)

A continuación, defina los intervalos en los que debe ejecutarse la automatización. Para que la fila con las entradas correspondientes se añada a la tabla cada semana, seleccione **semanalmente**.

![Selección de los intervalos en los que debe ejecutarse la automatización](images/run-frequency.png)

También puede seleccionar un **día de la semana** concreto y una **hora** concreta a la que se activará la automatización. En nuestro caso de uso tiene sentido elegir como momento una hora antes de la reunión semanal del lunes por la mañana.

![Selección del momento concreto de ejecución de la automatización](images/set-weekday-and-hour.png)

Como **acción automatizada**, defina en el siguiente paso la acción **Añadir fila**.

![Selección de la acción automatizada](images/select-add-record-as-a-action.png)

Haciendo clic en **Añadir campo**, puede definir todas las **entradas** que desee y que aparecerán automáticamente en la fila.

![Haga clic en Añadir campo para definir entradas](images/add-field.png)

Para que en la fila se registre automáticamente la fecha de la reunión de equipo prevista para el mismo día, seleccione la **columna de fecha** y el valor **El día de ejecución**.

![Definición de las entradas](images/definiton-of-the-records.png)

Con un clic en **Añadir campo** puede definir cualquier número de **entradas** adicionales que rellenen la fila tras activarse la automatización. Simplemente seleccione una **columna** correspondiente de su tabla en el menú desplegable y defina un valor en el campo de entrada adyacente.

![Defina cualquier número de entradas ](images/other-records.jpg)

Si, por ejemplo, la reunión de equipo se celebra habitualmente en una sala concreta, puede definir esa sala como valor fijo. Y si determinados temas (como altas/bajas/aniversarios) están en la agenda de cada reunión de equipo, también puede hacer que se introduzcan automáticamente en la fila.

### Probar la automatización

Si la automatización funciona como se desea, SeaTable añadirá automáticamente a su tabla una fila con las **entradas** previamente definidas tras activarse el desencadenante periódico (aquí: todos los lunes a las 7 h). Esto le ahorra algunas pulsaciones de teclas y podrá introducir después manualmente los datos que queden pendientes.

![Tabla tras activarse la automatización definida ](images/table-after-automation-new-record-to-current-table.png)

{{< warning  type="warning" headline="Consejo"  text="Para ahorrarse realmente trabajo y **no** tener que hacer cambios en los valores introducidos automáticamente, tiene sentido definir **únicamente** valores ya fijos que no tenga que ajustar manualmente a posteriori. Los ajustes en las entradas añadidas automáticamente son posibles en cualquier momento, pero limitan considerablemente la utilidad de la automatización." />}}

### Más ejemplos interesantes de automatizaciones:

- [Bloquear filas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Vincular entradas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

- [Añadir entradas a otras tablas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Enviar notificaciones mediante automatización]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Enviar correos electrónicos mediante automatización]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
