---
title: 'SeaTable 6.2: Code meets No-Code'
description: 'SeaTable 6.2 führt einen höchst flexiblen HTML-Seitentyp und weitere Verbesserungen im App Builder ein. Zudem gibt es neue Funktionen bei Formelspalten und externen Links.'
date: 2026-07-13
author: 'rdb'
url: '/de/seatable-release-6-2'
color: '#dc6165'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 6.2: Code meets No-Code'
    description: 'SeaTable 6.2: neuer HTML-Seitentyp und weitere Verbesserungen im App Builder sowie neue Funktionen bei Formelspalten und externen Links.'
register:
    show: true
---

Der [App Builder]({{< relref "help/app-builder" >}}) erhält mit SeaTable 6.2 einen neuen Seitentyp: **HTML-Seiten** erlauben die Erstellung vollständig individueller Seiten auf Basis von HTML, JavaScript und CSS. Damit entfallen in Sachen Datenvisualisierung nahezu alle Einschränkungen. Auch Webformulare lassen sich exakt nach Ihren Anforderungen gestalten und selbst komplexe Interaktionen können Sie problemlos umsetzen. Geht nicht, gibt's nicht mehr!

Auch sonst steht der App Builder in Version 6.2 im Fokus. Der Seitentyp [Einzelner Datensatz]({{< relref "help/app-builder/seitentypen-in-universellen-apps/seiten-vom-typ-einzelner-datensatz-in-universellen-apps" >}}) erhält gleich ein dreifaches Upgrade: Alle Spaltenwerte lassen sich nun einheitlich als Text darstellen, universell formatieren und – ein häufig geäußerter Wunsch – direkt auf der Seite "inline" bearbeiten.

Andere [Seitentypen]({{< relref "help/app-builder/seitentypen-in-universellen-apps" >}}) profitieren von einer erweiterten Berechtigungsverwaltung für Verknüpfungsspalten. Darüber hinaus sorgen kleinere Designanpassungen für mehr Übersicht: Apps ohne Seiten werden als solche gekennzeichnet, um Missverständnisse zu vermeiden, und der Avatar inklusive App-Benachrichtigungen hat einen neuen Ort gefunden.

[Formelspalten]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) erhalten mit SeaTable 6.2 gleich zwei neue Fähigkeiten: Die neue Funktion **datetimeFormat()** wandelt Datumswerte in Strings mit einem frei definierbaren Format um. Wenn Ihr bevorzugtes Datumsformat von SeaTable bisher nicht angeboten wurde, ist das damit ein Ding der Vergangenheit. Außerdem unterstützen String-Formeln jetzt **Zeilenumbrüche**, wodurch sich Texte aus unterschiedlichen Spalten deutlich flexibler zusammensetzen lassen.

Nicht zuletzt verbessert SeaTable 6.2 die Zusammenarbeit: [Externe Links]({{< relref "help/startseite/freigaben/externer-link-erklaert" >}}) und [Einladungslinks]({{< relref "help/startseite/freigaben/einladungs-link-erklaert" >}}) können jetzt mit einer Beschreibung versehen werden, sodass sich Zweck und vorgesehene Empfänger direkt am Link notieren lassen. Außerdem wurde das Menüband für Bases und Ansichten, die über externe Links aufgerufen werden, überarbeitet und übersichtlicher gestaltet.

Das [Changelog](https://cloud.seatable.io/dtable/view-external-links/c9124bcd934b47bc8f30/) protokolliert – wie immer – alle relevanten Änderungen.

Für [SeaTable Server]({{< relref "pages/product/seatable-server" >}}) steht Version 6.2 mit dem heutigen Tag im [SeaTable Docker Repository](https://hub.docker.com/r/seatable/seatable-enterprise) zum Download zur Verfügung.

Das Update von [SeaTable Cloud]({{< relref "pages/product/seatable-cloud" >}}) erfolgt **am 4. August**. Mit dem Update wird das Monatskontingent für die [Ausführung von Python-Skripten]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}) dynamisiert. Analog zu API-Aufrufen oder Automatisierungen wird das Gesamtkontingent für Python-Skripte an die Größe eines Teams geknüpft. Ein Plus Team erhält 250 Python-Skriptläufe, ein Enterprise Team 1.000 Python-Ausführungen pro Benutzer und Monat. Beim Free Abonnement gilt weiterhin ein pauschales Ausführungslimit von 100 pro Monat.

{{< warning headline="Breaking Changes bei Python-Skripten" >}}

Die Rückgabewerte des Context-Objekts und der Query-Methode für die Spaltentypen Datum, Formel sowie Formel für Verknüpfungen werden in Version 6.2 harmonisiert. Dies kann dazu führen, dass die Ausführung Ihrer Skripte zu Fehlern führt. Bitte prüfen und aktualisieren Sie Ihre Python-Skripte.

{{< /warning >}}

## Neuer App-Seitentyp: HTML-Seite

Mit dem **SeaTable App Builder** lassen sich leistungsfähige Anwendungen erstellen – ganz ohne Programmierung. Dank der vordefinierten Seitentypen entsteht in kurzer Zeit eine voll funktionsfähige Webanwendung. Diese Effizienz hat jedoch ihren Preis: Die **10 Seitentypen** bieten zwar zahlreiche Konfigurationsmöglichkeiten, geben Aufbau und Verhalten einer Seite aber vor. Individuelle Anpassungen, die darüber hinausgehen, waren bislang nicht möglich.

Sie möchten einen Diagrammtyp verwenden, den SeaTable nicht unterstützt? Ein hochgradig individualisiertes Webformular erstellen? Ein interaktives Schaubild mit klickbaren Elementen einbinden? Oder mehrere Darstellungen – beispielsweise Tabelle und einzelner Datensatz – auf einer Seite kombinieren? Mit dem neuen Seitentyp **HTML-Seite** lassen sich diese und viele weitere Anforderungen umsetzen.

![Neuer App-Seitentyp: HTML-Seite](HTMLPage.png)

HTML-Seiten können **statische Inhalte** anzeigen, Ihr Potenzial entfalten Sie jedoch in Verbindung mit den **Daten einer Base**. Genauso wie andere Seitentypen des App Builders können sie Daten aus einer Base abrufen und Datensätze in einer Base ändern. Bei der **Gestaltung der Benutzeroberfläche** sind Sie dagegen nahezu frei. Was sich mit HTML, CSS und JavaScript realisieren lässt, können Sie grundsätzlich auch als HTML-Seite im App Builder umsetzen.

Nicht verwirren lassen sollte man sich vom Namen. HTML-Seiten unterstützen nicht nur **HTML**, sondern ebenso **JavaScript und CSS**. Der gesamte Code der Seite wird als Bundle in die App hochgeladen. Die Funktionsweise, die möglichen Entwicklungsansätze sowie die Referenz des dazugehörigen Software Development Kits (SDK) finden Sie im [SeaTable Developer Manual](https://developer.seatable.com/html-pages/ 'SeaTable Developer Manual'). Auch ein Beispiel für eine Seite finden Sie dort.

Aktuell richtet sich der Seitentyp insbesondere an **Benutzer mit Programmiererfahrung**. Bereits in Entwicklung ist eine KI-Funktion, mit der sich HTML-Seiten künftig auch in natürlicher Sprache und ohne Programmierkenntnisse erstellen lassen.

## Verbesserter App-Seitentyp: Einzelner Datensatz

Der Seitentyp **Einzelner Datensatz** erhält in SeaTable 6.2 gleich mehrere Verbesserungen. Bislang konnten Sie Datensätze nur über die Zeilendetails bearbeiten, die Sie zunächst über die Schaltfläche „Eintrag bearbeiten“ öffnen mussten. Das bedeutete zusätzliche Klicks und einen unnötigen UX-Bruch im Bearbeitungsablauf.

Mit SeaTable 6.2 gehört dieser Zwischenschritt der Vergangenheit an. Verfügt ein Benutzer über die erforderlichen Bearbeitungsrechte, lassen sich Felder nun direkt auf der Seite bearbeiten. **Ein Klick auf ein Feld aktiviert den Bearbeitungsmodus**, Eingaben werden wie gewohnt validiert und Änderungen unmittelbar gespeichert. Das sorgt für einen deutlich flüssigeren und intuitiveren Arbeitsablauf.

![Inline-Editing auf Single Record Pages](SingleRecordPage_InlineEditing.png)

Auch die Darstellung wurde erweitert. **Spaltentypen** mit einer eigenen visuellen Darstellung – beispielsweise die Labels von [Einfachauswahl-]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) oder [Mitarbeiter-Spalten]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) – können jetzt optional als reiner Text angezeigt werden. Für alle als Text dargestellten Werte steht zudem ein einheitlicher Satz an **Formatierungsoptionen** zur Verfügung: Schriftgröße, Schriftfarbe, Ausrichtung und Hintergrund lassen sich unabhängig vom ursprünglichen Spaltentyp konsistent anpassen. So können Sie Seiten mit einem einheitlichen und aufgeräumten Erscheinungsbild gestalten.

## Erweiterte Berechtigungen für Verknüpfungen in der App

SeaTable 6.2 schließt eine Lücke in der Berechtigungsverwaltung von [Verknüpfungsspalten]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) im App Builder. Mit der neuen Berechtigung **Bestehende Einträge entfernen** lässt sich gezielt festlegen, ob Benutzer bestehende Verknüpfungen löschen dürfen.

Bislang konnte jeder Benutzer mit Bearbeitungsberechtigung bestehende Verknüpfungen entfernen. Dieses Verhalten lässt sich nun unabhängig von den übrigen [Seitenberechtigungen]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) für die Verknüpfungsspalte steuern.

![Neue Berechtigung in der App: Bestehende Verknüpfungen löschen](AppBuilder_RemoveExistingRecords.png)

Nun können Sie die Zugriffsrechte für Verknüpfungsspalten umfassend verwalten: Benutzer dürfen je nach Konfiguration neue Datensätze in der verknüpften Tabelle anlegen, bestehende Datensätze verknüpfen, ändern und entfernen – jeweils mit eigenen Berechtigungen. Das ermöglicht eine **deutlich präzisere Steuerung von Bearbeitungsrechten in Apps**.

## Neue Funktion in der Formelspalte

Die neue Funktion **datetimeFormat()** hilft Ihnen, Datumswerte genau so darzustellen, wie Sie diese benötigen. Der erste Parameter enthält das zu formatierende Datum bzw. den Verweis auf die Spalte, die den Wert enthält. Im zweiten Parameter definieren Sie das Zielformat.

![Formel für formatierte Datumswerte](FormulaColumn_datetimeFormat.png)

In String-Formeln können Sie nun mit "\n" bzw. '\n' einen **Zeilenumbruch** einfügen. Dies ist insbesondere dann hilfreich, wenn Sie mehrere Spalten verketten, aber die Werte nicht in eine Zeile schreiben möchten. Paradebeispiel dafür ist eine Adresse:

![Zeilenumbrüche in String-Formeln](FormulaColumn_LineBreak.png)

## Verbesserungen bei externen Links und Einladungslinks

Nicht zuletzt hält SeaTable 6.2 eine Optimierung für **externe Links und Einladungslinks** bereit. Diese können Sie jetzt mit einer **Beschreibung** versehen. So lassen sich beispielsweise Zweck und vorgesehene Empfänger direkt am Link notieren. Außerdem haben wir das Menüband für Bases und Ansichten, die über externe Links aufgerufen werden, überarbeitet und übersichtlicher gestaltet.

## Und noch einiges mehr

- **Verbessertes Base-Log**:​ Das [Base-Log]({{< relref "help/base-editor/historie-und-versionen/aenderungen-ueber-die-logs-rueckgaengig-machen" >}}) wurde an mehreren Stellen überarbeitet. Suchfelder erleichtern die Auswahl in großen Bases, Drop-down-Menüs präsentieren sich in einem einheitlichen Design und auch Aktionen in gelöschten Tabellen können Sie nun filtern.

- **Verbessertes Datums-Widget​**: Das Datums-Widget wurde hinsichtlich Bedienung und Darstellung optimiert und bietet ein noch komfortableres Arbeiten mit [Datumswerten]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}).

- **Emojis in Kommentaren​**: [Kommentare]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) unterstützen jetzt Emojis. Das macht Rückmeldungen, Reaktionen und die Zusammenarbeit noch ausdrucksstärker.

## Anpassung der Rückgabewerte in Python-Skripten

Mit dem Ziel einer Harmonisierung der Formate werden die Rückgabewerte einiger Spaltentypen für das Context-Objekt und die Query-Methode in SeaTable 6.2 aktualisiert. Dies erfordert gegebenenfalls die Anpassung Ihrer Python-Skripte.

Eine Gegenüberstellung der Rückgabewerte in SeaTable 6.1 und SeaTable 6.2 finden Sie im [SeaTable Forum](https://forum.seatable.com/t/important-changes-related-to-python-client-in-seatable-6-2/7435).

Für manuell ausgeführte Skripte, d.h. Skripte, die Sie per Button oder im Python-Editor von SeaTable ausführen, müssen Sie alle dort genannten Änderungen berücksichtigen. Skripte, die per Automation ausgeführt werden, müssen Sie nur in Bezug auf die Änderungen in Zusammenhang mit der Query-Methode anpassen.
