---
title: 'Bloquear una fila'
date: 2022-10-10
lastmod: '2023-01-27'
categories:
    - 'arbeiten-mit-zeilen'
author: 'vge'
url: '/es/ayuda/bloquear-fila-seatable'
aliases:
    - '/es/ayuda/sperren-einer-zeile'
seo:
    title: 'Bloquear filas en SeaTable – protege los cambios rápidos'
    description: 'Bloquea las filas en SeaTable manual o automáticamente para evitar modificaciones. Elige permisos y mantén la integridad de tus datos y procesos.'

---

{{< required-version "Más" "Empresa" >}}

Para evitar cambios no deseados en las filas, puede **bloquearlas**. Esto puede ser útil, por ejemplo, si hay más de una persona trabajando en una tabla. El bloqueo puede ser **manual** o [automático]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}).

## Para bloquear una fila

1. Abra cualquier tabla en la que desee bloquear una **fila**.
2. **Haga clic con el botón derecho del ratón** en la línea para abrir el menú desplegable.
3. Seleccione la opción **Bloquear Fila**.

En cuanto se bloquea una fila, aparece un pequeño **triángulo rojo** en **la columna de numeración**.

![Bloquear una línea](images/sperren-einer-zeile-1.png)

## Desbloquear filas

Del mismo modo que bloqueas una fila, también puedes volver a **desbloquearla**. Para ello, siga las instrucciones de clic descritas anteriormente y seleccione la opción **Desbloquear fila**.

{{< warning  headline="Autorización necesaria"  text="Sólo puede desbloquear filas que **usted mismo** haya bloqueado, a menos que tenga **derechos de administrador**. A continuación, también puede desbloquear filas que hayan sido bloqueadas por **otros** o por una **automatización**." />}}

## Bloqueo de filas con ayuda de un automatismo

{{< required-version "Empresa" >}}

En SeaTable puede crear **reglas de automatización** para **bloquear automáticamente las filas** en cuanto cumplan determinadas condiciones.

Esto es muy útil si desea bloquear muchas filas a la vez o si siempre desea evitar que una fila se siga editando a partir de un momento determinado (por ejemplo, cuando finaliza un proceso).

**Encontrará más información al respecto en el artículo** [Bloqueo de filas mediante automatización]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}).

![Bloquear una línea con un automatismo](images/lock-row-with-an-automation.png)

{{< warning  headline="Desbloqueo sólo posible manualmente"  text="**No se pueden** desbloquear filas bloqueadas con un automatismo del mismo modo. Esto sólo es posible manualmente y con los **derechos de administrador** necesarios." />}}
