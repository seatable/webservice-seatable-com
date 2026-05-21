---
title: 'Trucos y consejos para importar archivos CSV o XLSX'
date: 2022-10-15
lastmod: '2023-01-19'
categories:
    - 'import-von-daten'
author: 'nsc2'
url: '/es/ayuda/consejos-importar-csv-xlsx-seatable'
aliases:
    - '/es/ayuda/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien'
seo:
    title: 'Consejos para importar CSV/XLSX a SeaTable – evita errores'
    description: 'Aprende cómo importar datos en SeaTable sin fallos: estructura tablas, divide importaciones, verifica calidad y revisa resultados al finalizar.'
---

En SeaTable tiene la opción de **importar** tanto **archivos** **CSV** como **Excel (.xlsx)** en sus bases. Para que todo vaya según lo previsto durante la importación de datos y no se pierda ningún dato, hemos resumido para usted los **consejos y trucos** más importantes para importar archivos CSV o XLSX. Si sigue estos consejos y trucos, importará con éxito sus datos a SeaTable:

- Importar sólo estructuras de tablas
- Cree la estructura de la tabla en SeaTable antes de la importación
- Dividir la importación
- Garantizar la calidad de los datos
- Controlar la importación

## Importar sólo estructuras de tablas

A menudo surgen problemas al importar archivos Excel si contienen **estructuras** y contenidos que **no pertenecen a la tabla**. El siguiente gráfico muestra un caso así. El encabezamiento, la fecha y las columnas A y D no pertenecen a la tabla y deben eliminarse antes de la importación.

![Lista Excel con elementos erróneos](images/tipps-import.png)

**Los gráficos** tampoco se tienen en cuenta durante una importación, por lo que deben eliminarse antes del intento de importación.

## Cree la estructura de la tabla en SeaTable antes de la importación

Cuando SeaTable importa una lista de Excel, intenta determinar qué **tipo de columna** crear basándose en los **datos importados**. Los problemas surgen inevitablemente cuando SeaTable determina incorrectamente el tipo de columna y los datos no son compatibles con el tipo de columna. Por ejemplo, si SeaTable reconoce un número y, por tanto, crea una columna numérica, los textos y las palabras de esta columna ya no podrán importarse y las celdas seguirán siendo las mismas.

Aunque el reconocimiento de columnas suele funcionar de forma fiable, puede evitar fácilmente que se produzca este problema. En lugar de tener una nueva base creada por importación, cree primero usted mismo la base con todas las columnas de la tabla y luego importe sólo el contenido.

## Dividir la importación

La función de importación de SeaTable puede importar archivos Excel con **múltiples hojas de cálculo** y **decenas de miles de filas**. Sin embargo, la experiencia demuestra que cuantos más datos intente importar de una sola vez, más probabilidades tendrá de encontrar problemas.

Por lo tanto, siempre que sea posible, intente dividir la importación en **paquetes de datos más pequeños**. Mejor importar las hojas de cálculo por separado y una tras otra y dividir las tablas grandes en tablas pequeñas. De este modo, tendrá un mejor control sobre la importación y al final estará satisfecho con los datos completamente importados.

## Garantizar la calidad de los datos

La **preparación de los datos** es esencial para una importación sin problemas. Antes de importar archivos CSV o XLSX en una base, debe asegurarse siempre de que los datos se han limpiado y cumplen los requisitos de importación. Puede consultar las **limitaciones de las** [importaciones CS]({{< relref "help/startseite/import-von-daten/limitationen-beim-csv-excel-import" >}}).

## Comprobar la importación

Cada importación de datos incluye siempre una **comprobación de éxito**. No confíe en que todo ha funcionado sólo porque no recibe ningún mensaje de error. Compruebe que los datos importados **están completos** y **libres de errores** antes de empezar a procesarlos.
