---
title: 'Sincronización de un conjunto de datos compartidos'
date: 2022-12-15
lastmod: '2024-06-12'
categories:
    - 'gemeinsame-datensaetze'
author: 'nsc2'
url: '/es/ayuda/sincronizar-conjunto-datos-compartido'
aliases:
    - '/es/ayuda/synchronisation-eines-gemeinsamen-datensatzes'
seo:
    title: 'Sincronizar conjunto compartido SeaTable – explicación total'
    description: 'Descubra cómo sincronizar conjuntos de datos compartidos en SeaTable: manual, automático o forzado, detalles y efectos en filas y columnas.'
---

Puede **sincronizar** cualquier tabla que haya creado a partir de un conjunto de datos compartido. SeaTable sincroniza los datos del conjunto de datos compartidos con las columnas idénticas de la tabla. Los valores de estas columnas se **sobrescriben** si usted o los miembros de su grupo han realizado **cambios en el** conjunto de datos compartido desde la última sincronización.

Si desea actualizar las tablas vinculadas al registro de datos compartidos, puede **iniciar la** sincronización en **las tablas individuales por parte del usuario** (principio pull) o **forzarla para todas las tablas** (principio push), siempre que esté autorizado para ello como **creador** del registro de datos compartidos. Como usuario, puede realizar la sincronización **manualmente** en cada tabla o establecer una **sincronización periódica** automática.

## Sincronización manual con un conjunto de datos compartidos

![Sincronización de un conjunto de datos común](images/Synchronisation-eines-gemeinsamen-Datensatez.png)

1. Haga clic en el **icono del triángulo** situado a la derecha del nombre de una tabla creada con un registro común.
2. Haga clic en **Sincronizar con registro**.
3. Haga clic en **Sincronizar ahora**.

![Sincronización manual de un conjunto de datos común](images/Manuelle-Synchronisation-eines-gemeinsamen-Datensatzes.png)

{{< warning headline="Cambio de fecha sólo en caso de modificación" text="La fecha mostrada de la última sincronización sólo cambia si se han **realizado cambios en el registro de datos compartidos** y, por lo tanto, los datos pueden sincronizarse realmente. Si no se ha modificado ningún valor, la fecha de sincronización mostrada tampoco cambia." />}}

Si la sincronización se realiza correctamente, aparece el siguiente mensaje:

![Mensaje en caso de sincronización correcta de un conjunto de datos común](images/Meldung-bei-einer-erfolgreichen-Synchronisation-eines-gemeinsamen-Datensatzes.png)

## Sincronización periódica con un conjunto de datos común

![Sincronización de un conjunto de datos común](images/Synchronisation-2.0.png)

1. Haga clic en el **icono del triángulo** situado a la derecha del nombre de una tabla creada con un registro común.
2. Haga clic en **Sincronizar con registro**.
3. Haga clic en el botón **Activar sincronización automática**.
4. Seleccione si la sincronización automática debe realizarse **diariamente** o **cada hora**.

![Sincronización periódica de un conjunto común de datos](images/Periodische-Synchronisation-eines-gemeinsamen-Datensatzes.png)

### Restricciones a la sincronización periódica

- Actualmente, la sincronización periódica automática sólo se lleva a cabo si se han realizado **cambios** en el registro de datos compartido original.
- La sincronización horaria de un conjunto de datos comunes sólo está disponible actualmente para los usuarios con una **suscripción Enterprise**.

## Forzar la sincronización de todas las tablas dependientes

![Forzar la sincronización del conjunto de datos común](images/Force-sync-of-common-dataset.png)

1. Pase de la página de inicio a la zona de **Ficheros compartidos**.
2. Sitúe el ratón sobre el **registro de datos compartidos** que desea sincronizar y haga clic en los **tres puntos** del extremo derecho.
3. Haz clic en **Forzar sincronización**.

![Elija las bases para la sincronización con el conjunto de datos común](images/Choose-bases-for-sync-with-common-dataset.png)

4. Seleccione las **bases** que desea sincronizar con el conjunto de datos compartidos.
5. Confirme con **Forzar sincronización**.

Puede utilizar esta función para asegurarse de que los demás usuarios utilizan el estado actual del conjunto de datos compartidos en sus bases. De lo contrario, deberá confiar en que los usuarios hayan activado la sincronización automática o realicen ellos mismos la sincronización de forma periódica.

{{< warning headline="Autorización necesaria" text="Sólo puede forzar la sincronización si está autorizado a hacerlo como **creador** del registro de datos compartidos." />}}

## Efectos de la sincronización en la tabla

### Filas

- Las filas contenidas en la tabla pero no en el registro de datos compartidos se **eliminan** de la tabla.
- Las filas contenidas tanto en la tabla como en el registro de datos compartidos se **sobrescriben** en la tabla si se han realizado cambios desde la última sincronización.
- Las filas que no están contenidas en la tabla pero sí en el registro de datos compartidos se **añaden** a la tabla.
- Las filas que se han filtrado en el registro de datos compartidos desde la última sincronización también **desaparecen** de la tabla.

### Columnas

- Si ha **añadido nuevas columnas** al registro de datos compartidos, éstas también se **añadirán** a la tabla.
- Si **elimina columnas** del conjunto de datos compartidos, éstas permanecen en la tabla, pero los datos **dejan de estar sincronizados**.
- Si **oculta columnas** en el conjunto de datos compartidos, seguirán siendo visibles en la tabla, pero los datos **dejarán de estar sincronizados**.
- Si **se modifica el tipo de columna** en el registro de datos compartidos, también se **modificará** en la tabla.
- Si se [añaden nuevas columnas]({{< relref "help/startseite/gemeinsame-datensaetze/eine-mit-einem-gemeinsamen-datensatz-erstellte-tabelle-um-spalten-erweitern" >}}) a la tabla que no están contenidas en el conjunto de datos compartidos, éstas **no se sincronizan** y permanecen **inalteradas**.
- Si **cambia el nombre de las columnas del conjunto de datos compartido** en la tabla, los nombres de las columnas **no se sincronizan** y permanecen **modificados**.
