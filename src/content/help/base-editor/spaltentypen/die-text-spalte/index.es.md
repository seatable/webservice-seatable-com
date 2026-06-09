---
title: 'La columna de texto'
date: 2023-05-03
lastmod: '2024-03-11'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/es/ayuda/columna-de-texto'
aliases:
    - '/es/ayuda/validierung-der-eingabe-bei-textfeldern'
    - '/es/ayuda/validar-campo-texto-regex-seatable'
seo:
    title: 'La columna de texto en SeaTable'
    description: 'Use la columna de texto en SeaTable para cadenas alfanuméricas cortas como nombres, contraseñas o IBAN, y valide entradas con expresiones regulares.'
weight: 1
---

La columna de texto es uno de los **tipos de columna** más básicos en SeaTable y también se muestra en primer lugar en el menú de selección del tipo de columna.

![La columna de texto normal](images/select-regular-text-column.png)

De forma predeterminada, SeaTable añade automáticamente una **columna de texto** como primera columna a cada tabla recién creada. Además, puede añadir manualmente tantas columnas de texto como desee a su tabla. Puede consultar cómo hacerlo [aquí]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![La columna de texto](images/text-column-new.png)

La **primera columna** de una tabla tiene varias [características]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}) especiales, como puede leer en el artículo enlazado.

## Uso de la columna de texto

La columna de texto es especialmente adecuada para registrar y [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) cadenas alfanuméricas cortas, por ejemplo, **términos**, **nombres**, **contraseñas**, **matrículas de vehículos** o **IBAN**.

![Ejemplo de aplicación de la columna de texto normal](images/regular-text-example.png)

{{< warning  headline="UTF-8"  text="SeaTable admite todos los caracteres del estándar UTF-8, ya que UTF-8 es la codificación de caracteres más extendida del mundo en Internet." />}}

Al utilizar la columna, es conveniente que las entradas **sean cortas**, ya que solo se puede mostrar un **número limitado de caracteres** sin tener que aumentar el ancho de la columna.

![Las entradas demasiado largas no pueden mostrarse en su totalidad en una columna de texto sin aumentar el ancho de la columna](images/use-short-entries.png)

## Otros tipos de columnas basadas en texto

Tenga en cuenta que **no hay opciones de formato** disponibles para las entradas de la columna de texto. Si desea registrar textos estructurados con saltos de línea, listas, imágenes, etc., debería utilizar la columna [Texto con formato]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}).

En SeaTable existen otros tres tipos de columnas basadas en texto para casos de uso especiales:
- la [columna de correo electrónico]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}})
- la [columna de URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})
- la [columna de número de teléfono]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

{{< warning  headline="Nota" >}}
Existen numerosas funciones de texto para las [columnas de fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}), que se comportan como columnas de texto cuando los resultados son **cadenas de caracteres**.
{{< /warning >}}

## Establecer el valor por defecto

Puede definir un [valor predeterminado]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) para cada columna de texto. Este valor se introduce automáticamente en cada nueva fila de la tabla.

Si especifica la referencia **{creator.name}** o **{creator.id}** como valor por defecto, se introduce automáticamente el **nombre** o el **ID del usuario** que ha añadido la fila.

![Referenciar el nombre de usuario con un valor por defecto](images/Set-creator-name-as-default-value.png)

## Validar entradas

Cuando utilice columnas de texto en sus tablas, tiene la opción de validar las entradas. Mediante la validación, que admite expresiones regulares, puede **comprobar los valores de las celdas** y resaltar las celdas cuyo contenido se desvíe del formato válido.

Puede configurar la comprobación de formato ya al crear una columna de texto, activando el control deslizante.

![Activación de la validación de la entrada de columnas de texto](images/activate-validation-1.png)

Si desea validar las entradas de una columna de texto ya creada, haga clic primero en el **símbolo del triángulo** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} de la columna correspondiente y seleccione **Personalizar tipo de columna** en el menú desplegable.

1. Active el control deslizante **Validar entrada**
2. Defina un **formato de destino**.
![Definición del formato de destino](images/define-specific-format-2.png)
3. Confirme con **Enviar**.

### Consecuencia de la validación

Tras una validación correcta, las **celdas** cuyo **contenido se desvía** del formato de destino se resaltan en rojo.

![Celdas resaltadas en rojo con contenido diferente del formato de destino](images/marked-entries-which-not-match-the-format.png)

### Expresiones regulares

Para validar sus entradas en columnas de texto, SeaTable admite **expresiones regulares**. En la siguiente tabla encontrará algunos ejemplos:

| Expresión regular               | Función                                                                          |
| ------------------------------- | -------------------------------------------------------------------------------- |
| \[123456\]                      | Comprobar si una entrada corresponde a una nota escolar de 1 a 6.                |
| \[1-9\]\[0-9\]?\[0-9\]?\[a-z\]? | Comprobar el formato de un número de casa alemán (3 dígitos + 1 letra)           |
| \[0-9\]{5}                      | Comprobar el formato de los códigos postales alemanes (5x un número entre 0 y 9) |
| \[0-9/. \\-\]+                  | Comprobar el formato de un número de teléfono                                    |
| Max.\*Mustermann                | Buscar un posible segundo nombre de un autor                                     |

{{< warning  headline="Consejo"  text="Encontrará un **tutorial** detallado sobre el uso de expresiones regulares para comprobar cadenas [aquí (alemán)](https://danielfett.de/2006/03/20/regulaere-ausdruecke-tutorial/) y [aquí (inglés)](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)." />}}
