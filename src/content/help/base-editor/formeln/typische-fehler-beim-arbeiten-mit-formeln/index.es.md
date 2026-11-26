---
title: 'Errores típicos al trabajar con fórmulas'
date: 2023-05-03
lastmod: '2023-05-03'
categories:
    - 'formeln'
author: 'nsc2'
url: '/es/ayuda/errores-formulas-seatable'
aliases:
    - '/es/ayuda/typische-fehler-beim-arbeiten-mit-formeln'
seo:
    title: 'Errores comunes de fórmulas en SeaTable: solución'
    description: 'Identifique y corrija errores comunes en fórmulas de SeaTable: use bien comillas, paréntesis, comas y referencias de columnas.'

---

La [columna de fórmulas]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) le abre muchas posibilidades para trabajar con sus datos. Con la ayuda de las fórmulas puede, por ejemplo, relacionar entre sí valores de diferentes columnas y realizar cálculos con ellos. Sin embargo, dado que trabajar con fórmulas más complejas puede resultar difícil, sobre todo al principio, en este artículo le ofrecemos **soluciones a los problemas más conocidos**.

## Faltan comillas en los elementos de texto

Cada elemento de texto de sus fórmulas **debe** ir obligatoriamente entre comillas para que el editor de fórmulas lo reconozca. Si un texto **no** está entre comillas, puede aparecer el siguiente **mensaje de error**:

![Mensaje de error que aparece cuando faltan comillas alrededor de elementos de texto](images/Fehlermeldung-fehlende-Anfuehrungszeichen-bei-Textelementen.png)

#### Entrada incorrecta:

![Introducción incorrecta de elementos de texto](images/fehlerhafte-eingabe-anfuehrungszeichen.png)

#### Entrada correcta:

![Introducción correcta de elementos de texto](images/richtige-eingabe-anfuehrungszeichen.png)

{{< warning  headline="Consejo"  text="Los elementos de texto se marcan siempre en **rojo** en una fórmula y así pueden distinguirse de otros elementos. Si un elemento de texto **no** está marcado en **rojo** en el editor de fórmulas, significa que se ha introducido **incorrectamente**." />}}

## Faltan paréntesis en las funciones o están mal colocados

En el editor de fórmulas, **cada función** debe ir seguida primero de un **paréntesis de apertura** antes de que añada más elementos. Una vez que haya añadido a la fórmula todos los elementos de una función, esta debe terminar además con un **paréntesis de cierre**. Si **no** se ponen paréntesis, el editor de fórmulas **no** puede reconocer la función y pueden aparecer los siguientes mensajes de error:

![Mensaje de error que aparece si no se coloca ningún paréntesis de apertura después de una función](images/Fehlermeldung-bei-fehlender-Klammer-nach-einer-Funktion.png)

![Mensaje de error que aparece cuando los paréntesis de una función se colocan incorrectamente](images/fehlermeldung-klammern-bei-funktion-falsch-gesetzt.png)

#### Entrada incorrecta:

![Introducción incorrecta de una función](images/fehlerhafte-eingabe-funktion-1.png)

#### Entrada correcta:

![Introducción correcta de una función](images/korrekte-eingabe-funktion-1.png)

{{< warning  headline="Consejo"  text="Las funciones siempre se marcan en **azul** en una fórmula. Si hace clic en un paréntesis de apertura o de cierre en el editor de fórmulas, **se resalta el paréntesis correspondiente**. De este modo, podrá detectar más fácilmente los paréntesis que faltan o son incorrectos al introducir funciones." />}}

## Colocación incorrecta de paréntesis y llaves en general

La colocación correcta de paréntesis y llaves es uno de los mayores retos a la hora de introducir fórmulas. Ya sean **paréntesis o llaves**, deben colocarse siempre en el **lugar correcto** de una fórmula para que el editor de fórmulas la reconozca.

### Paréntesis

En la **sección anterior** de este artículo se explica cómo colocar correctamente los paréntesis al introducir funciones.

### Llaves

Utilice las llaves cuando desee hacer referencia a determinadas **columnas de la tabla**. El **nombre** de la columna deseada debe ir siempre rodeado de **dos llaves**. Si **no** se ponen llaves o se ponen **incorrectamente**, el editor de fórmulas **no** puede reconocer la referencia a la columna y pueden aparecer los siguientes mensajes de error:

![Mensaje de error que aparece si no se ponen llaves al hacer referencia a nombres de columnas](images/fehlermeldung-keine-geschweiften-klammern.png)

![Mensaje de error que aparece cuando las llaves se colocan incorrectamente al hacer referencia a nombres de columnas](images/fehlermeldung-geschweifte-klammern-falsch-gesetzt-1.png)

#### Entrada incorrecta:

![Introducción incorrecta de llaves al hacer referencia a nombres de columnas](images/fehlerhafte-eingabe-geschweifte-klammern-1.png)

#### Entrada correcta:

![Introducción correcta de llaves al hacer referencia a nombres de columnas](images/korrekte-eingabe.geschweifte-klammern.png)

### Referencias a columnas dentro de funciones

Si desea hacer referencia a nombres de columnas dentro de una función, debe prestar especial atención a la colocación correcta de paréntesis y llaves. Tenga en cuenta las reglas específicas para las funciones y las referencias a columnas. Si no está seguro de si una pareja de paréntesis o llaves está completa, recuerde que, al hacer clic en uno de estos signos en el editor de fórmulas, siempre se resalta el segundo.

#### Entrada incorrecta:

![Introducción incorrecta de una función con referencia a una columna](images/fehlerhafte-eingabe-einer-funktion-mit-spaltenverweis.png)

#### Entrada correcta:

![Introducción correcta de una función con referencia a una columna](images/korrekte-eingabe-einer-funktion-mit-spaltenverweis.png)

## Encadenar varias funciones

Si desea incluir **varias funciones** en su fórmula, debe asegurarse de separar siempre las distintas funciones con una **coma**.

Además, debe terminar las fórmulas que contienen varias funciones con **varios paréntesis de cierre**. Si su fórmula contiene, por ejemplo, tres funciones, también debe terminar con tres paréntesis de cierre en el editor de fórmulas.

Si **no** se tienen en cuenta estos puntos, el editor de fórmulas **no** puede reconocer la fórmula introducida y pueden aparecer los siguientes mensajes de error:

![Mensaje de error que aparece cuando una fórmula que contiene varias funciones no termina con el número necesario de paréntesis de cierre](images/fehlermeldung-zu-weinge-klammern-am-ende-der-formel.png)

![Mensaje de error que aparece si no se colocan comas entre las distintas funciones de una fórmula o si se colocan incorrectamente](images/fehlermeldung-falsche-kommasetzung.png)

#### Entrada incorrecta:

![Introducción incorrecta de una fórmula en la que se han encadenado varias funciones](images/fehlerhafte-eingabe-einer-formel-mit-mehreren-funktionen.png)

#### Entrada correcta:

![Introducción correcta de una fórmula en la que se han encadenado varias funciones](images/korrekte-eingabe-formel-mit-mehreren-funktionen.png)

{{< warning  headline="Consejo"  text="En fórmulas más complejas, trabaje siempre con **espacios y saltos de línea** para poder ver por separado las distintas funciones de su fórmula y detectar los errores con mayor facilidad." />}}

## Concatenar varios elementos de texto en una fórmula

Para concatenar varios elementos de texto en su fórmula, debe separar los distintos elementos de texto entre sí con un **símbolo &**. Si **no** se añaden **símbolos &** entre los elementos de texto, el editor de fórmulas **no** puede reconocer la fórmula introducida y aparece el siguiente mensaje de error:

![Mensaje de error que aparece cuando varios elementos de texto de una fórmula no están separados por &.](images/Fehlermeldung-bei-fehlendenen-zwischen-Textelementen.png)

#### Entrada incorrecta:

![Introducción incorrecta de varios elementos de texto en una fórmula](images/fehlerhafte-Eingabe-mehrere-Textelemente.png)

#### Entrada correcta:

![Introducción correcta de varios elementos de texto en una fórmula](images/korrekte-Eingabe-mehrere-Textelemente.png)

{{< warning headline="Consejo" text="Para que los distintos elementos de texto queden separados por un espacio, inserte **dos símbolos &** y **dos comillas (altas)** entre cada uno de los elementos de texto." />}}

![Edición de la fórmula para que los elementos de texto queden separados por un espacio](images/Leerzeichen-zwischen-Textelementen.png)
