---
title: 'Eliminar aplicaciones'
date: 2023-05-02
lastmod: '2026-11-16'
categories:
    - 'apps'
author: 'nsc2'
url: '/es/ayuda/eliminar-apps-definitivamente-seatable'
aliases:
    - '/es/ayuda/apps-loeschen'
seo:
    title: 'Elimine apps de su base SeaTable de forma definitiva'
    description: 'Elimine las aplicaciones que ya no necesita directamente desde su base SeaTable. Solo administradores o propietarios pueden hacerlo; datos y tablas se mantienen intactos.'

---

¿Desea eliminar de su base una aplicación que ya no necesita? ¡No hay problema! Esto se puede hacer en cualquier momento con solo unos pocos clics.

{{< warning  headline="Autorización necesaria en el grupo"  text="Para poder eliminar una aplicación, debe ser el **propietario** o **administrador del grupo** en el que se encuentra la **base** subyacente. Los simples **miembros del grupo** no están autorizados a hacerlo." />}}

## Eliminar una aplicación de una base

1. Abra la **base** donde desea eliminar una aplicación.
2. Haga clic en **Aplicaciones** en la cabecera Base.

![Haga clic en Aplicaciones en la cabecera Base](images/click-apps-in-the-base-header.jpg)

3. Pase el ratón por encima de la aplicación deseada y haga clic en los **tres puntos** de la derecha.
4. Seleccione **Eliminar**.
5. Confirme con **Eliminar**.

![Eliminar una aplicación](images/Delete-an-app.gif)

{{< warning  headline="La eliminación es definitiva" >}}

No **se puede recuperar** una aplicación eliminada. Si no está seguro de si podrá usar una aplicación en una fecha posterior, es mejor [deshabilitarla temporalmente]({{< relref "help/app-builder/app-verwaltung/apps-zeitweise-deaktivieren" >}}).

{{< /warning >}}

## Consecuencias de la supresión

Lo primero es lo primero: al borrar una **aplicación nunca se pierden los datos de la base subyacente**. Así que técnicamente solo está eliminando una interfaz de usuario y _no_ la base de datos en segundo plano.

Sin embargo, tenga en cuenta que cuando elimina una aplicación, todas las [páginas y carpetas]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) que se encuentran en la **aplicación** también **se eliminan de forma permanente** y _no se pueden restaurar_.
