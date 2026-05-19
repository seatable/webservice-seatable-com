---
title: 'SeaTable 5.0: App-Builder, neue Plugins und mehr Barrierefreiheit'
description: 'SeaTable 5.0 markiert den offiziellen Start des App-Builders: Apps ohne Programmierung erstellen, individuelle Oberflächen, differenzierte Berechtigungen. Visualisierungen wie Organigramm, Whiteboard und Beziehungsdiagramm, bessere Zugänglichkeit für alle User und feingranularer Excel-Import heben Daten-getriebene Teams aufs nächste Level.'
date: 2024-07-15
lastmod: '2024-07-15'
author: 'kgr'
url: '/de/seatable-release-5-0'
color: '#efba4b'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 5.0: App-Builder, neue Plugins & mehr'
    description: 'No-Code-App-Builder, 3 neue Visualisierungsplugins, barriereärmer, Excel-Import nach Spalte — großes Innovations­update mit SeaTable 5.0!'
---

Es ist so weit: Unser App-Builder geht offiziell an den Start! Mit dieser Version unserer **No-Code-Datenbank mit integriertem No-Code-App-Builder** kann jeder, ob Programmierer oder Citizen Developer, künftig ganz einfach eigene Apps erstellen! Mit SeaTable 5.0 sind wir bereit, auf dem internationalen Markt eine führende Position in der digitalen Transformation und Innovation einzunehmen.

Doch das ist nicht der einzige Paukenschlag – in SeaTable 5.0 stehen Ihnen **drei neue Plugins** für komplexe Visualisierungen zur Verfügung: Organigramm, Tabellenbeziehungen und Whiteboard. Die **verbesserte Barrierefreiheit** soll Menschen mit (Seh-)Beeinträchtigung die Nutzung von SeaTable erleichtern. Ein weiteres Glanzlicht setzt der **spaltengenaue Excel-Import**.

Heute Morgen haben wir SeaTable Cloud auf Version 5.0 aktualisiert. Alle Selbsthoster können das ebenfalls tun: Das Image von SeaTable 5.0 ist im bekannten [Docker Repository](https://hub.docker.com/r/seatable/seatable-enterprise) zum Download verfügbar. Im [Changelog]({{< relref "pages/changelog" >}}/) finden Sie wie immer die vollständige Liste der Änderungen.

## Ohne Code zur individuellen Business-App

Mit SeaTable 5.0 geht unser No-Code-App-Builder offiziell an den Start. Nachdem unsere Entwickler über die letzten Versionen hinweg viele neue Funktionen und Verbesserungen in den App-Builder implementiert haben, steht der Umsetzung Ihrer anspruchsvollen Anwendungsfälle nun nichts mehr im Weg. Erstellen Sie individuelle Business-Apps, ohne eine einzige Zeile Code zu schreiben, und nutzen Sie SeaTable als Frontend und Backend in einem!

### Neuer Seitentyp: Einzelner Datensatz

Die Entwicklung des App-Builders geht unvermindert weiter: Mit dem [Seitentyp]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) **Einzelner Datensatz** haben Sie die Möglichkeit, eine Seite mit statischen Elementen, Tabellenfeldern, Farben, Rahmen etc. zu designen, um die in einer Zeile gespeicherten Daten optisch aufzubereiten. Damit ähnelt dieser Seitentyp dem [Seitendesign-Plugin]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}), das Sie bereits aus der Base kennen.

Die Nutzer der App können auf dieser Seite – mit der jeweiligen [Berechtigung]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) – die einzelnen Datensätze sehen, suchen, durchblättern und bearbeiten. Dieser Seitentyp eignet sich zum Beispiel, um die Daten in einer Mitarbeiterdatenbank als persönliche Steckbriefe anzuzeigen.

![Single Record Page](Single-Record-Page-min.gif)

### Neue Funktionen bestehender Seitentypen

Auf [Tabellenseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}) können Sie ab sofort alle angezeigten Daten als **Excel-Datei exportieren**. Zudem können Sie über den Spaltenkopf von [Bild-]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) und [Datei-Spalten]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) **alle Anhänge als Zip-Datei herunterladen**. Die neuen Export-Funktionen sind hilfreich, wenn Sie anderen Nutzern bestimmte Dateien über die App zur Verfügung stellen möchten.

Auf [Galerieseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}) haben wir die **Einstellungen von Verknüpfungsspalten** ergänzt. So können Sie zum Beispiel festlegen, ob die Nutzer über die Galerieseite bestehende Einträge verknüpfen oder Einträge in einer anderen Tabelle hinzufügen dürfen. Auf [Abfrageseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}) aktualisieren sich die Abfrage-Ergebnisse nun sofort, wenn Sie Schaltflächen-Aktionen auslösen, die Veränderungen an den Daten bewirken.

## Drei Plugins für komplexe Visualisierungen

Ein weiteres Highlight von SeaTable 5.0 sind die neuen [Plugins]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}}), mit denen man die Abhängigkeiten, Strukturen und Prozesse in einer Base visualisieren kann.

### Organigramm

Mithilfe des Organigramm-Plugins lassen sich Hierarchien zwischen den Datensätzen in einer Tabelle darstellen, z. B. Positionen in einem Unternehmen oder [über- und untergeordnete Aufgaben in einem Projekt]({{< relref "templates/projects/work-breakdown-structure" >}}). Um die Abhängigkeiten der Datensätze zu visualisieren, brauchen Sie eine [Link-Spalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), die auf ein und dieselbe Tabelle referiert. Der Eintrag, mit dem Sie eine andere Zeile derselben Tabelle verlinken, wird als übergeordneter Datensatz dargestellt.

![Organigramm-Plugin](Organigramm-Plugin.png)

### Tabellenbeziehungen

Besonders wenn sich viele Tabellen mit Tausenden Zeilen in einer Base befinden, verliert man schnell den Überblick, wie diese miteinander in Beziehung stehen. Mithilfe des neuen Tabellenbeziehungen-Plugins können Sie sichtbar machen, welche Tabellen über welche Spalten miteinander verknüpft sind. Dabei werden nicht nur direkte Verbindungen über [Link-Spalten]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), sondern auch indirekte Verbindungen über Linkformel-Spalten angezeigt.

![Tabellenbeziehungen-Plugin](Table-Relationships-Plugin.png)

### Whiteboard

Das Whiteboard ist das erste Plugin, das losgelöst von den Daten in einer Base funktioniert. Es gibt Ihnen die Freiheit, Prozesse und Strukturen grafisch zu visualisieren, die Sie mit den bisherigen Plugins nicht darstellen können. Ebenso können Sie Layouts und Mockups frei skizzieren. Für die Gestaltung haben Sie verschiedene **Elemente** wie Vierecke, Ellipsen und Pfeile sowie **Werkzeuge** wie Stift und Radierer zur Auswahl.

![Whiteboard Plugin](Whiteboard-Plugin.png)

{{< warning headline="SeaTable ♥ Excalidraw" text="Das Whiteboard-Plugin basiert auf der beliebten Software [Excalidraw](https://plus.excalidraw.com/), die viele Anwender bereits kennen werden. Eine wichtige Einschränkung soll nicht unerwähnt bleiben: Zum Start von SeaTable 5.0 wird das Whiteboard keine Live-Zusammenarbeit unterstützen. Dies werden wir in Kürze nachliefern." />}}

## Verbesserte Barrierefreiheit

SeaTable möchte allen Benutzern einen optimalen Zugang zu seiner digitalen No-Code-Lösung ermöglichen. Daher haben wir für SeaTable 5.0 viel in die Verbesserung der Barrierefreiheit investiert. Dazu gehören die Optimierung der ARIA-Tags für eine verbesserte **Unterstützung von nicht-visuellen Ausgabegeräten**, Anpassungen an der Farbgebung für **stärkere Kontraste** und die Überarbeitung der **Tastatursteuerung**.

Mit Version 5.0 erreichen wir das Ziel, für die wichtigsten Seiten von SeaTable einen Lighthouse Accessibility Score von 90 und größer zu erzielen. Ab diesem Wert können Webseiten als im Wesentlichen barrierefrei gelten. Natürlich werden wir unsere Bemühungen um Barrierefreiheit in Zukunft mit unseren Partnern fortsetzen.

## Spaltengenauer Excel-Import

Bereits in Version 4.4 wurde der Import von XLSX-Dateien schneller, flexibler und stabiler. Mit SeaTable 5.0 wird der Import-Wizard noch leistungsfähiger: Im deutlich aufgewerteten Vorschaufenster können Sie jetzt detailliert selektieren, welche Tabellen – und sogar **welche Spalten einer XLSX-Arbeitsmappe** – SeaTable importieren soll. Wählen Sie unerwünschte Tabellen und Spalten einfach ab, um den Datenimport genauestens zu steuern.

![Excel-Import](Excel-Import.gif)

## Optimierung der API von SeaTable Cloud

Im Rahmen von SeaTable 5.0 haben wir auch einige Änderungen an der SeaTable API vorgenommen. Dies betrifft nur Anwender, die mithilfe der API ihre eigenen Anwendungen und Workflows umsetzen. Auf die Arbeit im Browser haben diese Änderungen keinen Einfluss.

Hier die wichtigsten Punkte in der Übersicht:

- Die API-Endpunkte [Get Row](https://api.seatable.com/reference/getrowdeprecated) und [List Rows](https://api.seatable.com/reference/listrowsdeprecated) werden auf das neue _API-Gateway_ umgeleitet.
- Das Format der Rückgabewerte von Link- und Linkformel-Spalten wird harmonisiert.
- Das _API-Gateway_ liefert zukünftig das aktuelle API-Nutzungslimit zurück.

Wenn Sie mehr erfahren wollen, finden Sie in diesem [Forumspost](https://forum.seatable.com/t/important-changes-to-api-and-seatable-cloud-with-version-5-0/4887) alle Details zu den Änderungen.

## Und vieles mehr

Dem **Editor für lange Texte** begegnen Sie an vielen Stellen. Wenn Sie formatierte Textfelder in den **Zeilendetails** oder in [Webformularen]({{< relref "help/base-editor/webformulare" >}}) ausfüllen, werden Sie bemerken, dass sich nun die Usability verbessert hat: Der Editor für lange Texte öffnet sich nicht mehr in einem weiteren Pop-up-Fenster, sondern inline, sodass Sie direkt losschreiben können.

![Editor für lange Texte in Webformularen](Long-text-editor-in-web-forms.png)

Auch die **Statistiken** kennen Sie von mehreren Stellen in SeaTable: vom [Statistik-Modul]({{< relref "help/base-editor/statistiken/anleitung-zum-statistik-modul" >}}) in der Base sowie von [individuellen Seiten in Universellen Apps]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}). Mit einer überarbeiteten Diagramm-Bibliothek haben wir die Statistiken nun deutlich aufgewertet und vereinheitlicht.

Früher konnten Sie Zeilen, die Sie in den [Big-Data-Speicher]({{< relref "help/base-editor/big-data/zeilen-ins-big-data-backend-verschieben" >}}) verschoben hatten, nicht über Snapshots wiederherstellen. Um unerwünschtem Datenverlust vorzubeugen, gibt es nun die Option, bei der [Wiederherstellung von Snapshots]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}}) auch den Big-Data-Speicher der damaligen Version wiederherzustellen.
