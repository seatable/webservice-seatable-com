---
title: 'La columna de selección única'
date: 2022-10-10
lastmod: '2025-07-15'
categories:
    - 'spalten'
author: 'kgr'
url: '/es/ayuda/columna-seleccion-unica-seatable'
aliases:
    - '/es/ayuda/anlegen-einer-einfachauswahl-spalte'
    - '/es/ayuda/hinzufuegen-von-optionen-zu-einer-einfachauswahl-spalte'
    - '/es/ayuda/einfachauswahl-optionen-exportieren-und-importieren'
    - '/es/ayuda/aendern-der-reihenfolge-von-einfachauswahl-optionen'
    - '/es/ayuda/kaskadierung-einer-einfachauswahl'
    - '/es/ayuda/die-einfachauswahl-spalte'
seo:
    title: 'Columna de selección única SeaTable: opciones, colores, cascada y valores predeterminados'
    description: 'Columna de selección única en SeaTable: cree opciones, personalice colores, use cascada y defina dependencias lógicas.'
weight: 7
---

Una columna de selección única es ideal si desea asignar **exactamente una opción** de una lista de opciones a definir a sus filas. Las opciones reciben **etiquetas** de colores con las que podrá clasificar sus registros de datos en **categorías** y organizar las tablas con claridad.

![Campo de selección única en SeaTable](images/single-select-column.png)

## Creación de una columna de selección única

Crear una columna de selección única es un juego de niños y puede hacerse con sólo unos clics. Encontrará información detallada en [Añadir una columna]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![Crear una columna de selección única](images/define-single-select-column.png)

1. Haga clic en el **símbolo más** situado a la derecha de la última columna de una tabla.
2. Dé un **nombre** a la nueva columna.
3. Seleccione **Selección única** como tipo de columna.
4. Confirme con **Submitir**.

## Añadir opciones de selección

Puede crear varias opciones en una columna de selección única, entre las que podrá elegir al rellenar las celdas. Puede añadir **nuevas opciones** a la columna de varias maneras:

- Añadir opciones a través de la configuración de la columna
- Añadir opciones a través de las celdas de la columna de selección única
- Importar opciones

{{< warning headline="Mismo principio para las columnas de selección múltiple" >}}
Todas las funciones presentadas en esta sección se aplican del mismo modo a la [columna de selección múltiple]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}).
{{< /warning >}}

### Añadir opciones a través de la configuración de la columna

![Añadir opciones a una columna de selección única](images/add-options-to-a-single-select-column.gif)

1. Haga clic en la **flecha desplegable** situada a la derecha del nombre de una columna de selección única.
2. Vaya a **Editar selección única**.
3. Cree tantas opciones como desee haciendo clic en **Añadir opción**.
4. Confirme cada entrada con el **botón Intro**.
5. Si lo desea, puede ajustar los **colores** asignados a las opciones.

### Añadir opciones a través de las celdas de la columna de selección única

![Añadir opciones a través de las filas de la columna de selección única](images/Hinzufuegen-von-Optionen-ueber-die-Zeilen.png)

1. Haga doble clic en una **celda** de la columna de selección única.
2. Introduzca en el **campo de búsqueda** un término adecuado que desee definir como **nueva opción**.
3. Haga clic en **Añadir opción**.
4. El término introducido se asigna entonces a la celda seleccionada y se añade a las distintas **opciones de selección** de la columna.

{{< warning headline="¿Selección única o enlace a otras entradas?" >}}
Si desea poder almacenar **datos adicionales** para cada opción de selección, debería considerar el uso de una [columna de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) en lugar de una columna de selección única. Para ello, cree la selección única como primera columna en una tabla adicional. Esto le permitirá introducir registros de datos completos para todas las opciones, que podrá asignar a cualquier número de filas en las tablas vinculadas.
{{< /warning >}}

## Exportación e importación de opciones

No sólo puede **añadir manualmente** las opciones, sino también **exportarlas** cómodamente desde una columna existente e **importarlas** a otra columna. Esto le ahorrará mucho trabajo si desea utilizar las mismas opciones –incluso en bases diferentes– para varias **columnas de selección única** y **columnas de selección múltiple**.

### Exportar opciones de una columna de selección

![Exportar opciones de una columna de selección única](images/export-options-of-a-single-select-column-new-1.png)

1. Haga clic en la **flecha desplegable** situada a la derecha del nombre de una columna de selección única o múltiple.
2. Seleccione **Editar selección única** o **Editar selección múltiple**.
3. Haga clic en **Exportar opciones**.

Las opciones se **exportan** ahora como un archivo JSON. Dependiendo de la configuración de su navegador, la descarga se habrá guardado directamente en su dispositivo o aún deberá especificar una ubicación de almacenamiento. En el siguiente paso, puede **importar** las opciones a otra columna de selección única o múltiple.

### Importar opciones a una columna de selección

![Importar opciones exportadas a una nueva columna de selección única](images/import-options-of-a-single-select-column-new-3.png)

1. Haga clic en la **flecha desplegable** situada a la derecha del nombre de una columna de selección única o múltiple.
2. Seleccione **Editar selección única** o **Editar selección múltiple**.
3. Haga clic en **Importar opciones**.
4. Seleccione el **archivo JSON** de su dispositivo y confirme la carga.

Las opciones se **importarán** a la columna seleccionada y estarán listas para ser rellenadas en las celdas correspondientes. Por supuesto, puede seguir añadiendo, eliminando y editando opciones como desee.

## Colores de las opciones de selección

Para diseñar visualmente la vista dentro de una tabla, SeaTable asigna un **color** a cada opción de una columna de selección única o múltiple. Posteriormente puede **ajustar** este color asignado aleatoriamente mediante la ruta mencionada a las opciones.

Abrirá el **selector de color** haciendo clic en el **símbolo de triángulo coloreado situado delante del nombre de la opción**.

![Colores de la columna de selección única](images/farben-einfachauswahl.png)

Actualmente hay **24 colores** disponibles para resaltar visualmente las opciones respectivas. Con una [suscripción Enterprise]({{< relref "help/teamverwaltung/abonnement/abo-pakete" >}}) también tiene la opción de crear [colores personalizados]({{< relref "help/base-editor/weitere-optionen/eigene-farben-in-einer-base-hinzufuegen" >}}) para sus opciones de selección.

## Cambiar el orden de las opciones

El orden de las opciones es crucial si desea [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) o [agrupar]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) por una sola columna de selección. SeaTable **no organiza las opciones alfabéticamente**, sino de forma flexible según el **orden de las opciones**, que puede definir como desee.

![Cambiar el orden de una columna de selección única](images/Sortierung-einer-Einfachauswahl-Spalte-aendern.gif)

1. Haga clic en la **flecha desplegable** situada a la derecha del nombre de la columna de selección única.
2. Vaya a **Editar selección única**.
3. **Arrastre y suelte** una opción hasta la posición deseada. Para ello, utilice los **seis puntos** situados a la izquierda delante de cada opción.

## Fijar valor por defecto

Para cada columna de selección única, tiene la opción de establecer un [valor por defecto]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}). El valor predeterminado se asigna **automáticamente** a cada nueva fila como opción.

1. Haga clic en la **flecha desplegable** situada a la derecha del nombre de la columna de selección única.
2. Vaya a **Fijar valor por defecto**.
3. En la lista, seleccione la **opción** que se va a utilizar como valor por defecto.

![Valor por defecto de una columna de selección única](images/default-value-single-select.png)

Si desea borrar de nuevo el valor por defecto, haga clic en el **icono de la papelera** {{< seatable-icon icon="dtable-icon-delete" >}}.

## Selección única en cascada

Mediante la función de cascada, puede definir una columna padre del mismo tipo para cada columna de selección única, que restringe las opciones disponibles de la columna de selección única subordinada. Esto ofrece las siguientes ventajas:

- La función en cascada le permite **reducir el número de opciones** disponibles en otra columna de selección única.
- Al definir dependencias, puede **crear relaciones lógicas** entre dos columnas de selección única.
- Especialmente con un gran número de opciones, esto puede ser muy útil para **minimizar los errores** que pueden producirse al introducir datos.
- Además, las columnas de selección única en cascada también pueden ayudar a **acelerar los procesos de trabajo**.

![Definición de cascada](images/Definierung-einer-Kaskadierung-1.png)

1. Haga clic en la **flecha desplegable** de una columna de selección única.
2. Haga clic en **Definir cascada**.
3. Seleccione una **columna de selección única** que vaya a actuar como columna padre.
4. Asigne cualquier número de **opciones subordinadas de la columna actual** a las **opciones padre** de esta columna.

![Asignar las opciones de la columna de selección única padre](images/Zuweisung-der-Optionen-bei-einer-Kaskadierung-1.png)

{{< warning headline="Nota importante" text="Sólo las columnas que se encuentran en **la misma tabla** que la columna para la que se va a definir la selección en cascada pueden actuar como columnas padre de selección única." />}}

### Ejemplo de cascada con sentido

![Definición de cascada mediante un ejemplo](images/Beispiel-fuer-eine-Kaskadierung-Bild-1.png)

En este ejemplo, la tabla contiene datos sobre diversas unidades de educación/formación continua para los empleados. Además de la primera columna, que registra diversas **formaciones**, ya existe una columna de selección única que especifica la **localización** respectiva de la formación. En este ejemplo se define una **cascada** para otra columna de selección única, que registra el **edificio** exacto.

![Asignación de las opciones de la columna seleccionada a las opciones de la columna de selección única supraordenada](images/Beispiel-fuer-eine-Kaskadierung-Bild-2.png)

En este ejemplo, la columna **"Location"**, que especifica la ciudad en la que tiene lugar el entrenamiento correspondiente, sirve como **columna de selección única superior**. El siguiente paso consiste en asignar **opciones subordinadas** de la recién creada columna de selección única **"Building"** a las tres ciudades de esta columna. En concreto, a las tres opciones **Londres**, **París** y **Berlín** se les asignan los edificios que se encuentran en la ciudad respectiva.

![Opciones disponibles en la columna de selección única tras definir una cascada](images/Beispiel-fuer-eine-Kaskadierung-Bild-3.png)

Las opciones o edificios que pueden seleccionarse en una celda de la columna subordinada "Building" dependen ahora de la ciudad seleccionada en la misma fila de la columna de selección única "Location". Esto le permite seleccionar **sólo** los edificios que se encuentran realmente en la ciudad correspondiente.