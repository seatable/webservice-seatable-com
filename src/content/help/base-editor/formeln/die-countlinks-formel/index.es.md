---
title: 'La fórmula Countlinks'
date: 2023-01-11
lastmod: '2023-01-24'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/es/ayuda/countlinks-formula-seatable'
aliases:
    - '/es/ayuda/die-countlinks-formel'
seo:
    title: 'Countlinks en SeaTable: contar registros relacionados'
    description: 'Con Countlinks cuente automáticamente las entradas enlazadas con una fila. Ideal para listas de participantes, análisis o cualquier tipo de enlace múltiple.'

---

La fórmula Countlinks cuenta el número de entradas enlazadas del tipo de columna **Enlace a otras entradas** de la fila correspondiente.

{{< warning  headline="La vinculación de tablas es un requisito básico" >}}

Sólo puede crear una columna con la fórmula Countlinks si ha enlazado dos tablas. Lea [aquí cómo crear un enlace de este tipo]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

{{< /warning >}}

## Ámbito de aplicación de la fórmula Countlinks

La **fórmula Countlinks** debe utilizarse siempre que desee mostrar el **número de entradas enlazadas con una fila**.

Por ejemplo, al planificar un taller, puede mostrar el número de participantes inscritos en una tabla aparte. La [columna de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) registraría así los nombres de todos los participantes.

![La fórmula Countlinks.](images/countlinks-2.png)

El uso de la fórmula Countlinks sólo tiene sentido si la opción **Limitar los enlaces a una fila como máximo** está desactivada en los ajustes de una columna de enlace. Si la opción estuviera activada, en el campo de la fórmula Countlinks siempre aparecería un uno (= una única fila enlazada).

## Creación de una fórmula Countlinks

![La fórmula Countlinks.](images/countlink.gif)

1. Cree una nueva columna del tipo **Fórmula para los enlaces**.
2. Dale a la columna un **nombre** adecuado.
3. Establezca la opción **Countlinks** como fórmula.
4. Seleccione ahora la **columna de** enlace cuyas entradas desea contar en el campo **Seleccionar** columna de enlace en **esta tabla**.
5. Haga clic en **Enviar**.
