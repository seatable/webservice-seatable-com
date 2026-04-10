---
title: 'Galerieseiten in SeaTable Apps'
date: 2023-12-04
lastmod: '2024-08-02'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/de/hilfe/galerieseiten-in-seatable-apps'
aliases:
    - '/de/hilfe/galerieseiten-in-universellen-apps'
seo:
    title: 'Galerieseiten in SeaTable Apps: Anleitung'
    description: 'Erstellen Sie Galerieseiten in SeaTable Apps: Bilder & Datensätze als Galerie, Filter, Berechtigungen & verknüpfte Tabellen flexibel nutzen.'
weight: 4
---

Mithilfe dieses Seitentyps können Sie **Bilder** und andere Daten, die Sie in Ihrer Tabelle gespeichert haben, in Form einer **Galerie** innerhalb einer App anzeigen lassen. Eine Galerieseite könnten Sie zum Beispiel für übersichtliche **Steckbriefe Ihrer Mitarbeiter** verwenden.

![Darstellung Ihrer Mitarbeiter in einer Galerie-Seite](images/page-type-gallery-example.png)

## Seiteneinstellungen

Wenn Sie die Einstellungen einer Seite ändern möchten, klicken Sie in der Navigation auf das entsprechende {{< seatable-icon icon="dtable-icon-set-up" >}} **Zahnrad-Symbol**.

![Einstellungen der Galerieseite ändern](images/Einstellungen-der-Galerieseite-aendern.png)

In den **Seiteneinstellungen** können Sie die **Tabelle**, die **Bild-Spalte** und die **Titel-Spalte** auswählen, aus denen die Galerie gespeist wird.

![Seiteneinstellungen der Galerieseite in SeaTable Apps](images/Seiteneinstellungen-der-Galerieseite-in-Universellen-Apps.png)

## Voreingestellte Filter, Sortierungen und ausgeblendete Spalten

Darüber hinaus können Sie voreingestellte Filter, Sortierungen und ausgeblendete Spalten definieren, um die angezeigten Daten für die Nutzer einzugrenzen und zu ordnen. Zum Filtern oder Sortieren klicken Sie auf **Filter hinzufügen** oder **Sortierung hinzufügen**, wählen Sie die gewünschte **Spalte** und **Bedingung** aus und bestätigen mit **Abschicken**.

![Add filter on gallery pages in SeaTable Apps](images/Add-filter-on-gallery-pages-in-Universal-Apps.png)

Die Nutzer können sich mehr Informationen zu einer Karteikarte in der Galerie anzeigen lassen, indem sie auf einen Eintrag klicken.

![Eintrag auf der Galerieseite öffnen](images/Eintrag-auf-der-Galerieseite-oeffnen.gif)

Entscheiden Sie daher, welche Daten **sichtbar** sein sollen, und blenden Sie die entsprechenden Spalten mithilfe der **Regler** ein oder aus.

![Hide columns on gallery pages in SeaTable Apps](images/Hide-columns-on-gallery-pages-in-Universal-Apps-1.png)

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="**Voreingestellte Filter**, **Sortierungen** und **ausgeblendete Spalten** können die App-Nutzer **nicht verändern**. Sie bekommen also, wie von Ihnen gewünscht, nur die gefilterten Einträge in einer festen Reihenfolge angezeigt." />}}

## Einstellungen der Verknüpfungsspalte

In den **Einstellungen der Verknüpfungsspalte** können Sie für jede verknüpfte Tabelle festlegen, welche Daten sichtbar und welche Operationen erlaubt sind.

![Link column settings on table pages in SeaTable Apps](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Hinzufügen neuer Einträge erlauben**: Wenn Sie diesen Regler aktivieren, können Nutzer neue Einträge in der verknüpften Tabelle hinzufügen. Über die Feldeinstellungen können Sie definieren, welche Spalten dabei **sichtbar** und welche Spalten **erforderlich** sind, also ausgefüllt werden müssen.
- **Verknüpfen bestehender Einträge erlauben**: Wenn Sie diesen Regler aktivieren, können Nutzer bestehende Einträge der verknüften Tabelle verlinken. Über die Feldeinstellungen können Sie definieren, welche Spalten dabei **sichtbar** sind.
- **Verknüpfungen auf maximal eine Zeile begrenzen**: Wenn Sie diesen Regler aktivieren, können Nutzer in den Zellen der Verknüpfungsspalte nur noch jeweils eine Zeile der verknüpften Tabelle verlinken.
- **Voreingestellte Filter**: Wenn Sie hier einen Filter hinzufügen, werden beim Verlinken von Einträgen nur Optionen angezeigt, die die Filterbedingungen erfüllen.
- **Big-Data-Funktion aktivieren**: Wenn die Big-Data-Funktion aktiviert ist, können Nutzer mehr als 20.000 Datensätze durchsuchen, sofern in der verknüpften Tabelle so viele Einträge vorhanden sind.

## Seitenberechtigungen

Für Galerieseiten können Sie folgende [Seitenberechtigungen]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) festlegen:

![Seitenberechtigungen von Galerieseiten](images/Seitenberechtigungen-von-Galerieseiten.png)

Entscheiden Sie, wer die Galerieseite sehen, Zeilen hinzufügen, bearbeiten und löschen darf. Dank der differenzierten Berechtigungsoptionen dieses Seitentyps können Sie dies genauestens einstellen.
