---
title: 'Operaciones de tratamiento de datos en SeaTable'
date: 2023-03-20
lastmod: '2023-04-28'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/es/ayuda/operaciones-procesamiento-datos-seatable'
aliases:
    - '/es/ayuda/datenverarbeitungsoperationen-in-seatable'
seo:
    title: 'Procesamiento de datos en SeaTable: operaciones avanzadas'
    description: 'Gestione cálculos y relaciones entre tablas en SeaTable para analizar y centralizar datos con operaciones matemáticas y vinculación.'
star: true
weight: 1
---

La función de tratamiento de datos es una característica útil de SeaTable que le permite realizar **operaciones** en una columna a través de varias filas. Al definir una operación, puede realizar diversos **cálculos matemáticos** o establecer **relaciones entre valores** de distintas tablas. Las operaciones de procesamiento de datos son especialmente eficaces en grandes conjuntos de datos en los que puede realizar un gran número de cálculos.

## El sentido de las operaciones de tratamiento de datos

SeaTable suele pensar en filas. Por ejemplo, una [fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) sólo puede relacionar los valores de una fila entre sí y [los enlaces entre tablas]({{< relref "help/base-editor/tabellen/tabellen-miteinander-verlinken" >}}) sólo se hacen de fila a fila.

El tratamiento de datos, por el contrario, es una función para realizar operaciones en una columna a través de varias filas. Básicamente, se distingue entre dos tipos diferentes de operaciones de tratamiento de datos:

- **Cálculos matemáticos** en todos los valores de una columna. Ejemplo: Números de acceso a un sitio web.
- Relacionar **valores** si son idénticos en dos tablas. Ejemplo: Asignar pagos recibidos a una factura.

## Operaciones matemáticas y de relación

Actualmente pueden realizarse las siguientes **operaciones matemáticas** mediante la función de tratamiento de datos:

- [Calcular valores acumulados]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}})
- [Calcular la clasificación]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Calcular los cambios]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calcular el porcentaje]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})

Actualmente pueden realizarse las siguientes **operaciones de relación** mediante la función de tratamiento de datos:

- [Comparar y enlazar]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-verknuepfen" >}})
- [Comparar y copiar]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})
- [Transferir nombres de usuario]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})

## Requisitos previos para la definición de las operaciones

Cada uno de los dos tipos de operaciones de tratamiento de datos tiene **requisitos** diferentes que deben cumplirse para crear la operación correspondiente.

- Las **operaciones matemáticas** requieren la presencia de **dos columnas de números** en su tabla.
- Para las **operaciones de relación**, se necesitan tipos de columna muy específicos en función de la aplicación, por ejemplo, una [columna de personal]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) y una columna de [texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}) cuando se transfieren nombres de usuario.

## Notas sobre la ejecución

Actualmente, las operaciones de tratamiento de datos pueden realizarse [manualmente]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-ausfuehren" >}}) o [mediante automatización]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}).

Cada vez que se ejecuta la operación de tratamiento de datos, los **resultados** se escriben en la **columna de resultados** independientemente. Si no desea sobrescribir ningún dato, deberá [crear]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}) para los resultados.

A diferencia de las columnas de **fórmulas**, que controlan permanentemente las columnas implicadas, **las** columnas de resultados _no_ se actualizan. Los cambios en los valores de la columna de origen _no_ afectan a los valores de la columna de resultado sin [automatización]({{< relref "help/base-editor/automationen/beispiel-datenverarbeitungsoperation-per-automation-ausfuehren" >}}) o reejecución. Por lo tanto, también puede sobrescribir manualmente los valores calculados o relacionados.

## Protección contra cambios

Para evitar malentendidos, recomendamos **no** realizar **ningún cambio manual en** las columnas implicadas y [bloquearlas para su edición]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}) tras la ejecución por seguridad (requiere una suscripción Plus o Enterprise).

![Columnas de resultados de acciones de tratamiento de datos bloqueadas para tratamiento ](images/locked-score-columns.jpg)

Tenga en cuenta que los valores calculados o relacionados son una **instantánea en** el momento de la ejecución. Si no vuelve a ejecutar la operación, los resultados pueden estar desfasados si los valores de la columna de origen han cambiado entretanto.
