---
title: 'Las columnas Texto y Texto con formato'
date: 2023-02-21
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/es/ayuda/campos-texto-vs-texto-formato-seatable'
aliases:
    - '/es/ayuda/die-spalten-text-und-formatierter-text'
seo:
    title: 'Campos texto vs texto con formato en SeaTable'
    description: 'Elija columnas de texto normal para entradas cortas y formato avanzado para textos largos y estructurados en sus tablas.'

---

SeaTable proporciona dos tipos de columnas diferentes para introducir **cadenas** y **textos de** cualquier tipo: **Texto** y **Texto con formato**. Pero, ¿cuál es exactamente la diferencia entre los dos tipos de columna? ¿Y en qué casos tiene sentido utilizar la columna de texto formateado?

## La columna de texto

La columna de texto es uno de los **tipos de columna** más básicos en SeaTable y también se muestra en primer lugar en el menú de selección del tipo de columna.

![La columna de texto normal](images/select-regular-text-column.png)

Además, SeaTable añade automáticamente una **columna de texto** como primera columna a cada tabla recién creada.

![La columna de texto "normal ](images/text-column-new.png)

La **primera columna de** una tabla tiene varias [características]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}) especiales, como puedes leer en el artículo enlazado.

### Uso de la columna de texto

La columna de texto es especialmente adecuada para recoger entradas cortas, como **términos**, **nombres**, **palabras** u otras **cadenas de caracteres** que no tienen un valor numérico calculable, por ejemplo, direcciones y números de teléfono.

![Ejemplo de aplicación de la columna de texto normal](images/regular-text-example.png)

Al utilizar la columna, es conveniente que las entradas **sean cortas**, ya que sólo se puede mostrar un **número limitado de caracteres** sin tener que aumentar el ancho de la columna.

![Las entradas demasiado largas no pueden mostrarse en su totalidad en una columna de texto sin aumentar el ancho de la columna.](images/use-short-entries.png)

{{< warning  headline="Nota importante"  text="Tenga en cuenta que **no hay opciones de formato** disponibles para las entradas de la columna de texto normal." />}}

Existen otros dos tipos de columnas basadas en texto en SeaTable para casos de uso especiales: la [columna de correo electrónico]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}) y la [columna de URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}}).

### Establecer el valor por defecto

Puede definir un [valor predeterminado]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) para cada columna de texto. Este valor se introduce automáticamente en cada nueva fila de la tabla.

Si especifica la referencia **{creator.name}** o **{creator.id}** como valor por defecto, se introduce automáticamente el **nombre** o el **ID del usuario** que ha añadido la fila.

![Referenciar el nombre de usuario con un valor por defecto](images/Set-creator-name-as-default-value.png)

## La columna Texto con formato

El tipo de columna **Texto con formato** es uno de los tipos de columna más específicos y se muestra en segundo lugar cuando se selecciona el tipo de columna.

![La columna Texto con formato](images/formatted-text-column.png)

### Uso de la columna Texto con formato

Las columnas de texto con formato son especialmente adecuadas para **textos largos**, como descripciones de productos, listas de control o publicaciones en redes sociales.

Las entradas **no** se escriben directamente en la celda, sino en un **editor** al que se accede con un clic y que ofrece diversas **opciones de formato**. A diferencia de la columna de texto, también puedes estructurar textos más largos.

![Ejemplo de aplicación de una columna de texto formateada](images/long-text-example.png)

Entre otras cosas, puedes elegir un **formato de párrafo**, poner la **fuente** en cursiva o negrita e insertar **enlaces**, **citas**, **listas**, **tablas** e **imágenes**.

{{< warning  headline="Límite de caracteres"  text="Se aplica un límite de 100.000 caracteres a las celdas individuales del tipo Texto con formato. Esto corresponde aproximadamente a 25 páginas A4 de texto. Por tanto, el límite de caracteres solo debería afectar a su trabajo en casos excepcionales." />}}
