---
title: 'Acciones de automatización'
date: 2023-01-27
lastmod: '2025-11-11'
categories:
    - 'automationen'
author: 'kgr'
url: '/es/ayuda/acciones-automatizacion-seatable'
aliases:
    - '/es/ayuda/automations-aktionen'
seo:
    title: 'Acciones de automatización en SeaTable: guía completa'
    description: 'Descubra todas las acciones automáticas: correo, añadir registros, bloquear datos, avisos, ejecución de scripts y operaciones de datos en SeaTable Enterprise.'
weight: 6
---

Las **acciones automatizadas** representan uno de los dos componentes esenciales de las automatizaciones. Las acciones se activan mediante **eventos de activación** definidos. Dependiendo del [disparador]({{< relref "help/base-editor/automationen/automations-trigger" >}}), SeaTable puede realizar diferentes acciones de automatización. Este artículo ofrece una **visión general** de los distintos tipos de acciones automatizadas.

## Acciones de automatización disponibles

La última versión de SeaTable ofrece un total de 15 acciones de automatización diferentes entre las que elegir:

- Enviar notificación
- Enviar notificación de aplicación
- Enviar correo electrónico
- Añadir registro
- Bloquear registro
- Modificar registro
- Añadir enlaces
- Añadir registro a otra tabla
- Ejecutar script Python
- Llamar a la IA
- Gestionar citas en Google Calendar
- Ejecutar procesado de datos
- Convertir página a PDF
- Generar PDF a partir de un documento y enviarlo
- Archivo

## Añadir, duplicar, mover y eliminar acciones de automatización

Para añadir una acción, haga clic en **el botón grande con el símbolo más** y seleccione la acción correspondiente en la lista desplegable. Tenga en cuenta que las acciones disponibles difieren en función del activador.

![añadir acciones de automatización](images/automated-actions.jpg)

Si ya ha configurado acciones más complejas, como el envío de correos electrónicos, el procesamiento de datos o funciones de IA, también puede duplicarlas. Simplemente haga clic en los **tres puntos** y después en **Duplicar**. De este modo, sólo tendrá que realizar pequeños ajustes en estas acciones y ahorrará mucho tiempo.

![duplicar acciones de automatización](images/duplicate-automated-actions.jpg)

El orden de las acciones puede modificarse fácilmente **arrastrando y soltando**. Mueva el puntero del ratón sobre una casilla de acción, mantenga pulsado el botón izquierdo del ratón en la **zona de arrastre de seis puntos** y desplace la acción a la posición deseada. Esto le permite personalizar de forma flexible la secuencia de automatización.

![Mover acciones de automatización](images/move-automated-actions.gif)

Por supuesto, también puede eliminar las acciones que ya no sean necesarias. Para ello, haga clic en los **tres puntos** y después en **Eliminar**. Tenga en cuenta que las acciones automatizadas se eliminan **inmediata y permanentemente** y no se pueden restaurar.

![eliminar acciones automatizadas](images/delete-automated-actions.gif)

## Acción automatizada: Enviar notificación

Al definir "Enviar notificación" como acción automatizada, puede establecer una notificación a uno o varios usuarios. Los usuarios seleccionados recibirán una **notificación** cada vez que se active el disparador correspondiente. Esta acción de automatización está disponible **para todos los disparadores de automatización**.

Puede editar los **destinatarios** y el **contenido** de las notificaciones en cualquier momento en la **configuración** de la acción. Para los destinatarios, puede seleccionar específicamente **usuarios individuales** o usuarios en una columna específica del tipo [Colaborador]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), [Creador]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) o [Último modificador]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}) . Escriba el mensaje deseado en el campo de texto y trabaje con las referencias de columna entre llaves para insertar valores específicos.

![enviar una notificación mediante automatización](images/send-notification-action-settings.jpg)

Los usuarios pueden encontrar sus notificaciones a través del {{< seatable-icon icon="dtable-icon-notice" >}} **icono de campana** junto a su avatar en la esquina superior derecha.

![Notificación entrante](images/example-action-notification.png)

El artículo [Enviar notificaciones mediante automatización]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}}) recorre esta automatización utilizando un caso de uso específico.

## Acción de automatización: Enviar notificación de aplicación

Al definir "Enviar notificación de app" como acción automatizada, puede enviar una notificación a uno o varios usuarios de una app. Los usuarios seleccionados recibirán una **notificación** en la app cada vez que se active el disparador correspondiente. Esta acción de automatización está disponible **para todos los disparadores de automatización**.

En los **configuraciones** de la acción, puede definir a qué **app** y a qué **destinatarios** deben enviarse las notificaciones. Para los destinatarios, puede seleccionar específicamente **usuarios individuales de la app** o notificar a los usuarios de una columna específica del tipo **Colaborador, Creador o Último modificador**. Introduzca el **contenido** deseado de la notificación en el campo de texto. Utilice las referencias de columna entre llaves para insertar valores específicos.

![enviar notificación de aplicación mediante automatización](images/send-app-notification-action-settings.jpg)

Los usuarios de la app correspondiente pueden encontrar sus notificaciones a través del {{< seatable-icon icon="dtable-icon-notice" >}} **icono de campana** junto a su avatar en la esquina superior derecha.

![Comprobar notificaciones en la app](images/check-app-notifications.jpg)

## Acción de automatización: Enviar correo electrónico

Al definir "Enviar correo electrónico" como acción automatizada, puede enviar correos electrónicos predefinidos a uno o varios usuarios. SeaTable envía un **correo electrónico** a cada usuario seleccionado en cuanto se activa el disparador correspondiente. Esta acción de automatización está disponible **para todos los disparadores de automatización**.

Puede editar la **cuenta de correo**, el **asunto**, el **receptor**, el **mensaje** y los **adjuntos** del correo electrónico en cualquier momento en la **configuración** de la acción. Utilice referencias a columnas entre llaves para insertar determinados valores en campos de texto.

![definición de la acción de automatización: Enviar correo electrónico](images/send-email-action-settings.jpg)

El artículo [Enviar correos electrónicos mediante automatización]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}) recorre esta automatización utilizando un caso de uso específico.

## Acción de automatización: Añadir registro

Si define "Añadir registro" como acción automatizada, se añadirá una **nueva fila** a la tabla cada vez que se active el disparador correspondiente. Puede definir los valores exactos de cada columna individualmente por adelantado.

![Acción de automatización: Añadir registro](images/add-record-action-settings.jpg)

La acción de automatización "Añadir registro" está disponible actualmente para los siguientes **disparadores de automatización**:
- Cuando se modifica una fila
- Cuando se añade una fila
- A una hora programada

El artículo [Añadir registros mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}}) recorre esta automatización utilizando un caso de uso específico.

## Acción de automatización: Bloquear registro

Si define "Bloquear registro" como una acción automatizada, la **fila** que activó la automatización queda bloqueada para su edición. No puede realizar más ajustes para esta acción – debe configurar las condiciones para el bloqueo de fila en el **disparador**. Tenga en cuenta que ya no podrá **desbloquear** las filas bloqueadas sin derechos de administrador.

![definición de la acción de automatización: Bloquear una fila en la tabla](images/lock-record-action.jpg)

![bloqueo de una fila en una tabla activada por una automatización](images/example-locked-records.jpg)

La acción de automatización "Bloquear registro" está disponible actualmente para los siguientes **disparadores de automatización**:
- Cuando se modifica una fila
- Cuando se añade una fila
- A una hora programada para las entradas que cumplan determinadas condiciones

El artículo [Bloquear filas utilizando la automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}) recorre esta automatización utilizando un caso de uso específico.

## Acción de automatización: Modificar registro

Si selecciona "Modificar registro" como acción automatizada, las **filas** de la tabla se ajustan de acuerdo con los **valores** definidos previamente tras activarse el disparador. Puede definir un valor para cada columna que las filas adoptarán automáticamente tras el cambio.

![Acción automatizada: Modificar registro](images/modify-record-action-settings.jpg)

La acción de automatización "Modificar registro" está disponible actualmente para los siguientes **disparadores de automatización**:
- Cuando se modifica una fila
- Cuando se añade una fila
- A una hora programada para las entradas que cumplan determinadas condiciones

## Acción de automatización: Añadir enlaces

Si selecciona "Añadir enlaces" como acción automatizada, se creará un [enlace a otras entradas]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) en la columna correspondiente cuando se active el activador. En los **configuraciones** de la acción, puede especificar exactamente en qué condiciones se añade el enlace a la tabla.

![Acción de automatización: Añadir enlaces](images/add-links-action-settings.jpg)

La acción de automatización "Añadir enlaces" está disponible actualmente para los siguientes **disparadores de automatización**:
- Cuando se modifica una fila
- Cuando se añade una fila
- A una hora programada

El artículo [Enlazar entradas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}}) recorre esta automatización utilizando un caso de uso específico.

## Acción de automatización: Añadir registro a otra tabla

Si selecciona "Añadir registro a otra tabla" como acción automatizada, se creará una **fila en otra tabla** cuando se active el disparador. En los **ajustes** de la acción, puede definir valores individuales para cada columna que se asignan a las filas de la tabla seleccionada como parte de la automatización. También puede seleccionar columnas del mismo tipo en la tabla de origen para copiar las entradas de las filas en la otra tabla.

![Acción de automatización: Añadir una fila en otra tabla](images/add-record-to-other-table-action-settings.jpg)

La acción de automatización "Añadir registro a otra tabla" está disponible actualmente para los siguientes **disparadores de automatización**:
- Cuando se modifica una fila
- Cuando se añade una fila

El artículo [Añadir entradas en otras tablas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) recorre esta automatización utilizando un caso de uso específico.

## Acción de automatización: Ejecutar script Python

Si selecciona la ejecución de un script de Python como acción automatizada, el disparador pone en marcha un **script de Python** previamente definido. Puede crear o editar el script en cualquier momento en el [editor de scripts]({{< relref "help/skripte/allgemein/anlegen-und-loeschen-eines-skriptes" >}}) y luego seleccionarlo en los **ajustes** de la acción.

![Acción de automatización: Ejecutar script Python](images/run-python-script-action-settings.jpg)

La acción de automatización "Ejecutar script Python" está disponible actualmente para los siguientes **disparadores de automatización**:
- Cuando se modifica una fila
- Cuando se añade una fila
- A una hora programada

## Acción de automatización: Llamar a la IA

Si selecciona la ejecución de una función de IA como acción automatizada, el desencadenante llama a un **modelo de IA** que ejecuta una acción predefinida en la tabla. Puede configurar la acción exacta que se ejecutará en los **ajustes**. Dependiendo del tipo de función de IA, pueden ser necesarias **columnas de entrada**, **columnas de salida** y un **prompt**.

![definición de una acción de automatización: Ejecutar IA](images/run-ai-action-settings.jpg)

Puede hacer que se ejecuten las siguientes **funciones de IA** con una automatización:

- **Resumir**: Resume el texto de una o varias columnas. Puede controlar la longitud, el tono, el formato y el idioma del resumen personalizando la indicación.
- **Clasificar**: Clasifica los registros a partir de una o varias columnas. Puede personalizar las categorías y las reglas mediante el prompt. El resultado termina en una columna de [selección única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) o de [selección múltiple]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}).
- **OCR**: Extrae texto de una [columna de imagenes]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}). El contenido reconocido se escribe en la columna resultante de tipo [Texto o Texto formateado]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}).
- **Extraer**: Extrae información específica de una columna de tipo texto o número según sus necesidades. La información extraída se escribe en las columnas resultantes.
- **Personalizar**: Genera contenido basado en su requerimiento. Utilice {nombre de columna} entre llaves para insertar el valor de la columna de una fila.

![acciones que pueden ejecutarse utilizando un modelo de IA](images/run-ai-functions.jpg)

La acción de automatización "Llamar a la IA" está disponible actualmente para los siguientes **disparadores de automatización**:
- Cuando se modifica una fila
- Cuando se añade una fila
- A una hora programada

## Acción de automatización: Gestionar citas en Google Calendar

Si selecciona "Gestionar citas en Google Calendar" como acción automatizada, se creará o actualizará una cita de SeaTable en un calendario de Google cuando se active el disparador. Hay algunos requisitos que deben cumplirse para que esta acción funcione sin problemas:
- En primer lugar, debe [sincronizar su cuenta de Google Calendar con SeaTable]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/google-calender-synchronisieren" >}}).
- Deben existir dos [columnas de fecha]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) en una tabla, que definan el **inicio** y el **final** de las fechas.
- También necesita una [columna de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) en la que Google pueda escribir el **identificador del evento** para poder sincronizar las citas.

![Requisitos para gestionar eventos en Google Calendar](images/manage-events-in-google-calendar-part-1.png)

También puede realizar otros ajustes. Añada un **título**, una **descripción**, una **localización** y **participantes** al evento. Para ello, escriba los detalles en los **campos de texto** o trabaje con **referencias a columnas entre llaves** para insertar valores específicos de la tabla. Activando los **controladores**, podrá decidir si desea enviar notificaciones, si se trata de una videoconferencia y si los invitados pueden editar la cita, ver la lista de invitados e invitar a otros invitados.

![más ajustes para eventos en Google Calendar](images/manage-events-in-google-calendar-part-2.png)

La acción de automatización "Gestionar eventos en Google Calendar" está disponible actualmente para los siguientes **disparadores de automatización**:
- Cuando se modifica una fila
- Cuando se añade una fila

## Acción de automatización: Ejecutar procesado de datos

Si selecciona la ejecución de un procesado de datos como acción automatizada, el activador inicia una [operación de tratamiento de datos]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) predefinida en la tabla. Puede configurar la acción exacta a realizar en los **ajustes**. Dependiendo del tipo de operación, pueden ser necesarias **ciertas columnas de entrada y salida**.

![definición de una acción de automatización: Ejecutar procesado de datos](images/run-data-processing-action-settings.jpg)

Puede hacer que se ejecuten las siguientes **operaciones de tratamiento de datos** con una automatización:

- [Calcular delta]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calcular porcentaje]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})
- [Calcular clasificación]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Extraer nombre de usuario]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})
- [Comparar y copiar]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})

![Operaciones de procesamiento de datos que pueden ejecutarse mediante automatización](images/run-data-processing-available-operations.jpg)

La acción de automatización "Ejecutar procesado de datos" está disponible actualmente para los siguientes **disparadores de automatización**:
- A una hora programada

## Acción de automatización: Convertir página a PDF

Si selecciona "Convertir página en PDF" como acción automatizada, SeaTable **creará un documento PDF a partir del conjunto de datos** cuando se active el disparador y lo guardará en una [columna de archivos]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}). Para ello, seleccione una **plantilla** que haya creado previamente en el [plugin de diseño de página]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}). También puede definir el **nombre del archivo** en los ajustes de la acción.

![Crear PDF mediante automatización](images/convert-page-to-pdf-action-settings.jpg)

La acción de automatización "Convertir página en PDF" está disponible actualmente con el siguiente **disparador de automatización**:
- A una hora programada para las entradas que cumplan determinadas condiciones

## Acción de automatización: Generar PDF a partir de un documento y enviarlo

Si selecciona "Generar PDF a partir de un documento y enviarlo" como acción automatizada, SeaTable **creará un documento PDF** cuando se active el disparador y lo guardará en la [gestión de archivos]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}). SeaTable también puede enviarlo directamente por correo electrónico.

En los **configuraciones** de la acción, seleccione una **plantilla** que haya creado previamente en el **Complemento de diseño de informes** y asígnele un **nombre de archivo**. A continuación, active el control deslizante para seleccionar una **carpeta propia** en la que desee guardar el archivo. Si sólo desea generar el documento, puede finalizar la configuración en este punto.

![crear y enviar PDF a partir de un diseño de informe utilizando la automatización](images/generate-pdf-from-document-action-settings.jpg)

Si a continuación desea enviar el documento generado, active el control deslizante "Enviar a correo electrónico". Puede editar la **cuenta de correo**, el **destinatario**, el **asunto** y el **mensaje** del correo electrónico en cualquier momento en los **configuraciones** de la acción.

![crear y enviar PDF a partir de un diseño de informe mediante automatización](images/generate-pdf-from-document-and-send-action-settings.jpg)

La acción de automatización "Generar PDF a partir de un documento y enviarlo" está disponible actualmente con el siguiente **disparador de automatización**:
- A una hora programada

## Acción de automatización: Archivar

Puede utilizar la acción de archivo para [mover automáticamente filas al almacén de big data]({{< relref "help/base-editor/big-data/zeilen-ins-big-data-backend-verschieben" >}}). Por supuesto, la función big data debe estar activada en la base correspondiente. Como ya ha definido la **vista** y cualquier condición de filtro para las filas que se van a archivar en la configuración del activador, no puede realizar ninguna configuración para la acción en sí.

![Archivar filas mediante automatización](images/automated-action-archive.png)

La acción de automatización "Archivar" está disponible actualmente para los siguientes **disparadores de automatización**:
- A una hora programada
- A una hora programada para las entradas que cumplan determinadas condiciones