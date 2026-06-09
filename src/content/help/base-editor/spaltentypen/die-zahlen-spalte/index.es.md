---
title: 'La columna de los números'
date: 2023-01-08
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'ssc'
url: '/es/ayuda/columna-numerica'
aliases:
    - '/es/ayuda/die-zahlen-spalte'
seo:
    title: 'Columna numérica en SeaTable – formatos y opciones'
    description: 'Aprende a usar columnas numéricas en SeaTable para sumas, porcentajes y monedas. Ajustes, validación y consejos prácticos.'
weight: 3
---

En SeaTable puede utilizar la **columna numérica** de muchas formas para trabajar con números de cualquier tipo (por ejemplo, número de artículos, porcentajes o precios en distintas monedas).

## Área de aplicación de la columna numérica

El uso de **columnas numéricas** le permite, por ejemplo, **calcular valores** con fórmulas y crear diagramas y estadísticas. Sin embargo, no es adecuado para guardar cadenas de cualquier longitud (por ejemplo, números de cuenta), ya que el redondeo se produce con más de 15 dígitos. En este caso, debe utilizar la [columna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

Además, SeaTable ofrece otras columnas que a veces se ajustan mejor a los valores que se van a almacenar:

- Duración y periodos = [columna de duración]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})
- Fecha y hora = [columna de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- Puntuaciones = [columna de calificación]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})
- Números de serie = [Autonumeración]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- Números de teléfono = [columna del número de teléfono]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})
- Geoinformación = [columna de geolocalización]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}})

## Añadir una columna numérica

![Añadir una columna numérica](images/hinzufuegen-einer-zahlenspalte.gif)

1. Haga clic en el **signo más** situado a la derecha de la última columna.
2. Dale un **nombre** a la columna.
3. Seleccione **Número** como tipo de columna.
4. Decide un **formato** (por ejemplo, número, porcentaje o moneda).
5. También puede configurar los detalles haciendo clic en **Otros ajustes**.
6. Añade la columna con **Enviar**.

## Ajustes de formato

También puede editar y ajustar el **formato de los números** a posteriori. Para ello, abra primero el menú desplegable con las **opciones de columna** a través del triángulo {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} situado en la cabecera de la columna y, a continuación, haga clic en {{< seatable-icon icon="dtable-icon-set-up" color="grey" >}} **Ajustes de formato**.

Ahora puede seleccionar un **formato** diferente, establecer **separadores** **decimales** y de **miles** y cambiar el número de **decimales**.

### Formatos disponibles de la columna numérica

Están disponibles los siguientes formatos de número:

- **Número**

    Utilización de un número simple, por ejemplo para el número de artículos.

- **Porciento**

    Uso de porcentajes, por ejemplo, para el progreso en la realización de tareas.

- **Monedas (yuan, dólar y euro)**

    Utilización de distintas monedas, por ejemplo para los precios de los productos.

- **Moneda personalizada**

    Utilización de una divisa personalizada en la que el símbolo de la divisa puede introducirse individualmente.

## Establecer el valor por defecto y validar la entrada

Puede [definir un valor por defecto]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) para cada columna numérica, que se introducirá automáticamente en cada fila que añada a su tabla.

Para identificar directamente los **errores** y los **valores extremos**, también puede **validar** la **entrada**. Para ello, defina un **intervalo numérico** en el que deben situarse los valores de la columna; las celdas con un valor superior o inferior se resaltan entonces en color.

Puede realizar estos ajustes al crear la columna numérica o posteriormente:

1. Abra el menú desplegable con las **opciones de columna** a través del triángulo {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} en la cabecera de la columna.
2. A continuación, haga clic en **Personalizar tipo de columna**.
3. Haga clic en **Más ajustes** y active los **controles deslizantes** correspondientes en la parte inferior.

![Configuración del formato de las columnas numéricas](images/Format-settings-of-number-columns.png)
