---
title: 'Las columnas Último modificador y Última modificación'
date: 2023-01-20
lastmod: '2023-08-04'
categories:
    - 'datum-dauer-und-personen'
author: 'nsc2'
url: '/es/ayuda/ultimo-editor-fecha-edicion-seatable'
aliases:
    - '/es/ayuda/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum'
seo:
    title: 'Último editor y fecha de edición en SeaTable'
    description: 'Las columnas de “último editor” y “fecha edición” de SeaTable muestran siempre quién modificó cada fila y cuándo, para máxima trazabilidad y orden.'
weight: 23
---

Las columnas **Último modificador** y **Última modificación** sólo son rellenadas **automáticamente** por SeaTable y por lo tanto son tipos de columnas especiales. Son muy útiles si desea saber **cuándo** y **quién editó por última vez** una entrada.

Como las dos columnas registran automáticamente los cambios en las entradas, son muy adecuadas como desencadenantes de [automatizaciones]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) y [ordenaciones]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}), por ejemplo.

## Las columnas Último modificador y Última modificación

Mientras SeaTable rellena la columna **Último modificador** con el nombre del usuario que editó por última vez una fila, la fecha y hora exacta en la que tuvo lugar la última edición se registra en la columna **Última modificación**.

![Las columnas "Último modificador" y "Última modificación" después de la creación por un usuario](images/last-modifiere-and-last-modified-time.png)

## Características especiales de los dos tipos de columnas

- **No es posible** modificar manualmente los valores introducidos automáticamente en las columnas Último modificador y Última modificación. Los valores se actualizan automáticamente en cuanto se realiza un cambio en una fila.
- Al **crear** los dos tipos de columna, **no** hay más opciones disponibles que el nombre de la columna.
- Sólo se puede crear **una** columna de cada tipo por tabla. Si intenta crear otra columna del mismo tipo, aparecerá el mensaje "Otra columna tiene este tipo de columna".

![Mensaje de error para la columna Último modificador](images/Fehlermeldung-bei-weiterer-Letzter-Bearbeiter-Spalte.png)

- Por este motivo, **no puede duplicar** las columnas Último modificador y Última modificación **ni personalizar su tipo de columna**.
