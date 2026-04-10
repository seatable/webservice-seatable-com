---
title: 'Kanbanseiten in SeaTable Apps'
date: 2023-12-07
lastmod: '2023-12-07'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/de/hilfe/kanbanseiten-in-universellen-apps'
aliases:
    - '/de/hilfe/kanbanseiten-in-seatable-apps'
seo:
    title: 'Kanbanseiten in SeaTable Apps: Workflows visuell steuern'
    description: 'Erfahren Sie, wie Sie Kanbanseiten in SeaTable nutzen, Karten individuell gestalten, Filter, Sortierungen, Berechtigungen und Big-Data-Optionen optimal einsetzen.'
weight: 7
---

Dieser Seitentyp bietet Ihnen die Möglichkeit, Einträge als Karteikarten auf einem **Kanban-Board** darzustellen. Ein konkreter Anwendungsfall könnte beispielsweise die **Visualisierung von Workflows und Projektfortschritten** sein.

![Kanbanseiten in SeaTable Apps](images/Kanbanseiten-in-Universellen-Apps.png)

## Seiteneinstellungen ändern

Wenn Sie die Einstellungen einer Seite ändern möchten, klicken Sie in der Navigation auf das entsprechende {{< seatable-icon icon="dtable-icon-set-up" >}} **Zahnrad-Symbol**.

![Einstellungen der Kanbanseite ändern](images/Einstellungen-der-Kanbanseite-aendern.png)

Legen Sie in den **Seiteneinstellungen** fest, auf welcher **Tabelle** das Kanban-Board basiert, nach welcher Spalte die Einträge **gruppiert** werden und aus welcher Spalte die **Titel** stammen.

![Seiteneinstellungen der Kanbanseite](images/Seiteneinstellungen-der-Kanbanseite-in-Universellen-Apps.png)

## Voreingestellte Filter, Sortierungen und ausgeblendete Spalten

Darüber hinaus können Sie voreingestellte Filter, Sortierungen und ausgeblendete Spalten definieren, um die angezeigten Daten für die Nutzer einzugrenzen und zu ordnen. Zum Filtern oder Sortieren klicken Sie auf **Filter hinzufügen** oder **Sortierung hinzufügen**, wählen Sie die gewünschte **Spalte** und **Bedingung** aus und bestätigen mit **Abschicken**.

![Add filter on Kanban pages](images/Add-filter-on-kanban-pages-in-Universal-Apps.png)

Die Nutzer können sich mehr Informationen zu einem Eintrag anzeigen lassen, indem sie auf eine Karteikarte klicken. Entscheiden Sie daher, welche Daten **sichtbar** sein sollen, und blenden Sie die entsprechenden Spalten mithilfe der **Regler** ein oder aus.

![Hide columns on Kanban pages](images/Hide-columns-on-gallery-pages-in-Universal-Apps-1.png)

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="**Voreingestellte Filter**, **Sortierungen** und **ausgeblendete Spalten** können die App-Nutzer **nicht verändern**. Sie bekommen also, wie von Ihnen gewünscht, nur die gefilterten Einträge in einer festen Reihenfolge angezeigt." />}}

## Einstellungen der Verknüpfungsspalte

In den **Einstellungen der Verknüpfungsspalte** können Sie für jede verknüpfte Tabelle festlegen, welche Daten sichtbar und welche Operationen erlaubt sind.

![Link column settings on Kanban pages](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Hinzufügen neuer Einträge erlauben**: Wenn Sie diesen Regler aktivieren, können Nutzer neue Einträge in der verknüpften Tabelle hinzufügen. Über die Feldeinstellungen können Sie definieren, welche Spalten dabei **sichtbar** und welche Spalten **erforderlich** sind, also ausgefüllt werden müssen.
- **Verknüpfen bestehender Einträge erlauben**: Wenn Sie diesen Regler aktivieren, können Nutzer bestehende Einträge der verknüften Tabelle verlinken. Über die Feldeinstellungen können Sie definieren, welche Spalten dabei **sichtbar** sind.
- **Verknüpfungen auf maximal eine Zeile begrenzen**: Wenn Sie diesen Regler aktivieren, können Nutzer in den Zellen der Verknüpfungsspalte nur noch jeweils eine Zeile der verknüpften Tabelle verlinken.
- **Voreingestellte Filter**: Wenn Sie hier einen Filter hinzufügen, werden beim Verlinken von Einträgen nur Optionen angezeigt, die die Filterbedingungen erfüllen.
- **Big-Data-Funktion aktivieren**: Wenn die Big-Data-Funktion aktiviert ist, können Nutzer mehr als 20.000 Datensätze durchsuchen, sofern in der verknüpften Tabelle so viele Einträge vorhanden sind.

## Weitere Seiteneinstellungen

Mit drei weiteren Reglern können Sie einstellen, dass SeaTable **leere Zeilen nicht anzeigen**, auf den Karteikarten die **Spaltennamen anzeigen** und **Text umbrechen** soll.

![Weitere Seiteneinstellungen der Kanbanseite](images/Weitere-Seiteneinstellungen-der-Kanbanseite-in-Universellen-Apps.png)

Andere **Daten** aus der zugrundeliegenden Tabelle können Sie ebenfalls auf den Karteikarten anzeigen lassen: Aktivieren Sie dazu beliebig viele **anzuzeigende Felder**.

## Seitenberechtigungen

Für Kanbanseiten können Sie folgende [Seitenberechtigungen]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) festlegen:

![Seitenberechtigungen von Galerieseiten](images/Seitenberechtigungen-von-Galerieseiten.png)

Entscheiden Sie, wer die Kanbanseite sehen, Zeilen hinzufügen, bearbeiten und löschen darf. Dank der differenzierten Berechtigungsoptionen dieses Seitentyps können Sie dies genauestens einstellen.
