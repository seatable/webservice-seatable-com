---
title: 'La fórmula Findmax'
date: 2023-02-13
lastmod: '2023-02-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/es/ayuda/formula-findmax-seatable'
aliases:
    - '/es/ayuda/die-findmax-formel'
seo:
    title: 'Fórmula Findmax de SeaTable: calcula el mayor valor de registros vinculados'
    description: 'Aprende a usar la fórmula Findmax en SeaTable para obtener el valor máximo de entradas numéricas vinculadas entre tablas, con ejemplos prácticos y consejos de uso.'
---

La **fórmula Findmax** busca el **valor máximo** entre las entradas de la columna vinculada y lo devuelve. Esto es útil si hay **varias entradas** en la tabla vinculada que hacen referencia al mismo registro (por ejemplo, de una persona) en otra tabla.

La fórmula Findmax sólo funciona con **valores numéricos**, por lo que el contenido de la columna vinculada también debe constar de valores numéricos. Además, el uso de la fórmula Findmax sólo tiene sentido si el control deslizante **Permitir vincular a varias filas** está activado al crear la columna **Enlace a otros registros**. Si la opción estuviera desactivada, la fórmula Findmax contendría siempre el mismo número que en la columna vinculada.

## Para qué necesitas la fórmula Findmax

La **función Findmax** debe utilizarse cuando desee **cruzar** valores numéricos almacenados en diferentes tablas. Digamos que utiliza SeaTable para recoger las **horas de trabajo de** sus empleados, donde una tabla almacena los empleados y otra tabla almacena la actividad diaria. A continuación, puede vincular cada registro de empleado a las horas de trabajo introducidas.

![fórmula findmax](images/findmax-1.png)

Para saber cuándo se conectó por última vez un empleado, puede utilizar la **fórmula Buscarmáx** para mostrar el **valor mayor** -en este caso la última vez- del total de horas de conexión de una columna.

![La fórmula findmax](images/findmax2-1.png)

Puede utilizar la fórmula Findmax con todos los valores numéricos para representar el **valor máximo**.

## Para utilizar la fórmula Findmax

### Añadir un enlace a la tabla

Consulte el [artículo sobre la columna de enlace]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) para obtener información sobre cómo crear una columna del tipo **Enlace a otros registros**. Este es un requisito básico para poder utilizar la fórmula Findmax.

### Añadir una columna con la fórmula Findmax

![fórmula findmax](images/findmax.gif)

1. Cree una nueva columna del tipo **Fórmula para los enlaces**.
2. Establezca la opción **Findmax** como fórmula.
3. Seleccione la columna creada anteriormente del tipo **Enlace a otros registros** de esta tabla.
4. En el campo **Seleccionar columna de consulta en la tabla vinculada "..."**, defina la columna de la otra tabla que desea vincular a la columna de aquí.
5. Haga clic en **Enviar**.

{{< warning  headline="Atención"  text="La fórmula Findmin sólo funciona con **valores numéricos**, por lo que la columna vinculada debe contener valores numéricos." />}}
