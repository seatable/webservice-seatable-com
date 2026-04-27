---
title: 'Vinculación de entradas mediante automatización'
date: 2023-01-30
lastmod: '2023-04-06'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/es/ayuda/vincular-registros-automatizacion'
aliases:
    - '/es/ayuda/verlinken-von-eintraegen-per-automation'
seo:
    title: 'Vincular registros en SeaTable automáticamente: guía'
    description: 'Automatiza enlaces entre registros en SeaTable: usa triggers, selecciona las columnas y crea vínculos automáticos entre tus datos fácilmente.'


---

Con la ayuda de las automatizaciones, ya no tendrá que vincular manualmente las entradas de sus tablas, sino que podrá hacer que estos pasos se realicen automáticamente. Basta con definir una automatización correspondiente para cualquier vista de tabla.

## Vinculación de entradas mediante automatización

![Bloqueo y archivo de líneas con automatización](images/how-to-use-automations-for-locking-rows-3.png)

1. Haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} en la cabecera Base y luego en **Reglas de automatización**.
2. Haga clic en **Añadir Regla**.
3. **Asigne un nombre a la** automatización y defina la **tabla** y la **vista en las** que debe funcionar.
4. Defina un **evento desencadenante que active** la automatización.
5. Haga clic en **Añadir acción** y seleccione **Añadir enlaces** como acción automatizada.
6. Confirme con **Enviar**.

## Creación de la automatización

En primer lugar, defina un **evento desencadenante** para la automatización.

![Eventos desencadenantes para bloquear y archivar líneas](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Nota importante" >}}

La acción automatizada **Añadir enlaces** está a su disposición **exclusivamente** está disponible para los siguientes eventos de activación:

- "Las entradas cumplen determinadas condiciones tras el tratamiento"
- "Se añade una nueva entrada"
- "Activador periódico"

{{< /warning >}}

A continuación, seleccione **"Añadir enlaces"** como acción automatizada.

![Añadir la acción automatizada](images/add-an-action.png) ![Añadir la acción automatizada: "Añadir enlaces"](images/add-action-add-links.png)

Finalmente, seleccione una **columna** que deba vincularse a la tabla seleccionada y defina una **condición específica** que deba cumplirse para que se ejecute la automatización.

![Definición de la acción automatizada](images/automated-actions-add-links.png)

Finalmente, confirme la automatización haciendo clic en **Enviar**.

![Confirmación de la automatización](images/confirm-the-automation.jpg)

## Ejemplo de aplicación

Un **caso de uso** concreto de este tipo de automatización podría darse, por ejemplo, si trabaja en el departamento de contabilidad de una empresa. Desea mantener tanto una tabla con todos los pagos que se reciben en una cuenta de la empresa (**Payments**) como una tabla con todas las facturas que deben pagarse a la empresa (**Invoices**).

En la tabla **Payments**, junto a los **números de transacción** de los pagos (P-0001, etc.), ya registra los **importes** de los distintos pagos (columna **"Value"**).

![Tabla de ejemplo Payments](images/Table-Payments-1.png)

Su tabla **Invoices**, por su parte, contiene los **números de factura** (columna **"Invoice-No"**) y los respectivos **importes de la factura** (columna **"Price Total"**).

![Tabla de ejemplo "Invoices"](images/Table-Invoices.png)

Con la ayuda de una **automatización** desea ahora **vincular** las dos tablas **Payments** e **Invoices** para poder asignar automáticamente los **pagos** recibidos a una **factura** en función de sus números de factura.

### Preparación de la automatización

Antes de poder crear la automatización, primero debe añadir dos columnas más a la tabla **Payments**. En la columna **"Inv-No"** introduce manualmente los números de factura que corresponden a los respectivos pagos, lo que más tarde **activará** la automatización. En la columna **"Invoices"** se añadirán automáticamente las **entradas vinculadas** de la tabla **Invoices** una vez creada la automatización.

![Ampliación manual de la tabla "Payments" con dos columnas](images/Manuelle-Erweiterung-der-Tabelle-22Payments22.png)

En la tabla **Invoices** también necesita otra columna (**"Collected Payments"**) en la que se añadirán las entradas vinculadas de la tabla **Payments** al ejecutarse la automatización.

![](images/Hinzufuegen-der-Spalte-22Collected-PAyments22.png)

A continuación, puede crear una **automatización** para la tabla **Payments**.

### Creación de la automatización

En primer lugar, asigne un nombre a la automatización y seleccione la tabla **Payments** junto con la vista del mismo nombre en la que debe actuar la automatización.

![Definición de la automatización del caso de uso](images/definition-of-the-automation-1.png)

Como **evento desencadenante** de la automatización, seleccione la opción **"Las entradas cumplen determinadas condiciones tras la edición"**. Como condición de filtro, añada que las dos columnas **"Inv-No"** y **"Value"** de la tabla "Payments" **no estén vacías**. Esta condición tiene sentido, ya que la automatización debe activarse en cuanto haya entradas en estas columnas.

![Definición del evento desencadenante del caso de uso ](images/trigger-example-1-1.png) ![Definición del evento desencadenante del caso de uso ](images/trigger-example-2-1.png)

Como **acción automatizada** de la automatización, defina finalmente la acción **"Añadir una columna vinculada a la tabla"**.

![Añadir la acción automatizada: "Añadir enlaces"](images/add-action-add-links.png)

La columna **"Invoices"** es la columna en la que se añadirán las entradas vinculadas al ejecutarse la automatización.

![Selección de la columna en la que se añaden las entradas vinculadas](images/automated-action-example-1.png)

En el último paso de la definición de la automatización, debe establecer otra **condición** que deba cumplirse para que se añada una entrada vinculada a la columna. En este ejemplo se define que cada **entrada** añadida en la columna **"Inv-No"** debe encontrarse también en la columna **"Invoice-No"** de la tabla **Invoices**.

En concreto, esto significa que cada **número de factura** que asigne manualmente a un pago en la tabla **Payments** debe existir ya en la tabla **Invoices** para que las correspondientes **entradas** de ambas tablas puedan **vincularse** entre sí.

![Definición de la condición final para activar la automatización](images/automated-action-example-2-1.png)

### Probar la automatización

Si a continuación introduce un número de factura en la columna **"Inv-No"** de la tabla **Payments** que ya esté presente en la tabla **Invoices**, la correspondiente **entrada vinculada** se añadirá automáticamente a la tabla en la columna **"Invoices"**.

![Añadir las entradas vinculadas al activar la automatización](images/Ausloesen-der-Automation-Beispiel-1-1-1.png)

{{< warning  type="warning" headline="Nota importante"  text="Si añade números de factura en la columna **\\"Inv-No\\"** que **aún no** se encuentran en la tabla **Invoices**, la automatización **no** se activará y, en consecuencia, **no** se añadirá ninguna entrada vinculada a la columna, ya que la entrada correspondiente en la tabla **Invoices** simplemente aún no existe." />}}

Al hacer clic en la entrada vinculada se abre una ventana en la que puede ver el contenido de la **entrada vinculada** de la tabla **Invoices**.

![Haciendo clic en la entrada vinculada, se puede ver el contenido de la columna vinculada en la otra tabla.](images/Informationen-der-verlinkten-Spalte.png)

Además, al activarse la automatización también se añaden las **entradas vinculadas** de la tabla **Payments** a la tabla **Invoices**. En la columna **"Collected Payments"** se asigna automáticamente a cada número de factura el correspondiente **número de pago (P-000X)**. Gracias a la **automatización** puede ver, por tanto, el **pago** correspondiente a cada factura y determinar rápidamente qué facturas están pagadas y cuáles siguen pendientes.

![Añadir las entradas vinculadas al activar la automatización](images/Ausloesen-der-Automation-Beispiel-2.png)

También en esta tabla, haciendo clic en la entrada vinculada, puede abrir una ventana en la que puede ver el contenido de la **entrada vinculada** de la tabla **Payments**.

![Haciendo clic en una entrada vinculada, se puede ver el contenido de la columna vinculada en la otra tabla.](images/Informationen-der-verlinkten-Spalte-2.png)

### Más artículos útiles en la sección Automatizaciones:

- [Visión general de las automatizaciones]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [Cómo funcionan las automatizaciones]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Crear una automatización]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Gestionar y agrupar automatizaciones]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Detener automatizaciones]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Eliminar automatizaciones]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Mostrar el registro de ejecución de una automatización]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Disparadores de automatización]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Acciones de automatización]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Bloquear filas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})

### Más ejemplos interesantes de automatizaciones:

- [Bloquear filas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Añadir filas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Añadir entradas a otras tablas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Enviar notificaciones mediante automatización]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Enviar correos electrónicos mediante automatización]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
