---
title: 'Desactivación de un webhook en caso de error'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/es/ayuda/desactivar-webhooks-errores'
aliases:
    - '/es/ayuda/deaktivierung-eines-webhooks-bei-fehlern'
seo:
    title: 'Desactivar webhooks por errores en SeaTable: guía fácil'
    description: 'Descubra cómo se desactivan los webhooks en SeaTable tras errores HTTP y cómo volver a activarlos para asegurar automatización fiable.'

---

Si se configura un webhook para una Base SeaTable, SeaTable envía una _solicitud POST_ a la URL de destino cada vez que se realiza un cambio. Normalmente, el sistema receptor devuelve un mensaje de estado en forma de [código de estado de tres dígitos](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes), que SeaTable procesa y desactiva el webhook si es necesario.

## Los códigos de estado HTTP más comunes

Existe toda una gama de códigos de estado, pero basta con conocer los más comunes:

- **200** - Con éxito
- **400** - Solicitud incorrecta
- **403** - Prohibido
- **500 - 511** - Errores del servidor

El código de estado más importante con diferencia es el 200, que indica que la solicitud se ha recibido y procesado correctamente. SeaTable considera correctos todos los códigos de estado del 200 al 299.

## SeaTable desactiva los webhooks en caso de error

Cuando SeaTable envía un webhook, SeaTable espera una respuesta en forma de dicho código de estado HTTP. En caso de error, el webhook se establece en estado _no válido_ y se interrumpe la ejecución. El momento en que esto ocurre depende del tipo de error:

| Error                           | Ejemplos                                                                                 | Desactivación                      |
| ------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------- |
| **Respuesta errónea o ausente** | Código de estado fuera del rango 200 a 299, sin respuesta en 30 segundos                 | tras cinco errores seguidos        |
| **Entrega imposible**           | Nombre no resoluble, conexión rechazada, error de certificado, URL de destino no pública | inmediatamente con el primer error |

Las redirecciones no se siguen: un código de estado como 301 o 302 cuenta como error. Una entrega correcta restablece el contador de errores.

![Webhook no válido](images/invalid-webhook.png)

{{< warning headline="Solo URL de destino públicas desde la versión 7.0.10" text="Desde la versión 7.0.10 de SeaTable, la URL de destino debe apuntar a una dirección pública. Los webhooks a direcciones internas no se entregan y se desactivan inmediatamente." />}}

## Las entregas fallidas no se reintentan

SeaTable no vuelve a enviar un webhook si la entrega falla. Los cambios realizados mientras un webhook está desactivado tampoco se entregan después. Si su sistema necesita datos completos, debería [sincronizar los datos con regularidad]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).

## Reactivar un webhook inactivo

Un webhook inválido puede reactivarse en cualquier momento. Cambie a la edición del webhook inválido haciendo clic en {{< seatable-icon icon="dtable-icon-rename" color="grey" >}} y guarde de nuevo el webhook sin realizar ningún cambio. El webhook volverá a estar activo inmediatamente.

Para evitar que se vuelvan a desactivar, el sistema receptor debe procesar los webhooks de forma fiable y devolver el código de estado 200 en un plazo de 30 segundos.
