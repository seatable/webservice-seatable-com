---
title: 'La fórmula Findmin'
date: 2023-02-13
lastmod: '2026-11-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/es/ayuda/formula-findmin'
aliases:
    - '/es/ayuda/die-findmin-formel'
seo:
    title: 'Fórmula Findmin en SeaTable – obtener el valor vinculado mínimo'
    description: 'Aprende a usar la fórmula Findmin en SeaTable para hallar el valor mínimo de registros vinculados entre varias tablas numéricas.'
---

La **fórmula Findmin** busca el **valor mínimo** entre las entradas de la columna vinculada y lo devuelve. Esto es útil si hay **varias entradas** en la tabla vinculada que hacen referencia al mismo registro (por ejemplo, de una persona o categoría) en otra tabla.

## Para qué puede utilizar la fórmula Findmin

Puede utilizar la fórmula Findmin con todos los valores alfanuméricos para determinar el **valor mínimo**. Supongamos que utiliza SeaTable para la [planificación presupuestaria]({{< relref "templates/finance/budget-plan" >}}), donde una tabla almacena los gastos y otra tabla las categorías. A continuación, puede vincular cada gasto con una categoría. Para saber cuál fue **el gasto más bajo por categoría**, puede utilizar la **fórmula Findmin** para mostrar el valor menor de todos los gastos vinculados.

![fórmula findmin](images/findmin.png)

## Para utilizar la fórmula Findmin

### Añadir un enlace a la tabla

Consulte el [artículo sobre la columna de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) para obtener información sobre cómo crear una columna del tipo **Enlace a otros registros**. Este es un requisito básico para poder utilizar la fórmula Findmin.

{{< warning headline="Se necesitan varias filas enlazadas" >}}

El uso de la fórmula Findmin sólo tiene sentido si la opción **Limitar los enlaces a una fila como máximo** está desactivada en los ajustes de una columna de enlace. Si la opción estuviera activada, la fórmula Findmin mostraría siempre el mismo valor que la única fila enlazada.

{{< /warning >}}

### Añadir una columna con la fórmula Findmin

![fórmula findmin](images/findmin.gif)

1. Cree una nueva columna del tipo **Fórmula para los enlaces**.
2. Establezca la opción **Findmin** como fórmula.
3. Seleccione la columna creada anteriormente del tipo **Vincular a otras entradas** de esta tabla.
4. Defina ahora la **columna de consulta en la tabla vinculada** cuyo registro con el valor mínimo debe mostrarse en la columna Findmin.
5. Seleccione la **columna de comparación en la tabla vinculada** en la que desea determinar el valor mínimo.
6. Haga clic en **Enviar**.
