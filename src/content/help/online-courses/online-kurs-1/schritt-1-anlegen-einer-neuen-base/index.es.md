---
title: 'Paso 1: Creación de una nueva base'
date: 2024-08-30
lastmod: '2024-09-04'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/es/ayuda/paso1-crear-base-gastos-seatable'
aliases:
    - '/es/ayuda/schritt-1-anlegen-einer-neuen-base'
seo:
    title: 'Paso 1 Curso SeaTable 1: nueva base para tus gastos'
    description: 'Primer paso del curso: crea una base SeaTable desde cero, añade y ajusta columnas y categorías para organizar tus gastos de forma estructurada.'
---

En este curso, crearemos una sencilla herramienta para registrar y gestionar tus gastos personales o profesionales. Cuando esté preparado, podrá registrar los gastos en cualquier momento, ya sea en su ordenador o en su teléfono móvil. Cada vez que saques la cartera, deberás documentar ese gasto. La recompensa a este esfuerzo es que puedes ver de un vistazo en qué te has gastado cuánto dinero.

Así que vamos a empezar este curso online creando la estructura necesaria para poder guardar estos resultados. Para ello, crearemos una base inicial y luego algunas columnas. Verás que los siguientes pasos son casi autoexplicativos.

{{< warning  headline="Un pequeño consejo para trabajar eficazmente con este curso en línea"  text="Me gustaría recomendarle que tenga dos ventanas de navegador abiertas en su monitor y las coloque una al lado de la otra. Abra este artículo en una ventana del navegador y abra su SeaTable en la otra. Así le resultará mucho más fácil seguir los pasos de este curso sin tener que cambiar constantemente de ventana." />}}

![](images/level1-browser-window-setup.png)

## Crear nueva base

Comenzamos en la página de inicio de SeaTable. Creamos una nueva base con el nombre `Expense Tracking` botón . A continuación, haga clic en esta base para ir al Editor de bases.

## Cambiar el nombre de la primera tabla

Por defecto, cada base contiene una tabla con el nombre `Table 1`que tiene una columna con tres filas.

- Suprima las tres líneas
- A continuación, cambie el nombre de la tabla por `Expenses`

{{< warning  headline="Ayuda en caso de atasco"  text="El uso de SeaTable debería ser intuitivo en la mayoría de los casos. Por ejemplo, puede eliminar filas de la misma forma a la que está acostumbrado en muchas otras soluciones de software: Seleccione las filas y haga clic con el botón derecho. Si todavía necesita ayuda, recuerde los artículos de ayuda que hemos recopilado para usted en la parte inferior de la página. Allí encontrará las instrucciones adecuadas para cada paso de este curso en línea." />}}

## Personalizar las columnas de la tabla y añadir otras nuevas

A continuación, pasamos a las columnas de la tabla para que nuestra base pueda registrar los datos deseados.

- Cambia el nombre de la primera columna de `Name` en `Reason`
- Ahora añada tres columnas más

**Columna 1:**

> Nombre: `Date`
>
> Tipo de columna: `{{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} Date`
>
> Formato: cualquiera
>
> Al minuto: `Yes`

**Nota:** En lugar del tipo de columna `{{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} Date` el tipo de columna `{{< seatable-icon icon="dtable-icon-creation-time" >}} Created time` puede utilizarse. Mientras que tiene que rellenar manualmente la columna de la fecha, ésta se rellenaría automáticamente con la fecha actual. Esto, por supuesto, ahorra tiempo. Sin embargo, la desventaja sería que ya no podría cambiar el valor de la fecha y, por ejemplo, ya no podría introducir retroactivamente gastos de otros días.

---

**Columna 2:**

> Nombre: `Amount`
>
> Tipo de columna: `{{< seatable-icon icon="dtable-icon-number" >}} Number`
>
> Formato: `Euro`

---

**Columna 3:**

> Nombre: `Category`
>
> Tipo de columna: `{{< seatable-icon icon="dtable-icon-single-election" >}} Single select`

---

{{< warning  headline="26 tipos de columnas"  text="Hasta ahora, sólo ha visto una fracción de los tipos de columnas posibles. Uno de los mayores puntos fuertes de SeaTable es que realmente puede almacenar cualquier tipo de información gracias a los 26 tipos de columnas disponibles actualmente." />}}

## Añadir opciones de selección única

Su selección única no tiene actualmente ninguna opción de selección. Por lo tanto, a continuación cree una nueva selección para la columna `Category` las cuatro opciones siguientes:

- Ropa
- Comestibles
- Ocio
- Viajar

## Breve control de calidad

Fantástico. Si has seguido las instrucciones al pie de la letra, tu base debería tener este aspecto:

![](images/level1-expenses-table.png)

Recapitulemos brevemente lo que acaba de crear con unos pocos clics de ratón: **Ahora tiene una base en la que puede registrar todos sus gastos futuros.**

Al mismo tiempo, al seleccionar los tipos de columna, se ha asegurado de que en las columnas sólo pueda introducirse la información adecuada.

Ese fue el paso 1 de este curso en línea. Desplázate hasta el final de este artículo y salta al **paso 2: Crear un formulario**.

## Artículo de ayuda con más información

- [Crear una nueva base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Cómo personalizar el tipo de columna]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}})
- [Borrar una línea]({{< relref "help/base-editor/zeilen/das-loeschen-von-zeilen" >}})
- [Añadir una columna]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}})
- [Añadir opciones a una columna de selección única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
- [Particularidades de la primera columna]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}})
- [Personalizar el aspecto de una base (icono y color)]({{< relref "help/startseite/bases/aussehen-einer-base-anpassen-icon-und-farbe" >}})
