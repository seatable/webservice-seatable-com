---
title: '¿Cuál es la diferencia entre acciones individuales y registros compartidos?'
date: 2023-03-21
lastmod: '2023-03-21'
categories:
    - 'haeufig-gestellte-fragen'
author: 'nsc2'
url: '/es/ayuda/diferencia-compartir-conjuntos-datos-comunes'
aliases:
    - '/es/ayuda/was-ist-der-unterschied-zwischen-individuellen-freigaben-und-gemeinsamen-datensaetzen'
seo:
    title: 'Compartir datos o conjuntos comunes en SeaTable: ¿qué elegir?'
    description: 'Descubra ventajas y diferencias entre compartir bases individualmente y utilizar conjuntos de datos comunes en SeaTable.'
---

En SeaTable, tiene a su disposición varios **recursos compartidos individuales**. Por ejemplo, tiene la opción de compartir bases, tablas y vistas individuales con usuarios individuales o grupos enteros.

Además, tiene la opción de crear **conjuntos de datos compartidos** que le permiten poner a disposición de otros grupos y usuarios una vista de tabla predefinida.

Pero, ¿cuál es la diferencia entre las dos funciones mencionadas y en qué contexto resulta más ventajosa una u otra?

## Opciones de liberación individual

Con una acción individual, concedes a otras personas **acceso a una base, tabla o vista**. Los usuarios autorizados ven el recurso compartido como una base independiente en la página de inicio. Dependiendo del tipo de recurso compartido, los demás usuarios sólo podrán ver o también editar tus datos.

Con las comparticiones individuales, todos los usuarios con los que se ha compartido la base, tabla o vista trabajan en **un mismo conjunto de datos**. Por ejemplo, los usuarios pueden añadir columnas a la tabla compartida o eliminar columnas existentes. Los **cambios** realizados se **sobrescriben** en el conjunto de datos compartido y, por tanto, también son **visibles para** todos los usuarios.

Por este motivo, las opciones de publicación individual resultan especialmente ventajosas cuando se trabaja en equipo con los mismos datos y se desean realizar cambios en el conjunto de datos compartidos.

{{< warning headline="Para más información" >}}

Si necesita más información sobre las opciones individuales de liberación, haga clic [aquí]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}).

{{< /warning >}}

## Conjuntos de datos comunes

Con la ayuda de **conjuntos de datos compartidos**, es posible poner una vista de tabla predefinida a disposición de otros grupos y usuarios, para que puedan acceder a datos específicos en una amplia gama de contextos y departamentos.

A diferencia de las comparticiones individuales, los registros compartidos representan una **tabla** maestra cuyo contenido se utiliza en otras tablas. Los miembros de tu equipo pueden adaptar en cualquier momento los **vástagos de** la tabla maestra para poder utilizar los datos del conjunto de datos compartidos en una amplia variedad de contextos.

Sin embargo, a diferencia de las versiones individuales, los **cambios** realizados por los usuarios **no** afectan al conjunto de datos subyacente. Las ramificaciones de la tabla maestra son independientes entre sí y tampoco pueden ser visualizadas por otros usuarios. Por este motivo, los conjuntos de datos compartidos resultan especialmente ventajosos cuando distintos departamentos y empleados de una empresa acceden a determinados conjuntos de datos en sus propios contextos.

Esto se ilustrará con el siguiente ejemplo:

- Una lista de personal relevante para varios grupos de usuarios (por ejemplo, RRHH, contabilidad y comunicación interna) puede ponerse a disposición de los miembros de su equipo a través de conjuntos de datos compartidos como **plantilla para nuevas tablas**.
- Después de que los miembros de su equipo hayan importado el conjunto de datos comunes a una base, pueden añadir columnas a la tabla como deseen y adaptarla a sus casos de uso específicos (por ejemplo, planificación de vacaciones, nóminas, lista de distribución para boletines internos).
- Las tablas que acceden a un conjunto de datos común pueden **sincronizarse** en cualquier momento, es decir, compararse con la última versión del conjunto de datos (por ejemplo, cuando se incorporan o abandonan nuevos empleados).
- Existe una relación descendente: los cambios en el conjunto de datos común se transfieren a las tablas dependientes durante la sincronización. Sin embargo, los cambios en estas tablas **no** afectan al conjunto de datos subyacente.

{{< warning headline="Para más información" >}}

[Aquí]({{< relref "help/startseite/gemeinsame-datensaetze/funktionsweise-von-gemeinsamen-datensaetzen" >}}) encontrará información más detallada y orientaciones concretas sobre el uso de conjuntos de datos compartidos.

{{< /warning >}}
