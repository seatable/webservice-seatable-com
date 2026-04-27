---
title: 'Conectar SeaTable con Claude Code'
description: 'Conecte Claude Code con su base de SeaTable a través del servidor MCP — explicado paso a paso.'
weight: 3
url: '/es/ayuda/conectar-agente-ia-con-claude-code'
seo:
    title: 'Conectar SeaTable con Claude Code — Configuración en 5 minutos'
    description: 'Cómo conectar Claude Code con su base de SeaTable a través del servidor MCP: crear un token API, añadir el servidor MCP por CLI y hacer su primera pregunta.'
---

En esta guía, conectará Claude Code con su base de SeaTable. Una vez configurado, podrá hacer preguntas a Claude sobre sus datos y hacer que edite entradas directamente desde el terminal. La configuración tarda unos cinco minutos.

## Requisitos previos

- Una cuenta de SeaTable Cloud con al menos una base
- Claude Code (instalable mediante `npm install -g @anthropic-ai/claude-code`, detalles en [docs.anthropic.com](https://code.claude.com/docs/en/overview))
- Una cuenta de Anthropic (necesaria para usar Claude)

## Paso 1: Crear un token API en SeaTable

El token API le da a Claude acceso a una base específica. Usted decide si Claude solo puede leer o también escribir datos.
Para obtener instrucciones sobre cómo crear un token API, consulte el artículo [Crear un token API]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}).

{{< warning headline="Guarde su token de forma segura" >}}

Un token API es válido indefinidamente y debe tratarse como una contraseña. Si lo pierde o se expone accidentalmente, puede eliminar el token API en cualquier momento y crear uno nuevo.

{{< /warning >}}

## Paso 2: Añadir el servidor MCP por CLI

Claude Code se configura a través de la línea de comandos. Abra un terminal y ejecute el siguiente comando:

```bash
claude mcp add seatable \
  --transport http \
  https://mcp.seatable.com/mcp \
  -H "Authorization: Bearer INSERTE-SU-TOKEN-API-AQUI"
```

Sustituya `INSERTE-SU-TOKEN-API-AQUI` por el token del paso 1.

Puede conectar varias bases al mismo tiempo. Ejecute el comando de nuevo para cada base usando un nombre único, por ejemplo `seatable-crm` y `seatable-proyectos` en lugar de `seatable`.

## Paso 3: Verificar la conexión

Inicie Claude Code y escriba el comando `/mcp`. Se mostrarán todos los servidores MCP configurados junto con su estado. Si la conexión es exitosa, verá **Status: connected** y **Auth: authenticated**.

![Conexión exitosa al servidor MCP de SeaTable en Claude Code](images/claude-code-connected-to-mcp-seatable-com.png)

Desde el menú `/mcp` también puede realizar otras acciones, como ver las herramientas disponibles, restablecer la conexión (**Reconnect**) o desactivar el servidor.

Ahora haga una primera pregunta de prueba:

> *«¿Qué tablas hay en mi base?»*

Claude consultará entonces la estructura de las tablas a través del servidor MCP y listará todas las tablas con sus columnas. Si esto funciona, la conexión está establecida.

## Hacer sus primeras preguntas

Ahora puede hacer preguntas a Claude sobre sus datos como si estuviera hablando con un colega. Aquí tiene algunos ejemplos para probar:

- *«¿Cuántas entradas tiene la tabla Contactos?»*
- *«Muéstrame todas las entradas donde el estado sea "Abierto".»*
- *«Resume los datos de la tabla Ingresos por mes.»*

Sus preguntas deben referirse a tablas y columnas que realmente existan en su base. Si no está seguro, simplemente pregunte primero a Claude sobre la estructura de la base. Conoce sus tablas y columnas y puede indicarle lo que está disponible.

No necesita escribir los nombres de tablas y columnas de forma exacta. Claude reconoce pequeños errores tipográficos y los corrige automáticamente. Escriba tranquilamente «Contactos» en lugar de «contactos» o «Proyectos» en lugar de «projects». Claude encontrará la tabla correcta.

## Próximos pasos

- [Ejemplos de uso de agentes de IA]({{< relref "help/ai/ai-agents/use-cases" >}})
- [Hacer buenas preguntas: cómo obtener las mejores respuestas]({{< relref "help/ai/ai-agents/good-questions" >}})
- [Solución de problemas de agentes de IA]({{< relref "help/ai/ai-agents/troubleshooting" >}})
- [Permisos y protección de datos para agentes de IA]({{< relref "help/ai/ai-agents/data-security" >}})
