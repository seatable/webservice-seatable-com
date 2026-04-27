---
title: 'La columna Fórmula para enlaces'
date: 2025-07-18
lastmod: '2025-07-18'
categories:
    - 'formeln'
author: 'kgr'
url: '/es/ayuda/columna-de-formula-de-enlaces'
aliases:
    - '/es/ayuda/die-spalte-formel-fuer-verknuepfungen'
seo:
    title: 'Columna de fórmula de enlaces en SeaTable'
    description: 'Aprenda a usar la columna de fórmula de enlaces para conectar, resumir y relacionar datos entre tablas en SeaTable.'

---

Con una fórmula para enlaces, puede **visualizar, resumir o relacionar datos de tablas enlazadas** en su tabla actual. Aquí es donde SeaTable muestra sus ventajas como [base de datos relacional]({{< relref "posts/relationale-datenbank" >}}).

Dispone de un total de **cinco fórmulas diferentes** para el tipo de columna. El requisito previo para utilizar la columna es la existencia de al menos una columna del tipo [enlace a otros registros]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) en su tabla.

## Crear una columna de tipo Fórmula para enlaces

Para aplicar una fórmula, primero debe añadir una nueva columna Fórmula para enlaces a su tabla.

![Selección de una fórmula para enlaces](images/add-a-link-formula.png)

1. Haga clic en el **símbolo más** a la derecha de la última columna.
2. Dé un **Nombre** a la columna.
3. Seleccione **Fórmula para enlaces** como tipo de columna.
4. Decida una **Fórmula** (por ejemplo, Rollup).
5. Seleccione la **columna de enlace** de la tabla de la que desea utilizar los datos.
6. Especifique la **columna de la tabla enlazada** a la que debe referirse la fórmula.
7. En función de la fórmula seleccionada, puede realizar **otros ajustes**.
8. Cree la columna con **Enviar**.

## 5 Fórmulas para enlaces

Encontrará más información y ejemplos de las cinco fórmulas diferentes en los siguientes artículos, que ilustran las ventajas y el uso de las fórmulas:
- [Lookup]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}})
- [Countlinks]({{< relref "help/base-editor/formeln/die-countlinks-formel" >}})
- [Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}})
- [Findmax]({{< relref "help/base-editor/formeln/die-findmax-formel" >}})
- [Findmin]({{< relref "help/base-editor/formeln/die-findmin-formel" >}})

## Formato de los resultados

Cada fórmula en SeaTable tiene como resultado un **número**, una **fecha** o un **texto/cadena**. A los resultados de una columna de fórmula para enlaces se les asigna automáticamente un **formato** específico. Si no está satisfecho con ello, puede **redetectarlo**. Para ello, haga clic en la **flecha desplegable** situada a la derecha del nombre de la columna y, a continuación, en **Editar ajustes de formato**.

![Formato de los resultados de la fórmula](images/format-settings-of-the-link-formula-column.png)

También dispone de diferentes **configuraciones de formato para los números** para las columnas Countlinks y Rollup: Porcentaje, divisas o duración, así como separadores decimales, separadores de miles y precisión.