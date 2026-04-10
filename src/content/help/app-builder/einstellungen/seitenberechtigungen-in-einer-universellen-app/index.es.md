---
title: 'Permisos de página en una aplicación'
date: 2023-05-03
lastmod: '2023-11-30'
categories:
    - 'universelle-apps'
author: 'nsc2'
url: '/es/ayuda/permisos-de-pagina-en-una-app-universal'
aliases:
    - '/es/ayuda/seitenberechtigungen-in-einer-universellen-app'
seo:
    title: 'Permisos de página en aplicación – guía SeaTable'
    description: 'Descubre cómo configurar y gestionar permisos de página en las aplicaciones de SeaTable para controlar roles y accesos.'
---

{{< required-version "Enterprise" >}}

Para controlar con precisión el **acceso a sus datos**, puede establecer **permisos de página individuales** para cada página que haya creado en una aplicación. Los permisos se editan a través de la configuración de la página.

{{< warning  type="warning" headline="Autorización de página por defecto" text="Cuando crea **páginas nuevas** en su aplicación, éstas conceden inicialmente todos los derechos disponibles a todos los usuarios. Sin embargo, si desea restringir los derechos de uso, deberá ajustar las autorizaciones de página." />}}

## Establecer y editar permisos de página

1. Abra una **Base** a la que ya haya añadido una aplicación.
2. Haga clic en **Aplicaciones** en la cabecera.
![Haga clic en Aplicaciones en la cabecera](images/click-apps-in-the-base-header.jpg)
3. Pase el ratón por encima de la aplicación y haga clic en el **icono del lápiz** {{< seatable-icon icon="dtable-icon-rename" >}}.
![Haga clic en el icono de edición](images/add-page-to-universal-app-1.png)
4. Seleccione la **página** deseada en la navegación de la parte izquierda de la página y haga clic en el **símbolo de la rueda dentada** {{< seatable-icon icon="dtable-icon-set-up" >}}.
![Haga clic en el icono de edición](images/page-permissions-universal-app.png)
5. Establezca los **permisos** deseados en los **ajustes de página** que aparecen en la parte derecha de la página.
![Determinar los permisos de la página](images/page-permissions.png)
6. Los permisos de página definidos se guardan **automáticamente** y se aplican **de inmediato**.

## Qué autorizaciones de página están disponibles

Puede establecer los siguientes permisos de página:

- ¿Quién puede añadir líneas?
- ¿Quién puede editar las líneas?
- ¿Quién puede suprimir líneas?
- ¿Quién puede ver la página?

No todas las autorizaciones de página están disponibles para todos los [tipos de página]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}). Eche un vistazo a esta visión general:

| Page type                             | Add records                                                     | Modify records                                                  | Delete records                                                  | View page                                                       |
| ------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------| --------------------------------------------------------------- | --------------------------------------------------------------- |
| Table page                            | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Form page                             | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Gallery page                          | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Calendar page                         | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Custom page                           | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Kanban page                           | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Timeline page                         | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Query page                            | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Single record page                    | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                     | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## A qué grupos de usuarios puede autorizar

Para cada permiso, puede elegir entre las siguientes opciones para limitar el grupo de personas: **Nadie**, **Administradores**, **Roles específicos** y **Todos**.

![Opciones de permisos de página disponibles ¿Quién puede ver la página?](images/page-permission-who-can-add-records.png)

Seleccione la opción **Roles específicos** para definir sus propios roles. Para ello, cree previamente nuevos **roles** para grupos de usuarios individuales en la [administración de usuarios y roles]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}), a los que podrá asignar permisos individualmente en cada página de la aplicación.

![Definición de funciones específicas que tienen una autorización correspondiente](images/define-roles.png)
