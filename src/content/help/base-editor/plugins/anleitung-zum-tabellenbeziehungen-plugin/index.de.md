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

Besonders wenn sich viele verknüpfte Tabellen mit Dutzenden Spalten in einer Base befinden, verliert man schnell den Überblick, wie diese miteinander in Beziehung stehen. Mithilfe des Tabellenbeziehungen-Plugins können Sie sichtbar machen, welche Tabellen über welche Spalten miteinander verknüpft sind.

Wie Sie das Plugin in einer Base aktivieren, erfahren Sie [hier]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}
).

![Tabellenbeziehungen-Plugin](images/Table-Relationships-Plugin.png)

## Funktionsweise des Plugins

Wenn Sie das Tabellenbeziehungen-Plugin eingerichtet und geöffnet haben, sehen Sie zunächst **alle Tabellen**, die sich in der Base befinden. Unter den farbig hinterlegten Tabellennamen sind **alle Spalten** aufgelistet, die in den jeweiligen Tabellen angelegt sind.

Um die Tabellenbeziehungen zu visualisieren, werden Ihnen nicht nur **durchgezogene Linien** für _direkte_ Verbindungen über [Verknüpfungsspalten]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), sondern auch **gestrichelte Linien** für _indirekte_ Verbindungen über Linkformel-Spalten (z. B. [Lookups]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}) angezeigt.

## Verwaltung eines Beziehungsdiagramms

Standardmäßig ist beim ersten Öffnen des Tabellenbeziehungen-Plugins bereits ein Diagramm mit allen Tabellenbeziehungen angelegt. Wenn Sie ein weiteres Beziehungsdiagramm erstellen möchten, klicken Sie auf {{< seatable-icon icon="dtable-icon-add-table" >}} **Beziehungsdiagramm hinzufügen**. Daraufhin öffnet sich ein Eingabefeld, in das Sie den gewünschten **Namen** tippen.

![Verwaltungsoptionen eines Beziehungsdiagramms](images/table-relationship-plugin-management-options.png)

Wenn Sie mit dem Mauszeiger über den Namen eines Diagramms fahren, erscheinen drei Symbole. Um die **Reihenfolge der Diagramme zu ändern**, halten Sie die linke Maustaste an der **Greiffläche** {{< seatable-icon icon="dtable-icon-drag" >}} gedrückt und ziehen es **per Drag-and-Drop** an die gewünschte Stelle.

![Optionen eines Beziehungsdiagramms](images/Options-of-Table-Relationship-Chart.png)

Darüber hinaus können Sie auf die **drei Punkte** klicken, um das Diagramm zu verwalten. Folgende Optionen stehen Ihnen zur Verfügung: 
- **umbenennen**
- **duplizieren**
- **löschen**
- **zurücksetzen**
- **als Bild exportieren**.

{{< warning  type="warning" headline="Hinweis"  text="Wenn nur ein einziges Diagramm im Plugin angelegt ist, können Sie dieses **nicht löschen**." />}}

## Einstellungen eines Beziehungsdiagramms

Über die **Einstellungen**, die Sie per Klick auf das **Zahnrad-Symbol** {{< seatable-icon icon="dtable-icon-set-up" >}} erreichen, können Sie Folgendes für ein Diagramm festlegen, indem Sie die **Regler (de-)aktivieren**:

- Möchten Sie **Verknüpfungen zu anderen Tabellen** (direkte Verbindungen) anzeigen?
- Möchten Sie **Verknüpfungen innerhalb einer Tabelle** (direkte Verbindungen) anzeigen?
- Möchten Sie **Formeln für Verknüpfungen** (indirekte Verbindungen) anzeigen? Wenn ja, welche Arten von Linkformeln?
- Möchten Sie **alle Spalten ungeachtet der Ansichten** anzeigen?
- Möchten Sie **Tabellen ohne Verknüpfungen** anzeigen?
- Möchten Sie **Tabellen anzeigen oder ausblenden**?

![Einstellungsmöglichkeiten eines Beziehungsdiagramms](images/table-relationship-plugin-settings.png)

## Designoptionen eines Beziehungsdiagramms

Gehen Sie oben rechts neben den Einstellungen auf den Reiter **Design**, um den Stil bestimmter Elemente in einem Diagramm zu ändern. Klicken Sie auf den **Drop-down-Pfeil** vor einem Element, um die verfügbaren Einstellungen auszuklappen:

- **Tabellen**: Farbe des Tabellenkopfes und Schriftgröße
- **Verknüpfungsspalten** (direkte Verbindungen): Linienbreite, Linienstil und Linienfarbe
- **Formeln für Verknüpfungen** (indirekte Verbindungen der ersten Ebene): Linienbreite, Linienstil und Linienfarbe
- **mehrstufige Formeln für Verknüpfungen** (verschachtelte Verbindungen höherer Ebenen, z. B. eine Lookup-Formel, die Werte über eine andere Verknüpfungsspalte der verknüpften Tabelle bezieht): Linienbreite, Linienstil und Linienfarbe
- **Hintergrundfarbe für Export festlegen**

![Designoptionen eines Beziehungsdiagramms](images/table-relationship-plugin-theme.png)

## Tabellen in einem Diagramm verschieben

Sie können die verschiedenen Tabellen in einem Diagramm beliebig **per Drag-and-Drop verschieben**. Halten Sie dazu die linke Maustaste gedrückt, ziehen Sie die Tabelle an die gewünschte Stelle und lassen Sie los.

![Tabellen eines Beziehungsdiagramms per Drag-and-Drop verschieben](images/Move-tables-in-a-Table-Relationship-Chart.gif)

## Notiz in einem Beziehungsdiagramm hinzufügen

Zudem können Sie eine Notiz in einem Beziehungsdiagramm hinzufügen, indem Sie auf das **Zettel-Symbol** in der linken unteren Ecke klicken. Anschließend haben Sie diese Optionen:

- Text bearbeiten
- Hintergrund ausblenden
- Text linksbündig, zentriert oder rechtsbündig setzen
- Notiz löschen

![Notiz auf einem Beziehungsdiagramm hinzufügen](images/add-note-on-table-relationship-chart.png)
