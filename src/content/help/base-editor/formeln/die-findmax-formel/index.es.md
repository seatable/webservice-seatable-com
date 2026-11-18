---
title: 'La fórmula Findmax'
date: 2023-02-13
lastmod: '2026-11-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/es/ayuda/formula-findmax-seatable'
aliases:
    - '/es/ayuda/die-findmax-formel'
seo:
    title: 'Fórmula Findmax de SeaTable: determinar el valor máximo de registros vinculados'
    description: 'Aprenda a usar la fórmula Findmax en SeaTable para obtener el valor más alto de varias entradas vinculadas, con ejemplos prácticos y más.'
---

La **fórmula Findmax** busca el **valor máximo** entre las entradas de la columna vinculada y lo devuelve. Esto es útil si hay **varias entradas** en la tabla vinculada que hacen referencia al mismo registro (por ejemplo, de una persona o categoría) en otra tabla.

## Para qué puede utilizar la fórmula Findmax

Puede utilizar la fórmula Findmax con todos los valores alfanuméricos para determinar el **valor máximo**. Supongamos que utiliza SeaTable para la [planificación presupuestaria]({{< relref "templates/finance/budget-plan" >}}), donde una tabla almacena los gastos y otra tabla las categorías. A continuación, puede vincular cada gasto con una categoría. Para saber cuál fue **el gasto más alto por categoría**, puede utilizar la **fórmula Findmax** para mostrar el valor mayor de todos los gastos vinculados.

![fórmula findmax](images/findmax.png)

## Para utilizar la fórmula Findmax

### Añadir un enlace a la tabla

Consulte el [artículo sobre la columna de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) para obtener información sobre cómo crear una columna del tipo **Enlace a otros registros**. Este es un requisito básico para poder utilizar la fórmula Findmax.

{{< warning headline="Se necesitan varias filas enlazadas" >}}

El uso de la fórmula Findmax sólo tiene sentido si la opción **Limitar los enlaces a una fila como máximo** está desactivada en los ajustes de una columna de enlace. Si la opción estuviera activada, la fórmula Findmax mostraría siempre el mismo valor que la única fila enlazada.

{{< /warning >}}

### Añadir una columna con la fórmula Findmax

![fórmula findmax](images/findmax.gif)

1. Cree una nueva columna del tipo **Fórmula para los enlaces**.
2. Establezca la opción **Findmax** como fórmula.
3. Seleccione la columna creada anteriormente del tipo **Enlace a otros registros** de esta tabla.
4. Defina ahora la **columna de consulta en la tabla vinculada** cuyo registro con el valor máximo debe mostrarse en la columna Findmax.
5. Seleccione la **columna de comparación en la tabla vinculada** en la que desea determinar el valor máximo.
6. Haga clic en **Enviar**.
