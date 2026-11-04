---
title: 'Schritt 6: Erstellen von Ansichten'
date: 2024-08-30
lastmod: '2024-09-19'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/de/hilfe/schritt-6-ansichten'
seo:
    title: 'Schritt 6: Ansichten anlegen und filtern in SeaTable'
    description: 'Lernen Sie, wie Sie mit SeaTable Ansichten erstellen, filtern, sortieren, gruppieren und Daten gezielt auswählen, um stets die Übersicht zu behalten.'
---

Sie haben eine solide Ausgabenverwaltung erstellt, die bereits automatisch die Gesamtausgaben pro Kategorie berechnet. Nun lernen Sie eine weitere Funktion von SeaTable kennen: **die Ansichten**.

Ansichten ermöglichen es Ihnen, durch Filter, Sortierungen, Gruppierungen und das Ausblenden von Informationen festzulegen, welche Daten einer Tabelle angezeigt werden. Ansichten gelten immer pro Tabelle, und Sie können beliebig viele Ansichten anlegen. So erhalten Sie stets die für Sie relevanten Informationen.

Ein Beispiel: Sie könnten eine Ansicht erstellen, die nur Ausgaben über 100 Euro anzeigt und diese nach Datum sortiert. So behalten Sie den Überblick über größere Ausgaben.

{{< warning  type="warning" headline="Änderungen an den Daten wirken auf alle Ansichten"  text="Es ist wichtig, dass Sie sich bewusst machen, dass eine Ansicht nur eine andere Darstellung derselben Daten ist. Änderungen an den Datensätzen in einer Ansicht wirken sich auf alle Ansichten derselben Tabelle aus, da sie alle auf denselben Datensatz zugreifen." />}}

## Eine zusätzliche Ansicht mit einer Gruppierung erstellen

Wechseln Sie zur Tabelle `Expenses` und legen Sie eine neue Ansicht an. Wählen Sie einen Namen, der den Zweck der Ansicht deutlich macht, wie z. B. `Group by date and category`.

Jede neu erstellte Ansicht enthält zunächst keine Gruppierungen, Sortierungen oder Filter. Das wollen wir nun ändern:

1. Gruppieren Sie die Daten in der Spalte `Date` nach Jahr.
2. Gruppieren Sie die Daten anschließend nach `Category-Link`.

![Ansicht „Group by date and category“ mit Gruppierung nach Jahr und Kategorie-Link](images/lvl1-view-groups.png)

## Eine Ansicht mit Filter und Gruppierung erstellen

Nachdem Sie die Gruppierung Ihrer Daten bereits beherrschen, geht es nun um die Filterung von Daten mithilfe einer Ansicht.

Erstellen Sie eine neue Ansicht mit dem Namen `Clothing Expenses by Year`, um die jährlichen Ausgaben für Kleidung darzustellen:

1. Fügen Sie einen Filter hinzu: `Category-Link` enthält `Clothing`, um nur die Einträge dieser Kategorie anzuzeigen.
2. Gruppieren Sie die gefilterten Daten nach Jahr.

Jetzt haben Sie mit wenigen Klicks eine Ansicht erstellt, die Ihnen die Ausgaben für Kleidung, gruppiert nach Jahren, übersichtlich präsentiert.

## Experimentieren Sie mit weiteren Ansichten

Damit endet dieser Online-Kurs, der gleichzeitig der Beginn Ihrer Reise mit SeaTable ist. Nehmen Sie sich ein paar Minuten Zeit, um mit weiteren Ansichten zu experimentieren – das Verständnis dafür gehört zu den wichtigsten Aspekten bei der Nutzung von SeaTable.

Ich ermutige Sie, SeaTable besser kennenzulernen. Sie haben bereits ein leistungsstarkes Tool erstellt, aber es gibt noch viel mehr zu entdecken!

Wenn Sie genug experimentiert haben, versuchen Sie das Quiz zu absolvieren und verdienen Sie sich Ihre Auszeichnung in unserem Community-Forum.

## Hilfeartikel mit weiteren Informationen

- [Was ist eine Ansicht?]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}
  )
- [Gruppierung, Sortierung und Filter]({{< relref "help/base-editor/ansichten/gruppierung-sortierung-und-filter" >}})
- [Anlegen einer neuen Ansicht]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}})
- [Ansichten pinnen]({{< relref "help/base-editor/ansichten/ansichten-pinnen" >}})
- [Die Status-Zeile und ihre Funktionen]({{< relref "help/base-editor/ansichten/die-status-zeile-und-ihre-funktionen" >}})
