---
title: 'Paso 1: Importar la base'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/es/ayuda/paso1-importar-base-seatable'
aliases:
    - '/es/ayuda/schritt-1-import-der-base'
seo:
    title: 'Paso 1 Curso SeaTable 2: importa la base, conoce la estructura'
    description: 'Inicia el segundo curso: importa la base DTABLE, explora los campos y fórmulas, y comprende los elementos esenciales para tus procesos online.'
---

Antes de poder asignar un nuevo proceso de negocio en SeaTable, primero debe crear la estructura de tabla adecuada. Es la única forma de registrar los datos necesarios para el proceso de forma significativa y procesarlos posteriormente de forma eficaz. Aunque puede inspirarse en las numerosas plantillas, normalmente es necesario pensar el proceso en detalle y definir claramente los datos relevantes.

Como este curso trata de la gestión de servicios en línea, necesitamos dos tablas centrales:

- Una tabla para registrar la oferta de cursos
- Una tabla para los participantes

En el primer curso ya ha aprendido a crear una base con distintos tipos de columnas. Por lo tanto, nos saltaremos este paso y empezaremos directamente con una base preparada.

Descargue el siguiente archivo a su PC e impórtelo como una nueva base en la página de inicio de SeaTable:

<a href="/SeaTable-Course-Level-2.dtable" download>Curso SeaTable Nivel 2.dtable</a>

Aunque no tenga que crear usted mismo la base, es importante que se familiarice a fondo con la estructura. Se han utilizado nuevos tipos de columnas que quizá no conozca del curso anterior.

## Los componentes de la base

A primera vista, la base parece bastante clara. Sólo consta de:

- 2 tablas
- 18 columnas
- 3 vistas
- 1 Formulario web

Pero no te dejes engañar por su sencillez: Esta estructura es asombrosamente potente. A continuación explico por qué hemos diseñado la base de esta manera.

### Su programa de estudios de un vistazo

En la tabla `Courses` encontrará toda la información importante sobre sus ofertas. Cada fila representa un curso o servicio que usted ofrece. Las columnas individuales proporcionan información detallada, como

- Nombre del curso
- Fecha y lugar del curso
- Número de participantes inscritos
- Estado del curso (completo o plazas disponibles)

Esta visión de conjunto estructurada le permite realizar un seguimiento de sus cursos y del número de participantes en todo momento.

![Tabla «Courses» con datos de cursos, número de participantes y estado por curso](images/lvl2-table-courses.png)

{{< warning  headline="Las fechas están en el pasado"  text="Observará que todas las fechas de los cursos están en el pasado. La sencilla razón de ello es que no hemos querido actualizar este curso en línea con regularidad. Por favor, ignore este hecho para este curso online." />}}

### Todo lo que necesita saber sobre los participantes en su curso

En la tabla `Registrations` se registran todos los datos de las personas que se han inscrito en sus cursos. Cada línea representa a un participante y contiene la siguiente información:

- Nombre del participante
- Dirección de correo electrónico
- El curso en el que la persona se ha inscrito
- Estado del pago (si ya se ha efectuado el pago)

Este cuadro le ofrece en todo momento una visión clara del estado actual del registro y de la situación de los pagos.

![Tabla «Registrations» con nombres, correos y cursos reservados de los participantes](images/lvl2-table-registrations.png)

{{< warning  headline="Columnas ocultas"  text="Se han ocultado dos columnas para mayor claridad. Más adelante verá que, de todos modos, sólo necesitamos estas columnas para la combinación de correspondencia." />}}

## Otras particularidades

Algunas funciones de esta base sólo pueden entenderse a través de determinadas configuraciones. Lea atentamente las siguientes explicaciones para comprender mejor las secciones siguientes.

### Columnas de fórmulas

En la tabla `Courses` encontrará dos importantes columnas de fórmulas, cuyas ventajas me gustaría explicarle:

- `{{< seatable-icon icon="dtable-icon-formula" >}} Title and Date`
- `{{< seatable-icon icon="dtable-icon-formula" >}} Status`

`{{< seatable-icon icon="dtable-icon-formula" >}} Title and Date` es una columna auxiliar que une los valores de las columnas "Título" y "Fecha". La fórmula utilizada es muy sencilla y sólo combina el título y la fecha del curso.

![Columna de fórmula «Title and Date» que combina título de curso y fecha en un solo campo](images/lvl2-formula-title-date.png)

A primera vista, esta columna parece superflua, ya que sólo combina los datos existentes. Pero créame: cuando analicemos el formulario de registro dentro de un momento, entenderá por qué esta columna es extremadamente útil.

---

La columna de fórmulas `{{< seatable-icon icon="dtable-icon-formula" >}} Status` determina automáticamente si aún quedan plazas disponibles en un curso o si el curso ya está completo. La lógica detrás de esto es relativamente simple, pero también podría tener en cuenta la fecha del evento cuando se utiliza de manera productiva.

![Columna de fórmula «Status» que calcula plazas libres o completo para cada curso](images/lvl2-formula-status.png)

{{< warning  headline="Las ventajas de las columnas de fórmulas"  text="Las columnas de fórmulas desempeñan un papel central en el desarrollo de bases potentes en SeaTable. Se utilizan para vincular información o definir determinados estados. El beneficio completo de estas columnas a menudo sólo se hace evidente cuando se trabaja con otras funciones." />}}

### Vista para seleccionar los cursos disponibles

En la tabla `Courses` existe una vista especial denominada `{{< seatable-icon icon="dtable-icon-main-view" >}} Available Courses`. Esta vista filtra la columna de fórmulas `{{< seatable-icon icon="dtable-icon-formula" >}} Status` y sólo muestra los cursos para los que aún quedan plazas disponibles. Los cursos que están completos se ocultan automáticamente.

Esta vista está bloqueada para que no se pueda editar {{< seatable-icon icon="dtable-icon-unlock" >}}para garantizar que no se modifica. Desempeña un papel importante, ya que determina las opciones de selección en la columna de enlaces. `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Registered for` limitado.

Si nos fijamos más detenidamente en el formulario de registro, queda claro por qué este punto de vista es tan útil.

![Configuración de la columna de enlace «Registered for» limitada a la vista «Available Courses»](images/lvl2-link-column-limit-to-view.png)

### Marcado por colores de filas y columnas

SeaTable ofrece la posibilidad de resaltar en color filas, columnas y celdas. Dos de estos efectos ya están integrados en esta plantilla:

- Las filas de los cursos se resaltan según su estado: Los cursos con plazas libres se resaltan en verde, mientras que los cursos con plazas completas se marcan en rojo.
- Los precios de los cursos se clasifican por colores en función del importe: Cuanto más caro es el precio, más oscuro es el color.

## Familiarícese con la base

Tómese el tiempo suficiente para explorar la base en detalle. Si aún no está familiarizado con determinadas funciones, no dude en leer los artículos de ayuda enlazados.

## Artículo de ayuda con más información

- [Creación de una base a partir de un archivo DTABLE]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei" >}})
- [Fórmulas básicas de SeaTable]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})
- [Codificación por colores de las líneas]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Vistas de la cerradura]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
