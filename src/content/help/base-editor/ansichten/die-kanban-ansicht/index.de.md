---
title: 'Die Kanban-Ansicht'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/de/hilfe/die-kanban-ansicht'
aliases:
    - '/de/hilfe/anleitung-zum-kanban-plugin'
seo:
    title: 'Kanban-Ansicht in SeaTable erstellen und nutzen'
    description: 'Lernen Sie, wie Sie die Kanban-Ansicht in SeaTable einrichten und für die Visualisierung von Prozessen optimal nutzen.'
weight: 14
---

Eine **Kanban-Ansicht** ist prädestiniert, um dynamische Prozesse mit verschiedenen Phasen darzustellen. In dieser Hinsicht ermöglicht sie Ihnen beispielsweise die Visualisierung von **Workflows** und **Projektfortschritten**. Besonders hilfreich ist sie bei der [Projektplanung]({{< relref "templates/projects/project-plan" >}}), [Softwareentwicklung]({{< relref "templates/it-engineering/bug-tracker" >}}) oder Aufgabenverteilung im Team.

{{< warning  type="warning" headline="Voraussetzungen" >}}

Um die Kanban-Ansicht sinnvoll verwenden zu können, benötigen Sie in Ihrer Tabelle mindestens eine Spalte, die eine eindeutige Zuordnung von Optionen zulässt. Dafür eignen sich zum Beispiel die Spaltentypen [Einfachauswahl]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) oder [Mitarbeiter]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}).

{{< /warning >}}

**In diesem How-to-Video zeigen wir Ihnen in nur wenigen Minuten, wie Sie in SeaTable eine Kanban-Ansicht erstellen.**
{{< youtube bKZSnqLmpEc >}}

## Aufbau einer Kanban-Ansicht

Eine Kanban-Ansicht besteht aus **Säulen**, die für verschiedene Schritte oder Phasen in einem Prozess stehen. Bei einem Workflow können das beispielsweise "Idee", "geplant", "in Arbeit" und "erledigt" sein.

![Kanban-Ansicht](images/kanban-view.jpg)

Die Säulen versehen Sie mit **beweglichen Karten**, die Sie sowohl innerhalb einer Säule als auch von einer Säule in die nächste **verschieben** können. Eine Kanban-Karte kann zum Beispiel für ein Arbeitspaket oder eine Aufgabe stehen.

![Kanban Verschiebungen](images/move-records-in-kanban-view.gif)

## So erstellen Sie eine Kanban-Ansicht

![Eine Kanban-Ansicht anlegen](images/create-kanban-view.jpg)

1. Klicken Sie auf den **Namen der aktuellen Ansicht**.
2. Klicken Sie auf **Ansicht oder Ordner hinzufügen** und wählen Sie den gewünschten **Ansichtstyp** aus.

![Eine Kanban-Ansicht benennen](images/name-kanban-view.jpg)

3. Geben Sie der neuen Ansicht einen **Namen**.
4. Aktivieren Sie den Regler, falls die neue Ansicht nicht für alle sichtbar, sondern **privat** sein soll.
5. Bestätigen Sie mit **Abschicken**.

![Eine Kanban-Ansicht gruppieren](images/group-kanban-view.jpg)

6. Klicken Sie auf **Gruppierung hinzufügen** und legen Sie fest, welche **Spalte** Sie für die Gruppierung, also die Definition der Säulen, verwenden wollen. Die Kanban-Ansicht generiert sich im Anschluss automatisch.

![Eine Kanban-Ansicht einstellen](images/kanban-view-settings.jpg)

7. Gehen Sie zu den **Einstellungen** und geben Sie im **Titelfeld** die Spalte an, mit der Sie die Kanban-Karten beschriften möchten.
8. Optional können Sie noch **Regler** aktivieren, um bestimmte Funktionen einzuschalten.

Falls Sie nachträglich noch etwas ändern möchten, klicken Sie auf das **Zahnrad-Symbol** {{< seatable-icon icon="dtable-icon-set-up" >}} in der oberen rechten Ecke und passen die Einstellungen an.

## Einstellungen der Kanban-Ansicht

Über die Regler-Optionen haben Sie die Möglichkeit, die visuelle Darstellung der Kanban-Ansicht zu verändern.

- Durch den Regler **Leere Werte nicht anzeigen** können Sie gegraute Platzhalter auf den Kanban-Karten entfernen.
- Der Regler **Spaltennamen anzeigen** blendet die Spaltennamen über allen aktivierten Informationen ein.
- Der Regler **Text umbrechen** formatiert Texte so, dass sie auf den Karten des Kanban-Boards vollständig lesbar sind.

![Einstellungen der Kanban-Ansicht](images/show-other-fields-in-kanban-view.gif) 

## Ansichtsoptionen

Folgende Optionen können Sie in einer Kanban-Ansicht nutzen:
- [Ansicht sperren]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- nach beliebigen Werten [filtern]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) oder [sortieren]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})
- nach genau einer Spalte [gruppieren]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})
- [Spalten ausblenden]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Ansicht mit anderen teilen]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Weitere Spalten ein- und ausblenden

![Spalten in der Kanban-Ansicht ausblenden](images/hide-columns-in-kanban-view.jpg) 

Wenn Sie weniger Informationen auf den Karten anzeigen möchten, klicken Sie auf **Ausblenden** und deaktivieren die **Regler** der jeweiligen Spalten. Durch die Reaktivierung der Regler werden die Einträge in den Spalten wieder auf den Karten sichtbar.

{{< warning  headline="Hinweis"  text="Wenn die Regler **nicht aktiviert** sind, können Sie die Werte in den ausgeblendeten Spalten auch nicht sehen oder bearbeiten, wenn Sie die **Zeilendetails** öffnen." />}}

## Einen neuen Datensatz in der Kanban-Ansicht hinzufügen

![Einen neuen Datensatz in der Kanban-Ansicht hinzufügen](images/add-record-in-kanban-view.jpg)

Klicken Sie am unteren Ende einer Säule auf **Zeile hinzufügen**. Ein neues Fenster öffnet sich. Legen Sie in den **Zeilendetails** einen neuen Datensatz an und pflegen Sie die gewünschten Informationen ein. Die Änderungen werden automatisch gespeichert, wenn Sie das Fenster schließen.

## Datensätze in der Kanban-Ansicht bearbeiten

Klicken Sie auf eine **Kanban-Karte** und ein Fenster mit den **Zeilendetails** öffnet sich. Nehmen Sie die gewünschten Anpassungen am Datensatz vor. Die Änderungen werden automatisch gespeichert, wenn Sie das Fenster schließen.
