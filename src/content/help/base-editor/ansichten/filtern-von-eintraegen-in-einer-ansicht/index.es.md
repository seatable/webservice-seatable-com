---
title: 'Filtrar entradas en una vista'
date: 2022-11-16
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/es/ayuda/filtrar-registros-vista-seatable'
aliases:
    - '/es/ayuda/filtern-von-eintraegen-in-einer-ansicht'
seo:
    title: 'Filtrar registros en una vista SeaTable: cómo aplicar filtros y personalizar'
    description: 'Aprende a mostrar solo los registros relevantes de tu tabla SeaTable aplicando filtros según campos, tipos de dato y combinando reglas con total flexibilidad.'
weight: 21
---

Con la función de filtrado de SeaTable, puede utilizar **reglas de filtrado** para filtrar las entradas deseadas de una tabla y mostrar sólo las entradas que cumplan determinados criterios. El conjunto de filtros sólo se refiere a la **vista activa**.

{{< warning headline="Nota importante" text="El filtrado sólo modifica el número de registros de datos que se muestran en la vista. La base de datos permanece inalterada por el filtrado y las filas invisibles no se eliminan. Por lo tanto, si han desaparecido registros de datos, compruebe si se encuentra en la vista correcta o si ha ocultado registros de datos con un filtro." />}}

## Filtrar entradas en una vista

![Filtrar entradas](images/Filtern-von-Eintraegen-1.gif)

1. Seleccione la **vista** en la que desea establecer un filtro.
2. Haga clic en **Filtro** en las opciones de visualización situadas encima de la tabla.
3. Vaya a **Añadir filtro** o **Añadir grupo de filtros**.
4. En el primer campo, seleccione la **columna** para la que desea definir una regla de filtrado.
5. En el campo central, defina la **condición** según la cual deben filtrarse las entradas.
6. En el último campo, decida a qué **opción** o **valor** debe referirse la condición.

## Las diferentes condiciones al filtrar

SeaTable admite el filtrado por todos los [tipos de columna]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) excepto botones.

Dependiendo del **tipo de columna** por el que quiera filtrar, las condiciones que puede seleccionar también se adaptan.

### He aquí algunos ejemplos

Tiene estas opciones de condición con un [Columna de texto]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}):

![Columna de texto filtrado](images/filtern-von-eintraegen-5.png)

Tiene estas opciones de condición con un [Columna de selección única]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}):

![Filtrar una sola columna de selección](images/filtern-von-eintraegen-6.png)

Tiene estas opciones de condición con un [Columna de imágenes]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}):

![Columna de imágenes filtradas](images/filtern-von-eintraegen-7.png)

Las filas **con celdas vacías** en la columna de filtrado no suelen mostrarse a menos que se busque explícitamente "está vacío".

## Eliminar un filtro

Puede **borrar** los filtros que haya creado haciendo clic en el botón **x**.

![Eliminar un filtro de una vista](images/filtern-von-eintraegen.png)

## Aplicar varios filtros

Puede crear uno o más filtros que restrinjan aún más la primera condición. Más información en el artículo [Vincular reglas de filtrado con AND y OR]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}}).

## Reorganizar filtros

Puede mover y reordenar los filtros moviendo el ratón sobre el icono **superficie de agarre de seis puntos**, presiona y mantén, tira y suelta.  

![Filtrar las entradas clasificadas](images/Filtern-von-Eintraegen-2.gif)
