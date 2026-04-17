---
title: 'Configurar una automatización IA'
description: 'Cree una automatización IA en SeaTable paso a paso — desde el disparador hasta la acción IA finalizada.'
weight: 2
url: '/es/ayuda/configurar-automatizacion-ia'
seo:
    title: 'Configurar una automatización IA en SeaTable — Guía paso a paso'
    description: 'Cómo crear una automatización IA en SeaTable: elegir un disparador, configurar la función IA, definir columnas de entrada y resultado, y probar la automatización.'
---

En esta guía creará una automatización con la acción **Ejecutar IA**. Una vez configurada, SeaTable procesará sus datos automáticamente mediante un modelo de IA — por ejemplo, para resumir textos, categorizar entradas o extraer información.

## Requisitos previos

- SeaTable (Cloud o Server) **versión 6.0** o superior
- Una base con una tabla que contenga datos de texto

{{< warning headline="Nota para clientes autoalojados" >}}

En **SeaTable Cloud**, el servidor de IA ya está integrado. SeaTable opera su propio modelo lingüístico (Gemma 3) en infraestructura GPU en Alemania — puede utilizar las automatizaciones IA de inmediato.

Si **autoaloja** SeaTable, debe operar su propio servidor de IA o configurar una conexión con un proveedor de IA en la nube. Para más información, consulte la [guía de instalación de SeaTable AI](https://admin.seatable.com/installation/components/seatable-ai/).

{{< /warning >}}

## Paso 1: Crear una regla de automatización

1. Abra su base y haga clic en {{< seatable-icon icon="dtable-icon-rule" >}} en el encabezado de la base, luego en **Reglas de automatización**.
2. Haga clic en **Añadir regla o carpeta** y seleccione **Añadir regla**.
3. Asigne a la automatización un **nombre** descriptivo, por ejemplo «Resumir solicitudes de soporte».

![Página de resumen de reglas de automatización](images/ai-automation-overview.png)

## Paso 2: Elegir un disparador

Haga clic en **Añadir disparador** y seleccione un disparador. Para las automatizaciones IA hay dos disparadores disponibles:

- **Cuando se modifica una fila** — la IA procesa la fila modificada inmediatamente
- **Cuando se añade una fila** — la IA procesa cada nueva entrada automáticamente

A continuación, seleccione la **tabla** y la **vista** en las que debe funcionar la automatización. Opcionalmente, puede definir **condiciones** para activar la automatización solo para determinadas entradas.

![Selección del disparador](images/automation-trigger-selection.png)

{{< warning headline="Nota" text="Los disparadores basados en tiempo (**A una hora programada** y **A una hora programada para registros que cumplen condiciones**) no admiten actualmente acciones de IA." />}}

## Paso 3: Añadir la acción IA

1. Haga clic en **Añadir acción**.
2. Seleccione **Ejecutar IA** en la parte inferior de la lista de acciones disponibles.

![Lista de acciones con la opción Ejecutar IA](images/automation-action-run-ai.png)

## Paso 4: Configurar la función IA

Tras seleccionar la acción **Ejecutar IA**, se abren a la derecha los **ajustes de la acción**. Configure lo siguiente:

### Tabla
Seleccione la tabla en la que debe trabajar la IA. Normalmente es la misma tabla que en el disparador.

### Función
Elija una de las cinco funciones IA disponibles:

| Función | Descripción | Uso típico |
|---|---|---|
| **Summarize** | Resume textos | Condensar descripciones largas |
| **Classify** | Asigna categorías | Categorizar solicitudes de soporte |
| **OCR** | Reconoce texto en imágenes | Leer tarjetas de visita, facturas |
| **Extract** | Extrae información específica | Extraer número de factura, fecha |
| **Custom** | Prompt personalizado | Traducir, evaluar, reformular |

![Menú desplegable con las cinco funciones IA](images/automation-select-ai-function.png)

### Columnas de entrada
Seleccione una o varias columnas cuyo contenido deba procesar la IA. Es el texto (o la imagen/archivo en el caso de OCR) que la IA recibe como entrada.

### Prompt
Para todas las funciones excepto OCR, puede introducir un **prompt** para controlar el resultado. Por ejemplo: «El resumen no debe superar dos frases y debe estar escrito en español.» Para OCR no es necesario ningún prompt — la IA reconoce el texto en la imagen automáticamente.

### Columna(s) de resultado
Seleccione la columna en la que debe escribirse el resultado de la IA. El tipo de columna debe coincidir con la función elegida — por ejemplo, una columna de texto para resúmenes o una columna de selección simple para clasificaciones.

## Paso 5: Guardar y activar

1. Haga clic en **Guardar** para guardar los ajustes de la acción.
2. La automatización está ahora activa y se ejecutará automáticamente la próxima vez que se produzca el evento disparador.

## Probar la automatización

Para probar la automatización de inmediato, active el evento manualmente:

- Para **Cuando se añade una fila**: cree una nueva fila con datos de prueba.
- Para **Cuando se modifica una fila**: modifique un valor en una columna supervisada.

A continuación, compruebe si la IA ha escrito el resultado en la columna de resultado. Puede consultar el estado y los posibles errores en el [registro de ejecución]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}}).

![Registro de ejecución de una automatización IA](images/automation-open-log.png)

## Problemas frecuentes

| Problema | Solución |
|---|---|
| La columna de resultado permanece vacía | Compruebe que la columna de entrada contiene realmente un valor. Las entradas vacías no producen ningún resultado. |
| Tipo de columna incorrecto | La columna de resultado debe coincidir con el resultado. Las clasificaciones necesitan una columna de selección simple; los resúmenes, una columna de texto. |
| La automatización no se activa | Compruebe que la automatización está activada y que la modificación se produce en la tabla y vista correctas. |

## Próximos pasos

Encontrará guías detalladas para cada función IA en estos artículos:

- [Resumir textos (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Clasificar entradas (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Reconocimiento de texto en imágenes (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
- [Extraer información (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Acción IA personalizada (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
