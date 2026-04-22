---
title: 'Die Kalender-Ansicht'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/de/hilfe/die-kalender-ansicht'
aliases:
    - '/de/hilfe/anleitung-zum-kalender-plugin'
    - '/de/hilfe/mehrere-kalender-fuer-eine-base-anlegen'
    - '/de/hilfe/neue-kalendereintraege-im-kalender-plugin-anlegen'
seo:
    title: 'Kalender-Ansicht in SeaTable – chronologischen Überblick nutzen'
    description: 'Die Kalender-Ansicht in SeaTable stellt Ihre Termine pro Jahr, Monat, Woche, Tag oder in der Agenda dar. Komplettes Setup und Tipps.'
weight: 13
---

Die Kalender-Ansicht zeigt Ihnen Daten aus einer Tabelle in **Kalenderform** an. Dabei können Sie sich einen Überblick über **verschiedene Zeiträume (Jahr, Monat, Woche, Tag)** verschaffen oder Termine als **Agenda** in Listenform anzeigen lassen.

Ein Beispiel ist der Monatsüberblick in einem Urlaubskalender:

![Die Kalender-Ansicht](images/calendar-view.jpg)

{{< warning  type="warning" headline="Voraussetzungen" >}}

Um die Kalender-Ansicht sinnvoll verwenden zu können, benötigen Sie mindestens eine [Datum-Spalte]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) in Ihrer Tabelle.

{{< /warning >}}

## So erstellen Sie eine Kalender-Ansicht

![Eine Kalender-Ansicht anlegen](images/create-calendar-view.jpg)

1. Klicken Sie auf den **Namen der aktuellen Ansicht**.
2. Klicken Sie auf **Ansicht oder Ordner hinzufügen** und wählen Sie den gewünschten **Ansichtstyp** aus.

![Eine Kalender-Ansicht benennen](images/name-calendar-view.jpg)

3. Geben Sie der neuen Ansicht einen **Namen**.
4. Aktivieren Sie den Regler, falls die neue Ansicht nicht für alle sichtbar, sondern **privat** sein soll.
5. Bestätigen Sie mit **Abschicken**.

![Eine Kalender-Ansicht erstellen](images/calendar-view-settings.jpg)

6. Geben Sie im **Titelfeld** die Spalte an, mit der Sie die Kalendereinträge labeln möchten.
7. Legen Sie fest, welche Datum-Spalte für das **Startdatum** verwendet werden soll. Die Kalender-Ansicht generiert sich im Anschluss automatisch.
8. Optional können Sie beim **Enddatum** eine Datum- oder Dauer-Spalte angeben, die den Zeitraum der Kalendereinträge definiert.
9. Zu guter Letzt wählen Sie aus, welcher Wochentag als **erster Tag der Woche** dienen soll.

Falls Sie nachträglich noch etwas ändern möchten, klicken Sie auf das **Zahnrad-Symbol** {{< seatable-icon icon="dtable-icon-set-up" >}} in der oberen rechten Ecke und passen die **Einstellungen** an.

## Ansichtsoptionen

Folgende Optionen können Sie in einer Kalender-Ansicht nutzen:
- [Ansicht sperren]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- nach beliebigen Werten [filtern]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) oder [sortieren]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})
- [Zeilenfarbe]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Ansicht mit anderen teilen]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Ansicht drucken]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})

## Die Darstellungsoptionen im Detail

Insgesamt gibt es 5 Darstellungsoptionen: Sie können sich Termine in einem kalendarischen **Jahres-**, **Monats-** oder **Wochenüberblick**, im **Tagesplaner** oder als **Agenda** in Listenform anzeigen lassen.

Zwischen den fünf Darstellungsoptionen der Kalender-Ansicht können Sie bequem wechseln. Klicken Sie hierzu einfach die entsprechende Option auf der **Schaltfläche** oberhalb des Kalenders an.

![Darstellungsoptionen der Kalender-Ansicht](images/display-options-calendar-view.png)

### Jahresüberblick

Hier sehen Sie das **Jahr** auf einen Blick. Der **Punkt** unter einem Datum zeigt Ihnen an, dass an diesem Tag ein Eintrag vorhanden ist. Außerdem haben Sie die Möglichkeit, durch Klicken auf den Termin die **Zeilendetails** aufzurufen.

![Jahresüberblick in der Kalender-Ansicht](images/year-overview-calendar-view.png)

### Monatsüberblick

Bei dieser Darstellung haben Sie alle Tage eines **Monats** im Blick. Auch hier können Sie die **Zeilendetails** aufrufen, indem Sie auf einen der Kalendereinträge klicken.

### Wochenüberblick

Diese Darstellung zeigt Ihnen auf der vertikalen Achse die **Uhrzeiten** und von links nach rechts die sieben Tage einer **Woche**. Auch hier können Sie die **Zeilendetails** öffnen, indem Sie auf einen der Termine klicken.

### Tagesplaner

Der Tagesplaner eignet sich besonders, wenn Sie mehrere Termine an einem **Tag** auf dem Schirm haben möchten. Ebenso wie der Wochenüberblick zeigt er Ihnen auf der vertikalen Achse die **Uhrzeiten** an. Auch hier können Sie die **Zeilendetails** öffnen, indem Sie auf einen der Termine klicken.

### Agenda-Darstellung

Die **Agenda** listet alle Termine innerhalb eines **Monats** auf und bietet Ihnen die Möglichkeit, bestimmte **Informationen** zu den Terminen im Überblick sehen zu können.

Dazu blenden Sie in den **Einstellungen** der Kalender-Ansicht einfach die gewünschten **Spalten** der Tabelle ein – zum Beispiel Thema, Status und Art einer Veröffentlichung.

![Agenda in der Kalender-Ansicht](images/calendar-view-agenda.jpg)

## Einen neuen Datensatz in der Kalender-Ansicht hinzufügen

Um **neue Einträge** in der Kalender-Ansicht hinzuzufügen, haben Sie verschiedene Möglichkeiten.

### 1. Über das große Plus-Symbol

![Einen neuen Datensatz in der Kalender-Ansicht hinzufügen](images/add-new-record-in-calendar-view.jpg)

Klicken Sie auf den **orangen Kreis mit dem Plus-Symbol** in der unteren rechten Ecke. Ein neues Fenster öffnet sich. Legen Sie in den **Zeilendetails** einen neuen Datensatz an und pflegen Sie die gewünschten Daten ein. Die Änderungen werden automatisch gespeichert, wenn Sie das Fenster schließen.

{{< warning  type="warning" headline="Hinweis"  text="Diese Funktion gibt es bei **allen** Darstellungsoptionen im Kalender." />}}

### 2. Über ein Kalenderfeld

![Neuen Kalendereintrag in der Kalender-Ansicht anlegen](images/add-record-in-monthly-calendar-view.jpg)

Fahren Sie mit dem Mauszeiger über ein **Feld** im Kalender und klicken Sie auf das **Plus-Symbol**, welches in der rechten oberen Ecke erscheint. Legen Sie in den **Zeilendetails** einen neuen Datensatz an und pflegen Sie die gewünschten Daten ein. Die Änderungen werden automatisch gespeichert, wenn Sie das Fenster schließen.

{{< warning  type="warning" headline="Hinweis"  text="Diese Funktion existiert nur für die Darstellungsoptionen **Monat** und **Woche**." />}}

### 3. Per Doppelklick

Wenn Sie einen **Doppelklick** auf eine Stelle im Kalender machen, öffnen sich die **Zeilendetails** ebenfalls. Ansonsten legen Sie den Eintrag genauso an wie bei den anderen Optionen.

{{< warning  type="warning" headline="Hinweis"  text="Der Doppelklick funktioniert nur bei den Darstellungsoptionen **Monat**, **Woche** und **Tag**." />}}

### 4. Termine aufziehen

Für diese Funktion benötigen Sie **zwei Datum-Spalten**, die **Uhrzeiten** erfassen können.

1. Erstellen Sie zwei Datum-Spalten für den **Start- und Endzeitpunkt** und schalten Sie dabei jeweils die Option **Minutengenau** an.
2. Öffnen Sie die **Kalender-Ansicht** und wählen Sie die **Wochen- oder Tagesübersicht** aus.
3. Wählen Sie in den **Einstellungen** (erreichbar über das Zahnrad-Symbol {{< seatable-icon icon="dtable-icon-set-up" >}}) die beiden Datum-Spalten für den Kalender aus.
4. Klicken Sie im Kalender auf den Zeitpunkt, an dem der Termin starten soll, halten Sie die **linke Maustaste** gedrückt und ziehen Sie den Kasten bis zur Uhrzeit auf, zu der der Termin enden soll.

![Termine in der Wochen- und Tagesübersicht aufziehen](images/add-record-in-weekly-calendar-view.gif) 

{{< warning  type="warning" headline="Hinweis"  text="Sie können Termine nur in der **Wochen- oder Tagesübersicht** aufziehen." />}}

## Termine per Drag-and-Drop verschieben

Sie können die Einträge in der Kalender-Ansicht bequem **per Drag-and-Drop verschieben**. Dadurch ändern sich automatisch die entsprechenden Werte in den Datum-Spalten Ihrer Tabelle. Diese Funktion ist für die **Monats-**, **Wochen-** und **Tagesübersicht** verfügbar.

![Kalendereinträge verschieben](images/move-record-in-weekly-calendar-view.gif)
