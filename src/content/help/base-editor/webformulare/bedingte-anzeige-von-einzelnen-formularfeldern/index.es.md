---
title: 'Visualización condicional de campos de formulario individuales'
date: 2023-01-08
lastmod: '2024-02-14'
categories:
    - 'webformulare'
author: 'vge'
url: '/es/ayuda/visualizacion-condicional-campos-formulario'
aliases:
    - '/es/ayuda/bedingte-anzeige-von-einzelnen-formularfeldern'
seo:
    title: 'Visualización condicional de campos en formularios SeaTable: cómo configurarlo'
    description: 'Descubra cómo mostrar campos en formularios web de SeaTable solo cuando se cumple una condición, para encuestas dinámicas y datos de mayor calidad.'
weight: 4
---

Al crear **formularios web**, puede establecer que determinados **campos** sólo sean visibles cuando se cumpla una **condición** en un campo anterior. Esto le permite mejorar la **orientación del usuario** al rellenar el formulario.

## Establecer una condición para un campo de formulario

1. Abra un **formulario web** existente.
2. Haga clic en un campo para abrir la **configuración del campo**.
3. Vaya a **Mostrar campo sólo cuando se cumplan las condiciones** y haga clic en el botón con el símbolo más, con el que puede **añadir una condición**.
4. Seleccione el **campo anterior** al que debe referirse la condición.
5. A continuación, establezca la **condición**. Dependiendo del tipo de columna subyacente, tiene diferentes opciones para elegir.

{{< warning  headline="Nota"  text="Sólo tiene la opción de una visualización condicional si hay al menos un campo anterior." />}}

## Ejemplo de aplicación

![Visualización condicional de campos en formularios web](images/Bedingte-Anzeige-von-Feldern-in-Webformularen.gif)

Supongamos que quiere realizar una encuesta de satisfacción entre los empleados de su empresa. Por ejemplo, quiere hacer la pregunta "¿Cuál es su grado de satisfacción con nuestro leasing de vehículos de empresa?", pero sabe que sólo se ofrece un vehículo de empresa a los empleados que ocupan puestos directivos. Por lo tanto, sólo quiere hacer esta pregunta a sus directivos.

En primer lugar, debe crear una [columna de calificación]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}}) en su tabla y añadirla como **campo** a su formulario web. A continuación, añada la **condición** de que el campo de calificación sólo se muestre si se ha seleccionado la opción "Head of" o "Team lead" en el **campo de selección "Cargo"** anterior. El campo de selección debe requerir una **entrada obligatoria**, ya que, de lo contrario, los directivos que dejen este campo en blanco tampoco verán la pregunta sobre el leasing de vehículos de empresa.

Para que los participantes no puedan hacer visibles los campos ocultos simplemente probando las condiciones, puede insertar **saltos de página**. Así, después de rellenar el campo obligatorio, los participantes tienen que hacer clic primero en **Página siguiente** y allí se les muestran o no los campos condicionales.
