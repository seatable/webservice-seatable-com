---
title: 'SeaTable 3.0: Datenvalidierung, Office-Webeditoren und neues Speicherbackend - SeaTable'
description: 'SeaTable 3.0 bringt automatische Datenvalidierung mit regulären Ausdrücken in Textfeldern, Office-Dokumentbearbeitung direkt im Browser, ein effizienteres Speicher-Backend sowie neue Funktionen für geteilte Datensätze und Teammanagement. Viele Detaillösungen sorgen für mehr Zusammenarbeit und Datensicherheit.'
date: 2022-06-21
lastmod: '2022-06-27'
author: 'rdb'
url: '/de/seatable-release-3-0'
color: '#cfe107'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 3.0: Datenvalidierung & Office Online'
    description: 'Datenvalidierung, Office-Dokumente online bearbeiten, neues Storage-Backend, verbesserte Teamverwaltung – vielseitige Neuerungen in 3.0!'
---

SeaTable 3.0 ist da! Das dritte Major Release von SeaTable bietet die Online-Bearbeitung von Office Dokumenten, eine automatische Datenvalidierung, mehr Funktionen für gemeinsame Datensätzen und eine neue Serverkomponente für die effizientere Speicherung von Bases. Über die vielen weiteren Detailverbesserungen und Bugfixes in der neuen Version gibt – wie immer – das [Changelog]({{< relref "pages/changelog" >}}) Auskunft. [SeaTable Cloud Benutzern](https://cloud.seatable.io/) stehen die neuen Funktionen ab sofort zur Verfügung. Das Image für SeaTable 3.0 wurde heute Nacht auf [Docker Hub](https://hub.docker.com/r/seatable/seatable-enterprise/tags) bereitgestellt.  
Neben den funktionalen Verbesserungen in der SeaTable App gibt es SeaTable Cloud Benutzer eine weitere Neuigkeit: Eine neue Teamverwaltung mit erweiterten Funktionen und verbessertem Design macht die Verwaltung von kleinen und insbesondere größeren Teams deutlich einfacher. Mehr zur neuen Teamverwaltung finden Sie im Artikel [Die neue Teamverwaltung]({{< relref "help/teamverwaltung/abonnement/die-funktionen-der-teamverwaltung-in-der-uebersicht" >}}).

## Automatische Datenvalidierung

In Textspalten lassen sich Strings jeder Art und Länge erfassen und bieten damit große Flexibilität. Einfach- und Mehrfachauswahlspalten eigenen sich durch die vordefinierten Werte ideal für die Strukturierung von Daten. Die neue Datenvalidierungsfunktion ermöglicht die Kombination der Vorteile von Textspalten mit denen von Auswahlspalten.

Bei aktivierter Datenvalidierung prüft SeaTable, ob der eingegebene Zellwert dem definierten Zielformat entspricht. Entspricht die Eingabe nicht dem Zielformat, so wird die Zelle rot hervorgehoben. In Webformularen führt eine nicht-konforme Eingabe zu einer Fehlermeldung und das Formular kann nicht eingereicht werden.

![Data validation in SeaTable 3.0](FormatCheck.png)

Das Zielformat wird in Form eines [regulären Ausdrucks](https://de.wikipedia.org/wiki/Regul%C3%A4rer_Ausdruck) definiert. Ein regulärer Ausdruck für eine Zahlenfolge mit genau 5 Stellen ist beispielsweise \[0-9\]{5}. Für reguläre Ausdrücke sprechen zwei Argumente: Sie sind eine weit verbreitete Methode und bieten ein Maximum an Flexibilität. Die Art der erlaubten Zeichen, die Länge, und auch die Syntax der Eingabe lässt sich mit regulären Ausdrücken präzise definieren.

Die Datenvalidierung steht in der Version 3.0 in Textspalten zur Verfügung. Wird ein Zielformat im Nachhinein hinzugefügt, dann werden alle bestehenden Einträge ebenfalls überprüft und die nicht-konformen Werte als solche markiert. Einer nachträglichen Aktivierung der Datenvalidierung in bestehenden Spalten steht also nichts im Weg.

## Online-Bearbeitung von Office Dokumenten

SeaTable macht die Zusammenarbeit im Team interaktiv. Eine Base ist mit wenigen Klicks geteilt und Eingaben in einer geteilten Base werden unmittelbar anderen Benutzern angezeigt. Anders bei Office Dateien in einer SeaTable Base. Um das Word Dokument, die Excel Tabelle oder die PowerPoint Präsentation zu bearbeiten, muss diese zuerst heruntergeladen werden. Die Bearbeitung erfolgt dann offline. Anderen Benutzern steht die geänderte Dokumentenversion erst nach dem manuellen Upload zur Verfügung steht. Dies war uns ein Dorn im Auge.

SeaTable 3.0 erweitert die Echtzeit-Kollaboration, wie man sie aus dem Tabelleneditor kennt, auf Office Dokumente. Dokumente lassen sich direkt im Browser und mit mehreren Personen gleichzeitig bearbeiten. Die Änderungen der Co-Autoren werden in Echtzeit angezeigt, so dass Sie genau wissen, wer und wo an dem Dokument arbeitet. Auch ein manueller Upload ist nicht mehr nötig. Wenn der letzte Benutzer das Dokument verlässt, dann wird der aktuelle Dokumentenstand automatisch an SeaTable zurück übergeben und in der Datei-Spalte als neue Dokumentenversion abgelegt.

Die Bearbeitung eines Office Dokuments aus SeaTable heraus könnte nicht einfacher sein: Ein Klick auf die Word, Excel bzw. PowerPoint Datei öffnet das Dokument in einem Editor in einem neuen Tab. Benutzer, die das Dokument aktuell bearbeiten, werden in der rechten oberen Ecke angezeigt. Änderungen dieser Benutzer werden direkt im angezeigten Dokument ausgeführt und durch ein Fähnchen deutlich gemacht. Die Speicherung erfolgt automatisch.

Die für die Online-Bearbeitung verwendeten Editoren stammen von [ONLYOFFICE](https://onlyoffice.com). Die Editoren des ONLYOFFICE Dokumentenservers zeichnen sich durch ein modernes Benutzerinterface und eine sehr gute Kompatibilität mit den Microsoft Dateiformaten aus. Außerdem kann der Dokumentenserver, wie auch SeaTable, selbst-gehostet werden.

Die Online-Bearbeitung ist in allen SeaTable Cloud Abonnements verfügbar, inklusive des kostenlosen Free Abonnements. Bei einem on-premises Betrieb von SeaTable muss der ONLYOFFICE Dokumentenserver installiert und konfiguriert werden. Die Einrichtungsanleitung finden Sie im [SeaTable Manual](https://manual.seatable.io/).

## Verbesserte Synchronisation von Bases

Mit der Funktion Gemeinsame Datensätze lassen sich die Daten aus einer Base in eine oder mehrere andere Bases synchronisieren. Sie sind besonders hilfreich, wenn Sie anderen Benutzern Daten für die Weiterverarbeitung und Anreicherung zur Verfügung stellen wollen, Sie diesen Benutzern aber keine Zugriffsrechte auf die von Ihnen verwalteten Liste (“Masterliste”) geben können. Die Version 3.0 enthält mehrere Verbesserungen, um die Erstellung, Synchronisation und Duplikation von gemeinsamen Datensätzen zu vereinfachen.

![Existing common datasets are displayed in the "New common dataset" dialog](ExistingCDS.png)

Ab SeaTable 3.0 werden im Dialog “Neuer gemeinsamer Datensatz” bereits erstellte gemeinsame Datensätze angezeigt. So wird die mehrfache Erstellung von gemeinsamen Datensätzen vermieden.

In der neuen Version werden Spalten, die durch den Import eines gemeinsamen Datensatz erstellt wurden, mit einem Sync-Icon markiert. So lassen sich die Spalten, die bei einem Re-Sync mit dem gemeinsamen Datensatz überschrieben werden, leicht von allen anderen Spalten unterscheiden. Die visuelle Markierung vermindert die Gefahr ungewollten Datenverlusts.

![Columns imported from CDS marked with sync icon](ColumnIconsCDS.png)

Bei der Duplikation einer Tabelle mit einem importierten gemeinsamen Datensatz wurden bisher nur die Daten dupliziert. Die Verknüpfung mit dem gemeinsamen Datensatz war in der duplizierten Tabelle nicht gegeben, so dass auch kein erneuter Sync möglich war. Die Duplikationsfunktion wurde nun so erweitert, dass Sie über einen Schalter die Verbindung zum gemeinsamen Datensatz entweder in die neu zu erstellende Tabelle übernehmen oder verwerfen.

## Höhere Speichereffizienz

Die neue SeaTable Server Komponente dtable-storage-server wird den Speicherbedarf für die Speicherung von Bases, Snapshots und Backups archivierter Zeilen deutlich reduziert. Die Komponente seaf-server, die dafür bisher zuständig war, wird auch weiterhin eine wichtige, aber reduzierte Rolle spielen

Technisch betrachtet ist der dtable-storage-server eine einfache Abstraktionsschicht für unterschiedliche Speicherbackends. Wie bisher werden lokaler Speicher und S3-Objektspeicher unterstützt. Damit bietet SeaTable attraktive Speicheroptionen für kleine, einfache Systeme wie für hochskalierbare Setups.

Bei neu installierten SeaTable Servern erfolgt die Speicherung von Bases automatisch im dtable-storage-server. Nur die Speicherung von Bildern und Datei übernimmt weiterhin der seaf-server. Anders verhält es sich bei bestehenden Systemen. Im Rahmen eines Upgrades eines SeaTable Servers 2.x wird der dtable-storage-server nicht automatisch installiert und konfiguriert. Dies muss manuell erfolgen; das Vorgehen ist im [SeaTable Manual](https://admin.seatable.com/upgrade/extra-upgrade-notice/#30) beschrieben. Eine Migration der bestehenden Bases in den dtable-storage-server wird empfohlen. Bei wenigen Bases ist der Export in eine DTABLE-Datei und der Reimport in eine neue Base das einfachste Vorgehen. Bei größere Base-Anzahl lässt sich dieser Prozess auch über die API automatisieren. Erfoderlich ist eine Migration aber nicht. SeaTable 3.0 kann Bases auch weiterhin aus dem seaf-server laden.

## Weitere Verbesserungen

Darüber hinaus gibt es zahlreiche weitere Verbesserungen, von denen wir hier die drei wichtigsten in aller Kürze vorstellen.

Die Menüstruktur im Kopf der Base wurde erweitert und überarbeitet. Die offensichtlichste Änderung ist der Avatar, der nun analog zur Homepage oben rechts angezeigt wird. Um für den Avatar Platz zu machen, ist die Drei-Punkte-Schaltfläche eine Zeile nach unten gewandert. Das Menü, dass sich hinter dieser Schaltfläche befindet, wurde überarbeitet. Ihrer Wichtigkeit entsprechend wurden beispielsweise die Benachrichtigungs- und Automationsregeln aus diesem Menü heraus gelöst. Sie verfügen nun über Ihr eigenes Icon in der oberen rechten Ecke.

[DTABLE-Dateien]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}), Exportdateien von Bases, enthalten nun auch Automationsregeln. Das gleiche gilt für die Kopie einer Base in eine andere Gruppe. Dies erspart unnötige manuelle Nacharbeit bei der Übertragung von Bases zwischen Gruppen und SeaTable Servern.

Im Kanban Plugin lässt sich nun die Titelspalte auswählen. Der Wert der Titelspalten steht, unabhängig von der Sequenz der Spalten in der Tabelle, ganz oben auf der Kanban Karte.
