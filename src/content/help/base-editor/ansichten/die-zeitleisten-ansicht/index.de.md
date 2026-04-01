---
title: 'Die Zeitleisten-Ansicht'
date: 2026-03-31
lastmod: '2026-03-31'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/de/hilfe/die-zeitleisten-ansicht'
seo:
    title: 'Zeitleisten-Ansicht: Zeiträume in SeaTable visualisieren'
    description: 'Mit der Zeitleisten-Ansicht verschaffen Sie sich einen klaren Überblick über Zeitspannen und deren Überschneidungen.'
weight: 15
---

Die **Zeitleisten-Ansicht** ermöglicht Ihnen die Darstellung verschiedener Zeitspannen auf einem **Zeitstrahl**. Dies ist beispielsweise sehr nützlich, wenn Sie die Abfolge von Prozessen visualisieren möchten oder sehen möchten, ob sich Zeiträume **überschneiden**. Dementsprechend können Sie die Zeitleisten-Ansicht unter anderem für die [Urlaubsplanung]({{< relref "templates/human-resources/holiday-request-management" >}}), [Projektpläne]({{< relref "templates/projects/project-plan" >}}) oder die Buchung von Konferenzräumen einsetzen.

![Die Zeitleisten-Ansicht](images/timeline-view.jpg)

{{< warning  type="warning" headline="Voraussetzungen" >}}

Dieser Ansichtstyp bildet **Zeitspannen** ab. Deshalb benötigen Sie **zwei** [Datum-Spalten]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) in einer Tabelle, die den **Beginn** und das **Ende** der Zeiträume definieren. Das Ergebnis ist ein **Gantt-Diagramm**.

{{< /warning >}}

## So erstellen Sie eine Zeitleisten-Ansicht

1. Klicken Sie auf den **Namen der aktuellen Ansicht**.
2. Klicken Sie auf **Ansicht oder Ordner hinzufügen** und wählen Sie den gewünschten **Ansichtstyp** aus.

![Eine Zeitleisten-Ansicht anlegen](images/create-timeline-view.png)

3. Geben Sie der neuen Ansicht einen **Namen**.
4. Aktivieren Sie den Regler, falls die neue Ansicht nicht für alle sichtbar, sondern **privat** sein soll.
5. Bestätigen Sie mit **Abschicken**.
6. Legen Sie daraufhin in den Einstellungen das **Start- und Enddatum** fest und den **Zeitraum**, den der Zeitstrahl umfassen soll. Die neue Ansicht generiert sich im Anschluss automatisch.
7. Geben Sie im obersten Eingabefeld die Spalte an, von der die **Blockbeschriftung** abhängt.

![Eine Zeitleisten-Ansicht erstellen](images/create-timeline-view.gif)

## Ansichtsoptionen

Folgende Optionen können Sie in einer Zeitleisten-Ansicht nutzen:
- [Ansicht sperren]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- nach beliebigen Werten [filtern]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) oder [sortieren]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})
- [Zeilenfarbe]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Ansicht mit anderen teilen]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Ansicht drucken]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})

## Darstellungsoptionen

Insgesamt gibt es 5 Darstellungsoptionen für die Skala des Zeitstrahls: **Jahr**, **Quartal**, **Monat**, **Woche** und **Tag**. Zwischen diesen Optionen können Sie bequem wechseln. Klicken Sie hierzu einfach die entsprechende Option im **Drop-down-Menü** über der Zeitleiste an.

![Darstellungsoptionen der Zeitleisten-Ansicht](images/display-options-timeline-view.jpg)

## Informationen ein- und ausblenden

Klicken Sie auf **Spalten anzeigen**, um durch Ein- und Ausblenden von Spalten mehr oder weniger Informationen anzeigen lassen. Aktivieren Sie die **Regler** der jeweiligen Spalten, um mehr Informationen aus den Datensätzen in der Zeitleiste angezeigt zu bekommen.

![Informationen aus anderen Spalten in der Zeitleiste anzeigen](images/other-fields-shown-in-timeline-view.gif)

## Datensätze in der Zeitleisten-Ansicht bearbeiten

Machen Sie einen Doppelklick auf einen Eintrag und ein Fenster mit den **Zeilendetails** öffnet sich. Nehmen Sie die gewünschten Anpassungen am Datensatz vor. Die Änderungen werden automatisch gespeichert, wenn Sie das Fenster schließen.

## Zeiträume verlängern, verkürzen oder verschieben

Um einen Zeitraum zu verlängern oder zu verkürzen, ziehen Sie mit gedrückter Maustaste **am linken oder rechten Rand eines Eintrags**. Wenn Sie einen Zeitraum verschieben möchten, halten Sie die linke Maustaste gedrückt und bewegen den Eintrag **per Drag-and-Drop** in die gewünschte Richtung. Die entsprechenden Werte in den Datum-Spalten passen sich automatisch an.

![Zeiträume in der Zeitleisten-Ansicht ändern](images/change-records-in-timeline-view.gif)