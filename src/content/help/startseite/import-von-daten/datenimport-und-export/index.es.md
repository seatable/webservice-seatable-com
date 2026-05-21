---
title: 'Importación y exportación de datos'
date: 2022-08-25
lastmod: '2024-03-11'
categories:
    - 'import-von-daten'
author: 'cdb'
url: '/es/ayuda/importacion-exportacion-datos-seatable'
aliases:
    - '/es/ayuda/datenimport-und-export'
seo:
    title: 'Importación y exportación de datos en SeaTable: bases, Excel, CSV'
    description: 'Descubre cómo importar y exportar bases y tablas en SeaTable con formatos DTABLE, Excel y CSV—guía completa, consejos y solución de problemas.'
star: true
weight: 1
---

Las funciones de importación de SeaTable permiten cambiar de otras soluciones a SeaTable con poco esfuerzo. Lo mismo se aplica al cambio de un sistema SeaTable a otro, por ejemplo, al migrar de SeaTable Cloud a un sistema autoalojado. Puede seguir trabajando sin problemas en una base que haya importado de otra instancia de SeaTable.

El tema de este artículo es cómo exportar bases y tablas de SeaTable e importarlas a SeaTable.

## Exportar base

Puede exportar el estado actual de tus bases incluyendo todas las tablas, [vistas]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}), [formularios web]({{< relref "help/base-editor/webformulare/webformulare" >}}) y plugins. Los [comentários]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), las [automatizaciones]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}) y el [historial de cambios]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}), así como [los datos del Big Data backend]({{< relref "help/base-editor/big-data/potenzial-big-data" >}}), **no se exportan**.

![Bases de exportación](images/export-bases.png)

SeaTable utiliza el [formato de archivo DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}) para exportar bases. Para más información, consulte el artículo [Guardar una base como archivo]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}) DTABLE.

## Exportar tabla

Puede **exportar a archivos Excel tablas** individuales de cada base a la que tenga acceso. Los contenidos de las columnas basadas en texto y números se copian como valores en el archivo de destino. Los [comentários]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), las [automatizaciones]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}) y el [historial de cambios]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) **no se exportan**.

![Exportación de tablas](images/export-tables.jpg)

Inicie la exportación de una tabla desde Base. Haga clic en la flecha desplegable situada a la derecha del nombre de la tabla que desea exportar. A continuación, seleccione **Exportar tabla a un archivo XLSX**.

![Confirmar la exportación de la tabla](images/confirm-view-export.png)

Decida si desea **incluir imágenes en el archivo de exportación** activando o no el interruptor. Confirme con **Exportar** para iniciar la descarga. Una vez finalizada la exportación, encontrará el archivo XLSX en la ubicación seleccionada de su dispositivo.

## Exportar vista

¿No desea exportar todos los datos de una tabla? ¡Entonces limite la [vista]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) con **filtros** y **columnas ocultas**! Si desea exportar una vista de tabla, haga clic en los **tres puntos** en las opciones de vista situadas encima de la tabla y, a continuación, en **Exportar vista a un archivo XLSX**. 

![Exportar vista](images/export-view.png)

Decida si desea **incluir imágenes en el archivo de exportación** activando o no el interruptor. 

![Confirmar la exportación de la vista](images/confirm-view-export.png)

En cuanto haga clic en **Exportar**, se iniciará la descarga. Después encontrará el archivo XLSX en la ubicación seleccionada de su dispositivo.

## Importar base

SeaTable admite la importación de bases desde su propio [formato DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}), desde **archivos Excel** y desde el **formato** genérico **CSV**. Asimismo, puede importar bases de Airtable a SeaTable.

Al importar un archivo **DTABLE**, la base se restablece exactamente con el mismo aspecto que tenía en el momento de la exportación. Al importar un archivo CSV o Excel, los valores del archivo CSV/XLSX se copian en columnas de tabla de una nueva base, y SeaTable intenta interpretar los tipos de columna basándose en los datos.

![Importar datos a una base](images/import-data-into-your-base.png)

Lo que hay que tener en cuenta al importar una base depende del tipo de archivo de importación. Sin embargo, el procedimiento es el mismo para todos los tipos de archivo: Vaya a la **página de inicio** y haga clic en **Añadir una base o carpeta** en el área o grupo donde desee tener la nueva base. Encontrará información más detallada en los siguientes artículos:

- [Creación de una base a partir de un archivo DTABLE]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei" >}})
- [Importar archivos de Excel a SeaTable]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}})
- [Importación de datos mediante CSV en SeaTable]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}})
- [Migración de bases de Airtable a SeaTable]({{< relref "help/startseite/import-von-daten/migration-von-airtable-bases-zu-seatable" >}})

## Importar tabla

En las bases existentes, puede **rellenar tablas individuales mediante la importación de CSV o Excel**. Tiene las siguientes opciones: Puede importar los datos en una **tabla** existente

![Importar datos en una tabla existente](images/Daten-in-eine-bestehende-Tabelle-importieren.png)

o importar los datos a una **nueva tabla**.

![Rellenar tablas existentes mediante la importación de datos](images/import-data-in-table.jpg)

La importación se realiza como [archivo CSV]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}}) o [archivo Excel]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}}) en la tabla. Para más información, consulte los artículos enlazados.

Si ya ha creado una tabla en **SeaTable** y la necesita en **otra** base, puede simplemente copiarla. Puede averiguar cómo importar tablas de otra base [aquí]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}}).

{{< warning  headline="Límite de memoria para líneas" >}}

El backend normal de SeaTable puede contener un máximo de 100.000 filas por tabla. Si desea importar un archivo Excel o CSV que contenga más de 100.000 filas, primero debe [activar el backend de Big Data]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) para poder importarlo.

{{< /warning >}}

## Otros artículos útiles sobre el tema de la importación de datos

- [Trucos y consejos para importar archivos CSV o XLSX]({{< relref "help/startseite/import-von-daten/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien" >}})
- [Limitaciones de la importación CSV/Excel]({{< relref "help/startseite/import-von-daten/limitationen-beim-csv-excel-import" >}})
- [Importación de registros de datos CSV a una base existente]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}})
