---
title: 'Resumen de todos los tipos de columnas'
date: 2022-08-25
lastmod: '2024-03-18'
categories:
    - 'arbeiten-mit-spalten'
author: 'cdb'
url: '/es/ayuda/tipos-columna-overview'
aiases:
    - '/es/ayuda/uebersicht-alle-spaltentypen'
seo:
    title: 'Tipos de columna en SeaTable: guía rápida de funciones'
    description: 'Conozca los 26 tipos de columna en SeaTable: texto, número, archivo, selección, fórmulas y relaciones. Explicación breve y ejemplos prácticos.'
star: true
weight: 1
---

En SeaTable puedes guardar información y datos en una gran variedad de formatos.

- Además de información sencilla basada en texto (por ejemplo, palabras, números, cantidades de dinero), SeaTable también admite el almacenamiento de información compleja (por ejemplo, archivos, imágenes, texto formateado, incluidos elementos insertados).
- Con los campos de selección, puede dividir sus datos en categorías definidas y las funciones de validación integradas (por ejemplo, URL, datos de posición) garantizan que sus entradas tengan un formato uniforme y directamente evaluable.
- Con las fórmulas se pueden realizar operaciones aritméticas y con los enlaces se crean relaciones entre entradas de distintas tablas que permiten realizar potentes operaciones con la base de datos.

Conozca aquí los 26 tipos de columnas de SeaTables.

## Columnas con entrada de datos manual

A cada columna de la tabla se le asigna un tipo. El tipo de columna determina qué datos puede introducir en las celdas de la columna. Por ejemplo, no puede introducir archivos en un campo de texto. La columna de fecha, en cambio, obliga a introducir una fecha en el formato seleccionado.

### Texto

Símbolo {{< seatable-icon icon="dtable-icon-single-line-text" >}} **Texto**

Este tipo de columna almacena **texto** sin formato y es uno de los tipos de columna más básicos de SeaTable. El contenido de texto consiste en **letras**, **números** y **caracteres especiales**, así como **espacios**. Por lo tanto, las columnas de texto se utilizan a menudo para nombres y descripciones (cortas).

[Más información sobre la columna de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})

### Texto largo

Símbolo: {{< seatable-icon icon="dtable-icon-long-text" >}} **Texto largo**

En este tipo de columna puede guardar **textos más largos** con elementos insertados, como **imágenes** y **tablas**. También dispone de varias opciones de formato y estructuración para sus textos mediante el lenguaje de marcado Markdown. Por ello, la columna _Texto largo_ se utiliza a menudo para descripciones y documentación. Si para la recopilación de información resulta útil que los textos contengan elementos de estructuración y/o que el texto y las imágenes estén muy juntos, entonces este tipo de columna es ideal.

[Más información sobre la columna Texto largo]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})

### Número

Símbolo: {{< seatable-icon icon="dtable-icon-number" >}} **Número**

Las columnas numéricas almacenan información **numérica** y pueden utilizarse de muchas maneras para trabajar con números de todo tipo. La información numérica puede ser un **número**, un **porcentaje** o una **cantidad de dinero**. Además, las columnas numéricas permiten **calcular valores** que se pueden visualizar con fórmulas y [estadísticas]({{< relref "help/base-editor/statistiken" >}}). Sin embargo, las columnas numéricas no son adecuadas para almacenar cadenas de cualquier longitud y la entrada de letras es rechazada por SeaTable en este tipo de columna.

[Más información sobre la columna de cifras]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})

### Fecha

Símbolo: {{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} **Fecha**

Con la ayuda de la columna de fecha, puede introducir **horas** y **fechas** en sus tablas hasta el minuto. Ten en cuenta que las columnas de fecha siempre interpretan la información introducida como una fecha, de modo que las entradas que no puedan interpretarse como fechas siempre se descartan como no válidas.

[Más información sobre la columna de fechas]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})

### Duración

Símbolo: {{< seatable-icon icon="dtable-icon-duration" >}} **Duración**

La columna de duración es un tipo de columna numérica especializada para almacenar **medidas de tiempo, intervalos e intervalos**, por lo que puede registrar un periodo de tiempo al minuto o incluso al segundo. Por esta razón, la columna es especialmente adecuada, entre otras cosas, para registrar la duración de diversos acontecimientos. Al utilizar la columna, sin embargo, tenga en cuenta que las entradas no numéricas siempre se descartan como no válidas.

[Más información sobre la columna permanente]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})

### Selección única

Símbolo: {{< seatable-icon icon="dtable-icon-single-election" >}} **Selección única**

En una celda de una columna de selección única, puede seleccionar un **valor** de una lista de opciones definidas. Usted mismo crea la lista de opciones definidas por columna de selección única y puede adaptarla a circunstancias cambiantes en cualquier momento. Por lo tanto, la selección única es especialmente adecuada para categorizar y agrupar sus datos.

[Más información sobre la columna de selección única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})

### Selección múltiple

Símbolo: {{< seatable-icon icon="dtable-icon-multiple-selection" >}} **Selección múltiple**

Con una selección múltiple, puede seleccionar **cualquier número de valores** de una lista de opciones definidas. Al igual que con la selección simple, usted mismo crea la lista de valores posibles y la adapta a sus necesidades individuales. La selección múltiple es, por tanto, ideal para la búsqueda de palabras clave, también llamada etiquetado.

[Más información sobre la columna de selección múltiple]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}})

### Imagen

Símbolo: {{< seatable-icon icon="dtable-icon-picture" >}} **Imagen**

El tipo de columna Imagen almacena cualquier número de **archivos de** imagen en los formatos de archivo **BMP**, **GIF**, **ICO**, **JPG**, **PNG**, **SVG** y **TIF**. La columna de imagen es, por tanto, una columna de archivo restringida a formatos de archivo de imagen.

[Más información sobre la columna de imágenes]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}})

### Archivo

Símbolo: {{< seatable-icon icon="dtable-icon-file" >}} **Fichero**

El tipo de columna Archivo almacena cualquier número de archivos de **cualquier tipo**. SeaTable ofrece una función de vista previa para numerosos formatos de archivo de imagen.

[Más información sobre la columna de archivos]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}})

### E-mail

Símbolo: {{< seatable-icon icon="dtable-icon-email" >}} **E-mail**

Las columnas de correo electrónico son columnas de texto especializadas para capturar y almacenar **direcciones de correo electrónico** y permiten su uso directo con un clic del ratón. La columna de correo electrónico es especialmente útil para los formularios web. El uso de un campo de correo electrónico en lugar de una columna de texto garantiza que la entrada tiene la sintaxis de una dirección de correo electrónico válida. Además, las columnas de correo electrónico pueden utilizarse para enviar correos electrónicos a través de [botones]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) y [automatizaciones]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}).

Si necesitas información más detallada sobre la columna de correo electrónico, echa un vistazo a este [artículo]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}).

### URL

Símbolo: {{< seatable-icon icon="dtable-icon-url" >}} **URL**

Las columnas URL interpretan la información introducida como un **recurso** en la red local o en Internet y permiten el acceso directo mediante un clic. Dado que las entradas en este tipo de columna no se validan, en una celda puede almacenarse una dirección de Internet (por ejemplo, https://seatable.com) o una dirección IP (por ejemplo, 192.168.178.1).

[Más información sobre la columna URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})

### Casilla de verificación

Símbolo: {{< seatable-icon icon="dtable-icon-check-square-solid" >}} **Casilla**

Las casillas de verificación permiten recoger **información binaria**: Sí o No o marca _activada_ frente a _marca no activada_. No es posible introducir más datos. Por lo tanto, son muy adecuadas para marcar tareas como completadas, por ejemplo, es decir, para llevar un registro de si las filas cumplen una determinada condición de sí/no. Por esta razón, también puede hacer un uso excelente de las columnas de casillas de verificación para [filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}), [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) o [agrupar]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}).

[Más información sobre la columna de casillas de verificación]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}})

### Calificación

Símbolo: {{< seatable-icon icon="dtable-icon-rate" >}} **Calificación**

Una columna de calificación le permite **calificar** sus registros para darles un **rango** o **puntuación de calidad**. Puede seleccionar una escala de valoración del 1 al 10 y elegir entre diferentes colores y formas. Esto permite evaluar y puntuar los datos de forma rápida y sencilla para que todo el mundo lo entienda.

[Más información sobre la columna de calificación]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})

### Número de teléfono

Símbolo: {{< seatable-icon icon="dtable-icon-telephone" >}} **Número de teléfono**

SeaTable tiene su propio tipo de columna para números de teléfono. En comparación con una columna de texto normal, la columna de número de teléfono ofrece la ventaja de que puede **llamar a un número de teléfono** con un clic del ratón.

[Más información sobre la columna de número de teléfono]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

### Fórmula

Símbolo: {{< seatable-icon icon="dtable-icon-formula" >}} **Fórmula**

Con la ayuda de las fórmulas, puede **relacionar** diferentes valores de columnas de una fila y crear diferentes **funciones** basadas en el contenido de estas columnas. Entre otras cosas, puedes calcular con valores de tus tablas, modificar valores o relacionar valores de una misma fila.

¿Necesitas más información sobre la columna de fórmulas? Entonces echa un vistazo a este [artículo]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}). Como las fórmulas son una función muy compleja, en nuestro manual encontrará muchos otros artículos de ayuda. Haga clic [aquí]({{< relref "help/base-editor/formeln" >}}) y será redirigido a la página de resumen.

### Enlace a otros registros

Símbolo: {{< seatable-icon icon="dtable-icon-link-other-record" >}} **Enlace a otros registros**

En las celdas de este tipo de columna puede introducir cualquier número de **referencias a registros de otras tablas** de la base. La columna de enlace está pensada para asignar relaciones entre registros de diferentes tablas. La columna de enlace puede utilizarse para representar relaciones 1:n y n:1, así como relaciones n:m.

Para más información sobre el tipo de columna Enlace a otros registros, [haga clic aquí]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}).

### Fórmula para enlaces

Símbolo: {{< seatable-icon icon="dtable-icon-link-formulas" >}} **Fórmula para enlaces**

Con la fórmula para enlaces, puede **mostrar** datos de **tablas enlazadas** en su tabla actual y **relacionarlos** entre sí. Para el tipo de columna se dispone entonces de un total de cinco fórmulas diferentes, con las que también se pueden realizar cálculos estadísticos. El requisito previo para utilizar la columna es la existencia de al menos una columna del tipo **Enlace a otros registros** de su tabla.

[Más sobre la columna Fórmula para enlaces]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}})

### Colaborador

Símbolo: {{< seatable-icon icon="dtable-icon-collaborator" >}} **Colaborador**

En una columna de colaboradores, puede introducir cualquier número de **usuarios** que tengan al menos acceso de lectura a la base. Los usuarios de SeaTable sin acceso no pueden introducirse en la columna de colaboradores. Tampoco se permiten otras entradas. La columna de colaboradores es especialmente útil para la gestión de proyectos. Por ejemplo, si introduce tareas que deben completarse en una tabla, puede registrar las personas que realizan las tareas y la persona responsable en columnas del tipo Colaborador.

[Más información sobre la columna de colaboradores]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}})

### Botón

Símbolo: {{< seatable-icon icon="dtable-icon-button" >}} **Botón**

Con los botones puede **automatizar** el tratamiento de datos o la ejecución de determinadas acciones. Tenga en cuenta, sin embargo, que siempre tendrá que manejar los botones **manualmente**. Con la ayuda del botón que puede añadir a las filas de esta columna, se desencadenan determinadas acciones definidas de antemano. Por este motivo, este tipo de columna es especialmente adecuado para automatizar pasos del proceso.

Para más información sobre el botón y las acciones que pueden activarse en columnas de este tipo, consulte este [artículo]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}).

### Geolocalización

Símbolo: {{< seatable-icon icon="dtable-icon-location" >}} **Geolocalización**

En esta columna puede registrar **ubicaciones** y visualizarlas más tarde con el [complemento de mapas]({{< relref "help/base-editor/plugins/anleitung-zum-karten-plugin" >}}). Para ello, puede seleccionar la entrada con país y región o con latitud y longitud. Además, tiene la opción de encontrar un país o región mediante la función de búsqueda y añadirlo como entrada.

[Más información sobre la columna de geolocalización]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}})

### Firma digital

Símbolo: {{< seatable-icon icon="dtable-icon-rename" >}} **Firma digital**

Puede almacenar **firmas digitales** en una columna de firmas, que se guardan automáticamente en la gestión de archivos de su Base. Las firmas digitales son muy adecuadas para la captura de datos mediante **formularios web**, por ejemplo para que las solicitudes se firmen cómodamente en línea.

[Más información sobre la columna de firmas]({{< relref "help/base-editor/spaltentypen/die-signatur-spalte" >}})

## Tipos de columnas con recogida automática de datos

Además de los tipos de columnas en los que usted como usuario introduce datos, hay otros cinco tipos de columnas en SeaTable cuyo contenido SeaTable genera automáticamente. Estas columnas no pueden ser editadas manualmente por el usuario. Se utilizan principalmente con fines de documentación.

### Creador

Símbolo: {{< seatable-icon icon="dtable-icon-creator" >}} **Creador**

SeaTable documenta automáticamente el **nombre del usuario** que creó la fila en la columna del creador.

[Más información sobre la columna del creador]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})

### Fecha y hora de creación

Símbolo: {{< seatable-icon icon="dtable-icon-creation-time" >}} **Fecha y hora de creación**

SeaTable documenta automáticamente la **fecha y hora de creación de la fila** en esta columna. La fecha y la hora se muestran en el formato AAAA-MM-DD HH:MM.

[Más información sobre la columna Fecha y hora de creación]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})

### Último modificador

Símbolo: {{< seatable-icon icon="dtable-icon-creator" >}} **Último modificador**

SeaTable documenta automáticamente el **nombre del usuario** que realizó el **último cambio** en una entrada en la columna Último modificador. Dado que la columna registra automáticamente los cambios en las entradas, resulta muy adecuada, por ejemplo, como activador de automatizaciones, así como para filtros y ordenaciones.

[Más información sobre la columna Último modificador]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})

### Última modificación

Símbolo: {{< seatable-icon icon="dtable-icon-creation-time" >}} **Última modificación**

SeaTable documenta la **fecha y hora de la última modificación de una entrada** en la columna Última modificación. La fecha y la hora se muestran en el formato AAAA-MM-DD HH:MM. Dado que la columna registra automáticamente los cambios en las entradas, es muy adecuada como activador de automatizaciones, así como para filtros y ordenaciones.

[Más información sobre la columna Última modificación]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})

### Autonumeración

Símbolo: {{< seatable-icon icon="dtable-icon-autonumber" >}} **Autonumeración**

El tipo de columna Autonumeración crea un **número que aumenta automáticamente** para cada nueva fila. Este tipo de columna se utiliza siempre que se necesite un identificador único para cada registro.

[Más información sobre la columna Autonumeración]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}}).
