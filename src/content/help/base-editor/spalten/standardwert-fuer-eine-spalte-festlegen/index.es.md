---
title: 'Establecer valor por defecto para una columna'
date: 2023-11-07
lastmod: '2024-06-11'
categories:
    - 'arbeiten-mit-spalten'
author: 'kgr'
url: '/es/ayuda/establecer-valor-predeterminado-columna'
aliases:
    - '/es/ayuda/standardwert-fuer-eine-spalte-festlegen'
seo:
    title: 'Establecer valor predeterminado en una columna'
    description: 'Descubra cómo definir valores predeterminados en columnas de SeaTable para completar filas nuevas automáticamente y agilizar la gestión de datos.'
---

Si define un **valor** por defecto para una columna, éste se **introduce automáticamente en cada nueva** fila de la tabla. Con los valores por defecto predefinidos, puede ahorrarse unos cuantos clics al [añadir nuevas filas]({{< relref "help/base-editor/zeilen/hinzufuegen-einer-zeile" >}}). Por supuesto, después puede ajustar manualmente los valores introducidos automáticamente.

## Cómo establecer valores por defecto

![Establecer el valor por defecto de una columna](images/Standardwert-festlegen.gif)

1. Haga clic en el **icono** triangular **desplegable** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} situado a la derecha del nombre de la columna para la que desea definir un valor por defecto.
2. Seleccione la opción **Establecer valor por defecto**.
3. Introduzca el **valor por defecto** deseado. Dependiendo del tipo de columna, tiene varias opciones para elegir.
4. Confirme el proceso con el **botón Intro** o **haciendo clic** fuera de la ventana de diálogo.
5. Si ahora **crea** una **nueva fila**, SeaTable introduce automáticamente los valores correspondientes. A continuación, puede **ajustar** los datos como de costumbre.

{{< warning  headline="Atención"  text="Los valores por defecto se utilizan **universalmente** al crear nuevas filas, es decir, las filas que se crean mediante una acción automatizada o de botón también contienen los valores por defecto." />}}

También puede definir un valor por defecto directamente al [crear una nueva columna]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

## Para qué tipos de columnas puede definir valores por defecto

Se pueden definir valores por defecto para muchos, pero no todos, [los tipos de columnas en]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) SeaTable. Las columnas cuyo contenido es generado automáticamente por SeaTable[(fórmulas]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}), [archivo]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) y [firma]({{< relref "help/base-editor/spaltentypen/die-signatur-spalte" >}}).

**A continuación encontrará un resumen de los tipos de columna para los que puede definir valores por defecto:**

| Tipo de columna          | Admite valores por defecto                                    |
| ------------------------ | ------------------------------------------------------------- |
| Número automático        | {{< icon "circle-xmark" >}}                                   |
| Imagen                   | {{< icon "circle-xmark" >}}                                   |
| Casilla de verificación  | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Archivo                  | {{< icon "circle-xmark" >}}                                   |
| Fecha                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Duración                 | {{< icon "circle-xmark" >}}                                   |
| Selección individual     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Correo electrónico       | {{< icon "circle-xmark" >}}                                   |
| Creador                  | {{< icon "circle-xmark" >}}                                   |
| Creado                   | {{< icon "circle-xmark" >}}                                   |
| Texto con formato        | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Fórmula                  | {{< icon "circle-xmark" >}}                                   |
| Fórmula para los enlaces | {{< icon "circle-xmark" >}}                                   |
| Geoposición              | {{< icon "circle-xmark" >}}                                   |
| Último editor            | {{< icon "circle-xmark" >}}                                   |
| Selección múltiple       | {{< icon "circle-xmark" >}}                                   |
| Empleados                | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Clasificación            | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Botón                    | {{< icon "circle-xmark" >}}                                   |
| Firma                    | {{< icon "circle-xmark" >}}                                   |
| Texto                    | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL                      | {{< icon "circle-xmark" >}}                                   |
| Número                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Última edición           | {{< icon "circle-xmark" >}}                                   |

## Valores por defecto referenciados en columnas de texto

Si especifica la referencia **{creator.name}** o **{creator.id}** como valor por defecto en una [columna de texto]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}), el **nombre** o **ID del usuario** que añadió la línea se introduce automáticamente.

![Referenciar el nombre de usuario con un valor por defecto](images/Set-creator-name-as-default-value.png)

## Alcance de los valores por defecto

Los valores por defecto se aplican **siempre que** se puedan crear nuevas líneas:

- en una [tabla]({{< relref "help/base-editor/zeilen/hinzufuegen-einer-zeile" >}})
- en una [columna de enlaces]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})
- mediante [un botón]({{< relref "help/base-editor/schaltflaechen/zeilen-per-schaltflaeche-in-eine-andere-tabelle-kopieren" >}}) (acción: "Copiar fila a otra tabla")
- mediante [automatización]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) (acciones: "Añadir fila" y "Añadir nueva entrada en otra tabla")
- en la [vista Calendario, Kanban, Galería y Árbol]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}})
- mediante [formularios web]({{< relref "help/base-editor/webformulare/webformulare" >}})
- en las [páginas de]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}), [formularios]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}) y [Kanban]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kanbanseiten-in-universellen-apps" >}}) de las aplicaciones

![El valor por defecto se aplica en todas las líneas nuevas](images/Standardwert-greift-ueberall-bei-neuen-Zeilen.gif)

## Valores por defecto en formularios web

Además de los valores por defecto definidos en la tabla, [los formularios web]({{< relref "help/base-editor/webformulare/webformulare" >}}) también permiten establecer valores por defecto para los campos del formulario vinculados a las columnas. También puede establecer si se permite a los usuarios **cambiar** estos valores por defecto al rellenar el formulario.

![Establecer valores por defecto en formularios web](images/Set-default-values-in-web-forms.png)

{{< warning  headline="Nota importante"  text="Si se define un valor por defecto tanto en la tabla como en el formulario web, el valor del formulario se aplica a todas las filas que se creen a través del formulario web. Los valores por defecto definidos en la tabla **sólo tienen** efecto si no se define ningún valor por defecto en el editor de formularios." />}}

## Valores por defecto en las aplicaciones

Los valores por defecto definidos en la base también afectan a las filas que se introducen en las páginas de **tabla, formulario y Kanban** de las [aplicaciones]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}). El único [tipo de página]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) para el que todavía se pueden establecer valores por defecto en la app es [la página de]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}) formulario. Los ajustes funcionan exactamente igual que para los formularios web: Para ello, active los controles deslizantes como se muestra en la captura de pantalla anterior.
