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

## Configuración de opciones para un gráfico de relaciones de tabla

Por defecto, se crea un gráfico con todas las relaciones de tabla cuando se abre el plugin de relaciones de tabla por primera vez. {{< seatable-icon icon="dtable-icon-add-table" >}} Si desea crear otro gráfico, haga clic en **Añadir nueva** relación de tabla. Se abrirá un campo de entrada en el que podrá introducir el **nombre** deseado.

![Opciones de un gráfico de relaciones de tablas](images/Options-of-Table-Relationship-Chart.png)

{{< seatable-icon icon="dtable-icon-drag" >}} Para **cambiar** el **orden de los** gráficos, mantenga pulsado el botón izquierdo del ratón sobre la **superficie de agarre** y **arrastre y suelte** un gráfico en la posición deseada. También puede **renombrar**, **duplicar** o **eliminar** los gráficos.

{{< warning  headline="Nota"  text="Si sólo se crea un gráfico en el plugin, **no podrá eliminarlo**." />}}

{{< seatable-icon icon="dtable-icon-set-up" >}} En los **ajustes**, a los que puede acceder haciendo clic en el **símbolo de la rueda dentada**, puede especificar lo siguiente para el gráfico **(des)activando** los **controles deslizantes**:

- ¿Desea mostrar **enlaces a otras entradas** (conexiones directas)?
- ¿Desea visualizar **fórmulas de enlaces** (enlaces indirectos)?
- ¿Desea mostrar **fórmulas de dos niveles para los enlaces** (por ejemplo, una fórmula de búsqueda que toma valores de la columna de búsqueda de otra tabla)?
- ¿Desea mostrar **tablas sin enlaces**?

![Configuración de opciones para un gráfico de relaciones de tabla](images/Settings-of-Table-Relationship-Chart.png)

## Mover tablas en un gráfico

Puede desplazar las distintas tablas del gráfico según sus necesidades mediante la **función de arrastrar y soltar**. Para ello, mantenga pulsado el botón izquierdo del ratón, arrastre la tabla a la posición deseada y suéltelo.

![Mover tablas en un gráfico de relaciones de tablas mediante arrastrar y soltar](images/Move-tables-in-a-Table-Relationship-Chart.gif)
