---
title: 'La columna de archivos'
date: 2022-11-16
lastmod: '2024-08-02'
categories:
    - 'dateien-und-bilder'
author: 'vge'
url: '/es/ayuda/columna-archivos-seatable'
aliases:
    - '/es/ayuda/die-datei-spalte'
seo:
    title: 'Columna de archivos en SeaTable – gestión de documentos'
    description: 'Descubre cómo usar la columna de archivos en SeaTable para subir, compartir, renombrar, eliminar y organizar tus documentos fácilmente.'
weight: 10
---

En una **columna de archivos** puede guardar uno o varios archivos y añadir así documentos a la fila correspondiente.

## Cómo crear una columna de archivos

![Crea una columna.](images/Wie-man-eine-Spalte-anlegt.gif)

1. Haga clic en el **símbolo \[+**\] situado a la derecha de la última columna de la tabla.
2. Dé un **nombre** a la columna en el campo superior.
3. Seleccione el tipo de columna **Fichero** en el menú desplegable.

## Cargar nuevos archivos

Puedes **cargar archivos** en la columna de archivos haciendo clic con el ratón en una **celda** y seleccionando el **símbolo más** que aparece. Puedes **arrastrar y soltar** archivos en la ventana recién abierta o hacer clic con el ratón para cargar archivos desde tu dispositivo.

![Carga de archivos adjuntos en una columna de archivos](images/upload-files-into-file-column.gif)

{{< warning  headline="Nota"  text="SeaTable admite archivos individuales de **hasta 200 MB de** tamaño. Puede cargar **cualquier tipo de archivo** en una columna de archivos, pero solo determinados documentos de Office e imágenes pueden mostrarse y editarse directamente en SeaTable." />}}

### Cargar varios archivos nuevos al mismo tiempo

![Cargar varios archivos adjuntos al mismo tiempo](images/upload-multiple-files-into-file-column.gif)

1. Haga clic en la **celda de** una columna de archivo.
2. Haz clic en el **símbolo más** que aparece.
3. Se abre una nueva ventana. Aquí puedes cargar archivos desde tu dispositivo mediante **arrastrar y soltar** o **hacer clic**.
4. Seleccione varios archivos a la vez seleccionando todos los documentos que desea cargar y cargándolos juntos.

{{< warning  headline="Conectado a la gestión de archivos" >}}

Los archivos que cargue localmente en una columna de archivos se guardarán en una **carpeta del** sistema a la que podrá acceder a través de la [gestión de archivos]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) de su Base.

{{< /warning >}}

## Añadir archivos existentes

Además de los archivos nuevos que subas localmente a la celda de una columna de archivos, también puedes añadir archivos existentes, que pueden proceder de **tres fuentes**:

- Últimos **subidos**: Aquí encontrarás los últimos archivos subidos que están guardados en el [gestor de archivos]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) Base.
- **Mis carpetas**: aquí tienes acceso a los archivos de tus propias carpetas, que puedes crear y rellenar en el [gestor de archivos]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}).
- **Seafile**: Aquí puede seleccionar los archivos de [las bibliotecas]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/eine-seafile-bibliothek-an-seatable-anbinden" >}}) Seafile que están conectados a su base.

![Añadir archivos existentes a una columna de archivos](images/Add-existing-files-to-a-file-column.png)

1. Haga clic en la **celda de** una columna de archivos y, a continuación, en el **símbolo más** que aparece.
2. Se abre una nueva ventana. En la navegación de la izquierda, seleccione la **fuente** desde la que desea añadir un archivo.
3. Haga clic en la **estructura de carpetas hasta llegar** al archivo deseado.
4. Seleccione el **archivo** e insértelo en la celda con **Enviar**.

## Descarga de archivos

![Descarga de archivos.](images/Herunterladen-von-Dateien.gif)

1. En la columna de archivos, **haga doble clic** en la celda que contiene los documentos que desea descargar.
2. Se abre una nueva ventana. Aquí se enumeran **todos los archivos** almacenados en la celda.
3. De este modo, se puede crear un **archivo único** descargar:
    - Sitúe el puntero del ratón sobre el documento y haga clic en el **icono de descarga** {{< seatable-icon icon="dtable-icon-download" >}}.
4. Así que puedes **varios archivos** descargar:
    - Haga clic en **Seleccionar.**
    - Seleccione la opción **Seleccionar todo** o **marque** las casillas situadas delante de los archivos.
    - A continuación, haga clic en **Descargar**.

Si desea descargar todos los archivos de una columna, abra el menú desplegable situado encima de la cabecera de la columna y seleccione **Descargar todo**.

![Descargar todos los archivos en una columna](images/Download-all-files.png)

A continuación, puede especificar **su propio nombre de archivo** y se mostrará el **número de archivos** que contiene la exportación.

![Ventana de diálogo para descargar todos los archivos](images/Download-all-files-dialog.png)

Si pulsa sobre los **tres puntos**, tiene dos opciones para guardar el archivo: Al **descargarlo**, se guarda en tu dispositivo un archivo zip del que puedes extraer todos los archivos. También puedes guardar los archivos **en Seafile**. Para ello, primero debes [conectar una biblioteca Seafile a tu Base]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/eine-seafile-bibliothek-an-seatable-anbinden" >}}).

## Renombrar archivos

![Cambiar el nombre de los adjuntos de una columna de archivos.](images/Datei-Spalte-Anhaenge-umbenennen.gif)

1. Abra la ventana **Todos los ficheros** **haciendo doble clic** en una celda de la columna Fichero.
2. Sitúe el puntero del ratón sobre el archivo cuyo nombre desea cambiar y haga clic en los **tres puntos**.
3. Seleccione la opción **Renombrar** e introduzca un nuevo **nombre de archivo**.

## Eliminar archivos

![Eliminar los archivos adjuntos.](images/Loeschen-von-Anhaengen.gif)

1. Abra la ventana **Todos los ficheros** **haciendo doble clic** en una celda de la columna Fichero.
2. De este modo, se puede crear un **archivo único** Borrar
    - Mueva el puntero del ratón sobre el archivo que desea eliminar y haga clic en los **tres puntos**.
    - Seleccione la opción **Borrar**.
3. Así que puedes **varios archivos** Borrar
    - Haga clic en **Seleccionar.**
    - Seleccione la opción **Seleccionar todo** o **marque** las casillas situadas delante de los archivos.
    - Haga clic en **Eliminar.**

{{< warning  headline="Nota" >}}

De este modo, los archivos **no** se eliminan de forma permanente. Sólo se [eliminan de forma permanente]({{< relref "help/base-editor/dateien/wie-man-dateien-dauerhaft-entfernt" >}}) cuando se borran los archivos en el [gestor de archivos]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) Base.

{{< /warning >}}

## Preguntas frecuentes

{{< faq "¿Se puede descargar un archivo durante una lectura compartida?" >}}Sí. Aunque un usuario sólo tenga **permiso de** lectura, puede descargar archivos.
{{< /faq >}}
{{< faq "¿Se pueden reproducir archivos de audio en SeaTable?" >}}No. Para poder reproducir **archivos de** audio, primero debes descargarlos.
{{< /faq >}}
{{< faq "¿Es posible cambiar el orden de los ficheros en una columna de ficheros?" >}}No, el orden **no puede** modificarse dentro de una columna de archivo. El documento cargado en primer lugar es el primero. Según el orden en que cargue los documentos, podrá determinar el orden dentro de la columna de archivos.

{{< /faq >}}
