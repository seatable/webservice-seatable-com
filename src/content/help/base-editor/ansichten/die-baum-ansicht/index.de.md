---
title: 'Die Baum-Ansicht'
date: 2026-04-01
lastmod: '2026-04-01'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/de/hilfe/die-baum-ansicht'
seo:
    title: 'Baum-Ansicht: Hierarchie verknüpfter Datensätze darstellen'
    description: 'Nutzen Sie die Baum-Ansicht in SeaTable, um die Hierarchie verknüpfter Datensätze zu visualisieren und komplexe Daten strukturiert darzustellen.'
weight: 16
---

Die **Baum-Ansicht** ermöglicht die kompakte **hierarchische Darstellung** verknüpfter Datensätze. Das heißt, Sie können Daten, die in verschiedenen **miteinander verknüpften Tabellen** liegen, auf unterschiedlichen Ebenen in einem Baumdiagramm visualisieren. Gerade bei großen Datenmengen wie Finanz- oder Projektdaten, schafft die Ansicht einen strukturierten Überblick.

![Die Baum-Ansicht](images/tree-view.png)

{{< warning  type="warning" headline="Voraussetzungen" >}}

Um die Baum-Ansicht sinnvoll nutzen zu können, benötigen Sie eine Base mit **mindestens zwei Tabellen**, die über eine [Verknüpfungsspalte]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) miteinander verbunden sind.

{{< /warning >}}

## Funktionsweise der Baum-Ansicht

Bevor Sie eine Baum-Ansicht anlegen, sollten Sie sich überlegen, welche **Baumstruktur** (also Hierarchie verknüpfter Datensätze in Ihrer Base) Sinn ergibt: Bei einem [Projektportfolio]({{< relref "templates/projects/project-portfolio" >}}) könnten dies beispielsweise die Abteilungen auf der ersten Ebene, die Projekte auf der zweiten Ebene und die Aufgaben auf der dritten Ebene sein. Dementsprechend müssen die Abteilungen, Projekte und Aufgaben in drei verschiedenen Tabellen erfasst sein, die miteinander verknüpft sind. Jede Aufgabe ist einem Projekt zugeordnet, das wiederum einer Abteilung untergeordnet ist.

![Beispiel für eine Baumstruktur](images/example-for-tree-view.png)

Wie die Datensätze voneinander abhängen bzw. welche Tabellen sich auf welcher Ebene befinden, definieren Sie über die **Levels**. Aktuell können Sie in der Baum-Ansicht bis zu drei Ebenen, das heißt Daten aus drei Tabellen darstellen.

## Wie Sie eine Baum-Ansicht anlegen

1. Klicken Sie auf den **Namen der aktuellen Ansicht**.
2. Klicken Sie auf **Ansicht oder Ordner hinzufügen** und wählen Sie den gewünschten **Ansichtstyp** aus.

![Eine Baum-Ansicht anlegen](images/create-tree-view.png)

3. Geben Sie der neuen Ansicht einen **Namen**.
4. Aktivieren Sie den Regler, falls die neue Ansicht nicht für alle sichtbar, sondern **privat** sein soll.
5. Bestätigen Sie mit **Abschicken**.

![Baum-Ansicht benennen](images/name-tree-view.png)

6. Klicken Sie auf das **Zahnrad-Symbol** {{< seatable-icon icon="dtable-icon-set-up" >}} in der oberen rechten Ecke und passen die **Einstellungen** an.
7. Legen Sie fest, welche **Tabelle** auf dem jeweiligen Level angezeigt werden soll. Klicken Sie dazu in das Feld für **Level 2** und **Level 3**, um in der Drop-down-Liste die gewünschte Tabelle auszuwählen. **Level 1** wird immer von der Tabelle belegt, in der sich die Ansicht befindet.

![Hierarchie in der Baum-Ansicht festlegen](images/tree-view-settings.jpg)

Die verknüpften Datensätze auf der zweiten und dritten Ebene des Baumdiagramms sind anschließend unter den jeweils übergeordneten Datensätzen gruppiert.

## Informationen ein- und ausblenden

Über die **Einstellungen**, die Sie per Klick auf das **Zahnrad-Symbol** {{< seatable-icon icon="dtable-icon-set-up" >}} erreichen, können Sie die sichtbaren Spalten für jede Ebene des Baumdiagramms festlegen. Wählen Sie dafür zuerst das **Level** aus, auf dem Sie Spalten ein- oder ausblenden möchten. Wenn Sie anschließend die entsprechenden **Regler** am rechten Rand deaktivieren, sind die Spalten nicht im Baumdiagramm sichtbar.

![Spalten in der Baum-Ansicht ausblenden oder verschieben](images/hide-and-move-columns-in-tree-view.png)

### Spalten verschieben

Zudem haben Sie auf jedem Level die Möglichkeit, die Spalten anders als in der Tabellenansicht anzuordnen. Halten Sie dazu die linke Maustaste auf der **Sechs-Punkte-Greiffläche** vor dem Spaltennamen gedrückt und verschieben Sie die Spalte **per Drag-and-Drop** an die gewünschte Stelle.

## Ansichtsoptionen

Folgende Optionen können Sie in einer Baum-Ansicht nutzen:
- [Ansicht sperren]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- nach beliebigen Werten [filtern]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) oder [sortieren]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})
- **Alle einklappen** oder **Alle erweitern**

## Verknüpfte Datensätze einklappen und ausklappen

Um alle verknüpften Datensätze unter einem Eintrag einzuklappen, klicken Sie auf den **Drop-down-Pfeil** links vor der Zeile. Um die Datensätze wieder auszuklappen, gehen Sie genauso vor.

![Datensätze in der Baum-Ansicht ausklappen](images/collapse-records-in-tree-view.gif)

## Spaltenbreite anpassen

Um abgeschnittene Einträge oder große Lücken zwischen den Werten zu vermeiden, können Sie nach Belieben **die Spaltenbreite anpassen**. Halten Sie dazu die linke Maustaste auf der Begrenzungslinie zwischen zwei Spalten gedrückt und ziehen Sie den Cursor nach links oder rechts.

![Spaltenbreite anpassen in der Baum-Ansicht](images/adjust-column-width-in-tree-view.gif)

## Datensätze in der Baum-Ansicht hinzufügen und bearbeiten

Um einen neuen Datensatz auf der ersten Ebene der Baum-Ansicht hinzuzufügen, klicken Sie auf den **orangen Kreis mit dem Plus-Symbol** in der unteren rechten Ecke. Anschließend öffnen sich die **Zeilendetails**. Füllen Sie diese wie gewünscht aus und schließen Sie das Fenster, um den Datensatz zu speichern.

Um einen neuen Datensatz auf der zweiten oder dritten Ebene der Baum-Ansicht hinzuzufügen, klicken Sie auf **\+ Zeile hinzufügen**. Die angelegte Zeile wird automatisch mit dem übergeordneten Datensatz verknüpft und entsprechend gruppiert. Die restlichen Felder können Sie direkt in der Zeile ausfüllen.

![Datensätze in der Baum-Ansicht hinzufügen und bearbeiten](images/add-record-in-tree-view.png)

Ebenso lassen sich bestehende Einträge direkt in der Baum-Ansicht bearbeiten. Außerdem können Sie mit einem Klick auf **Erweitern** die Zeilendetails öffnen und Änderungen vornehmen.

![Datensätze in der Baum-Ansicht hinzufügen und bearbeiten](images/expand-record-in-tree-view.png)

Die Daten werden natürlich auch in den zugrundeliegenden Tabellen gespeichert.