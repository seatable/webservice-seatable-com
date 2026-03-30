---
title: 'Eliminar enlaces externos y enlaces de invitación'
date: 2023-03-02
lastmod: '2023-03-02'
categories:
    - 'freigaben'
author: 'nsc2'
url: '/es/ayuda/eliminar-enlaces-compartidos'
aliases:
    - '/es/ayuda/externe-links-und-einladungs-links-loeschen'
seo:
    title: 'Eliminar enlaces externos y de invitación en SeaTable'
    description: 'Descubra cómo borrar enlaces compartidos externos e invitación en SeaTable, con información sobre permisos y consecuencias de eliminar.'

---

Puede **eliminar** tanto los **enlaces externos** como **los enlaces de invitación** en cualquier momento y de dos formas distintas. Tenga en cuenta qué consecuencias tiene la eliminación para el acceso a sus datos.

## Formas de eliminar enlaces externos y enlaces de invitación

- Supresión mediante el icono de compartir {{< seatable-icon icon="dtable-icon-share" >}} para bases o vistas
- Supresión a través de la [administración del equipo]({{< relref "help/teamverwaltung/abonnement/die-funktionen-der-teamverwaltung-in-der-uebersicht" >}})

{{< warning  headline="Nota"  text="Los enlaces externos están disponibles para las bases y las vistas, los enlaces de invitación sólo para las bases." />}}

## Eliminación mediante el icono de compartir

![Haga clic en el icono de compartir](images/share-single-tablesheets-from-the-base-options.png)

1. Abra la **base** o **vista** cuyo enlace desea eliminar.
2. Haga clic en el **icono de compartir** {{< seatable-icon icon="dtable-icon-share" >}} para bases o vistas.
3. Dependiendo del tipo de enlace que desee eliminar, haga clic en **Enlace de invitación** o **Enlace externo**.
4. Mueva el ratón sobre el enlace y haga clic en el **símbolo x**.

![Eliminar enlaces externos y enlaces de invitación](images/delete-invitation-and-external-links.jpg)

## Supresión a través de la administración del equipo

{{< warning  headline="Sólo para administradores de equipo"  text="Para acceder a la administración del equipo, debe ser **administrador del mismo**." />}}

1. Vaya a la **página de inicio** de SeaTable y haga clic en la **imagen de** su **avatar**.

![Acceso a la dirección del equipo](images/Zugriff-auf-die-Teamverwaltung.png)

3. Abra la **gestión de equipos de** su cuenta.
4. Haga clic en **Bases** en la navegación.
5. Dependiendo del tipo de enlace que desee eliminar, haga clic en **Enlaces de invitación** o **Enlaces externos**.
6. Seleccione el **enlace** que desea eliminar.
7. Confirme la eliminación activando la tecla **Controlador** y haga clic en **Borrar enlace de invitación** (para los enlaces de invitación) o **Suprimir liberación** (para enlaces externos).  
   ![Confirmar la eliminación](images/confirm-delete-invitation-and-external-links-way2.jpg)

{{< warning  headline="Sólo funciona con enlaces de base" >}}

No se puede eliminar un [enlace externo para una vista]({{< relref "help/startseite/freigaben/externen-link-fuer-eine-ansicht-erstellen" >}}) a través de la administración del equipo, sino sólo a través del icono de compartir para las vistas.

{{< /warning >}}

## Consecuencias de la supresión

### Supresión de un enlace de invitación

La supresión de un **enlace de invitación** tiene las siguientes **consecuencias**:

Si los usuarios intentan abrir un enlace de invitación **eliminado**, aparece el siguiente **mensaje de error**.

![Mensaje de error al abrir enlaces de invitación eliminados](images/fehlermeldung-geloeschter-einladungs-link.jpg)

Una vez eliminado el enlace de invitación, **ningún otro usuario** podrá acceder a la base compartida.

{{< warning  headline="Los usuarios invitados conservan el acceso" >}}

Los usuarios que aceptaron tu invitación antes de que se borrara el enlace pueden seguir accediendo a la base compartida y aparecen en la lista de [usuarios compartidos]({{< relref "help/startseite/freigaben/anlegen-einer-benutzerfreigabe" >}}). Sin embargo, por supuesto puedes eliminar el recurso compartido allí.

{{< /warning >}}

### Supresión de un enlace externo

La supresión de un **enlace** externo tiene las siguientes **consecuencias**:

Si los usuarios intentan abrir un enlace externo **eliminado**, aparece el siguiente **mensaje de error**.

![Mensaje de error al eliminar un enlace externo](images/Fehlermeldung-bei-Loeschung-eines-externen-Links.png)

Al eliminar un enlace externo, todos los usuarios **pierden el** acceso a los datos. Incluso los sitios web en los que se ha incrustado una vista a través de un enlace externo ya no pueden mostrar los datos.
