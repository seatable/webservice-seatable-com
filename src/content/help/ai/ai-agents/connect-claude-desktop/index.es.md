---
title: 'Conectar SeaTable con Claude Desktop'
description: 'Conecte Claude Desktop con su base de SeaTable a través del servidor MCP — explicado paso a paso.'
weight: 2
url: '/es/ayuda/conectar-agente-ia-con-claude-desktop'
seo:
    title: 'Conectar SeaTable con Claude Desktop — Configuración en 5 minutos'
    description: 'Cómo conectar Claude Desktop con su base de SeaTable a través del servidor MCP: crear un token API, añadir la configuración y hacer su primera pregunta.'
---

En esta guía, conectará Claude Desktop con su base de SeaTable. Una vez configurado, podrá hacer preguntas a Claude sobre sus datos y hacer que edite entradas directamente desde el chat. La configuración tarda unos cinco minutos.

## Requisitos previos

- Una cuenta de SeaTable Cloud con al menos una base
- Claude Desktop (disponible gratuitamente en [claude.ai/download](https://claude.ai/download/))
- Una cuenta de Anthropic (necesaria para usar Claude)

{{< warning headline="El plan gratuito es suficiente, pero requiere una configuración especial" >}}

La cuenta gratuita de Anthropic actualmente admite conexiones a servidores MCP personalizados, pero estos deben configurarse manualmente a través de archivos de configuración.

{{< /warning >}}

## Paso 1: Crear un token API en SeaTable

El token API le da a Claude acceso a una base específica. Usted decide si Claude solo puede leer o también escribir datos.
Para obtener instrucciones sobre cómo crear un token API, consulte el artículo [Crear un token API]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}).

{{< warning headline="Guarde su token de forma segura" >}}

Un token API es válido indefinidamente y debe tratarse como una contraseña. Si lo pierde o se expone accidentalmente, puede eliminar el token API en cualquier momento y crear uno nuevo.

{{< /warning >}}

## Paso 2: Configurar Claude Desktop

Claude Desktop utiliza un archivo de configuración JSON para integrar servidores MCP.

1. Abra Claude Desktop.
2. Vaya a **Settings** → **Developer**

![Añadir un servidor MCP personalizado en Claude Desktop](images/claude-add-custom-mcp.png)

3. El archivo `claude_desktop_config.json` se abre en su editor de texto.
4. Añada la siguiente configuración:

```json
{
  "mcpServers": {
    "seatable": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": [
        "C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx-cli.js",
        "mcp-remote",
        "https://mcp.seatable.com/mcp",
        "--header",
        "Authorization: Bearer INSERTE-SU-TOKEN-API-AQUI"
      ]
    }
  }
}
```

5. Sustituya `INSERTE-SU-TOKEN-API-AQUI` por el token del paso 1.
6. Guarde el archivo y reinicie Claude Desktop.

Puede conectar varias bases al mismo tiempo. Cree una entrada separada en `mcpServers` para cada base con un nombre único, por ejemplo `seatable-crm` y `seatable-proyectos`.

## Paso 3: Verificar la conexión

Después de reiniciar, verá la conexión a **SeaTable** en `Tools` dentro de Claude Desktop. Esto indica que el servidor MCP está conectado. Haga clic en él para ver las herramientas disponibles — debería encontrar herramientas de SeaTable como `list_tables`, `list_rows` o `query_sql`.

También puede comprobar el estado de la conexión en los ajustes.

![Estado de la conexión del servidor MCP](images/claude-mcp-connected.png)

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
