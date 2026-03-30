---
title: 'Compartición de bases y vistas'
date: 2023-01-13
lastmod: '2023-02-22'
categories:
    - 'freigaben'
author: 'cdb'
url: '/es/ayuda/compartir-base-vista-opciones'
aliases:
    - '/es/ayuda/base-und-ansichtsfreigaben-im-ueberblick'
seo:
    title: 'Compartir bases y vistas en SeaTable: opciones, derechos y administración claros'
    description: 'Descubre las opciones para compartir bases, tablas y vistas en SeaTable, gestionar derechos personalizados y controlar la colaboración con facilidad.'
star: true
weight: 1
---

¿Ha organizado su información en una **base**, **tabla** o **vista** y desea **compartirla** con otras personas o trabajar en ella conjuntamente? En SeaTable, esto se hace fácil y rápidamente con un **recurso compartido**. De esta forma puede conceder acceso a sus datos a un único **usuario**, a un **grupo** o a **personas externas**.

En este artículo de explicación y visión general, aprenderá sobre las **opciones de uso compartido** disponibles en SeaTable y cómo utilizarlas eficientemente para colaborar con otros.

## Autorizaciones de Compartición

En SeaTable, tiene la opción de dar acceso a **personas o grupos específicos** a bases, tablas y vistas para trabajar con los datos conjuntamente. Aunque esto tiene muchas ventajas para el **trabajo en equipo**, puede haber **información confidencial** a la que no quiera que todos los miembros del equipo tengan acceso.

Por eso SeaTable le permite definir permisos por niveles en cada recurso compartido. Al especificar si debe ser un recurso compartido **de sólo lectura**, un recurso compartido de **lectura y escritura** o un [recurso compartido personalizado]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}), usted mantiene el control total sobre quién **está** **autorizado a hacer qué en** su base, tabla o vista. Esto significa, por supuesto, que también tienes la posibilidad de **cambiar** y **revocar** permisos.

## Funcionalidad y tipos de desbloqueo

Con un recurso compartido, concedes a otras personas **acceso a** una base, tabla o vista. Los usuarios autorizados verán el recurso compartido como una base separada en la página de inicio, con el usuario que comparte también mencionado. Dependiendo del tipo de recurso compartido, los demás usuarios sólo podrán ver o también editar tus datos.

La compartición puede hacerse a nivel de una **base** o de una **vista**. Si comparte una vista, el usuario autorizado sólo tiene acceso a los datos de esta vista. Las filas y columnas ocultas por la configuración de la vista, así como otras tablas de la base, permanecen ocultas para el usuario.

A cada compartición - ya sea para una base, tabla o vista - se le asigna un nivel de permiso. Los dos permisos básicos son el uso compartido **de sólo lectura** y el uso compartido **con** permisos de **lectura y escritura**.

- **Compartir con derechos de lectura**: Los permisos de lectura permiten a los usuarios ver tablas y datos y cambiar la configuración de la vista, como filtros y agrupaciones. Sin embargo, los usuarios no pueden realizar cambios en las tablas y los datos con este permiso.
- Compartir con derechos **de lectura y escritura**: En el caso de la compartición con derechos de lectura y escritura, los usuarios autorizados pueden realizar cambios en las tablas y los datos, pero no pueden instalar complementos ni compartir la base o la vista con otras personas o grupos.

Para ofrecerle aún más opciones a la hora de compartir una base que en el caso de los dos permisos básicos, SeaTable también ofrece [permisos]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}) de uso compartido personalizados para bases. Con un permiso de uso compartido personalizado, puede **compartir** **varias tablas y vistas** en una base a la vez, incluyendo diferentes niveles de permiso.

Cada compartición, independientemente de la autorización asignada, puede ser **rescindida** en cualquier momento por el propietario o un administrador.

## Compartición de las bases

La Compartición de una base puede hacerse a distintos grupos de personas:

- [Compartición con un usuario]({{< relref "help/startseite/freigaben/anlegen-einer-benutzerfreigabe" >}})
- [Compartición con un grupo]({{< relref "help/startseite/freigaben/eine-base-an-eine-gruppe-freigeben" >}})
- [Compartición a través de un enlace de invitación]({{< relref "help/startseite/freigaben/einladungs-link-erklaert" >}})
- [Compartición a través de un enlace externo]({{< relref "help/startseite/freigaben/externer-link-erklaert" >}})

Al compartir con un usuario o grupo, compartes la base **dentro de tu equipo**. El enlace Compartir por invitación le permite dar acceso a una base a personas **ajenas a su equipo** (pero dentro de SeaTable). Con el enlace externo, usted comparte bases o vistas externamente, independientemente de si alguien tiene una cuenta SeaTable o no.

Todas estas acciones se realizan a través del **diálogo** **compartir** - una ventana a la que puede acceder a través del **icono compartir** {{< seatable-icon icon="dtable-icon-share" >}} en las opciones de la base o a través de la página de **inicio** de SeaTable. Mueva el puntero del ratón a la **base** que desea compartir y haga clic en los **tres puntos** que aparecen a la derecha. A continuación, puede abrir el diálogo de compartir haciendo clic en **Compartir**.

## Gestionar las acciones básicas

La administración de sus recursos compartidos básicos se realiza del mismo modo que su creación a través del diálogo de recursos compartidos. Los recursos compartidos o enlaces existentes se muestran en las respectivas opciones de uso compartido.

Una autorización existente para un usuario o grupo puede ampliarse o restringirse en cualquier momento modificando la autorización de autorización. Para ello, haga clic en el **icono del lápiz** {{< seatable-icon icon="dtable-icon-rename" >}}. Haga clic en el **símbolo x** para finalizar una acción o eliminar un enlace. Todos los cambios tienen efecto inmediato. La protección por contraseña, la fecha de caducidad y la URL **no pueden** modificarse para un enlace existente.

> También puede obtener una visión general de todas las versiones y enlaces a una base en [Bases en la administración]({{< relref "help/teamverwaltung/bases/bases-in-der-teamverwaltung" >}}) del equipo, siempre que sea administrador del equipo.

## Compartición de las tablas

Si no desea [compartir]({{< relref "help/startseite/freigaben/einzelne-tabellenblaetter-einer-base-freigeben" >}}) una base completa, sino sólo [tablas]({{< relref "help/startseite/freigaben/einzelne-tabellenblaetter-einer-base-freigeben" >}}) individuales, por supuesto también es posible. La [compartición personalizada]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}) le permite compartir varias tablas y vistas al mismo tiempo y enviarlas a los miembros de un equipo o a grupos enteros.

## Compartición de las vistas

La compartición de una vista se crea en la tabla abierta. Cuando esté en la vista que desea compartir, haga clic en el **icono** de compartir {{< seatable-icon icon="dtable-icon-share" >}} en las opciones de vista. No lo confunda con el icono de compartir de Base.

![Compartir iconos en una base](images/share-icons-new-1.png)

A continuación, aparecerá el conocido **cuadro de diálogo** para compartir, en el que también podrá crear vistas compartidas del mismo modo que para las bases. Una vista puede compartirse con tres grupos de personas:

- [Compartir a un miembro del equipo]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Compartir a un grupo]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-eine-gruppe" >}})
- [Compartir a través de un enlace externo]({{< relref "help/startseite/freigaben/externen-link-fuer-eine-ansicht-erstellen" >}})

En cuanto haga clic en el botón **Enviar** de una opción de uso compartido, la persona o el grupo seleccionados podrán acceder a la vista con el permiso concedido. Para compartir una vista con varios usuarios o grupos, repita este proceso.

Al igual que con las bases, puede crear un **enlace externo** para compartir la vista públicamente. La vista compartida siempre se muestra a los usuarios autorizados como una **base** en la página de **inicio**.
