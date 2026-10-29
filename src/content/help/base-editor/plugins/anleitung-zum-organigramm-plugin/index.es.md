---
title: 'Guía del plugin de organigrama'
date: 2024-07-18
lastmod: '2025-02-28'
categories:
    - 'plugins'
author: 'kgr'
url: '/es/ayuda/guia-plugin-organigrama'
aliases:
    - '/es/ayuda/anleitung-zum-organigramm-plugin'
seo:
    title: 'Plugin Organigrama: Visualiza equipos y jerarquías'
    description: 'Plugin de organigrama: Muestra jerarquías, equipos, o estructuras de proyectos con claridad. Configuración fácil en SeaTable.'
---

Puede utilizar el complemento de organigrama para mostrar **jerarquías** entre los registros de datos de una tabla. Esto es útil, por ejemplo, para visualizar los cargos en una empresa o las [tareas superordinadas y subordinadas en un proyecto]({{< relref "templates/projects/work-breakdown-structure" >}}).

**Vea nuestro vídeo explicativo con subtítulos en espanhol.**
{{< youtube OD71y5CJ7vo >}}

Puede encontrar información sobre cómo activar el plugin en una base [aquí]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

![Plugin de organigrama](images/Organigramm-Plugin.png)

## Requisitos y funcionalidad del plugin de organigrama

Para definir qué registros de datos dependen unos de otros, necesita un [enlace que haga referencia a una misma tabla]({{< relref "help/base-editor/tabellen/verknuepfungen-innerhalb-einer-tabelle" >}}). La entrada que vincule en esta columna a otra fila de la misma tabla se mostrará como **registro de datos superior**.

![Columna de enlace para un organigrama](images/Verknuepfungsspalte-fuer-ein-Organigramm.png)

> En el ejemplo de aplicación con los puestos en una empresa, se vincularía por tanto el respectivo responsable del empleado en la columna de vinculación. El resultado son los niveles del organigrama: Los jefes de departamento estarían en el segundo nivel y el director general en el superior.

Si desea ilustrar los registros de datos del organigrama con imágenes, también necesitará una [columna de imágenes]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) en la tabla, donde podrá cargar fotos y gráficos.

## Opciones de configuración de un organigrama

Por defecto, se crea un organigrama vacío cuando abre el plugin de organigrama por primera vez. {{< seatable-icon icon="dtable-icon-add-table" >}} Si desea crear otro organigrama, haga clic en **Añadir organigrama**. Se abrirá un campo en el que podrá introducir el **nombre** que desee.

![Opciones de organigramas](images/Optionen-fuer-Organigramme.png)

{{< seatable-icon icon="dtable-icon-drag" >}} Para **cambiar** el **orden de los organ**igramas, mantenga pulsado el botón izquierdo del ratón en la **zona de agarre** y **arrastre y suelte** el organigrama en la posición deseada. También puede **renombrar**, **duplicar** o **eliminar** organigramas.

{{< warning  headline="Nota"  text="Si sólo se ha creado un organigrama en el plugin, **no podrá eliminarlo**." />}}

{{< seatable-icon icon="dtable-icon-set-up" >}} Puede definir lo siguiente para el organigrama a través de los **ajustes**, a los que puede acceder haciendo clic en el **símbolo de la rueda dentada**:

- **Tabla**: Seleccione la tabla a partir de la cual SeaTable debe generar el organigrama.
- **Vista**: seleccione la vista con los registros de datos que se mostrarán en el organigrama.
- **Relación**: Seleccione la columna de relación en la que se basa la jerarquía.
- **Título**: Seleccione una columna cuyos valores deban mostrarse como título.
- **Imagen de portada**: seleccione una columna de imágenes para ilustrar los registros de datos.
- **Otras columnas**: Seleccione columnas adicionales cuyos valores deban mostrarse.

![Configuración del organigrama](images/Einstellungen-eines-Organigramms.png)

{{< warning  headline="Nota"  text="Actualmente, el organigrama sólo puede tener **una cabeza** en el nivel superior de la jerarquía. Si su empresa tiene varios directores generales, por ejemplo, debe colocar el nombre de la empresa en la parte superior." />}}
