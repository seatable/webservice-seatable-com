---
title: 'Validación de entrada para campos de texto con expresiones regulares'
date: 2023-05-03
lastmod: '2024-03-11'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/es/ayuda/validar-campo-texto-regex-seatable'
aliases:
    - '/es/ayuda/validierung-der-eingabe-bei-textfeldern'
seo:
    title: 'Validar campos de texto SeaTable con expresiones regulares'
    description: 'Supervise y marque errores en los campos de texto de SeaTable usando regex. Garantice la calidad del dato comprobando formatos y señalando inconsistencias.'

---

Cuando utilice columnas de texto en sus tablas, tiene la opción de validar las entradas. Mediante la validación, que admite expresiones regulares, puede comprobar los valores de las celdas y resaltar las celdas cuyo contenido se desvíe del formato válido.

{{< warning  headline="Nota" >}}

Básicamente, hay dos formas diferentes de validar las entradas en las columnas de texto. La validación puede realizarse tanto al **añadir una nueva** [columna]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) de texto **ya creadas**.

{{< /warning >}}

## Validar entradas

![Activación de la validación de la entrada de columnas de texto](images/activate-validation-1.png)

1. Si desea validar las entradas de una columna de texto ya creada, haga clic primero en el **símbolo del triángulo** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} de la columna correspondiente.
2. Seleccione **Personalizar tipo de columna** en el menú desplegable.
3. Activar el control deslizante **Validar entrada**
4. Definir un **formato de destino**.
5. Confirme con **Enviar**.

![Definición del formato de destino](images/define-specific-format-2.png)

## Consecuencia de la validación

Tras una validación correcta, las **celdas** cuyo **contenido se desvía** del formato objetivo se resaltan en rojo.

![Celdas resaltadas en rojo con contenido diferente del formato de destino](images/marked-entries-which-not-match-the-format.png)

## Expresiones regulares

SeaTable soporta **expresiones regulares** para validar sus entradas en columnas de texto.  
Puede encontrar algunos ejemplos en la siguiente tabla:

| Expresión regular               | Función                                                                          |     |     |     |     |
| ------------------------------- | -------------------------------------------------------------------------------- | --- | --- | --- | --- |
| \[123456\]                      | Compruebe si una entrada corresponde a un curso escolar de 1 a 6.                |     |     |     |     |
| \[1-9\]\[0-9\]?\[0-9\]?\[a-z\]? | Comprobar el formato de un número de casa alemán (3 dígitos + 1 letra)           |     |     |     |     |
| \[0-9\]{5}                      | Comprobar el formato de los códigos postales alemanes (5x un número entre 0 y 9) |     |     |     |     |
| \[0-9/. \\-\]+                  | Comprobar el formato de un número de teléfono                                    |     |     |     |     |
| Max\*Mustermann                 | Buscar un posible segundo nombre de un autor                                     |     |     |     |     |

{{< warning  headline="Consejo"  text="Encontrará un **tutorial** detallado sobre el uso de expresiones regulares para comprobar cadenas [aquí (alemán](https://danielfett.de/2006/03/20/regulaere-ausdruecke-tutorial/) ) y [aquí (inglés)](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)." />}}
