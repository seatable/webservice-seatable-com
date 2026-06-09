---
title: 'SeaTable 4.4: Universal App, Excel Import & Common Datasets'
description: 'Universal App unterstützt Buttons in Abfragen, Spalten-Füllgriff und Kalender-Drag&Drop. Mitarbeiter-Spalten im Formular, mehr Charts, Titelbalken auf Custom-Pages ausblendbar, Gallery- und Query-Apps durch Universal-Lösung ersetzt. Excel-Import stabil/flexibel, Common Datasets besser gemanagt, Defaultwerte überall.'
date: 2024-05-15
lastmod: '2024-05-15'
author: 'kgr'
url: '/de/seatable-release-4-4'
color: '#96b228'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 4.4: Universal App, Excel-Import, Datasets'
    description: 'Universal App Builder mit Buttons, flexibler Kalender, verbesserter Excel-Import, Common Datasets und Defaultwerte — SeaTable 4.4 liefert Komfort!'
---

In SeaTable 4.4 setzen wir die Entwicklung des Universal App Builders mit Verve fort. Viele neue Funktionen ermöglichen noch leistungsfähigere und komfortablere Webanwendungen. Darüber hinaus haben wir die Importfunktion und die gemeinsamen Datensätze aufpoliert. Die praktischen Standardwerte greifen nun universell.

Heute Morgen haben wir SeaTable Cloud auf Version 4.4 aktualisiert. Alle Selbsthoster können das ebenfalls tun: Das Image von SeaTable 4.4 ist im bekannten [Docker Repository](https://hub.docker.com/r/seatable/seatable-enterprise) zum Download verfügbar. Im [Changelog]({{< relref "pages/changelog" >}}) finden Sie wie immer die vollständige Liste der Änderungen.

## Flexiblerer, leistungsfähigerer App Builder

In SeaTable 4.4 haben wir wieder jede Menge Verbesserungen und Bugfixes an der [Universellen App]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}) vorgenommen, von denen fast alle [Seitentypen]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) profitieren. Das Ende der Beta-Phase rückt damit in greifbare Nähe.

### Buttons auf Abfrageseiten

[Abfrageseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}) unterstützen nun die Ausführung von Schaltflächen-Aktionen: Nach einer erfolgreichen Datenabfrage können Sie in der angezeigten Trefferliste [Schaltflächen]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) betätigen, um Aktionen auszuführen. Dies ist eine besondere Neuerung, denn bisher war in SeaTable nirgends eine Interaktion mit abgefragten Zeilen möglich.

![Schaltflächen auf Abfrageseiten ausführen](Schaltflaechen-auf-Abfrageseiten-ausfuehren.gif)

Ein Anwendungsbeispiel ist eine interne Stellenbörse: Die Abfrageseite erlaubt die schnelle Suche nach relevanten Positionen. Ist eine interessante Stelle dabei, dann reicht ein Klick auf die Schaltfläche in den Suchergebnissen, um sich direkt für die Stelle zu bewerben.

### Drag and Drop im Kalender

Bislang war es nicht möglich, Termine auf der [Kalenderseite]({{< relref "help/app-builder/seitentypen-in-universellen-apps/kalenderseiten-in-universellen-apps" >}}) zu ändern. Mit SeaTable 4.4 bekommen Sie hier mehr Flexibilität. Ab jetzt können Sie Ihre Termine im Kalender komfortabel per Drag and Drop verschieben. Zudem können Sie die Werte in den entsprechenden [Datum-Spalten]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) über die Zeilendetails bearbeiten, sofern Sie die notwendige [Berechtigung]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) besitzen.

### Vereinfachtes Datenhandling auf der Tabellenseite

Wie in der Base können Sie nun auch auf den [Tabellenseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}) Ihrer Apps mit nur einem Klick auf den Spaltenkopf [alle Einträge in einer Spalte markieren]({{< relref "help/base-editor/tabellen/hinzufuegen-von-daten-per-copy-and-paste" >}}). Auch der praktische [Füllgriff]({{< relref "help/base-editor/zeilen/duplizieren-einer-zeile" >}}) ist nun möglich: Ziehen Sie das kleine Quadrat in der unteren rechten Ecke einer Zelle nach unten, um den Wert in alle darunterliegenden Zeilen zu übertragen.

![Spalteneinträge markieren](Spalteneintraege-markieren-und-Fuellgriff-in-App.gif)

### Mitarbeiter-Spalte auf Formularseiten verfügbar

Wenn Sie eine [Mitarbeiter-Spalte]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) in Ihrer Tabelle nutzen, ist diese in [Webformularen]({{< relref "help/base-editor/webformulare" >}}) **nicht** verfügbar. Jedoch können Sie ab SeaTable 4.4 Mitarbeiter-Spalten auf [Formularseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/formularseiten-in-universellen-apps" >}}) der Universellen App hinzufügen. So können sich Ihre Teammitglieder beispielsweise bei einem Urlaubsantrag selbst auswählen und müssen ihre Namen nicht mehr manuell eintragen. Zuvor müssen Sie in den [App-Einstellungen]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern/" >}}) die Option aktivieren, dass die Mitarbeiterliste angezeigt werden soll.

### Mehr Customizing-Optionen für individuelle Seiten

In Version 4.4 können Sie auf der [individuellen Seite]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}) die **Titelleiste** ausblenden. So lassen sich optisch ansprechende Landingpages gestalten. Bei den Elementen Bild und Karte erlauben Drop-down-Menüs die schnelle **Verlinkung** von anderen Seiten der App. Bei den **Statistiken** haben wir weitere Diagrammtypen hinzugefügt und zusätzliche Konfigurationsmöglichkeiten ergänzt, welche die Erstellung von Dashboards noch komfortabler machen. Um die vielen Stiloptionen übersichtlich darzustellen, haben wir den Stil des Diagramms und den allgemeinen Stil in zwei verschiedene Reiter aufgeteilt.

## Galerie- und Datenabfrage-Apps

Wie in den letzten Release Notes angekündigt, haben wir in SeaTable 4.4 den **Galerie App Builder entfernt**. Wenn Sie eine neue App mit einer [Galerie]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}) anlegen wollen, dann steht Ihnen mit dem Universal App Builder eine funktional höherwertige Alternative zur Verfügung.

{{< warning headline="Gut zu wissen" text="**Bestehende Galerie-Apps funktionieren weiterhin**. Wir empfehlen aber, bestehende Galerie-Apps auf Universelle Apps umzustellen, um von Weiterentwicklungen und Verbesserungen zu profitieren." />}}

![Create app dialog](Create-app-dialog-.png)

Auch bei der [Datenabfrage-App]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}) hat sich einiges getan. Der alte App Builder für Datenabfragen wurde entfernt und durch einen neuen auf Basis des Universal App Builders ersetzt. Das heißt: Sie können natürlich weiterhin öffentliche Apps für die Abfrage Ihrer Bases anlegen, das Interface sieht nun aber aus wie im Universal App Builder. Für bestehende Abfrage-Apps gilt das Gleiche wie für Galerie-Apps: Sie müssen nichts tun und können diese weiter verwenden.

{{< warning headline="Effizienzgewinn" text="Durch die beschriebenen Änderungen können wir uns auf die Weiterentwicklung des Universal App Builders fokussieren und damit eine höhere Entwicklungsgeschwindigkeit für kommende Features erreichen." />}}

## Angenehmere User Experience beim Excel Import

Mit SeaTable 4.4 wird der [Import von Excel Tabellen]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}}) schneller, flexibler und stabiler: Tabellen mit vielen Tausend Zeilen werden nun in wenigen Augenblicken in SeaTable bereitgestellt. Im deutlich verbreiterten Vorschaufenster können Sie jetzt wählen, welche Tabellen einer Arbeitsmappe – alle oder nur einzelne – Sie aus der XLSX-Datei importieren möchten. Während Sonderzeichen in Spaltennamen und andere Spezialfälle in der Vergangenheit zu unerwünschten Ergebnissen führten, werden diese nun zuverlässig berücksichtigt. Verbesserte Fehlermeldungen geben klare Hinweise auf Konflikte, insbesondere beim [Import in den Big-Data-Speicher]({{< relref "help/base-editor/big-data/eine-excel-tabelle-ins-big-data-backend-importieren" >}}).

![Excel-Import](Excel-Import.png)

{{< warning headline="Kleiner Vorgeschmack" text="Mit SeaTable 5.0 machen wir den Import noch flexibler! Dann lassen sich auch einzelne Spalten einer Tabelle auswählen und vom Import ausschließen." />}}

## Mehr Funktionen für gemeinsame Datensätze

[Gemeinsame Datensätze]({{< relref "help/startseite/gemeinsame-datensaetze/funktionsweise-von-gemeinsamen-datensaetzen" >}}) sind sehr nützlich, wenn Sie und Ihre Teammitglieder bestimmte Tabellen (z. B. eine Mitarbeiterliste) über verschiedene [Gruppen]({{< relref "help/startseite/gruppen/einfuehrung-in-die-arbeit-mit-gruppen" >}}) hinweg in Ihren Bases benötigen. Mit SeaTable 4.4 kommen zu den bestehenden Funktionen drei weitere hinzu:

1. Wenn Sie eine [Base kopieren]({{< relref "help/startseite/bases/eine-base-in-eine-gruppe-kopieren" >}}), in die gemeinsame Datensätze eingebunden sind, können Sie entscheiden, ob Sie die Verbindung zu diesen Datensätzen beibehalten wollen. Die Gruppe, in die Sie die Base kopieren, muss dafür natürlich Zugriff auf die gemeinsamen Datensätze haben.

    ![Retain link to common dataset when copying a base](Retain-link-to-common-dataset-when-copying-a-base.gif)

2. Nach der [Wiederherstellung von Bases aus Snapshots]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}}) oder der [Erstellung einer Base aus einer Vorlage]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}}) können Sie bestehende Tabellen mit einem gemeinsamen Datensatz verknüpfen und dadurch die Synchronisation mit den dortigen Daten ermöglichen. Bisher ließen sich gemeinsame Datensätze nicht reimportieren, sondern nur in neue Tabellen einbinden.

    ![Reimport common dataset](Reimport-common-dataset.gif)

3. Der Ersteller eines gemeinsamen Datensatzes kann neuerdings die [Synchronisation]({{< relref "help/startseite/gemeinsame-datensaetze/synchronisation-eines-gemeinsamen-datensatzes" >}}) aller abhängigen Tabellen mit dem Datensatz erzwingen und so sicherstellen, dass die anderen Benutzer in ihren Bases den aktuellen Stand der Daten verwenden. In der Vergangenheit mussten Sie darauf vertrauen, dass die Benutzer die automatische Synchronisation eingerichtet haben oder die Synchronisation manuell anstoßen.

    ![Force sync of common dataset](Force-sync-of-common-dataset.png)

## Standardwerte greifen überall

Mit Version 4.4 generalisiert SeaTable die Anwendung von [Standardwerten]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}). Wenn Sie eine neue Zeile anlegen, sei es in der Tabelle einer Base oder App, per [Link-Spalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), [Webformular]({{< relref "help/base-editor/webformulare" >}}), [Schaltfläche]({{< relref "help/base-editor/schaltflaechen/zeilen-per-schaltflaeche-in-eine-andere-tabelle-kopieren" >}}) oder [Automation]({{< relref "help/base-editor/automationen/automations-aktionen" >}}), kommen die Standardwerte bei der Erstellung der Zeile überall zum Tragen. Bisher griffen die Standardwerte nur, wenn in einer Tabelle manuell eine neue Zeile angelegt wurde.

Da sich der Wirkungsbereich der Standardwerte erheblich vergrößert hat, haben wir bei den Spaltenoptionen auch einen prominenten Menüpunkt geschaffen, über den Sie die Standardwerte bequem einstellen können.

![Standardwert greift überall bei neuen Zeilen](Standardwert-greift-ueberall-bei-neuen-Zeilen.gif)

{{< warning headline="Hinweis" text="Wenn sowohl in der Tabelle als auch im Webformular ein Standardwert definiert ist, greift der Wert aus dem Formular für alle Zeilen, die über das Formular erstellt werden." />}}

Übrigens: Sogar bei der Neuanlage von Zeilen per API können Sie die Standardwerte mit dem entsprechenden Parameter aktivieren.

## Und vieles mehr

Den **Editor für formatierten Text** kennen Sie bereits von verschiedenen Stellen in SeaTable, z. B. von der [Base-Beschreibung]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}}), dem [Spaltentyp für lange Texte]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) oder [E-Mail-Nachrichten]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}). Mit SeaTable 4.4 haben wir die Usability verbessert und einige Bugs behoben. Hier nur zwei: Bisher wurden mehrfache Zeilenumbrüche beim Schließen des Editors entfernt und bestehender Text beim Tippen in der Zelle überschrieben. Im neuen Editor bleiben mehrfache Zeilenumbrüche erhalten und können dazu dienen, den Text übersichtlicher zu strukturieren. Auch die Gefahr von ungewollten Löschungen haben wir beseitigt: Bei der Eingabe wird der neue Text dem bestehenden Text vorangestellt.

In der neuen Version haben wir auch die **Benachrichtigungszentrale** {{< seatable-icon icon="dtable-icon-notice" >}} auf der Startseite verbessert. Jetzt können Sie alle [Benachrichtigungen]({{< relref "help/startseite/benachrichtigungen/sinn-und-zweck-von-benachrichtigungen-in-seatable" >}}) im System an einem Ort sehen, die Quelle der Benachrichtigung nachvollziehen und mit einem Klick zur entsprechenden Seite gelangen.

Zu guter Letzt haben wir den Dialog für das **Zurücksetzen des SeaTable Passworts** optimiert. Dafür haben wir das Design vereinheitlicht und mehr Funktionen hinzugefügt. Wenn Sie in Ihren persönlichen Einstellungen das [Passwort ändern]({{< relref "help/startseite/persoenliche-einstellungen/eigenes-passwort-aendern" >}}), können Sie es sich nun per Klick auf das Augensymbol im Klartext einblenden lassen. Zudem bekommen Sie automatisch die Stärke Ihres neuen Passworts angezeigt.
