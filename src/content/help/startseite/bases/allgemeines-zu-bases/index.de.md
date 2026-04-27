---
title: 'Allgemeines zu Bases in SeaTable'
date: 2022-08-25
lastmod: '2023-05-03'
categories:
    - 'arbeiten-mit-bases'
author: 'cdb'
url: '/de/hilfe/bases-funktionen-verwaltung-seatable'
aliases:
  - '/de/hilfe/bases'
seo:
    title: 'Bases in SeaTable: Funktionen und Verwaltung im Überblick'
    description: 'Alles zu Bases in SeaTable: Verwaltung, Erstellung, Freigabe, Export, Löschung, Eigentümerwechsel und Funktionen für produktives Arbeiten.'
star: true
weight: 1
---

Bases sind in SeaTable von zentraler Bedeutung. Wann auch immer Sie Daten in SeaTable erfassen, auswerten, bearbeiten oder teilen, befinden Sie sich in einer Base.

Auf den ersten Blick ist eine Base nur ein **Container** für eine oder mehrere **Tabellen**. Aus dieser Perspektive liegt es nahe, eine Base mit einer Arbeitsmappe in Excel zu vergleichen. Dieser Vergleich wird einer Base aber nicht gerecht. Den Arbeitsmappen, wie man sie aus herkömmlichen Tabellenkalkulationen kennt, sind Bases in SeaTable weit überlegen, denn sie bieten:

- [Relationale Datenbankfunktionen]({{< relref "posts/relationale-datenbank" >}}) und die [Verknüpfung von Tabellen]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}})
- [Über 20 Spaltentypen]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}), die alle gängigen Datenformate abdecken
- Diverse [Freigabemöglichkeiten]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) zum einfachen Teilen von Daten
- Echtzeit-[Zusammenarbeit]({{< relref "help/erste-schritte/einfuehrung-funktionen/zusammenarbeit" >}}) mit anderen Nutzern und Echtzeit-Übertragung aller Änderungen
- Eine [Kommentarfunktion]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) zu jedem Datensatz in einer Zeile
- Vollständige [Versionierung]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) aller Änderungen
- Einen integrierten [Webformular-Editor]({{< relref "help/base-editor/webformulare/webformulare" >}}) und grafische [Plugins]({{< relref "help/base-editor/ansichten" >}})
- Einfache Integrationsmöglichkeiten dank REST-API

Bases sind also weit mehr als "Tabellenbehälter" im Web. Diese Vorteile werden Sie sehr schnell zu schätzen wissen und nie wieder missen wollen!

## Eigentümer von Bases

Jede Base hat einen (und nur einen) **Eigentümer**. Die Übertragung der Eigentümerschaft an einer Base von einem Nutzer auf einen anderen Nutzer ist jedoch möglich.

Der Eigentümer einer Base ist entweder ein **Benutzer** oder eine **Gruppe**. Ist ein Benutzer der Eigentümer einer Base, dann hat nur dieser die volle Verfügungsgewalt. Gehört die Base einer Gruppe, so haben alle Administratoren der Gruppe vollen Zugriff auf sie. Hier erfahren Sie mehr zu den [Berechtigungen einzelner Gruppenmitglieder]({{< relref "help/startseite/gruppen/gruppenmitglieder-und-ihre-berechtigungen" >}}).

Die direkte Übertragung der Eigentümerschaft von einem Nutzer auf einen anderen Nutzer ist aktuell (Stand: 20.3.2023) nicht möglich. Sie können einen **Eigentümerwechsel** aber indirekt durchführen, indem Sie eine Base exportieren und durch den neuen Eigentümer importieren lassen. Mehr Informationen zum Import und Export von Bases finden Sie im Beitrag [Datenimport und -export]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}).

## Erstellung von Bases

Sie legen **neue Bases** über die Startseite an. Auf dieser befinden Sie sich immer, wenn Sie sich in SeaTable einloggen. Wenn Sie gerade in einer Base arbeiten, kommen Sie mit einem Mausklick auf das **Base-Icon** {{< seatable-icon icon="dtable-icon-dtable-logo" >}} oben links zurück auf die Startseite.

Im Bereich **Meine Bases** und in jeder **Gruppe**, in der Sie Administrator sind, finden Sie die Schaltfläche **Eine Base oder Ordner hinzufügen**. Mit einem Klick auf diese Schaltfläche erstellen Sie eine neue Base dort, wo Sie wollen.

Bei der Erstellung einer neuen Base haben Sie **drei Optionen**. Mehr dazu erfahren Sie in den jeweiligen Artikeln:

- [Leere Base erstellen]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Base aus einer Datei importieren]({{< relref "help/startseite/import-von-daten/welche-import-formate-unterstuetzt-seatable" >}})
- [Base aus einer Vorlage erstellen]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}})

## Verwaltung von Bases

Sie verwalten Bases über das **Kontextmenü** auf der Startseite. Wenn Sie den Mauszeiger auf eine Ihrer Bases bewegen, dann erscheint rechts neben dem Namen ein **Stift-Icon** {{< seatable-icon icon="dtable-icon-rename" >}} und ein **Drei-Punkte-Icon** {{< seatable-icon icon="dtable-icon-more-vertical" >}} für die erweiterten Optionen. Diese werden Sie für die Verwaltung Ihrer Bases regelmäßig benötigen.

An Sie freigegebene Bases können Sie **nicht verwalten**. In den erweiterten Funktionen solcher Bases stehen Ihnen nur zwei Optionen zur Verfügung: **Freigegebene Base verlassen** und **Kopieren**.

## Bases umbenennen

Sie können Bases, deren Eigentümer oder Administrator Sie sind, nachträglich **umbenennen**. Bewegen Sie den Mauszeiger auf den Namen der umzubenennenden Base und klicken Sie dann auf das **Stift-Icon** {{< seatable-icon icon="dtable-icon-rename" >}}. Sie können den Namen nun ändern und per Klick auf die **Enter-Taste** speichern. Lesen Sie [hier]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}}) nach, was Sie bei der Namensgebung beachten sollten.

## Icon und Farbe einer Base ändern

Sie können den Bases, deren Eigentümer oder Administrator Sie sind, einen neuen Look verpassen. Wie das geht, erfahren Sie [hier]({{< relref "help/startseite/bases/aussehen-einer-base-anpassen-icon-und-farbe" >}}). Um frischen Wind in Ihre Bases zu bringen, stehen Ihnen **mehr als 10 Farben** und **mehr als 25 Icons** zur Verfügung.

## Base-Beschreibung hinzufügen

Sie können Ihren Bases eine Beschreibung hinzufügen, um anderen Benutzern eine „Gebrauchsanweisung“ zu geben oder ergänzende Informationen zu einer Base festzuhalten. Wie Sie diese Funktion nutzen, lernen Sie [hier]({{< relref "help/base-editor/weitere-optionen/wie-man-einer-base-eine-beschreibung-hinzufuegt" >}}).

## Bases freigeben

Sie können Bases, deren Eigentümer oder Administrator Sie sind, anderen **Benutzern und Gruppen freigeben** und diesen damit Zugriff auf die Daten gewähren. Freigaben erfolgen mit unterschiedlichen Berechtigungen, sodass Sie jederzeit die Kontrolle über Änderungen in Ihren Bases haben.

Mehr Informationen zu dieser wichtigen und äußerst hilfreichen Funktion finden Sie im Artikel [Base- und Ansichtsfreigaben im Überblick]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}).

## Base kopieren

Sie können alle Bases, auf die Sie Zugriff haben, **kopieren**. Je nachdem, woher die Base stammt und wohin Sie die Base kopieren wollen, hilft Ihnen entweder der Artikel [Duplizieren einer Base]({{< relref "help/startseite/bases/eine-base-in-eine-gruppe-kopieren" >}}) weiter.

## Bases in Ordner verschieben oder zu Favoriten hinzufügen

Wenn sich eine Vielzahl an Bases auf Ihrer Startseite angesammelt hat, kann es für die Übersichtlichkeit sinnvoll sein, [mehrere Bases in Ordnern zusammenzufassen]({{< relref "help/startseite/bases/eine-base-zu-den-favoriten-hinzufuegen" >}}).

## Base exportieren

Zur Datensicherung, für die Übertragung an einen anderen Benutzer oder den Transfer auf einen anderen SeaTable Server können Sie Bases exportieren. Grundsätzlich erfolgt der Export in eine [DTABLE-Datei]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}).

Mehr Informationen zum Export von Bases finden Sie im Beitrag [Speichern einer Base als DTABLE-Datei]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}})

## Bases löschen und wiederherstellen

Sie können Bases, deren Eigentümer oder Administrator Sie sind, bei Bedarf [löschen]({{< relref "help/startseite/papierkorb/loeschen-einer-base" >}}) und bis zu 30 Tage lang [wiederherstellen]({{< relref "help/startseite/papierkorb/eine-geloeschte-base-wiederherstellen" >}}). Befolgen Sie dazu die Anleitungen in den verlinkten Artikeln.

### Base aus Snapshot wiederherstellen

Sie können die Snapshots der Bases, deren Eigentümer oder Administrator Sie sind, anzeigen und wiederherstellen. Alles Wissenswerte zu Snapshots in SeaTable erfahren Sie in den Artikeln

- [Speichern der aktuellen Base als Snapshot]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}})
- [Wiederherstellung eines Snapshots]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}})

## E-Mail-Konto in einer Base einrichten

Wenn Sie E-Mails aus einer Base versenden möchten, müssen Sie Ihr E-Mail-Konto mit der Base verbinden. Wie Sie von dieser nützlichen Funktion in SeaTable Gebrauch machen, zeigen wir Ihnen im Artikel [Einrichtung eines E-Mail-Kontos in einer Base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).
