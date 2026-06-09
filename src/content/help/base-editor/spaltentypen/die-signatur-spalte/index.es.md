---
title: 'La columna de firmas'
date: 2023-06-27
lastmod: '2024-03-18'
categories:
    - 'dateien-und-bilder'
author: 'nsc2'
url: '/es/ayuda/columna-firmas'
aliases:
    - '/es/ayuda/die-signatur-spalte'
seo:
    title: 'Columna de firmas: guarda firmas digitales en SeaTable'
    description: 'Capture firmas digitales en SeaTable con la columna de firma y adminístrelas como archivos PNG directamente en la gestión de archivos de la base.'
weight: 26
---

Puede almacenar una firma digital en una **columna de firma**, que se guarda como archivo PNG en el gestor de archivos Base.

## Cómo crear una columna de firmas

![Crear una columna de firma](images/add-a-signature-column-to-your-table-4.gif)

1. Haga clic en el **símbolo \[+**\] situado a la derecha de la última columna de la tabla.
2. Dé un **nombre** a la columna en el campo superior.
3. Seleccione el tipo de columna Columna de **firma** en el menú desplegable.

## Capturar una firma digital

Si haces clic en cualquier celda de la **columna de firma**, se abre automáticamente una ventana con un **panel** en el que puedes firmar con el ratón y -en dispositivos con pantalla táctil- con un bolígrafo o el dedo.

{{< warning  headline="Consejo" >}}

Las firmas digitales son muy adecuadas para la recogida de datos mediante [formularios web]({{< relref "help/base-editor/webformulare/webformulare" >}}), por ejemplo para que las solicitudes se firmen cómodamente en línea.

{{< /warning >}}

!["Depositar una firma en una columna de firmas](images/add-a-signature-into-a-signature-column-1.gif)

## Asegurar una firma digital

Para guardar una firma introducida en el panel, basta con hacer clic en **Guardar**. La firma introducida en el panel se guardará en la celda y podrá recuperarse en cualquier momento haciendo doble clic.

![Firma almacenada en una columna de firma ](images/stored-signatur-in-cell-1.png)

## Modificar una firma digital

Si no está satisfecho con su firma y desea firmar de nuevo, simplemente haga clic en **Firmar de nuevo**. Tenga en cuenta que se sobrescribirá toda la firma que haya introducido. **No** es posible modificar partes individuales de su firma.

![Firmar de nuevo en el panel de firma](images/resign.jpg)

{{< warning  headline="Fichero no eliminado" >}}

Sin embargo, la firma original sigue estando disponible como archivo PNG en el [gestor de archivos]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) Base si ya la ha guardado.

{{< /warning >}}

## Firmas digitales en el gestor de archivos

Cada firma almacenada también se guarda en la [gestión de archivos]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) de su Base como un archivo PNG en una **carpeta del sistema**.

![Carpeta en la gestión de archivos de su Base donde se almacenan sus firmas ](images/stored-signatures-in-filemanagement.jpg)

Desde ahí puedes **descargar** y **eliminar** tus firmas.

![](images/Bild-06.06.23-um-19.18-511x87.jpg)
