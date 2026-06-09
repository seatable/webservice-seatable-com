---
title: 'Ejemplo de fórmula: Fusión de columnas de texto con ayuda de una fórmula'
date: 2023-01-28
lastmod: '2023-09-18'
categories:
    - 'formeln'
author: 'nsc2'
url: '/es/ayuda/ejemplo-formula-unir-columnas-texto'
aliases:
    - '/es/ayuda/formelbeispiel-zusammenfuehren-von-text-spalten-mit-hilfe-einer-formel'
seo:
    title: 'Ejemplo de fórmula: unir columnas de texto en SeaTable'
    description: 'Aprende a usar fórmulas en SeaTable para fusionar varias columnas de texto en un solo campo, útil para nombres completos y más.'
---

Las fórmulas de SeaTable le ofrecen varias formas de trabajar con los datos de sus tablas. Una de ellas es la fusión de contenidos de diferentes [columnas de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}). Con la ayuda de una fórmula correspondiente, puede combinar cualquier número de contenidos de diferentes columnas en una columna de fórmula.

## Fusión de columnas de texto

En el ejemplo concreto, se trata de utilizar una fórmula para fusionar el contenido (apellido, nombre y cargo) de las tres primeras columnas en un **nombre completo**.

![Tabla de ejemplo para fusionar distintos contenidos en una columna de fórmulas](images/example-table-zusammenfuehren-von-inhalten-mit-Formel.png)

Para ello, añada primero una **columna de fórmulas** a la tabla, en cuyo editor podrá insertar después la fórmula.

![Añadir una fórmula en el campo de texto previsto a tal efecto](images/insert-formular-example-1.png)

Para combinar el contenido de diferentes columnas de texto en una sola columna, siempre debe hacer referencia a los **nombres de las columnas** en las que se encuentra el contenido correspondiente en su tabla. Es especialmente importante que los nombres de las columnas estén entre **corchetes**, ya que de lo contrario SeaTable **no podrá** reconocer los contenidos que se van a combinar.

{{< warning  headline="Consejo"  text="Los **nombres de las columnas** de la tabla abierta aparecen a la izquierda en el **editor de fórmulas** y pueden insertarse en la fórmula con un **doble clic**." />}}

![Cuando haga referencia a nombres de columnas en sus tablas, enciérrelos siempre entre llaves](images/verweis-auf-spaltennamen-in-formel-beispiel-2.png)

Para combinar el contenido de las columnas de texto en una columna de fórmula, disponga primero los nombres de las columnas en el **orden** deseado en la fórmula y separe cada uno de ellos con un **símbolo &**, que encontrará en el editor de fórmulas con los **operandos**.

![Coloque los nombres de las distintas columnas en el orden deseado en la fórmula y sepárelos con el símbolo &.](images/insert-symbols.png)

Para separar los distintos contenidos con un **espacio**, añada un **símbolo &** y **dos comillas (arriba)** **después de** los dos primeros nombres de columna.

![Añadir un símbolo & adicional y dos comillas después de los dos primeros nombres de columna](images/insert-and-22-22-to-the-formular.png)

Tras confirmar la fórmula introducida, el contenido de las columnas de texto se fusiona automáticamente y el **resultado** aparece automáticamente en la columna de fórmulas.

![Columna Fórmula después de confirmar la fórmula introducida.](images/table-example-2-after-formular.png)

{{< warning  headline="Consejo profesional" >}}

Siempre que utilice columnas de texto en una fórmula y estas columnas también puedan estar vacías, se recomienda utilizar la función _recortar( )_. Esta función elimina los espacios al principio y al final de un texto. La fórmula completa es entonces, por ejemplo,

```
trim( {Title} & " " & {Surname} & " " & {Name} )
```

{{< /warning >}}
