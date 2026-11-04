---
title: "Anleitung zum Statistik-Modul"
date: 2023-02-06
lastmod: "2024-03-18"
categories: 
  - "statistiken-und-datenanalyse"
author: "vge"
url: "/de/hilfe/anleitung-zum-statistik-modul"
seo:
    title: 'Statistiken und Diagramme im SeaTable Statistik-Modul'
    description: 'Erstellen Sie ansprechende Grafiken und Dashboards mit dem Statistik-Modul von SeaTable. Daten visuell analysieren, Trends erkennen und Layouts individuell anpassen.'
weight: 1
---

Mit dem **Statistik-Modul** können Sie die Daten aus Ihrer Tabelle visuell in Form von verschiedenen **Grafiken** und **Diagrammen** darstellen. Dies ist für Ihre Arbeit in SeaTable äußerst nützlich: Dank der **Dashboards** behalten Sie immer den Überblick über die Zahlen und statistischen Entwicklungen in Ihrer Base.

![Statistik-Modul](images/erweitertes-statistik-plugin-release-notes.gif)

## Das Statistik-Modul öffnen

Das Statistik-Modul ist standardmäßig in jeder Base eingerichtet. Sie erreichen es stets über die Schaltfläche "Statistiken" im **Base-Header**.

![Statistik-Modul im Base-Header](images/statistic-plugin-in-base-header.jpg)

## Eine Grafik erstellen

1. Öffnen Sie das Statistik-Modul und klicken Sie rechts oben auf die Schaltfläche {{< seatable-icon icon="dtable-icon-add-table" >}} **Grafik hinzufügen**.
Sie haben die Möglichkeit, aus verschiedenen **Typen** von Grafiken und Diagrammen auszuwählen. Scrollen Sie durch die Auswahl oder klicken Sie in der Optionsleiste auf die beschrifteten Icons, um direkt an die gewünschte Stelle zu springen.

![Im Statistik-Modul navigieren.](images/Navigieren-im-Statistik-Plugin-1.png)

2. Wählen Sie den passenden **Typ** für Ihre Statistik aus und klicken Sie auf **Einreichen**.

### Dateneinstellungen

3. Legen Sie fest, aus welcher **Tabelle** und **Ansicht** die Grafik die Daten beziehen soll.
4. Je nach Grafik können Sie unterschiedliche **Dateneinstellungen** vornehmen – bei einem Säulendiagramm zum Beispiel, welche Werte Sie auf der **X- und Y-Achse** darstellen möchten.

![Neue Grafik im Statistik-Modul erstellen.](images/Dateneinstellungen.png)

Sie beginnen die Detailarbeit an einem Säulendiagramm mit der Auswahl der Spalte, welche die **Werte für die X-Achse** liefern soll. Klicken Sie auf das entsprechende Drop-down-Feld und wählen Sie die **Spalte** aus. Mit einem Regler können Sie einstellen, ob Sie **leere Zeilen** im Diagramm berücksichtigen wollen.

Wählen Sie dann, wie die **Werte auf der Y-Achse** dargestellt werden sollen. Sie können wählen zwischen der **Anzahl** der Einträge, die einen bestimmten Wert in der gewählten Spalte aufweisen, und der Option **Feld zusammenfassen**, bei der Sie in **numerischen Spalten** entweder die Summe, den Durchschnitt, die Anzahl eindeutiger Werte, das Maximum oder das Minimum auswerten können. Bei **gruppierten** oder **gestapelten** Diagrammen können Sie eine Spalte mit Optionen angeben, nach denen Sie gruppieren möchten.

Alle Einstellungsänderungen werden **in Echtzeit** ausgeführt, d.h. das Diagramm wird bei jeder Einstellungsänderung unmittelbar **aktualisiert**. So können Sie direkt sehen, ob Sie das gewünschte Ergebnis erzielt haben oder nachjustieren müssen.

### Stileinstellungen

5. Geben Sie der Grafik einen **Titel**. Klicken Sie dazu auf den Tab **Diagrammstil** und tragen Sie den gewünschten Namen ein.
6. Wenn die von Ihnen gewählte Grafik **Stileinstellungen** erlaubt, können Sie beispielsweise **Titel der X- und Y-Achse**, **Farben** oder **Datenbeschriftungen** konfigurieren.

![Einstellungen beimzufügen einer neuen Grafik im Statistik-Modul.](images/Stileinstellungen.png)

## Grafiken auf dem Dashboard

7. Nachdem Sie das Einstellungsfenster geschlossen haben, erscheint die gespeicherte Grafik auf Ihrem **Dashboard**.

Sie können **mehrere Dashboards** anlegen und auf jedem Dashboard beliebig viele Grafiken erstellen. Um die **Reihenfolge der Grafiken** zu ändern, ziehen Sie diese **per Drag-and-Drop** an die gewünschte Stelle. Fahren Sie dazu mit dem Mauszeiger über den **Titel** einer Grafik, bis ein **Pfeilkreuz** angezeigt wird, und halten Sie die **Maustaste** gedrückt.

![Im Statistik-Modul Grafiken verschieben.](images/Dashboard_Sortierung_Statistik-Plugin.gif)

## Optionen für eine Grafik

Wenn Sie mit dem Mauszeiger über eine Grafik fahren, erscheinen in der rechten oberen Ecke ein **Doppelpfeil-Symbol** {{< seatable-icon icon="dtable-icon-open" >}} und ein **Drei-Punkte-Symbol** {{< seatable-icon icon="dtable-icon-more-level" >}}. Wählen Sie den Doppelpfeil aus, um eine Grafik im **Vollbildmodus** anzuzeigen. Auf alle anderen Optionen können Sie über die drei Punkte zugreifen:

- Grafik bearbeiten
- Grafik kopieren
- Als Bild exportieren
- Grafik löschen

![Statistik-Modul Grafik Optionen](images/Statistik-Plugin-Grafik-Optionen.gif)

## Weitere Anzeige-Optionen

Per Klick auf {{< seatable-icon icon="dtable-icon-full-screen" >}} können Sie sich das gesamte Fenster des Statistik-Moduls im **Vollbildmodus** anzeigen lassen.

![Statistik-Modul Vollbildmodus](images/Statistik-Plugin-Vollbildmodus.gif)

Über die Symbole {{< seatable-icon icon="dtable-icon-night-mode" >}} und {{< seatable-icon icon="dtable-icon-day-mode" >}} können Sie zwischen **hellem und dunklem Modus** wechseln.

![Statistik-Modul Nachtmodus](images/Statistik-Plugin-dark-mode.png)
