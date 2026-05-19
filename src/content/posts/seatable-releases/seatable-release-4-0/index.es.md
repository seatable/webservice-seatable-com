---
title: 'SeaTable 4.0: nuevo tipo de columna, gestión de archivos mejorada y avances con Universal App Builder - SeaTable'
description: 'Ahora puedes firmar digitalmente tus documentos y gestionar archivos/folders más fácilmente. Integración nativa con Seafile para big data, estadísticas avanzadas fusionadas, mejoras visuales en el Universal App Builder y branding personalizable. Ideal para equipos modernos y análisis complejos.'
date: 2023-06-27
lastmod: '2023-06-27'
author: 'kgr'
url: '/es/seatable-release-4-0'
color: '#3aa3f4'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 4.0: firmas digitales y gestor archivos'
    description: 'Gestión avanzada de archivos, firmas digitales, integración Seafile, estadísticas fusionadas, nuevo App Builder: grandes mejoras en SeaTable 4.0.'
---

Mientras el sol abrasa en el exterior, nuestros desarrolladores han mantenido la cabeza fría y han completado la cuarta gran versión de SeaTable. La versión 4.0 de SeaTable mejora las funciones existentes, pero también sacia la sed de nuevas características. Novedades de la versión 4.0: un tipo de columna para firmas digitales, un gestor de archivos integrado para facilitar la gestión de archivos adjuntos y, para nuestros clientes de Cloud Enterprise, una función de logotipo personalizado como opción de marca.

SeaTable 4.0 también optimiza la integración de su aplicación hermana Seafile. La integración de las bibliotecas Seafile en SeaTable Bases no sólo es ahora más fácil, sino también más potente. Lo mismo se aplica a las funciones estadísticas, que hemos consolidado en SeaTable 4.0. El Universal App Builder (Beta) avanza a pasos agigantados y le ofrece extraordinarias posibilidades de preparación de datos para grupos de usuarios individuales. Nos complace presentarle estos aspectos destacados y muchas otras mejoras menores.

Esta mañana hemos actualizado SeaTable Cloud a la versión 4.0. Todos los auto-alojadores pueden hacer lo mismo: La imagen SeaTable 4.0 está disponible para su descarga en el conocido [repositorioDocker](https://hub.docker.com/r/seatable/seatable-enterprise) . Como siempre, puede encontrar la lista completa de cambios en el [registro de cambios]({{< relref "pages/changelog" >}}).

## Nuevo tipo de columna para firmas digitales

No hay nada más vinculante que una firma, ya sea en contratos, escrituras o cartas. En SeaTable puede crear todos estos documentos. Entonces, ¿qué podría ser más obvio que digitalizar firmas manuscritas con SeaTable? La nueva columna de firma lo hace posible. Guarde su firma digital simplemente firmando en una celda de esta columna de imagen especial con un gesto de barrido utilizando el ratón o, en dispositivos con pantalla táctil, con un bolígrafo o un dedo.

![Añadir una firma en una columna de firma](Add-a-signature-in-a-signature-column.gif)

Esto permite flujos de trabajo para procesos de empleados y clientes que antes no podía asignar en SeaTable: Con un campo de firma insertado, puede, por ejemplo, hacer que las solicitudes de vacaciones o las inscripciones a seminarios en [formularios web]({{< relref "help/base-editor/webformulare" >}}) y [aplicaciones universales]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}) sean firmadas por la persona que las cumplimenta. Del mismo modo, los clientes pueden confirmar a un instalador que los servicios se han llevado a cabo in situ. Mediante el [complemento de diseño de páginas]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}), las firmas pueden insertarse fácilmente en documentos, que luego pueden enviarse como archivos adjuntos por correo electrónico. La perfecta integración del nuevo tipo de columna crea muchas oportunidades para que los procesos sean más vinculantes.

## Potente gestión de archivos en Base

La gestión de archivos en SeaTable 4.0 revoluciona el trabajo con archivos en sus bases. Con el nuevo gestor de archivos, puede gestionar archivos de forma fácil y cómoda directamente en sus bases y las nuevas carpetas personalizadas le ofrecen aún más flexibilidad a la hora de almacenar y organizar archivos. Se elimina la anterior gestión de archivos adjuntos, a la que sólo se podía acceder a través de las opciones avanzadas de una base en la página de inicio.

El gestor de archivos, al que se accede mediante el icono de tres puntos situado en la parte superior derecha de Base y que se añade a la barra de herramientas, se presenta de la forma más familiar imaginable: Archivos y carpetas a la derecha, navegación a la izquierda: los usuarios se sentirán como en casa.

![Arrastrar y soltar archivos desde la gestión de archivos a una columna de archivos](dateien-aus-dem-dateimanagement-per-drag-and-drop-in-eine-dateispalte-ziehen.gif)

Los archivos existentes se pueden renombrar, copiar, mover, descargar y eliminar en el gestor de archivos. También se pueden crear y editar nuevos documentos de Office directamente a través del editor integrado. Ahora puedes cargar fácilmente archivos y carpetas desde tu dispositivo o añadirlos al gestor de archivos mediante arrastrar y soltar. Los archivos también pueden arrastrarse y soltarse desde el gestor de archivos a las celdas de las columnas de las tablas correspondientes y asignarse así a los registros de datos. Para disponer del máximo espacio posible, el gestor de archivos puede redimensionarse y fijarse como barra lateral.

![Estructura de carpetas en la gestión de archivos](Ordnerstruktur-im-Dateimanagement-2.png)

Las carpetas del sistema están relacionadas con la estructura de Base y contienen imágenes, archivos y firmas de las respectivas columnas, así como los archivos de configuración de apps y formularios web. En las carpetas personalizadas, puedes almacenar y organizar archivos de forma independiente en carpetas individuales. A continuación, los archivos están disponibles en scripts de Python y otras funciones como formularios web o el complemento de diseño de páginas; sin embargo, algunas de estas integraciones sólo se completarán en futuras versiones.

## Integración facilitada de Seafile para grandes volúmenes de datos

Hablando de gestión de archivos: si almacenas muchos archivos grandes (por ejemplo, imágenes y vídeos) en tus bases, alcanzarás rápidamente el límite de 100 MB por base, a partir del cual ya no podrás [exportar]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}) tus bases. Esto supone una pérdida de flexibilidad. Otro límite que se vuelve relevante cuando se almacenan muchos archivos en SeaTable es el límite de [almacenamiento]({{< relref "pages/prices" >}}) por suscripción. Para ambos límites, SeaTable 4.0 ofrece una solución de valor añadido con la nueva opción de integración de Seafile, la aplicación hermana de SeaTable.

Como solución empresarial de sincronización y uso compartido de archivos, [Seafile](https://de.seafile.com/) está predestinada a gestionar cualquier cantidad de archivos de gran tamaño. Además, gracias a sus clientes, ofrece la mejor integración posible en el entorno de trabajo individual, incluido el soporte offline. La nueva integración permite utilizar los archivos almacenados en Seafile directamente en SeaTable. Se combinan los dos productos en una solución de una sola fuente y se combinan los puntos fuertes de Seafile con los de SeaTable.

Integrar Seafile en SeaTable no podría ser más fácil: Genere un token API para una biblioteca Seafile a través de la interfaz web de Seafile, cree una nueva cuenta de terceros en SeaTable y añada allí el token (véase la figura). Una vez vinculada correctamente, la biblioteca Seafile aparece en la gestión de archivos.

![Integración facilitada de Seafile para grandes volúmenes de datos](verbesserte-integration-mit-seafile-release-notes.png)

Se pueden conectar servidores Seafile alojados y autoalojados. [Póngase en contacto con nuestro equipo de ventas]({{< relref "pages/contact" >}}) si desea alojar usted mismo un servidor Seafile. Para los clientes de SeaTable Dedicated ofrecemos co-hosting Seafile.

## El plug-in de estadísticas y el módulo de estadísticas se fusionan en una sola herramienta

SeaTable le ofrece una amplia gama de opciones para el [análisis estadístico de datos]({{< relref "help/base-editor/statistiken" >}}) y su presentación gráfica. Hasta ahora, tenía a su disposición tanto un módulo de estadísticas con funciones básicas como el complemento de estadísticas avanzadas. En SeaTable 4.0, este último se traslada al lugar donde solía estar el módulo básico, por lo que ya no necesitará configurar un plugin. Toda la potencia estadística de SeaTable está ahora integrada en una potente herramienta, a la que puede acceder con un solo clic a través del botón "Estadísticas" de la cabecera Base.

![El plug-in de estadísticas y el módulo de estadísticas se fusionan en una sola herramienta](erweitertes-statistik-plugin-release-notes.gif)

Por supuesto, todos los gráficos y diagramas que ya haya creado, ya sea en el módulo Estadísticas o en el complemento Estadísticas avanzadas, se conservarán y se trasladarán automáticamente al nuevo panel de control.

## Progresos con Universal App Builder

El [Universal App Builder]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}) (Beta) goza de gran popularidad, nuestro equipo de desarrollo está trabajando a toda velocidad en los últimos retoques y ¡los resultados son impresionantes! Todos los tipos de [página]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) tienen ahora un diseño uniforme y ofrecen la función de búsqueda por columnas en la configuración de datos que ya conoce de las bases. Además, todos los tipos de página admiten ahora el [filtro "ID real del usuario conectado"]({{< relref "help/base-editor/ansichten/was-ist-die-id-des-users-und-warum-kann-man-danach-filtern" >}}). Uno de los puntos centrales del trabajo de desarrollo ha sido la página individual, cuyo manejo hemos mejorado notablemente. También hemos corregido errores en los diagramas. No se descuidaron los demás tipos de página. Se optimizó el soporte de columnas para las páginas de formularios web, Kanban y Timeline. Un aspecto destacado del Universal App Builder en SeaTable 4.0 es el nuevo tipo de página "Query", que integra la funcionalidad de la [aplicación de consulta de datos]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}) en la Universal App.

![La aplicación universal](SeaTable_Universal-App.png)

En las versiones 4.1 y 4.2 se añadirán otras funciones que ya están establecidas en las bases. Entre ellas, por ejemplo, el formato condicional y la altura de línea variable. Entonces también finalizará la fase beta de Universal App Builder.

## Y mucho más

Los pequeños logros de SeaTable también te hacen la vida más agradable: las carpetas de la página de inicio se abren ahora en una ventana aparte, lo que te permite ver mejor las bases allí clasificadas.

![Nueva vista de carpetas en la página de inicio](ordner-auf-der-startseite-release-notes.gif)

Bloquear una fila - con una regla de automatización o manualmente a través del menú contextual de la fila, esto ha sido posible para los usuarios de Enterprise desde hace algún tiempo. Ahora la [columna de botones]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) también tiene "Bloquear fila" como nueva acción. Utilícela en combinación con las otras siete acciones para completar procesos complejos simplemente con un clic del ratón. Además, hemos añadido valores de fecha dinámicos a la acción "Editar fila" y hemos mejorado la visualización de las opciones de selección.

Si hace clic en la celda de una [columna de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), se abre un diálogo ampliado de SeaTable 4.0: Puede enlazar entradas existentes o -y esto es nuevo- añadir una fila. Esto le permite crear una nueva fila en la tabla vinculada y una entrada vinculada en la tabla abierta al mismo tiempo, lo que le ahorra algo de esfuerzo: antes, tenía que cambiar primero a la tabla vinculada para añadir una nueva fila, que luego podía vincular en la otra tabla. En la configuración de la columna de enlace, también puede especificar que sólo se puedan crear y enlazar entradas nuevas seleccionando la opción de no mostrar el botón "Enlazar entradas existentes".

Con una suscripción Enterprise, puede utilizar el logotipo de su propia empresa en la página de inicio en lugar del logotipo de SeaTable para anclar su diseño corporativo. Si valora tanto la estética como el rendimiento, le encantará lo siguiente: Hemos agilizado y acelerado la creación de PDF en el [plugin Diseño de]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}) página para que no pierda tiempo esperando.

## Nuevo límite

En el registro de bases, SeaTable guarda los cambios que usted y los miembros de su equipo realizan en una base. Hasta ahora, podía desplazarse al pasado y ver el historial sin límite. Con SeaTable 4.0 estamos introduciendo un límite de 1.000 entradas en el registro de la base. La documentación de los cambios realizados incluso más atrás en el tiempo se eliminará y, por lo general, ya no será necesaria. Puede encontrar información adicional sobre el historial en SeaTable [aquí]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}).

## Ajuste de precios

Desde la versión 1.0, hemos ampliado la funcionalidad de SeaTable paso a paso. También hemos realizado importantes inversiones en integraciones más sencillas y potentes, en la mejora de la documentación y en el aumento de la seguridad. Junto con la dinámica de precios generalmente altos, esto requiere un ajuste de nuestros precios para las [licencias de SeaTable Server]({{< relref "pages/product/seatable-server" >}}).

| Número de usuarios | Precio hasta ahora | Precio nuevo | Cambia    |
| ------------------ | ------------------ | ------------ | --------- |
| 3                  | 0 €                | 0 €          | \--       |
| 10                 | 400 €              | 500 €        | \+ 25,0 % |
| 25                 | 1.500 €            | 1.250 €      | \- 16,7 % |
| 50                 | 3.500 €            | 4.500 €      | \+ 28,6 % |

Para los nuevos clientes, los nuevos precios de licencia se aplicarán a partir del 1 de agosto de 2023. Los clientes existentes de SeaTable Server seguirán recibiendo ampliaciones de licencia a los precios antiguos hasta el 31 de diciembre de 2023.

**El ajuste de precios se aplica explícitamente sólo a los autoalojadores. Los precios de SeaTable Cloud no cambian.**
