---
title: 'Cambiar la configuración global de una aplicación'
date: 2023-05-03
lastmod: '2025-07-03'
categories:
    - 'universelle-apps'
author: 'kgr'
url: '/es/ayuda/cambiar-ajustes-globales-app-universal'
aliases:
    - '/es/ayuda/einstellungen-einer-universellen-app-aendern'
seo:
    title: 'Cambiar ajustes globales en una aplicación'
    description: 'Descubra cómo personalizar la configuración global, URLs y permisos en una aplicación de SeaTable de forma sencilla.'
---

Dentro de una **aplicación**, puede realizar varios **ajustes globales** que afectan a la configuración y el aspecto de toda la aplicación con sólo unos clics.

## Cambiar la configuración de una aplicación

1. Abra una **base** en la que desee editar una aplicación existente.
2. Haga clic en **Aplicaciones** en la cabecera Base.
![Haga clic en Aplicaciones en la cabecera Base](images/click-apps-in-the-base-header.jpg)
3. Pase el ratón por encima de la aplicación y haga clic en el **icono del lápiz** {{< seatable-icon icon="dtable-icon-rename" >}}.
![Editar aplicaciones](images/Apps-bearbeiten.png)
4. Haga clic en el **símbolo de la rueda dentada** situado en la parte superior izquierda de la página.
![Icono de rueda dentada para los ajustes de la aplicación](images/Zahnrad-Symbol-fuer-App-Einstellungen.png)
5. Realice los ajustes deseados en la **configuración** de la aplicación.

{{< warning  headline="Autorización necesaria en el grupo"  text="Para poder editar una app, debe ser el **propietario** o **administrador del grupo** en el que se encuentra la **base** subyacente. **Los miembros del** grupo simple sólo pueden ver y utilizar las apps." />}}

## Editar el nombre de la aplicación

En la primera sección de la configuración de la aplicación, puede personalizar el **nombre de** la aplicación y guardarlo haciendo clic en **Enviar**.

![Cambiar el nombre de la aplicación](images/Change-app-name.png)

## URL definida por el usuario

En la segunda sección, puede personalizar parte de la **URL** con la que puede llamar y enlazar a su aplicación. Solo tiene que introducir la URL que desea en el **campo de texto** y tener en cuenta los **requisitos** que se indican a continuación al introducirla. A continuación, puede **guardar** y **copiar** la URL introducida.

![Editar URL personalizada](images/Edit-custom-URL.png)

**Requisitos:** La parte de la URL definida por el usuario debe tener entre 5 y 30 caracteres y sólo puede contener **letras (a-z), números (0-9) y guiones**.

## Mostrar y ocultar la navegación

En la tercera sección, puede decidir si la **barra de navegación** debe mostrarse u ocultarse por defecto al abrir la aplicación. La barra de navegación es el área de la izquierda que todos los usuarios utilizan para navegar a las [páginas y carpetas]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) de la app.

![Ocultar la navegación de la aplicación por defecto](images/Hide-app-navigation-by-default.png)

Esta es la configuración por defecto cuando se abre la aplicación por primera vez. Cada usuario de la aplicación puede mostrar y ocultar la barra de navegación según sus necesidades mediante los **iconos** o **combinaciones de teclas** correspondientes.

![Mostrar y ocultar la navegación](images/Hide-and-show-navigation.gif)

## Ajustes para la colaboración

En la cuarta sección, puede decidir si su **lista de empleados** debe ser visible para todos los usuarios de la aplicación. A continuación, puede introducir personas en [columnas de empleados]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) o añadirlas a [comentarios]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}). Si desea que sus empleados permanezcan invisibles para los demás, deberá desactivar esta función.

![Cargar la lista de colaboradores en las aplicaciones](images/Load-collaborator-list-in-apps.png)

También puede establecer si desea cargar los **comentarios desde la base subyacente**. Por defecto, sólo los comentarios escritos en la aplicación son visibles en ésta. Si no desea que los usuarios de la app vean los comentarios de la base, debe desactivar esta función.

{{< warning type="warning" headline="Los comentarios son posibles en estos tipos de página" text="La función de comentarios de la app se encuentra actualmente en las páginas de tabla, galería, kanban, calendario y línea de tiempo." />}}

## Gestión de macrodatos

Esta sección sólo es relevante si ha activado el [almacenamiento]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) en su Base. Las aplicaciones pueden acceder a los datos en el almacenamiento de big data y guardar las entradas creadas a través de la aplicación directamente allí. Sin embargo, las nuevas entradas se guardan en la base por defecto. Para establecer el almacenamiento de big data como **ubicación de almacenamiento de las nuevas entradas**, basta con activar el control deslizante. Como muestra la captura de pantalla, puede especificar para cada tabla si las nuevas filas deben escribirse en la base (casilla vacía) o en el almacenamiento de big data (casilla marcada).

![Gestión de macrodatos en aplicaciones](images/Big-data-management-in-apps.png)

## Acceso abierto

En la última sección, puede establecer un acceso abierto, es decir, hacer que su aplicación sea de acceso público. Para ello, debe permitir el **Acceso de usuarios no registrados**. Cualquiera que llame al enlace podrá entonces ver (pero no modificar) los datos de la aplicación.

![Acceso abierto a una aplicación](images/Open-access-to-an-app.png)

También puede permitir la **Descarga de archivos e imágenes**. Sin embargo, si no desea que todo el mundo pueda utilizar su app sin restricciones, también puede activar la **protección mediante contraseña**. Al acceder a la URL de la app, los usuarios deberán introducir la contraseña correcta para poder ver los datos.

También puede activar que **cada usuario conectado que utilice su aplicación se registre automáticamente como usuario de la aplicación**. Al hacerlo, usted determina qué **rol** se asigna a los usuarios durante el registro. Dependiendo de su [autorización]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) en las páginas individuales, los usuarios con este rol también pueden añadir, editar o eliminar filas.

## Editar la configuración de páginas individuales

Los ajustes mencionados hasta ahora afectan a **toda** una **aplicación**. Si desea cambiar la configuración de una **página individual**, haga clic en el **símbolo de rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}} de la página correspondiente en la navegación.

![Abrir la configuración de la página](images/page-permissions-universal-app.png)
