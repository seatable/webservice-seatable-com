---
title: 'Anleitung zum Tabellenbeziehungen-Plugin'
date: 2024-07-29
lastmod: '2024-08-01'
categories:
    - 'plugins'
author: 'kgr'
url: '/de/hilfe/anleitung-zum-tabellenbeziehungen-plugin'
seo:
    title: 'Anleitung Tabellenbeziehungen-Plugin in SeaTable'
    description: 'Erfahren Sie, wie Sie mit dem Tabellenbeziehungen-Plugin Ihre Base-Tabellen und Verknüpfungen visualisieren und effizient verwalten.'

---

Besonders wenn sich viele Tabellen mit Dutzenden Spalten in einer Base befinden, verliert man schnell den Überblick, wie diese miteinander in Beziehung stehen. Mithilfe des Tabellenbeziehungen-Plugins können Sie sichtbar machen, welche Tabellen über welche Spalten miteinander verknüpft sind.

Wie Sie das Plugin in einer Base aktivieren, erfahren Sie [hier]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}
).

![Tabellenbeziehungen-Plugin](images/Table-Relationships-Plugin.png)

## Funktionsweise des Plugins

Wenn Sie das Tabellenbeziehungen-Plugin eingerichtet und geöffnet haben, sehen Sie zunächst **alle Tabellen**, die sich in der Base befinden. Unter den farbig hinterlegten Tabellennamen sind **alle Spalten** aufgelistet, die in den jeweiligen Tabellen angelegt sind.

Um die Tabellenbeziehungen zu visualisieren, werden Ihnen nicht nur **durchgezogene Linien** für _direkte_ Verbindungen über [Verknüpfungsspalten]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), sondern auch **gestrichelte Linien** für _indirekte_ Verbindungen über Linkformel-Spalten (z. B. [Lookups]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}) angezeigt.

## Einstellungsmöglichkeiten einer Tabellenbeziehungen-Grafik

Standardmäßig ist beim ersten Öffnen des Tabellenbeziehungen-Plugins bereits eine Grafik mit allen Tabellenbeziehungen angelegt. Wenn Sie eine weitere Grafik erstellen möchten, klicken Sie auf {{< seatable-icon icon="dtable-icon-add-table" >}} **Neue Tabellenbeziehung hinzufügen**. Daraufhin öffnet sich ein Eingabefeld, in das Sie den gewünschten **Namen** tippen.

![Optionen einer Tabellenbeziehungen-Grafik](images/Options-of-Table-Relationship-Chart.png)

Um die **Reihenfolge der Grafiken zu ändern**, halten Sie die linke Maustaste an der **Greiffläche** {{< seatable-icon icon="dtable-icon-drag" >}} gedrückt und ziehen eine Grafik **per Drag-and-Drop** an die gewünschte Stelle. Darüber hinaus können Sie die Grafiken **umbenennen**, **duplizieren** oder **löschen**.

{{< warning  type="warning" headline="Hinweis"  text="Wenn nur eine einzige Grafik im Plugin angelegt ist, können Sie diese **nicht löschen**." />}}

Über die **Einstellungen**, die Sie per Klick auf das **Zahnrad-Symbol** {{< seatable-icon icon="dtable-icon-set-up" >}} erreichen, können Sie Folgendes für die Grafik festlegen, indem Sie die **Regler (de-)aktivieren**:

- Möchten Sie **Verknüpfungen zu anderen Einträgen** (direkte Verbindungen) anzeigen?
- Möchten Sie **Formeln für Verknüpfungen** (indirekte Verbindungen) anzeigen?
- Möchten Sie **zweistufige Formeln für Verknüpfungen** anzeigen (z. B. eine Lookup-Formel, die Werte aus der Lookup-Spalte einer anderen Tabelle bezieht)?
- Möchten Sie **Tabellen ohne Verknüpfungen** anzeigen?

![Einstellungsmöglichkeiten einer Tabellenbeziehungen-Grafik](images/Settings-of-Table-Relationship-Chart.png)

## Tabellen in einer Grafik verschieben

Sie können die verschiedenen Tabellen in der Grafik beliebig **per Drag-and-Drop verschieben**. Halten Sie dazu die linke Maustaste gedrückt, ziehen Sie die Tabelle an die gewünschte Stelle und lassen Sie los.

![Tabellen in einer Tabellenbeziehungen-Grafik per Drag-and-Drop verschieben](images/Move-tables-in-a-Table-Relationship-Chart.gif)
