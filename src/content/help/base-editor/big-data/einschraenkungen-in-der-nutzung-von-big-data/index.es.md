---
title: 'Limitaciones en el uso de Big Data'
date: 2023-05-11
lastmod: '2024-12-16'
categories:
    - 'big-data'
author: 'nsc2'
url: '/es/ayuda/big-data-limitaciones-seatable'
aliases:
    - '/es/ayuda/einschraenkungen-in-der-nutzung-von-big-data'
seo:
    title: 'SeaTable Big Data: limitaciones y consejos útiles'
    description: 'Descubra las principales limitaciones de Big Data en SeaTable: sincronización, edición, permisos, acciones y buenas prácticas para un manejo de datos eficiente.'

---

Una vista normal en SeaTable permite trabajar **en colaboración** **en tiempo real** **hasta 100.000** filas. Big Data le permite **almacenar un número ilimitado** de filas, pero reduce su capacidad de colaboración. Antes de utilizar Big Data, asegúrese de echar un vistazo a este artículo de ayuda para averiguar qué limitaciones debe esperar al utilizar Big Data.

## Limitaciones de los macrodatos

El almacenamiento de big data le ofrece **un almacenamiento de filas** en gran medida **ilimitado**, pero también viene con ciertas limitaciones. A continuación encontrará un resumen de las **restricciones**:

- Los cambios realizados en una entrada de Big Data **no** **se sincronizan** en tiempo real en el navegador de otro usuario. Los cambios sólo son visibles para otros usuarios tras una **recarga** de la página.
- No **se pueden compartir** vistas de Big Data, ni individualmente ni con [autorizaciones de uso compartido definidas por el usuario]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}).
- **No se pueden** crear **nuevas filas** en una vista de big data. Esto debe hacerse siempre en una [vista normal]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) ninguna fila.
- En una vista de big data, no se puede [ajustar]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}).
- **No se pueden modificar** las entradas [enlazadas]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) en las entradas de big data. Los enlaces a filas de la memoria de big data **no se muestran** en las vistas normales, pero sí en una vista de big data.
- El formato condicional[(resaltar filas en color]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}).
- Las [operaciones de procesamiento de datos]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) **no** están disponibles para big data. La única excepción es [comparar y unir]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}}). Esta operación puede unir entradas de la memoria de big data con filas de cualquier otra tabla, independientemente de si las filas están almacenadas en la base o en la memoria de big data.
- La función [de buscar y reemplazar]({{< relref "help/base-editor/tabellen/suchen-und-ersetzen-von-werten-in-seatable" >}}) **no** está disponible.

{{< warning  headline="Muchas de estas limitaciones de Big Data no se aplican a la aplicación" >}}

La mayoría de los usuarios de almacenamiento de big data no sienten que su trabajo se vea afectado por estas restricciones. Sin embargo, si le afectan, puede echar un vistazo a la [aplicación]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). Algunas de las restricciones mencionadas no se aplican allí.

{{< /warning >}}
