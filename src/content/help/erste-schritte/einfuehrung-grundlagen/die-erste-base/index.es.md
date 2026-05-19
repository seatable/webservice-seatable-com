---
title: 'La primera base'
date: 2022-08-25
lastmod: '2023-05-15'
categories:
    - 'kurzanleitungen'
author: 'cdb'
url: '/es/ayuda/crear-primera-base-seatable'
aliases:
    - '/es/ayuda/die-erste-base'
seo:
    title: 'SeaTable: cómo crear y gestionar tu primera base'
    description: 'Aprende a crear una base en SeaTable, agregar tablas, columnas y relaciones para organizar tus datos y colaborar de manera efectiva.'
---

En SeaTable usted organiza sus datos en [bases]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}). Una base es un contenedor para una o varias tablas. Las tablas de una base pueden ser independientes entre sí o, como en una base de datos, estar vinculadas mediante relaciones.

También puedes [compartir]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) con otros miembros del equipo o [invitar a]({{< relref "help/startseite/freigaben/unterschiede-zwischen-einladungs-links-und-externen-links" >}}) terceros externos a trabajar en ellas juntos.

SeaTable mantiene un [historial]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) de cada base en segundo plano, lo que le permite deshacer cambios y restaurar estados anteriores si lo necesita.

## La página de inicio

Después de iniciar sesión, te encontrarás en la página de **inicio**. Aquí puede gestionar sus bases. Si ha seleccionado [plantillas]({{< relref "templates" >}}) durante el registro, se mostrarán aquí.

Haciendo clic en la **imagen del avatar**, en la esquina superior derecha, puedes pasar a la [configuración personal]({{< relref "help/startseite/persoenliche-einstellungen" >}}) para ajustar, por ejemplo, el idioma del sistema.

Haz clic en **Añadir base** para crear tu primera base. Dele un **nombre**, pulse **Intro** y la base se colocará en la página de inicio. Si pasa el puntero del ratón por encima del nombre de la base, aparecerá a la derecha el **símbolo de un lápiz** {{< seatable-icon icon="dtable-icon-rename" >}} y el símbolo de tres puntos {{< seatable-icon icon="dtable-icon-more-vertical" >}} para las funciones ampliadas.

Con el icono del lápiz, puedes cambiar el nombre de la base y asignarle un icono y un color diferentes. Las funciones avanzadas incluyen, por ejemplo, [compartir]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) una base o [exportarla]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}). Para abrir la base, haz clic en su nombre.

## Vista de la tabla

La nueva Base contiene una [tabla]({{< relref "help/erste-schritte/einfuehrung-funktionen/einfuehrung-in-die-arbeit-mit-bases-und-tabellen" >}}) desde el principio. La vista de tabla es la vista central, pero no la única, de SeaTable. En la vista de tabla usted gestiona las tablas de la base, define su estructura de columnas e introduce o analiza sus datos.

SeaTable ofrece un total de [más de 20 tipos de columnas]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}). Probablemente ya esté familiarizado con las columnas de texto, números y fechas de las hojas de cálculo convencionales. Por supuesto, SeaTable también las conoce. Además, SeaTable ofrece columnas para imágenes y archivos, botones y casillas de verificación, así como campos de selección única y múltiple.

¿Quieres añadir fotos a una entrada? Basta con arrastrar la imagen a una columna de imágenes para que SeaTable la guarde directamente en la tabla. En SeaTable tienes todos tus datos en un solo lugar.

Otro tipo de columna que no le resultará familiar de una hoja de cálculo es el enlace [a otras entradas]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Con los enlaces se crean relaciones entre filas de diferentes tablas. Este procedimiento, que se corresponde con el funcionamiento de las bases de datos relacionales, evita las entradas dobles, garantiza la coherencia de los datos y crea una visión de conjunto.

He aquí un ejemplo de aplicación: Una empresa de gestión inmobiliaria registra los objetos gestionados en una tabla y los vincula a los inquilinos gestionados en otra tabla. Si algo cambia en las propiedades del objeto, el gestor sólo tiene que modificar el ajuste en la tabla de objetos. Mediante la vinculación, la información modificada se actualiza automáticamente para todos los inquilinos asignados.

[Puede crear tablas adicionales utilizando las pestañas de tabla]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}}). Cada tabla tiene un diseño individual: diseñe las columnas según sus propios deseos y necesidades.
