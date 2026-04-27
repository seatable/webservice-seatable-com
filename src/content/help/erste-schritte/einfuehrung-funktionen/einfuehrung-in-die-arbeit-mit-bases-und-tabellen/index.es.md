---
title: 'Introducción al trabajo con bases y tablas'
date: 2023-01-07
lastmod: '2023-03-24'
categories:
    - 'seatable-nutzen'
author: 'cdb'
url: '/es/ayuda/introduccion-bases-tablas-seatable'
aliases:
    - '/es/ayuda/einfuehrung-in-die-arbeit-mit-bases-und-tabellen'
seo:
    title: 'Introducción a Bases y Tablas en SeaTable – guía esencial'
    description: 'Aprenda a gestionar Bases y Tablas en SeaTable. Pasos, vistas, tipos de columnas y consejos para estructuras y relaciones de datos eficientes.'
---

Cada uno de los iconos cuadrados de su página de inicio representa una **base**. Se trata de una base de datos, comparable a un libro de trabajo de una hoja de cálculo convencional, y puede contener varias **tablas** sobre distintos temas.

![Vista general de la base en SeaTable](images/base-overview.png)

Una base representa una **unidad** autónoma en SeaTable. Por lo tanto, debe contener toda la información que necesita para un proyecto o proceso específico.

Por ejemplo, la base para su canal de ventas puede contener tablas separadas para clientes potenciales, empresas y oportunidades de negocio. Del mismo modo, puede utilizar una base para planificar una boda y crear tablas independientes para los posibles lugares de celebración, los asistentes y las listas de tareas pendientes.

## Crear una nueva base

SeaTable ofrece varias maneras de crear una nueva base. Si es nuevo en SeaTable, le recomendamos que comience con una **plantilla** para que pueda ver cómo se construye normalmente una base. Puede elegir una plantilla existente adaptada a su caso de uso de nuestra galería de plantillas y luego simplemente adaptarla a sus propias necesidades.

Si está familiarizado con la creación de sus propias tablas, columnas y vistas, puede empezar con una base vacía.

- [Creación de una base mediante una plantilla]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}})
- [Crear una nueva base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Importar archivos de Excel a SeaTable]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}})
- [Duplicar una base existente]({{< relref "help/startseite/bases/duplizieren-einer-bestehenden-base" >}})

## Gestionar las bases

Una vez que haya dominado los primeros pasos y haya creado sus primeras bases, podrá descubrir toda una serie de funciones adicionales en la página de inicio y en sus bases. Todo lo que necesita saber sobre la gestión de sus bases lo encontrará en el capítulo [Bases]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}).

## Tablas y vistas en una base

La tabla es el nivel más importante en el que puede organizar sus datos en SeaTable, comparable a una hoja de cálculo. Básicamente, **las tablas** son el siguiente nivel por debajo de las bases en la estructura organizativa de SeaTable.

Dado que SeaTable es una [base de datos relacional]({{< relref "posts/relationale-datenbank" >}}), puede vincular la información de diferentes tablas de una base mediante [enlaces]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}), [automatizaciones]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) y otras funciones.

Una tabla consta de filas y columnas. Todas las entradas de una **fila** forman un **conjunto de datos** coherente. Los [tipos de columna]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) en SeaTable definen qué **tipos de datos** puede introducir en una **columna**.

Cada vez que visualiza sus datos en una tabla, lo hace a través de una [vista]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}). Las vistas le ofrecen un sinfín de opciones para mostrar los datos de sus tablas de forma diferente: filtrarlos, ordenarlos, agruparlos, ocultarlos, etc.
