---
title: 'SeaTable 5.2: Erweiterte Filter in der Base und ein neues Plugin'
date: 2025-02-25
lastmod: '2025-02-25'
author: 'rdb'
url: '/de/seatable-release-5-2'
categories:
    - 'product-features'
color: '#9dcde3'
seo:
    title: 'SeaTable 5.2 Release: Filtergruppen, Whiteboard-Plugin & App-Builder'
    description: 'SeaTable 5.2: Filtergruppen (UND/ODER), spaltenübergreifende Formatierung, Whiteboard-Plugin, App-Builder-Features & API-News auf einen Blick!'
---

Das zweite Minor Release der Version 5 von SeaTable enthält zahlreiche Bugfixes und Detailverbesserungen, um die Arbeit mit SeaTable noch einfacher zu machen und Ihre Anwendungsfälle noch besser zu unterstützen: In Bases ermöglichen die **neuen Filtergruppen** eine deutlich präzisere Selektion von Daten(sätzen). Spaltenübergreifende Filter in der bedingten Zeilen- und Zellformatierung erlauben eine bisher so nicht mögliche handlungsorientierte Hervorhebung von Daten. Im **App Builder** profitiert jeder Seitentyp von größeren und kleineren Verbesserungen unterschiedlicher Art – erweiterte Berechtigungen, bessere Usability und mehr Funktionen. Zu SeaTable 5.2 gehören auch ein neues **Whiteboard-Plugin** und Verbesserungen an den Plugins Seitendesign und Kalender. Im [Changelog]({{< relref "pages/changelog" >}}/) finden Sie – wie immer – die vollständige Liste der Änderungen.

Heute Morgen um 6 Uhr mitteleuropäischer Zeit wurde SeaTable Cloud auf Version 5.2 aktualisiert und das neue Plugin bereitgestellt. Wir freuen uns über Ihr Feedback. SeaTable Server Admins finden das Docker Image von SeaTable 5.2 im bekannten [Docker Repository](https://hub.docker.com/r/seatable/seatable-enterprise) zum Download.

## Komplexe Filterregeln mit Filtergruppen

Version 5.2 macht SeaTables [Filterfunktionen]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) noch leistungsfähiger. Die neuen Filtergruppen erlauben die **Kombination von Filterregeln mit den logischen Operatoren UND und ODER**. Beispiel: Gesucht sind Männer geboren nach 1979 (Filtergruppe 1) oder Frauen geboren nach 1984 (Filtergruppe 2). Eine solche Filterung war in SeaTable bisher nicht möglich. In früheren Versionen waren alle Filterregeln entweder mit logischem UND oder ODER verknüpft.

![Filtergruppen mit logisch verknüpften UND/ODER-Bedingungen für komplexe Datenselektionen](Fitlergroups.png)

In kommenden Versionen führen wir Filtergruppen auch in Apps, Formularen und Automationen ein.

## Bedingte Formatierung mit spaltenübergreifendem Filter

Erweiterte Filtermöglichkeiten bietet die Version 5.2 auch in der bedingten [Zeilen-]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}) und [Zellformatierung]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}). Sie wollen eine Zelle auf Basis der Werte in anderen Spalten rot einfärben, um Aufmerksamkeit darauf zu lenken? Mit SeaTable 5.2 geht das! Die Farbcodierung einer Zeile oder Zelle lässt sich nun in Abhängigkeit jedes einzelnen Spaltenwerts in einem Datensatz formatieren. Und damit ist noch nicht Schluss: Die bedingte Formatierung kann auch Werte in mehreren Spalten berücksichtigen, unabhängig vom Spaltentyp.

![Spaltenübergreifende bedingte Zeilen- und Zellformatierung basierend auf mehreren Spaltenwerten](ConditionalFormatting.png)

## Funktionale Verbesserungen im App Builder

Der Seitentyp [Einzelner Datensatz]({{< relref "help/app-builder/seitentypen-in-universellen-apps/seiten-vom-typ-einzelner-datensatz-in-universellen-apps" >}}) profitiert von gleich mehreren Verbesserungen, aber auch die Formular-, Tabellen- und Dashboardseiten erhalten neue Funktionen bzw. Elemente. Bei den Seitentypen Zeitstrahl, Kalender und Abfrage haben wir die Berechtigungssteuerung ausgebaut und in den App-Einstellungen die Versionsverwaltung und die QR-Code-Funktion verbessert.

### Seitentyp Einzelner Datensatz

In den Seiteneinstellungen dieses Seitentyps findet sich ab SeaTable 5.2 die Funktion **Voreingestellt schreibgeschützte Spalten**, die bereits von anderen Seitentypen bekannt ist. In Kombination mit der [Seitenberechtigung]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) “Wer darf Zeilen bearbeiten?” kann der App-Admin präzise festlegen, welche Spaltenwerte eines Datensatzes durch die Benutzer erfasst bzw. geändert werden können und welche nicht.

![Seitentyp „Einzelner Datensatz“ mit Einstellung für voreingestellt schreibgeschützte Spalten](ROcolumns-SingleRecordPage.png)

Bei [gesperrten Datensätzen]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) erhält der Benutzer nun auch eine Rückmeldung, dass die Bearbeitung nicht möglich ist. Ein entsprechender Hinweis wird eingeblendet, wenn Sie den Mauszeiger in der Toolbar auf “Eintrag bearbeiten” bewegen.

Neben der Berechtigungssteuerung enthält die neue Version auch noch zwei Verbesserungen zur Steigerung der Nutzerfreundlichkeit: Felder vom Typ [URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}}) und [E-Mail]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}) sind ab sofort klickbar. Der Aufruf einer Webseite oder das Schreiben einer E-Mail geht so noch schneller. (Dateien in Dateispalten werden in der Version 5.3 klickbar.) Bei Bild-Elementen auf der Seite können Sie den Füllmodus einstellen. Drei Modi stehen Ihnen zur Verfügung: Anpassen, ausfüllen und dehnen.

### Seitentyp Formular

Einfache [Webformulare]({{< relref "help/base-editor/webformulare" >}}), die sich in der Base erstellen lassen, bieten eine **Weiterleitungsoption**. Benutzer werden nach der Einreichung automatisch zu einer Webseite umgeleitet. Diese Funktion haben wir nun auch auf den [Formularseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}) ergänzt und dabei die Besonderheiten der App berücksichtigt. Eine Weiterleitung kann entweder zu einer anderen App-Seite oder zu einer externen URL erfolgen. Die anderen App-Seiten lassen sich bequem aus einem Drop-down-Menü auswählen. Ebenfalls einstellen lässt sich, ob die Umleitung in einem neuen oder im gleichen Tab erfolgt.

### Seitentyp Tabelle

Die **voreingestellten Filter** in den Dateneinstellungen erlauben nun die Auswahl aller relevanten Spaltentypen inklusive [Formel-]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) und [Verknüpfungsspalten]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}). Damit ist eine wichtige funktionale Einschränkung bei der Vorfilterung der Daten aufgehoben. Mit der Implementierung von Filtergruppen in einer der kommenden Versionen wird dieser Seitentyp die gleichen leistungsfähigen Filtermöglichkeiten bieten wie die Base.

### Individuelle Seiten

Die [individuelle Seite]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}) erhält einen neuen Statistiktyp: Die **Einfache Tabelle** erlaubt – ähnlich wie die [Tabellenseite]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}) – die tabellarische Darstellung eines durch den App-Admin vorgefilterten und vorsortierten Datensatzes. Anders als auf der Tabellenseite ist es mit dem neuen Statistiktyp möglich, zwei oder mehr Tabellen auf einer Seite zu vereinen. In der Version 5.2 können App-Benutzer selbst keine eigenen Filter- und Sortierungregeln setzen. Diese Funktion werden wir in Zukunft ergänzen.

![Statistiktyp „Einfache Tabelle“ zur Anzeige vorgefilterter Datensätze in einer individuellen Seite](BasicTable.png)

### Seitentyp Kalender

SeaTable 5.2 liefert eine dringend notwendige Funktion für die [Kalenderseite]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kalenderseiten-in-universellen-apps" >}}) nach: Das **Hinzufügen von neuen Einträgen** direkt auf Seiten dieses Typs. Dafür haben wir die von anderen Seitentypen bekannte Seitenberechtigung “Wer darf Zeilen hinzufügen?” in den Seiteneinstellungen ergänzt. Zusammen mit der schon bestehenden Berechtigung “Wer darf Zeilen bearbeiten?” kann der App-Admin rollengenau festlegen, welche Benutzer bestehende Einträge ändern und neue anlegen dürfen. Bei bestehenden App-Seiten des Typs Kalender ist die neue Berechtigung auf “Niemand” gestellt.

### Seitentyp Zeitstrahl

Auch dieser Seitentyp profitiert von einer Erweiterung der Seitenberechtigungen. Dank der neuen Berechtigung “Wer darf Zeilen bearbeiten?” sind nun auch auf [Zeitstrahlseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/zeitstrahlseiten-in-universellen-apps" >}}) **direkte Änderungen an bestehenden Datensätzen** möglich. Ziehen Sie mit der Maus am Anfang oder Ende eines Balkens, ändert sich automatisch der Datumswert, was das Ereignis verlängert bzw. verkürzt. In existierenden Apps ist die neue Berechtigung an “Niemand” vergeben.

### Seitentyp Abfrage

Bisher war auf [Abfrageseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}) eine Interaktion mit den angezeigten Daten nur über Schaltflächen möglich. Da diese nur vordefinierte Aktionen ausführen konnten, waren individuelle Änderungen außen vor. Dies ändert sich nun durch die Option **Abfrageergebnis bearbeitbar machen**. Ist diese aktiviert, dann können die Werte der in der Abfrage enthaltenen Datensätze über die Zeilendetails bearbeitet werden. In öffentlichen Apps, auf die ohne Benutzeranmeldung zugegriffen wird, hat die Option jedoch keine Wirkung.

## Neues Whiteboard-Plugin

“Neues” Whiteboard-Plugin – gibt’s das Whiteboard-Plugin nicht schon seit [SeaTable 5.0]({{< relref "posts/seatable-releases/seatable-release-5-0" >}})? Das ist richtig, aber auch die Aussage “neues Whiteboard-Plugin” ist richtig. Das neue Plugin **Whiteboard (tldraw)** steht dem bisherigen Plugin in Sachen Gestaltungsmöglichkeiten in nichts nach, bietet darüber hinaus aber auch eine optimale **Unterstützung der Online-Kollaboration**. Sie können alleine, zu zweit oder im Team am Whiteboard arbeiten – alle Änderungen werden in Echtzeit aktualisiert und sind bei allen anderen Benutzern unmittelbar sichtbar.

Das neue Whiteboard-Plugin können Sie ergänzend oder als Alternative zum bisherigen Whiteboard-Plugin installieren und in Bases verwenden. Bestehende Whiteboards werden nicht automatisch migriert, Inhalte lassen sich aber mittels Copy-and-Paste mit wenig Aufwand übertragen. Wir empfehlen den kurzfristigen Wechsel zum neuen Whiteboard. Das neue Plugin nutzt eine separate Serverkomponente, die durch das namensgebende [tldraw Projekt](https://tldraw.dev/) bereitgestellt wird. Selbsthoster müssen diese Komponente installieren. Die Anleitung findet sich im [Admin Handbuch](http://admin.seatable.com/installation/components/whiteboard/).

Der Austausch des Plugins war nötig geworden, da das “alte” Whiteboard-Plugin, das auf dem Open-Source-Projekt [excalidraw](https://github.com/excalidraw/excalidraw) basiert, sich bei gleichzeitiger Nutzung durch mehrere Benutzer als störanfällig erwies. Mit der Version 6.0 im Sommer 2025 werden wir das alte Plugin aus SeaTable Cloud entfernen. Alle Whiteboards im alten Whiteboard-Plugin werden dann nicht mehr verfügbar sein.

![Whiteboard-Plugin „Whiteboard (tldraw)“ mit gleichzeitiger Echtzeitbearbeitung durch mehrere Nutzer](tldraw-collaboration.png)

## Wichtige Änderungen an der API von SeaTable

Mit der Veröffentlichung von Version 5.2 möchten wir eine wichtige Änderung an der API von SeaTable ankündigen. Dies betrifft nur Anwender, die mithilfe der API ihre eigenen Anwendungen und Workflows umsetzen. Auf die Nutzung im Webinterface haben diese Änderungen keinen Einfluss.

In diesem [Forumspost](https://forum.seatable.com/t/important-changes-to-api-and-seatable-cloud-with-version-5-2/6317) finden Sie Details zu den Änderungen. Hier die wichtigsten Punkte in der Übersicht:

- Zur Harmonisierung der API-Struktur werden bestimmte Endpunkte als veraltet markiert. Neue Endpunkte stehen bereits zur Verfügung.
- Mit Version 6.0 werden die veralteten Endpunkte deaktiviert.
- Unsere Integrationen für [n8n](https://n8n.io/integrations/seatable/) und [Zapier](https://zapier.com/apps/seatable/integrations) haben wir bereits auf die neuen Endpunkte umgestellt. Die [Make App](https://www.make.com/en/integrations/seatable) wird in Kürze folgen.

Wenn Sie individuelle Skripte oder Integrationen nutzen, prüfen Sie bitte, ob Sie die alten Endpunkte verwenden. Wenn ja, dann müssen Sie diese bis spätestens zur SeaTable Version 6.0 anpassen.

## Und vieles mehr

SeaTable 5.2 hat noch weitere Neuigkeiten, die mehr als eine explizite Erwähnung verdienen:

Die Möglichkeit zur **Verwaltung von hierarchischen Daten in einer Tabelle** erreicht in SeaTable 5.2 ein neues Niveau: Eltern- und Kindbeziehungen werden in separaten Spalten erfasst und dargestellt. SeaTable stellt sicher, dass zu jeder Eltern- auch eine Kindbeziehung existiert. So lassen sich Beziehungen in beide Richtungen problemlos analysieren. Die Abbildung verdeutlicht den Unterschied zwischen SeaTable 5.2 (links) und SeaTable 5.1 (rechts) für das Topmanagement einer fiktiven Organisation.

![Gegenüberstellung interner Verknüpfungen in SeaTable 5.2 und 5.1 mit getrennten Eltern-/Kindspalten](InternalLinking-SeaTable-5.2-vs.-SeaTable-5.1.png)

Für Benutzer bringt dies nur Vorteile ohne zusätzliche Komplexität. Legt ein Benutzer eine **Verknüpfungsspalte**, die Einträge in ein- und derselben Tabelle verknüpft, neu an, dann erstellt SeaTable automatisch die zweite Verknüpfungsspalte. Die Plugins [Organigramm]({{< relref "help/base-editor/plugins/anleitung-zum-organigramm-plugin" >}}) und [Baum]({{< relref "help/base-editor/plugins/anleitung-zum-tree-plugin" >}}) können mit der verbesserten Datenstruktur ebenfalls umgehen.

Bei bestehenden Verknüpfungen innerhalb einer Tabelle findet keine Anpassung statt. Wenn Sie wechseln wollen, dann legen Sie eine neue Verknüpfungsspalte an und fügen die Links ein. Danach können Sie die alte Verknüpfungsspalte löschen.

SeaTable unterstützt mit der neuen Version die **Anmeldung an Google und Microsoft E-Mail-Konten mittels OAuth**. (Microsoft nennt das “moderne Authentifizierung”.) Gerade die Nutzung von Microsoft E-Mail-Konten war bisher nur unter großen Einschränkungen möglich, nachdem Microsoft die Authentifizierung mittels Benutzername und Passwort abgekündigt hat. Im Benutzerhandbuch finden Sie detaillierte Anleitungen, wie Sie ein Gmail, Outlook.com oder MS 365 Konto in einer SeaTable Base als [Drittanbieterkonto einbinden]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).

Tabellen lassen sich nun, wie man es aus Microsoft Excel kennt, ausblenden. Ein **ausgeblendetes Tabellenblatt** wird nicht mehr als Tab angezeigt und ist nur noch über das Drop-down-Menü aufrufbar.

[Checkboxen]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}}) bieten in SeaTable 5.2 mehr Stiloptionen und noch mehr Farboptionen. Wer den grünen Haken nicht mag, kann nun aus 69 anderen Optionen wählen.

Im [Kalender-Plugin]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}) lassen sich neue Einträge nun auch per Doppelklick oder über die neue Schaltfläche “+” anlegen.

## Zwei funktionale Änderungen

[Kommentierte Zeilen]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) werden in der Tabellenansicht der Base mit Sprechblasen-Icons gekennzeichnet. Bisher betrug die Anzeigedauer für diese Icons sieben Tage. Mit SeaTable 5.2 wird diese Dauer auf 180 Tage verlängert. Wundern Sie sich also nicht, wenn Ihre Tabellen mehr Sprechblasen aufweisen. Alle Zeilen mit einem Kommentar in den letzten 180 Tagen tragen nun ein Sprechblasen-Icon. Natürlich bleiben auch weiterhin alle Kommentare nach Ablauf der 180 Tage in der Base gespeichert.

Geschweifte Klammern in Tabellennamen können Konflikte bei Formeln provozieren. Aus diesem Grund verhindert SeaTable ab der Version 5.2 die Verwendung von **{** und **}** in Tabellennamen. Bestehende Tabellennamen werden nicht geändert.
