---
title: 'Visión general de todas las integraciones en y con SeaTable'
date: 2023-03-22
lastmod: '2023-07-19'
categories:
    - 'skripte-api-integrationen'
author: 'cdb'
url: '/es/ayuda/integraciones-seatable'
aliases:
    - '/es/ayuda/integrationen-seatable'
seo:
    title: 'Integraciones SeaTable: API, webhooks, automatización y más'
    description: 'Conozca todas las integraciones de SeaTable: API REST, webhooks, JS/Python, correo, Zapier, Make y plugins propios para flujos eficientes.'
---

Las integraciones amplían la forma de trabajar e interactuar con SeaTable. Por ejemplo, las integraciones le permiten acceder a sus datos dentro de SeaTable con otras herramientas y soluciones de software, o puede diseñar flujos de trabajo que automaticen ciertos pasos. También puede desarrollar sus propias aplicaciones o programas que utilicen SeaTable como backend.

Puede que ya se haya dado cuenta. No existe "una" integración SeaTable, sino que dependiendo del área de aplicación, existen otras integraciones disponibles. Este artículo le dará una visión general de las diferentes integraciones y posibilidades.

## Resumen de las integraciones disponibles

SeaTable ofrece actualmente cinco opciones de integración diferentes, que se presentarán con más detalle a continuación.

- Javascript y Python
- Integraciones en SeaTable
- API de SeaTable
- Webhooks
- Plataformas de automatización

## Scripts en SeaTable

SeaTable permite ejecutar scripts personalizados de JavaScript y Python en una base. Esto permite a los usuarios con cierta experiencia en programación automatizar pasos de trabajo o tareas recurrentes. Los scripts pueden iniciarse manualmente, mediante un botón o a través de la automatización.

## Integraciones en SeaTable

En una base, SeaTable ofrece la posibilidad de activar **integraciones de terceros**. Actualmente, dentro de esta integración sólo está disponible la integración con una cuenta de correo electrónico. Esta integración de correo electrónico permite enviar correos electrónicos desde SeaTable mediante automatizaciones o botones. Otra opción es activar la sincronización de correo electrónico, que hace que todos los correos electrónicos de la cuenta de correo electrónico estén disponibles en SeaTable.

## API de SeaTable

La API de SeaTable proporciona una interfaz universal a través de la cual puede interactuar con los datos de SeaTable utilizando cualquier software o lenguaje de programación. Por ejemplo, puede utilizar la API de SeaTable para escribir automáticamente en SeaTable datos capturados en otro software. O si desea construir un frontend personalizado para algunos datos de SeaTable, puede utilizar la API para acceder a los datos directamente sin la interfaz web.

## Webhooks

Los webhooks se configuran dentro de SeaTable para una Base a la vez. Una vez que se configura un webhook, SeaTable envía un mensaje a una URL de su elección cada vez que se realiza un cambio en esa base. En esta URL, el software recibe los webhooks y los procesa. Dependiendo de qué cambio se hizo en la Base, puede realizar una actividad de seguimiento correspondiente.

Un ejemplo típico de webhook sería el seguimiento del estado de pago de una factura o suscripción. Tan pronto como se establece una factura al estado _Pagado_ en SeaTable, otro software debe realizar una acción correspondiente. Usted podría implementar esto fácilmente con un webhook. Cada cambio en las facturas en SeaTable se envía a través de webhook al otro software y sólo reacciona al mensaje de estado que es relevante para usted.

Los webhooks se utilizan normalmente cuando no se desea consultar el estado de una información con regularidad, sino cuando se desea ser informado proactivamente cuando se producen cambios. Para consultas de estado regulares, la API de SeaTable suele ser la mejor opción.

## Plataformas de automatización

En la vida cotidiana, la gente suele trabajar no solo con un software, sino con muchas soluciones al mismo tiempo. Los contactos comerciales se almacenan en un CRM como Hubspot o Pipedrive, las citas y los correos electrónicos se almacenan en Google, los boletines se envían con [Mailchimp](https://mailchimp.com/) o Brevo(https://www.brevo.com/). A menudo, quieres que un evento en un software conduzca a una actividad en otro software. Así, si envías un nuevo boletín con Brevo, automáticamente envías una publicación en Facebook. O si alguien envía una solicitud de cita en su sitio web, que los datos de contacto se transfieran automáticamente a su CRM.

Es precisamente en estos casos en los que una de las muchas plataformas de automatización puede ayudarle. Estas te ayudan a conectar dos o más soluciones de software sin experiencia en programación y a reaccionar a determinados desencadenantes con determinadas acciones.

Actualmente, las siguientes plataformas de automatización ofrecen soporte para SeaTable:

- [Zapier](https://zapier.com/apps/seatable/integrations)
- [Make (antes Integromat)](https://www.make.com/en/integrations/seatable)
- [n8n](https://n8n.io/integrations/seatable/)
- [Locoia](https://www.locoia.com/connector-integrations/)
- [En](https://integrately.com/integrations/seatable)

## Desarrollo propio

¿Ha encontrado SeaTable a su gusto, pero le falta alguna que otra función? ¿Desea automatizar ciertas tareas e integrar SeaTable en sistemas existentes? Con SeaTable tiene todas estas posibilidades. La capacidad de integración y ampliación forma parte del ADN de SeaTable.

Los plugins del mercado de SeaTable se basan en el SDK en tiempo real de SeaTable. Con esto usted puede desarrollar sus propios plugins con poco esfuerzo. [Puede encontrar todos los detalles sobre el SDK de SeaTable en la documentación para desarrolladores](https://developer.seatable.com). Puede importar sus propios plugins a través del Gestor de Plugins.

La integración de SeaTable con otros sistemas es prácticamente ilimitada gracias a la potente API REST de SeaTable. Toda la información sobre la API de SeaTable se puede encontrar en [la documentación de la API de SeaTable](https://api.seatable.com).

Tanto para los plug-ins como para la integración, se utilizan lenguajes de programación conocidos, como JavaScript y Python. Sus desarrolladores pueden ponerse manos a la obra de inmediato.
