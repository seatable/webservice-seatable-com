---
title: 'Cómo funcionan las automatizaciones'
date: 2023-01-31
lastmod: '2025-12-01'
categories:
    - 'automationen'
author: 'kgr'
url: '/es/ayuda/como-funcionan-automatizaciones-seatable'
aliases:
    - '/es/ayuda/funktionsweise-von-automationen'
seo:
    title: 'Cómo funcionan las automatizaciones en SeaTable'
    description: 'Descubre cómo las automatizaciones optimizan procesos en SeaTable: disparadores, acciones, condiciones y ejemplos de flujos eficientes.'
weight: 4
---

Las automatizaciones son una potente función de SeaTable que le permite automatizar procesos. Al automatizar los pasos, no sólo se ahorra tiempo, sino que también se minimizan los errores humanos al trabajar con datos.

## Información básica

- Las automatizaciones se crean siempre como reglas de automatización individuales que se refieren a una **vista de tabla** específica.
- Los dos componentes más importantes de una automatización son el **evento desencadenante** y la(s) **acción(es) automatizada(s)**.

## Eventos desencadenantes

Un disparador es un evento que actúa como **desencadenante** de la automatización. Este evento se define individualmente para cada regla de automatización. El hecho de que **se hayan añadido o editado filas** en una vista de tabla puede actuar como disparador. Un **tiempo** específico en un intervalo definido (diario, semanal o mensual) también puede activar una automatización.

Para determinados eventos, como la adición de filas, también puede realizar otros **ajustes**. Por ejemplo, puede determinar si **todas las columnas** de la vista de tabla o sólo las columnas seleccionadas deben **supervisarse** para detectar la aparición del evento desencadenante. Si selecciona columnas individuales en este contexto, la automatización sólo se activa si el evento se produce en las columnas seleccionadas.

Además, puede limitar las **condiciones** del evento desencadenante para que la automatización sólo se active si se encuentran **determinados datos** en determinadas columnas. Por ejemplo, puede definir los valores exactos que deben estar presentes en una columna seleccionada después de añadir o modificar una entrada para que se active la automatización.

Puede consultar todo lo demás en el artículo [Disparadores de automatización]({{< relref "help/base-editor/automationen/automations-trigger" >}}).

## Acciones automatizadas

Las acciones automatizadas son aquellas que **se desencadenan** al producirse el evento desencadenante especificado. Por tanto, las acciones automatizadas son siempre una **consecuencia** de eventos desencadenantes y sólo se producen cuando esos eventos se dan en las condiciones especificadas.

En función del evento seleccionado, puede elegir entre distintas acciones, como **enviar un correo electrónico** o una **notificación** a uno o varios usuarios, **añadir, modificar o bloquear un registro** o **ejecutar scripts de Python o funciones de inteligencia artificial**.

Para muchas acciones también deben cumplirse **requisitos** adicionales. Por ejemplo, se necesitan determinados tipos de columnas, una cuenta de correo electrónico o plantillas en el plugin de diseño de páginas o de diseño de informes para hacer posibles automatizaciones más complejas.

{{< warning  headline="Nota"  text="Por supuesto, tiene la opción de asignar **varias acciones** a un único evento desencadenante." />}}

Si desea obtener más información sobre las [acciones automatizadas]({{< relref "help/base-editor/automationen/automations-aktionen" >}}), lea el artículo.

## Cómo funcionan las automatizaciones

A continuación se explica con más detalle la funcionalidad de las automatizaciones mediante un ejemplo.

{{< warning  headline="Nota importante"  text="El ejemplo ficticio pretende ilustrar el **funcionamiento básico** de las automatizaciones de complejidad reducida y, por tanto, sólo contiene una cantidad relativamente pequeña de datos. Por regla general, las automatizaciones tienen un efecto mucho mayor en los **conjuntos de datos más extensos**." />}}

![Tabla de ejemplo](images/example-for-a-simple-automation-1.jpg)

Podría utilizar la tabla de ejemplo que se muestra en la imagen en el departamento de RRHH de una empresa para registrar el **estado del empleo** y el estado de los **pagos salariales**, además de los datos de los empleados.

A continuación, crearía una **automatización** para la vista de la tabla con el fin de automatizar un paso de trabajo. En concreto, cuando un empleado abandona la empresa, es decir, siempre que la entrada de la columna **Estado** cambia de "empleado" o "autónomo" a "terminado", "baja parental" o "jubilado", la entrada de la columna **Payroll** debe pasar de "activa" a "inactiva".

![Ejemplo-Automatización](images/example-for-a-simple-automation-2.jpg)

Para automatizar este paso del proceso, defina primero el evento "Cuando se cambia una fila" como un **disparador**. En la configuración del disparador, seleccione la **tabla** y la **vista** e introduzca la columna "Estado" como **columna supervisada**. Como **condición específica** para activar la automatización, especifique que la fila editada en la columna correspondiente debe tener el valor "terminado", "baja parental" o "jubilado".

![definición del evento desencadenante](images/example-for-a-simple-automation-3.jpg)

A continuación, seleccione la opción **Modificar registro** como **acción automatizada**. En concreto, la entrada de la columna "Payroll" debe pasar de "activa" a "inactiva" después de que se haya disparado el evento desencadenante.

![definición de la acción automática de la automatización de ejemplo](images/example-for-a-simple-automation-4.jpg)

Una vez creada la automatización, el cambio manual en la columna "Estado" **desencadena automáticamente** el **ajuste deseado de la entrada** en la columna "Payroll".

![ejecución de la automatización de ejemplo](images/example-for-a-simple-automation.gif)