---
title: 'Páginas de registro único en aplicaciones de SeaTable'
date: 2024-07-26
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/es/ayuda/pagina-registro-unico-apps-seatable'
aliases:
    - '/es/ayuda/seiten-vom-typ-einzelner-datensatz-in-universellen-apps'
    - '/es/ayuda/pagina-registro-unico-apps-universales'
seo:
    title: 'Página de registro único en SeaTable Apps – completo'
    description: 'Crea páginas con datos individuales y estáticos en SeaTable Apps, gestiona permisos y visualización avanzada para cada registro.'
weight: 11
---

Con el [tipo de página]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) de **registro único**, tiene la opción de diseñar una página con elementos estáticos, campos de tabla dinámicos, colores, marcos, etc. para presentar visualmente **los datos almacenados en una fila**.

Los usuarios de la aplicación pueden ver, buscar, explorar o incluso editar los registros de datos individuales en esta página, con la autorización pertinente. Este tipo de página es adecuada, por ejemplo, para mostrar los datos de una base de datos de empleados como perfiles personalizados.

![Página de registro único](images/Single-Record-Page-min.gif)

## Configuración de página

Si desea cambiar la configuración de una página, haga clic en el **símbolo de rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondiente en la barra de navegación.

![Cambiar la configuración de la página de la galería](images/Einstellungen-der-Galerieseite-aendern.png)

En la **configuración de la página**, puede seleccionar la **tabla** en la que se guardan los registros de datos individuales.

### Elementos estáticos

De forma similar a las [páginas a medida]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}), también puede añadir **elementos estáticos** a las páginas del tipo de registro único que se utilizan para diseñar la página y permanecen iguales en todos los registros de datos. Estos elementos son

- Texto
- Texto con formato
- Línea horizontal
- Imagen
- Contenedor
- Carta

![Elementos estáticos del tipo de página Registro único](images/Statische-Elemente-des-Seitentyps-Einzelner-Datensatz.png)

Para obtener información más detallada sobre las **opciones de configuración** de estos elementos, consulte [este artículo de ayuda]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}).

### Campos de la tabla

Todas las columnas de la tabla desde las que se pueden insertar datos en la página aparecen como campos de la tabla. El contenido de los campos depende de los registros de datos individuales de la tabla y cambia en función del registro.

Al igual que los elementos estáticos, cada campo de tabla también tiene su propia **configuración de elementos**. En primer lugar, seleccione si desea mostrar el **nombre** del campo que sirve de encabezamiento del registro. En caso afirmativo, puede establecer la **alineación** exacta, el **tamaño de la fuente**, el **peso de la fuente** y el **color de la fuente**.

También puede definir un **color de fondo** y un **marco** para cada campo de la tabla.

![Configuración de elementos de un campo de tabla en páginas de registro único](images/Element-settings-of-a-table-field-on-Single-Record-Pages-in-the-Universal-App.png)

Para todos los tipos de columnas basadas en texto y números, también tiene la opción de establecer el **tamaño de la fuente, el peso de la fuente, el color de la fuente y la alineación de los valores mostrados**.

También hay algunas características especiales para los siguientes tipos de columnas:

- Si pulsa sobre una dirección de correo electrónico en una **columna de correo**, se abrirá el cliente de correo electrónico instalado en su dispositivo (por ejemplo, Microsoft Outlook o Mozilla Thunderbird).
- Si pulsa sobre un enlace en una columna **URL**, se abrirá el sitio web correspondiente en una nueva pestaña de su navegador.
- Si hace clic en un símbolo de miniatura en una columna **Archivo**, el archivo se abrirá en un visor adecuado en una nueva pestaña de su navegador. Si tiene configurado un editor de Office en línea, también podrá abrir y editar documentos de Office directamente en el navegador.
- Con las **columnas de enlace**, todas los registros vinculados al registro de datos pueden visualizarse claramente en una tabla. Puede ajustar la anchura de las columnas y también ocultarlas a través de la configuración del elemento para que sólo se muestre la información esencial de los registros vinculados.

![Link columns on Single Record pages](images/link-columns-on-single-record-pages.png)

## Copiar, mover o eliminar elementos

Si desea copiar, desplazar o eliminar un elemento existente en su página, sólo tiene que utilizar los tres **símbolos** correspondientes situados en la esquina superior derecha del marco.

![Copiar, mover y eliminar elementos en páginas personalizadas](images/Copy-move-and-delete-elements-on-custom-pages.gif)

## Filtros preestablecidos y clasificación

También puede definir filtros y clasificaciones predefinidos para limitar y organizar los registros de datos que se pueden mostrar a los usuarios. Para filtrar u ordenar, haga clic en **Añadir filtro** o **Añadir ordenación**, seleccione la **columna** y la **condición** deseadas y confirme con **Enviar**.

![Añadir filtros en páginas de registro único](images/Add-filters-on-Single-Record-pages-in-Universal-Apps.png)

Los usuarios sólo pueden ver la información de un único registro de datos que usted muestra a través de los campos de la tabla integrada.

{{< warning  headline="Nota importante"  text="Los usuarios de la aplicación **no pueden cambiar** los **filtros** ni la **ordenación** **preestablecidos**. Por lo tanto, solo verán los registros filtrados en un orden fijo, como deseen." />}}

## Configuración gráfica del fondo de la página

Puede realizar los siguientes ajustes gráficos para toda la página del tipo de registro único:

- Seleccione blanco, gris o un color definido por el usuario como **color de fondo** de la página.
- Establezca los **márgenes de la página** (superior, inferior, izquierdo, derecho).
- Decida si desea **ocultar** la **barra de título**.
- Decida si desea **ocultar** la **barra de herramientas** que los usuarios pueden utilizar para pasar de un registro a otro.

![Configuración del fondo de página de las páginas del tipo Registro único](images/Seitenhintergrund-Einstellungen-von-Seiten-des-Typs-Einzelner-Datensatz.png)

## Cambiar entre las registros

Si ha desplegado la barra de herramientas, los usuarios de la aplicación con la autorización de página correspondiente pueden pasar de un registro de datos a otro. {{< seatable-icon icon="dtable-icon-left" color="grey" >}} {{< seatable-icon icon="dtable-icon-right" color="grey" >}} Para ello, haga clic en **Registro anterior** o **Registro siguiente**. {{< seatable-icon icon="dtable-icon-search" color="grey" >}} También puede **buscar un registro** concreto.

![Pasar de un registro a otro en páginas de un solo registro](images/Switch-between-records-on-single-record-pages.gif)

## Modificar registro

Con la autorización adecuada, los usuarios de la aplicación pueden editar los registros de datos individuales en esta página.

![Modificar el registro en páginas de registro único](images/Modify-record-on-single-record-pages.gif)

- Haga clic en **Modificar registro** en la barra de herramientas.
- Se abre la ventana con los **detalles de la línea**. Realice allí los cambios deseados en el registro de datos.
- Cierre la ventana haciendo clic en el **símbolo x** para guardar los cambios.

## Generar código QR para registros individuales

También encontrará un **generador de códigos QR** en la barra de herramientas. El código QR contiene el enlace al registro mostrado en ese momento. Adjuntado a un objeto o dispositivo, puede escanear el código QR con una tableta o un teléfono inteligente y consultar todos los datos de la aplicación sin necesidad de utilizar el teclado. Esto facilita aún más, por ejemplo, la [gestión de inventarios]({{< relref "templates/operations/inventory-list" >}}).

![Más opciones de diseño en la página de registro único en SeaTable 5.1](images/SingleRecordPage.png)

## Ejecutar acciones de botón

Al igual que en las páginas de tablas y consultas, aquí también puede utilizar columnas de tipo [botón]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}). Tanto si desea crear un documento PDF, editar un registro de datos o ejecutar un script, puede iniciar todas estas **acciones con sólo pulsar un botón**. Para ello **no** se requiere autorización de edición. De este modo, los administradores de aplicaciones pueden restringir las interacciones del usuario para este tipo de página a unas pocas acciones predefinidas.

## Configuración de la columna de enlaces

En **la configuración de la columna de enlace**, puede especificar qué datos son visibles y qué operaciones están permitidas para cada tabla enlazada.

![Configuración de columnas de enlace en páginas de registro único](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Configuración de campos**: Aquí puede definir exactamente a qué columnas se aplican las siguientes autorizaciones.
- **Añadir y vincular nuevos registros**: Si activa este control deslizante, los usuarios podrán añadir nuevas entradas a la tabla vinculada. Puede utilizar la configuración de campos para definir qué columnas son **visibles** y qué columnas son **obligatorias**, es decir, deben rellenarse.
- **Vincular registros existentes**: Si activa este control deslizante, los usuarios podrán vincular entradas existentes en la tabla vinculada. Puede utilizar los ajustes de campo para definir qué columnas son **visibles**.
- **Limitar los enlaces a máximo un registro**: Si activa este control deslizante, los usuarios sólo podrán enlazar una fila de la tabla enlazada en las celdas de la columna de enlace.
- **Filtros preestablecidos**: si añade un filtro aquí, al enlazar las entradas sólo se mostrarán las opciones que cumplan las condiciones del filtro.
- **Activar la función de big data**: Si la función big data está activada, los usuarios pueden buscar en más de 20.000 registros de datos, siempre que haya este número de entradas en la tabla vinculada.
- **Modificar registros enlazados**: Si activa este control deslizante, los usuarios podrán editar las entradas existentes en la tabla vinculada. Puede utilizar los ajustes de campo para definir qué columnas son **editables**.

## Autorizaciones de páginas

Puede definir las siguientes [autorizaciones de página]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) para las páginas del tipo de registro único:

![Autorizaciones de páginas de calendario](images/Seitenberechtigungen-von-Kalenderseiten.png)

Decida quién está autorizado a **ver** y **editar** los registros de datos individuales. En esta página no se pueden añadir ni eliminar filas de la tabla.

{{< warning  headline="Atención con los botones" >}}

[Los botones]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) **siempre** se pueden pulsar independientemente de las autorizaciones de la página. Esto significa que todos los usuarios de la app pueden realizar determinados cambios en los registros de datos que hayas definido previamente, aunque las columnas afectadas estén bloqueadas para ellos o el usuario no esté autorizado a editar la página.

{{< /warning >}}

## Columnas de sólo lectura

Además de la autorización de página "¿Quién puede editar filas?", puede utilizar columnas de sólo lectura para definir con precisión qué valores de columna de un registro de datos pueden y no pueden modificar los usuarios.

![Columnas de sólo lectura en páginas de registro único](images/Read-only-columns-on-single-record-pages.png)

Vaya a la **configuración de la página** y marque las **casillas** de las columnas que deben ser **de sólo lectura** para los usuarios. Puede reconocer las columnas de solo lectura porque aparecen resaltadas en **gris** en los detalles de la fila.
