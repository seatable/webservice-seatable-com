---
title: 'SeaTable 6.1: Mehr Power für Apps, Bases und Integrationen'
description: 'SeaTable 6.1 bringt Neues für den App Builder, den Base Editor und im Bereich Integrationen. Es ist für alle etwas dabei.'
date: 2026-03-20
author: 'rdb'
url: '/de/seatable-release-6-1'
color: '#fad102'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 6.1: Mehr Power für Apps, Bases und Integrationen'
    description: 'SeaTable 6.1 bringt Neues für den App Builder, den Base Editor und im Bereich Integrationen. Es ist für alle etwas dabei.'
register:
    show: true
---

Im **App Builder** erhöht sich die Anzahl der [Seitentypen]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) auf 10; neu dabei ist der Seitentyp **Karte**. Auf den anderen Seitentypen erweitert SeaTable 6.1 die Möglichkeiten von Verknüpfungsspalten. Diese lassen sich nun einheitlich konfigurieren und mit fein abgestuften Berechtigungen belegen. App-Benutzer dürfen sich über eine **Druckoption für Dashboards** sowie erweiterte Filter- und Sortierfunktionen freuen.

Im **Base Editor** steht die [Verknüpfungsspalte]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) durch ein funktionales Upgrade im Mittelpunkt: Dynamische Filterregeln ermöglichen es, die auswählbaren Zeilen in Abhängigkeit von der jeweiligen Ursprungszeile zu steuern – jede Zeile bekommt damit ihre individuelle Auswahl. Ebenfalls neu sind die beiden [Ansichtstypen]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) **Baum** und **Zeitstrahl**, welche die gleichnamigen Plugins ersetzen. In den Base Logs schaffen Filter mehr Übersicht über die Aktivitäten in einer Base.

Auch im Bereich **Integrationen** hat sich einiges getan: SeaTable 6.1 führt eine Anbindung an Google Kalender und eine Importfunktion von Airtable ein. An die Seite des verbesserten Tabellenbeziehungen-Plugins gesellt sich das neue [KI-Chat-Plugin]({{< relref "help/ai/ai-chat/introduction" >}}), das Auswertungen und Änderungen an Daten mittels natürlicher Sprache möglich macht.

SeaTable 6.1 steht ab sofort im bekannten [Docker Repository](https://hub.docker.com/r/seatable/seatable-enterprise) zum Download zur Verfügung; im [Changelog](https://cloud.seatable.io/dtable/view-external-links/c9124bcd934b47bc8f30/) finden Sie – wie immer – die vollständige Liste aller Änderungen.

Das neue Release wird am 25. März auf [SeaTable Cloud]({{< relref "pages/product/seatable-cloud" >}}) ausgerollt. Mit dem Update geht eine Aufwertung der Free und Plus Abonnements einher. **Automationen**, bisher exklusiv im Enterprise Abonnement enthalten, werden künftig auch in [Free und Plus]({{< relref "pages/prices" >}}) verfügbar sein. Free Teams erhalten 100 Automationsausführungen pro Monat; Plus Teams 500 Ausführungen pro Monat und Teammitglied. Der Preis des Plus Abonnements bleibt dabei unangetastet und Free bleibt kostenlos.

## Leistungsfähigere Apps

Räumliche Verteilungen lassen sich in Bases mit dem [Karten-Plugin]({{< relref "help/base-editor/plugins/anleitung-zum-karten-plugin" >}}) visualisieren. Der neue Seitentyp **Karte** macht dies nun auch in Apps möglich. Mittels Seiten-Voreinstellungen lassen sich, wie auch auf anderen Seiten, Datensätze ausblenden und der Umfang der angezeigten Datensätze einschränken. Anzeigewert und Hover-Effekt lassen sich ebenfalls konfigurieren.

![Neuer Seitentyp für geografische Karten](map-page-app-builder-seatable-6-1.png)

{{< warning headline="Hinweis für Selbsthoster" >}}

In der Konfiguration von SeaTable Server muss ein **Google API Token** hinterlegt werden, damit der Seitentyp im App Builder angezeigt und genutzt werden kann. Details sind im [Admin Manual](https://admin.seatable.com/configuration/plugins/#map-plugin) nachzulesen.

{{< /warning >}}

SeaTable 6.1 vereinheitlicht die Einstellungsoptionen und das Berechtigungskonzept für **Verknüpfungsspalten im App Builder**. Auf Seiten vom Typ Galerie, Kanban, Kalender, Zeitleiste und einzelner Datensatz lassen sich drei Berechtigungen individuell aktivieren:

- Neue Einträge erstellen und verknüpfen
- Bestehende Einträge verknüpfen
- Verknüpfte Einträge bearbeiten

In SeaTable 6.2 wird die vierte Berechtigung **Bestehende Verknüpfungen entfernen** hinzukommen. Auf Seiten vom Typ Dashboard und Abfrage werden auch weiterhin keine Verknüpfungseinstellungen verfügbar sein, weil diese beiden Seitentypen grundsätzlich keine Bearbeitung erlauben.

Die **Spalteneinstellungen für die verknüpfte Tabelle** ermöglichen die individuelle Anpassung dieser Berechtigungen an den konkreten Anwendungsfall. Der App-Admin kann definieren, welche Spalten in der verknüpften Tabelle angezeigt werden, welche bearbeitbar und welche Pflichtfelder sind.

Auf den Seitentypen Galerie, Kanban und Kalender wurden in der neuen Version **Sortier- und Filterfunktionen** ergänzt. Diese erlauben es den App-Benutzern, den Umfang der angezeigten Daten und deren Darstellung anzupassen – ein spürbarer Gewinn an Übersichtlichkeit, sobald die Datenmenge wächst.

Mehr Flexibilität bietet die **neue Druckfunktion auf der Dashboard-Seite**. Wenn aktiviert, dann lässt sich mit dieser eine Seite ganz einfach auf Papier bringen.

## Leistungsfähigerer Base Editor

### Zwei neue Ansichtstypen

Der neue Ansichtstyp **Baumansicht** stellt Datensätze in einer hierarchischen Struktur mit auf- und zuklappbaren Knoten – einer Baumstruktur – dar und ermöglicht so eine intuitive Visualisierung der Zusammenhänge zwischen den Datensätzen. Die **Hierarchie der Datensätze** ergibt sich dabei durch die Verknüpfungen zwischen den Tabellen. Die Baumansicht eignet sich insbesondere für die Verwaltung von Produktkategorien und Projektorganisationen.

{{< warning headline="Nutzungshinweis" >}}
Die neue Baumansicht ist aktuell auf **drei Hierarchieebenen** begrenzt und unterstützt keine Verknüpfungen innerhalb einer Tabelle.
{{< /warning >}}

Der zweite neue Ansichtstyp **Zeitleistenansicht** ordnet Datensätze auf einem Zeitstrahl an und ist damit erste Wahl, wenn zeitliche Zusammenhänge und Abhängigkeiten im Vordergrund stehen.

![Neue Ansichtstypen](two-new-views-seatable-6-1.png)

Die neuen Ansichten werden **die gleichnamigen Plugins ersetzen**. Die Reimplementierung als Ansichten ist aber mehr als nur eine Änderung des Benutzerinterfaces. Als vollwertige Ansichten lassen sie sich über Ansichtsfreigaben gezielt teilen und in benutzerdefinierten Freigaben berücksichtigen, was mit einem Plugin schlicht nicht möglich ist. Die Baumansicht legt zudem funktional nach. Für jede Hierarchieebene können die anzuzeigenden Spalten ausgewählt werden. Beim [Baum-Plugin]({{< relref "help/base-editor/plugins/anleitung-zum-tree-plugin" >}}) war dies auf die oberste Ebene beschränkt.

### Filterregeln in Verknüpfungsspalten

Etwas versteckt in den Einstellungen der Verknüpfungsspalte findet sich eine der nützlichsten Neuerungen: Die Option **Verknüpfungen mit einer Filterregel einschränken**. Damit lässt sich die Auswahl der verknüpfbaren Zeilen auf Basis einfacher oder komplexer Regeln einschränken. Die Filter selbst können statisch oder dynamisch sein:

- Bei einem **statischen Filter** wird ein einheitlicher Filterwert genutzt, um die Zeilen in der verknüpften Tabelle zu filtern (z. B. nur Zeilen, die nicht den Wert "archiviert" haben, sind verknüpfbar). Der Effekt ist somit analog der Option **Verknüpfungen auf eine Ansicht einschränken**.
- Bei einem **dynamischen Filter** ist der Filterwert, der für die Filterung der Zeilen in der verknüpften Tabelle verwendet wird, ein Spaltenwert der aktiven Zeile (z. B. nur Zeilen, deren Status identisch mit dem Status der aktiven Zeile ist, sind verknüpfbar). **Zeilen mit unterschiedlichen Filterwerten** haben somit abweichende verknüpfbare Zeilen.

![Filterregeln in Verknüpfungsspalten](dynamic-link-selection-filters-seatable-6-1.png)

### Filteroptionen in den Base Logs

Administratoren werden sich über die Filteroptionen in den [Base Logs]({{< relref "help/base-editor/historie-und-versionen/aenderungen-ueber-die-logs-rueckgaengig-machen" >}}) freuen. Die Logs lassen sich nun nach Benutzer, Tabelle und Zeitraum filtern. Natürlich sind auch kombinierte Filter möglich. Wer in einer Base mit vielen Nutzern **Änderungen nachverfolgen oder rückgängig machen** möchte, wird die neue Übersichtlichkeit schnell zu schätzen wissen.

## Mehr Integrationen

Der Umstieg von Airtable zu SeaTable ist mit SeaTable 6.1 so unkompliziert wie nie: Beim Anlegen einer neuen Base einfach **Base von Airtable importieren** auswählen, im Importdialog eine Airtable Base ID und einen Personal Access Token eingeben, fertig. Den Rest erledigt SeaTable.

Die zweite neue Integration betrifft Google Kalender. Die neue Automatisierungsaktion **Termine in Google Kalender verwalten** ermöglicht es, Termine direkt aus SeaTable heraus in einem Google Kalender anzulegen und bestehende zu aktualisieren.

### Upgrade des Tabellenbeziehungen-Plugins

Das [Tabellenbeziehungen-Plugin]({{< relref "help/base-editor/plugins/anleitung-zum-tabellenbeziehungen-plugin" >}}) ist ein alter Bekannter und erhält mit SeaTable 6.1 ein umfangreiches Upgrade :

- Tabellen lassen sich individuell ausblenden
- Angezeigte Spalten lassen sich über die Auswahl einer Ansicht steuern
- Verknüpfungen innerhalb einer Tabelle lassen sich ausblenden
- Umfangreiche Formatierungsfunktionen
- Export-Funktion
- Diagramm-zurücksetzen-Funktion
- Notizfunktion

So lassen sich auch für komplexe Bases übersichtliche Beziehungsdiagramme erstellen.

![Verbessertes Tabellenbeziehungen-Plugin](table-relationship-plugin-seatable-6-1.png)

### Chatten Sie mit einer künstlichen Intelligenz

Brandneu ist das **KI-Chat-Plugin**. Es erlaubt, Bases in natürlicher Sprache zu bearbeiten und auszuwerten. Datensätze anlegen, Werte ändern, Zeilen verknüpfen, Auswertungen erstellen – auf Deutsch, Englisch, Französisch und weiteren Sprachen. Gerade bei Ad-hoc-Auswertungen jenseits der Standardfunktionen spielt das Plugin seine Stärken aus.

Ein Beispielprompt für die Auswertung einer Adressdatenliste wäre: „Liste alle Personen aus der Adressdatenliste auf, die in einer Stadt mit mehr als 1 Million Einwohner wohnen.“ Das Modell wertet daraufhin die Wohnadressen aus, ermittelt die Einwohnerzahl des Wohnorts und erzeugt auf dieser Basis die Ergebnisliste.

![KI-Chat-Plugin](chat-ai-plugin-seatable-6-1.png)

Um das Plugin zu nutzen, müssen Sie in den [Settings]({{< relref "help/ai/ai-chat/setup" >}}) des Plugins einen **API-Token für eines der unterstützten LLMs** hinterlegen. Zu den [unterstützten Modellen]({{< relref "help/ai/ai-chat/supported-models" >}}) gehören solche von Anthropic, OpenAI und Mistral. Weitere Modelle werden demnächst ergänzt.

{{< warning headline="Beta-Stadium" >}}
Das KI-Chat-Plugin befindet sich im Beta-Stadium. Wir freuen uns, wenn Sie Ihre Erfahrungen mit uns im [SeaTable Forum](https://forum.seatable.com/t/we-need-your-feedback-ai-chat-for-seatable/7265) teilen.
{{< /warning >}}

## Und noch mehr

- [Formulare]({{< relref "help/base-editor/webformulare/webformulare" >}}) – sowohl klassische als auch solche in Apps – können ab sofort **mehrseitig** gestaltet werden. Das erhöht die Übersichtlichkeit spürbar, sobald viele Felder im Spiel sind.

- [E-Mail-Spalten]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}) erlauben die Speicherung von E-Mail-Adressen im Format 'Anzeigename < mail@example.com >'. Das Senden von E-Mails an solche Adressen schlug bisher fehl – sowohl in Automatisierungsregeln als auch bei Schaltflächen. Dies ist mit SeaTable 6.1 Geschichte.

- Die neue [Automations-Aktion]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) **Archivieren** erlaubt es, das Verschieben von Datensätzen aus dem Base Editor in das [Big-Data-Backend]({{< relref "help/base-editor/big-data/zeilen-ins-big-data-backend-verschieben" >}}) zu automatisieren. Die Aktion wird für beide periodischen Trigger angeboten.

## Abkündigungen

Mit SeaTable 6.2 werden zwei Funktionen aus SeaTable entfernt.

1. Die Funktion zur **Synchronisation von E-Mails mittels IMAP** wird mit SeaTable 6.2 aus SeaTable entfernt. Wir bitten betroffene Nutzer, die Synchronisation über eine der unterstützten Automationsplattformen – Make, n8n oder Zapier – nachzubilden.
2. Mit SeaTable 6.2 endet auch die Unterstützung von Apps, die auf dem [Galerie- oder Datenabfrage-App-Builder]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}) von SeaTable Version 4.3 und früher basieren. Wir empfehlen, diese Apps auf den [Universellen App Builder]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}) zu migrieren, der erheblich mehr Möglichkeiten bietet.

SeaTable 6.2 wird voraussichtlich Mitte/Ende Mai 2026 erscheinen.
