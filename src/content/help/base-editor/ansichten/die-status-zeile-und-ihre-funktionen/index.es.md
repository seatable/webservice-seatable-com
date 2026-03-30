---
title: 'La barra de estado y sus funciones'
date: 2023-02-21
lastmod: '2023-02-21'
categories:
    - 'ansichtsoptionen'
author: 'nsc2'
url: '/es/ayuda/barra-de-estado-y-sus-funciones'
aliases:
    - '/es/ayuda/die-status-zeile-und-ihre-funktionen'
seo:
    title: 'Barra de estado en SeaTable – contar y calcular valores'
    description: 'Conoce cómo usar la barra de estado: cuenta filas, calcula sumas, promedios, medianas y otros valores automáticamente.'
weight: 30
---

La **barra de estado** se encuentra en la parte inferior de sus tablas y cumple básicamente dos funciones diferentes, que se explican con más detalle en este artículo:

- **Función 1**: Contar las filas de una vista
- **Función 2**: Indicación de un valor calculado a partir de todas las entradas (por ejemplo, suma, media, etc.) en el caso de columnas numéricas.

Gracias a la barra de estado, siempre tendrá a la vista estos **valores estadísticos** básicos en cuanto abra una tabla.

## Contar las filas de una vista

La barra de estado indica en el borde inferior izquierdo el número de todas las **filas** que hay en la vista de **tabla** abierta en ese momento. Si [filtra en una]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) vista, la barra de estado cuenta sólo las entradas restantes de la tabla.

![La barra de estado indica siempre el número de filas de la vista de tabla abierta en ese momento](images/status-cell-function-1.jpg)

Además, puede [seleccionar líneas]({{< relref "help/base-editor/zeilen/mehrere-zeilen-selektieren" >}}) individuales – entonces la barra de estado se refiere sólo a las entradas seleccionadas.

## Indicación de un valor calculado a partir de todas las entradas

Para las **columnas basadas en números**, la barra de estado de cada columna da un **valor** calculado a partir de todas las entradas.

![Valores calculados en las líneas de estado](images/the-status-cell-function-2-1.png)

## Opciones de cálculo

Para las columnas basadas en números, las siguientes **opciones de cálculo** están disponibles en la barra de estado:

- Cálculo de la **suma de** todas las entradas de la columna
- Cálculo del **valor medio** de todas las entradas de la columna
- Cálculo de la **mediana** a partir de todas las entradas de la columna
- Determinar el **valor máximo** de todas las entradas de la columna
- Determinar el **valor mínimo** de todas las entradas de la columna
- Ningún cálculo

![Opciones de cálculo de la barra de estado](images/berechnungsoptionen-status-zeile.png)

## Tipos de columnas y formatos compatibles

Para los siguientes tipos de columna, la barra de estado refleja un valor calculado:

- [Columnas numéricas]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
    - Número
    - Porcentaje
    - Moneda
- [Columnas de duración]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})
- [Columnas de calificación]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})
- Valores numéricos en [columnas de fórmulas]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

Para los siguientes tipos de columnas, la barra de estado **no** refleja un valor calculado, aunque (pueden) contener números:

- [Columnas de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- [Fecha y hora de creación]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) y [Última modificación]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})
- [Autonumeración]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- Números en [columnas de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})
