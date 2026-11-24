---
title: 'Modelos de IA compatibles'
description: 'El plugin de chat con IA es compatible con modelos de Anthropic, OpenAI y Mistral. Descubra qué modelo es adecuado para cada caso de uso.'
weight: 3
url: '/es/ayuda/plugin-chat-ia-modelos-compatibles'
seo:
    title: 'Modelos de IA compatibles en el plugin de chat de SeaTable'
    description: 'Descripción general de los modelos de IA compatibles en el plugin de chat de SeaTable: Claude, GPT, Mistral. Comparación, recomendaciones y costes.'
---

El plugin de chat con IA utiliza de forma predeterminada **SeaTable AI**, que ya está instalada. Además, es compatible con modelos de lenguaje de tres proveedores externos: **Anthropic**, **OpenAI** y **Mistral**. Usted elige qué modelo desea utilizar. Los costes por tokens se cargan directamente a su suscripción de SeaTable o se pagan al proveedor externo correspondiente de su modelo.

## SeaTable AI

La SeaTable AI preinstalada se basa en **Qwen 3.8 27B**, un modelo de pesos abiertos con 27 000 millones de parámetros desarrollado por Alibaba. El modelo de IA se aloja en centros de datos alemanes de Exoscale, el mismo proveedor que también facilita los servidores de SeaTable Cloud. Está diseñado para el razonamiento avanzado, la programación, la investigación, el procesamiento de documentos y las tareas complejas de varios pasos, y se publica bajo la licencia Apache 2.0.

Además, puede aportar su propia **clave API** para el plugin de chat con IA y conectar así un **modelo de IA externo en la nube**.

## Descripción general de los modelos de proveedores externos

Cada proveedor ofrece dos modelos: uno rápido y económico para tareas sencillas y otro más potente para análisis exigentes.

| Proveedor | Modelo | Puntos fuertes | Tendencia de coste |
|---|---|---|---|
| **Anthropic** | Claude Haiku | rápido, eficiente, ideal para consultas sencillas | económico |
| **Anthropic** | Claude Sonnet | potente, preciso en análisis complejos | medio |
| **OpenAI** | GPT-6 Luna | rápido, rentable, versátil | económico |
| **OpenAI** | GPT-6.1 Sol | muy potente, alta calidad de respuesta | más elevado |
| **Mistral** | Mistral Small | rápido, económico, buen rendimiento base | económico |
| **Mistral** | Mistral Large | potente, ideal para tareas complejas | más elevado |

## Configurar la clave API

Para poder utilizar un modelo externo en el plugin de chat con IA, necesita una **clave API** del proveedor correspondiente. Esta se crea directamente en la página web del proveedor:

- **Anthropic**: Cree una clave API en [console.anthropic.com](https://console.anthropic.com/).
- **OpenAI**: Cree una clave API en [platform.openai.com](https://platform.openai.com/).
- **Mistral**: Cree una clave API en [v2.auth.mistral.ai/login](https://v2.auth.mistral.ai/login).

En los tres proveedores debe registrar un **método de pago**. Los costes dependen del número de tokens consumidos y se facturan directamente por el proveedor.

## Recomendaciones según el caso de uso

### Consultas sencillas y respuestas rápidas

Para buscar valores individuales, resúmenes breves o preguntas de filtrado sencillas, los modelos económicos son los más adecuados: **Claude Haiku**, **GPT-6 Luna** o **Mistral Small**. Estos ofrecen respuestas rápidas a bajo coste.

### Análisis complejos y evaluaciones de datos

Si desea evaluar conjuntos de datos extensos, identificar patrones o realizar cálculos de varios pasos, opte por **Claude Sonnet**, **GPT-6.1 Sol** o **Mistral Large**. Estos modelos ofrecen resultados más precisos en tareas exigentes.

### Creación de textos y tareas de redacción

Para redactar correos electrónicos, informes o descripciones basándose en sus datos, se recomiendan **Claude Sonnet** o **GPT-6.1**. Ambos modelos generan textos de alta calidad lingüística.

## Costes y facturación

### Con SeaTable AI

Los tokens consumidos por la IA se convierten en **créditos de IA** y se descuentan de su saldo: 1 millón de tokens de entrada equivale a 500 créditos de IA y 1 millón de tokens de salida, a 1500 créditos de IA.

La cantidad de créditos de IA de la que dispone depende de la [suscripción de SeaTable]({{< relref "pages/prices" >}}) de su equipo. Con SeaTable Plus son **50 créditos de IA por usuario** al mes y con SeaTable Enterprise, **500 créditos de IA por usuario**.

Puede consultar en cualquier momento cuánto saldo le queda y cuánto ha consumido en la **barra de la columna lateral izquierda** del plugin de chat con IA.

![Créditos de IA consumidos y restantes en SeaTable AI](images/seatable-ai-credits.png)

### Con modelos de IA externos

Todos los costes por tokens se facturan directamente entre usted y el proveedor de IA correspondiente. SeaTable no cobra tarifas adicionales por el uso del plugin de chat con IA. Los precios exactos por token se encuentran en la página de precios del proveedor correspondiente.
