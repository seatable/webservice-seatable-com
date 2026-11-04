---
title: 'Navegación en la interfaz de usuario de SeaTable'
date: 2024-08-30
lastmod: '2024-09-05'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/es/ayuda/navegar-interfaz-seatable'
aliases:
    - '/es/ayuda/navigieren-in-der-benutzeroberflaeche-von-seatable'
seo:
    title: 'Cómo navegar la interfaz de usuario de SeaTable'
    description: 'Descubre la interfaz de SeaTable: inicio, bases, tablas y vistas. Aprende dónde encontrar cada función y navega cada área fácilmente siguiendo los pasos.'

weight: 3
---

Empecemos por cómo orientarse en SeaTable. SeaTable es una solución web que puede utilizar fácilmente con su navegador. Repasaremos brevemente los diferentes elementos de la interfaz y le mostraremos qué significa cada icono y dónde encontrar lo que necesita al crear sus bases.

Abra su navegador, llame a la página de inicio de sesión de SeaTable e inicie sesión con sus datos de acceso. La página de inicio debería tener este aspecto:

{{< zoom image="images/elements_seatable_homepage.png" alt="Elementos de la página de inicio de SeaTable" >}}

## La página de inicio

La página de inicio está dividida en dos áreas: La navegación (izquierda) y el resumen de bases (derecha). Es probable que aún no vea ninguna base o sólo unas pocas. Sin embargo, esto cambiará en breve. Una base siempre está representada por una ficha de color y su nombre a la derecha.

### ¿Qué es exactamente una base?

Una base es una base de datos. Una base consta de una o varias tablas y puede contener muchos miles de líneas. Todas las bases a las que un usuario tiene acceso se muestran en la página de inicio. SeaTable distingue entre diferentes espacios de trabajo dependiendo de quién creó la base o quién tiene acceso a ella. Las palabras clave correspondientes están aquí:

- **Mis bases**: Tú mismo has creado bases en esta área y mientras no compartas explícitamente la base con alguien o con un grupo, sólo tú tienes acceso a ella.
- **Favoritos**: Puedes marcar cualquier base como favorita para encontrarla siempre en esta zona.
- **Grupos**: SeaTable se nutre de la colaboración. Puede utilizar los grupos para que un grupo de personas pueda acceder a una base.

## El editor base

Ahora abre una de tus bases haciendo clic con el ratón sobre una de ellas. Si todavía no tienes una base, simplemente crea una. El nombre de tu base no importa por ahora.

Al principio sólo verás tres celdas vacías en tu base, así que no te confundas cuando te expliquemos los distintos elementos utilizando una base de ejemplo rellena.

{{< zoom image="images/elements_seatable_base.png" alt="Elementos de la base SeaTable" >}}

Uf, la primera visión de una base puede ser bastante aterradora. Hay tantos botones y opciones de interacción esperando a ser utilizados. Veamos en detalle los distintos elementos.

### Tablas

En el área de cabecera de cada base, las tablas de su base se muestran unas junto a otras en forma de pestañas. Las tablas en SeaTable son comparables a las hojas de cálculo en Excel o a las tablas en una base de datos. Dependiendo de si ya conoce una u otra. Puede crear columnas en cada tabla para registrar y guardar la información deseada. Mientras que todas las columnas son iguales en Excel, en SeaTable tiene que seleccionar un tipo de columna al crear cada una. Esto le permite especificar qué información desea guardar en esta columna. Suena complicado, pero no lo es:

- Sólo se pueden guardar números en una columna numérica, pero no imágenes
- Sólo puede guardar valores de fecha en una columna de fecha, pero no números.
- En un ... - Creo que has entendido el principio.

### Líneas

La información se almacena en las filas de una tabla. Cada fila representa un registro de datos. Por ejemplo, si crea una tabla `Expenses` con 50 líneas, entonces ha introducido una salida en cada una de las 50 líneas.

### Vistas

Una vista es una representación definida por el usuario de las filas de una tabla. Cada vista se define por la ordenación, los filtros, la agrupación, la ocultación de columnas y otros ajustes de vista utilizados.

Una tabla puede contener una o varias vistas. Todas las vistas de una tabla acceden al mismo conjunto de datos. Esto significa que si se modifica el valor de una celda en una vista, el valor se modifica en la tabla subyacente y, por tanto, también en todas las vistas de la tabla.

En este curso online examinaremos el concepto de vistas con más detalle y lo ilustraremos con casos de uso concretos.

## Resumen

En esta lección ha aprendido sobre varios elementos de la interfaz de SeaTable. No se deje intimidar por las múltiples posibilidades de la interfaz de usuario. En la siguiente parte de este curso online, empezaremos a construir su propio **sistema de gestión de gastos**, que le permitirá utilizar y familiarizarse con muchas de las funciones de SeaTable.

Si desea familiarizarse más intensamente con la interfaz de usuario y los términos de SeaTable, le recomendamos nuestro [glosario]({{< relref "help/erste-schritte/einfuehrung-grundlagen/glossar-der-von-seatable-verwendeten-begriffe" >}}). En él se explica detalladamente la interfaz de usuario y la terminología de SeaTable.

## Artículo de ayuda con más información

En los siguientes artículos, incluiremos siempre una sección al final de la página con enlaces a nuestra sección de ayuda. De esta forma, le guiaremos a través de este curso en línea, pero sin visualizar cada clic del ratón con una captura de pantalla. Si te quedas atascado, los artículos de ayuda deberían ayudarte.

- [Crear una nueva base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [¿Qué es una vista?]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}})
- [Glosario]({{< relref "help/erste-schritte/einfuehrung-grundlagen/glossar-der-von-seatable-verwendeten-begriffe" >}})
- [Añade una base a tus favoritos]({{< relref "help/startseite/bases/eine-base-zu-den-favoriten-hinzufuegen" >}})
