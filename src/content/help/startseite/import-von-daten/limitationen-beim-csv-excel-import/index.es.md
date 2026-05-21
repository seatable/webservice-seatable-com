---
title: 'Limitaciones de la importación CSV/Excel'
date: 2022-10-15
lastmod: '2024-05-10'
categories:
    - 'import-von-daten'
author: 'nsc2'
url: '/es/ayuda/limitaciones-importacion-csv-excel'
aliases:
    - '/es/ayuda/limitationen-beim-csv-excel-import'
seo:
    title: 'Limitaciones en la importación CSV/Excel en SeaTable explicadas'
    description: 'Descubre las restricciones al importar archivos CSV y Excel en SeaTable Cloud y Server. Tamaño de archivo, filas permitidas y recomendaciones clave.'

---

SeaTable dispone de una potente función de importación para facilitarle al máximo la **importación de registros de datos desde archivos XLSX o CSV**. En la mayoría de los casos, la importación funciona sin dificultades. Si intenta importar demasiados registros a la vez, SeaTable le advertirá del límite. Mientras que puede elegir libremente los **límites para el tamaño del archivo y el número de filas** en los servidores SeaTable autoalojados, SeaTable Cloud le impone ciertos límites.

## Tamaño máximo de archivo y número de líneas para SeaTable Cloud

Si importa archivos Excel, SeaTable lo soporta para archivos de hasta un tamaño máximo de **100 MB** y hasta **50.000 filas**. Debido a estos generosos límites, nunca debería tener problemas con el tamaño del archivo. Si tiene un archivo más grande o con más filas, deberá dividirlo en dos **archivos Excel** y realizar la importación en dos pasos.

{{< warning  headline="Límite de memoria para líneas" >}}

El backend normal de SeaTable puede contener un máximo de 100.000 filas por tabla. Si desea importar un archivo Excel o CSV que contenga más de 100.000 filas, primero debe [activar el]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) backend de big data para poder [importar]({{< relref "help/base-editor/big-data/eine-excel-tabelle-ins-big-data-backend-importieren" >}}).

{{< /warning >}}

## Gráficos y archivos incrustados

**No** es posible importar gráficos y archivos mediante un archivo XLSX. Para dicha importación debe utilizar la API de SeaTable, con la que podrá importar imágenes y archivos sin dificultad.

## Enlaces a otros registros

No es posible importar datos al tipo de columna **Enlace a otros registros**. Dado que SeaTable es una [base de datos relacional]({{< relref "posts/relationale-datenbank" >}}), los enlaces funcionan además de forma diferente a las referencias cruzadas en Excel.

Todo lo relativo al manejo de la columna de enlace en SeaTable se encuentra [aquí]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

{{< warning headline="Nota" >}}
Tras la importación, también puede utilizar la operación de procesamiento de datos [Comparar y enlazar]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}}) para crear enlaces entre registros específicos.
{{< /warning >}}

## Formatos de archivo diferentes

La función de importación de SeaTable se ha probado con archivos de **LibreOffice**, así como con archivos actuales de **Microsoft Excel**. Otros programas de Office (como los de la empresa Softmaker) **no** se prueban activamente, lo que puede dar lugar a resultados de importación divergentes. En caso de duda, utiliza Microsoft Excel o el programa gratuito LibreOffice para obtener los mejores resultados.

{{< warning  headline="Utilizar Excel o Libre Office" >}}

Si sigue teniendo problemas para importar datos, le recomendamos que consulte el artículo [Consejos y trucos para importar archivos CSV o XLSX]({{< relref "help/startseite/import-von-daten/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien" >}}). En él se describen los escollos típicos.

{{< /warning >}}
