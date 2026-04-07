---
title: 'SeaTable 1.4: Neue Optionen für die Datenverwaltung und die Online Collaboration - SeaTable'
description: 'Datenmanagement wird flexibler: Mit SeaTable 1.4 gibt’s jetzt echte URL-Spalten, neue Wizards für Verknüpfungen, Queries über mehrere Tabellen hinweg, Teamchat in Echtzeit, Webhooks für externe Tools und Python für Scripts. Dazu viele Designverbesserungen und mehr Übersicht samt neuem Navigationskonzept und Activity-Feed.'
date: 2020-10-29
lastmod: '2023-07-11'
author: 'rdb'
url: '/de/seatable-release-1-4'
color: '#396afc'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 1.4: URL-Spalte, Linking, Realtime-Chat'
    description: 'URL-Spalte, vereinfachtes Linking, Abfragen über verknüpfte Felder, Team-Chat, Webhooks, Python-Skripte – das steckt im Major-Update 1.4!'
---

Wir freuen uns, die Veröffentlichung von SeaTable 1.4 bekannt zu geben! Wir haben einen neuen Spaltentyp, verbesserte Datenbankfunktionen, einen Realtime Chat und viele weitere Verbesserungen in dieses neue Release gepackt. Die Organisation von Daten und die Zusammenarbeit im Team war nie so einfach und bequem! Und das beste ist: Jeder Nutzer profitiert von den neuen Features, inklusive des Free Abos.

Eine vollständige Liste der Änderungen finden Sie im [SeaTable Changelog]({{< relref "pages/changelog" >}}). Diese Release Note stellt die wichtigsten und aufregendsten Änderungen von SeaTable 1.4 dar. Auf geht’s!

## Willkommen im Team Spaltentyp #18

SeaTable 1.4 erhält einen weiteren Spaltentyp: Die [URL-Spalte]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}#url). Diese verhält sich wie eine Text-Spalte, der Zelleninhalt wird aber als Verweis auf eine Netzwerkressource interpretiert. Internet- und IP-Adressen wie https://seatable.com, [www.seafile.com](https://www.seafile.com/en/home/), 192.168.178.1 und localhost:8000 sind in der URL-Spalte gut aufgehoben.

Die Adresse einer Netzwerkressource lässt sich aus einer URL-Spalte mit zwei Klicks aufrufen. Beim ersten Klick erscheint am rechten Zellenrand ein Link-Icon. Mit einem zweiten Klick auf dieses Icon wird die Adresse in einem neuen Browser Tab aufgerufen; http(s) wird automatisch als Präfix ergänzt. Wenn Sie sich nun fragen, warum zwei Klicks notwendig sind, hier der Grund: Zwei Klicks schützen vor irrtümlichen Webseitenaufrufen beim Navigieren in der Tabelle, was gerade auf Mobilgeräten leicht passieren kann.

## Leistungsfähigere und einfachere Datenbankfunktionen

Der neue Assistent für die Verknüpfungsspalte und die erweiterten Abfragemöglichkeiten werden insbesondere aber nicht nur Datenbankfans begeistern! SeaTable macht Datenbanken so einfach, wie sie sein sollten!

### Verknüpfungen ganz einfach

Das Verknüpfen von Einträgen war in der Version 1.3 noch etwas mühsam. Ein Dropdown-Menü listete die Einträge der ersten Spalten in der verlinkten Tabelle auf. Kompakt, aber unpraktisch, wenn die verlinkte Tabelle zwei oder mehr Zeilen mit den gleichen Werten in Spalte 1 aufwies. Dieses Problem ist in SeaTable 1.4 gelöst!

Das Dropdown hat Platz gemacht für einen neuen, detailreichen und kontextsensiblen Assistenten. Ein Doppelklick auf eine Zelle öffnet ihn. Bei einer leeren Zelle zeigt der Assistent die ersten Spalten der verlinkten Tabelle an. Verwirrung darüber, welcher Eintrag in der Zieltabelle nun den richtige ist, ist damit ein Ding der Vergangenheit. Bei einem Doppelklick auf eine Zelle mit bereits verlinkten Einträgen zeigt der Assistent die Details der verlinkten Einträge an. Weitere Einträge können über die Schaltfläche “Neuen Link hinzufügen” in der oberen rechten Ecke verknüpft werden.

![New wizard for link to other records columns](linking-dialog.png)

Der neue Assistent vereinfacht die Verknüpfung von Tabellen, das ist aber nicht das Einzige, was er kann. Direkt aus dem Assistenten heraus lassen sich auch neue Einträge in der verknüpften Tabelle erstellen. Ganz ohne Wechsel der Tabellen, ohne Klickorgien und Zeitverlust. Mit dem neuen Assistenten arbeiten Sie gleichzeitig in zwei unterschiedlichen Tabellen.

### Volle Datenbankpower

Datenbankabfragen quer über mehrere Tabellen haben etwas magischen an sich. In früheren Versionen von SeaTable waren Abfragen nur über direkt miteinander verlinkte Tabellen möglich. Diese Einschränkung wurde in SeaTable 1.4 aufgehoben! Solange Einträge per Verknüpfungen verbunden sind, kann SeaTable diese verfolgen und den Zielwerte ausgeben – unabhängig von der Zahl der Verknüpfungen, denen SeaTable dafür folgen muss. Die intuitive Implementierung dieser Funktion in SeaTable stellt sicher, dass nicht nur Datenbankexperten in den Genuss dieses Hauchs von Magie kommen.

Stellen Sie sich vor, Sie verwalten Ihre IT-Assets mit SeaTable. In Tabelle 1 verwalten Sie die Benutzer, Tabelle 2 enthält die Räume und Tabelle 3 listet die Hardware auf. Jeder Benutzer ist per 1:1-Verknüpfung mit einem Zimmer und einer 1:n-Beziehung mit den IT-Assets verbunden. Der Benutzer stellt somit das Bindeglied zwischen Raum und Asset dar. Mit SeaTable 1.4 ist die Erstellung einer Liste der IT-Assets pro Raum eine Sache von wenigen Klicks.

## Chatten mit Kollegen in Echtzeit

Effiziente Online Zusammenarbeit geht nicht ohne gute Kommunikation im Team. Die Version 1.4 führt nun die Lösung ein, mit der Sie mit Ihren Teammitgliedern im engen Kontakt bleiben! Ideen besprechen, neue Datensätze kommentieren und Änderungen diskutieren, all das ist ganz einfach möglich und geschieht dort, wo es passieren soll: direkt in den Daten.

![Real-time chat in comments](comment-chat.png)

Wenn Sie die Kommentarfunktion noch nicht kennen, dann wählen Sie eine Zeile aus und drücken Sie die Leertaste, um die Zeilendetails aufzurufen. In der oberen rechten Ecken finden Sie die Kommentarspalte. SeaTables verbessertes Backend informiert die Benutzer ohne Zeitverzug über neue Kommentare. Sind die Benutzer online, dann kann der Gruppenchat losgehen. Ansonsten werden die Benutzer per [Benachrichtigung]({{< relref "help/startseite/benachrichtigungen" >}}) informiert. Tauschen Sie Ihre Ideen und Eindrücke mit den Kollegen, wenn sie frisch sind.

## Webhooks für bessere Automatisierung

Was ist besser als SeaTable? SeaTable im Zusammenspiel mit Ihren anderen Lieblingsanwendungen! Aus diesem Grund haben wir uns bemüht, mit [Zapier](https://zapier.com/apps/seatable/integrations) schnellstmöglich eine komfortable Integrationsmöglichkeit anzubieten.

Aber Zapier war nur der erste Schritt. Webhooks, die mit dieser Version eingeführt werden, sind der zweite. Mit SeaTables Webhooks wird es ganz einfach, ereignisbasiert Aktionen in externen Anwendungen auszulösen. Hier zwei einfache Beispiele: Ein Zähler wird um eins erhöht, wenn ein neuer Eintrag angelegt wird oder eine E-Mail wird versendet, wenn ein Wert eine kritische Schwelle überschreitet.

## SeaTable Skripte nun auch in Python

![Python support in SeaTable scripts](python.png)

Nicht zuletzt bietet SeaTable 1.4 auch eine Neuerung für Entwickler. Diesmal sind es gute Nachrichten für Python Liebhaber.

SeaTable 1.3 führte SeaTables Skripting Engine ein. JavaScript war die unterstützte Skriptsprache. Mit SeaTable 1.4 lassen sich nun auch Skripte in Python entwickeln und ausführen. Importieren Sie Ihr Python Skript oder entwickeln Sie es direkt in SeaTables Skript Editor und automatisieren Sie so die Datenverarbeitung und bauen Sie Ihre Individualanwendung. Mehr Informationen über SeaTables Skripte finden Sie im [SeaTable Scripts Programming Manual](https://developer.seatable.com/scripts/) (nur auf Englisch verfügbar).

Spoiler: In einer der nächsten Versionen werden wir die Möglichkeit ergänzen, Skripte zeitgesteuert auszuführen.

## Viele weitere Verbesserungen

Nicht SeaTables gesamtes Entwicklerteam von rund 30 Leuten arbeitet an diesen großen Entwicklungen. Viel Arbeit und Leidenschaft fließt auch in die zahllosen kleinen, inkrementellen Verbesserungen von SeaTable, die wir mit jeder Version vornehmen und SeaTable so Stück für Stück besser machen. An dieser Stelle nur die wichtigsten Verbesserungen unter diesen Kleinen.

Wir haben die Navigation auf der linken Seite in der Basebibliothek neu organisiert. Die neue Navigation enthält zwei Kategorien: Der Workspace enthält die Bases, Webformulare und Aktivitätenübersicht. Hilfe und Ressourcen bietet Direktlinks zu unserer wachsenden Templatesammlung sowie zum Benutzerhandbuch.

Zum Thema Aktivitätenübersicht: Dieses Menü selbst ist mit seinem neuen Design kaum wiederzuerkennen. In der Vergangenheit wurden hier alle Aktivitäten ohne weitere Struktur in chronologischer Reihenfolge aufgelistet. Bei steigender Benutzungsintensität wurde das schnell unübersichtlich. Die neue Aktivitätenübersicht behält die chronologische Grundstruktur bei, gruppiert die Aktivitäten aber Base bei Base und schafft so viel mehr Übersicht. Ein Klick auf eine Base öffnet die Details der Änderungen am gewählten Tag.

Kleine, aber feine Verbesserungen hat auch die Tabellenansicht erfahren. Wenn Sie nun eine Base zum ersten Mal öffnen, dann wird automatisch die Beschreibung der Base aufgerufen. Dies ist sehr nützlich, wenn Sie Bases mit anderen teilen. So werden Ihre Kollegen mit den Informationen versorgt, die Sie sie sehen lassen wollen, bevor sie sich auf die Daten stürzen.

Sie sind interessiert oder sogar inspiriert? Dann worauf warten? Die Anmeldung ist im Nu gemacht und SeaTable ist dauerhaft kostenlos! Bei Fragen oder Zweifeln, Ideen oder Feedback schreiben Sie uns bitte oder hinterlassen Sie ein Kommentar im [Forum](https://forum.seatable.com).
