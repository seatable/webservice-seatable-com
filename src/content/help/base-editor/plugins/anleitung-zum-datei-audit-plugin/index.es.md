---
title: 'Instrucciones para el plugin de auditoría de archivos'
date: 2026-11-26
lastmod: '2026-11-26'
categories:
    - 'plugins'
author: 'bha'
url: '/es/ayuda/guia-plugin-auditoria-archivos'
aliases:
    - '/es/ayuda/anleitung-zum-datei-audit-plugin'
seo:
    title: 'Guía del plugin de auditoría de archivos de SeaTable'
    description: 'El plugin de auditoría de archivos de SeaTable localiza los archivos que una base ya no usa, las referencias a archivos que faltan y qué ocupa su almacenamiento.'
---

El **plugin de auditoría de archivos** examina los **archivos almacenados en su base**: todo lo que se ha subido a la base —en las columnas de archivo, de imagen y de firma, en los textos largos, en los comentarios, los formularios y las apps—, además de los archivos de sus propias carpetas personalizadas del [gestor de archivos]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}). Compara lo que hay en el almacenamiento con lo que su base referencia realmente, e informa de la diferencia en ambos sentidos: **archivos que ya nadie usa** y **referencias a archivos que ya no existen**. También le muestra en qué se va el espacio.

En SeaTable, el almacenamiento se llena sin que uno se dé cuenta, porque quitar un archivo de una celda **no lo elimina**: el archivo permanece en el gestor de archivos de la base para que se pueda [restaurar]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}}). Con el tiempo, una base puede acabar almacenando mucho más de lo que muestran sus filas.

El plugin no necesita ninguna configuración: la primera vez que lo abre, la auditoría se ejecuta sola. Ejecutar la auditoría no modifica nada: los archivos solo se eliminan y las referencias solo se quitan cuando usted lo pide, elemento por elemento o grupo por grupo.

{{< zoom image="images/file-audit-plugin.png" alt="El plugin de auditoría de archivos mostrando el almacenamiento de una base por carpeta y sus recursos huérfanos" >}}

Puede averiguar cómo activar un plugin en una base [aquí]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

## Cómo funciona la auditoría {#how-the-audit-works}

Una auditoría hace tres cosas:

1. **Lista el almacenamiento de la base**: cada archivo, con su carpeta y su tamaño.
2. Recopila todos los archivos que la base **referencia**, dondequiera que se usen:
    - las **columnas de archivo y de imagen** de todas las tablas, y las **firmas** de las columnas de firma,
    - las imágenes insertadas en las celdas de **texto largo**,
    - las imágenes de la **descripción de la base** y de los **comentarios de las filas**,
    - las imágenes de los **formularios web** de la base y de los formularios de sus **apps**,
    - las **filas archivadas**, que se leen como las demás.
3. Comprueba las **otras bases a las que usted tiene acceso**, para encontrar en ellas filas que muestren archivos almacenados en esta base (véase [Archivos compartidos entre bases](#files-shared-between-bases) más abajo).

A continuación compara las listas y muestra el resultado. La auditoría se ejecuta con **sus propios permisos** —no hay que crear ningún token— y el informe se guarda con la base: cuando vuelve a abrir el plugin, encuentra el último resultado, con su fecha, en lugar de una nueva ejecución. **Volver a ejecutar la auditoría** la inicia de nuevo, algo que conviene hacer después de cualquier cambio.

{{< warning type="warning" headline="Los scripts no se auditan" text="Los **scripts** de la base se almacenan como archivos propios, pero el plugin no los ve en absoluto: igual que en el gestor de archivos, no aparecen en el árbol de recursos de la base, su tamaño no se cuenta y **su contenido no se lee**, de modo que un archivo que use un script no se considera una referencia. Aun así, los scripts son recursos de la base: al exportarla, **solo la opción «Include assets» los conserva**." />}}

## Qué muestra el plugin

### Resumen y almacenamiento por carpeta

La parte superior del informe resume la situación: el **total de recursos en almacenamiento**, cuántos están **referenciados en la base**, cuántos son **huérfanos** y qué parte del almacenamiento representan, y después el número de **referencias faltantes** y de **URLs externas**.

**Almacenamiento por carpeta** muestra en qué se va el espacio. Haga clic en una carpeta para ver su detalle. Sus propias carpetas (**carpetas personalizadas**) se muestran aparte de las **carpetas del sistema** que SeaTable crea para las columnas de archivo y de imagen, las firmas, los formularios y las apps. Algunas carpetas del sistema contienen archivos que SeaTable necesita para que la base funcione y que, por diseño, ninguna fila referencia —archivos de plugins, las páginas y la configuración de cada app, logotipos e imágenes de fondo de los formularios, y plantillas de diseño de páginas—: se marcan como **Carpeta del sistema — NO ELIMINAR** y nunca aparecen como huérfanos. En cambio, los archivos que los usuarios suben a través de una app se auditan como cualquier otro archivo subido.

### Recursos huérfanos {#orphaned-assets}

Un **recurso huérfano** es un archivo del almacenamiento al que ya no hace referencia ninguna fila: normalmente, un archivo quitado de una celda o uno que ha quedado tras eliminar una fila. La lista se agrupa por carpeta: puede eliminar un solo archivo o todos los archivos huérfanos de una carpeta a la vez.

Si uno de los lugares enumerados [más arriba](#how-the-audit-works) **no se ha podido leer** durante una ejecución —los comentarios o las filas archivadas, por ejemplo—, la sección lo indica y **la eliminación queda desactivada** en esa ejecución: de lo contrario, se propondría eliminar todos los archivos que solo se usan allí. Vuelva a ejecutar la auditoría para intentarlo de nuevo.

Antes de eliminar nada, lea las advertencias de esa sección y las [limitaciones](#limitations) que se describen más abajo: un huérfano es un archivo *al que el plugin no ha encontrado ninguna referencia*, lo que no es exactamente lo mismo que un archivo que nadie necesita.

{{< warning type="warning" headline="Los archivos eliminados van a la papelera" text="Los archivos que elimina el plugin van a la **papelera** del gestor de archivos, donde permanecen **60 días** y pueden restaurarse. Pasado ese plazo, o una vez vaciada la papelera, se pierden definitivamente: las instantáneas no incluyen archivos. Para conservar una copia de seguridad completa, **exporte la base con la opción «Include assets»** antes de eliminar nada." />}}

### Referencias faltantes

Una **referencia faltante** es lo contrario: una fila cuya columna de archivo o de imagen apunta a un archivo que **ya no existe** en el almacenamiento. La celda sigue mostrando una entrada, pero no hay nada detrás. Puede quitar la referencia obsoleta de una fila, de todas las filas de una columna o de todas partes a la vez. El resto de la celda no se modifica.

### URLs externas

Las columnas de imagen también pueden contener enlaces a archivos **alojados fuera de SeaTable**. El plugin los lista, agrupados por tabla y columna. No se comprueban durante la auditoría, porque la ralentizaría: inicie usted mismo la comprobación con **Verificar URL externas**. Cada enlace aparece entonces como **correcto**, **roto** o **no verificable**: muchos sitios no permiten que un navegador compruebe sus archivos desde otro sitio, así que *no verificable* no significa que el enlace esté roto. Después puede quitar los enlaces rotos.

### Archivos compartidos entre bases {#files-shared-between-bases}

Las dos últimas secciones tratan de los **archivos que pasan de una base a otra**, un caso fácil de pasar por alto y la razón por la que el plugin comprueba sus otras bases en cada auditoría.

Cuando **copia una celda o una fila** de una base a otra, SeaTable copia la referencia al archivo, **no el propio archivo**. El archivo sigue almacenado en la base original y la otra base lo muestra desde allí, aunque esté en otro espacio de trabajo. Nada en ninguna de las dos bases indica que ahora están vinculadas. **Importar una tabla** desde otra base funciona de otro modo: también copia los archivos, de modo que después las dos bases son independientes. **Prefiera este método** siempre que necesite los archivos en ambas bases.

- **Archivos usados por otras bases** lista los archivos almacenados en *esta* base que muestran filas de *otra* base. Se excluyen de la lista de huérfanos, aunque ya nada en esta base haga referencia a ellos: eliminar uno rompería la otra base.
- **Referencias a archivos de otras bases** es el caso inverso: filas de *esta* base que muestran un archivo almacenado en *otra* base. Aquí no son ni huérfanos ni referencias faltantes, y el plugin no puede comprobar si esos archivos siguen existiendo.

Un archivo mostrado de esta forma conserva los **permisos de la base que lo almacena**. Las personas que no tienen acceso a esa base ven una **celda vacía** donde usted ve el archivo, así que la misma fila puede verse de forma distinta para dos personas.

## Permisos y seguridad

- Con acceso de **solo lectura** a la base, puede leer todo el informe, pero los botones para eliminar y quitar no están disponibles.
- En un **grupo** que usted no administra, puede seguir eliminando archivos, pero el plugin le advierte de que pueden haberlos subido otros miembros y le pide una confirmación explícita.
- Antes de modificar una fila por primera vez —al quitar una referencia faltante o un enlace roto—, el plugin crea una **instantánea** de la base. Esta le permite recuperar el **contenido de las celdas** que el plugin ha quitado: los nombres de archivo y los enlaces, no los propios archivos. Eliminar archivos no modifica ninguna fila y no está cubierto: las instantáneas no incluyen archivos (véase la advertencia [más arriba](#orphaned-assets)).

## Limitaciones {#limitations}

{{< warning type="warning" headline="Solo se comprueban las bases a las que usted tiene acceso" text="La búsqueda de referencias en otras bases abarca las bases que usted puede ver: las de sus espacios de trabajo y grupos, y las que se han compartido con usted. Una base de un compañero a la que usted no tiene acceso puede perfectamente mostrar un archivo de la suya, y el plugin no tiene forma de saberlo. **Por tanto, un huérfano del informe nunca es una prueba de que un archivo no se use.** Esas bases nunca aparecen en el informe, ya que el plugin no sabe que existen. Solo las bases que usted puede ver pero que el plugin no ha logrado leer durante una ejecución —tras un error, por ejemplo— se nombran en el informe, junto con el motivo." />}}

La auditoría tiene algunos otros puntos ciegos que conviene conocer antes de eliminar:

- **Solo se leen los lugares enumerados [más arriba](#how-the-audit-works).** Un archivo al que se haga referencia de cualquier otra forma no se considera una referencia y, por tanto, puede aparecer como huérfano: por ejemplo, un archivo cuya dirección está almacenada en una columna de texto o de URL, o que se usa en un script o desde una herramienta externa (orquestador, etc.).
- **Sus propias carpetas cuentan como las demás.** Un archivo que haya subido a una carpeta personalizada del gestor de archivos para guardarlo allí aparece como huérfano mientras ninguna fila haga referencia a él.
- **Los archivos de las carpetas personalizadas no se rastrean entre bases.** Una fila hace referencia a ellos mediante un identificador que no indica qué base los almacena, así que el plugin no puede saber si otra base usa alguno.
- **Una base creada por importación o copia puede seguir usando archivos de la base original.** Cuando importa una base desde un archivo `.dtable` o la copia, sus archivos también se copian, pero algunos lugares conservan sus enlaces a la base original: según cómo se haya creado la base, las imágenes de la descripción de la base, de los formularios web y de los formularios de apps, o los archivos de las filas archivadas. El plugin enumera estos enlaces en **Referencias a archivos de otras bases**, y las copias que dejan sin usar en esta base aparecen como huérfanas. Sus imágenes se cargan desde la base original, y algunas pueden no mostrarse a otras personas, aunque tengan acceso a esa base. Los comentarios de las filas tampoco forman parte de una exportación ni de una copia, por lo que las imágenes insertadas en ellos también quedan huérfanas en la nueva base.
- **El informe describe el momento en que se ejecutó.** Cualquiera puede añadir o quitar una referencia después, en esta base o en otra: vuelva a ejecutar la auditoría antes de eliminar.
- En una cuenta con muchas bases, comprobarlas todas **lleva su tiempo**.

## Otros artículos útiles

- [Todos los plugins de un vistazo]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}})
- [La gestión de archivos de una base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}})
- [Acceso a archivos e imágenes eliminados]({{< relref "help/haeufig-gestellte-fragen/wissen-und-tipps/zugriff-auf-geloeschte-anhaenge" >}})
- [Cómo eliminar archivos permanentemente]({{< relref "help/base-editor/dateien/wie-man-dateien-dauerhaft-entfernt" >}})
- [Activación de un plugin en una base]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}})
