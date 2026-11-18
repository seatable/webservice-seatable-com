---
title: 'Gestión de versiones e instantáneas de una aplicación'
date: 2023-11-29
lastmod: '2024-02-16'
categories:
    - 'universelle-apps'
author: 'kgr'
url: '/es/ayuda/control-versiones-y-snapshots-app-universal'
aliases:
    - '/es/ayuda/versionsverwaltung-und-snapshots-einer-universellen-app'
seo:
    title: 'Control de versiones y snapshots en la aplicación'
    description: 'Descubra cómo usar snapshots para guardar, ver, restaurar y gestionar versiones en la aplicación y mantener control total sobre sus cambios.'
---

Puede utilizar **instantáneas** para guardar la versión actual de una aplicación. Puede **crear**, **ver**, **restaurar** y **eliminar** instantáneas en la gestión de versiones del SeaTable App Builder. Además, puede añadir **notas** a las instantáneas individuales para registrar información sobre una versión.

{{< warning  type="warning" headline="Permiso necesario en el grupo"  text="Para poder utilizar las instantáneas de aplicaciones, debe ser **propietario** o **administrador del grupo** en el que se encuentra la **base** subyacente. Los simples **miembros del grupo** no tienen acceso a la gestión de versiones." />}}

## Cuándo son útiles las instantáneas de aplicaciones

Las instantáneas de aplicaciones son **capturas** del estado de una aplicación y funcionan de forma similar a las [instantáneas de base]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}}). Puede utilizar las instantáneas de aplicaciones para guardar la versión actual de una aplicación como copia de seguridad, lo que puede resultar útil, por ejemplo, si va a realizar cambios importantes y es posible que desee restaurar un estado anterior.

{{< warning  type="warning" headline="Cuidado con la pérdida de datos"  text="A diferencia de las instantáneas de base, las instantáneas de aplicaciones **no** guardan **registros**, sino solo la **estructura** y la **configuración** de la aplicación. Esto significa que si modifica o elimina determinadas entradas de la base subyacente a través de la aplicación, no podrá restaurarlas mediante las instantáneas de la aplicación." />}}

### Qué guarda una instantánea de aplicación

Una instantánea de aplicación guarda los siguientes elementos y ajustes:

- [Ajustes]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) como el **nombre**, el **icono** y la **combinación de colores** de la aplicación
- [Páginas y carpetas]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) de la aplicación
- Ajustes y [permisos]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) de las páginas individuales

### Qué no guarda una instantánea de aplicación

Una instantánea de aplicación no guarda:

- la **URL personalizada** de una aplicación
- los **datos** de la base subyacente
- los **comentarios** sobre registros individuales
- los [roles de usuario y enlaces de invitación]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}) de la aplicación

## Crear una instantánea de la aplicación

1. Abra una **aplicación** en [modo de edición]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}).
   ![SeaTable App Builder en modo edición con lista de apps abierta](images/Apps-bearbeiten.png)
2. Haga clic en {{< seatable-icon icon="dtable-icon-history" >}} **Gestión de versiones** en la parte superior izquierda de la página.
   ![Gestión de versiones de una aplicación con lista de snapshots existentes](images/Version-management-in-Universal-App-Builder.png)
3. Se abre una ventana. Cree allí una **nueva instantánea**.
4. Si lo desea, puede añadir una **nota** a la instantánea.
5. Confirme con **Enviar**.

![Creación de un nuevo snapshot de app en la gestión de versiones con nota opcional](images/Version-management-in-Universal-Apps.gif)

{{< warning  headline="Numeración de las versiones"  text="Para cada instantánea se registran la **hora de creación** exacta y un **número de versión**. No se sorprenda si sus instantáneas no reciben números consecutivos (1, 2, 3 …). SeaTable cuenta cada cambio que realice en una aplicación como una versión independiente. Por ello, entre dos instantáneas puede haber rápidamente docenas de versiones." />}}

En cuanto haya creado una instantánea, dispone de cuatro operaciones entre las que elegir:

- **Ver versión**
- **Restaurar versión**
- **Nota**
- **Eliminar versión**

## Ver una instantánea de la aplicación

Antes de restaurar una instantánea y volver precipitadamente a otra versión, debería echar primero un vistazo a esa versión. Para ello, siga el mismo procedimiento que antes: haga clic en los **tres puntos** del extremo derecho de una instantánea y seleccione la operación **Ver versión** en el menú desplegable.

![Vista previa de una versión guardada de la aplicación en el SeaTable App Builder](images/Preview-version-of-app-snapshot.png)

## Restaurar una instantánea de la aplicación

Para restaurar una instantánea de la aplicación, haga clic en los **tres puntos** y seleccione la operación correspondiente en el menú desplegable.

![Diálogo para restaurar un snapshot de la aplicación como versión actual](images/Restore-version-of-app-snapshot.png)

{{< warning  type="warning" headline="Atención"  text="La restauración de instantáneas en el SeaTable App Builder funciona de forma diferente que en la base, donde la instantánea se restaura en una nueva base y se conserva la versión actual. **En el SeaTable App Builder, en cambio, la versión actual se descarta al restaurar una instantánea.**" />}}

En cuanto restaure una instantánea, la aplicación vuelve al estado guardado de esa versión anterior. Todos los **cambios** que haya realizado desde entonces en las páginas, carpetas y ajustes de la aplicación **se perderán**. Por lo tanto, es aconsejable guardar también la versión actual en una instantánea antes de restaurar otra. Así podrá alternar entre diferentes versiones.

## Editar una nota

Si desea añadir, modificar o eliminar posteriormente la nota de una versión, puede hacerlo en cualquier momento. Abra el campo de texto correspondiente haciendo clic en los **tres puntos** del extremo derecho de una instantánea y seleccionando **Nota** en el menú desplegable. Guarde los cambios con **Enviar**.

![Diálogo para editar o añadir una nota a un snapshot de la aplicación](images/Modify-notes-of-app-snapshot.png)

## Eliminar una instantánea de la aplicación

Puede eliminar en cualquier momento una instantánea que ya no necesite. Haga clic en los **tres puntos** del extremo derecho de una instantánea y seleccione la operación **Eliminar versión** en el menú desplegable.

![Diálogo de confirmación para eliminar de forma definitiva un snapshot de la aplicación](images/Delete-version-of-app-snapshot.png)

{{< warning  type="warning" headline="Atención"  text="La eliminación de una instantánea de aplicación es definitiva. El estado guardado de la versión anterior se pierde de forma irrevocable y no se puede restaurar." />}}
