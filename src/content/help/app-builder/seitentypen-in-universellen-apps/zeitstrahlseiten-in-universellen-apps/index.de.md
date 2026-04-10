---
title: 'Zeitstrahlseiten in SeaTable Apps'
date: 2023-12-04
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/de/hilfe/zeitstrahlseiten-in-seatable-apps'
aliases:
    - '/de/hilfe/zeitstrahlseiten-in-universellen-apps'
seo:
    title: 'Zeitstrahlseiten in SeaTable Apps: Projekte & Planung'
    description: 'Zeitstrahlseiten in SeaTable Apps: Termine, Projekte und Urlaube als Timeline visualisieren, bearbeiten und filtern.'
weight: 8
---

Dieser Seitentyp ermöglicht Ihnen die Darstellung verschiedener Zeitspannen in Form eines **Zeitstrahls**. Da diese Datenansicht Überschneidungen von Terminen aufdeckt, könnte beispielsweise die **Urlaubsplanung in einem Unternehmen** ein konkreter Anwendungsfall sein.

![Timeline page in SeaTable Apps](images/Timeline-page-in-Universal-Apps.png)

## Seiteneinstellungen

Wenn Sie die Einstellungen einer Seite ändern möchten, klicken Sie in der Navigation auf das entsprechende {{< seatable-icon icon="dtable-icon-set-up" >}} **Zahnrad-Symbol**.

![Einstellungen der Zeitstrahlseite ändern](images/Einstellungen-der-Zeitstrahlseite-aendern.png)

In den **Seiteneinstellungen** können Sie zunächst die grafische Darstellung der Zeitleisten einstellen. Wählen Sie dazu die [Zeilenfarbe]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}) oder eine [Einfachauswahl-Spalte]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) aus, welche die **Farbe der Blöcke** bestimmt. Auch für die **Beschriftung der Blöcke** können Sie eine Spalte festlegen.

![Grafische Einstellung der Zeitleisten in SeaTable Apps](images/Grafische-Einstellung-der-Zeitleisten.png)

Um den Zeitraum der Einträge zu definieren, benötigen Sie eine [Datum-Spalte]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) für das **Startdatum**. Für das **Enddatum** können Sie eine weitere Datum-Spalte oder eine andere numerische Spalte – [Zahl]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}), [Dauer]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}}) oder [Formel]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) – verwenden, welche die Anzahl an Tagen angibt. Zudem können Sie die **Zeitspanne** auswählen, wie viele Jahre der Zeitstrahl abdecken soll.

![Seiteneinstellungen der Zeitstrahlseite in SeaTable Apps](images/Seiteneinstellungen-der-Zeitstrahlseite-in-Universellen-Apps.png)

## Voreingestellte Filter und ausgeblendete Spalten

Sie können **voreingestellte Filter** und **ausgeblendete Spalten** definieren, um die angezeigten Daten für die Nutzer einzugrenzen. Klicken Sie dazu auf **Filter hinzufügen**, wählen Sie die gewünschte **Spalte** und **Bedingung** aus und bestätigen Sie mit **Abschicken**.

![Add filter on timeline pages in SeaTable Apps](images/Add-filter-on-timeline-pages-in-Universal-Apps.png)

Die Nutzer können sich mehr Informationen zu einem Eintrag anzeigen lassen, indem sie einen Block auf dem Zeitstrahl anklicken. Entscheiden Sie daher, welche Daten **sichtbar** sein sollen, und blenden Sie die entsprechenden Spalten mithilfe der **Regler** ein oder aus.

![Hide columns on timeline pages in SeaTable Apps](images/Hide-columns-on-timeline-pages-in-Universal-Apps.png)

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="**Voreingestellte Filter** und **ausgeblendete Spalten** können die App-Nutzer **nicht verändern**. Sie bekommen also, wie von Ihnen gewünscht, nur die gefilterten Daten angezeigt." />}}

Wenn Sie eine **Gruppierung** hinzufügen, dann kann die Anzeige der Balken auch in **Swimlanes** erfolgen. Bei nicht überlappenden Aktivitäten führt diese Ansichtsoption zu einer kompakten, übersichtlichen Darstellung.

![Grouping on timeline pages](images/Grouping-on-timeline-pages.png)

## Eintrag auf dem Zeitstrahl bearbeiten oder verschieben

Sie können Einträge kinderleicht bearbeiten, indem Sie auf einen **Balken** klicken und in den sich öffnenden **Zeilendetails** die gewünschten Änderungen vornehmen.

![Einträge auf Zeitstrahlseiten ändern](images/Eintraege-auf-Zeitstrahlseiten-aendern.gif)

Noch dazu können Sie direkt auf dem Zeitstrahl die **Zeitspanne verlängern** oder **verkürzen**. Greifen Sie dazu den rechten oder linken **Rand des Balkens** und ziehen Sie ihn bis zum gewünschten Datum.

![Einträge auf Zeitstrahlseiten verschieben](images/Eintraege-auf-Zeitstrahlseiten-verschieben.gif)

Zudem können Sie Einträge auf dem Zeitstrahl komfortabel **per Drag-and-Drop verschieben**. Dabei passt SeaTable automatisch die jeweiligen **Datumswerte** an.

## Seitenberechtigungen

Ganz unten in den Seiteneinstellungen können Sie eingrenzen, wer die Zeitstrahlseite **sehen** und Einträge **bearbeiten** darf. Über Zeitstrahlseiten können Sie keine Zeilen hinzufügen oder löschen.

![Seitenberechtigungen von Zeitstrahlseiten](images/Seitenberechtigungen-von-Kalenderseiten.png)
