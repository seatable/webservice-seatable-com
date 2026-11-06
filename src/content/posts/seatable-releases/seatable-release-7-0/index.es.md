---
title: 'SeaTable 7.0: generación de páginas con IA, chat de IA listo para producción y automatizaciones más inteligentes'
description: 'SeaTable 7.0 gira en torno a la IA. Describa una página en lenguaje natural y el App Builder la generará como página HTML. El plugin de Chat IA deja atrás la fase beta y ahora utiliza de forma predeterminada un modelo alojado en Exoscale. Un SDK mejorado para páginas HTML, acciones de automatización nuevas y mejoradas, numerosas mejoras de seguridad y la retirada del generador de aplicaciones de consulta de datos completan esta versión.'
date: 2026-11-06
author: 'rdb'
url: '/es/seatable-release-7-0'
color: '#dc6165'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 7.0: el no-code da un salto adelante con la IA'
    description: 'SeaTable 7.0 pone la IA en primer plano: analice sus bases con IA y cree páginas HTML para sus aplicaciones con IA y el nuevo SDK para HTML.'
register:
    show: true
---

Con la versión 7.0, SeaTable da un gran paso adelante en inteligencia artificial. Dos novedades destacan especialmente: en el App Builder, ahora puede generar páginas HTML con IA simplemente describiendo qué debe hacer la página y qué aspecto debe tener. Y el plugin de Chat IA, presentado como beta en SeaTable 6.1, ya está listo para su uso en producción. Ambas funciones se apoyan en un modelo de IA más potente que, en SeaTable Cloud, se ejecuta en la infraestructura de nuestro socio Exoscale.

Pero SeaTable 7.0 ofrece mucho más que IA. El SDK para páginas HTML, que también utilizan las páginas generadas con IA, recibe cuatro mejoras solicitadas por nuestros usuarios. Las automatizaciones incorporan dos nuevas acciones para registros vinculados, y dos acciones existentes ganan en versatilidad. Entre bastidores, esta versión incluye numerosas correcciones de errores y mejoras de seguridad que responden al riesgo inmediato que suponen los bots impulsados por IA y los exploits generados automáticamente. Pequeñas mejoras en los formularios, las estadísticas y la autenticación de dos factores completan la versión. Y una función se retira: ya no es posible crear nuevas aplicaciones de consulta de datos, aunque las existentes siguen funcionando.

Esta mañana hemos actualizado SeaTable Cloud a la versión 7.0. Recomendamos a todos los administradores de sistemas autoalojados que hagan lo mismo, sobre todo por las mejoras de seguridad. La imagen Docker de SeaTable 7.0 está disponible para su descarga en [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise/). Como siempre, encontrará la lista completa de cambios en el [registro de cambios]({{< relref "pages/changelog" >}}#release-7).

## Generar páginas HTML con IA

SeaTable 7.0 le permite crear páginas HTML directamente en el App Builder mediante un chat de IA. Describa en lenguaje natural qué debe hacer la página y qué aspecto debe tener, y la IA la creará por usted. Para generar la página, la IA utiliza el SDK de SeaTable para páginas HTML (encontrará más información sobre el SDK en la siguiente sección). Por ello, una página generada con IA puede ser tan capaz como una escrita a mano.

Empezar es muy sencillo: haga clic en el icono “AI” de la barra izquierda. Un asistente le guiará por la configuración: asigne un nombre al proyecto, elija un estilo de interfaz, defina las fuentes de datos y los permisos de la página y describa la página que desea. A continuación, la IA genera una primera versión y la muestra en una vista previa. A partir de ahí, puede perfeccionar la página conversando con la IA hasta que haga exactamente lo que necesita. Con un clic en “Publicar”, la página se añade a su aplicación de SeaTable.

![Generar una página HTML con IA en SeaTable 7.0](AI-generated_HTML_page.png)

El chat conserva toda la conversación junto con cada versión de la página. Así, puede retomar el trabajo donde lo dejó en cualquier momento o volver a una versión anterior si un cambio no ha dado el resultado esperado. Las conversaciones y las páginas no publicadas se conservan durante 365 días. Y si prefiere ajustar una página por su cuenta, puede descargarla y editarla manualmente.

Si tiene curiosidad por saber qué ocurre entre bastidores, haga clic en el enlace “Proceso de pensamiento” del chat. Para cada paso, muestra el prompt del sistema, su entrada y el resultado devuelto por la IA. Una sección de estadísticas añade el tiempo y el número de tokens que ha consumido el paso.

![Proceso de pensamiento de la IA en el chat de IA](Thought_process_AI_chat.png)

En SeaTable Cloud, la generación de páginas se ejecuta en un potente modelo de pesos abiertos alojado por nuestro socio de infraestructura Exoscale, que también opera los servidores de SeaTable Cloud. Por lo tanto, sus prompts y los esquemas de sus bases no son procesados por ningún otro tercero. Los datos almacenados en sus bases nunca se envían al modelo de IA. Quienes autoalojen SeaTable pueden utilizar un modelo en la nube de uno de los principales laboratorios de IA o conectar un modelo autoalojado de su elección. SeaTable es compatible con todos los LLM que dispongan de un endpoint compatible con OpenAI.

{{< warning headline="Infraestructura de IA mejorada" >}}
El modelo de IA en el que se basa la generación de páginas HTML es Qwen 3.8 27B, un gran modelo de lenguaje multimodal con 27 000 millones de parámetros desarrollado por Alibaba. Está diseñado para el razonamiento avanzado, la programación, la investigación, el procesamiento de documentos y las tareas complejas de varios pasos, y se publica bajo la licencia Apache 2.0. Qwen 3.8 27B sustituye además al modelo de pesos abiertos [Gemma 4 E4B de Google DeepMind]({{< relref "posts/seatable-releases/seatable-release-6-0" >}}#despliegue-de-ia-sin-comprometer-la-protección-de-datos), que hasta ahora impulsaba las acciones de IA automatizadas de SeaTable.
{{< /warning >}}

## SDK mejorado para páginas HTML

El SDK de SeaTable para páginas HTML conecta sus páginas personalizadas con los datos de su base, tanto si las escribe usted mismo como si las genera con IA. A partir de los comentarios de los usuarios, SeaTable 7.0 añade cuatro mejoras que lo hacen considerablemente más potente.

En primer lugar, el SDK ahora trabaja con los nombres de los usuarios. Hasta ahora solo podía leer los datos de las filas de la base y no tenía forma de consultar nombres, por lo que las páginas únicamente podían mostrar nombres de usuario internos como `a1b2c3…@auth.local`. Ahora sus páginas pueden mostrar de un vistazo quién es quién.

En segundo lugar, el SDK puede identificar al usuario que ha iniciado sesión. Hasta ahora, una página no tenía forma de saber quién la estaba viendo. Con el nuevo método `getCurrentUser()`, las páginas pueden filtrar los datos según el usuario actual, por ejemplo, para mostrar a cada miembro del equipo únicamente sus propias tareas.

En tercer lugar, el SDK ofrece nuevos métodos para añadir y eliminar enlaces individuales en las columnas de enlace. Hasta ahora, el método `updateRow()` solo podía actualizar una columna de enlace en su conjunto, sustituyendo todos los enlaces existentes. Los nuevos métodos facilitan añadir una tarea a un proyecto, incluir una posición en un presupuesto o eliminar a un participante de un seminario sin tocar los demás enlaces.

En cuarto lugar, el SDK admite tres nuevas acciones: enviar un correo electrónico, enviar una notificación y ejecutar un script. Con ellas, las páginas HTML pueden enviar mensajes y ejecutar scripts con solo pulsar un botón, por ejemplo, para confirmar una reserva por correo electrónico directamente desde la página. Las cuentas de correo electrónico y los scripts que desee utilizar deben estar configurados en la base.

![Tres nuevas acciones en páginas HTML: enviar correo electrónico, enviar notificación y ejecutar script](Action_permissions_HTML_page.png)

## Plugin de Chat IA listo para producción

El plugin de Chat IA se presentó como función beta en [SeaTable 6.1]({{< relref "posts/seatable-releases/seatable-release-6-1" >}}#chat-con-inteligencia-artificial). Permite editar y analizar bases en lenguaje natural: crear registros, cambiar valores, vincular filas o analizar datos, en español, inglés, alemán, francés y otros idiomas. (No se admiten cambios en el esquema de la base).

Con SeaTable 7.0, el plugin deja atrás la fase beta. A partir de los comentarios de los usuarios, hemos mejorado tanto el plugin como el servidor MCP que utiliza. Las solicitudes son ahora considerablemente más eficientes, lo que reduce de forma significativa el consumo de tokens. También hemos actualizado la lista de modelos de IA en la nube compatibles.

El plugin también se ha vuelto mucho más fácil de usar. Durante la fase beta, tenía que proporcionar su propio token de API para un LLM compatible. En SeaTable Cloud, el plugin utiliza ahora de forma predeterminada nuestro propio modelo de IA alojado en Exoscale. Los tokens consumidos se convierten en créditos de IA y se descuentan de su saldo de créditos de IA: 1 millón de tokens de entrada equivale a 500 créditos de IA, y 1 millón de tokens de salida equivale a 1500 créditos de IA. Si prefiere no utilizar el modelo predeterminado, puede elegir otro de los modelos compatibles de los principales laboratorios de IA.

{{< warning headline="Próximamente para sistemas autoalojados" >}}
El plugin de Chat IA está disponible actualmente solo para clientes de SeaTable Cloud y SeaTable Dedicated. Lo pondremos a disposición de los sistemas autoalojados en los próximos meses.
{{< /warning >}}

## Reglas de automatización mejoradas

SeaTable 7.0 incorpora dos nuevas acciones de automatización, hace más versátiles dos acciones existentes y aporta más detalle al registro de automatización.

La primera acción nueva, “Añadir registro a una tabla vinculada”, funciona de forma muy parecida a la acción existente “Añadir registro a otra tabla”: crea un nuevo registro en otra tabla. Además, vincula el nuevo registro con el registro que ha activado la automatización. La segunda acción nueva, “Modificar registro vinculado en otra tabla”, complementa a la primera y modifica registros vinculados existentes en otras tablas. Por ejemplo, cuando cambia el estado de un registro, todos los registros vinculados dependientes pueden actualizarse de inmediato. Ambas acciones nuevas están disponibles con el disparador “Cuando se modifica una fila”.

![Nueva acción de automatización para registros vinculados en SeaTable 7.0](New_automated_actions.png)

La acción “Convertir página a PDF” genera un PDF a partir de una plantilla de diseño de página y lo guarda en una columna de archivo. En SeaTable 6.x solo estaba disponible con el disparador de hora programada. Ahora puede utilizarla con todos los disparadores que tienen contexto de fila: “Cuando se modifica una fila”, “Cuando se añade una fila” y “A una hora programada para las entradas que cumplan determinadas condiciones”. Esto abre la puerta a flujos de trabajo totalmente automatizados. Por ejemplo, un cliente envía una solicitud de presupuesto, SeaTable genera el presupuesto (con o sin ayuda de la IA) y este se envía al cliente por correo electrónico.

La acción “Gestionar citas en Google Calendar” ahora también puede eliminar citas de un calendario.

Por último, el registro de automatización es más informativo: además de la hora de activación, ahora también indica cuándo finalizó la ejecución.

## Y mucho más

Los formularios de varias páginas ahora pueden mostrar una barra de progreso para que quienes los rellenan vean cuánto les falta. Además, los mensajes de confirmación de envío ahora admiten texto enriquecido.

Las estadísticas de las aplicaciones de SeaTable se han reconstruido con D3.js, una biblioteca de JavaScript potente y muy extendida para la visualización de datos. Este cambio técnico allana el camino para gráficos más personalizables en el futuro. Las estadísticas de la base le seguirán en la próxima versión menor.

Al configurar la autenticación de dos factores, SeaTable ahora muestra la clave secreta para que pueda guardarla en su gestor de contraseñas.

Y una cosa más: las aplicaciones nativas de SeaTable para iOS y Android llegarán pronto. Las pruebas finales ya están en marcha. ¡Permanezca atento!

## Función retirada: aplicaciones de consulta de datos

Con SeaTable 7.0 hemos retirado el generador de aplicaciones de consulta de datos. Ya no es posible crear nuevas aplicaciones de este tipo. Las aplicaciones de consulta de datos existentes no se ven afectadas y siguen funcionando con normalidad.

Para las nuevas aplicaciones, utilice las aplicaciones universales. Pueden ofrecer las mismas funciones que las aplicaciones de consulta de datos, y muchas más. Encontrará cómo crearlas en las [páginas de ayuda sobre las aplicaciones universales]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}).
