---
title: 'Ejemplo de fórmula: Buscar una palabra en un texto'
date: 2023-01-28
lastmod: '2023-09-19'
categories:
    - 'formeln'
author: 'nsc2'
url: '/es/ayuda/formula-buscar-palabra-texto'
aliases:
    - '/es/ayuda/formelbeispiel-nach-einem-wort-in-einem-text-suchen'
seo:
    title: 'Ejemplo de fórmula SeaTable: Buscar y resaltar palabras en textos automáticamente'
    description: 'Aprende a buscar palabras en columnas de texto en SeaTable usando fórmulas y resalta los aciertos con mensajes personalizados o indicadores visuales.'
---

Las fórmulas de SeaTable le ofrecen diferentes maneras de trabajar con los datos de sus tablas. Una posibilidad es buscar **palabras en un** texto. Introduciendo la fórmula correspondiente, puede buscar automáticamente cualquier palabra en una [columna de]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) texto y obtener una sugerencia -por ejemplo, "palabra encontrada/no encontrada"- escrita como resultado en una columna de fórmulas de su tabla.

## Buscar una palabra en un texto

En el ejemplo concreto, el objetivo es buscar una **palabra** en la columna de texto **"Solicitud"** utilizando una fórmula.

![Tabla de ejemplo para buscar palabras en un texto mediante una fórmula ](images/example-table-search-words-in-text.png)

Para ello, añada primero una **columna de fórmulas** a la tabla, en cuyo editor podrá insertar después la **fórmula**.

![Introducir la fórmula en el campo de texto previsto a tal efecto](images/input-formula-example-text.jpg)

Para buscar una palabra en una columna de texto, añada primero un operador **If** a la fórmula, que encontrará en el editor de fórmulas, en la pestaña **Funciones lógicas**. Examina si se aplica o no una **condición** definida y devuelve un determinado **valor** en función del resultado positivo o negativo.

![Añade la función "si" a la fórmula.](images/add-if-to-formular.jpg)

En el siguiente paso, se amplía la fórmula con la función **buscar**, con ayuda de la cual se puede buscar una palabra concreta en la columna de texto. Encontrará la función en el editor de fórmulas, en las **funciones de texto**.

![Añadir la función de texto "find" a la fórmula](images/add-find-to-formula.jpg)

Las dos funciones van seguidas en la fórmula por la **palabra concreta** que desea buscar en la columna de texto. Escriba la palabra **entre com** illas en la fórmula.

![Añadir la palabra buscada en la columna de texto](images/add-the-word-searching-for.jpg)

El siguiente componente de la fórmula es el **nombre de la columna** en la que debe comprobarse la presencia de la palabra buscada. Es especialmente importante que el nombre de la columna esté entre **llaves**, ya que de lo contrario SeaTable **no podrá** reconocer el texto que debe comprobarse con la fórmula.

{{< warning  headline="Consejo"  text="Los **nombres de las columnas** de la tabla aparecen a la izquierda en el **editor de fórmulas** y pueden insertarse en la fórmula con un **doble clic**." />}}

![Añada el nombre de la columna para comprobar la presencia de la palabra buscada.](images/add-reference-column.jpg)

Hinter dem Spaltennamen fügen Sie die mathematische Gleichung “**1 > 0**” ein. Diese ist für die Formel von Bedeutung, da Sie angibt, dass ein spezifischer **Wert** zurückgegeben wird, sobald das gesuchte Wort **mindestens einmal** in der Text-Spalte gefunden wird. Achten Sie in der Formel darauf, die Klammer **nach** der ersten Zahl zu **schließen**. Die **Vergleichszeichen** ( > , < , = , etc.) finden Sie im Formeleditor unter **Operatoren**.

![Añadir la ecuación matemática para completar la condición](images/add-.jpg)

Por último, defina en la columna de fórmulas los **valores** que se le devuelven por **encontrar** o **no** la palabra buscada en el texto. El **primer** valor introducido aparece siempre en la columna de fórmulas si la palabra buscada se ha **encontrado** en el texto, el segundo valor en el caso contrario. Coloque siempre los valores **entre com** illas y sepárelos con una **coma**.

![Añada los valores que se devolverán si la palabra buscada está presente o ausente en la columna de la fórmula.  ](images/add-values.jpg)

Antes de confirmar, sigue siendo importante tener en cuenta que debe **cerrar el paréntesis** para que la fórmula se acepte como válida.

![Finalización de la fórmula con el cierre del corchete](images/finish-formula.jpg)

Después de confirmar la fórmula introducida, puede ver en el valor de la **columna de fórmulas** si la palabra buscada se ha encontrado en la columna de texto.

![El resultado de la fórmula aparece automáticamente en la columna de fórmulas después de confirmar la fórmula.](images/table-after-formular-search-word.png)
