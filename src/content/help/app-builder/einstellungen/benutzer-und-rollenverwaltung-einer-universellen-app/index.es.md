---
title: 'Administración de usuarios y roles de una aplicación'
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
    description: 'Añada usuarios, asigne roles y cree enlaces de invitación para administrar permisos en las aplicaciones de SeaTable. Guía completa.'
---

Ya sea añadir **nuevos usuarios**, asignar **roles** o crear **enlaces de invitación**: en la administración de usuarios y roles de una aplicación puede llevar a cabo diversas tareas administrativas. Puede acceder a la **administración de usuarios y roles** a través del modo de edición de su aplicación.

{{< warning  headline="Permiso necesario en el grupo"  text="Para poder editar una aplicación, debe ser **propietario** o **administrador del grupo** en el que se encuentra la **base** subyacente. Los **miembros del grupo** normales solo pueden ver y utilizar las aplicaciones." />}}

## Administración de usuarios y roles de la aplicación

1. Abra una **base** a la que ya haya añadido una aplicación.
2. Haga clic en **Aplicaciones** en la cabecera de la base.
   ![Haga clic en Aplicaciones en la cabecera de la base](images/click-apps-in-the-base-header.jpg)
3. Pase el ratón por encima de la aplicación y haga clic en el **icono del lápiz** {{< seatable-icon icon="dtable-icon-rename" >}}.
   ![Haga clic en el icono del lápiz](images/add-page-to-universal-app-1.png)
4. Abra la **administración de usuarios y roles** en la parte superior izquierda de la página.
   ![Icono de la administración de usuarios y roles](images/Symbol-fuer-Benutzer-und-Rollenverwaltung.png) 
5. Realice los **ajustes** deseados.

## Los ajustes en detalle

### Usuarios

En la primera sección encontrará un resumen de todos los **usuarios** que tienen acceso a su aplicación. Además, aquí también encontrará el **rol** y el **estado** de cada usuario.

![Resumen de la pestaña Usuarios de la administración de usuarios y roles de una aplicación](images/user-and-role-management-overview-1.png)

En esta sección también dispone de diversas opciones para **gestionar los usuarios actuales** de su aplicación.

Utilice la **función de búsqueda** para encontrar un usuario concreto. Esta función puede resultar especialmente útil si su aplicación tiene un gran número de usuarios.

![Función de búsqueda para usuarios de la aplicación](images/search-function-app-users.png)

Para añadir un usuario a la aplicación, haga clic en **Importar usuarios**, búsquelo en el campo de entrada y, a continuación, asígnele un rol.

![Haga clic en Importar usuarios](images/import-user-to-app.jpg)

![Importación de un usuario a su aplicación](images/import-users-to-app.png)

Haga clic en **Sincronizar usuarios con la base** para recopilar automáticamente los **usuarios de la aplicación** en una tabla de su base.

![Haga clic en Sincronizar usuarios con la base](images/click-sync-users-to-base-1.jpg) ![Tabla en la que se recopilan automáticamente los usuarios de la aplicación](images/table-with-app-users.png)

Si en el futuro añade más usuarios de esta forma, siempre puede volver a hacer clic en **Sincronizar usuarios con la base** para añadir los **nuevos usuarios** a la tabla.

![Si en el futuro añade más usuarios a su aplicación, ...](images/if-you-add-more-users-to-your-app.png)

![... siempre puede volver a hacer clic en Sincronizar usuarios con la base para añadir automáticamente los nuevos usuarios a la tabla.](images/added-imported-app-users-to-table.png)

Para **eliminar** un usuario de la aplicación, basta con hacer clic en el **icono X**, que encontrará a la derecha del estado del usuario correspondiente.

![Eliminar usuario](images/delete-user.jpg)

Haciendo clic en los **iconos de lápiz** {{< seatable-icon icon="dtable-icon-rename" >}} que encontrará para cada usuario, puede editar su **rol** y su **estado**.

{{< warning  headline="Nota importante"  text="Tenga en cuenta que el **usuario** que ha añadido la aplicación a la base se registra automáticamente como **Admin**. **No** es posible editar ni el rol ni el estado de este usuario, y tampoco se le puede eliminar de la aplicación." />}}

![Iconos de edición para cada usuario](images/edit-icons-users.jpg)

Para el **rol de un usuario**, el menú desplegable le ofrece todos los roles que puede definir en la siguiente sección de la administración de usuarios y roles.

![Selección del rol de un usuario](images/select-role-of-user.png)

El **estado** de un usuario puede establecerse en **Activo** o **Inactivo**. Mientras que los usuarios **activos** tienen acceso a la aplicación y a su contenido, los usuarios **inactivos** pierden este acceso.

![Edición del estado de un usuario de la aplicación](images/edit-status-of-app-user.png)

Los usuarios que no tienen acceso a su aplicación ven este mensaje:

![Acceso denegado a la aplicación para usuarios inactivos](images/no-permission-for-inactive-users.png)

### Roles

En esta sección puede definir cualquier número de **roles** que podrá asignar a los distintos usuarios de la aplicación en la sección anterior.

![Definición de diferentes roles para los usuarios de la aplicación](images/define-roles-for-app-users.jpg)

Aquí solo establece primero los **nombres** de los roles. Qué **permisos** tienen los usuarios con los distintos roles es algo que puede definir individualmente para cada página de la aplicación.

[Obtenga más información sobre los permisos de página aquí.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

### Enlace de invitación

En la tercera sección de la administración de usuarios y roles, puede generar un **enlace de invitación** individual para la aplicación.

En primer lugar, establezca el **rol** de los usuarios que accederán a la aplicación mediante el enlace de invitación.

![Selección del rol que recibirán los usuarios que accedan a la aplicación mediante el enlace de invitación](images/select-role-for-invite-link.png)

A continuación, tiene la opción de establecer una **contraseña** que se deberá introducir tras abrir el enlace de invitación para obtener acceso a la aplicación.

![Añadir una contraseña al enlace de invitación](images/add-password-protection.png)

Opcionalmente, también puede añadir al enlace de invitación un **tiempo de caducidad** automático que determine cuánto tiempo es válido.

![Añadir un tiempo de caducidad automático al enlace de invitación](images/add-auto-expiration.png)

Haga clic en **Generar** para crear el enlace de invitación. A continuación, el enlace se mostrará abajo y tendrá la opción de **copiarlo** o **eliminarlo**.

![Enlace de invitación generado con las opciones disponibles para copiarlo y eliminarlo](images/copy-and-delete-link-universal-app.png)

Como alternativa, tiene la opción de generar un **código QR** para abrir y compartir la aplicación.

![Mostrar el código QR para abrir y compartir la aplicación](images/show-qr-code-universal-app.png)

Escanee el **código QR** mostrado para abrir su aplicación, o compártalo con otros usuarios para darles **acceso** a su aplicación.

![Código QR para abrir y compartir la aplicación](images/qr-code-to-share-universal-app.png)
