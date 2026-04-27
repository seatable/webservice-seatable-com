---
title: 'Trasladar filas al almacén de big data'
date: 2022-09-23
lastmod: '2024-05-13'
categories:
    - 'big-data'
author: 'cdb'
url: '/es/ayuda/mover-filas-big-data-backend'
aliases:
    - '/es/ayuda/zeilen-ins-big-data-backend-verschieben'
seo:
    title: 'Mover filas al almacenamiento Big Data en SeaTable – guía'
    description: 'Descubre cómo mover, archivar y recuperar filas en el almacenamiento Big Data en SeaTable. Tutorial para activar y usar funciones avanzadas.'

---

{{< required-version "Empresa" >}}

Sólo se pueden crear **nuevas filas** en **las vistas normales** de SeaTable. A continuación, puede mover las filas de la vista **manual o automáticamente** al almacenamiento de big data.

{{< warning  headline="Requisito previo" >}}

Sólo puede mover filas al almacén de big data si [ya está activado]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) dentro de la base.

{{< /warning >}}

## Mover filas al almacén de big data

![Mover filas a la memoria de big data](images/move-rows-to-big-data.gif)

1. Haga clic en los **tres puntos** de las opciones de visualización.
2. Seleccione la opción **Vista de archivo**.
3. **Confirme** el traslado de todas las filas visibles al almacén de big data.

{{< warning  headline="Consejo" >}}

Por ejemplo, si desea **archivar entradas antiguas**, puede filtrar previamente la vista con los tipos de columna [Fecha de creación]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) o [Última modificación]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}).

{{< /warning >}}

A continuación, las filas se transfieren al almacén de big data. Como resultado, ya no son visibles en la vista normal. [Cree una vista de big data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}) para mostrar los datos en la memoria de big data.

## Archivo automatizado

También puede crear una **regla de automatización con la acción "Archivar"** para que SeaTable mueva automáticamente las filas de una vista al almacenamiento de big data en un momento determinado.

Encontrará más información al respecto en [Acciones de automatización]({{< relref "help/base-editor/automationen/automations-aktionen" >}}).

## ¿Cómo reconocer si los datos están almacenados en big data o no?

Las filas almacenadas en la memoria de big data tienen un pequeño **triángulo gris en la columna de numeración**.

**Es bueno saberlo:**

- En una [vista normal]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}}), **no** se muestra **ninguna fila de la memoria de big data**.
- En una [vista de big data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}), se pueden mostrar **todas las filas**, independientemente de dónde estén guardadas en ese momento.

## Recuperar entradas del almacén de big data

[En este artículo]({{< relref "help/base-editor/big-data/zeilen-aus-dem-big-data-backend-zurueckholen" >}}) se explica cómo recuperar entradas de la memoria de big data.
