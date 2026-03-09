---
title: 'Acción de IA personalizada (Custom)'
description: 'Con la función de IA Custom, usted define su propio prompt y deja que la IA ejecute cualquier tarea sobre sus datos.'
weight: 7
url: '/es/ayuda/automatizacion-ia-accion-personalizada'
seo:
    title: 'Automatización IA: Acción de IA personalizada en SeaTable'
    description: 'Cómo crear automatizaciones de IA personalizadas en SeaTable: escriba su propio prompt y haga que los textos se traduzcan, reformulen o evalúen.'
---

La función de IA **Custom** es la más flexible de las cinco acciones de IA. Usted escribe su propio prompt y determina libremente lo que la IA hace con sus datos. Todo lo que no encaje en las cuatro funciones estándar (Summarize, Classify, OCR, Extract) puede implementarse con Custom.

## Casos de uso típicos

- **Traducir**: Traducir textos automáticamente a otro idioma.
- **Reformular**: Reescribir textos en otro tono o estilo (p. ej., formal, orientado al cliente, simplificado).
- **Sugerencias de respuesta**: Generar un borrador de respuesta basado en una consulta de cliente.
- **Evaluar**: Valorar textos según sus propios criterios en una escala (p. ej., relevancia, calidad, urgencia).
- **Generar**: Crear descripciones de productos, publicaciones en redes sociales o metatextos a partir de viñetas.
- **Corregir**: Corregir automáticamente errores ortográficos y gramaticales en textos.

## Requisitos previos

- Una tabla con al menos una columna cuyo contenido deba procesar la IA.
- Una **columna de Texto** o **columna de Texto formateado** para el resultado.

## Guía paso a paso

### 1. Crear una automatización y elegir un disparador

Cree una nueva regla de automatización como se describe en el artículo [Configurar la automatización de IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Elija el disparador adecuado para su caso de uso.

### 2. Añadir la acción "Llamar a la IA"

Haga clic en **Añadir acción** y seleccione **Llamar a la IA**.

### 3. Seleccionar la función "Custom"

En la configuración de la acción, elija:

- **Tabla**: La tabla en la que la IA debe trabajar.
- **Función**: **Custom**

![Ajustes de la acción con la función Custom seleccionada](images/ai-automation-custom.png)

### 4. Escribir el prompt

El prompt es el núcleo de la función Custom. Aquí formula la instrucción para la IA. Utilice **{Nombre de columna}** entre llaves para insertar el valor de una columna de la fila actual en el prompt.

**Estructura de un buen prompt:**

```
Traduce el siguiente texto al inglés.
Mantén el tono y el formato.

Texto: {Descripción}
```

En este ejemplo, `{Descripción}` se reemplaza en cada ejecución por el contenido real de la columna "Descripción".

![Campo de entrada del prompt con referencia de columna](images/ai-automation-custom-reference-column-by-name.png)

### 5. Establecer la columna de resultado

Seleccione la columna en la que se debe escribir el resultado de la IA. Esta debe ser de tipo **Texto** o **Texto formateado**.

### 6. Guardar y probar

Haga clic en **Guardar** y pruebe la automatización con una entrada. Compruebe si el resultado en la columna de resultado cumple con sus expectativas y ajuste el prompt si es necesario.

## Ejemplos de prompts para tareas comunes

### Traducir textos

```
Traduce el siguiente texto al inglés.
Mantén los términos técnicos y no los traduzcas.

Texto: {Descripción del producto}
```

### Generar una sugerencia de respuesta

```
Escribe una respuesta amable y profesional
a la siguiente consulta de cliente. La respuesta
no debe superar las cinco frases.

Consulta: {Consulta del cliente}
```

### Reformular un texto

```
Reformula el siguiente texto para que sea adecuado
para un comunicado de prensa. Utiliza un tono objetivo
y profesional.

Texto original: {Notas}
```

### Evaluar contenido

```
Evalúa el siguiente texto en una escala del 1 al 5
en cuanto a su urgencia. Responde solo con el
número y una breve justificación en una frase.

Texto: {Solicitud de soporte}
```

### Generar una descripción de producto

```
Crea una descripción de producto atractiva para una
tienda en línea basada en los siguientes puntos clave.
La descripción debe tener entre 50 y 80 palabras.

Nombre del producto: {Nombre}
Características: {Características}
Público objetivo: {Público objetivo}
```

### Corregir ortografía y gramática

```
Corrige los errores ortográficos y gramaticales en el
siguiente texto. No cambies el contenido ni las
formulaciones. Devuelve solo el texto corregido.

Texto: {Texto libre}
```

## Ejemplo de aplicación: Traducir descripciones de productos

Su tabla de productos contiene descripciones de productos en alemán. Para la tienda en línea internacional, necesita traducciones al inglés. En lugar de traducir cada descripción manualmente, la IA debe hacerlo automáticamente.

**Configuración:**

- **Disparador**: Cuando se añade una fila
- **Función**: Custom
- **Prompt**: *Traduce el siguiente texto en alemán al inglés. Utiliza un tono atractivo adecuado para una tienda en línea. Mantén los nombres de productos y las marcas tal como están. Texto: {Descripción DE}*
- **Columna de resultado**: Descripción EN (columna de Texto)

En cuanto se introduce un nuevo producto con descripción en alemán, la traducción al inglés aparece automáticamente en la columna de resultado.

## Consejos para buenos prompts

- **Sea concreto.** "Escribe un buen texto" produce resultados impredecibles. "Escribe una descripción de producto de 50 a 80 palabras en un tono amable" es mucho mejor.
- **Utilice referencias de columnas.** Con `{Nombre de columna}` puede combinar valores de varias columnas en un prompt para proporcionar contexto.
- **Defina el formato de salida.** ¿El resultado debe ser una sola frase? ¿Una lista? ¿Un número con justificación? Especifíquelo en el prompt.
- **Pruebe e itere.** Pruebe el prompt con diferentes entradas. Si los resultados no son adecuados, ajuste la formulación.
- **Escriba el prompt en el idioma de destino.** Si el resultado debe estar en inglés, escriba el prompt en inglés. Esto mejora la calidad de los resultados.

## Próximos pasos

- [Resumir textos (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Clasificar entradas (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Extraer información (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Reconocimiento de texto en imágenes (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
