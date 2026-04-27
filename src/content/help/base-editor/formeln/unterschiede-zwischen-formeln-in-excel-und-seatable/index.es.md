---
title: 'Diferencias entre fórmulas en Excel y SeaTable'
date: 2023-02-03
lastmod: '2023-02-03'
categories:
    - 'formeln'
author: 'ssc'
url: '/es/ayuda/diferencias-entre-formulas-excel-seatable'
aliases:
    - '/es/ayuda/unterschiede-zwischen-formeln-in-excel-und-seatable'
seo:
    title: 'Diferencias entre fórmulas en Excel y SeaTable'
    description: 'Descubre las diferencias clave entre las fórmulas de Excel y SeaTable: referencia a celdas o columnas, lógica y consejos de uso.'
---

¿Es usted un usuario de Excel familiarizado con la escritura de fórmulas y acaba de empezar a utilizar SeaTable? Entonces este artículo es para usted. Aunque los principios de las funciones de fórmula en SeaTable son similares, hay algunas diferencias importantes que debe aprender al principio y que le compensarán si quiere convertirse en un experto en fórmulas SeaTable.

## Diferencia central

La diferencia más importante en la función de fórmula de SeaTable y Excel es el **rango efectivo de las fórmulas**.

Mientras que en **Excel** puede introducir una fórmula en cualquier celda, que luego hace referencia a cualquier otra celda de la hoja de cálculo, las fórmulas en **SeaTable** hacen referencia a **columnas enteras** y no a celdas concretas.

Dado que SeaTable actúa como una [base de datos relacional]({{< relref "posts/relationale-datenbank" >}}) en este contexto, las fórmulas se aplican a toda la columna de una tabla, de modo que la misma fórmula se aplica a cada entrada de esa columna.

## Referencia de líneas

### Excel

Cualquier celda en particular puede ser referenciada en otra celda. Por ejemplo, para determinar el origen de cada compra en una tabla, se escribiría una fórmula que hiciera referencia a cada  
celda -como A3- para comprobar el tipo de fuente.

La fórmula utilizada a continuación es  
**\= IF(A3 = "Online", "Web", "Tienda")**

![Referenciación de celdas en Excel](images/table-excel-vs.-seatable-1.png)

La fórmula se refiere a _celdas_ específicas, como A3.

### SeaTable

Una fórmula se aplica siempre a toda una _columna_ y **no a** celdas específicas. Por ejemplo, para identificar el origen de cada compra, escribiría una fórmula que haga referencia a la columna {Tipo de compra} y la fórmula comprobará esa columna para cada entrada de la tabla.

La fórmula utilizada a continuación es:

**IF({Tipo de compra}= "En línea", "Web", "Tienda")**

![Referencia de columnas en SeaTable](images/table-excel-vs-seatable-2.png)

La fórmula se refiere a columnas enteras, como {Tipo de compra}.

## Valores de otras tablas

Las fórmulas de SeaTable funcionan dentro de _las tablas_, no a través de _las bases_.  
Al igual que en el caso anterior, por defecto las fórmulas de SeaTable sólo hacen referencia a _columnas_ dentro de la misma _tabla_. Sin embargo, hay formas de tomar un valor de otra tabla para referenciarlo en un campo de fórmula (este enfoque utiliza registros enlazados, que se tratan con más detalle [aquí]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) ).

### Excel

Para hacer referencia a un registro de otra tabla, debe escribir referencias específicas a la otra tabla en un formato como el siguiente:

**\=IF(Tareas!B1='Mejoras en el hogar',Tareas!A1,0).**

A continuación, deberá aplicar esta fórmula a cada celda en la que desee ejecutar la fórmula (cambiando las referencias de celda para cada celda en la que desee ejecutar la fórmula).

![Referencia a otro conjunto de datos en Excel](images/table-excel-vs-seatable-3.png)

### SeaTable

Para hacer referencia a un registro de otra tabla, primero puede vincularlo utilizando el tipo de columna **"Vincular a otros registros"**. Una vez que un registro de una tabla, por ejemplo "Proyectos", está vinculado a un registro de otra tabla, por ejemplo "Tareas", puede hacer referencia a cada fila de ambas tablas utilizando una **columna de** **búsqueda**, **rollup** o **recuento**.

En el siguiente ejemplo, se utiliza una **columna de rollup** para consultar fácilmente los costes de las tareas individuales asociadas a un proyecto y sumar los gastos para determinar el coste total del proyecto.

![Columna de Rollup para referenciar el coste de cada tarea asociada a un proyecto y totalizar los gastos para determinar el coste total del proyecto.](images/reference-to-other-bases.gif)

La función crea un abanico de posibilidades para escribir fórmulas tanto sencillas como complejas para referenciar datos entre tablas.
