---
title: 'Administración de usuarios y funciones de una aplicación'
date: 2023-05-02
lastmod: '2024-12-13'
categories:
    - 'universelle-apps'
author: 'nsc2'
url: '/es/ayuda/gestion-usuarios-y-roles-app-universal'
aliases:
    - '/es/ayuda/benutzer-und-rollenverwaltung-einer-universellen-app'
seo:
    title: 'Gestión de usuarios y roles en aplicación'
    description: 'Añade usuarios, asigna roles y crea enlaces de invitación para administrar permisos en las aplicaciones de SeaTable. Guía completa.'
---

Ya sea añadiendo **nuevos usuarios**, asignando **roles** o creando **enlaces de** invitación, puedes llevar a cabo varias actividades administrativas en la administración de usuarios y roles de una aplicación. Puede acceder a la administración de usuarios y **roles** a través del modo de edición de su aplicación.

{{< warning  headline="Autorización necesaria en el grupo"  text="Para poder editar una app, debes ser el **propietario** o **administrador del grupo** en el que se encuentra la **base** subyacente. **Los miembros del** grupo simple sólo pueden ver y utilizar las apps." />}}

## Administración de usuarios y funciones de la aplicación

1. Abra una **Base** a la que ya haya añadido una aplicación.
2. Haga clic en **Aplicaciones** en la cabecera Base.

![Haga clic en Aplicaciones en la cabecera Base](images/click-apps-in-the-base-header.jpg)

4. Pase el ratón por encima de la aplicación y haga clic en el **icono del lápiz** {{< seatable-icon icon="dtable-icon-rename" >}}.

![Haga clic en el icono de edición](images/add-page-to-universal-app-1.png)

6. Abra la **administración de usuarios y funciones** en la parte superior izquierda de la página.

![Icono de gestión de usuarios y funciones](images/Symbol-fuer-Benutzer-und-Rollenverwaltung.png)

8. Realice los **ajustes** deseados.

## Los ajustes en detalle

### Usuario

En la primera sección encontrará un resumen de todos los **usuarios** que tienen acceso a su aplicación. Además, también encontrará la **función** y el **estado** del usuario correspondiente.

![Descripción general de la pestaña Usuarios de la administración de usuarios y roles de una aplicación](images/user-and-role-management-overview-1.png)

Esta sección también le ofrece varias opciones para **gestionar los usuarios actuales de** su aplicación.

Utilice la función de **búsqueda para** encontrar un usuario concreto. Esta función puede ser especialmente útil con un gran número de usuarios de la app.

![Función de búsqueda para usuarios de aplicaciones](images/search-function-app-users.png)

Para añadir un usuario a la aplicación, haga clic en **Importar usuario**, busque el usuario en el campo de entrada y asígnele una función.

![Haga clic en Importar usuario ](images/import-user-to-app.jpg)

![Importe un usuario a su aplicación](images/import-users-to-app.png)

Haga clic en **Sincronizar usuarios con Base** para recopilar automáticamente los **usuarios de la App** en una tabla de su Base.

![Haga clic en Sincronizar usuario con base](images/click-sync-users-to-base-1.jpg)  
![Tabla en la que se recogen automáticamente los usuarios de la app](images/table-with-app-users.png)

Si en el futuro añades más usuarios de esta forma, siempre puedes volver a hacer clic en **Sincronizar usuarios con Base** para añadir los **nuevos usuarios** a la tabla.

![Si en el futuro añades más usuarios a su aplicación, ...](images/if-you-add-more-users-to-your-app.png)

![... siempre puede volver a hacer clic en Sincronizar usuarios con Base para añadir automáticamente los nuevos usuarios a la tabla.](images/added-imported-app-users-to-table.png)

Para **eliminar** un usuario de la aplicación, basta con hacer clic en el **símbolo X**, que encontrará a la derecha del estado del usuario en cuestión.

![Borrar usuario](images/delete-user.jpg)

Haciendo clic en los **iconos de lápiz** {{< seatable-icon icon="dtable-icon-rename" >}}, que encontrará para cada usuario, podrá editar su **función** y su **estado**.

{{< warning  headline="Nota importante"  text="Tenga en cuenta que el **usuario** que ha añadido la aplicación a Base se registra automáticamente como **Admin**. Tanto el rol como el estado de este usuario **no pueden** ser editados y el usuario no puede **ser** eliminado de la app." />}}

![Edición de iconos para cada usuario ](images/edit-icons-users.jpg)

Para la **función de un usuario,** todas las funciones están disponibles para su selección en el menú desplegable, que puede definir en la siguiente sección de la administración de usuarios y funciones.

![Seleccionar el rol de un usuario ](images/select-role-of-user.png)

El **estado de** un usuario puede ser **Activo** o **Inactivo**. Mientras que los usuarios **activos** tienen acceso a la app y a su contenido, los **inactivos** pierden este acceso.

![Editar el estado de un usuario de la aplicación](images/edit-status-of-app-user.png)

Los usuarios que no tengan acceso a su aplicación verán este mensaje:

![Denegación de acceso a la aplicación a los usuarios inactivos ](images/no-permission-for-inactive-users.png)

### Rodillos

En esta sección puede definir cualquier número de **roles**, que puede asignar a los distintos usuarios de la aplicación en la sección anterior.

![Definición de diferentes roles para los usuarios de la aplicación ](images/define-roles-for-app-users.jpg)

Aquí inicialmente sólo se definen los **nombres de** los roles. Puedes definir qué **permisos** tienen los usuarios con los diferentes roles individualmente para cada página de la app.

[Obtenga más información sobre los permisos de página aquí.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

### Enlace de invitación

En la tercera sección de la administración de usuarios y roles, puede generar un **enlace de invitación** individual para la aplicación.

En primer lugar, defina la **función de** los usuarios que acceden a la aplicación mediante el enlace de invitación.

![Selección del rol que se otorgará al usuario que utilizará la aplicación mediante el enlace de invitación.](images/select-role-for-invite-link.png)

A continuación, tiene la opción de establecer una **contraseña** que deberá introducir tras abrir el enlace de invitación para poder acceder a la aplicación.

![Añadir una contraseña al enlace de invitación](images/add-password-protection.png)

Opcionalmente, también puede añadir un **tiempo de caducidad** automático al enlace de invitación en cuanto a la duración de su validez.

![Añadir caducidad automática al enlace de invitación ](images/add-auto-expiration.png)

Haga clic en **Generar** para crear el enlace de invitación. El enlace se muestra a continuación y tiene la opción de **copiarlo** o **eliminarlo**.

![Enlace de invitación generado con opciones disponibles para copiar y eliminar el enlace de invitación](images/copy-and-delete-link-universal-app.png)

También tiene la opción de generar un **código QR** para abrir y compartir la aplicación.

![Mostrar el código QR para abrir y compartir la aplicación](images/show-qr-code-universal-app.png)

Escanee el **código QR** mostrado para abrir su aplicación o compártalo con otros usuarios para darles **acceso a** su aplicación.

![Código QR para abrir y compartir la aplicación](images/qr-code-to-share-universal-app.png)
