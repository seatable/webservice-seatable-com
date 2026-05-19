---
title: 'Enlaces dentro de una tabla'
date: 2025-02-28
lastmod: '2025-02-28'
categories:
    - 'verknuepfungen'
author: 'kgr'
url: '/es/ayuda/vincular-registros-misma-tabla'
aliases:
    - '/es/ayuda/verknuepfungen-innerhalb-einer-tabelle'
seo:
    title: 'Vincular registros en la misma tabla: SeaTable'
    description: 'Aprende a vincular datos dentro de una tabla SeaTable: jerarquía, relaciones padre-hijo, columnas dobles y consejos de configuración.'

---

Puede utilizar una **columna de enlace** en SeaTable no sólo para enlazar varias tablas, sino también para **relacionar registros de datos de una misma tabla**.

Esto es especialmente útil si los datos de su tabla tienen una **jerarquía**.

## Añadir un enlace dentro de una tabla

![Añadir un enlace dentro de una tabla](images/Verlinkung-innerhalb-einer-Tabelle-hinzufuegen.gif)

1. Haga clic en el **signo más** situado a la derecha de la última cabecera de columna.
2. Introduzca el **nombre de la columna principal** en el campo de entrada.
3. Seleccione **Enlace a otras entradas** como tipo de columna.
4. Seleccione **la tabla actual** como tabla a vincular.
5. Confirme con **Enviar**.
6. SeaTable añade automáticamente una **segunda columna para las entradas subordinadas**.

{{< warning  headline="Atención" >}}

Las dos columnas de enlace están **inextricablemente** unidas. Si **elimina** una de las dos columnas, la otra también desaparece inmediatamente. Sin embargo, si sólo quieres ver una de las dos columnas en tu tabla, puedes [ocultar]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}}) la otra.

{{< /warning >}}

## Vinculación de registros de datos en una tabla

![Relaciones padre-hijo en una tabla](images/Eltern-Kind-Beziehungen-in-einer-Tabelle.gif)

1. Haga clic en una **celda de la columna de enlaces** y, a continuación, en el **símbolo más** que aparece.
2. Ahora se muestran las **filas** disponibles **en la tabla**. Haga clic en la(s) fila(s) que desee vincular a la fila seleccionada.
3. **La entrada enlazada** se muestra inmediatamente en ambas columnas de enlace.

{{< warning  headline="Consejo"  text="Puede utilizar la **función de búsqueda integrada** en el diálogo de enlaces para buscar en las entradas de la tabla y encontrar rápidamente la fila deseada." />}}

## ¿Por qué hay dos columnas para el mismo enlace?

Si crea una columna de enlace que vincule entradas de una misma tabla, SeaTable crea automáticamente una segunda columna de enlace.

- En la **primera** columna de enlace, puede ver los registros de datos que están **supeditados a** una fila.
- En la **segunda** columna de enlace, puede ver los registros de datos que están **subordinados a** una fila.

Por lo tanto, los **padres y los hijos** de una relación padre-hijo se registran y se muestran en columnas separadas. De este modo, SeaTable garantiza que haya un registro de datos padre e hijo para cada relación.

{{< warning  headline="Nota"  text="Si **elimina** un **enlace**, borrará simultáneamente la entrada en la columna del enlace padre o hijo." />}}

## Artículos relacionados

- Si desea **visualizar** claramente los vínculos jerárquicos, le recomendamos encarecidamente el [plugin de organigrama]({{< relref "help/base-editor/plugins/anleitung-zum-organigramm-plugin" >}}).
- Para todas las demás preguntas sobre el manejo de columnas de enlace, consulte el artículo sobre [la columna de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).
