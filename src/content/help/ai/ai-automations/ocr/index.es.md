---
title: 'Reconocimiento de texto en imágenes (OCR)'
description: 'Con la función de IA OCR, reconoce automáticamente texto en imágenes y documentos escaneados en su base de SeaTable.'
weight: 5
url: '/es/ayuda/automatizacion-ia-reconocimiento-texto-ocr'
seo:
    title: 'Automatización IA: Reconocimiento de texto (OCR) en SeaTable'
    description: 'Cómo reconocer texto en imágenes automáticamente en SeaTable: configurar una automatización IA con la función OCR — leer tarjetas de visita, facturas y documentos.'
---

La función de IA **OCR** (Optical Character Recognition) reconoce texto en imágenes y escribe el contenido reconocido en una columna de texto. Esto le permite convertir automáticamente documentos escaneados, fotos de tarjetas de visita o imágenes de facturas en texto que se puede buscar.

## Casos de uso típicos

- **Tarjetas de visita**: capturar automáticamente fotos de tarjetas de visita como texto.
- **Facturas y recibos**: convertir facturas escaneadas en texto legible.
- **Albaranes**: extraer texto de albaranes fotografiados.
- **Notas manuscritas**: digitalizar fotos de notas manuscritas.
- **Documentos**: hacer disponibles como texto contratos o formularios escaneados.

## Requisitos previos

- Una tabla con una [columna de imagen]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) o una [columna de archivo]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) que contenga las imágenes o documentos a reconocer.
- Una [columna de texto o columna de texto formateado]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) para el texto reconocido.

## Guía paso a paso

### 1. Crear una automatización y elegir un disparador

Cree una nueva regla de automatización como se describe en el artículo [Configurar automatización IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Un disparador típico es **Cuando se añade una fila** — de esta manera cada imagen recién subida se procesa automáticamente.

Alternativamente, puede usar **Cuando se modifica una fila** y definir la columna de imagen como columna supervisada. En este caso, el reconocimiento OCR se activa cada vez que se inserta una nueva imagen en la columna.

### 2. Añadir la acción "Llamar a la IA"

Haga clic en **Añadir acción** y seleccione **Llamar a la IA**.

### 3. Seleccionar la función "OCR"

En la configuración de la acción, elija:

- **Tabla**: la tabla en la que la IA debe trabajar.
- **Función**: **OCR**

![Ajustes de la acción con la función OCR seleccionada](images/ai-automation-ocr.png)

### 4. Definir la columna de entrada

Seleccione la columna de la cual la IA debe reconocer el texto. Puede usar una **columna de imagen** o una **columna de archivo** como columna de entrada. Con una columna de archivo, puede procesar por ejemplo PDFs o documentos escaneados.

{{< warning headline="Nota" text="Si una columna de imagen o archivo contiene varios archivos, solo se procesa el **primer archivo**. Idealmente, suba solo una imagen o documento por fila a la columna de entrada." />}}

### 5. Definir la columna de resultado

Seleccione la columna en la que se debe escribir el texto reconocido. Esta debe ser de tipo **Texto** o **Texto formateado**.

### 6. Guardar y probar

Haga clic en **Guardar** y suba una imagen de prueba con texto claramente legible a la columna de imagen. Después de unos segundos, el texto reconocido debería aparecer en la columna de resultado.

## Ejemplo de aplicación: digitalizar tarjetas de visita

Su equipo de ventas fotografía tarjetas de visita en ferias y sube las fotos a una tabla de SeaTable. La IA debe reconocer automáticamente el texto de la tarjeta de visita para que pueda buscar los datos de contacto.

**Configuración:**

- **Disparador**: Cuando se añade una fila
- **Función**: OCR
- **Columna de entrada**: Imagen de tarjeta de visita (columna de imagen)
- **Columna de resultado**: Texto reconocido (columna de texto)

En cuanto se crea una nueva entrada con una imagen de tarjeta de visita, la IA lee el texto de la imagen y lo escribe en la columna de resultado. Desde allí, puede seguir procesando los datos — por ejemplo, con una acción **Extract** posterior para extraer específicamente el nombre, la empresa y el número de teléfono.

{{< warning headline="Consejo" text="Combine OCR con la función **Extract** en una segunda acción dentro de la misma automatización. De esta manera, primero reconoce el texto y luego extrae la información relevante en columnas separadas en un segundo paso." />}}

## Consejos para buenos resultados

- **La calidad de la imagen importa.** Cuanto más nítida y con mayor contraste sea la imagen, mejor será el reconocimiento de texto. Las fotos borrosas o la mala iluminación pueden provocar errores.
- **El texto impreso funciona de forma más fiable que la escritura a mano.** El texto mecanografiado se reconoce casi sin errores. En la escritura a mano, la calidad depende de la legibilidad.
- **Mantenga la imagen recta.** Las imágenes muy distorsionadas o giradas pueden dificultar el reconocimiento.
- **Use formatos de imagen comunes.** JPG y PNG funcionan de forma fiable.

## Combinar OCR con Extract

La función OCR entrega el **texto reconocido completo** como texto continuo. Si desea extraer información específica individual (por ejemplo, nombre, dirección, número de factura), puede añadir una segunda acción con la función [Extract]({{< relref "help/ai/ai-automations/extract" >}}) en la misma automatización. De esta manera, el texto reconocido se estructura en columnas individuales en un segundo paso.

## Próximos pasos

- [Extraer información (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Resumir textos (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Acción IA personalizada (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
