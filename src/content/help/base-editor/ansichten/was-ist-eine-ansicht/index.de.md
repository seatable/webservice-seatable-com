---
title: 'Was ist eine Ansicht?'
date: 2023-01-13
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/de/hilfe/was-ist-eine-ansicht'
seo:
    title: 'Was ist eine Ansicht in SeaTable?'
    description: 'Erfahren Sie, wie Ansichten in SeaTable funktionieren und wie Sie individuelle Sichten auf Ihre Tabellendaten anlegen.'
star: true
weight: 1
---

Immer wenn Sie Ihre Daten in einer Tabelle anschauen, betrachten Sie diese über eine **Ansicht**. Selbst wenn Sie eine brandneue Tabelle angelegt haben, betrachten Sie diese bereits in der standardmäßig mitgelieferten Ansicht **"Default View"**.

## Wozu werden Ansichten verwendet?

In einer herkömmlichen Tabelle sehen Sie die Daten immer auf die gleiche Weise. Sie können zwar Zeilen und Spalten hinzufügen oder löschen, aber nicht dieselben Daten aus unterschiedlichen Blickwinkeln betrachten.

In SeaTable können Sie Ansichten erstellen und mithilfe von **Filtern, Sortierungen, Gruppierungen, Ausblendungen, farblichen Hervorhebungen und der Zeilenhöhe** festlegen, welchen Ausschnitt Ihrer Daten Sie auf welche Weise betrachten wollen. So können Sie sich genau die Daten anzeigen lassen, die gerade individuell für Sie relevant sind, ohne Datensätze verändern oder löschen zu müssen.

Zudem können Sie bestimmte Darstellungsformen wählen, um die Daten ansprechend zu visualisieren. Hier sind Beispiele für **Ansichtstypen**, die Sie erstellen können:

![Ansichtstypen](images/create-table-view.jpg)

- Tabellenansicht
- Kanban-Ansicht
- Kalenderansicht
- Galerie-Ansicht
- Zeitleisten-Ansicht
- Baum-Ansicht
- Big-Data-Ansicht

Es ist wichtig zu verstehen, dass eine Ansicht nur eine andere Art ist, **dieselben zugrundeliegenden Daten** zu betrachten! Das heißt, wenn Sie die Daten einer Tabelle in einer Ansicht bearbeiten, ändern sich diese Daten in allen Ansichten der Tabelle, da alle Ansichten denselben Datensatz repräsentieren.

{{< warning  type="warning" headline="Hinweis" >}}

Weitere Darstellungsformen wie Organigramm oder Landkarte können Sie in Form von [Plugins]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}}) verwenden.

{{< /warning >}}

## Die Tabellenansicht

Die **Tabellenansicht** ist die Standard-Darstellungsform in einer SeaTable Base. Sie ist einer Tabellenkalkulation sehr ähnlich, da die Datensätze in Zeilen und Spalten organisiert sind.

![Tabellenansicht](images/table-view.jpg)

Wenn Sie eine gefilterte Ansicht erstellen oder Spalten ausblenden, bekommen Sie nur die Datenmenge angezeigt, die Sie gerade benötigen. Indem Sie nach bestimmten Ordnungsprinzipien sortieren oder gruppieren, lässt sich die Ansicht ebenfalls übersichtlicher gestalten.

## Die Kanban-Ansicht

Wenn Sie **Spalten mit einer begrenzten Anzahl an Optionen** in Ihrer Tabelle haben, können Sie Ihre Zeilen in Gruppen zusammenfassen. Eine spezielle Darstellungsform davon ist die **Kanban-Ansicht**. Sie eignet sich besonders, um **Prozesse mit verschiedenen Phasen** darzustellen.

![Die Kanban-Ansicht](images/kanban-view.jpg)

Mehr dazu erfahren Sie im Artikel über die [Kanban-Ansicht]({{< relref "help/base-editor/ansichten/die-kanban-ansicht" >}}).

## Die Kalender-Ansicht

Wenn Sie eine Tabelle mit **Datum-Spalten** haben, können Sie eine Kalenderansicht erstellen, die alle Ihre Datensätze **chronologisch** ordnet.

![Die Kalender-Ansicht](images/calendar-view.jpg)

Mehr dazu erfahren Sie im Artikel über die [Kalender-Ansicht]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}).

## Die Galerie-Ansicht

Wenn Sie eine Tabelle mit einer **Bild-Spalte** besitzen, können Sie eine Galerie-Ansicht anlegen, um die Datensätze mit Vorschaubildern zu illustrieren.

![Die Galerie-Ansicht](images/gallery-view.jpg)

Mehr dazu erfahren Sie im Artikel über die [Galerie-Ansicht]({{< relref "help/base-editor/ansichten/die-galerie-ansicht" >}}).

## Die Zeitleisten-Ansicht

Wenn Sie eine Tabelle mit **zwei Datum-Spalten** haben, können Sie eine Zeitleisten-Ansicht erstellen, die verschiedene Zeitspannen auf einem **Zeitstrahl** visualisiert. Sie eignet sich besonders, um die Abfolge von Prozessen darzustellen oder zu prüfen, ob sich Zeiträume **überschneiden** – etwa bei der Urlaubsplanung, Projektplänen oder der Buchung von Räumen.

![Die Zeitleisten-Ansicht](images/timeline-view.jpg)

Mehr dazu erfahren Sie im Artikel über die [Zeitleisten-Ansicht]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}).

## Die Baum-Ansicht

Wenn Sie eine Base mit **mindestens zwei miteinander verknüpften Tabellen** haben, können Sie eine Baum-Ansicht erstellen, um verknüpfte Datensätze **hierarchisch** darzustellen. Sie eignet sich besonders, um komplexe Strukturen wie Projektportfolios oder Organisationshierarchien übersichtlich zu visualisieren – mit bis zu drei Ebenen im Baumdiagramm.

![Die Baum-Ansicht](images/tree-view.jpg)

Mehr dazu erfahren Sie im Artikel über die [Baum-Ansicht]({{< relref "help/base-editor/ansichten/die-baum-ansicht" >}}).

## Die Big-Data-Ansicht

Wenn Sie den **Big-Data-Speicher** in Ihrer Base aktiviert haben, können Sie **große Datenmengen archivieren**, die nicht unmittelbar für jeden Anwender sichtbar sind. Um auf die Daten im Big-Data-Speicher zugreifen zu können, ist eine spezielle Big-Data-Ansicht erforderlich.

![Die Big-Data-Ansicht](images/create-big-data-view.jpg)

Mehr dazu erfahren Sie im Artikel über die [Big-Data-Ansicht]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}).

## Weitere Artikel zum Thema Ansichten

- [Anlegen einer neuen Ansicht]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}})
- [Umbenennen einer Ansicht]({{< relref "help/base-editor/ansichten/umbenennen-einer-ansicht" >}})
- [Löschen einer Ansicht]({{< relref "help/base-editor/ansichten/loeschen-einer-ansicht" >}})
- [Das Duplizieren von Ansichten]({{< relref "help/base-editor/ansichten/das-duplizieren-von-ansichten" >}})
- [Unterschiede zwischen privaten und normalen Ansichten]({{< relref "help/base-editor/ansichten/unterschiede-zwischen-privaten-und-normalen-ansichten" >}})
- [Das Drucken einer Ansicht]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})
- [Die Reihenfolge von Ansichten ändern]({{< relref "help/base-editor/ansichten/die-reihenfolge-von-ansichten-aendern" >}})
- [Ansichten in Ordnern gruppieren]({{< relref "help/base-editor/ansichten/ansichten-in-ordnern-gruppieren" >}})
- [Filtern von Einträgen in einer Ansicht]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})
- [Filter-Regeln mit UND und ODER verknüpfen]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}})
- [Sortieren von Einträgen in einer Ansicht]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})
- [Gruppieren von Einträgen in einer Ansicht]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})
- [Einfärben von Zellen]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}})
- [Farbliche Markierung von Zeilen]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Zeilenhöhe anpassen]({{< relref "help/base-editor/ansichten/zeilenhoehe-anpassen" >}})
- [Anzahl der fixierten Spalten anpassen]({{< relref "help/base-editor/spalten/anzahl-der-fixierten-spalten-anpassen" >}})
- [Ausblenden und Verschieben von Spalten]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Ansichten sperren]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Freigabe einer Ansicht an ein Teammitglied]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Externen Link für eine Ansicht erstellen]({{< relref "help/startseite/freigaben/externen-link-fuer-eine-ansicht-erstellen" >}})
