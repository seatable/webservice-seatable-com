---
title: 'Paso 5: Certificado de asistencia'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/es/ayuda/paso-5-certificado-de-asistencia'
aliases:
    - '/es/ayuda/schritt-5-teilnahmebescheinigung'
seo:
    title: 'Paso 5: Certificado de asistencia en PDF por email'
    description: 'Descubra cómo crear y enviar por email certificados de asistencia en PDF para los estudiantes del curso usando SeaTable.'
---

Una vez finalizado el servicio, querrá redondear el proceso enviando a los participantes un correo electrónico final. Este correo electrónico puede tener diversos contenidos, como

- Una confirmación de participación
- Gracias por su participación
- Solicitud de comentarios
- Un código de descuento para el próximo curso
- …

## Crear y enviar la confirmación de participación

En esta sección utilizaremos SeaTable para generar una confirmación de participación en formato PDF y enviarla a los participantes por correo electrónico.

### Combinación de correspondencia con el plugin de diseño de páginas

SeaTable ofrece varios plugins que le permiten añadir vistas y funciones adicionales a sus datos. El plugin de diseño de páginas le permite crear documentos PDF - similar a una combinación de correspondencia en Microsoft Word.

Con este plugin, puede crear plantillas que contengan tanto contenido estático (como texto o logotipos) como datos dinámicos de su base. Cada fila de la tabla puede generar un documento individual.

{{< warning  headline="Versátiles posibilidades de aplicación"  text="El plugin de diseño de páginas ofrece muchas posibilidades: Además de certificados de participación, también puede crear facturas, certificados, circulares y mucho más." />}}

Para este curso ya hemos preparado una plantilla sencilla para crear una confirmación de participación. El nombre, el curso y la fecha del curso se insertan automáticamente, mientras que el resto del texto permanece inalterado.

Tómate unos minutos para explorar las posibilidades del plugin. Por ejemplo, prueba a añadir un logotipo o un gráfico a tu firma.

![](images/lvl2-page-design.png)

Si pulsa en `{{< seatable-icon icon="dtable-icon-download" >}} PDF` el PDF generado se guardará en su PC.

{{< warning  headline="Las plantillas siempre hacen referencia a una tabla"  text="Al crear una nueva plantilla, sólo se pueden utilizar datos de una tabla. Si necesita datos de una columna vinculada, debe incluirlos mediante columnas de consulta. Esta es la razón por la que en la tabla Registrations existen tres columnas de búsqueda ocultas. Estas columnas solo son necesarias para el plugin de diseño de páginas y, por tanto, pueden permanecer ocultas." />}}

### Envío por correo electrónico

Por supuesto, no querrás descargar el PDF manualmente y cargarlo de nuevo para enviarlo por correo electrónico. En su lugar, puede hacer clic en un botón del `Registrations` que ejecuta dos acciones sucesivamente:

- `{{< seatable-icon icon="dtable-icon-pdf" >}} Crear PDF y guardar en columna`
- `{{< seatable-icon icon="dtable-icon-email" >}} Enviar email`

La configuración de estas acciones ya debería resultarle familiar. Al crear el PDF, seleccione la plantilla deseada y la columna en la que debe guardarse el documento. Al enviar el correo electrónico, especifique la columna desde la que debe enviarse el archivo adjunto.

{{< warning  headline="Las acciones se ejecutan una tras otra"  text="No es un problema que el botón cree primero el archivo PDF y luego lo envíe. SeaTable espera a que se haya creado el PDF antes de enviar el correo electrónico." />}}

### Algunas palabras sobre la gestión de archivos

En SeaTable, los archivos y las imágenes no se almacenan directamente en las celdas, sino en el almacén central de datos de la base. Las celdas sólo contienen enlaces a los respectivos archivos. Esta gestión centralizada tiene varias ventajas:

- Los archivos pueden utilizarse varias veces sin tener que cargarlos de nuevo.
- Aunque borres un archivo de una celda, sigue estando disponible en la administración central hasta que lo borres definitivamente.

Tómese unos minutos para familiarizarse con la gestión de archivos de SeaTable. Encontrará más información en los artículos de ayuda enlazados al final de esta sección.

## Artículo de ayuda con más información

- [Guía del plugin de diseño de páginas]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}})
- [Guardar un documento PDF por botón en una columna]({{< relref "help/base-editor/schaltflaechen/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern" >}})
- [La columna de archivos]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}})
- [La gestión de archivos de una base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}})
