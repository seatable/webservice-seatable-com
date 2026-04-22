---
title: 'SeaTable 4.3: Nuevos enlaces de formularios, automatizaciones y funciones de la aplicación'
description: 'Haz URLs propias para formularios, automatiza la creación de PDF y avisos en apps, añade colaboradores entre equipos, aprovecha comentarios y nuevas tarjetas. Correos con texto enriquecido, colores a medida, autorizaciones finas, exportación flexible, nueva API: el trabajo en equipo nunca fue tan fluido.'
date: 2024-02-08
lastmod: '2024-02-16'
author: 'kgr'
url: '/es/seatable-release-4-3'
color: '#fd5d04'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 4.3: enlaces, automatización y apps'
    description: 'Enlaces a formularios personalizados, PDF y notificaciones automáticas, mejoras en apps universales: SeaTable 4.3 impulsa la gestión inteligente.'
---

La temporada de carnaval en Alemania se acerca a su punto álgido, ¡y los cañones de confeti también estallan en SeaTable! La versión 4.3 trae consigo algunas funciones y mejoras muy esperadas.

Disfruta de un nuevo diálogo para crear **enlaces de formularios** en el que podrás adaptar las URL a tus deseos personales. Utilice dos nuevas **automatizaciones** para crear documentos y enviar notificaciones a los usuarios de la aplicación. O prueba las nuevas funciones de la **aplicación universal**: Entre otras cosas, puedes esperar comentarios, dos elementos adicionales para la página individual y una mejor personalización del esquema de colores.

Esta mañana hemos actualizado SeaTable Cloud a la versión 4.3. Todos los auto-alojadores pueden hacer lo mismo: La imagen de SeaTable 4.3 está disponible para su descarga en el conocido [repositorioDocker](https://hub.docker.com/r/seatable/seatable-enterprise) . Como siempre, puede encontrar la lista completa de cambios en el [registro de cambios]({{< relref "pages/changelog" >}}).

También hemos actualizado los plugins a Webpack 5 y actualizado el framework a React 17.0.2, lo que garantizará una mayor seguridad y estabilidad en el futuro y permitirá funciones adicionales.

## Nuevo diálogo y enlaces definidos por el usuario para formularios web

Para compartir sus [formularios web]({{< relref "help/base-editor/webformulare" >}}) con otros usuarios, antes había dos cuadros de diálogo diferentes: uno en el que podía copiar un **enlace generado automáticamente** y otro en el que podía ampliar este enlace con [valores rellenados previamente]({{< relref "help/base-editor/webformulare/formularfelder-per-url-vorbefuellen" >}}). Ahora hemos combinado estas opciones en un único cuadro de diálogo para aumentar la facilidad de uso.

También hemos añadido la nueva opción de crear **URL personalizadas** para formularios web. Después puedes editarlas, guardarlas como código QR, copiarlas o eliminarlas.

![Nuevo diálogo de enlace de formularios en SeaTable 4.3](Formularlink-Dialog.gif)

{{< warning headline="Nota" text="La parte definida por el usuario que se añade al enlace debe tener **entre 5 y 30 caracteres** y sólo puede contener **letras**, **números** y **guiones**. Además, cada URL debe ser única: Si una URL definida por el usuario ya está en uso, aparece un mensaje de error." />}}

## Acciones automatizadas: Guardar PDF y enviar notificación de aplicación

¡Atención aficionados a la automatización! SeaTable 4.3 añade dos nuevas opciones a las [acciones automa]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) tizadas:

1. En primer lugar, tiene la posibilidad de guardar periódicamente los PDF de las entradas que cumplan determinadas condiciones.
2. En segundo lugar, ahora puedes enviar notificaciones que deben recibir determinados usuarios de una aplicación universal.

Antes, en SeaTable sólo podía [crear documentos PDF]({{< relref "help/base-editor/schaltflaechen/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern" >}}) manualmente [mediante un botón]({{< relref "help/base-editor/schaltflaechen/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern" >}}). La nueva opción de crear **automáticamente** documentos a partir de registros de datos específicos en un momento determinado le ahorra clics y agiliza aún más sus procesos.

Puede utilizar las **notificaciones de la** aplicación para informar a los usuarios de una aplicación sobre los cambios en los registros de datos relevantes, por ejemplo. Esta acción puede [activarse]({{< relref "help/base-editor/automationen/automations-trigger" >}}) mediante los cuatro [eventos desencadenantes]({{< relref "help/base-editor/automationen/automations-trigger" >}}).

![Enviar notificación de aplicación](App-Benachrichtigung-senden.png)

Los usuarios de la aplicación correspondiente pueden acceder a sus notificaciones a través del icono de campana {{< seatable-icon icon="dtable-icon-notice" >}} situado junto a su avatar en la esquina superior derecha.

## Columna de empleados entre equipos

En la [columna]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) de empleados, antes sólo era posible seleccionar a las personas que ya tenían acceso a la base correspondiente. A partir de SeaTable 4.3, puede introducir a **todos los miembros de su** equipo en las columnas de empleados, aunque no tengan acceso a determinadas bases. Esto facilita enormemente la asignación de registros de datos a sus empleados, independientemente de su autorización de acceso.

Esta funcionalidad es especialmente útil en la aplicación universal. Puede activar la opción de que los miembros del equipo sean visibles para todos los usuarios en la lista desplegable de los [ajustes de]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern/" >}}) la app Universal. Si no quieres que los usuarios puedan ver los registros de datos de otros, establece **filtros preestablecidos**: si una página se filtra por columna de empleado con la condición "incluye al usuario actual", cada usuario de la app universal solo verá las entradas que se le asignen en la tabla.

![Columna de empleados en la aplicación universal](Mitarbeiter-Spalte-in-der-Universellen-App.gif)

## Nuevas mejoras de la aplicación universal

Una novedad de la aplicación universal es la [función de comentarios]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), que ya reconocerá en la misma forma de Base. Anota tus comentarios o información adicional en los registros de datos de otros usuarios de la aplicación y mantén conversaciones sobre la marcha.

{{< warning headline="Es bueno saberlo" text="Los comentarios en la aplicación son completamente **independientes** de los comentarios en la base. Esto significa que cada comentario solo es visible donde se publica." />}}

En la [página individual]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}), le esperan dos nuevos elementos: el **contenedor** y el **mapa**. El contenedor proporciona una cuadrícula con la que puede organizar otros elementos (textos, imágenes, estadísticas) más fácilmente y agruparlos.

![Elemento contenedor en página personalizada en SeaTable 4.3](Container-element-on-custom-page.png)

La tarjeta, que combina una imagen, un titular y un texto en una plantilla de diseño, también garantiza un bonito diseño de página.

![Elemento tarjeta en página personalizada en SeaTable 4.3](Card-element-on-custom-page.png)

Además, el **color de fondo** de las páginas individuales se puede configurar como se desee desde SeaTable 4.3 y se ha corregido la superposición no deseada de elementos. El diseño general de la aplicación universal también se presenta ahora en un color uniforme en todas las páginas, que se puede seleccionar en la [configuración global]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern/" >}}).

### Autorizaciones en páginas de tablas

La herencia de [autorizaciones de columna]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}) de la base se suprime con SeaTable 4.3. Si desea bloquear la edición de una columna en la aplicación universal, puede establecerla como **"solo lectura"** en la configuración de [la página de la tabla]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}).

También se han eliminado todas las restricciones para [las acciones de los botones]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}). Ahora todos los usuarios de la aplicación pueden realizar cambios predefinidos en los registros de datos, aunque las columnas afectadas estén bloqueadas para ellos y el usuario no esté autorizado a editar la página.

## Anuncio importante: Eliminación de la app de galería y consulta de datos

En la versión 4.4, la [aplicación de galería]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}) y la [aplicación de consulta de datos]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}) desaparecerán, ya que su funcionalidad ahora se puede asignar completamente con los **tipos de página** correspondientes en la aplicación universal. Por lo tanto, Universal App Builder será la única opción para crear aplicaciones en SeaTable en el futuro.

Si utiliza las dos aplicaciones que expiran, le recomendamos que reconstruya sus casos de uso con páginas de [galería]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}) y páginas [de]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}) consulta en el App Builder antes de la próxima versión. Por cierto, ahora puedes añadir campos a las páginas de consulta que permiten a los usuarios buscar valores específicos en **las columnas de enlace**.

{{< warning headline="¡Atención, peligro de confusión!" >}}

También conoces la [galería]({{< relref "help/base-editor/ansichten/die-galerie-ansicht" >}}) y la [consulta]({{< relref "help/base-editor/plugins/anleitung-zum-sql-abfrage-plugin" >}}) SQL como **plugins** que puedes añadir a tus bases. Estos, por supuesto, permanecerán en su lugar.

{{< /warning >}}

## Y mucho más

Si [envía correos electrónicos mediante automatización]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}), antes sólo podía introducir el mensaje como **texto sin formato** en el campo de texto. A partir de SeaTable 4.3, es posible redactar los mensajes en **formato de texto enriquecido o HTML** mediante botones, igual que al enviar correos electrónicos. Para ello, basta con activar el control deslizante situado a la derecha, encima del campo de texto.

![Texto enriquecido en mensajes de correo electrónico automatizados](Rich-text-in-automated-e-mail-messages.png)

Si desea utilizar **autorizaciones de columna** para proteger los valores de cambios no deseados, en el futuro podrá definirlo con mayor precisión. Además de _usuarios específicos_, _administradores_ y _nadie_, ahora también se puede optar por **determinados grupos**.

En el futuro, habrá una opción para [exportar]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}) bases sin los archivos adjuntos cargados en el gestor de archivos si superan el límite de exportación de 100 MB por base.

En términos de API, SeaTable 4.3 soporta por primera vez [consultas JOIN](https://developer.seatable.com/scripts/sql/reference/), con las que podrá consultar aquellos registros de datos de diferentes tablas que compartan una intersección común de atributos. Encontrará más información al respecto en el Manual del desarrollador.

## Instalación simplificada de SeaTable y componentes adicionales

Por último, tenemos un regalo especial para los **clientes locales**: para coincidir con el lanzamiento de la versión 4.3 de SeaTable Cloud, también hemos revisado las **instrucciones de instalación** en nuestro [manual de administración](https://admin.seatable.com).

Nuestro principal objetivo es facilitar aún más la **instalación y futuras actualizaciones de su propio servidor SeaTable**. Por ejemplo, en el futuro el servicio se iniciará automáticamente cuando inicie el contenedor asociado, y ya no tendrá que iniciar las actualizaciones de la base de datos manualmente. Estas son sólo algunas de las muchas pequeñas mejoras que le harán la vida más fácil como administrador y que ahora puede encontrar en el manual del administrador.

También simplificamos la instalación de componentes adicionales como el **pipeline Python** para ejecutar código Python en SeaTable y la **plataforma de automatización n8n**. Cada una de estas extensiones es proporcionada por nosotros lista para usar y puede ser instalada con sólo unos pocos comandos. Así podrá sacar aún más partido a su servidor.
