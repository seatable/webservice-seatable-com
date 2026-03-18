---
title: 'Permisos y privacidad de datos'
description: 'Descubra cómo el plugin de chat con IA gestiona sus datos y qué mecanismos de seguridad existen para proteger su información.'
weight: 5
url: '/es/ayuda/plugin-chat-ia-permisos-y-privacidad'
seo:
    title: 'Plugin de chat con IA: permisos y privacidad de datos'
    description: 'Así protege el plugin de chat con IA sus datos: diálogos de confirmación, transparencia en el flujo de datos y control sobre el proveedor de IA.'
---

El plugin de chat con IA conecta sus datos de SeaTable con un modelo de lenguaje externo. Este artículo explica cómo funciona el flujo de datos, qué mecanismos de protección intervienen y cómo puede mantener el control sobre sus datos.

## ¿Cómo fluyen sus datos?

Cuando hace una pregunta en el chat con IA, el flujo de datos se desarrolla en cuatro pasos:

1. **Su pregunta** se envía al proveedor de IA seleccionado.
2. El plugin consulta los datos relevantes de su base.
3. **Los resultados de la consulta** se transmiten al proveedor de IA para que el modelo de lenguaje pueda evaluarlos.
4. El modelo formula una respuesta y la envía de vuelta al plugin.

Esto significa: los datos que el plugin consulta para responder a su pregunta se transmiten al proveedor de IA externo. Esto es técnicamente necesario, ya que un modelo de lenguaje solo puede procesar los datos que recibe.

## Elección del proveedor de IA

Usted decide qué proveedor y qué modelo utilizar. Las opciones disponibles son Anthropic (Claude), OpenAI y Mistral. Cada proveedor tiene sus propias políticas de privacidad de datos. Los grandes proveedores se comprometen contractualmente a que los datos procesados a través de su API **no se utilizan para entrenar modelos**. Aun así, revise las condiciones de uso actuales de su proveedor elegido.

## Confirmación antes de realizar cambios

El plugin distingue claramente entre operaciones de lectura y de escritura. Antes de ejecutar una acción destructiva (p. ej., modificar o eliminar filas), el plugin muestra un **diálogo de confirmación**. Este le informa sobre qué cambios se realizarán y cuántas filas están afectadas.

Tiene tres opciones:

- **Aprobar una sola vez**: solo se ejecuta esta acción concreta.
- **Aprobar para toda la sesión**: las acciones posteriores de este tipo se ejecutan sin nueva confirmación.
- **Rechazar**: la acción no se ejecuta.

También en el caso de grandes cantidades de resultados, el plugin solicita confirmación antes de procesar miles de filas. De este modo, mantiene el control en todo momento.

## Máximo control mediante autoalojamiento

Quien desee evitar que los datos se transmitan a proveedores externos puede alojar SeaTable de forma autónoma y combinarlo con un modelo de lenguaje local. En esta configuración, sus datos no abandonan en ningún momento su propia red.

## Información adicional

Encontrará una descripción detallada sobre la seguridad de los datos al utilizar la IA con SeaTable en el artículo [Permisos y privacidad de datos en agentes de IA]({{< relref "help/ai/ai-agents/data-security" >}}). Allí se tratan, entre otros temas, los permisos de los tokens API, las estrategias para minimizar la exposición de datos y el autoalojamiento en detalle.
