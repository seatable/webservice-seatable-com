---
title: 'Páginas de calendario en aplicaciones de SeaTable'
date: 2023-12-04
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/es/ayuda/paginas-de-calendario-en-apps-seatable'
aliases:
    - '/es/ayuda/kalenderseiten-in-universellen-apps'
    - '/es/ayuda/calendario-en-apps-universales'
seo:
    title: 'Páginas de calendario en apps de SeaTable'
    description: 'Agenda colaborativa en SeaTable: visualiza y gestiona eventos, tareas y proyectos en el calendario de la app.'
weight: 5
---

Este tipo de página le permite mostrar las entradas de una o dos [columnas de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) de su tabla en un **calendario**. Un caso de uso específico podría ser, por ejemplo, la visualización en el calendario de las próximas **reuniones**.

![Próximas reuniones en una vista de calendario de la página de calendario](images/calendar-page-example.png)

## Configuración de página

Si desea cambiar la configuración de una página, haga clic en el **símbolo de rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondiente en la barra de navegación.

![Cambiar la configuración de la página de calendario](images/Einstellungen-auf-der-Kalenderseite-aendern.png)

En la **configuración de la página**, puede seleccionar el **título**, la **fecha de inicio** y el **color** de las **entradas** que aparecen en el calendario, así como el **día en que comienza** la semana, entre otras cosas.

![Configuración del tipo de página: Calendario ](images/page-settings-calendar-page.png)

## Filtros preestablecidos y columnas ocultas

Puede definir **filtros preestablecidos** y **columnas ocultas** para limitar los datos que se muestran a los usuarios.

![Añadir filtro en las páginas de calendario](images/Add-filter-on-calendar-pages-in-Universal-Apps.png)

Para ello, haga clic en **Añadir filtro**, seleccione la **columna** y la **condición** deseadas y confirme con **Enviar**.

Los usuarios pueden ver más información sobre una cita haciendo clic en una entrada del calendario.

![Abrir entradas del calendario en una aplicación](images/Kalendereintraege-in-der-Universellen-App-oeffnen.gif)

Por lo tanto, decida qué datos deben ser **visibles** y muestre u oculte las columnas correspondientes utilizando los **controles deslizantes**.

![Ocultar columnas en páginas de calendario](images/Hide-columns-on-calendar-pages-in-Universal-Apps.png)

{{< warning  headline="Nota importante"  text="Los usuarios de la aplicación **no pueden cambiar** los **filtros preestablecidos** ni las **columnas ocultas**. Por tanto, solo verán los datos filtrados como deseen." />}}

## Añadir entrada de calendario

Si dispone de la autorización adecuada, puede **añadir nuevas entradas** directamente en una página de calendario. En la vista del mes, haga clic en el pequeño **signo más** situado en la esquina superior derecha de una ficha. La **fecha de** este día ya está rellenada.

Independientemente de la fecha, también puede hacer clic en el gran **símbolo circular "más"** situado en la esquina inferior derecha de la página. Se abrirá una ventana con los **detalles de la línea**. Introduzca allí todos los datos necesarios y guarde la entrada haciendo clic en **Enviar**.

![Añadir una entrada de calendario en una aplicación](images/Kalendereintrag-hinzufuegen.gif)

## Editar y mover entradas de la agenda

Puede editar fácilmente las entradas de la agenda **haciendo clic en una entrada** y realizando los cambios deseados en los **detalles de la línea** que se abren. También puede mover cómodamente las entradas del calendario **mediante arrastrar y soltar**. SeaTable ajusta automáticamente los valores en las respectivas [columnas de fechas]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}).

![Mover y editar entradas en las páginas del calendario](images/Eintraege-auf-Kalenderseiten-verschieben-und-bearbeiten.gif)

## Configuración de la columna de enlaces

En **la configuración de la columna de enlace**, puede especificar qué datos son visibles y qué operaciones están permitidas para cada tabla enlazada.

![Configuración de columnas de enlace en páginas de calendario](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Configuración de campos**: Aquí puede definir exactamente a qué columnas se aplican las siguientes autorizaciones.
- **Añadir y vincular nuevos registros**: Si activa este control deslizante, los usuarios podrán añadir nuevas entradas a la tabla vinculada. Puede utilizar la configuración de campos para definir qué columnas son **visibles** y qué columnas son **obligatorias**, es decir, deben rellenarse.
- **Vincular registros existentes**: Si activa este control deslizante, los usuarios podrán vincular entradas existentes en la tabla vinculada. Puede utilizar los ajustes de campo para definir qué columnas son **visibles**.
- **Limitar los enlaces a máximo un registro**: Si activa este control deslizante, los usuarios sólo podrán enlazar una fila de la tabla enlazada en las celdas de la columna de enlace.
- **Filtros preestablecidos**: si añade un filtro aquí, al enlazar las entradas sólo se mostrarán las opciones que cumplan las condiciones del filtro.
- **Activar la función de big data**: Si la función big data está activada, los usuarios pueden buscar en más de 20.000 registros de datos, siempre que haya este número de entradas en la tabla vinculada.
- **Modificar registros enlazados**: Si activa este control deslizante, los usuarios podrán editar las entradas existentes en la tabla vinculada. Puede utilizar los ajustes de campo para definir qué columnas son **editables**.

## Autorizaciones de páginas

En la parte inferior de la configuración de la página, puede restringir exactamente qué usuarios están autorizados a interactuar con la página. Especifica quién está autorizado a ver la página, añadir líneas o modificar entradas.

![Autorizaciones de página en páginas de calendario](images/Seitenberechtigungen-auf-Kalenderseiten.png)
