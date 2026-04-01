---
title: 'La vista en árbol'
date: 2026-04-01
lastmod: '2026-04-01'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/es/ayuda/la-vista-en-arbol'
seo:
    title: 'Vista en árbol: muestra la jerarquía de los registros de datos enlazados'
    description: 'Utilice la vista en árbol de SeaTable para visualizar la jerarquía de los registros de datos vinculados y mostrar datos complejos de forma estructurada.'
weight: 16
---

La **vista en árbol** permite la **visualización jerárquica** compacta de registros de datos enlazados. Esto significa que puede visualizar datos que se encuentran en diferentes **tablas vinculadas** a distintos niveles en un diagrama de árbol. La vista proporciona una visión general estructurada, especialmente en el caso de grandes cantidades de datos, como los datos financieros o de proyectos.

![la vista en árbol](images/tree-view.png)

{{< warning type="warning" headline="Requisitos" >}}

Para utilizar la vista en árbol de forma sensata, necesita una base con **al menos dos tablas** que estén enlazadas entre sí mediante una [columna de enlace]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}).

{{< /warning >}}

## Cómo funciona la vista en árbol

Antes de crear una vista en árbol, debe considerar qué **estructura de árbol** (es decir, jerarquía de registros de datos vinculados en su base) tiene sentido: En una [cartera de proyectos]({{< relref "templates/projects/project-portfolio" >}}), por ejemplo, podrían ser los departamentos en el primer nivel, los proyectos en el segundo y las tareas en el tercero. En consecuencia, los departamentos, los proyectos y las tareas deben registrarse en tres tablas diferentes vinculadas entre sí. Cada tarea está asignada a un proyecto, que a su vez está subordinado a un departamento.

![Ejemplo de estructura de árbol](images/example-for-tree-view.png)

Defina cómo dependen los registros de datos unos de otros y qué tablas se encuentran en cada nivel utilizando los **niveles**. Actualmente puede mostrar hasta tres niveles, es decir, datos de tres tablas, en la vista en árbol.

## Cómo crear una vista en árbol

1. Haga clic en el **nombre de la vista actual**.
2. Haga clic en **Añadir vista o carpeta** y seleccione el **tipo de vista** deseado.

![crear una vista en árbol](images/create-tree-view.png)

3. Dé un **nombre** a la nueva vista.
4. Active el control deslizante si la nueva vista no debe ser visible para todos sino **privada**.
5. Confirme con **Submitir**.

![Nombrar la vista del árbol](images/name-tree-view.png)

6. Haga clic en el **icono de la rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} en la esquina superior derecha y ajuste la **configuración**.
7. Especifique qué **tabla** debe mostrarse en el nivel correspondiente. Para ello, haga clic en el campo de **Nivel 2** y **Nivel 3** para seleccionar la tabla deseada de la lista desplegable. **Nivel 1** siempre está ocupado por la tabla en la que se encuentra la vista.

![Establecer jerarquía en la vista de árbol](images/tree-view-settings.jpg)

A continuación, los registros de datos vinculados del segundo y tercer nivel del diagrama de árbol se agrupan bajo los respectivos registros de datos de nivel superior.

## Mostrar y ocultar información

A través de los **configuraciones**, a los que puede acceder pulsando el **icono de la rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}}, puede definir las columnas visibles para cada nivel del diagrama de árbol. Para ello, seleccione primero el **Nivel** en el que desea mostrar u ocultar las columnas. Si a continuación desactiva el **deslizador** correspondiente en el lado derecho, las columnas no serán visibles en el diagrama de árbol.

![Ocultar o mover columnas en la vista en árbol](images/hide-and-move-columns-in-tree-view.png)

### Mover columnas

También tiene la opción de disponer las columnas de forma diferente a la vista de tabla en cada nivel. Para ello, mantenga pulsado el botón izquierdo del ratón sobre la **zona de agarre de seis puntos** situada delante del nombre de la columna y mueva la columna **arrastrando y soltando** hasta la posición deseada.

## Opciones de vista

Puede utilizar las siguientes opciones en la vista de árbol:
- [Bloquear vista]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrar]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) u [ordenar]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) por cualquier valor
- **Comprimir todo** o **Expandir todo**

## Contraer y expandir registros de datos vinculados

Para contraer todos los registros de datos enlazados bajo una entrada, haga clic en la **flecha desplegable** situada a la izquierda de la fila. Para volver a expandir los registros de datos, proceda del mismo modo.

![Contraer registros en vista de árbol](images/collapse-records-in-tree-view.gif)

## Ajustar la anchura de columna

Para evitar entradas truncadas o grandes espacios entre los valores, puede **ajustar la anchura de la columna** según sus necesidades. Para ello, mantenga pulsado el botón izquierdo del ratón sobre la línea divisoria entre dos columnas y arrastre el cursor hacia la izquierda o la derecha.

![Ajustar el ancho de columna en vista de árbol](images/adjust-column-width-in-tree-view.gif)

## Añadir y editar registros de datos en la vista en árbol

Para añadir un nuevo registro de datos en el primer nivel de la vista en árbol, haga clic en el **círculo naranja con el símbolo más** de la esquina inferior derecha. Se abrirán entonces los **Detalles de la fila**. Rellénelos como desee y cierre la ventana para guardar el registro de datos.

Para añadir un nuevo registro de datos en el segundo o tercer nivel de la vista en árbol, haga clic en **\+ Añadir registro**. La fila creada se vincula automáticamente al registro de datos padre y se agrupa en consecuencia. Puede rellenar los campos restantes directamente en la fila.

![Añadir y editar registros de datos en la vista en árbol](images/add-record-in-tree-view.png)

Las entradas existentes también pueden editarse directamente en la vista en árbol. También puede hacer clic en **Ampliar** para abrir los detalles de la fila y realizar cambios.

![añadir y editar registros de datos en la vista en árbol](images/expand-record-in-tree-view.png)

Por supuesto, los datos también se guardan en las tablas subyacentes.