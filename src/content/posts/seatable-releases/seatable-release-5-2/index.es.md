---
title: 'SeaTable 5.2: filtros avanzados en la base y un nuevo plugin'
date: 2025-02-25
lastmod: '2025-02-25'
author: 'rdb'
url: '/es/seatable-release-5-2'
categories:
    - 'product-features'
color: '#9dcde3'
seo:
    title: 'SeaTable 5.2: novedades de filtros, plugin Whiteboard y mejoras App Builder'
    description: 'SeaTable 5.2: ¡Grupos de filtros (Y/O), formato intercolumnar, plugin Pizarra, mejoras en App Builder y novedades API en un vistazo!'
---

La segunda versión menor de la versión 5 de SeaTable contiene numerosas correcciones de errores y mejoras de detalle para que trabajar con SeaTable sea aún más fácil y para que sus casos de uso sean aún más compatibles: En Bases, los **nuevos grupos de filtros** permiten una selección mucho más precisa de los datos (registros). Los filtros de columnas cruzadas en el formato condicional de filas y celdas permiten resaltar los datos de una forma que antes no era posible. En el **App Builder**, cada tipo de página se beneficia de mejoras mayores y menores de diversa índole: autorizaciones ampliadas, mejor usabilidad y más funciones. SeaTable 5.2 también incluye un nuevo **plugin de pizarra** y mejoras en los plugins de diseño de página y calendario. Como siempre, puede encontrar la lista completa de cambios en el [registro de cambios]({{< relref "pages/changelog" >}}/).

Esta mañana a las 6am hora central europea, SeaTable Cloud fue actualizado a la versión 5.2 y el nuevo plugin fue puesto a disposición. Esperamos sus comentarios. Los administradores del servidor SeaTable pueden descargar la imagen Docker de SeaTable 5.2 desde el conocido [repositorioDocker](https://hub.docker.com/r/seatable/seatable-enterprise) .

## Reglas de filtrado complejas con grupos de filtros

La versión 5.2 hace aún más potentes las [funciones de filtro]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) de SeaTable. Los nuevos grupos de filtros permiten **combinar reglas de filtrado con los operadores lógicos Y y O**. Ejemplo: Buscar hombres nacidos después de 1979 (grupo de filtrado 1) o mujeres nacidas después de 1984 (grupo de filtrado 2). Este tipo de filtrado no era posible anteriormente en SeaTable. En versiones anteriores, todas las reglas de filtrado se vinculaban con los operadores lógicos Y u O.

![Grupos de filtros con condiciones combinadas AND/OR para selecciones de datos complejas](Fitlergroups.png)

En futuras versiones, también introduciremos grupos de filtros en aplicaciones, formularios y automatizaciones.

## Formato condicional con filtro de columnas cruzadas

La versión 5.2 también ofrece opciones de filtro ampliadas en el [formato]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}) condicional de [filas]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}) y [celdas]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}). ¿Desea colorear de rojo una celda en función de los valores de otras columnas para llamar la atención sobre ella? Con SeaTable 5.2 puede hacerlo. El código de colores de una fila o celda puede formatearse ahora en función del valor de cada columna individual de un conjunto de datos. Y eso no es todo: el formato condicional también puede tener en cuenta los valores de varias columnas, independientemente del tipo de columna.

![Formato condicional de filas y celdas entre columnas según varios valores de columna](ConditionalFormatting.png)

## Mejoras funcionales en el App Builder

El tipo de página de [registro único de datos]({{< relref "help/app-builder/seitentypen-in-universellen-apps/seiten-vom-typ-einzelner-datensatz-in-universellen-apps" >}}) se beneficia de varias mejoras, pero las páginas de formularios, tablas y cuadros de mando también reciben nuevas funciones y elementos. Hemos ampliado el control de autorización para los tipos de página de cronología, calendario y consulta, y hemos mejorado la gestión de versiones y la función de código QR en los ajustes de la aplicación.

### Tipo de página Registro de datos individual

A partir de SeaTable 5.2, la configuración de página para este tipo de página incluye la función **Predeterminar columnas de sólo lectura**, que ya es familiar de otros tipos de página. En combinación con la [autorización de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) "¿Quién puede editar filas?", el administrador de la aplicación puede definir con precisión qué valores de columna de un registro de datos pueden ser introducidos o modificados por los usuarios y cuáles no.

![Tipo de página «Registro único» con ajuste para columnas predefinidas como solo lectura](ROcolumns-SingleRecordPage.png)

En el caso de los [registros de datos bloqueados]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}), ahora el usuario también recibe un aviso de que no es posible editarlos. Aparecerá el mensaje correspondiente al situar el puntero del ratón sobre "Editar entrada" en la barra de herramientas.

Además del control de autorizaciones, la nueva versión contiene dos mejoras para aumentar la facilidad de uso: ahora se puede hacer clic en los campos de tipo [URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}}) y [correo electrónico]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}). De este modo, se puede acceder más rápidamente a un sitio web o escribir un correo electrónico. (A partir de la versión 5.3, también se puede hacer clic en los archivos de las columnas de archivos). Hay tres modos disponibles: Personalizar, Rellenar y Estirar.

### Tipo de página Formulario

Los [formularios web]({{< relref "help/base-editor/webformulare" >}}) sencillos que pueden crearse en Base ofrecen una **opción de redirección**. Los usuarios son redirigidos automáticamente a un sitio web tras el envío. Ahora también hemos añadido esta función a las [páginas de formularios]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}), teniendo en cuenta las características especiales de la app. Los usuarios pueden ser redirigidos a otra página de la aplicación o a una URL externa. Las otras páginas de la aplicación pueden seleccionarse cómodamente en un menú desplegable. También se puede establecer si la redirección tiene lugar en una nueva pestaña o en la misma pestaña.

### Tipo de página Tabla

Los **filtros preestablecidos** de la configuración de datos permiten ahora seleccionar todos los tipos de columnas pertinentes, incluidas [las columnas de]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) [fórmulas]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) y [enlaces]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}). Esto elimina una importante restricción funcional en el prefiltrado de datos. Con la implementación de grupos de filtros en una de las próximas versiones, este tipo de página ofrecerá las mismas potentes opciones de filtro que la base.

### Páginas personalizadas

La [página individual]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}) ha recibido un nuevo tipo de estadística: similar a la [página de tabla]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}), la **tabla simple** permite la visualización tabular de un conjunto de datos que han sido prefiltrados y preclasificados por el administrador de la aplicación. A diferencia de la página de tabla, el nuevo tipo de estadística permite combinar dos o más tablas en una página. En la versión 5.2, los usuarios de la aplicación no pueden establecer sus propias reglas de filtrado y ordenación. Añadiremos esta función en el futuro.

![Tipo de estadística «Tabla básica» que muestra registros prefiltrados en una página personalizada](BasicTable.png)

### Tipo de página Calendario

SeaTable 5.2 proporciona una función urgentemente necesaria para la [página de calendario]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kalenderseiten-in-universellen-apps" >}}): **Añadir nuevas entradas** directamente a las páginas de este tipo. Para ello, hemos añadido la autorización de página "¿Quién puede añadir filas?" en la configuración de la página, que es familiar de otros tipos de página. Junto con la autorización existente "¿Quién puede editar filas?", el administrador de la aplicación puede definir exactamente qué usuarios pueden modificar las entradas existentes y crear otras nuevas. Para las páginas de aplicación existentes de tipo calendario, la nueva autorización se establece en "Nadie".

### Tipo de página Línea de tiempo

Este tipo de página también se beneficia de una ampliación de las autorizaciones de página. Gracias a la nueva autorización "¿Quién puede editar filas?", ahora también es posible **realizar cambios directos en los registros de datos existentes** en las [páginas de línea de tiempo]({{< relref "help/app-builder/seitentypen-in-universellen-apps/zeitstrahlseiten-in-universellen-apps" >}}). Si arrastra el ratón al principio o al final de una barra, el valor de la fecha cambia automáticamente, lo que amplía o acorta el evento. En las aplicaciones existentes, la nueva autorización se asigna a "Nadie".

### Consulta de tipo de página

Anteriormente, la interacción con los datos mostrados en las [páginas de consulta]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}) sólo era posible mediante botones. Como éstos sólo podían realizar acciones predefinidas, no era posible realizar cambios individuales. Esto cambia ahora con la opción **Hacer editable el resultado de la consulta**. Si está activada, los valores de los registros de datos contenidos en la consulta pueden editarse a través de los detalles de la fila. Sin embargo, la opción no tiene ningún efecto en las aplicaciones públicas a las que se accede sin necesidad de iniciar sesión.

## Nuevo plugin de pizarra

"Nuevo" plugin de pizarra - ¿no ha existido el plugin de pizarra desde [SeaTable 5.0]({{< relref "posts/seatable-releases/seatable-release-5-0" >}})? Eso es correcto, pero la afirmación "nuevo plugin de pizarra blanca" también es correcta. El nuevo plugin de **pizarra blanca (tldraw)** no tiene nada que envidiar al plugin anterior en cuanto a opciones de diseño, pero también ofrece un **soporte óptimo para la colaboración en línea**. Puedes trabajar solo, en parejas o en equipo en la pizarra - todos los cambios se actualizan en tiempo real y son inmediatamente visibles para todos los demás usuarios.

Puedes instalar el nuevo plugin de pizarra además o como alternativa al plugin de pizarra existente y utilizarlo en Bases. Las pizarras existentes no se migran automáticamente, pero el contenido puede transferirse con poco esfuerzo mediante copiar y pegar. Recomendamos cambiar a la nueva pizarra lo antes posible. El nuevo plugin utiliza un componente de servidor separado que es proporcionado por el [proyecto](https://tldraw.dev/) homónimo [tldraw](https://tldraw.dev/). Los autoalojadores deben instalar este componente. Las instrucciones se encuentran en el [manual del administrador](http://admin.seatable.com/installation/components/whiteboard/).

La sustitución del plugin se había hecho necesaria porque el "antiguo" plugin de pizarra, que se basa en el proyecto de código abierto [excalidraw](https://github.com/excalidraw/excalidraw), resultó ser propenso a fallos de funcionamiento cuando era utilizado por varios usuarios al mismo tiempo. Con la versión 6.0 en verano de 2025, eliminaremos el antiguo plugin de SeaTable Cloud. Todas las pizarras del antiguo plugin dejarán de estar disponibles.

![Plugin de pizarra «Whiteboard (tldraw)» con edición colaborativa en tiempo real por varios usuarios](tldraw-collaboration.png)

## Cambios importantes en la API de SeaTable

Con el lanzamiento de la versión 5.2, nos gustaría anunciar un cambio importante en la API de SeaTable. Esto sólo afecta a los usuarios que utilizan la API para implementar sus propias aplicaciones y flujos de trabajo. Estos cambios no tienen ningún impacto en el uso de la interfaz web.

Encontrará información detallada sobre los cambios en este [mensaje del foro](https://forum.seatable.com/t/important-changes-to-api-and-seatable-cloud-with-version-5-2/6317). He aquí un resumen de los puntos más importantes:

- Para armonizar la estructura de la API, algunos puntos finales se han marcado como obsoletos. Los nuevos puntos finales ya están disponibles.
- La versión 6.0 desactiva los puntos finales obsoletos.
- Ya hemos convertido nuestras integraciones para [n8n](https://n8n.io/integrations/seatable/) y [Zapier](https://zapier.com/apps/seatable/integrations) a los nuevos puntos finales. La [aplicación Make](https://www.make.com/en/integrations/seatable) lo hará en breve.

Si utiliza scripts o integraciones personalizadas, compruebe si está utilizando los endpoints antiguos. Si es así, deberá adaptarlos para la versión 6.0 de SeaTable como muy tarde.

## Y mucho más

SeaTable 5.2 tiene otras novedades que merecen algo más que una mención explícita:

La capacidad de **gestionar datos jerárquicos en una tabla** alcanza un nuevo nivel en SeaTable 5.2: las relaciones padre e hijo se registran y muestran en columnas separadas. SeaTable garantiza que cada relación padre tenga también una relación hijo. Esto facilita el análisis de las relaciones en ambas direcciones. La ilustración muestra la diferencia entre SeaTable 5.2 (izquierda) y SeaTable 5.1 (derecha) para la alta dirección de una organización ficticia.

![Comparación de enlaces internos en SeaTable 5.2 y 5.1 con columnas separadas de padre e hijo](InternalLinking-SeaTable-5.2-vs.-SeaTable-5.1.png)

Para los usuarios, esto sólo aporta ventajas sin complejidad adicional. Si un usuario crea una nueva **columna de** enlace que vincule entradas de una misma tabla, SeaTable crea automáticamente la segunda columna de enlace. Los plugins de [organigrama]({{< relref "help/base-editor/plugins/anleitung-zum-organigramm-plugin" >}}) y [árbol]({{< relref "help/base-editor/plugins/anleitung-zum-tree-plugin" >}}) también pueden manejar la estructura de datos mejorada.

Los enlaces existentes dentro de una tabla no se ajustan. Si desea cambiar, cree una nueva columna de enlace e inserte los enlaces. A continuación, puede eliminar la antigua columna de enlaces.

La nueva versión de SeaTable admite el **inicio de sesión con cuentas de correo electrónico de Google y Microsoft mediante OAuth**. (Microsoft denomina a esto "autenticación moderna".) El uso de cuentas de correo electrónico de Microsoft en particular solo era posible anteriormente con grandes restricciones después de que Microsoft suspendiera la autenticación mediante nombre de usuario y contraseña. En el manual de usuario encontrará instrucciones detalladas sobre cómo [integrar]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}) una cuenta de Gmail, Outlook.com o MS 365 en una Base SeaTable como [cuenta de terceros]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).

Ahora las tablas pueden ocultarse, como es habitual en Microsoft Excel. Una **hoja de cálculo oculta** ya no se muestra como una pestaña y sólo se puede acceder a través del menú desplegable.

[Las casillas de verificación]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}}) ofrecen más opciones de estilo y aún más opciones de color en SeaTable 5.2. Si no le gusta la marca verde, ahora puede elegir entre otras 69 opciones.

En el [plugin de calendario]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}), ahora también se pueden crear nuevas entradas haciendo doble clic o utilizando el nuevo botón "+".

## Dos cambios funcionales

[Las filas anotadas]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) se etiquetan con iconos de bocadillos en la vista de tabla Base. Anteriormente, estos iconos se mostraban durante siete días. Con SeaTable 5.2, esta duración se ampliará a 180 días. Así que no se sorprenda si sus tablas tienen más bocadillos. Todas las filas con un comentario en los últimos 180 días tienen ahora un icono de bocadillo. Por supuesto, todos los comentarios seguirán guardándose en la base una vez transcurridos los 180 días.

Las llaves en los nombres de tabla pueden provocar conflictos en las fórmulas. Por esta razón, SeaTable versión 5.2 y superiores evitan el uso de **{** y **}** en nombres de tablas. Los nombres de tabla existentes no se modifican.
