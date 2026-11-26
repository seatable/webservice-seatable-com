---
title: 'Consejos para trabajar con fórmulas'
date: 2023-05-03
lastmod: '2023-09-21'
categories:
    - 'formeln'
author: 'nsc2'
url: '/es/ayuda/consejos-formulas-seatable'
aliases:
    - '/es/ayuda/tipps-zum-arbeiten-mit-formeln'
seo:
    title: 'Consejos para trabajar con fórmulas en SeaTable'
    description: 'Sugerencias para fórmulas en SeaTable: saltos de línea, sintaxis, colores, paréntesis, planificación y cómo evitar errores frecuentes.'

---

Aquí encontrará ayuda y consejos para facilitar su trabajo con las fórmulas de Seatable. [Aquí]({{< relref "help/base-editor/formeln/formelreferenz" >}}) encontrará una lista de todas las fórmulas disponibles.

## Utilizar espacios y saltos de línea

No tenga miedo de utilizar **espacios** y **saltos de línea** al crear fórmulas. Le ayudarán a mantener una visión de conjunto de las distintas funciones y otros elementos, sobre todo en las fórmulas más complejas.

En el **editor de fórmulas** puede establecer espacios y saltos de línea casi a su gusto. Solo hay que tener cuidado al utilizar **funciones**. **No** se puede poner ningún espacio directamente **después de** una función, por ejemplo _lower()_.

### Ejemplo de aplicación

![Los espacios y saltos de línea pueden establecerse casi arbitrariamente en el asistente de fórmulas. Las únicas excepciones son las funciones.](images/benutzen-Sie-leerzeichen-und-spaltenumbrueche.png)

## Utilizar la sintaxis en el editor de fórmulas

Cuando haga clic en un **elemento** del editor de fórmulas que desee añadir a su fórmula, aparecerá información útil. Justo debajo del nombre del elemento seleccionado, verá una breve descripción de su **funcionamiento**, así como una posible **sintaxis** y un **ejemplo** concreto de cómo podría quedar en una fórmula. Al escribir fórmulas más complejas, esta **información** puede ser útil para evitar errores o incertidumbres.

![Información sobre un elemento del asistente de fórmulas](images/Informationen-zu-einem-Element.png)

## Observe la coloración de los distintos elementos de la fórmula

Para poder distinguir entre sí los distintos elementos de su fórmula, se marcan en un **color** diferente en función de su tipo. Puede leer [aquí]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}#klare-farbsprache-zur-orientierung) qué elementos se muestran en cada color.

Utilice los distintos **colores** como guía para tener una mejor visión general de su fórmula. Además, el resaltado por colores de los elementos de la fórmula también puede funcionar como una especie de **autocontrol** en dos casos:

- Los **elementos de texto** no se marcan en **rojo** en su fórmula hasta que se encierran **entre comillas**.
- **Las referencias a columnas** no se marcan en **púrpura** en la fórmula hasta que se rodean de **llaves**.

Si los elementos de fórmula mencionados **no** están marcados en el **color** correspondiente en su fórmula, es que los ha introducido **incorrectamente**. Para corregirlo, utilice la sintaxis.

## Observe el resaltado de los paréntesis que van juntos

Los **paréntesis que van juntos** se **resaltan** en el editor de fórmulas en cuanto se hace clic en un paréntesis de apertura o de cierre. Esto facilita la detección de paréntesis que **faltan** o son **incorrectos**.

![Los paréntesis de apertura y cierre siempre aparecen resaltados en el editor de fórmulas](images/example-brackets.png)

## Planificar fórmulas

La lógica y la construcción de una fórmula pueden ser a veces un reto. Un ejercicio útil en este caso es escribir en un lenguaje sencillo qué objetivo concreto quiere alcanzar.

Una forma óptima de planificar una fórmula podría ser, por ejemplo, la siguiente:

1. En primer lugar, escriba con sus propias palabras el **objetivo** que desea alcanzar con la fórmula (por ejemplo, calcular los días que faltan para un acontecimiento).
2. Busque una **función** adecuada en el editor de fórmulas (por ejemplo, dateDif).
3. Utilice la **sintaxis** de la función para comprobar la ortografía correcta – por ejemplo, dateDif(fecha de inicio, fecha final, unidad).
4. Escriba la **fórmula** en el campo de texto del editor de fórmulas. Utilice **saltos de línea** y **espacios** para hacer más visible la lógica de su fórmula. Sobre todo al principio, puede ser útil escribir solo partes de una fórmula e ir añadiéndole más elementos poco a poco.
5. Preste atención a posibles **mensajes de error**. Si aparece alguno, intente primero corregirlo usted mismo comprobando la fórmula con ayuda de la sintaxis. Si necesita más ayuda, utilice nuestro artículo de ayuda [Errores típicos al trabajar con fórmulas]({{< relref "help/base-editor/formeln/typische-fehler-beim-arbeiten-mit-formeln" >}}).
