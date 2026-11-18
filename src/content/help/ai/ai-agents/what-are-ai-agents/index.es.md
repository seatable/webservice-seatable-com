---
title: '¿Qué son los agentes de IA?'
description: 'Los agentes de IA acceden directamente a sus datos de SeaTable a través de MCP. Descubra cómo funciona y qué puede hacer con ello.'
weight: 1
url: '/es/ayuda/que-son-los-agentes-de-ia'
seo:
    title: '¿Qué son los agentes de IA y cómo funcionan con SeaTable?'
    description: 'Los agentes de IA se conectan directamente a sus datos de SeaTable a través del servidor MCP. Lea, escriba y analice sus datos en lenguaje natural — sin conocimientos de programación.'
---

Los asistentes de IA como Claude, ChatGPT o Copilot son herramientas potentes — pero tienen un problema fundamental: no conocen sus datos. Si desea hacer una pregunta sobre sus proyectos, clientes o inventario, primero tiene que exportar los datos, pegarlos en el chat y explicar a la IA qué significan las columnas. Esto es engorroso y propenso a errores.

**Los agentes de IA resuelven exactamente este problema.** Un agente de IA es un asistente de IA que puede acceder directamente a sus datos a través de una interfaz estandarizada. En SeaTable, esto se realiza mediante el **Model Context Protocol (MCP)** — un estándar abierto respaldado por toda la industria de la IA.

## Lo más importante en resumen

- El **servidor MCP oficial de SeaTable** (`https://mcp.seatable.com/mcp`) conecta ChatGPT, Claude Desktop, Claude Code, Cursor y otros asistentes compatibles con MCP con su base.
- El acceso se concede por base, solo lectura o lectura y escritura, según el token.
- El agente trabaja con los datos, no con la estructura: no crea ni borra tablas ni columnas.
- Gratuito y de código abierto (licencia MIT), para SeaTable Cloud e instalaciones autoalojadas.

## ¿Cómo funciona?

Cuando conecta un agente de IA a su base de SeaTable, ocurre lo siguiente:

1. Usted hace una pregunta en lenguaje natural, por ejemplo: *"¿Qué tareas están atrasadas?"*
2. El agente de IA reconoce que necesita datos de su base y los consulta a través del servidor MCP.
3. El servidor MCP lee las filas relevantes de SeaTable y las devuelve al agente.
4. El agente evalúa los datos y responde — de forma clara y precisa.

Todo esto toma solo unos segundos. Usted no nota nada, excepto que recibe una respuesta precisa.

## ¿Qué puede hacer un agente de IA con mis datos?

Eso depende de los permisos que usted otorgue. Con un **token de lectura**, el agente puede consultar, buscar y analizar sus datos. Con un **token de lectura y escritura**, puede además crear, modificar o eliminar entradas — pero solo después de su confirmación.

En términos concretos, esto significa:

- **Consultar**: "Muéstrame todos los clientes de Berlín con una facturación superior a 5.000 euros."
- **Analizar**: "¿Cuántas tareas se completaron esta semana? Agrupar por empleado."
- **Crear**: "Crea una nueva entrada en la tabla Contactos para Müller GmbH."
- **Modificar**: "Cambia el estado de todas las tareas atrasadas a 'Escalado'."
- **Vincular**: "Vincula el nuevo contacto con el proyecto 'Rediseño del sitio web'."

El agente reconoce automáticamente la estructura de su base — tablas, columnas, tipos de columnas — y utiliza los formatos correctos. También corrige errores tipográficos en los nombres de tablas o columnas de forma autónoma en la mayoría de los casos.

{{< youtube 5T4pWJgfOgc >}}

## ¿Cuál es la diferencia entre agentes de IA y automatizaciones de IA?

SeaTable también ofrece **automatizaciones de IA** — acciones automatizadas que involucran a la IA cuando ocurren ciertos eventos, por ejemplo para resumir textos o categorizar entradas. Estas se ejecutan en segundo plano basándose en reglas, sin ninguna intervención por su parte.

Los agentes de IA funcionan de manera diferente: son **interactivos**. Usted hace una pregunta, el agente responde. Usted da una instrucción, el agente la ejecuta. Es un diálogo — como con un colega que conoce su base de datos de memoria.

| | Automatizaciones de IA | Agentes de IA |
|---|---|---|
| **Disparador** | Automático (regla/evento) | Manual (su pregunta) |
| **Interacción** | Ninguna — se ejecuta en segundo plano | Diálogo en lenguaje natural |
| **Uso típico** | Resumir textos, categorizar | Consultar, analizar, editar datos |
| **Configuración** | Configurada en SeaTable | A través de un asistente de IA externo (p. ej. Claude) |

Ambos enfoques se complementan: las automatizaciones para tareas rutinarias recurrentes, los agentes para preguntas puntuales e interacción flexible.

## ¿Qué necesito para empezar?

- Una **cuenta de SeaTable Cloud** (o una instalación autoalojada)
- Un **asistente de IA** que soporte MCP — por ejemplo ChatGPT, Claude Desktop, Claude Code o Cursor
- Un **token API** para la base a la que el agente debe acceder

La configuración toma solo unos minutos. Hay guías paso a paso para [ChatGPT]({{< relref "help/ai/ai-agents/connect-chatgpt" >}}), [Claude Desktop]({{< relref "help/ai/ai-agents/connect-claude-desktop" >}}), [Claude Code]({{< relref "help/ai/ai-agents/connect-claude-code" >}}) y [Cursor]({{< relref "help/ai/ai-agents/connect-cursor" >}}).

## ¿Es seguro?

El agente de IA solo accede a la base para la que usted ha creado un token API. No a otras bases, no a su cuenta. A través del token, usted controla si el agente solo puede leer o también escribir.

Es importante saber: cuando el agente consulta sus datos, los resultados se transmiten al proveedor de IA (por ejemplo Anthropic para Claude) para que el modelo de lenguaje pueda procesarlos. Los principales proveedores se comprometen a no utilizar los datos de la API para el entrenamiento de modelos. Si necesita el máximo control, puede autoalojar SeaTable y combinarlo con un modelo de lenguaje local.

Más información sobre seguridad y permisos en el artículo "Permisos y protección de datos para agentes de IA".