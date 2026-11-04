---
title: 'Schritt 5: Auswertungen mit Hilfe der Verknüpfungen'
date: 2024-08-30
lastmod: '2024-09-05'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/es/ayuda/paso-5-analisis-con-vinculos'
aliases:
    - '/es/ayuda/schritt-5-auswertungen-verknuepfungen'
seo:
    title: 'Paso 5: Análisis con vínculos en SeaTable'
    description: 'Aprende a usar vínculos en SeaTable para crear análisis estadísticos rápidos y precisos que resuman y conecten tus datos automáticamente.'

---

Ahora hemos vinculado los registros de datos de ambas tablas. Es importante que este enlace no sea unilateral. Si enlaza la tabla `Categories` verá que también se ha añadido una nueva columna que muestra los enlaces. En nuestro caso, esto significa que una incidencia está vinculada a una categoría, y que una categoría puede estar vinculada a muchas incidencias.

Todavía no hemos obtenido ningún beneficio directo de los enlaces, pero esto está a punto de cambiar: Con la ayuda de los enlaces, podemos crear análisis estadísticos en cuestión de segundos. Por ejemplo, podemos determinar fácilmente a cuánto asciende la suma de todos los gastos de la categoría `Travel` es.

## Aumentar la altura de la línea

En primer lugar, aumente la altura de la fila en la tabla `Categories` para ver más enlaces. Encontrará la opción correspondiente `{{< seatable-icon icon="dtable-icon-row-height-default" >}}` en la fila situada sobre el nombre de la columna. También puede arrastrar columnas individuales para ver más contenido.

![Vista de tabla con altura de filas ajustada para ver mejor las vinculaciones](images/level1-row-height.png)

## Análisis de las categorías

Ahora cree una nueva columna en la tabla `Categories` a.

> Nombre: `Sum`
>
> Tipo de columna: `{{< seatable-icon icon="dtable-icon-link-formulas" >}} Enlazar fórmula`
>
> Fórmula: `rollup`
>
> Columna de enlace en esta tabla: `Expenses`
>
> Columna a resumir: `{{< seatable-icon icon="dtable-icon-number" >}} Amount`
>
> Método de resumen: `Suma`

![Columna de fórmula de enlace «Sum» con ajuste rollup para sumar importes vinculados](images/lvl1-rollup.png)

A continuación, puede cambiar el formato de la columna `Sum` a euros para que los totales mostrados tengan el formato correspondiente en euros.

## Cálculo automático con cada cambio

¿No es fantástico? En la columna `Sum` los gastos totales de cada categoría se muestran siempre automáticamente. Aunque haga clic en otros gastos de la `Expenses` el total se actualiza inmediatamente.

Por supuesto, eso no es todo. Puede limitar el análisis a años concretos o añadir condiciones adicionales. A medida que adquiera más experiencia con SeaTable, podrá crear este tipo de análisis con sólo unos clics.

Esto nos lleva al final de esta sección. Desplázate hasta el final y pasa al sexto y penúltimo tema de este curso online.

{{< warning  headline="Análisis estadísticos como un profesional"  text="SeaTable ofrece muchas más opciones para analizar estadísticamente sus datos. Así que puede esperar con impaciencia el segundo curso en línea, en el que sin duda examinaremos este tema con más detalle." />}}

## Artículo de ayuda con más información

- [Ajustar la altura de la fila en las vistas de tabla]({{< relref "help/base-editor/ansichten/zeilenhoehe-anpassen" >}})
- [La fórmula Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}})
