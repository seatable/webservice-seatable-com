---
title: 'Colorear celdas en vistas de tabla'
date: 2022-10-26
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'vge'
url: '/es/ayuda/colorear-celdas'
aliases:
    - '/es/ayuda/einfaerben-von-zellen'
seo:
    title: 'Colorear celdas en vistas de tabla de SeaTable según reglas y valores propios'
    description: 'Descubre cómo colorear celdas en SeaTable usando reglas o valores personalizados y resalta datos para analizar mejor. Guía detallada por pasos.'
weight: 28
---

A diferencia de Excel, en las vistas de tabla de SeaTable no puede simplemente colorear las celdas a su gusto, sino que debe colorearlas según las **reglas** que establezca o en función de los **valores** de una **columna**. ¿Suena complicado? Pero no lo es.

{{< warning  headline="Nota" >}}

Además de la opción de **colorear las celdas**, también existe la posibilidad de colorear [las filas]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}). En este caso, sin embargo, las celdas no se colorean, sino que se colocan marcas de color al principio de las filas.

{{< /warning >}}

## Colorear por reglas o por valores

Cada columna en una vista de tabla ofrece la posibilidad de **Colorear las celdas de la columna**:  
![Opción de formato de columna mostrada en SeaTable](images/color-cells.png)

SeaTable se comportará de forma diferente dependiendo del **tipo de columna** para la que llame a esta opción. Para [columnas numéricas]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}), puede utilizar tanto reglas como valores para colorear. Para todos los demás tipos de columnas, sólo están disponibles las reglas para colorear.

![Vista general de colorear celdas por reglas o valores](images/color-cells-rules-values.png)

## Para colorear las celdas según una regla

![Ejemplo: colorear celdas usando una regla](images/einfaerben-von-zellen-beispiel-1-1.gif)

1. Haga clic en el **símbolo del triángulo** en la cabecera de la tabla de una columna.
2. Seleccione la opción **Colorear celdas de la columna**.
3. Ir a **Reglas de uso**.
4. Haga clic en **Añadir Regla**.
5. Haga clic en la nueva línea que aparece para definir la regla.
6. Seleccione una **columna** y decida una **condición** en el campo central.
7. Introduzca el **valor** al que se asocia la condición.
8. Haga clic en el **icono del triángulo de color** situado delante de la regla para abrir el selector de color y cambiar el color de las celdas a las que se aplica su regla.

Al utilizar una regla, se colorean **todas las celdas** de una columna a las que **se aplica** una regla. Por ejemplo, una regla de este tipo podría ser: "Colorear de amarillo todas las celdas con una valoración de tres o más estrellas".

![Resultado: una regla colorea celdas coincidentes en amarillo](images/Einfaerben-von-Zellen-mit-einer-Regel.png)

Puede crear **varias reglas con diferentes colores** por columna.

![Varias reglas con diferentes colores en una columna](images/Einfaerben-von-Zellen-mit-mehreren-Regeln.png)

También puede definir **varias condiciones** por regla, que pueden referirse a todas las columnas de la tabla. Por ejemplo, colorear la [columna de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) con el titular de un artículo si el **estado** no es "terminado", la **fecha de publicación** es futura y ya hay una **imagen** disponible.

![Regla con múltiples condiciones para colorear celdas](images/Regel-mit-mehreren-Bedingungen-fuer-die-farbliche-Zeilenmarkierung.png)

{{< warning  headline="Diferentes opciones según el tipo de columna"  text="La **selección** de posibles condiciones se adapta dinámicamente al tipo de columna." />}}

## Para colorear las celdas por valores

![Ejemplo: colorear celdas según valores en SeaTable](images/einfaerben-von-zellen-beispiel-2-1.gif)

1. Haga clic en el **símbolo del triángulo** en la cabecera de la tabla de una columna.
2. Seleccione la opción **Colorear celdas de la columna**.
3. Ir a **Utilizar valores**.
4. Haga clic en la **selección de** colores para elegir entre más colores
5. Decida a partir de qué **valor** y hasta qué valor desea colorear las celdas.
6. Haga clic en **Enviar**.

Con la opción **Utilizar valores** se colorea toda la columna. Cuanto mayor sea un valor en todo el espectro, más oscuro o claro será el color de la célula.

![Degradado de claro a oscuro según valores de celda](images/einfaerben-von-zellen-2.png)

Este tipo de coloración le ayuda a hacer visibles de forma rápida y sencilla **los valores atípicos** (es decir, valores particularmente pequeños o particularmente grandes) en una columna.

## Localizar duplicados

![Ejemplo: resaltar valores duplicados en una columna](images/einfaerben-von-zellen-beispiel-3.gif)

1. Haga clic en el **símbolo del triángulo** en la cabecera de la tabla de una columna.
2. Seleccione la opción **Colorear celdas de la columna**.
3. Ir a **Resaltar duplicados**.

Con la ayuda de la opción **Resaltar duplicados**, se pueden encontrar rápidamente valores idénticos en una columna.

## Preguntas frecuentes

### Rellenar todas las celdas con el mismo color

Para ello, defina una regla que se aplique a todas las celdas deseadas. Por ejemplo, puede colorear todas las celdas **rellenas** de una columna seleccionando la condición **no está vacía**.

![Ejemplo FAQ: colorear todas las celdas completas](images/einfaerben-von-zellen-6.png)

### Color en las próximas citas

Aquí tiene dos opciones para colorear las celdas respectivas de una columna de fecha. O bien selecciona la condición es **en o después** y una **fecha exacta** - o bien selecciona la opción **es dentro** y un periodo en el futuro.

![Ejemplo: resaltar fechas próximas con colores](images/einfaerben-von-zellen-7.png)

### Colorear una fecha específica

Seleccione la opción **es igual a** e introduzca la fecha correspondiente.

![Ejemplo: colorear una fecha específica](images/einfaerben-von-zellen-8.png)
