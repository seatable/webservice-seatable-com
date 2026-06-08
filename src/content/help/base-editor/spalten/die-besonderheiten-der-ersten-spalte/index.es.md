---
title: 'Las características especiales de la primera columna'
date: 2022-10-13
lastmod: '2024-03-15'
categories:
    - 'arbeiten-mit-spalten'
author: 'nsc2'
url: '/es/ayuda/particularidades-primera-columna'
aliases:
  - '/es/ayuda/die-besonderheiten-der-ersten-spalte'
seo:
    title: 'Particularidades de la primera columna en SeaTable detalladas'
    description: 'Descubre qué la hace especial, los tipos permitidos y limitaciones en SeaTable. Aprende a ajustar su configuración fácilmente.'
---

La **primera** columna de una tabla en SeaTable tiene varias características especiales y restricciones en comparación con las otras columnas. Aquí puede averiguar cómo personalizar la primera columna en SeaTable.

## Particularidades de la primera columna de SeaTable

- A diferencia de las demás columnas, **no puede ocultar** la primera columna de una tabla.
- A diferencia de las demás columnas, **no puede desplazar** la primera columna de una tabla.
- A diferencia de las demás columnas, **no puede eliminar** la primera columna de una tabla.
- Sin embargo, a diferencia de las demás columnas, la primera puede **fijarse** individualmente.
- Para la **primera** columna, sólo hay **seis tipos de columna** entre los que elegir:
  - [Texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})
  - [Número]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
  - [Fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
  - [Selección única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
  - [Número automático]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
  - [Fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

## Cómo personalizar el tipo de la primera columna

![Ajuste de la primera columna](images/change-the-first-column.gif)

1. Haga clic en el **símbolo** triangular **desplegable** situado a la derecha del nombre de la primera columna.
2. Vaya a **Personalizar tipo de columna**.
3. Haga clic en el **campo** del tipo de columna actual.
4. Seleccione un **nuevo tipo de** columna para la primera columna.
5. Si es necesario, **ajuste el formato**.
6. Haga clic en **Enviar**.
7. Confirme el ajuste haciendo clic en **Convertir**.

## Fórmulas en la primera columna

Si define una **fórmula** como **primera** columna de una tabla, puede utilizar la fórmula simple **{nombre de columna}**, por ejemplo, para **citar** las entradas de casi todas las demás columnas de su tabla. Esto funciona incluso si el otro tipo de columna **no** se admite en la primera columna.

![Posibilidades con el tipo de columna Fórmula en la primera columna de una tabla](images/formular-in-the-first-column-1.png)

## Preguntas frecuentes

{{< faq "¿Cuáles son las limitaciones de la primera columna?" >}}La primera columna no puede **ocultarse**, **moverse** ni **borrarse**.
{{< /faq >}}
{{< faq "¿Es posible cambiar después el tipo de la primera columna?" >}}Sí, es posible. En algunos casos, sin embargo, puede ocurrir que se **pierda** información al [cambiar el tipo de columna]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}}), por ejemplo de texto a número. Por lo tanto, después de una conversión, compruebe si toda la información se ha transferido correcta y completamente.
{{< /faq >}}
{{< faq "¿Qué es un número automático?" >}}Si desea que sus filas tengan un **número de identificación único**, el tipo de columna [Número]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}}) automático puede serle útil. Algunos ejemplos son los números de factura, los casos de prueba o los ID de empleado. El número también puede completarse con cualquier prefijo.

{{< /faq >}}
