---
title: 'Captura de tiempos de un cambio de estado con una automatización'
date: 2023-04-28
lastmod: '2023-04-28'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/es/ayuda/automatizar-registro-cambios-estado-fechas'
aliases:
    - '/es/ayuda/zeitpunkte-einer-statusaenderung-mit-einer-automation-erfassen'
seo:
    title: 'Automatiza el registro de cambios de estado y fechas en SeaTable'
    description: 'Descubre cómo crear automatizaciones en SeaTable para registrar automáticamente las fechas y horas de cambios de estado, y mejorar tus procesos de negocios.'
---

Con la ayuda de [las automatizaciones]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}), ya no tiene que registrar **manualmente** las horas de un cambio de estado, sino que puede hacer que SeaTable lo haga **automáticamente**.

## Registre las horas de los cambios de estado mediante automatización

![Envío automatizado de correos electrónicos](images/how-to-use-automations-for-locking-rows-3.png)

1. Haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} en la cabecera Base y luego en **Reglas de automatización**.
2. Haga clic en **Añadir Regla**.
3. Dé un **nombre** a la automatización y defina la **tabla** y la **vista en las** que debe funcionar.
4. Defina el **evento desencadenante que activa** la automatización.
5. Haga clic en **Añadir Acción** y seleccione **Añadir Nueva Entrada en Otra Tabla** como acción automatizada.
6. Defina la **tabla** en la que se insertará la entrada y los **campos** precumplimentados.
7. Confirme con **Enviar**.

## Creación de la automatización

En primer lugar, defina el **evento desencadenante** adecuado para la automatización.

{{< warning  headline="Nota importante"  text="Para poder registrar las horas de los cambios de estado con una automatización, tiene que **obligatorio** el evento desencadenante **Las entradas cumplen determinadas condiciones tras el cambio** seleccionar. Con la ayuda de los otros eventos desencadenantes, puede seleccionar los cambios de estado **no** capturar." />}}

![Eventos desencadenantes básicamente disponibles para su selección](images/trigger-options-for-archivating-rows.png)

A continuación, seleccione **Añadir nueva entrada en otra** tabla como acción automatizada.

![Añadir la acción automatizada](images/add-an-action.png) ![Selección de la acción automatizada](images/add-action-example2.png)

En el siguiente paso, seleccione la **tabla** en la que se añadirá la entrada tras activarse el disparador.

![Selección de la tabla en la que se añadirá la entrada tras activarse el disparador.](images/select-table-to-add-entry-after-automation-example-1.png)

A continuación, haga clic en **Añadir campo** para seleccionar las columnas para las que desea definir valores fijos en la nueva entrada.

![Haga clic en Añadir campo](images/add-field.png)

Seleccione ahora la **columna** correspondiente en el menú desplegable y defina el **valor** precargado en el campo de entrada. Dependiendo del [tipo de columna]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) seleccionado, tiene diferentes **opciones** para elegir.

![Definición de la entrada y de la columna que se le va a añadir](images/define-column-to-be-added.png)

Por último, confirme la automatización haciendo clic en **Enviar**.

![Confirmación de la automatización](images/confirm-the-automation.jpg)

## Ejemplo de aplicación

Un **caso de uso** concreto para este tipo de automatización podría darse, por ejemplo, si desea registrar los distintos **pedidos de** su empresa en una tabla.

Al hacerlo, desea registrar automáticamente en otra tabla los **momentos** en los que se producen **cambios** en el estado del pedido de uno o varios pedidos de su tabla. De este modo, podrá controlar el **estado** de sus pedidos en todo momento y realizar un seguimiento de cada **cambio de estado**, desde "pago requerido" hasta "producto entregado correctamente".

Concretamente, esto puede hacerse con la ayuda de una tabla ("Pedido") en la que registre los distintos **pedidos** que ha realizado para su empresa. En este contexto, podría recoger el **número de** pedido, el **importe** y el **estado de** cada uno de los pedidos.

![Cuadro para el estudio de los distintos pedidos realizados](images/table-with-different-orders-1.png)

En otra tabla ("Registro del estado de los pedidos") también desea ver los distintos **números de pedido** junto con los **importes** correspondientes. Además, en esta tabla se introduce la **hora del último** cambio de estado en la [columna de]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) fecha "último **cambio de estado** ".

![Tabla en la que se recogen automáticamente las horas del último cambio de estado](images/table-order-status-log.png)

Mediante una automatización, cada vez que cambie el **estado** de un pedido en la tabla "Pedidos", la **hora del** cambio de estado se añadirá a la columna "último cambio de estado" de la tabla "Registro de estado de pedidos". Además, la automatización también añadirá automáticamente los **números de** pedido y los **importes a** la tabla "Registro de estado de pedidos".

### Creación de la automatización

En primer lugar, asigne un **nombre** a la automatización y seleccione tanto la **tabla** ("Pedidos") como la **vista** ("Todos los pedidos").

![Ajustes básicos de la automatización](images/set-basic-settings-automation-example-status-change.png)

Como **evento desencadenante de** la automatización, seleccione la opción **Requiere el cumplimiento de determinadas condiciones tras el procesamiento**.

![Definición del evento desencadenante](images/define-trigger-example-status-change.png)

Añadir como **condición de filtrado** que la columna **Estado** de la tabla "Pedidos" no debe estar **vacía** tras la edición para poder registrar los cambios de estado.

![Añadir una condición de filtro para activar el evento de activación](images/add-filter-condition-example-automation-status-change.png)

Como **acción automatizada**, defina la acción **Añadir nueva entrada en otra tabla**.

![Selección de la acción automatizada](images/add-action-example2.png)

En el siguiente paso, seleccione la **tabla**"Registro de estado de pedidos" como tabla en la que se añadirá la hora del cambio de estado una vez activada la automatización.

![Selección de la tabla en la que se añaden las entradas cuando se activa la automatización](images/select-table-to-put-in-entries-after-automation.png)

A continuación, defina los **valores** con los que deben rellenarse previamente determinados campos. Para que la **hora** correspondiente **a un cambio de estado** se añada siempre automáticamente a la columna de fecha "último cambio de estado", defina el valor **día de ejecución** para esta columna.

![Definición de los valores que se añaden automáticamente a la tabla cuando se activa la automatización](images/define-time-of-status-change-to-be-added-1.png)

Para **citar** los distintos **números de pedido** y los **importes** correspondientes en la tabla "Order-Status-Log", escriba los nombres de las columnas entre llaves en el campo de texto correspondiente: {Order-ID} & {Amount}

![Definición de los valores que se añaden automáticamente a la tabla cuando se activa la automatización](images/define-entries-to-be-added-to-table-after-automation.png)

### Probar la automatización

Si **modifica** el **estado de** varios pedidos en su tabla después de confirmar la automatización, ...

![Ajuste del estado de varios pedidos](images/change-status-of-different-orders.gif)

... tanto las horas de los cambios de estado como las entradas definidas (número de pedido e importe) se introducen automáticamente en la tabla "Registro de estado de pedidos".

![Tabla Registro del estado del pedido tras activar la automatización](images/table-after-automation-status.png)
