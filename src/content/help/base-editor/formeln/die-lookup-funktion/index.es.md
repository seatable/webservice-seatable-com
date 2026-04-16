---
title: 'La fórmula de búsqueda'
date: 2022-10-13
lastmod: '2023-04-06'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/es/ayuda/columna-lookup-seatable'
aliases:
    - '/es/ayuda/die-lookup-funktion'
seo:
    title: 'Columna lookup: consulta datos desde tablas vinculadas'
    description: 'Consulte y muestre fácilmente información de tablas vinculadas con la columna lookup en SeaTable. Ideal para evitar duplicidades.'

---

La función de búsqueda permite mostrar valores adicionales de una tabla ya vinculada en la tabla actual. Esto le evita tener que introducir los datos dos veces y, al mismo tiempo, puede relacionarlos entre sí. En Excel esta función se conoce como _VLOOKUP_ o _SVERWEIS_.

## ¿Cuándo necesitas la fórmula de búsqueda?

La función de búsqueda debe utilizarse siempre que se quiera cruzar información almacenada en diferentes tablas. Digamos que está utilizando SeaTable para la [gestión de proyectos]({{< relref "pages/landing-pages/industry-solutions/project-management" >}}), donde los proyectos se almacenan en una tabla y las tareas asociadas al proyecto se almacenan en otra tabla. Cada proyecto está vinculado a un conjunto de tareas.

![Vincular las tareas de un proyecto a un proyecto](images/linked-tables-seatable.png)

Como gestor de proyectos, es posible que desee mostrar información sobre las tareas asociadas a cada proyecto. La fórmula Lookup puede utilizarse para seleccionar una columna de la tabla vinculada y mostrar sus valores. Por ejemplo, puede mostrar automáticamente los miembros del proyecto responsables de cada tarea.

![Columna de búsqueda](images/lookup-columns.png)

Esto puede ser útil para acceder fácilmente a la información de tablas cruzadas, establecer automatizaciones, fórmulas, etc. A continuación aprenderás más sobre el uso de la función de búsqueda.

## Para utilizar la columna Lookup

### Añadir un enlace a la tabla

La función de búsqueda sólo puede utilizarse si ya existe una columna del tipo _Enlace a otras entradas_. Si aún no dispone de una columna de este tipo, créela primero. [Aquí]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) puede ver cómo funciona.

### Añadir una fórmula de búsqueda

Al principio, la fórmula de búsqueda puede confundirle. Pero pronto verá que le encantará esta función de columna increíblemente versátil y potente. Para añadir una columna con la fórmula Lookup:

![Configuración de una columna de búsqueda](images/setup-of-lookup-column.gif)

1. Cree una nueva columna del tipo **Fórmula para los enlaces**.
2. Establezca la opción **Lookup** como fórmula.
3. Seleccione una **columna de enlace**. Este campo se rellena automáticamente si sólo tiene una columna de enlaces.
4. Con la **columna de consulta de la tabla vinculada**, se determina de qué columna de la otra tabla deben tomarse los valores.
5. Haga clic en **Enviar**.

## Preguntas frecuentes sobre la columna Lookup

{{< faq "¿Es posible introducir varios valores en una tabla mediante lookup?" >}}Definitivamente. Sólo hay que crear otra columna y volver a utilizar la función de búsqueda. De este modo, podrá leer y mostrar toda la información que desee de la tabla vinculada.
{{< /faq >}}
{{< faq "¿Se pueden modificar las búsquedas a posteriori?" >}}Por supuesto, esto es posible. Haga clic en el **símbolo del triángulo situado** a la derecha del nombre de la columna y, a continuación, en **Personalizar tipo de columna**. Ajuste la configuración de la columna e inmediatamente aparecerá la información deseada.
{{< /faq >}}
{{< faq "¿Funcionan las búsquedas con múltiples enlaces?" >}}Cada fórmula de búsqueda sólo puede obtener información de **una** columna de las tablas vinculadas. Pero, por supuesto, puedes enlazar varias tablas mediante columnas de enlace y crear otras columnas de consulta para leer y mostrar aún más información.
{{< /faq >}}
{{< faq "¿Se pueden filtrar las entradas que se consultan por búsqueda?" >}}Sí, puede filtrar las entradas como desee. Para ello, active el correspondiente **Controlador** en el _Ajustes de columna_ y seleccione el **Columna(s)** cuyas entradas deben consultarse. Puede seleccionar cualquier número de **Condiciones de filtrado** definir.

{{< /faq >}}
