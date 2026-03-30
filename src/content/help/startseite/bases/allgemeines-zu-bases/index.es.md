---
title: 'Información general sobre las bases en SeaTable'
date: 2022-08-25
lastmod: '2023-05-03'
categories:
    - 'arbeiten-mit-bases'
author: 'cdb'
url: '/es/ayuda/bases-funciones-gestion-seatable'
aliases:
    - '/es/ayuda/bases'
seo:
    title: 'Bases en SeaTable: guía completa para gestión eficiente'
    description: 'Bases en SeaTable: saiba cómo organizarlas, gestionarlas, compartir, exportar, restaurar, eliminar y trabajar más productivo cada día.'
star: true
weight: 1
---

Las bases tienen una importancia central en SeaTable. Siempre que introduzca, analice, edite o comparta datos en SeaTable, estará en una base.

A primera vista, una base no es más que un **contenedor** para una o varias **tablas**. Desde esta perspectiva, parece obvio comparar una base con un libro de Excel. Sin embargo, esta comparación no hace justicia a una base. Las bases en SeaTable son muy superiores a los libros de trabajo tal y como se conocen en las hojas de cálculo convencionales, porque ofrecen:

- Funciones de [bases de datos relacionales]({{< relref "posts/relationale-datenbank" >}}) y [vinculación de tablas]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})
- [Más de 20 tipos de columnas]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) que cubren todos los formatos de datos habituales
- Varias [opciones para compartir]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) datos fácilmente
- [Colaboración]({{< relref "help/erste-schritte/einfuehrung-funktionen/zusammenarbeit" >}}) en tiempo real con otros usuarios y transmisión en tiempo real de todos los cambios
- Una [función de comentario para]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) cada registro de una fila
- [Versionado]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) de todos los cambios
- Un [editor de formularios web]({{< relref "help/base-editor/webformulare/webformulare" >}}) y [plugins]({{< relref "help/base-editor/ansichten" >}}) gráficos integrados
- Opciones de integración sencillas gracias a la API REST

Las bases son, por tanto, mucho más que "contenedores de tablas" en la web. Apreciará rápidamente estas ventajas y no querrá volver a prescindir de ellas.

## Propietario de bases

Cada base tiene un (y sólo un) **propietario**. No obstante, es posible transferir la propiedad de una base de un usuario a otro.

El propietario de una base puede ser un **usuario** o un **grupo**. Si un usuario es el propietario de una base, sólo este usuario tiene pleno poder de disposición. Si la base pertenece a un grupo, todos los administradores del grupo tienen pleno acceso a ella. Aquí puede obtener más información sobre los [permisos de cada uno de los miembros]({{< relref "help/startseite/gruppen/gruppenmitglieder-und-ihre-berechtigungen" >}}) del grupo.

La transferencia directa de propiedad de un usuario a otro no es posible actualmente (a partir de 20.3.2023). Sin embargo, se puede **cambiar** la propiedad indirectamente exportando una base y haciendo que el nuevo propietario la importe. Encontrará más información sobre la importación y exportación de bases en el artículo [Importación y exportación de datos]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}).

## Creación de bases

Puede crear **nuevas bases** a través de la página de inicio. Siempre estará en la página de inicio cuando se conecte a SeaTable. Si está trabajando en una base, puede volver a la página de inicio haciendo clic en el **icono de la base** {{< seatable-icon icon="dtable-icon-dtable-logo" >}} en la parte superior izquierda.

En el área **Mis Bases** y en cada **grupo** en el que seas administrador, encontrarás el botón **Añadir una Base o Carpeta**. Haz clic en este botón para crear una nueva base donde quieras.

Tiene **tres opciones** a la hora de crear una nueva base. Puede obtener más información al respecto en los artículos correspondientes:

- [Crear una base vacía]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Importar la base desde un archivo]({{< relref "help/startseite/import-von-daten/welche-import-formate-unterstuetzt-seatable" >}})
- [Crear base a partir de una plantilla]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}})

## Gestión de la base

Las bases se gestionan a través del **menú contextual** de la página de inicio. Si pasas el puntero del ratón por encima de una de tus bases, aparecerá un **icono en forma de lápiz** a la derecha del nombre {{< seatable-icon icon="dtable-icon-rename" >}} y un **icono de tres puntos** {{< seatable-icon icon="dtable-icon-more-vertical" >}} para las opciones avanzadas. Las necesitarás regularmente para gestionar tus bases.

No puede **gestionar** bases que le hayan sido liberadas. Sólo hay dos opciones disponibles en las funciones avanzadas de dichas bases: **Salir de la base compartida** y **Copiar**.

## Renombrar bases

Posteriormente podrá **renombrar** las bases de las que sea propietario o administrador. Sitúe el puntero del ratón sobre el nombre de la base que desea renombrar y, a continuación, haga clic en el **icono del lápiz** {{< seatable-icon icon="dtable-icon-rename" >}}. Ahora puede cambiar el nombre y guardarlo pulsando la **tecla Intro**. Lee [aquí]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}}) lo que debes tener en cuenta a la hora de poner nombre a una base.

## Cambiar el icono y el color de una base

Puedes dar un nuevo aspecto a las bases de las que eres propietario o administrador. Descubre cómo hacerlo [aquí]({{< relref "help/startseite/bases/aussehen-einer-base-anpassen-icon-und-farbe" >}}). Para dar un soplo de aire fresco a tus bases, tienes a tu disposición más de **10 colores** y **más de 25 iconos**.

## Añadir descripción de la base

Puedes añadir una descripción a tus bases para dar a otros usuarios "instrucciones de uso" o para registrar información adicional sobre una base. Puedes aprender a utilizar esta función [aquí]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}}).

## Bases de la liberación

Puedes **compartir** las bases que posees o administras con otros **usuarios y grupos**, dándoles acceso a los datos. El uso compartido se realiza con diferentes permisos para que siempre tengas el control sobre los cambios en tus bases.

Encontrará más información sobre esta función tan importante y útil en el artículo [Base y ver comunicados de]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) un vistazo.

## Base de copias

Puedes **copiar** todas las bases a las que tengas acceso. Dependiendo de la procedencia de la base y del lugar al que quieras copiarla, te ayudará el artículo [Duplicar una]({{< relref "help/startseite/bases/eine-base-in-eine-gruppe-kopieren" >}}).

## Mover bases a carpetas o añadir a favoritos

Si se ha acumulado un gran número de bases en tu página de inicio, puede ser útil para mayor claridad [agrupar varias bases en carpetas]({{< relref "help/startseite/bases/eine-base-zu-den-favoriten-hinzufuegen" >}}) las bases a las que accedes con más frecuencia.

## Base de exportación

Puede exportar bases para hacer una copia de seguridad de los datos, para transferirlos a otro usuario o para transferirlos a otro servidor SeaTable. Básicamente, la exportación tiene lugar en un [archivo DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}).

Para obtener más información sobre la exportación de bases, consulte el artículo [Guardar una base como archivo DTABLE]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}).

## Borrar y restaurar bases

Puedes [borrar]({{< relref "help/startseite/papierkorb/loeschen-einer-base" >}}) las bases que poseas o administres si es necesario y [restaurarlas]({{< relref "help/startseite/papierkorb/eine-geloeschte-base-wiederherstellen" >}}) durante un máximo de 30 días. Sigue las instrucciones de los artículos enlazados.

### Restaurar base desde instantánea

Puede ver y restaurar instantáneas de las bases que posee o administra. Todo lo que necesita saber sobre las instantáneas en SeaTable se puede encontrar en los siguientes artículos

- [Guardar la base actual como una instantánea]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}})
- [Restaurar una instantánea]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}})

## Crear una cuenta de correo electrónico en una base

Si desea enviar correos electrónicos desde una Base, necesita conectar su cuenta de correo electrónico a la Base. Le mostramos cómo hacer uso de esta útil función en SeaTable en el artículo [Configurar una cuenta de correo electrónico en una]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}) Base.
