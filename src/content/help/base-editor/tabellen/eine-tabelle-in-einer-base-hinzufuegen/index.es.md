---
title: 'Añadir una tabla en una Base'
date: 2022-09-28
lastmod: '2025-02-28'
categories:
    - 'arbeiten-in-tabellen'
author: 'nsc2'
url: '/es/ayuda/anadir-tabla-base-seatable'
aliases:
    - '/es/ayuda/eine-tabelle-in-einer-base-hinzufuegen'
seo:
    title: 'Añadir tabla nueva a una base en SeaTable: fácil'
    description: 'Cree o importe una tabla nueva a una base existente. Añada manualmente o desde archivo y gestione vínculos entre tablas fácilmente.'

---

Las bases constan de una o varias tablas, que a su vez pueden contener datos muy diferentes y enlazarse entre sí. Una base puede contener **hasta 200 tablas**. Sin embargo, en aras de la claridad, debería considerar dividir las tablas en varias bases y sincronizar los datos con la función [Conjuntos de datos compartidos]({{< relref "help/startseite/gemeinsame-datensaetze/funktionsweise-von-gemeinsamen-datensaetzen" >}}) si tiene más de 20 tablas.

## Añadir una tabla en una base

1. En el **Base abierta** En la esquina superior izquierda verás las pestañas con todos los **Tablas** de la base.

    ![Tablas en una base de SeaTable](images/Tabellen-in-seatable.png)

2. Haga clic en el **símbolo más** situado a la derecha de la última pestaña de la tabla.
3. Ahora seleccione **Añadir tabla**.
4. Dé un **nombre** a la nueva tabla y confirme con **Enviar**.

## Importar tabla desde un archivo

También puede importar tablas de **archivos** a su Base. La importación se realiza como [archivo CSV]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}#tabelle_importieren) encontrará información detallada sobre la importación de datos.

![Importar tabla desde un archivo](images/import-data-in-table.jpg)

## Importar tabla de otra base

En SeaTable, [las bases]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}) son básicamente unidades separadas, pero no es raro necesitar datos en otra base. En lugar de tener que exportar una tabla de una base e importarla a la base deseada, SeaTable ofrece la cómoda opción de **importar** tablas **directamente** desde otras bases y transferir así datos a través de los límites de las bases.

![Importar una tabla de otra base](images/import-table-from-other-base.gif)

Con los [registros compartidos]({{< relref "help/startseite/gemeinsame-datensaetze/funktionsweise-von-gemeinsamen-datensaetzen" >}}), también puede compartir una tabla maestra en un grupo y utilizar y sincronizar los vástagos de la tabla en diferentes bases. Para más información [, haz clic aquí]({{< relref "help/startseite/gemeinsame-datensaetze/mit-einem-gemeinsamen-datensatz-eine-neue-tabelle-anlegen" >}}).

## Mantener la visión de conjunto

A veces una imagen vale más que mil palabras. SeaTable también permite utilizar emojis en el nombre de la tabla, lo que acorta las pestañas de la tabla.

![Emojis en el nombre de la tabla](images/emojis-seatable-table-name.png)

Encontrará instrucciones detalladas en el artículo [Utilizar emojis en los nombres de tabla]({{< relref "help/base-editor/tabellen/verwendung-von-emojis-im-tabellennamen" >}}).
