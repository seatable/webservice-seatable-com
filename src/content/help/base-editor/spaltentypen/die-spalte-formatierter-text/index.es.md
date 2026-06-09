---
title: 'La columna de texto largo'
date: 2023-02-21
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'kgr'
url: '/es/ayuda/columna-de-texto-largo'
aliases:
    - '/es/ayuda/die-spalten-text-und-formatierter-text'
    - '/es/ayuda/campos-texto-vs-texto-formato-seatable'
seo:
    title: 'La columna de texto largo en SeaTable'
    description: 'Use la columna de texto largo en SeaTable para registrar textos estructurados de cualquier longitud con saltos de línea, listas, imágenes y más.'
weight: 2
---

Para el **registro de textos estructurados de cualquier longitud**, SeaTable pone a su disposición el tipo de columna *Texto largo*. En este artículo descubrirá cuáles son las diferencias respecto a la columna de texto y en qué casos tiene sentido recurrir a la columna de texto largo.

## Uso de la columna de texto largo

A diferencia de la columna de texto, el tipo de columna **Texto largo** no registra cadenas de caracteres sin estructura, sino textos con formato que incluyen saltos de línea, listas, imágenes, etc.

![La columna de texto largo](images/formatted-text-column.png)

Las columnas de texto largo son especialmente adecuadas para registrar **textos largos**, como descripciones de productos, listas de control o publicaciones en redes sociales.

{{< warning  headline="UTF-8"  text="SeaTable admite todos los caracteres del estándar UTF-8, ya que UTF-8 es la codificación de caracteres más extendida del mundo en Internet." />}}

Las entradas **no** se escriben directamente en la celda, sino en un **editor** al que se accede con un clic y que ofrece diversas **opciones de formato**. A diferencia de la columna de texto, así también puede estructurar textos más largos.

![Ejemplo de aplicación de una columna de texto largo](images/long-text-example.png)

Entre otras cosas, puede elegir un **formato de párrafo**, poner la **fuente** en cursiva o negrita e insertar **enlaces**, **citas**, **listas**, **tablas** e **imágenes**.

{{< warning  type="warning" headline="Límite de caracteres"  text="Se aplica un límite de 100.000 caracteres a las celdas individuales del tipo Texto largo. Esto corresponde aproximadamente a 25 páginas A4 de texto. Por tanto, el límite de caracteres solo debería afectar a su trabajo en casos excepcionales." />}}

## Otros tipos de columnas basadas en texto

Si desea registrar **cadenas de caracteres cortas sin formato** (p. ej., nombres, contraseñas, matrículas de vehículos), debería utilizar la [columna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

Además de la columna de texto largo, en SeaTable existen otros tres tipos de columnas basadas en texto para casos de uso especiales:
- la [columna de correo electrónico]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}})
- la [columna de URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})
- la [columna de número de teléfono]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

## Establecer el valor por defecto

Puede definir un [valor predeterminado]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) para cada columna de texto largo. Este texto se introduce automáticamente en la celda de cada nueva fila creada.

1. Haga clic en la **flecha desplegable** situada a la derecha del nombre de la columna.
2. Vaya a **Establecer valor por defecto**.
3. Al hacer clic en **Editar texto**, se abre el editor, donde puede redactar el texto que servirá de valor por defecto.

## Restricciones en filtros, ordenación y agrupación

No es posible ordenar ni agrupar las entradas de una tabla según las columnas de texto largo. En cuanto a los filtros, solo dispone de las opciones "está vacío" y "no está vacío".
