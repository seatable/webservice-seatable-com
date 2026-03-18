---
title: '¿Qué es el plugin de chat con IA?'
description: 'El plugin de chat con IA le permite chatear directamente con sus datos en SeaTable. Haga preguntas en lenguaje natural y la IA responde con datos reales.'
weight: 1
url: '/es/ayuda/plugin-chat-ia-en-seatable'
seo:
    title: 'Plugin de chat con IA en SeaTable: chatee con sus datos'
    description: 'El plugin de chat con IA en SeaTable permite la conversación natural con sus datos. Haga preguntas, analice datos y edítelos directamente en su base.'
star: true
---

El plugin de chat con IA (Beta) es una nueva extensión de SeaTable (a partir de la versión 6.1), con la que puede utilizar un chat basado en IA directamente en su base. Haga preguntas en lenguaje natural y la IA responde basándose en sus datos reales. No necesita software externo, ni un asistente de IA separado, ni ninguna configuración técnica. El chat funciona directamente en SeaTable.

## ¿Cómo funciona el plugin de chat con IA?

El plugin se basa en el **Model Context Protocol (MCP)**, el mismo estándar abierto que utilizan los [agentes de IA]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}). En segundo plano, el chat accede a sus datos a través del servidor MCP de SeaTable, lee tablas, columnas y entradas, y le proporciona respuestas precisas.

La diferencia clave con respecto a los agentes de IA: no necesita instalar ninguna aplicación externa como Claude Desktop o Cursor. El chat está disponible directamente como plugin en SeaTable. Abra el plugin, haga su pregunta y reciba la respuesta, todo dentro de su base.

## ¿Qué puede hacer el plugin de chat con IA?

El chatbot puede tanto **leer** como **escribir** sus datos. De este modo, puede, por ejemplo:

- **Consultar datos**: "¿Qué proyectos tienen una fecha límite en los próximos 7 días?"
- **Crear análisis**: "¿Cómo se distribuyen los tickets de soporte por categoría?"
- **Crear entradas**: "Crea un nuevo contacto con el nombre Müller GmbH."
- **Modificar datos**: "Cambia el estado de todas las tareas completadas a 'Archivado'."

## Modelos de IA compatibles

Para el plugin de chat con IA, usted aporta su propia clave API. Puede elegir entre los siguientes proveedores y modelos:

| Proveedor | Modelos |
|---|---|
| **Anthropic (Claude)** | Haiku, Sonnet |
| **OpenAI** | GPT-4o, GPT-4o mini |
| **Mistral** | Large, Small |

## Tres funciones de IA en SeaTable

SeaTable ofrece tres funciones de IA diferentes, que se distinguen fundamentalmente en su modo de funcionamiento:

| | Automatizaciones de IA | Agentes de IA | Plugin de chat con IA |
|---|---|---|---|
| **Disponible desde** | Versión 6.0 | Versión 6.0 | Versión 6.1 (Beta) |
| **Activación** | Automática (regla/evento) | Manual (su pregunta) | Manual (su pregunta) |
| **Interacción** | Ninguna, se ejecuta en segundo plano | Diálogo en la herramienta de IA externa | Diálogo directamente en SeaTable |
| **Uso típico** | Categorizar, resumir, extraer | Análisis ad hoc, tareas complejas | Preguntas rápidas, editar datos |
| **Modelo de IA** | Servidor de IA propio de SeaTable (UE) | Proveedor externo | Proveedor externo (clave API propia) |
| **¿Se necesita software externo?** | No | Sí (p. ej., Claude Desktop, Cursor) | No |

Las [automatizaciones de IA]({{< relref "help/ai/ai-automations/introduction" >}}) son adecuadas para tareas recurrentes que deben ejecutarse en segundo plano basándose en reglas. Los [agentes de IA]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}) ofrecen la máxima flexibilidad a través de clientes MCP externos. El **plugin de chat con IA** cierra la brecha entre ambos: uso interactivo de la IA sin software externo, directamente donde se encuentran sus datos.

## Estado Beta

El plugin de chat con IA se encuentra actualmente en fase Beta. El alcance funcional y la interfaz de usuario pueden cambiar en futuras versiones.
