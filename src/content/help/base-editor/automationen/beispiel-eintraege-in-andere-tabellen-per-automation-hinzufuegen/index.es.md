---
title: 'Añadir entradas a otras tablas mediante automatización'
date: 2023-03-03
lastmod: '2023-04-12'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/es/ayuda/anadir-registros-otras-tablas-automatizacion-seatable'
aliases:
    - '/es/ayuda/eintraege-in-andere-tabellen-per-automation-hinzufuegen'
seo:
    title: 'Añada registros a otras tablas por automatización'
    description: 'Automatice la creación de registros en otras tablas SeaTable según condiciones; ahorre tiempo y evite tareas repetitivas.'
---

Con la ayuda de las automatizaciones, ya no tendrá que realizar entradas en otras tablas manualmente, sino que podrá hacer que estos pasos se lleven a cabo automáticamente. La gran ventaja de esto es que el desencadenante no tiene que estar en la misma tabla que la acción desencadenada.

## Añadir entradas a otras tablas mediante automatización

![Añadir entradas a otras tablas mediante automatización](images/how-to-use-automations-for-locking-rows-3.png)

1. Haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} en la cabecera Base y luego en **Reglas de automatización**.
2. Haga clic en **Añadir Regla**.
3. **Asigne un nombre a la** automatización y defina la **tabla** y la **vista en las** que debe activarse.
4. Defina un **evento desencadenante que active** la automatización.
5. Haga clic en **Añadir Acción** y seleccione **Añadir Nueva Entrada en Otra Tabla** como acción automatizada.
6. Defina la **tabla** en la que se insertará la entrada y los **campos** precumplimentados.
7. Confirme con **Enviar**.

## Creación de la automatización

Defina un **evento desencadenante** para la automatización tras determinar primero en qué **tabla** y **vista** se producirá.

![Eventos desencadenantes básicamente disponibles para su selección](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Nota importante" >}}

La acción automatizada **Añadir nueva entrada en otra tabla** está a su disposición. **exclusivamente** está disponible para los siguientes eventos de activación:

- [Las entradas cumplen determinadas condiciones tras el tratamiento]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_eintraege_erfuellen_nach_bearbeitung_bestimmte_bedingungen)
- [Se añade una nueva entrada]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_ein_neuer_eintrag_wird_hinzugefuegt)

{{< /warning >}}

A continuación, seleccione **Añadir nueva entrada en otra tabla** como acción automatizada.

![Añadir la acción automatizada](images/add-an-action.png) ![Selección de la acción automatizada](images/add-action-example2.png)

En el siguiente paso, seleccione la **tabla** a la que se añadirá la entrada una vez activado el desencadenante.

![Selección de la tabla a la que se añadirá la entrada al activarse la automatización](images/select-table.png)

A continuación, haga clic en **Añadir campo** para seleccionar las columnas para las que desea definir valores predefinidos en la nueva entrada.

![Haga clic en Añadir campo](images/add-field.png)

Ahora, en el menú desplegable, seleccione una **columna** correspondiente y defina el **valor** precumplimentado en el campo de entrada. Dependiendo del [tipo de columna]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}
) seleccionado, dispondrá de distintas **opciones**.

![Definición de la entrada y de la columna a la que se añadirá](images/set-table-and-entry.png)

Finalmente, confirme la automatización haciendo clic en **Enviar**.

![Confirmación de la automatización](images/confirm-the-automation.jpg)

## Ejemplo de aplicación

Un **caso de uso** concreto de este tipo de automatización podría darse, por ejemplo, si como responsable de una empresa es responsable de los nuevos empleados que se incorporan a su equipo. En el proceso de incorporación podría establecerse que, el primer día de trabajo, debe solicitar el **pago del salario** del empleado y documentar la **entrega de un coche de empresa**.

Cuando usted añade al nuevo empleado a su tabla, desea informar automáticamente al departamento de Recursos Humanos de que ha entregado el coche de empresa y de que pueden preparar la nómina del primer mes. Para ello, SeaTable debe **añadir una nueva entrada a la tabla del departamento de Recursos Humanos**.

En su caso, esto puede ponerse en práctica con una tabla en la que mantenga distintos datos de los empleados. En este contexto podría registrar, entre otras cosas, el nombre de los empleados o de las nuevas incorporaciones, su departamento y su fecha de incorporación.

![Tabla de ejemplo del caso de uso](images/example-table.3.png)

Con la ayuda de una automatización, cada vez que añada un nuevo empleado a la tabla, deberá añadirse automáticamente una nueva entrada a otra tabla, utilizada por el departamento de Recursos Humanos para gestionar los pagos de salarios y los coches de empresa.

### Creación de la automatización

En primer lugar, asigne un **nombre** a la automatización y seleccione tanto la **tabla** (employee lists) como la **vista** (new employees) en las que debe activarse la automatización.

![Asignación de nombre a la automatización, selección de la tabla y la vista en las que debe actuar](images/set-table-and-view-example-3.png)

Como **evento desencadenante** de la automatización, seleccione la opción **Las entradas cumplen determinadas condiciones tras la edición**.

![Selección del evento desencadenante](images/trigger-condition.png)

Para que **sólo** se añadan nuevas entradas a la tabla del departamento de Recursos Humanos cuando haya introducido el **nombre** de un nuevo empleado **en su tabla**, seleccione como **condición de filtro** que la columna "employee" **no esté vacía** tras la edición.

![Añadir una condición de filtro](images/set-condition-example-3.png)

Como **acción automatizada**, defina la acción **Añadir nueva entrada en otra tabla**.

![Selección de la acción automatizada](images/add-action-example2.png)

En el siguiente paso, seleccione la tabla "Payments" como **tabla** a la que se añadirá una entrada una vez activada la automatización.

![Selección de la tabla a la que se añadirá la entrada al activarse la automatización](images/select-table-example3.png)

A continuación, defina los **valores** con los que deben precumplimentarse determinados campos. Para citar el nombre de un nuevo empleado en la nueva entrada de la tabla del departamento de Recursos Humanos, escriba el **nombre** de la columna de su tabla en la que se encuentra dicho valor, encerrado entre llaves, en el campo de texto: {employee}

![Definición de las entradas que se añadirán a la tabla seleccionada](images/define-the-entrys-in-the-second-table.png)

### Probar la automatización

Si, tras confirmar la automatización, introduce en su tabla el nombre de un nuevo empleado, ...

![Añadir un nuevo empleado a su tabla](images/example-after-trigger-3.1.png)

... las entradas definidas se añadirán automáticamente a la tabla del departamento de Recursos Humanos.

![Tabla del departamento de Recursos Humanos tras activarse la automatización](images/example-after-trigger-3.2.png)

### Más ejemplos interesantes de automatizaciones:

- [Bloquear filas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Vincular entradas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Añadir filas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Enviar notificaciones mediante automatización]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Enviar correos electrónicos mediante automatización]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
