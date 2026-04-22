---
title: 'SeaTable 6.0: El no-código se vuelve inteligente'
description: 'SeaTable 6.0 une no‑code y IA: nuevas funciones de IA, editor de automatización renovado, vistas de calendario, Kanban y galería y columna de teléfono.'
date: 2025-11-04
author: 'rdb'
url: '/es/seatable-release-6-0'
color: '#ff9831'
categories:
    - 'product-features'
seo:
    title:
    description:
register:
   show: true    
---

SeaTable 6.0 combina los puntos fuertes del no-código y de la inteligencia artificial (IA). **Con las nuevas funciones de IA** se pueden analizar, modificar y ampliar los registros de datos, evaluar los documentos y extraer con precisión la información relevante. Y todo ello sin preocuparse por la protección y confidencialidad de los datos: SeaTable es compatible con una amplia gama de proveedores y modelos de IA. Por supuesto, también es posible el **autoalojamiento de modelos de IA**. Adoptamos este enfoque en aras de la protección de sus datos.

**El editor completamente revisado para las reglas de automatización** hace que utilizar las nuevas funciones de IA sea un juego de niños. Pero todas las demás automatizaciones también se benefician de la interfaz de usuario orientada al flujo de trabajo del editor de reglas y de sus funciones ampliadas.

**Los nuevos tipos de vista Calendario, Kanban y Galería**, que sustituyen a los plugins del mismo nombre, también ofrecen más claridad y funciones. Al igual que la conocida vista de tabla, los tres nuevos tipos de vista admiten la colaboración al más alto nivel con funciones como el uso compartido de vistas, las vistas privadas y la edición colaborativa de datos en tiempo real.

Numerosas mejoras en el App Builder y el Base Editor, como la disponibilidad universal de filtros complejos y **el nuevo tipo de columna de número de teléfono**, optimizan las funcionalidades existentes y satisfacen las necesidades de los clientes.

Esta mañana hemos actualizado SeaTable Cloud a la versión 6.0. Los autoalojadores que han podido utilizar una versión beta desde el 30 de septiembre ya pueden descargar la versión estable desde el conocido [Repositorio Docker](https://hub.docker.com/r/seatable/seatable-enterprise) de SeaTable Server. Como siempre, la lista completa de cambios puede consultarse en el [registro de cambios](https://cloud.seatable.io/dtable/view-external-links/c9124bcd934b47bc8f30/).

## AI-ready con automatizaciones de IA (beta)

Analizar textos, traducir manuscritos, extraer información de documentos, crear borradores basados en palabras clave y mucho más: las nuevas funciones de IA de SeaTable llevan la potencia de la IA moderna directamente a SeaTable.

Existen **funciones de IA dedicadas** para tareas estándar. Funciones como *Resumir*, *OCR*, *Extraer* y *Clasificar* facilitan al máximo el uso de la IA en los procesos empresariales. Basta con seleccionar la función y definir las columnas de entrada y salida. Las instrucciones detalladas, en caso necesario, pueden pasarse al modelo de IA a través de un indicador.

![Nuevas funciones de IA](new-ai-function.png)

Si no se dispone de una función de IA específica, se puede utilizar la **función personalizada**. Con ella, el modelo de IA funciona únicamente sobre la base de su prompt individual. Basta con transferir información del conjunto de datos haciendo referencia a una columna entre llaves, por ejemplo: "Escriba una historia con 1000 palabras basándose en las palabras clave de {Palabras clave}"

Las nuevas funciones de IA están integradas en las automatizaciones de SeaTable y son igual de fáciles de crear, utilizar y gestionar, probablemente incluso más gracias al editor revisado. Por supuesto, también puede añadir funciones de IA a las reglas de automatización existentes para hacerlas aún más potentes.

### Despliegue de IA sin comprometer la protección de datos

SeaTable Cloud utiliza un **Gemma3** con 12.000 millones de parámetros como modelo de IA. Este Large Language Model (LLM) multimodal de Google funciona **en un servidor alemán** de Hetzner Online GmbH y es gestionado por los administradores de SeaTable Cloud. El intercambio de datos entre SeaTable Cloud y el modelo lingüístico está **cifrado**. Por lo tanto, sus datos no se envían a otro proveedor de IA ni al extranjero.

Todos los suscriptores de SeaTable Cloud Enterprise reciben **500 créditos de IA por miembro del equipo**. Los créditos de IA se calculan de tal forma que permiten realizar pruebas exhaustivas. Se requieren créditos adicionales para cargas de trabajo productivas. Se pueden proporcionar gratuitamente previa solicitud durante la fase beta.

**Los autoalojadores de SeaTable Server** también pueden alojar ellos mismos su LLM, pero no están obligados a hacerlo. **SeaTable AI**, un nuevo componente de SeaTable Server, se basa en LiteLLM y, por tanto, admite la conexión de una gran variedad de modelos y proveedores, incluidos todos los servicios LLM con una API compatible con OpenAI. SeaTable AI se despliega utilizando Docker o Docker Compose, como ocurre con el resto de componentes de SeaTable Server. En el [Manual del administrador](https://admin.seatable.com/) encontrará configuraciones de muestra para numerosos LLM populares.

### Perspectivas para un mayor desarrollo de la IA

Las funciones de IA de SeaTable 6.0 son beta y se mejorarán y ampliarán dinámicamente en los próximos meses. El trabajo en un **asistente de IA** y un **servidor MCP** está en pleno desarrollo. Pronto estarán disponibles otros modelos de IA para su selección en SeaTable Cloud. Además de los LLM alojados por la propia SeaTable, entonces también estarán disponibles los modelos de los conocidos proveedores **OpenAI, Anthropic, Meta y xAI**, así como los del proveedor europeo **Mistral**. Los administradores del servidor SeaTable también podrán configurar varios modelos de IA. Esto le permitirá utilizar el modelo óptimo para cada caso de uso.

El **seguimiento del uso** y la **gestión de autorizaciones** son otros puntos centrales del desarrollo. Nuestro objetivo: la máxima transparencia y control sobre el uso de los créditos de IA en SeaTable.

## Automatización más fácil que nunca

En SeaTable 6.0, **crear y gestionar reglas de automatización** es aún más fácil y cómodo. Un editor completamente revisado ofrece más claridad y funciones adicionales.

![Nuevo diseño del editor de automatización](new-automation-editor.png)

El editor de SeaTable 6.0 se extiende por todo el ancho de la pantalla y permite así **un nuevo diseño**: Todas las reglas existentes se encuentran en la parte izquierda, de forma análoga a las vistas. **Cambiar entre dos reglas** es ahora cuestión de un solo clic. La regla de automatización activa se encuentra en la zona central. La **configuración del disparador o de las acciones** se muestra dinámicamente en el lado derecho. Otro factor de comodidad es la **altura variable del panel del editor**. Esto significa que los nombres de las columnas y los datos de muestra permanecen visibles mientras trabaja en una regla de automatización.

El nuevo editor también satisface el deseo expresado con frecuencia de poder **agrupar y mover las reglas de automatización**. Además, las acciones pueden duplicarse en una regla.

## Tres plugins se convierten en vistas

Los tres plugins [Calendario]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}), [Galería]({{< relref "help/base-editor/ansichten/die-galerie-ansicht" >}}) y [Kanban]({{< relref "help/base-editor/ansichten/die-kanban-ansicht" >}}) han sido parte integral de SeaTable desde la versión 1.0. Ahora, después de 5 años, tienen una nueva forma: Los plugins de Calendario, Kanban y Galería se convertirán en **Vistas de Calendario, Kanban y Galería**. En SeaTable 6.1, le seguirá el [plugin de Línea de tiempo]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}).

La reimplementación de los plugins como vistas ofrece varias ventajas: Por un lado, facilita mucho su uso. **No es necesario instalar los plugins en una base**, ya que las vistas están disponibles inmediatamente. Por otra parte, los administradores de SeaTable Server apreciarán la integración: En el futuro tampoco será necesario actualizar los plugins por separado.

![Nueva vista del calendario](new-view-list-pinned.png)

Además, las nuevas vistas son muy superiores a los plugins anteriores en cuanto a funcionalidad: Las vistas de Calendario, Kanban y Galería pueden compartirse individualmente como una [vista compartida]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}}) o parte de una [autorización compartida personalizada]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}). La anterior necesidad de [compartir toda la base]({{< relref "help/startseite/freigaben/eine-base-an-eine-gruppe-freigeben" >}}) para trabajar juntos en un calendario o tablero Kanban ya no es necesaria. Las vistas de todo tipo también ofrecen **vistas privadas** opcionales que sólo el creador puede ver. Todas las vistas, a excepción de la de Big Data, también admiten **edición colaborativa en tiempo real**. Un cambio realizado por un usuario se muestra inmediatamente a los demás usuarios.

{{< warning headline="Atención" text="Con SeaTable 6.0, los tres plugins ya no pueden instalarse en las bases. En las bases en las que ya se utilicen los plugins, seguirán estando disponibles hasta nuevo aviso y podrán utilizarse sin restricciones. Sin embargo, nuestra recomendación es otra: ¡Aproveche las nuevas vistas! El cambio no podría ser más fácil. Los tres plugins ofrecen **migración con un solo clic**. Esto convierte una pestaña de un plugin en una vista del mismo tipo sin más esfuerzo." />}}

## Más flexibilidad en el App Builder

En el [App Builder]({{< relref "help/app-builder" >}}) de SeaTable 6.0, notará **el nuevo botón naranja más**. Puede utilizarlo para añadir un nuevo elemento a la navegación, sin importar en qué parte de su aplicación se encuentre. Al pulsar el botón se revela una innovación funcional: además de páginas y carpetas, ahora también puede insertar **enlaces directos a sitios web externos** en la navegación. Esto significa que un enlace a una política de privacidad o a una wiki externa ya no necesita estar incrustado en una página, sino que puede aparecer de forma destacada directamente en la navegación. Varios clientes nos habían pedido esta opción de diseño.

![Insertar enlace directo](new-direct-link-in-apps.gif)

Las otras mejoras en el App Builder también giran en torno al tema de la flexibilidad: Los ajustes de página de los [tipos de página]({{< relref "help/app-builder/seitentypen-in-universellen-apps" >}}) Calendario, Kanban, Galería y Línea de tiempo ahora también permiten **proteger columnas individuales de los cambios**. Todos los tipos de página relevantes ofrecen ahora esta funcionalidad.

Ha estado disponible en Base desde la versión 5.2 y ahora también lo está en App Builder: **filtros complejos**. Tanto los ajustes de datos como los ajustes de las columnas de enlace admiten ahora grupos de filtros. Los usuarios de una página de tabla ahora también pueden utilizar patrones de búsqueda con operadores lógicos AND y OR.

## Más funciones en la administración del equipo

La [administración del equipo]({{< relref "help/teamverwaltung" >}}) de SeaTable Cloud ha sido ampliamente revisada con la versión principal. Lo primero que llama la atención es la armonización del diseño de la administración de equipos con el de la página web. Sin embargo, las nuevas funciones son de mayor importancia para el uso:

- Configuración del SSO a través de SAML (sólo para los abonados Enterprise)
- Integración de un registro para las actividades del equipo (sólo para los abonados Enterprise)
- Integración de un registro para los inicios de sesión del equipo
- Envío de facturas por correo electrónico
- Gestión de múltiples métodos de pago


## Otras mejoras

La versión 6.0 introduce el tipo de columna 26 de SeaTable. **El nuevo tipo de columna Número de teléfono** facilita aún más la comunicación. Un clic en el icono de teléfono de una celda transfiere el número de teléfono a su aplicación de telefonía. En los teléfonos móviles, esto funciona sin ninguna configuración adicional. Lo mismo ocurre en el escritorio si se ha configurado un acceso directo al software de telefonía en el navegador.

![Columna-tipo-número-teléfono](new-column-type-phone-number.gif)

La [función de exportación]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}) admite la **exportación de datos archivados en el almacenamiento de Big Data** con SeaTable 6.0. Si activa la opción al exportar, SeaTable crea primero el archivo de exportación en formato DTABLE y le informa mediante una notificación cuando el proceso ha finalizado. A continuación, el archivo se descarga a través del gestor de archivos Base. Los datos del almacén de big data se guardan en formato binario en la carpeta "archivo" del fichero DTABLE. Por supuesto, un archivo DTABLE con Big Data puede volver a importarse fácilmente a SeaTable como cualquier otro archivo DTABLE.

La introducción de datos en [columnas de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) resulta más cómoda. Anteriormente, SeaTable requería la introducción de una fecha completa. Si se omitía una parte, por ejemplo el año o un cero a la izquierda, la entrada no era válida. Ahora ya no. "25-11-4" se interpreta correctamente como 2025-11-04. Y lógicamente, esto no sólo funciona para fechas en formato ISO.

¡Pruebe SeaTable 6.0! Estamos seguros de que quedará encantado.

{{< newsletter title="Manténgase informado" subtitle="" submit="Suscríbase ahora" >}}

Suscríbase a nuestro **boletín informativo** y no vuelva a perderse ninguna noticia sobre SeaTable!

{{< /newsletter >}}
