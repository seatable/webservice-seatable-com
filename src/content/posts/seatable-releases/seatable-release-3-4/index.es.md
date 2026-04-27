---
title: 'SeaTable 3.4: diseño dinámico de páginas, más funciones de búsqueda y formularios web mejorados'
description: 'Diseña documentos con elementos autoajustables, personaliza formularios y prellénalos con enlace, busca en menús y listas. Nueva Data Query App para hallar datos en múltiples columnas. Mejoras en contexto de filas, registros y límites editables: mucho poder nuevo para equipos orientados a detalles.'
date: 2023-03-01
lastmod: '2023-03-01'
author: 'rdb'
url: '/es/seatable-release-3-4'
color: '#f36f22'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 3.4: Diseño dinámico y búsqueda avanzada'
    description: 'Motivos dinámicos en PDF, búsquedas múltiples, formularios y vistas flexibles: SeaTable 3.4 trae más control y personalización a tus datos.'
---

¡El despertar de la primavera en SeaTable! Mientras en el exterior brotan las primeras flores, nosotros salimos de las vacaciones de invierno con SeaTable 3.4. Prepárese para una experiencia de usuario mejorada y aún más libertad de diseño. El plugin de diseño de páginas despliega ahora todo su potencial al igual que el editor de formularios web, con funciones ampliadas para el posicionamiento dinámico de elementos y otras opciones útiles. Descubra la nueva función de búsqueda al filtrar, ordenar y agrupar en los ajustes de vista y al crear opciones en columnas de selección. También se han introducido notables innovaciones en la aplicación de consulta de datos, que ahora permite realizar búsquedas refinadas en varios campos. El menú contextual de la fila también tiene más opciones y las entradas del registro de filas lucen un nuevo esplendor.

¿Siente curiosidad? ¡Pues ponte en marcha! Esta mañana hemos actualizado SeaTable Cloud a la versión 3.4. Todos los auto-alojadores pueden hacer lo mismo - y ahora incluso liberar el límite de líneas por base. La imagen de SeaTable 3.4 está disponible para su descarga [en el conocido repositorio Docker](https://hub.docker.com/r/seatable/seatable-enterprise) . Como siempre, puede encontrar la lista completa de cambios en el [registro de cambios]({{< relref "posts/seatable-releases/seatable-release-3-4" >}}).

## Posicionamiento dinámico de elementos en el diseño de la página

Con el complemento de diseño de páginas, puede convertir los datos de sus bases en documentos descriptivos. Con sólo pulsar un botón, se crea una carta-formulario, un certificado o una lista de existencias. Hasta ahora, el complemento de diseño de páginas era menos adecuado para crear documentos con contenido de longitud variable, como ofertas o facturas. Con SeaTable 3.4 hemos eliminado esta restricción.

El complemento de diseño de páginas de SeaTable 3.4 permite por primera vez el posicionamiento dinámico de elementos en la página. En función de la longitud de los elementos precedentes, los elementos siguientes se desplazan hacia abajo en la página. Esto permite utilizar la misma plantilla tanto si una oferta contiene uno como una docena de elementos. Los saltos de página y las páginas nuevas se insertan automáticamente. Puede ajustar individualmente los márgenes superior e inferior.

![SeaTable 3.4 - Posicionamiento dinámico de elementos en el plugin de diseño de páginas](SeaTable-3.4-DynamicPositioningElements.png)

La nueva función "Adaptar automáticamente la tabla al contenido" está disponible para el elemento de la vista "Todas las entradas de la vista", así como para la representación tabular de los enlaces en "Campos de tabla". Cuando se activa la función, el marcador de posición del elemento tabla (elemento enmarcado en verde en la captura de pantalla) define la longitud mínima de la tabla que se va a insertar. Si la tabla es más larga que el marcador de posición, éste se amplía automáticamente.

La función anterior "Añadir más páginas si el tamaño del marcador de posición no es suficiente para todas las entradas", que se introdujo en la [versión 3.1]({{< relref "posts/seatable-releases/seatable-release-3-1" >}}), ya no existe en SeaTable 3.4 y se sustituye por la función más potente. Si se activó en una plantilla para un elemento de tabla, entonces la nueva función se activa automáticamente.

## Búsqueda en varios campos con la aplicación de consulta de datos

Las apps externas de SeaTable facilitan el acceso público a los datos de las tablas. En particular, la aplicación de consulta de datos se utiliza para consultar de forma rápida y específica conjuntos de datos con muchos cientos o incluso miles de filas (por ejemplo, un catálogo de productos o una lista de miembros). Con SeaTable 3.4 hemos eliminado el inconveniente de que las consultas sólo podían realizarse a través de un único campo.

Ahora se pueden realizar consultas sobre cualquier número de campos. Para cada campo, puede especificar si es obligatorio o si la entrada es opcional. Para los campos basados en texto, también puede activar una búsqueda difusa y forzar la consideración de mayúsculas y minúsculas. Combinando las opciones, puede controlar la búsqueda en gran medida. El menú para ocultar columnas individuales en los resultados de la búsqueda y las opciones de ordenación se mantienen sin cambios.

![SeaTable 3.4 - Mejora de la aplicación de consulta de datos](SeaTable-3.4-DataQueryApp.png)

En el caso de múltiples campos de consulta, siempre se aplica una operación booleana Y, es decir, todos los valores introducidos deben aparecer en los resultados de la búsqueda. Por supuesto, la aplicación de consulta de datos sigue siendo inadecuada para la información confidencial, ya que no requiere la autenticación del usuario. Cerraremos esta brecha funcional con otra app externa, que presentaremos próximamente.

## Formularios web mejorados

En [SeaTable 3.]({{< relref "posts/seatable-releases/seatable-release-3-3" >}}) 3 cambiamos el editor de formularios a diseño de bloques. Esto hizo posible organizar los campos en cualquier orden. También introdujimos las anotaciones de elementos estáticos y la línea separadora. En realidad había otras mejoras en desarrollo, pero no llegaron a la versión de Navidad. Ahora estamos compensando esta carencia.

El editor de formularios de SeaTable 3.4 ofrece la opción de definir un nombre para cada elemento del formulario, que se mostrará en el formulario web en lugar del nombre de la columna. De este modo es posible nombrar las columnas de la tabla independientemente del formulario web: Los nombres de las columnas pueden ser cortos y concisos, mientras que los nombres de los campos del formulario pueden ser algo más largos para facilitar su uso. Esto le da aún más libertad a la hora de diseñar sus formularios web.

![SeaTable 3.4 - Nuevo editor de enlaces de formularios personalizados](SeaTable-3.4-FormLinkEditor.png)

Dos mejoras se refieren a la capacidad de SeaTable para pre-llenar formularios web a través de parámetros URL. Si bien esta característica ha existido durante algún tiempo, carecía de una manera fácil de usar para crear y gestionar enlaces de formulario personalizados, así como la opción de proteger un valor pre-llenado de los cambios por parte del usuario del formulario. Hemos abordado y resuelto ambos problemas en SeaTable 3.4.

Detrás del botón "... Más" del editor de formularios hay una nueva ventana para crear cualquier número de enlaces de formulario. Cada enlace puede contener uno o varios valores de formulario ya rellenados. Además, puede especificar para cada valor si debe ser sobrescribible o estar protegido contra escritura. Los enlaces creados se identifican mediante un nombre de libre elección. Esto facilita volver a llamar los enlaces de formulario existentes y cambiarlos si es necesario.

## Función de búsqueda y filtro en la configuración de la vista

En el caso de las tablas con muchas columnas, las listas de selección de los ajustes de vista pueden llegar a ser bastante largas y confusas. Para reducir al mínimo el esfuerzo de búsqueda, ahora hay una función de búsqueda y filtro en todos los menús principales de los ajustes de vista (filtrar, ordenar, agrupar, ocultar y formatear filas). Es muy fácil de usar: introduzca el nombre de la columna que busca y sólo se mostrará la columna deseada. Por supuesto, esto también funciona si sólo introduce parte del nombre, por ejemplo si no está muy seguro de cómo se llama la columna que busca. A continuación, puede seleccionar la columna que necesita de la lista filtrada de resultados sin mucho esfuerzo.

![SeaTable 3.4 - Filtros en la configuración de la vista](SeaTable-3.4-FilterInViewSettings.png)

Dado que esta práctica función de búsqueda también faltaba en las columnas de selección única y múltiple con muchas opciones, también la hemos integrado allí. De este modo, al crear nuevas opciones, nunca más tendrá que comprobar laboriosamente si una opción ya existe o no.

## Y mucho más

Si echa un vistazo al registro de cambios, encontrará muchas más mejoras que no podemos explicar aquí individualmente. Sólo cabe mencionar aquí muy brevemente tres mejoras más.

![SeaTable 3.4 - Nueva función añadir/duplicar múltiples filas](SeaTable-3.4-AddMultipleRows.png)

Mediante el menú contextual de filas, al que se accede en las tablas haciendo clic con el botón derecho del ratón, ahora puede insertar varias filas en blanco y también duplicar varias filas seleccionadas.

Los registros en los detalles de las filas son más compactos en SeaTable 3.4 que antes. Todos los cambios que un usuario ha realizado en una fila en un momento determinado se muestran en una entrada colectiva. Anteriormente, se mostraba una entrada de registro separada para cada cambio.

Hasta ahora, el límite de líneas por base se mantenía en 100.000 líneas. Si se superaba el límite, la base sólo podía abrirse en modo lectura. Con SeaTable 3.4, los autoalojadores tienen más control sobre el límite de líneas. En determinados casos de uso, el límite puede aumentarse a través de los archivos de configuración. Encontrará más información al respecto en el [manual de Sea](https://admin.seatable.com/configuration/base-rows-limit/)Table.

## Dos limitaciones funcionales

Las bases y vistas compartidas a grupos ya no se pueden mover a carpetas con la nueva versión. Las bases y vistas compartidas que se han movido a una carpeta en el pasado se muestran ahora fuera de la carpeta.

Se ha eliminado el permiso de acceso "Grupos específicos" para formularios web. Si eres uno de los pocos usuarios que lo han utilizado, tendrás que restablecer el permiso de uso compartido.

## Anuncio de un cambio significativo de funciones

SeaTable 3.5 introduce un límite de 100.000 caracteres para las celdas individuales del tipo Texto con formato. 100.000 caracteres corresponden aproximadamente a 25 páginas A4 de texto. Por tanto, el límite de caracteres debería afectar a muy pocos usuarios.

Créditos de la imagen: weestock en Freepik
