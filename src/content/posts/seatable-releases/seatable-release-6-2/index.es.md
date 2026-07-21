---
title: 'SeaTable 6.2: El código se une al no-code'
description: 'SeaTable 6.2 introduce un tipo de página HTML sumamente flexible y otras mejoras en el App Builder. Además, hay nuevas funciones en las columnas de fórmula y los enlaces externos.'
date: 2026-07-13
author: 'rdb'
url: '/es/seatable-release-6-2'
color: '#dc6165'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 6.2: El código se une al no-code'
    description: 'SeaTable 6.2: nuevo tipo de página HTML y otras mejoras en el App Builder, así como nuevas funciones en las columnas de fórmula y los enlaces externos.'
register:
    show: true
---

Con SeaTable 6.2, el [App Builder]({{< relref "help/app-builder" >}}) incorpora un nuevo tipo de página: las **páginas HTML** permiten crear páginas totalmente personalizadas basadas en HTML, JavaScript y CSS. Con ello desaparecen prácticamente todas las limitaciones en materia de visualización de datos. También los formularios web pueden diseñarse exactamente según sus necesidades, e incluso las interacciones complejas se pueden implementar sin problemas. ¡Lo imposible ya no existe!

Por lo demás, el App Builder también es protagonista en la versión 6.2. El tipo de página [Registro único]({{< relref "help/app-builder/seitentypen-in-universellen-apps/seiten-vom-typ-einzelner-datensatz-in-universellen-apps" >}}) recibe de una sola vez una triple mejora: ahora todos los valores de columna se pueden mostrar de forma uniforme como texto, formatear de manera universal y –un deseo expresado con frecuencia– editar directamente «en línea» en la página.

Otros [tipos de página]({{< relref "help/app-builder/seitentypen-in-universellen-apps" >}}) se benefician de una gestión de permisos ampliada para las columnas de enlace. Además, pequeños ajustes de diseño aportan mayor claridad: las aplicaciones sin páginas se marcan como tales para evitar malentendidos, y el avatar, junto con las notificaciones de la aplicación, ha encontrado una nueva ubicación.

Las [columnas de fórmula]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) reciben con SeaTable 6.2 dos nuevas capacidades a la vez: la nueva función **datetimeFormat()** convierte los valores de fecha en cadenas de texto con un formato de libre definición. Si su formato de fecha preferido no lo ofrecía SeaTable hasta ahora, eso pasa a ser cosa del pasado. Además, las fórmulas de texto admiten ahora **saltos de línea**, con lo que resulta mucho más flexible componer textos a partir de distintas columnas.

Por último, SeaTable 6.2 mejora la colaboración: los [enlaces externos]({{< relref "help/startseite/freigaben/externer-link-erklaert" >}}) y los [enlaces de invitación]({{< relref "help/startseite/freigaben/einladungs-link-erklaert" >}}) ahora pueden acompañarse de una descripción, de modo que el propósito y los destinatarios previstos se puedan anotar directamente en el enlace. Además, se ha rediseñado y hecho más claro el menú de cinta para las bases y vistas que se abren a través de enlaces externos.

El [changelog](https://cloud.seatable.io/dtable/view-external-links/c9124bcd934b47bc8f30/) registra –como siempre– todos los cambios relevantes.

Para [SeaTable Server]({{< relref "pages/product/seatable-server" >}}), la versión 6.2 está disponible para su descarga a partir de hoy en el [repositorio Docker de SeaTable](https://hub.docker.com/r/seatable/seatable-enterprise).

La actualización de [SeaTable Cloud]({{< relref "pages/product/seatable-cloud" >}}) se realizará **el 4 de agosto**. Con la actualización, el cupo mensual para la [ejecución de scripts de Python]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}) se vuelve dinámico. Al igual que ocurre con las llamadas a la API o las automatizaciones, el cupo total de scripts de Python queda vinculado al tamaño de un equipo. Un equipo Plus recibe 250 ejecuciones de scripts de Python, y un equipo Enterprise 1000 ejecuciones de Python por usuario y mes. En la suscripción Free se sigue aplicando un límite fijo de 100 ejecuciones al mes.

{{< warning headline="Breaking Changes en los scripts de Python" >}}

Los valores de retorno del objeto de contexto y del método de consulta para los tipos de columna Fecha, Fórmula y Fórmula para enlaces se armonizan en la versión 6.2. Esto puede provocar que la ejecución de sus scripts genere errores. Por favor, revise y actualice sus scripts de Python.

{{< /warning >}}

## Nuevo tipo de página de aplicación: la página HTML

Con el **App Builder de SeaTable** se pueden crear aplicaciones potentes, sin necesidad de programar. Gracias a los tipos de página predefinidos, en poco tiempo surge una aplicación web plenamente funcional. Sin embargo, esta eficiencia tiene su precio: si bien los **10 tipos de página** ofrecen numerosas posibilidades de configuración, predeterminan la estructura y el comportamiento de una página. Las personalizaciones individuales que fueran más allá no eran posibles hasta ahora.

¿Desea utilizar un tipo de gráfico que SeaTable no admite? ¿Crear un formulario web sumamente personalizado? ¿Incrustar un diagrama interactivo con elementos en los que se pueda hacer clic? ¿O combinar varias representaciones –por ejemplo, una tabla y un registro único– en una misma página? Con el nuevo tipo de página **página HTML** se pueden hacer realidad estos y muchos otros requisitos.

![Nuevo tipo de página de aplicación: la página HTML](HTMLPage.png)

Las páginas HTML pueden mostrar **contenidos estáticos**, pero despliegan todo su potencial en combinación con los **datos de una base**. Igual que otros tipos de página del App Builder, pueden recuperar datos de una base y modificar registros en una base. En cambio, en el **diseño de la interfaz de usuario** dispone de una libertad casi total. Lo que se puede realizar con HTML, CSS y JavaScript se puede llevar a cabo, en principio, también como página HTML en el App Builder.

No hay que dejarse confundir por el nombre. Las páginas HTML no solo admiten **HTML**, sino también **JavaScript y CSS**. Todo el código de la página se sube a la aplicación como un paquete (bundle). El funcionamiento, los posibles enfoques de desarrollo y la referencia del correspondiente Software Development Kit (SDK) los encontrará en el [Manual del desarrollador de SeaTable](https://developer.seatable.com/html-pages/ 'SeaTable Developer Manual'). También encontrará allí un ejemplo de página.

Actualmente, este tipo de página se dirige en especial a **usuarios con experiencia en programación**. Ya está en desarrollo una función de IA con la que en el futuro se podrán crear páginas HTML también en lenguaje natural y sin conocimientos de programación.

## Tipo de página de aplicación mejorado: Registro único

El tipo de página **Registro único** recibe en SeaTable 6.2 varias mejoras a la vez. Hasta ahora solo podía editar registros a través de los detalles de la fila, que primero tenía que abrir con el botón «Editar entrada». Esto suponía clics adicionales y una interrupción innecesaria de la experiencia de usuario en el flujo de edición.

Con SeaTable 6.2, este paso intermedio queda atrás. Si un usuario dispone de los permisos de edición necesarios, ahora los campos se pueden editar directamente en la página. **Un clic sobre un campo activa el modo de edición**, las entradas se validan como de costumbre y los cambios se guardan de inmediato. Esto proporciona un flujo de trabajo notablemente más fluido e intuitivo.

![Edición en línea en las páginas de registro único](SingleRecordPage_InlineEditing.png)

También se ha ampliado la presentación. Los **tipos de columna** con una representación visual propia –por ejemplo, las etiquetas de las columnas de [selección única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) o de [colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}})– ahora se pueden mostrar opcionalmente como texto sin formato. Además, para todos los valores mostrados como texto se dispone de un conjunto uniforme de **opciones de formato**: el tamaño de fuente, el color de fuente, la alineación y el fondo se pueden ajustar de forma coherente, con independencia del tipo de columna original. Así podrá diseñar páginas con un aspecto uniforme y ordenado.

## Permisos ampliados para los enlaces en la aplicación

SeaTable 6.2 cierra una brecha en la gestión de permisos de las [columnas de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) en el App Builder. Con el nuevo permiso **Eliminar entradas existentes** se puede definir de forma específica si los usuarios pueden borrar enlaces existentes.

Hasta ahora, cualquier usuario con permiso de edición podía eliminar enlaces existentes. Este comportamiento se puede controlar ahora para la columna de enlace con independencia de los demás [permisos de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}).

![Nuevo permiso en la aplicación: eliminar enlaces existentes](AppBuilder_RemoveExistingRecords.png)

Ahora puede gestionar de forma integral los derechos de acceso para las columnas de enlace: según la configuración, los usuarios pueden crear nuevos registros en la tabla enlazada, así como enlazar, modificar y eliminar registros existentes, cada uno con sus propios permisos. Esto permite un **control notablemente más preciso de los derechos de edición en las aplicaciones**.

## Nueva función en la columna de fórmula

La nueva función **datetimeFormat()** le ayuda a mostrar los valores de fecha exactamente como los necesita. El primer parámetro contiene la fecha que se debe formatear o la referencia a la columna que contiene el valor. En el segundo parámetro define el formato de destino.

![Fórmula para valores de fecha con formato](FormulaColumn_datetimeFormat.png)

En las fórmulas de texto ya puede insertar un **salto de línea** con «\n» o '\n'. Esto resulta especialmente útil cuando concatena varias columnas pero no desea escribir los valores en una sola línea. El ejemplo por excelencia es una dirección:

![Saltos de línea en fórmulas de texto](FormulaColumn_LineBreak.png)

## Mejoras en los enlaces externos y los enlaces de invitación

Por último, SeaTable 6.2 depara una optimización para los **enlaces externos y los enlaces de invitación**. Ahora puede acompañarlos de una **descripción**. Así, por ejemplo, el propósito y los destinatarios previstos se pueden anotar directamente en el enlace. Además, hemos rediseñado y hecho más claro el menú de cinta para las bases y vistas que se abren a través de enlaces externos.

## Y bastante más

- **Registro de la base mejorado**:​ El [registro de la base]({{< relref "help/base-editor/historie-und-versionen/aenderungen-ueber-die-logs-rueckgaengig-machen" >}}) se ha rediseñado en varios puntos. Los campos de búsqueda facilitan la selección en bases grandes, los menús desplegables se presentan con un diseño uniforme y ahora también puede filtrar las acciones en tablas eliminadas.

- **Widget de fecha mejorado​**: El widget de fecha se ha optimizado en cuanto a manejo y presentación y ofrece un trabajo aún más cómodo con los [valores de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}).

- **Emojis en los comentarios​**: Los [comentarios]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) ahora admiten emojis. Esto hace que los comentarios, las reacciones y la colaboración sean aún más expresivos.

## Adaptación de los valores de retorno en los scripts de Python

Con el objetivo de armonizar los formatos, en SeaTable 6.2 se actualizan los valores de retorno de algunos tipos de columna para el objeto de contexto y el método de consulta. Esto puede requerir la adaptación de sus scripts de Python.

Encontrará una comparación de los valores de retorno en SeaTable 6.1 y SeaTable 6.2 en el [Foro de SeaTable](https://forum.seatable.com/t/important-changes-related-to-python-client-in-seatable-6-2/7435).

Para los scripts ejecutados manualmente, es decir, los scripts que ejecuta mediante un botón o en el editor de Python de SeaTable, debe tener en cuenta todos los cambios allí mencionados. Los scripts que se ejecutan mediante automatización solo debe adaptarlos en lo relativo a los cambios relacionados con el método de consulta.
