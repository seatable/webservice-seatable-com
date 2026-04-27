---
title: 'Automatización de las operaciones de tratamiento de datos'
date: 2023-04-28
lastmod: '2023-05-03'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/es/ayuda/automatizar-operacion-datos-seatable'
aliases:
    - '/es/ayuda/datenverarbeitungsoperation-per-automation-ausfuehren'
seo:
    title: 'Automatice operaciones de datos en SeaTable'
    description: 'Ejecu­te operaciones de procesamiento de datos con automatizaciones y ahorre tiempo: cálculos, enlaces y más, de forma recurrente y segura.'

---

Con la ayuda de las automatizaciones, ya no tiene que realizar una operación de tratamiento de datos manualmente, sino que puede hacer que se realice automáticamente. La variedad de [operaciones]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) de tratamiento de datos disponibles -desde cálculos matemáticos hasta la creación de vínculos entre valores de distintas tablas- abre nuevas posibilidades para automatizar sus procesos de trabajo.

## Realizar una operación de tratamiento de datos por automatización

![Realizar operaciones de tratamiento de datos mediante automatización](images/how-to-use-automations-for-locking-rows-3.png)

1. Haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} en la cabecera Base y luego en **Reglas de automatización**.
2. Haga clic en **Añadir Regla**.
3. Asigne un **nombre** a la automatización y defina la **tabla** y la **vista en las** que debe activarse.
4. Defina un **evento desencadenante que active** la automatización.
5. Haga clic en **Añadir Acción** y seleccione **Ejecutar Operación de Proceso de Datos** como acción automatizada.
6. Seleccione cualquier **operación de tratamiento de datos**.
7. Realice los **ajustes** necesarios (por ejemplo, tabla, columna de origen, columna de resultado) en la **operación de tratamiento de datos**.
8. Confirme con **Enviar**.

## Creación de la automatización

Una vez determinado en qué **tabla** y **vista** debe desencadenarse **la** automatización, defina el [evento desencadenante]({{< relref "help/base-editor/automationen/automations-trigger" >}}). Actualmente, sólo un desencadenante **periódico** puede dar lugar a una operación de tratamiento de datos. Por lo tanto, debe definir un **momento** en el que la automatización deba activarse diaria, semanal o mensualmente.

![Selección del desencadenante de automatización de la acción: Ejecutar operación de tratamiento de datos](images/select-trigger-for-data-operation-per-automation.png)

{{< warning  headline="Nota importante"  text="La acción automatizada **Ejecutar la operación de tratamiento de datos** está a su disposición **exclusivamente** disponible en el siguiente evento desencadenante:" />}}

!["Activador periódico]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_periodischer_trigger)

A continuación, seleccione **Ejecutar operación de tratamiento de datos** como acción automatizada y elija la [operación de tratamiento de datos]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) deseada.

![Añadir la acción automatizada](images/add-an-action.png)

![Selección de la operación de tratamiento de datos que se ejecutará como acción automatizada de la automatización](images/select-data-operation-for-automation.png)

Dispone de las siguientes **operaciones de tratamiento de datos**:

- [Calcular valores acumulados]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}})
- [Calcular variaciones]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calcular porcentaje]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})
- [Calcular ranking]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Transferir nombres de usuario]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})
- [Comparar y copiar]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})

En el siguiente paso, realice **ajustes** específicos en la **operación de tratamiento de datos** que deba ejecutarse mediante la automatización. Dependiendo de la operación seleccionada, se le pedirá que defina **tablas** y/o **columnas** (por ejemplo, columna de origen y de resultado) que desea utilizar para los cálculos matemáticos o para establecer relaciones entre valores de distintas tablas.

![Ajustes específicos que deben realizarse en la operación de tratamiento de datos](images/specific-settings-for-data-processing-operation.png)

Finalmente, confirme la automatización con **Enviar** para guardarla y ejecutarla en el momento definido del desencadenante, o haga clic en **Ejecutar ahora** para que la automatización se ejecute **directamente**.

![Guardar la automatización o ejecutarla directamente](images/cancel-run-now-or-submit-automation.png)

## Ejemplo de aplicación

Un caso de uso concreto de este tipo de automatización podría darse, por ejemplo, si desea registrar en su tabla el número de visitas diarias a un sitio web. Para ello, desea **sumar** fila por fila, en una nueva columna, las **cifras de visitas** de cada día, recogidas en una [columna numérica]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}) existente.

Hasta ahora, [el cálculo de las cifras de visitas acumuladas mediante una operación de tratamiento de datos]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}}) sólo era posible **manualmente**. Con una automatización correspondiente, a partir de ahora es posible calcular las cifras de visitas acumuladas **todos los días** a una hora fija de forma **automática**.

Para la implementación, necesita en primer lugar una tabla en la que los distintos **días** estén registrados en una [columna de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) y las **cifras de visitas** al sitio web en una [columna numérica]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}).

![Tabla de ejemplo para el caso de uso de la automatización: Calcular valores acumulados](images/Beispiel-Tabelle-automation-data-processing-kumulierte-werte-berechnen.png)

A continuación, añada a la tabla una **segunda columna numérica** en la que, tras cada ejecución de la automatización, se calcularán los valores acumulados. La nueva columna _Cumulated Visitors_, inicialmente vacía, actúa en la operación de tratamiento de datos como **columna de resultado**, mientras que la columna _Unique Visitors_ es la **columna de origen**.

![Añadir una segunda columna numérica](images/Beispiel-Tabelle-automation-data-processing-kumulierte-werte-berechnen-2.png)

Para crear la automatización, siga los pasos descritos en la sección [Creación de la automatización]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}}). Además, seleccione la columna _Unique Visitors_ como **columna de origen** y la columna recién añadida _Cumulated Visitors_ como **columna de resultado**.

![Selección de la columna de origen y de resultado](images/auswahl-quell-und-ergebnisspalte-im-anwendungsfall.png)

Tras confirmar la automatización, SeaTable calcula diariamente, a la hora seleccionada, el **número acumulado de visitantes del sitio web** y lo escribe automáticamente en la columna de resultado. El cálculo automático de los valores acumulados requiere, naturalmente, que el **número de visitantes del sitio web del día anterior** se escriba diariamente, **antes** de la ejecución de la automatización, en la columna _Unique Visitors_.

Tabla **antes** de activarse la automatización:

![Tabla de ejemplo antes de activarse la automatización](images/Beispiel-Tabelle-vor-Ausloesung-der-Auomation-Kumulierte-Werte-Berechnen.png)

Tabla **después** de activarse la automatización:

![Tabla de ejemplo después de activarse la automatización](images/Beispiel-Tabelle-nach-Ausloesung-der-Automation-Kumulierte-Werte-berechnen.png)
