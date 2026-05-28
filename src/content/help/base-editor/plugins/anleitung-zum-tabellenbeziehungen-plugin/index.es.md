---
title: 'Instrucciones para el plugin de relaciones entre tablas'
date: 2024-07-29
lastmod: '2024-08-01'
categories:
    - 'plugins'
author: 'kgr'
url: '/es/ayuda/guia-plugin-relaciones-tablas'
aliases:
    - '/es/ayuda/anleitung-zum-tabellenbeziehungen-plugin'
seo:
    title: 'Guía del plugin de relaciones entre tablas SeaTable'
    description: 'Aprenda a usar el plugin relaciones entre tablas de SeaTable para visualizar y gestionar conexiones entre tablas en sus bases.'

---

Especialmente cuando hay muchas tablas con docenas de columnas en una base, es fácil perder la pista de cómo se relacionan entre sí. Puedes utilizar el complemento de relaciones entre tablas para visualizar qué tablas están vinculadas entre sí a través de qué columnas.

Puede encontrar información sobre cómo activar el plugin en una base [aquí]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

![Plugin de relaciones entre tablas](images/Table-Relationships-Plugin.png)

## Funcionamiento del plugin

Una vez que haya configurado y abierto el plugin de relaciones entre tablas, verá en primer lugar **todas** las tablas de la base. **Todas las columnas** que se crean en las respectivas tablas aparecen bajo los nombres de tabla coloreados.

Para visualizar las relaciones de la tabla, no sólo verá **líneas continuas** para los enlaces _directos_ a través de [columnas de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), sino también **líneas discontinuas** para los enlaces _indirectos_ a través de columnas de fórmulas de enlace (por ejemplo, [búsquedas]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}).

## Gestión de un diagrama de relaciones

Por defecto, ya se crea un diagrama con todas las relaciones de tabla al abrir el plugin de relaciones entre tablas por primera vez. Si desea crear otro diagrama de relaciones, haga clic en {{< seatable-icon icon="dtable-icon-add-table" >}} **Añadir diagrama de relaciones**. Se abrirá un campo de entrada en el que podrá introducir el **nombre** deseado.

![Opciones de gestión de un diagrama de relaciones](images/table-relationship-plugin-management-options.png)

Cuando coloca el cursor del ratón sobre el nombre de un diagrama, aparecen tres iconos. Para **cambiar el orden de los diagramas**, mantenga pulsado el botón izquierdo del ratón sobre la **superficie de agarre** {{< seatable-icon icon="dtable-icon-drag" >}} y **arrastre y suelte** un diagrama en la posición deseada.

![Opciones de un diagrama de relaciones](images/Options-of-Table-Relationship-Chart.png)

Además, puede hacer clic en los **tres puntos** para gestionar el diagrama. Dispone de las siguientes opciones:
- **renombrar**
- **duplicar**
- **eliminar**
- **restablecer**
- **exportar como imagen**.

{{< warning  type="warning" headline="Nota"  text="Si sólo se crea un único diagrama en el plugin, **no podrá eliminarlo**." />}}

## Ajustes de un diagrama de relaciones

En los **ajustes**, a los que puede acceder haciendo clic en el **símbolo de la rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}}, puede especificar lo siguiente para un diagrama **(des)activando** los **controles deslizantes**:

- ¿Desea mostrar **enlaces a otras tablas** (conexiones directas)?
- ¿Desea mostrar **enlaces dentro de una tabla** (conexiones directas)?
- ¿Desea mostrar **fórmulas de enlaces** (conexiones indirectas)? En caso afirmativo, ¿qué tipos de fórmulas de enlace?
- ¿Desea mostrar **todas las columnas independientemente de las vistas**?
- ¿Desea mostrar **tablas sin enlaces**?
- ¿Desea **mostrar u ocultar tablas**?

![Opciones de configuración de un diagrama de relaciones](images/table-relationship-plugin-settings.png)

## Opciones de diseño de un diagrama de relaciones

Vaya a la pestaña **Diseño** en la parte superior derecha junto a los ajustes para cambiar el estilo de determinados elementos en un diagrama. Haga clic en la **flecha desplegable** delante de un elemento para mostrar los ajustes disponibles:

- **Tablas**: color del encabezado de la tabla y tamaño de fuente
- **Columnas de enlace** (conexiones directas): grosor de línea, estilo de línea y color de línea
- **Fórmulas de enlaces** (conexiones indirectas de primer nivel): grosor de línea, estilo de línea y color de línea
- **Fórmulas de enlace de varios niveles** (conexiones anidadas de niveles superiores, por ejemplo, una fórmula de búsqueda que obtiene valores a través de otra columna de enlace de la tabla vinculada): grosor de línea, estilo de línea y color de línea
- **Establecer color de fondo para la exportación**

![Opciones de diseño de un diagrama de relaciones](images/table-relationship-plugin-theme.png)

## Mover tablas en un diagrama

Puede mover las distintas tablas en un diagrama según sus necesidades mediante la **función de arrastrar y soltar**. Para ello, mantenga pulsado el botón izquierdo del ratón, arrastre la tabla a la posición deseada y suéltelo.

![Mover tablas en un diagrama de relaciones mediante arrastrar y soltar](images/Move-tables-in-a-Table-Relationship-Chart.gif)

## Añadir una nota a un diagrama de relaciones

Además, puede añadir una nota a un diagrama de relaciones haciendo clic en el icono de la nota en la esquina inferior izquierda. A continuación, dispone de las siguientes opciones:

- editar texto
- ocultar fondo
- alinear el texto a la izquierda, al centro o a la derecha
- eliminar nota

![Añadir una nota a un diagrama de relaciones](images/add-note-on-table-relationship-chart.png)
