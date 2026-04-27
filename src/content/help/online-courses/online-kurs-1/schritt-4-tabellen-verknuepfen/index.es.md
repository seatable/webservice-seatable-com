---
title: 'Paso 4: Vincular las tablas'
date: 2024-08-30
lastmod: '2024-09-19'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/es/ayuda/paso-4-enlazar-tablas'
aliases:
   - '/es/ayuda/schritt-4-tabellen-verknuepfen'
seo:
    title: 'Paso 4: Enlazar y gestionar tablas SeaTable para mayor eficiencia'
    description: 'Aprenda a enlazar y administrar tablas en SeaTable para análisis flexibles, gestión centralizada de datos y conexión automática de registros clave.'
---

Se pueden enlazar múltiples tablas en SeaTable utilizando columnas de enlace. A continuación añadiremos una segunda tabla con categorías de gastos y enlazaremos las dos tablas para demostrar esta potente función.

## Excurso: Ventajas de la opción de vincular registros de datos

Enlazar registros de datos es una de las funciones centrales de SeaTable, lo que la diferencia claramente de las hojas de cálculo convencionales y le confiere las prestaciones de una base de datos relacional. Suena complejo, pero no lo es, como pronto descubrirá por sí mismo. He aquí las tres ventajas más importantes de los datos enlazados:

- **Más visión de conjunto**: al vincular tablas, se crea una estructura clara y organizada. En lugar de almacenar toda la información en una única tabla y arriesgarse a redundancias, puede gestionar los datos relacionados -como gastos y categorías- en tablas separadas. Esto mantiene la coherencia de los datos y evita las entradas duplicadas.
- **Análisis de datos más flexible**: con las tablas vinculadas, puede combinar y analizar datos de distintas fuentes de forma específica. Por ejemplo, puedes analizar rápida y fácilmente todos los gastos de una categoría o departamento concretos.
- **Mantenimiento de datos más sencillo**: los cambios en una tabla central se aplican automáticamente a todas las tablas vinculadas. Esto garantiza que tus datos estén siempre actualizados y sean coherentes sin que tengas que actualizarlos varias veces.

## Ampliación de la estructura de base

Para poder crear enlaces, necesitamos una segunda tabla, que crearemos a continuación.

1. Crear una segunda tabla con el nombre `Categories` en la misma base.
2. La tabla `Categories` sólo requiere una columna: `Name`. Se crea por defecto, por lo que no es necesario hacer nada aquí.
3. Añadir manualmente cuatro entradas a la tabla `Categories` en:

    - `Travel`
    - `Clothing`
    - `Groceries`
    - `Leisure`

    ![Tabla «Categories» con cuatro categorías de ejemplo: Travel, Clothing, Groceries, Leisure](images/level1-categories.png)

4. Volver a la table `Expenses`.

5. Inserta otra columna. Dale a la nueva columna el nombre `Category-Link` y seleccione el tipo de columna `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Link to other records` off. La columna enlaza con la tabla `Categories`.  
   ![Diálogo para crear la columna de enlace «Category-Link» hacia la tabla «Categories»](images/level1-create-link-column.png)

## Vinculación de filas entre las dos tablas

Ahora tiene dos opciones para vincular los registros de datos de ambas tablas:

1. Puede asignar una entrada en el `Expenses` Seleccionar manualmente una línea de la tabla `Categories` pulsando dentro de la celda en el {{< key "+" >}} y, a continuación, seleccione la categoría adecuada. Esto se convierte rápidamente en una tarea tediosa y propensa a errores con grandes cantidades de datos.  
   ![Vinculación manual de un registro de gasto con una categoría mediante el icono de suma](images/level1-link-rows.png)
2. También puede utilizar la función [Opciones de tratamiento de datos]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) de SeaTable para automatizar la configuración de los enlaces.  
   ![Menú «Data Processing» con selección de una operación de procesamiento de datos en la tabla](images/level1-data-operation.png)

### Enlazar células por operación de tratamiento de datos

Para ello, cree una nueva operación de tratamiento de datos con el nombre `Assign Category` y seleccione el tipo de operación `Auto add link` de.

También debe realizar los siguientes ajustes para que SeaTable sepa cómo desea vincular sus datos:

- Tabla: `Expenses`
- Otra tabla: `Categories`
- Si columna: `{{< seatable-icon icon="dtable-icon-single-election" >}} Category`
- Columna: `{{< seatable-icon icon="dtable-icon-single-line-text" >}} Name`

![Operación de procesamiento «Assign Category» con tipo «Auto add link» y campos correspondientes](images/level1-auto-add-link.png)

Haga clic en Ejecutar para llevar a cabo la operación. Verá que todas las filas de la tabla `Expenses` con una línea de la tabla `Categories` estaban vinculados.

{{< warning  headline="Cuando faltan enlaces"  text="Si algunas filas no tienen enlace después de la operación de tratamiento de datos, es probable que haya cometido un error tipográfico en las cuatro entradas de la tabla `Categories`. Corrija el error tipográfico y simplemente vuelva a realizar la operación de tratamiento de datos." />}}

## Eliminar la columna innecesaria

Una vez enlazadas todas las entradas, puede editar el archivo `Category` en la tabla `Expenses` borrar. La información duplicada es superflua y debe evitarse.

## Revisión del formulario web

Si ahora vuelve a abrir el formulario web para introducir gastos, observará que ya no se solicita el tipo de gasto. ¿Por qué?  
Al suprimir la columna `Category` la opción de entrada en el formulario web se cancela automáticamente, ya que SeaTable ya no dispone de una columna correspondiente para guardar los datos.

¿Qué aprendemos de todo esto? Un gran poder conlleva una gran responsabilidad. En SeaTable, puede añadir o eliminar columnas en cuestión de segundos. La mayoría de los ajustes en una columna son inofensivos. Sin embargo, si elimina columnas o cambia su tipo, debe comprobar brevemente si esto afecta a otros componentes.

¿Por qué no pruebas la nueva columna añadida? `Category-Link` al formulario web para que puedas introducir tus gastos como de costumbre. Seguro que puedes arreglártelas.

## Artículo de ayuda con más información

- [Añadir una tabla a una base]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}})
- [Cómo enlazar tablas en SeaTable]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})
- [Tratamiento de datos Comparación y enlace]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}})
