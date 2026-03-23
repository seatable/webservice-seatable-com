---
title: 'SeaTable 3.0: Validación de datos, editores web de oficina y nuevo backend de almacenamiento - SeaTable'
description: 'Domine la entrada de datos con validación en columnas, colabore en Word, Excel o PowerPoint en tiempo real, optimice almacenamiento y use nuevos controles de gestión de equipos. Sincronización entre bases mejorada y mejoras menores en menú y exportaciones. Colaborar y organizar datos nunca fue tan fácil.'
date: 2022-06-21
lastmod: '2022-06-27'
author: 'rdb'
url: '/es/seatable-release-3-0'
color: '#cfe107'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 3.0: Validación y documentos Office online'
    description: 'Valide datos flexiblemente, edite Office online y use nuevo backend; sincronización y gestión mejoradas en SeaTable 3.0.'
---

¡SeaTable 3.0 ya está aquí! La tercera gran versión de SeaTable ofrece edición en línea de documentos de Office, validación automática de datos, más funciones para conjuntos de datos compartidos y un nuevo componente de servidor para un almacenamiento más eficaz de las bases. Como siempre, el [registro de cambios]({{< relref "pages/changelog" >}}) ofrece información sobre otras muchas mejoras y correcciones de errores en la nueva versión. Las nuevas funciones están disponibles inmediatamente para [los usuarios de SeaTable Cloud](https://cloud.seatable.io/). La imagen de SeaTable 3.0 se ha publicado esta noche en [Docker](https://hub.docker.com/r/seatable/seatable-enterprise/tags) Hub.  
Además de las mejoras funcionales en la aplicación de SeaTable, hay otra novedad para los usuarios de SeaTable Cloud: una nueva gestión de equipos con funciones ampliadas y un diseño mejorado que facilita la gestión de equipos pequeños y, sobre todo, grandes. Puede obtener más información sobre la nueva dirección del equipo en el artículo [La nueva dirección]({{< relref "help/teamverwaltung/abonnement/die-funktionen-der-teamverwaltung-in-der-uebersicht" >}}) del equipo.

## Validación automática de datos

En las columnas de texto se pueden introducir cadenas de cualquier tipo y longitud, lo que ofrece una gran flexibilidad. Las columnas de selección simple y múltiple son ideales para estructurar los datos debido a sus valores predefinidos. La nueva función de validación de datos permite combinar las ventajas de las columnas de texto con las de las columnas de selección.

Si la validación de datos está activada, SeaTable comprueba si el valor de la celda introducido se corresponde con el formato de destino definido. Si la entrada no se corresponde con el formato de destino, la celda se resalta en rojo. En los formularios web, una entrada no conforme dará lugar a un mensaje de error y el formulario no podrá ser enviado.

![Validación de datos en SeaTable 3.0](FormatCheck.png)

El formato de destino se define en forma de [expresión regular](https://de.wikipedia.org/wiki/Regul%C3%A4rer_Ausdruck). Por ejemplo, una expresión regular para una secuencia de números con exactamente 5 dígitos es \[0-9\]{5}. Hay dos argumentos a favor de las expresiones regulares: son un método muy utilizado y ofrecen la máxima flexibilidad. El tipo de caracteres permitidos, la longitud y también la sintaxis de la entrada pueden definirse con precisión mediante expresiones regulares.

La validación de datos está disponible en las columnas de texto en la versión 3.0. Si se añade un formato de destino posteriormente, también se comprueban todas las entradas existentes y se marcan como tales los valores no conformes. Por lo tanto, nada se opone a la activación posterior de la validación de datos en las columnas existentes.

## Edición en línea de documentos de Office

SeaTable hace que la colaboración en equipo sea interactiva. Una base se comparte con unos pocos clics y las entradas de una base compartida se muestran inmediatamente a otros usuarios. Los archivos de oficina en una base SeaTable son diferentes. Para editar un documento de Word, una hoja de cálculo de Excel o una presentación de PowerPoint, primero hay que descargarlo. La edición se realiza entonces fuera de línea. Los demás usuarios sólo tienen acceso a la versión modificada del documento tras la carga manual. Esto era una espina clavada.

SeaTable 3.0 amplía la colaboración en tiempo real conocida del editor de tablas a los documentos de Office. Los documentos pueden editarse directamente en el navegador y con varias personas al mismo tiempo. Los cambios de los coautores se muestran en tiempo real, para que sepas exactamente quién está trabajando en el documento y dónde. La carga manual ya no es necesaria. Cuando el último usuario abandona el documento, el estado actual del documento se transfiere automáticamente a SeaTable y se almacena en la columna de archivos como una nueva versión del documento.

Editar un documento de Office desde SeaTable no podría ser más fácil: un clic en el archivo de Word, Excel o PowerPoint abre el documento en un editor en una nueva pestaña. Los usuarios que están editando el documento en ese momento aparecen en la esquina superior derecha. Los cambios realizados por estos usuarios se llevan a cabo directamente en el documento visualizado y se indican con una bandera. El guardado se realiza automáticamente.

Los editores utilizados para la edición en línea son de [ONLYOFFICE](https://onlyoffice.com). Los editores del servidor de documentos ONLYOFFICE se caracterizan por una moderna interfaz de usuario y una muy buena compatibilidad con los formatos de archivo de Microsoft. Además, el servidor de documentos, al igual que SeaTable, puede ser autoalojado.

La edición en línea está disponible en todas las suscripciones de SeaTable Cloud, incluida la suscripción gratuita. Para el funcionamiento local de SeaTable, el servidor de documentos ONLYOFFICE debe ser instalado y configurado. Las instrucciones de configuración se encuentran en el [Manual de SeaTable](https://manual.seatable.io/).

## Mejora de la sincronización de las bases

La función Registros compartidos permite sincronizar los datos de una Base con otra u otras Bases. Son especialmente útiles si desea poner los datos a disposición de otros usuarios para su posterior tratamiento y enriquecimiento, pero no puede dar a estos usuarios derechos de acceso a la lista que usted gestiona ("lista maestra"). La versión 3.0 incluye varias mejoras para simplificar la creación, sincronización y duplicación de registros compartidos.

![Los conjuntos de datos comunes existentes se muestran en el cuadro de diálogo "Nuevo conjunto de datos comunes".](ExistingCDS.png)

A partir de SeaTable 3.0, los conjuntos de datos comunes ya creados se muestran en el diálogo "Nuevo conjunto de datos comunes". Esto evita la creación múltiple de conjuntos de datos comunes.

En la nueva versión, las columnas creadas al importar un registro común se marcan con un icono de sincronización. Esto hace que sea fácil distinguir las columnas que se sobrescribirán con el conjunto de datos comunes durante una resincronización de todas las demás columnas. El marcado visual reduce el riesgo de pérdida involuntaria de datos.

![Columnas importadas de CDS marcadas con el icono de sincronización](ColumnIconsCDS.png)

Al duplicar una tabla con un conjunto de datos común importado, hasta ahora sólo se duplicaban los datos. El enlace al conjunto de datos común no figuraba en la tabla duplicada, por lo que no era posible renovar la sincronización. La función de duplicación se ha ampliado para que se pueda transferir el enlace del conjunto de datos común a la nueva tabla que se va a crear o descartarlo mediante un conmutador.

## Mayor eficiencia de almacenamiento

El nuevo componente del servidor SeaTable dtable-storage-server reducirá significativamente los requisitos de memoria para el almacenamiento de bases, instantáneas y copias de seguridad de las filas archivadas. El componente seaf-server, que anteriormente se encargaba de ello, seguirá desempeñando un papel importante pero reducido

Técnicamente, el dtable-storage-server es una simple capa de abstracción para diferentes backends de almacenamiento. Como antes, se admite el almacenamiento local y el almacenamiento de objetos S3. Así, SeaTable ofrece atractivas opciones de almacenamiento tanto para sistemas pequeños y sencillos como para configuraciones altamente escalables.

Con los servidores SeaTable recién instalados, las bases se almacenan automáticamente en el servidor dtable-storage. Sólo el almacenamiento de imágenes y archivos sigue siendo realizado por el seaf-server. La situación es diferente para los sistemas existentes. Al actualizar un servidor SeaTable 2.x, el servidor de almacenamiento dtable no se instala y configura automáticamente. Esto debe hacerse manualmente; el procedimiento se describe en el [manual de SeaTable](https://admin.seatable.com/upgrade/extra-upgrade-notice/#30). Se recomienda una migración de las bases existentes al servidor de almacenamiento dtable. Para un pequeño número de bases, la exportación a un archivo DTABLE y la reimportación a una nueva base es el procedimiento más sencillo. Con un mayor número de bases, este proceso también puede automatizarse a través de la API. Sin embargo, la migración no es necesaria. SeaTable 3.0 puede seguir cargando bases desde el seaf-server.

## Otras mejoras

Además, hay otras muchas mejoras, de las cuales presentamos aquí muy brevemente las tres más importantes.

Se ha ampliado y revisado la estructura de los menús de la cabecera de la Base. El cambio más evidente es el avatar, que ahora se muestra en la parte superior derecha, de forma análoga a la página de inicio. Para dejar espacio al avatar, el botón de tres puntos se ha desplazado una línea hacia abajo. El menú detrás de este botón ha sido revisado. En consonancia con su importancia, las reglas de notificación y automatización, por ejemplo, se han eliminado de este menú. Ahora tienen su propio icono en la esquina superior derecha.

Los[archivos DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}), archivos de exportación de bases, ahora también contienen reglas de automatización. Lo mismo ocurre al copiar una base a otro grupo. Esto ahorra el trabajo manual innecesario al transferir bases entre grupos y servidores SeaTable.

Ahora se puede seleccionar la columna del título en el plugin de Kanban. El valor de las columnas de título está en la parte superior de la tarjeta Kanban, independientemente de la secuencia de las columnas en la tabla.
