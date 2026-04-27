---
title: 'Páginas de línea de tiempo en aplicaciones de SeaTable'
date: 2023-12-04
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/es/ayuda/paginas-de-linea-de-tiempo-en-apps-seatable'
aliases:
    - '/es/ayuda/zeitstrahlseiten-in-universellen-apps'
    - '/es/ayuda/paginas-de-cronologia-en-apps-universales'
seo:
    title: 'Páginas de línea de tiempo en apps de SeaTable'
    description: 'Visualiza y planifica proyectos y eventos con cronogramas interactivos en SeaTable Apps.'
weight: 8
---

Este tipo de página le permite mostrar diferentes intervalos de tiempo en forma de **línea de tiempo**. Como esta vista de datos revela fechas que se solapan, la **planificación de las vacaciones en una empresa**, por ejemplo, podría ser un caso de uso específico.

![Página Timeline en SeaTable Apps](images/Timeline-page-in-Universal-Apps.png)

## Configuración de página

Si desea cambiar la configuración de una página, haga clic en el **símbolo de rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondiente en la barra de navegación.

![Cambiar la configuración de la página de la línea de tiempo](images/Einstellungen-der-Zeitstrahlseite-aendern.png)

En la **configuración de la página**, puede establecer en primer lugar la representación gráfica de las líneas de tiempo. Para ello, seleccione el [color de la fila]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}) o de una columna [de selección]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}), que determina el **color de los** bloques. También puede definir una columna para el **etiquetado de los** bloques.

![Ajuste gráfico de las líneas de tiempo en las aplicaciones](images/Grafische-Einstellung-der-Zeitleisten.png)

Para definir el período de las entradas, necesita una [columna de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) para la **fecha de inicio**. Para la **fecha de finalización**, puede utilizar otra columna de fecha o una columna numérica diferente – [número]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}), [duración]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}}) o [fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) – que indique la cantidad de días. Además, puede seleccionar el **intervalo de tiempo**, es decir, cuántos años debe abarcar la línea de tiempo.

![Configuración de la página de la línea de tiempo en aplicaciones](images/Seiteneinstellungen-der-Zeitstrahlseite-in-Universellen-Apps.png)

## Filtros preestablecidos y columnas ocultas

Puede definir **filtros preestablecidos** y **columnas ocultas** para limitar los datos que se muestran a los usuarios. Para ello, haga clic en **Añadir filtro**, seleccione la **columna** y la **condición** deseadas y confirme con **Enviar**.

![Añadir filtro en las páginas de línea de tiempo en SeaTable Apps](images/Add-filter-on-timeline-pages-in-Universal-Apps.png)

Los usuarios pueden ver más información sobre una entrada haciendo clic en un bloque de la línea de tiempo. Por lo tanto, decida qué datos deben ser **visibles** y muestre u oculte las columnas correspondientes utilizando los **controles deslizantes**.

![Ocultar columnas en páginas de cronología en SeaTable Apps](images/Hide-columns-on-timeline-pages-in-Universal-Apps.png)

{{< warning  headline="Nota importante"  text="Los usuarios de la aplicación **no pueden cambiar** los **filtros preestablecidos** ni las **columnas ocultas**. Por tanto, solo verán los datos filtrados como deseen." />}}

Si añade una **agrupación**, las barras también pueden visualizarse en **swimlanes**. En el caso de las actividades que no se solapan, esta opción de visualización da como resultado una visualización compacta y clara.

![Agrupación en páginas de cronología](images/Grouping-on-timeline-pages.png)

## Editar o mover una entrada en la línea de tiempo

Puede editar fácilmente las entradas haciendo clic en una **barra** y realizando los cambios deseados en los **detalles de la línea** que se abren.

![Modificar las entradas de las páginas de la cronología](images/Eintraege-auf-Zeitstrahlseiten-aendern.gif)

También puede **ampliar** o **reducir** el **lapso de** tiempo directamente en la línea de tiempo. Para ello, agarra el **borde** derecho o izquierdo **de la barra** y arrástralo hasta la fecha deseada.

![Mover entradas a páginas de cronología](images/Eintraege-auf-Zeitstrahlseiten-verschieben.gif)

También puede **mover** cómodamente las entradas en la línea de tiempo **mediante arrastrar y soltar**. SeaTable ajusta automáticamente los **valores de fecha** respectivos.

## Configuración de la columna de enlaces

En **la configuración de la columna de enlace**, puede especificar qué datos son visibles y qué operaciones están permitidas para cada tabla enlazada.

![Configuración de columnas de enlace en páginas de línea de tiempo](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Configuración de campos**: Aquí puede definir exactamente a qué columnas se aplican las siguientes autorizaciones.
- **Añadir y vincular nuevos registros**: Si activa este control deslizante, los usuarios podrán añadir nuevas entradas a la tabla vinculada. Puede utilizar la configuración de campos para definir qué columnas son **visibles** y qué columnas son **obligatorias**, es decir, deben rellenarse.
- **Vincular registros existentes**: Si activa este control deslizante, los usuarios podrán vincular entradas existentes en la tabla vinculada. Puede utilizar los ajustes de campo para definir qué columnas son **visibles**.
- **Limitar los enlaces a máximo un registro**: Si activa este control deslizante, los usuarios sólo podrán enlazar una fila de la tabla enlazada en las celdas de la columna de enlace.
- **Filtros preestablecidos**: si añade un filtro aquí, al enlazar las entradas sólo se mostrarán las opciones que cumplan las condiciones del filtro.
- **Activar la función de big data**: Si la función big data está activada, los usuarios pueden buscar en más de 20.000 registros de datos, siempre que haya este número de entradas en la tabla vinculada.
- **Modificar registros enlazados**: Si activa este control deslizante, los usuarios podrán editar las entradas existentes en la tabla vinculada. Puede utilizar los ajustes de campo para definir qué columnas son **editables**.

## Autorizaciones de páginas

En la parte inferior de la configuración de la página, puede restringir quién puede **ver** la página de la línea de tiempo y **editar** las entradas. No se pueden añadir ni eliminar filas a través de las páginas de línea de tiempo.

![Autorizaciones de página para las páginas de la línea de tiempo](images/Seitenberechtigungen-von-Kalenderseiten.png)
