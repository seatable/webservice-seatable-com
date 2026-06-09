---
title: 'El tipo de columna Autonumeración'
date: 2023-01-07
lastmod: '2023-02-10'
categories:
    - 'text-und-zahlen'
author: 'ssc'
url: '/es/ayuda/columna-numeracion-automatica'
aliases:
    - '/es/ayuda/der-spaltentyp-automatische-nummer'
seo:
    title: 'Columna de numeración automática SeaTable – completa'
    description: 'Descubre cómo asignar números automáticos únicos en SeaTable, manejar formatos, reinicio y consejos para evitar duplicados o saltos.'
weight: 24
---

El tipo de columna **Autonumeración** genera un número creciente automáticamente para cada nueva fila. Este tipo de columna se utiliza cuando se necesita un identificador único para cada registro.

Tenga en cuenta que esta columna **no** sirve para contar el número de registros de una tabla. Si [elimina una fila]({{< relref "help/base-editor/zeilen/das-loeschen-von-zeilen" >}}), los registros restantes **no** se vuelven a numerar. Esto puede dar lugar a **lagunas** en la numeración.

Para **volver a numerar** los registros (por ejemplo, para eliminar huecos), puede eliminar la columna _Autonumeración_ y volver a crearla, o cambiar el tipo de columna y convertirla de nuevo en _Autonumeración_.

![Líneas con número automático](images/auto-number.gif)

## Hay tres formatos disponibles

Al crear la columna _Autonumeración_, se determina el **formato** que deben tener los valores de esta columna. Puede elegir un **número** con un determinado número de dígitos y anteponer a este número una **cadena de letras** o dígitos (por ejemplo, la **fecha** actual).

![Opciones formales de SeaTable para la columna numérica automática](images/Formatmoeglichkeiten-spalten.png)

## Preguntas frecuentes

Aunque el tipo de columna _Autonumeración_ parece relativamente sencillo, hay algunas características especiales que deben tenerse en cuenta.

{{< faq "¿Es posible influir en el siguiente valor utilizado?" >}}Sí. En las opciones de la columna, ésta ofrece la posibilidad de **restablecer** el **número automático** a un valor determinado, que luego recibe la fila siguiente.
{{< /faq >}}
{{< faq "¿Los valores de la columna pueden aparecer dos veces?" >}}Sí, esto puede ocurrir. Si restablece el número automático, los valores también pueden producirse dos veces. Por lo tanto, los valores de esta columna no son únicos.
{{< /faq >}}
{{< faq "¿Puede la columna contener también sólo valores únicos?" >}}Sí. Si utiliza una suscripción Plus o Enterprise de SeaTable, puede **bloquear la columna para editarla**. De este modo, nadie puede restablecer el número y cada valor sigue siendo único.

{{< /faq >}}
