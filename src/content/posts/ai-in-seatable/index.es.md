---
title: 'IA en SeaTable: procesamiento automático o preguntar directamente'
description: 'SeaTable ofrece dos vías para integrar la IA en su trabajo: automatizaciones que leen facturas, clasifican tickets y resumen textos, conforme al RGPD en nuestro servidor en Alemania. Y un chatbot de IA que entiende sus datos y responde a preguntas en lenguaje natural.'
date: 2026-03-17
lastmod: '2026-03-17'
url: '/es/ia-en-seatable-automatizaciones-y-chatbot'
seo:
    title: 'IA en SeaTable: automatizaciones y chatbot para sus datos'
    description: 'SeaTable ofrece dos vías para la IA: automatizaciones conformes con el RGPD en nuestro servidor en Alemania y un chatbot de IA que entiende sus datos y responde a sus preguntas.'
categories:
    - 'low-code-no-code'
tags:
    - 'Procesos informáticos'
    - 'Inteligencia artificial'
    - 'No Code & Low Code'
    - 'Seguridad informática y protección de datos'
color: '#ff3d33'
---

Imagine que abre su base de SeaTable con 2.000 entradas de proyectos. Pero en lugar de aplicar filtros, configurar vistas y escribir fórmulas, escribe:

> «¿Qué proyectos están atrasados? Agrúpalos por responsable.»

Y la IA responde. No con una suposición vaga, sino con los datos reales de su base. Y en cuestión de segundos. Esto no es ciencia ficción. Es posible ahora mismo con el nuevo plugin de chat con IA de SeaTable.

Pero empecemos desde el principio. Porque la IA en SeaTable es mucho más que un chatbot.

## Hasta ahora: automatizaciones de IA, los asistentes invisibles

Con SeaTable 6.0 introdujimos las automatizaciones de IA. El principio: usted define una tarea y la IA la ejecuta automáticamente en segundo plano. Fila por fila, sin que tenga que esperar activamente.

![Anlage einer neuen KI-Automationen in SeaTable](images/ai-automation-overview.png)

Hay cuatro funciones disponibles: **Summarize, OCR, Extract y Classify**. Además, existe una **Custom Function** con la que puede definir sus propios prompts.

![KI Funktionen in Seatable Automationen](images/automation-select-ai-function.png)

### ¿Qué significa esto en la práctica?

- **Procesamiento de facturas:** Las facturas entrantes se leen mediante OCR. El número de factura, la fecha, el importe y el remitente se registran automáticamente en las columnas correspondientes, sin necesidad de introducirlos manualmente.
- **Tickets de soporte:** Las consultas entrantes se analizan, categorizan y asignan al equipo adecuado. Antes de que una persona vea la solicitud, ya está clasificada.
- **Resumen de documentos:** Un informe de 20 páginas se condensa en pocos segundos a los puntos esenciales.
- **Clasificación multilingüe:** Ya sea en alemán, inglés o francés: la IA reconoce el idioma y clasifica el contenido correctamente.

### ¿Dónde se ejecutan estas automatizaciones?

En **nuestro propio servidor de IA en Alemania**, en el centro de datos de Hetzner. Operamos nuestro propio modelo de lenguaje, que se encarga del procesamiento. Sus datos no abandonan en ningún momento nuestra infraestructura europea.

Para organizaciones que valoran la conformidad con el RGPD y la soberanía de los datos (universidades, instituciones de investigación, sector público), esto es decisivo. Ningún dato fluye hacia OpenAI, Google u otros proveedores estadounidenses.

Los clientes Enterprise reciben créditos de IA incluidos en su suscripción.

## A partir de ahora: el chatbot de IA. Hable con sus datos

Las automatizaciones son potentes, pero trabajan según reglas fijas: una fila de entrada, un resultado de salida. Pero ¿qué ocurre cuando tiene una pregunta abierta? ¿Cuando no sabe qué filtro aplicar o cuando necesita un análisis sobre toda su base de datos?

Para eso existe, a partir de SeaTable 6.1, el **plugin de chat con IA** (Beta).

![AI Chat Plugin SeaTable](images/ai-chat-plugin.png)

### Cómo funciona

Abra el chat en su base y formule su pregunta en lenguaje natural. La IA conoce la estructura de su base (tablas, columnas, vínculos) y consulta de forma selectiva los datos relevantes. Sin exportaciones, sin copiar y pegar, sin necesidad de explicar la estructura de la tabla.

Algunos ejemplos:

- *«¿Cuántos deals abiertos tenemos por encima de 10.000 euros que no han tenido contacto en los últimos 30 días?»*
- *«Resume las consultas de soporte de la última semana y muestra los temas más frecuentes.»*
- *«Crea una entrada de seguimiento en la tabla de actividades para cada tarea atrasada.»*

Sí, el chatbot no solo puede leer, sino también **escribir**: crear filas, actualizarlas, vincularlas y eliminarlas. Todo directamente en su base.

### ¿Cómo es esto posible?

Detrás del chatbot se encuentra el **SeaTable MCP Server**. MCP significa Model Context Protocol, un estándar abierto que permite a los modelos de IA interactuar activamente con fuentes de datos. En lugar de copiar sus datos en el chat, la IA consulta de forma autónoma a través de MCP lo que necesita. En vivo, en tiempo real, siempre actualizado.

Esto diferencia fundamentalmente nuestro enfoque de soluciones en las que se exportan datos como CSV y se pegan en una ventana de ChatGPT. El chatbot trabaja directamente con su base, sin rodeos y sin pérdida de información.

### ¿Qué modelos se admiten?

El chatbot utiliza modelos de IA de alto rendimiento capaces de responder preguntas complejas y trabajar con sus datos en múltiples pasos. Actualmente admitimos:

- **Anthropic Claude** (Haiku y Sonnet)
- **OpenAI** (GPT-4o y GPT-4o mini)
- **Mistral** (Mistral Large y Mistral Small)

Usted aporta su propia clave API y paga los costes de tokens directamente al proveedor correspondiente. Esto es transparente: puede ver exactamente cuánto cuesta cada interacción y mantiene el control total.

## ¿Por qué dos vías en lugar de una?

Una pregunta legítima. ¿Por qué no ejecutar todo a través del chatbot?

La respuesta: porque diferentes tareas tienen diferentes requisitos.

| | Automatizaciones de IA | Chatbot de IA |
|---|---|---|
| **Tarea** | Definida: OCR, resumen, clasificación | Abierta: preguntas, análisis, búsqueda exploratoria |
| **Interacción** | En segundo plano, automática | Diálogo en tiempo real |
| **Datos** | Una fila como entrada | Toda la base como fundamento |
| **Modelo de IA** | Nuestro servidor en Alemania | Su modelo (Claude, OpenAI o Mistral) |
| **Soberanía de datos** | Máxima: los datos permanecen en nuestra infraestructura | Usted decide: los datos se envían al proveedor de IA elegido |
| **Costes** | Incluidos en la suscripción Enterprise | Costes de tokens con el proveedor de IA |

Ambas vías se complementan. Utilice las automatizaciones para tareas recurrentes que deben ejecutarse de forma fiable en segundo plano. Utilice el chatbot cuando tenga preguntas que no pueda responder con un filtro.

## Sus datos permanecen bajo su control

Independientemente de la vía que elija: el control y la seguridad son la máxima prioridad.

**Con las automatizaciones**, sus datos nunca abandonan nuestra infraestructura europea. El modelo de lenguaje se ejecuta en nuestro propio servidor en Alemania.

**Con el chatbot**, los datos se transmiten al proveedor de IA que usted haya elegido. Esto es técnicamente necesario para que el modelo pueda responder a sus preguntas. Pero usted decide qué proveedor es.

![Flujo de datos en el chatbot de IA](images/dataflow-ai-agent.png)

Y no solo eso: el plugin de chat con IA distingue automáticamente entre operaciones de lectura y acciones destructivas como eliminaciones o actualizaciones. Antes de que se modifiquen datos, el plugin solicita su confirmación: qué se va a cambiar exactamente y cuántas filas se ven afectadas. Puede aprobar una sola vez, permitir para toda la sesión o rechazar. También en el caso de conjuntos de resultados especialmente grandes, se solicita confirmación antes de que la IA procese miles de filas.

## Cómo empezar

### Automatizaciones de IA

Disponibles para todos los clientes Enterprise en SeaTable Cloud y para instalaciones propias a partir de la versión 6.0. Cree una nueva automatización en su base, seleccione una función de IA (Summarize, OCR, Extract, Classify o Custom) y defina la columna de entrada y la de salida. La automatización se ejecutará a partir de ese momento con cada nueva entrada.

Con SeaTable 6.1 pondremos las automatizaciones (y con ellas también las automatizaciones de IA) a disposición en menor escala también para los clientes Free y Plus.

Encontrará instrucciones detalladas en nuestra [sección de ayuda]({{< relref "help/ai/ai-automations" >}}).

### Chatbot de IA

A partir de SeaTable 6.1 podrá instalar el plugin de chat con IA (Beta) en su base. Introduzca su clave API (Claude, OpenAI o Mistral) en la configuración del plugin. Formule su primera pregunta. El chatbot reconocerá automáticamente la estructura de su base y responderá a su consulta.

## Perspectivas

Trabajamos continuamente en la ampliación de las funciones de IA en SeaTable:

- **Gestión mejorada de claves API:** Actualmente, la clave API se almacena en la configuración del plugin. Para una versión futura estamos desarrollando una solución centralizada y más segura para la gestión de claves API.
- **Seguimiento del uso de IA:** Una vista transparente de su consumo de tokens.
- **Asistente de IA general:** Un asistente que le permita interactuar con varias bases simultáneamente.

Las posibilidades de integrar la IA en su trabajo diario crecen rápidamente. Con SeaTable dispone de las herramientas para beneficiarse de ello, sin comprometer el control sobre sus datos.

{{< newsletter />}}
