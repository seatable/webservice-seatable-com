---
title: 'SeaTable 1.5: Editor, acciones y formularios web mejorados - SeaTable'
description: 'Menús en línea y sin modals, tablas y vistas con permisos selectivos, formularios con agradecimiento, redirección y textos propios, estadísticas y gráficos mejorados, plugins pulidos y triggers Python. Una versión más cómoda, precisa y adaptable desde el primer clic.'
date: 2020-11-27
lastmod: '2022-06-14'
author: 'rdb'
url: '/es/seatable-release-1-5'
color: '#fba303'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 1.5: editor, permisos, formularios'
    description: 'Editor renovado, permisos personalizados, formularios flexibles y mejores plugins: SeaTable 1.5 impulsa la usabilidad.'
---

Hoy hemos actualizado cloud.seatable.io a la versión 1.5 de SeaTable. Con el próximo inicio de sesión, todos los usuarios se beneficiarán de nuevas e interesantes características y de una serie de mejoras en la interfaz y en las funciones existentes. A primera vista, notará los numerosos cambios menores y mayores en el editor de tablas, lo que se traduce en una mayor eficiencia del flujo de trabajo y una mejor experiencia del usuario. Los nuevos permisos de uso compartido personalizados proporcionan más control y flexibilidad a la hora de trabajar en colaboración en las bases. Las opciones de personalización mejoradas hacen de los formularios web de SeaTable una herramienta aún más versátil para la recogida de datos.

La lista completa de cambios se puede encontrar, como siempre, en [el registro de cambios de SeaTable]({{< relref "pages/changelog" >}}). Esta nota de lanzamiento presenta los cambios más importantes y emocionantes de esta nueva versión.

## Editor de tablas mejorado

Dado que la mayoría de los usuarios pasan la mayor parte de su tiempo en el editor de tablas, dedicamos mucha atención y esfuerzo a buscar formas de hacer que los numerosos menús, asistentes y vistas del editor sean aún más fáciles de usar. Creemos que hemos avanzado mucho en este sentido con la versión 1.5. Hemos sustituido los modales por menús en línea, hemos mejorado el diseño de los menús y hemos actualizado la biblioteca de software de la vista de estadísticas a la última versión. Además, hemos mejorado los complementos de visualización. En definitiva, introducir y editar datos en el editor de tablas de SeaTable 1.5 es ahora mucho más divertido.

### Adieu Modals

Los modales eran más comunes en versiones anteriores de SeaTable. Por ejemplo, los diálogos "Insertar columna" y "Ajustar tipo de columna" eran [modales](https://en.wikipedia.org/wiki/Modal_window) de este tipo, en los que los controles aparecían en primer plano y el fondo estaba oculto. Aunque nos han servido bien hasta ahora, los modales ofrecen margen de mejora en términos de facilidad y eficiencia de trabajo: cuando el modal se abre en medio de la pantalla, pide al usuario que vaya allí con el ratón. Y lo que es más grave, al desactivar las barras de desplazamiento, la información relevante no puede salir de detrás de un modal cuando éste la tapa. ¿Qué hemos hecho? Hemos sustituido los modales por menús no modales que ofrecen todas las funciones de sus predecesores sin sus inconvenientes.

![Se han sustituido los modales por menús no modales](Nonmodal_Menus.png)

### Menús simplificados

El menú de opciones de las columnas de selección simple y múltiple es otro modal que hemos convertido en un menú no modal. Sin embargo, no lo dejamos así. También hemos sustituido el menú de varios niveles existente, algo engorroso, por un menú plano mucho más cómodo. Ahora se pueden crear, modificar y eliminar opciones en una ventana transparente. El número de clics necesarios se ha reducido al mínimo.

### Edición simultánea de varias tablas

[SeaTable 1.4]({{< relref "posts/seatable-releases/seatable-release-1-4" >}}) introdujo un nuevo asistente que facilita la vinculación de las entradas. Este asistente se abre con un clic en una celda de enlace y luego muestra todas las entradas de la columna vinculada en una ventana transparente. Otro clic en una entrada crea el enlace a la entrada en la celda. En otras palabras, con el nuevo asistente, vincular entradas se ha convertido en algo tan sencillo como seleccionar un valor de un menú desplegable.

SeaTable 1.5 hace que este asistente sea aún más potente: ahora las entradas de la columna vinculada no sólo pueden visualizarse, sino también editarse directamente. Al hacer clic en una entrada vinculada se abren sus detalles y todos los cambios realizados aquí se guardan directamente en la tabla vinculada. Si quiere saltar a la tabla vinculada, puede hacerlo con el enlace directo en la parte superior de los detalles.

![Los registros enlazados ahora pueden editarse directamente desde la columna "enlazar otros registros".](Editing_Linked_Records_With_Wizard.png)

### Aún más preciso

No sólo se han actualizado las columnas de selección y enlace, sino también las columnas de números y fórmulas. Ahora se puede definir la precisión decimal en la columna de números. Los decimales pueden ajustarse individualmente a un valor de 0 a 8 en cada una de esas columnas. Por supuesto, esto se aplica independientemente del formato (número, porcentaje y moneda) y del separador decimal seleccionado.

Si el resultado de una fórmula es un número (por ejemplo, para las fórmulas suma, redondeo y promedio), todas las opciones de formato de la columna de números también están disponibles en la columna de fórmulas. Para una máxima flexibilidad, el formato de la columna de la fórmula es independiente de las columnas utilizadas en la fórmula.

### Mejores estadísticas

El módulo de estadísticas de SeaTable utiliza la [biblioteca de software de visualización de datos de código abierto G2](https://g2.antv.antgroup.com/en). G2 permite generar una variedad de evaluaciones basadas en la web de forma interactiva y dinámica en SeaTable.

En SeaTable 1.5 hemos actualizado G2 a la actual versión 4.0. El equipo de visualización de datos del Grupo Ant lo publicó en la primavera de 2020. Junto con algunas mejoras relativas a la integración, esta actualización aumenta la fiabilidad y la estabilidad generales del módulo de estadísticas.

### Mejora de los plugins de visualización

Tampoco se ha descuidado el plugin de mapas y línea de tiempo. El plugin del mapa ahora recuerda la última posición del usuario. Si ahora abre de nuevo la vista del mapa, puede continuar directamente donde lo dejó por última vez. En el plugin de la línea de tiempo, hemos reducido la velocidad de desplazamiento, que muchos usuarios encontraban demasiado rápida.

## Acciones definidas por el usuario

Imagina que quieres compartir una base con los miembros de tu equipo con diferentes derechos de acceso: Todos los colegas deberían tener al menos acceso de lectura, pero algunos colegas deberían tener también acceso de lectura y escritura a algunas tablas y unos pocos colegas elegidos a dedo deberían tener acceso completo a todas las tablas. Suena complicado de aplicar y, de hecho, lo era. Había que dividir una base en varias bases y compartirla con los distintos grupos con diferentes derechos. Hasta ahora.

![SeaTable 1.5 ahora es compatible con los permisos de uso compartido personalizados](Custom_Sharing_Permission.png)

En la nueva versión introducimos permisos de liberación definidos por el usuario. Gracias a ellos, el escenario que acabamos de mencionar es posible sin muchos dolores de cabeza. Un permiso de uso compartido personalizado consiste en derechos de acceso individuales para todas las tablas y vistas de una base. Con un permiso de uso compartido personalizado, puede, por ejemplo, conceder acceso de lectura a una tabla pero ampliar el acceso de lectura y escritura a otra tabla de la base. Pero eso no es todo: las acciones personalizadas también pueden especificarse a nivel de vista. Por lo tanto, puede conceder acceso de lectura y escritura a una vista específica de una tabla, pero de sólo lectura a la vista por defecto. Si no quiere conceder acceso a una tabla o vista, también es posible. Simplemente no conceda acceso de lectura ni de escritura. Y lo mejor de todo es que puedes definir tantos [permisos de uso compartido]({{< relref "help/startseite/freigaben" >}}) personalizados como quieras para cada base. ¿Ha estado anhelando una gestión de permisos más granular en SeaTable? ¡Ahora lo tienes!

## Formularios web más flexibles

Los potentes formularios web de SeaTable han tenido una gran demanda en los últimos meses. Estamos encantados de que innumerables restaurantes, cafés y bares de toda Europa hayan encontrado en SeaTable una solución sencilla para aplicar los requisitos de registro de los clientes durante la pandemia de Corona.

Basándonos en los comentarios de los clientes y con la esperanza de apoyar a este sufrido sector, hemos añadido tres opciones para personalizar los formularios web: En primer lugar, ahora se pueden crear mensajes individuales de "Gracias por su participación". Si desea enviar un agradecimiento especial a sus invitados o facilitarles más información después de que hayan respondido a las preguntas, SeaTable 1.5 le permite hacerlo. En segundo lugar, el reenvío automático ha sido una función muy solicitada. Es un placer para nosotros implementarla también en esta nueva versión. Si se especifica una dirección de reenvío, SeaTable reenvía automáticamente a esta dirección. En tercer lugar, también hemos flexibilizado las funciones de sugerencia. Además de la sugerencia en la parte inferior del formulario, ahora también existe la posibilidad de mostrar una sugerencia delante de los campos del formulario.

![Los formularios web de SeaTable ofrecen ahora más opciones de personalización](Extra_Customization_Options_Webforms.png)

Cruzamos los dedos para que la pandemia de Corona sea pronto algo para los libros de historia. Por otra parte, esperamos que estas mejoras sirvan de apoyo a los usuarios de SeaTable en los sectores más afectados en su trabajo si la pandemia se prolonga.

## Otras mejoras

En esta nota de la versión sólo se comentan en detalle los cambios más importantes. El registro de cambios contiene el historial completo de cambios. Echa un vistazo allí! Entre las mejoras menores que vale la pena mencionar están los disparadores de tiempo para los scripts de Python (véase [la nota de lanzamiento de SeaTable 1.4]({{< relref "posts/seatable-releases/seatable-release-1-4" >}}) y la eliminación de los problemas de rendimiento cuando se manejan conjuntos más grandes de filas en el editor de tablas.

Obtenga una cuenta SeaTable para su equipo y utilice SeaTable de forma permanente y gratuita. Agradecemos sus opiniones y comentarios en el [foro](https://forum.seatable.com/).
