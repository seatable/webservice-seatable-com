---
title: 'Exportar una base como archivo DTABLE'
date: 2023-01-11
lastmod: '2024-03-11'
categories:
    - 'import-von-daten'
author: 'kgr'
url: '/es/ayuda/exportar-base-archivo-dtable'
aliases:
    - '/es/ayuda/speichern-einer-base-als-dtable-datei'
seo:
    title: 'Exportar una Base como archivo DTABLE en SeaTable: instrucciones clave'
    description: 'Exporte su base SeaTable como archivo DTABLE para backups o transferencias: contenido completo, sin historial, observe el límite de tamaño.'
---

Puedes exportar una base como archivo DTABLE en cualquier momento y guardar así una copia de seguridad completa en tu dispositivo. Puedes descubrir cómo funciona y qué debes tener en cuenta en el siguiente artículo.

## Para exportar una base

![Base de exportación](images/Base-exportieren.png)

1. Vaya a la **página de inicio** de SeaTable.
2. Mueva el puntero del ratón hasta el nombre de la **base** que desea exportar y haga clic en el **icono de tres puntos** que aparece en el extremo derecho.
3. Seleccione la opción **Exportar**.

![Exportación de la base](images/export-base.png)

4. Decida si desea incluir los **Assets** (p. ej. imágenes y archivos) y la última **copia de seguridad de Big Data** en el archivo de exportación, activando o desactivando los interruptores.
5. Confirme con **Exportar**.

Dependiendo de la configuración de su navegador, la **descarga** se iniciará automáticamente o se le preguntará dónde desea guardar el archivo de exportación. Si es necesario, seleccione un **lugar de almacenamiento** adecuado y confirme la selección.

En cuanto su archivo con la extensión **.dtable** aparezca en la ubicación de almacenamiento especificada, la exportación de la base se habrá completado.

{{< warning  headline="Nota" >}}

Tenga en cuenta que el **archivo DTABLE** puede llegar a ser muy **grande** si ha hecho un uso extensivo de columnas de archivos e imágenes en la base exportada. En SeaTable Cloud se pueden exportar bases con un **tamaño máximo de hasta 100 MB**. Puede utilizar el [administrador de archivos]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) para **eliminar los archivos adjuntos** en las bases que superen este límite de tamaño para permitir la exportación.

{{< /warning >}}

## ¿Qué almacena un archivo DTABLE?

El archivo DTABLE exportado contiene el estado actual de su base incluyendo todos los

- Tablas y vistas,
- Filas, columnas y valores,
- Imágenes y archivos,
- Formularios web,
- Estadísticas,
- Guiones,
- Plugins y
- Aplicaciones.

{{< warning  headline="Atención"  text="Sin embargo, un archivo DTABLE **no** guarda el historial de la base. Las instantáneas, los comentarios, el contenido eliminado en la papelera de reciclaje y el registro no se incluyen en el archivo de exportación. Los datos del backend de Big Data tampoco se exportan al archivo DTABLE." />}}

## Restaurar una base a partir de un archivo DTABLE

Puede **importar** un archivo DTABLE a SeaTable como nueva base en cualquier momento. Puede obtener más información sobre este tema en el artículo [Creación de una base a partir de un archivo DTABLE]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei" >}}).
