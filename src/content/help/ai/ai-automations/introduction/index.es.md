---
title: '¿Qué son las automatizaciones de IA?'
description: 'Las automatizaciones de IA procesan datos en su base automáticamente — desde categorizar hasta resumir.'
weight: 1
url: '/es/ayuda/automatizaciones-ia-en-seatable'
seo:
    title: 'Automatizaciones de IA en SeaTable: procesar datos automáticamente'
    description: 'Las automatizaciones de IA de SeaTable categorizan, traducen y resumen sus datos automáticamente — conforme al RGPD en servidores en Alemania.'
star: true
---

Desde la versión 6.0, SeaTable ofrece acciones de automatización basadas en IA que pueden procesar sus datos automáticamente. Resumir textos, categorizar solicitudes de soporte, extraer datos de facturas o traducir contenido — todo esto ocurre directamente en su base, activado por las reglas de automatización que ya conoce de SeaTable. Sin plataforma de IA externa, sin seguimiento manual.

{{< youtube A1_LWaFWveM >}}

## ¿Cómo funcionan las automatizaciones de IA?

Las automatizaciones de IA son acciones dentro del sistema de automatización de SeaTable. Siguen el mismo principio que todas las demás automatizaciones: un **disparador** inicia una o más **acciones**. La diferencia es que las acciones de IA utilizan un modelo de lenguaje para comprender y procesar el contenido.

Un flujo de trabajo típico es el siguiente:

1. Se crea una nueva entrada en una tabla (disparador).
2. Una acción de IA lee el contenido de una columna específica — por ejemplo el texto de una solicitud de soporte.
3. El modelo de lenguaje analiza el texto y escribe el resultado en otra columna — por ejemplo la categoría "Problema técnico" o un resumen en tres frases.

Esto ocurre de forma totalmente automática en segundo plano. No necesita intervenir ni formular preguntas — la IA trabaja basándose en reglas según las especificaciones que usted definió en la automatización.

## ¿Qué puede automatizar la IA?

En SeaTable, usted crea una automatización con la acción Run AI y elige una de las cinco funciones disponibles:

- **Summarize**: Los textos largos, informes o notas se condensan automáticamente a lo esencial. Útil cuando una columna contiene descripciones detalladas y necesita un breve resumen en otra columna.
- **Classify**: Los textos entrantes se analizan y se asignan a una categoría. Ejemplo típico: las solicitudes de soporte se clasifican automáticamente como "Técnico", "Facturación" o "General" y se almacenan en una columna de selección única.
- **OCR**: El texto se reconoce y extrae de imágenes o documentos escaneados — por ejemplo de una foto de una tarjeta de visita o un albarán escaneado.
- **Extract**: Se extrae información específica de texto no estructurado — por ejemplo número de factura, fecha e importe de una factura.
- **Custom**: Para todos los casos que no encajan en las cuatro funciones estándar, usted define su propio prompt. Esto le permite hacer que la IA traduzca textos, redacte sugerencias de respuesta o evalúe contenido según sus propios criterios.

## Automatizaciones de IA vs. agentes de IA

SeaTable ofrece dos formas de hacer que la IA trabaje con sus datos. Ambas se complementan pero funcionan de manera fundamentalmente diferente:

**Las automatizaciones de IA** se ejecutan automáticamente en segundo plano, activadas por reglas. Son adecuadas para tareas recurrentes que deben ejecutarse de la misma manera para cada nueva entrada — por ejemplo categorizar cada solicitud de soporte entrante o resumir cada nueva nota.

**Los agentes de IA** trabajan de forma interactiva. Usted hace una pregunta, el agente responde. Esto es adecuado para análisis puntuales, consultas flexibles y tareas únicas — por ejemplo "¿Qué clientes no tuvieron facturación este mes?"

| | Automatizaciones de IA | Agentes de IA |
|---|---|---|
| **Disparador** | Automático (regla/evento) | Manual (su pregunta) |
| **Interacción** | Ninguna — se ejecuta en segundo plano | Diálogo en lenguaje natural |
| **Uso típico** | Categorizar, resumir, extraer | Consultar, analizar, editar |
| **Modelo de IA** | Servidor de IA propio de SeaTable (UE) | Proveedor externo (p. ej. Anthropic) |
| **Procesamiento de datos** | Completamente dentro de la UE | Los datos se transmiten al proveedor de IA |

Más información sobre los agentes de IA en el artículo [¿Qué son los agentes de IA?]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}).

## Protección de datos: IA hecha en Europa

Una ventaja clave de las automatizaciones de IA frente a los servicios de IA externos: **sus datos no salen de la UE.** SeaTable opera su propio servidor de IA con el modelo de código abierto Gemma-3-12B en infraestructura GPU en Hetzner en Alemania.

En términos concretos, esto significa:

- Sus datos no se transmiten a OpenAI, Google u otros proveedores estadounidenses.
- No se realiza entrenamiento con sus datos — el modelo está preentrenado y no aprende de sus entradas.
- El procesamiento cumple con el RGPD y está sujeto exclusivamente al derecho europeo.

Para organizaciones que trabajan con datos personales, documentos confidenciales o información comercial sensible, esta es una diferencia decisiva en comparación con soluciones de IA donde los datos fluyen hacia EE. UU.

## Disponibilidad

Las automatizaciones de IA están disponibles a partir de SeaTable versión 6.0. Los clientes Enterprise pueden utilizar las funciones sin coste adicional. Un cuota limitada estará disponible para los planes Free y Plus a partir de la versión 6.1.

## Próximos pasos

- Configurar automatizaciones de IA — guía paso a paso