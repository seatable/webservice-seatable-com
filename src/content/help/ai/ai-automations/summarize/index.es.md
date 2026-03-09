---
title: 'Resumir textos (Summarize)'
description: 'Con la función de IA Summarize, resuma automáticamente textos largos en su base SeaTable.'
weight: 3
url: '/es/ayuda/automatizacion-ia-resumir-textos'
seo:
    title: 'Automatización IA: Resumir textos automáticamente en SeaTable'
    description: 'Cómo resumir textos automáticamente en SeaTable: configurar una automatización IA con la función Summarize — controlar longitud, tono e idioma mediante el prompt.'
---

La función de IA **Summarize** resume automáticamente el contenido de una o varias columnas. Esto es especialmente útil cuando su tabla contiene descripciones largas, informes o notas y necesita un resumen compacto en una columna adicional.

## Casos de uso típicos

- **Solicitudes de soporte**: Comprimir descripciones detalladas de problemas de clientes en dos o tres frases.
- **Notas de reuniones**: Condensar actas extensas en un breve resumen.
- **Reseñas de productos**: Reducir reseñas largas a los puntos esenciales.
- **Candidaturas**: Resumir cartas de presentación o currículos en forma abreviada.

## Requisitos previos

- Una tabla con al menos una **columna de texto** o **columna de texto con formato** que sirva como entrada.
- Una **columna de texto** o **columna de texto con formato** para el resultado (el resumen).

## Guía paso a paso

### 1. Crear una automatización y elegir un disparador

Cree una nueva regla de automatización como se describe en el artículo [Configurar automatización IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Elija un disparador adecuado — por ejemplo **Cuando se añade una fila**, para que cada nueva entrada se resuma automáticamente.

### 2. Añadir la acción "Llamar a la IA"

Haga clic en **Añadir acción** y seleccione **Llamar a la IA**.

### 3. Seleccionar la función "Summarize"

En la configuración de la acción, elija:

- **Tabla**: La tabla en la que debe trabajar la IA.
- **Función**: **Summarize**

![Configuración de la acción para la función de IA Summarize](images/ai-automation-summarize.png)

### 4. Definir las columnas de entrada

Seleccione una o varias columnas cuyo contenido debe resumirse. Si selecciona varias columnas, la IA combina el contenido de todas las columnas en un único resumen.

### 5. Personalizar el prompt

En el campo **Summary prompt**, puede controlar cómo debe verse el resumen. Si deja el campo vacío, la IA crea un resumen estándar. Con un prompt, puede influir en la longitud, el tono, el formato y el idioma.

**Ejemplos de prompts:**

| Prompt | Resultado |
|---|---|
| *El resumen debe tener un máximo de 50 palabras.* | Resumen corto y conciso |
| *Resume el texto en tres puntos.* | Vista general en puntos |
| *Crea un resumen formal en español.* | Tono formal, idioma español |
| *Resume lo más importante en una frase.* | Resumen en una frase |

{{< warning headline="Consejo" text="Escriba el prompt en el idioma en el que espera el resultado. Un prompt en español generalmente producirá un resumen en español." />}}

### 6. Definir la columna de resultado

Seleccione la columna en la que se debe escribir el resumen. Esta debe ser de tipo **Texto** o **Texto con formato**.

### 7. Guardar y probar

Haga clic en **Guardar**. Pruebe la automatización activando el evento disparador — por ejemplo, cree una nueva fila con un texto más largo. El resumen debería aparecer en la columna de resultado en pocos segundos.

## Ejemplo de aplicación: Resumir solicitudes de soporte

Imagine una tabla en la que las solicitudes de soporte llegan a través de un formulario web. Cada solicitud contiene una **Descripción del problema** detallada en una columna de texto. Para el jefe de equipo, se debe generar automáticamente una **Descripción breve** para que pueda revisar las solicitudes más rápidamente.

**Configuración:**

- **Disparador**: Cuando se añade una fila
- **Función**: Summarize
- **Columna de entrada**: Descripción del problema
- **Prompt**: *Resume la solicitud de soporte en un máximo de dos frases. Menciona el problema principal y la función afectada.*
- **Columna de resultado**: Descripción breve

En cuanto un cliente envía el formulario y se crea una nueva fila, la IA escribe automáticamente una descripción breve en la columna de resultado.

## Consejos para buenos resultados

- **Indique la longitud deseada.** Sin indicación, la longitud del resumen puede variar. Un prompt como "máximo 50 palabras" garantiza resultados uniformes.
- **Utilice varias columnas de entrada** cuando el contexto esté distribuido en diferentes columnas. La IA tiene en cuenta todas las entradas.
- **Pruebe con datos reales.** Cree algunas filas de prueba con textos realistas para evaluar la calidad antes de poner la automatización en producción.

## Próximos pasos

- [Clasificar entradas (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Extraer información (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Acción de IA personalizada (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
