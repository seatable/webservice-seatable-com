---
title: 'Solución de problemas'
description: 'Soluciones para los problemas más frecuentes con el plugin de chat con IA en SeaTable.'
weight: 6
url: '/es/ayuda/plugin-chat-ia-solucion-de-problemas'
seo:
    title: 'Plugin de chat con IA: solución de problemas frecuentes'
    description: 'Soluciones para problemas frecuentes con el plugin de chat con IA: errores de clave API, respuestas ausentes y problemas con el plugin.'
---

Si el plugin de chat con IA no funciona como se espera, aquí encontrará soluciones para los problemas más frecuentes. Encontrará información general sobre la configuración en el artículo [Configurar el plugin de chat con IA]({{< relref "help/ai/ai-chat/setup" >}}).

## Problemas con la clave API

### Clave API no válida

Si el mensaje de error indica una clave API no válida, compruebe lo siguiente:

- Asegúrese de que la clave se haya introducido correctamente y no contenga espacios accidentales.
- Verifique si la clave API todavía está activa. Algunos proveedores desactivan las claves tras un determinado periodo de inactividad.
- Compruebe que el **proveedor** seleccionado en la configuración del plugin coincida con la clave API. Por ejemplo, una clave de OpenAI no funciona con el proveedor Anthropic.

### Saldo o cuota agotados

La mayoría de los proveedores de IA trabajan con un saldo prepago. Si ya no se generan respuestas, compruebe su saldo en el panel de control del proveedor correspondiente:

- [Anthropic Console](https://console.anthropic.com/)
- [OpenAI Platform](https://platform.openai.com/)
- [Mistral Console](https://v2.auth.mistral.ai/login)

## Respuestas ausentes o incorrectas

### La IA no encuentra los datos

Asegúrese de que los datos solicitados realmente existen en la base. Mencione en su pregunta el nombre exacto de la tabla y la columna para que la IA pueda identificar los datos correctos.

### Resultados imprecisos o erróneos

Formule su pregunta de la manera más precisa posible. Evite formulaciones vagas e indique concretamente qué tabla y qué columnas son relevantes. En tareas complejas, puede ser útil dividir la solicitud en varios pasos sencillos.

### Tiempo de espera agotado o sin respuesta

Las consultas muy extensas pueden provocar un tiempo de espera agotado. Simplifique la solicitud o limítese a una sola tabla. Tenga en cuenta también que los modelos más pequeños como Haiku, GPT-4o mini o Mistral Small pueden alcanzar sus límites en tareas complejas de varios pasos.

## Problemas con el plugin

### El plugin no se muestra

Compruebe si el plugin está instalado y activado en el gestor de plugins. Para ello, abra la sección **Plugins** en el encabezado de la base y busque **AI Chat**.

### El plugin no carga

Recargue la página en el navegador. Si el problema persiste, pruebe con otro navegador o borre la caché del navegador.

### Los ajustes no se guardan

Asegúrese de haber confirmado los ajustes con **Save** después de introducir la clave API. Sin guardar, los datos introducidos se pierden al cerrar el diálogo de configuración.

## Consejos generales

- Comience con una pregunta sencilla como "¿Qué tablas hay?", para verificar la conexión con el proveedor de IA.
- Si la IA ofrece resultados inesperados, pídale que explique su razonamiento.
- Divida las tareas complejas en varios pasos pequeños para obtener mejores resultados.
