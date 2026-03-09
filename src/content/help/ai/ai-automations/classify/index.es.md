---
title: 'Clasificar entradas (Classify)'
description: 'Con la función de IA Classify, asigna automáticamente categorías a las entradas de su base SeaTable.'
weight: 4
url: '/es/ayuda/automatizacion-ia-clasificar-entradas'
seo:
    title: 'Automatización IA: Clasificar automáticamente entradas en SeaTable'
    description: 'Cómo clasificar automáticamente entradas en SeaTable: configurar una automatización IA con la función Classify — definir categorías y asignar textos automáticamente.'
---

La función de IA **Classify** analiza el contenido de una o varias columnas y asigna cada entrada a una categoría. El resultado se escribe en una columna de selección simple o selección múltiple. De esta manera, puede clasificar automáticamente los textos entrantes sin tener que leer cada entrada manualmente.

## Casos de uso típicos

- **Tickets de soporte**: Clasificar automáticamente las solicitudes como "Technical", "Billing", "General" o "Feature Request".
- **Comentarios y valoraciones**: Categorizar los comentarios de clientes por sentimiento (positivo, neutral, negativo).
- **Bandeja de entrada de correo electrónico**: Ordenar los mensajes entrantes por tema o urgencia.
- **Solicitudes de empleo**: Clasificar las cartas de presentación por área de especialización o nivel de experiencia.

## Requisitos previos

- Una tabla con al menos una **columna de texto** que sirva como entrada.
- Una **columna de selección simple** o **columna de selección múltiple** para el resultado.

{{< warning headline="Importante" text="Las categorías en las que la IA debe clasificar deben estar ya creadas como **opciones de selección** en la columna de selección simple o de selección múltiple. La IA solo puede asignar opciones existentes." />}}

## Guía paso a paso

### 1. Crear categorías en la columna de selección

Antes de configurar la automatización, cree todas las **categorías** deseadas como opciones en la columna de selección simple (o selección múltiple). Por ejemplo: "Technical", "Billing", "General", "Feature Request".

![Columna de selección simple con categorías configuradas](images/ai-automation-classify-options.png)

### 2. Crear una automatización y elegir un disparador

Cree una nueva regla de automatización como se describe en el artículo [Configurar una automatización IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Un disparador típico es **Cuando se añade una fila**, para que cada nueva entrada se clasifique inmediatamente.

### 3. Añadir la acción «Llamar a la IA»

Haga clic en **Añadir acción** y seleccione **Llamar a la IA**.

### 4. Seleccionar la función «Classify»

En la configuración de la acción, elija:

- **Tabla**: La tabla en la que la IA debe trabajar.
- **Función**: **Classify**

![Opciones de acción para la función Classify](images/ai-automation-classify.png)

### 5. Definir las columnas de entrada

Seleccione una o varias columnas cuyo contenido la IA debe analizar para determinar la categoría. La IA lee los textos de estas columnas y decide en función del contenido qué categoría se ajusta mejor.

### 6. Personalizar el prompt

En el campo del prompt, puede dar a la IA instrucciones adicionales sobre cómo debe clasificar. Esto es especialmente útil cuando los nombres de las categorías por sí solos no son suficientemente claros.

**Ejemplos de prompts:**

| Prompt | Efecto |
|---|---|
| *Clasifica la solicitud según el tema principal.* | Asignación simple por tema |
| *Elige "Technical" si se trata de mensajes de error o fallos de funcionamiento. Elige "Billing" si se trata de pagos o facturas. Todo lo demás es "General".* | Reglas claras para cada categoría |
| *Evalúa el sentimiento del texto: positivo, neutral o negativo.* | Análisis de sentimiento |

{{< warning headline="Consejo" text="Cuanto más precisamente describa en el prompt lo que significa cada categoría, más fiablemente clasificará la IA. Especialmente con categorías similares, una delimitación clara merece la pena." />}}

### 7. Definir la columna de resultado

Seleccione la [columna de selección simple]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) o la [columna de selección múltiple]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}) en la que se debe escribir el resultado.

- **Selección simple**: La IA selecciona exactamente una categoría.
- **Selección múltiple**: La IA puede asignar varias categorías simultáneamente.

### 8. Guardar y probar

Haga clic en **Guardar** y pruebe la automatización con una entrada cuya categoría sea obvia. Compruebe si la IA asigna la categoría esperada.

## Ejemplo de aplicación: Categorizar tickets de soporte

En su helpdesk, las solicitudes de soporte llegan diariamente a través de un formulario web. Cada solicitud contiene una **descripción** del problema. Desea que cada ticket se asigne automáticamente a una categoría para que sus colaboradores puedan trabajar con los tickets de forma filtrada.

**Configuración:**

- **Disparador**: Cuando se añade una fila
- **Función**: Classify
- **Columna de entrada**: Descripción
- **Prompt**: *Clasifica la solicitud de soporte. Elige "Technical" para errores, bloqueos y fallos de funcionamiento. Elige "Billing" para preguntas sobre pagos, facturas o suscripciones. Elige "Feature Request" para sugerencias de mejora. Todo lo demás es "General".*
- **Columna de resultado**: Categoría (selección simple con las opciones "Technical", "Billing", "Feature Request", "General")

En cuanto llega un nuevo ticket, la IA lo asigna automáticamente a la categoría correspondiente. Sus colaboradores pueden entonces filtrar por categoría y priorizar sus tickets.

## Consejos para buenos resultados

- **Mantenga el número de categorías manejable.** De cinco a diez categorías suelen funcionar bien. Con demasiadas categorías similares, la precisión disminuye.
- **Describa cada categoría en el prompt.** Especialmente con nombres de categorías ambiguos, una breve explicación ayuda a la IA en la asignación.
- **Use una selección simple** cuando cada entrada deba asignarse a exactamente una categoría. Use una selección múltiple solo cuando una entrada pueda pertenecer realmente a varias categorías.
- **Revise los primeros resultados.** Ajuste el prompt si la IA clasifica incorrectamente de forma repetida.

## Próximos pasos

- [Resumir textos (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Extraer información (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Acción IA personalizada (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
