---
title: 'Comentar las filas'
date: 2022-11-16
lastmod: '2025-02-27'
categories:
    - 'arbeiten-mit-zeilen'
author: 'kgr'
url: '/es/ayuda/comentar-filas-seatable'
aliases:
    - '/es/ayuda/die-kommentarfunktion-in-seatable'
    - '/es/ayuda/zeilen-kommentieren'
seo:
    title: 'Comenta filas en SeaTable – comunicación y colaboración'
    description: 'Agrega comentarios a las filas de SeaTable para dar feedback y mantener toda la conversación en contexto. Imágenes y menciones incluidas.'
---

Puede comentar las filas en SeaTable, por ejemplo, para darse su opinión o plantear preguntas dentro de un equipo. No debe llevar a cabo estas **conversaciones** por correo electrónico o en programas de chat, sino preferiblemente directamente donde están los datos, es decir, en la **fila** correspondiente de la tabla. De este modo, incluso semanas y meses después, estará claro cómo se comunicaron y cuál es el estado actual sin tener que buscar durante mucho tiempo.

Si colabora con otros usuarios en una tabla, puede mantener una conversación separada en cada fila individual. Las filas en las que hay una conversación en curso se marcan con un **icono de burbuja** en la primera columna.

¡Pruébelo! Hay **dos maneras** de acceder a la función de comentarios.

## Comentar las filas a través del menú desplegable

1. Haga clic con **el botón derecho del ratón** en una fila para abrir el **menú desplegable**.
2. Seleccione la opción **Comentar fila**.
3. Se abrirá una **columna de comentarios** en la parte derecha de la página.
4. Escriba su comentario y confirme con **Enviar**.

![Comentar filas](images/Kommentieren-einer-Zeile.gif)

## Comentar las filas a través de la vista detallada

1. Mueva el ratón hasta la **numeración** del principio de la fila.
2. Abra **los detalles de la fila** haciendo clic en el **icono de la doble flecha**.
3. En la ventana que aparece, haga clic en el **símbolo de la puerta**, arriba a la derecha.
4. En la categoría de **comentarios** puede escribir comentarios.

![Comentario](images/kommentar.png)

## Añadir miembros del equipo al chat

Puede llamar la atención de los miembros del equipo sobre su comentario añadiéndolos al chat mediante el símbolo **Plus**. También puede añadir un {{< key "@" >}} y el **Nombre del miembro** para añadir miembros del equipo al chat. El miembro recibe un [notificación en SeaTable]({{< relref "help/startseite/benachrichtigungen/sinn-und-zweck-von-benachrichtigungen-in-seatable" >}}) y será notificado de nuevos comentarios en el historial del chat.

## Añadir imágenes a un comentario

También puede añadir **imágenes** a sus comentarios mediante el **icono de imagen** situado debajo del campo de entrada. Éstas sólo son visibles en la ventana de comentarios y no se guardan en una [columna de imágenes]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) de la tabla, sino en la [gestión de archivos de la base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}).

## Visualización de las filas comentadas

En la primera columna de la tabla aparece, para las filas comentadas, un **icono en forma de burbuja de diálogo** con un número que indica el **número de comentarios** en los últimos 180 días. Haga clic en el icono para abrir la columna de comentarios con el historial del chat.

![Muestra los comentarios dentro de una fila](images/kommentar-blase.png)

{{< warning  headline="Nota"  text="Si nadie escribe un nuevo comentario en una fila durante **180 días**, el **icono de burbuja de diálogo** vuelve a **desaparecer**. Los comentarios se conservan y aún pueden consultarse a través de los **detalles de la fila**, pero ya no es visible en la tabla que esta fila fue comentada anteriormente." />}}

## Borrar comentarios y marcar como resuelto

Sólo los **propietarios** y **administradores** de la base y **el creador del comentario** pueden **borrar** comentarios. Para ello, haga clic en los **tres puntos** a la derecha de un comentario y seleccione la opción {{< seatable-icon icon="dtable-icon-delete" >}} **Borrar**.

Todos los usuarios pueden también **marcar comentarios como resueltos** del mismo modo. Los comentarios marcados como resueltos se indican con un color verde.

![Comentario resuelto](images/Kommentare-als-erledigt-markieren-1.png)

## Visibilidad de los comentarios

Los comentarios son visibles para todas las personas con acceso a la tabla. Esto incluye también a las personas que acceden a una tabla a través de una [vista compartida]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}}).

{{< warning headline="Sin comentarios a través de enlaces externos" text="Si comparte una base o una vista a través de un enlace externo, los usuarios no podrán ver ningún comentario en ella." />}}

**Todos los comentarios de las apps** que se basan en la base también son visibles en la base. En las apps, tiene libertad de elección: por defecto, sólo se ven los comentarios publicados en la misma app. Sin embargo, puede activar en los [ajustes de la app]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) que todos los comentarios de la base se muestren también en la app.

## No importar, exportar o copiar comentarios

Los comentarios no se pueden copiar ni migrar y sólo se guardan donde se hicieron originalmente. El comportamiento es el siguiente:

- Al [duplicar filas]({{< relref "help/base-editor/zeilen/duplizieren-einer-zeile" >}}), no se copia ningún comentario. Esto también se aplica a la **manipulación de relleno** y al **copiado y pegado** de filas.
- Las tablas que [importa de otras bases](https://seatable.com/de/hilfe/eine-tabelle-in-einer-base-hinzufuegen/#tabelle-aus-einer-anderen-base-importieren) o cree a partir de un [conjunto de datos compartido]({{< relref "help/startseite/gemeinsame-datensaetze/mit-einem-gemeinsamen-datensatz-eine-neue-tabelle-anlegen" >}}) tampoco contienen comentarios.
- Los comentarios tampoco se guardan en [instantáneas]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}}) o [archivos exportados]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}).