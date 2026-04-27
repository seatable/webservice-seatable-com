---
title: 'SeaTable 2.5: Optimiertes Archiv, Datenverarbeitung und Automationen - SeaTable'
description: 'Das Archiv wächst: jetzt alle Spaltentypen inkl. Formeln & Links. Daten­verarbeitung flexibler, Python-Skripte per Automation, Bewertungs­funktion mit vier Icons und automatischer Summary. Excel-Import, Galerie-Optionen, neue Zählfunktionen, mobile Verbesserungen und Integration von vier Automations­plattformen – so wird SeaTable vielseitiger!'
date: 2021-11-16
lastmod: '2023-07-11'
author: 'rdb'
url: '/de/seatable-release-2-5'
color: '#e7cae0'
categories:
    - 'product-features'
seo: 
    title: 'SeaTable 2.5: Archiv, Daten­prozesse & Automation'
    description: 'Archivfunktion unterstützt jetzt Berechnungen, Links & Formeln, bessere Datenverarbeitung, neue Automationsoptionen und vielseitige Bewertungs­spalte: 2.5 ist da!'
---

SeaTable 2.5 ist da! Das neue Docker Image wurde bereits Ende letzter Woche auf Docker Hub bereitgestellt und heute Morgen wurde dann SeaTable Cloud auf die neuste Version gehoben. Das neue Release macht zahlreiche Funktionen von SeaTable noch besser! Die Archivfunktion mit ihrem wachsenden Funktionsumfang empfiehlt sich für eine wachsende Anzahl an Anwendungsfällen, die verfügbaren Datenverarbeitungsfunktionen werden flexibler und die integrierten Automationen sowie die Rating Spalte bieten neue Optionen. Auch eine Erwähnung wert: Spalten vom Typ Verknüpfung und Formel für Verknüpfungen werden nun vollständig in externen Ansichten unterstützt. Lesen Sie weiter, um mehr über diese Neuerungen zu erfahren. Die vollständige Liste der Änderungen finden Sie – wie immer – im [SeaTable Changelog]({{< relref "pages/changelog" >}}).

## Überarbeitete Archivfunktion

Seit Einführung des Archivs als Beta-Funktion in der [Version 2.3]({{< relref "posts/seatable-releases/seatable-release-2-3" >}}) haben unsere Entwickler pausenlos daran gearbeitet, die Archivfunktion für den Produktiveinsatz bereit zu machen. Mit der Version 2.5 haben wir dieses Ziel noch nicht ganz erreicht, die neue Version stellt aber einen riesigen Schritt in diese Richtung dar.

Die Archivfunktion unterstützt nun alle 24 Spalten, inklusive der drei Spaltentypen Formel, Verknüpfung und Formel für Verknüpfung. Der fehlende Schreibzugriff auf die Archivdaten bleibt auch in SeaTable 2.5 eine Einschränkung, diese drei Spalte sind aber Sonderfälle: Werte in den beiden Formel-Spalten werden dynamisch berechnet, je nach Spezifikation der Formel. Wenn eine Formel geändert wird, dann werden die Werte in den archivierten Zeilen neu berechnet. Ändert der Benutzer die Nachschlagespalte in einer Formel für Verknüpfungen, die Archivdaten reflektieren diese Änderung. Das Gleiche gilt für die Verknüpfungsspalte. Eine Umstellung der Anzeigespalte erfolgt gleichermaßen im gesamten Datenbestand, Archiv inklusive. Auf diese Weise bleiben die archivierte Daten vergleichbar mit den nicht-archivierten Daten.

![Die überarbeitete Archiv-Ansicht von SeaTable](archive-view.jpg)

SeaTable 2.5 ergänzt darüber hinaus eine Druckfunktion für Archivansichten und erlaubt nun auch das Ausblenden einzelner Spalten in einer solchen Ansicht. Eine Suchfunktion und eine Excel Exportfunktion wurden schon in [SeaTable 2.4]({{< relref "posts/seatable-releases/seatable-release-2-4" >}}) implementiert.

## Optimierte Datenverarbeitungsoperationen

SeaTables Datenverarbeitungsoperationen werden häufig für die Migration von Excel Anwendungen zu SeaTable benötigt. In SeaTable 2.5 wurden zwei Operationen verbessert.

Die Vergleichen und verknüpfen Operation erstellt automatisiert Verknüpfungen zwischen ähnlichen Zeilen in zwei Tabellen. Mit ihr ist die Umwandlung von Excel Tabellen in eine relationale Datenbank im Handumdrehen erledigt. Nun neu in SeaTable 2.5 ist die Unterstützung aller wichtigen Spaltentypen (inkl. Einfachauswahlspalten) für die Definition der Vergleichsregel. Außerdem bietet die Operation nun auch mehr Flexibilität für den Fall, dass die Tabellen bereits doppelt verknüpft sind. In diesem Fall wird der Benutzer aufgefordert, die Spalten, in der die Verknüpfungen ergänzt werden sollen, über ein Dropdown-Menü auszuwählen.

Die Kumulierte Werte berechnen Operation berechnet zeilenübergreifende Summen für Spalten mit numerischen Daten – eine Standardfunktion in Excel. Die Operation steht bereits seit der Einführung der Datenverarbeitungsfunktion in [SeaTable 2.1]({{< relref "posts/seatable-releases/seatable-release-2-1" >}}) zur Verfügung, wurde nun aber auf Basis von Benutzerfeedback angepasst. Konkret wurde das Handling der allerersten Spalte kritisiert. Nun nach der Überarbeitung summiert die Operation ausschließlich über die Quellspalte und schreibt die Ergebnisse in die Ergebnisspalte.

## Neue Automationen und Trigger

> **SeaTable unterstützt nun vier Plattformen zur Prozessautomation:**  
> Automationen waren ein Schwerpunktthema in den vergangenen Wochen und Monaten. Wir sind stolz darauf, dass SeaTable nun auf vier Integrationsplattformen verfügbar ist: Neben [Zapier](https://zapier.com/apps/seatable/integrations), auf dem SeaTable schon bereits seit Anfang 2021 vertreten ist, lassen sich nun auch mit [Integromat](https://www.make.com/en/integrations/seatable), [n8n](https://n8n.io/integrations/seatable/) und [Locoia](https://www.locoia.com/connector-integrations/) anspruchsvolle Workflows bauen.

Bei aller Aufmerksamkeit auf externe [Integrationen]({{< relref "pages/integrations" >}}) haben wir SeaTables eigene Automationen nicht aus den Augen verloren. Die zentrale Neuerung ist die Aktion Python Skript ausführen. Sie lässt sich durch die Trigger “Neue Zeile”, “Einträge erfüllen nach der Änderung eine bestimmte Bedingung” und “Periodisch ausführen” auslösen. Die automatisierte Ausführung von Python Skripten für eine einzelne Zeile oder ein ganzes Datenset unter Verwendung eines klaren Regelsets ist fast schon eine Superkraft!

![Python Scripte können nun per Automation gestartet werden.](python-script-durch-automation-511x448.jpg)

Die bestehende Aktion “Zeile sperren” erhält das neue Trigger-Ereignis “Periodisch ausführen für Zeilen, die eine bestimmte Bedingung erfüllen”. In Kombination mit den beiden anderen Triggern “Neue Zeile” und “Einträge erfüllen nach der Änderung bestimmte Bedingungen” hat der Benutzer nun optimale Kontrolle über die automatische Sperrung von Zeilen.

Schließlich haben die beiden geplanten Ereignisse “Periodisch ausführen” und “Periodisch ausführen für Zeilen, die eine bestimmte Bedingung erfüllen” eine manuelle Ausführungsoption erhalten. So lassen sich Automationen mit diesen Triggern komfortabel testen.

## Mehr Optionen für die Rating Spalte

Wir alle lieben eine große Auswahl! Die neue Rating Spalte erfüllt genau diese Sehnsucht nach “mehr”. In SeaTable bietet die Rating Spalte nun vier Stile. Neben dem Stern als Standardicon kann man nun auch das Herz, den Daumen-hoch oder die Flagge als Icon wählen. Auch muss das Icon nicht mehr orange sein.

![Die neue Bewertungsspalte in SeaTable 2.5](Bewertungsspalte.jpg)

Bei der überarbeiteten Rating Spalte geht es aber nicht nur um Ästhetik, sondern auch um Bequemlichkeit. So wie für andere numerische Spalten berechnet SeaTable nun auch für Rating Spalten am unteren Ende der Tabelle aggregierte Werte – Minimum, Maximum, Durchschnitt und Summe. In gruppierten Ansichten ermittelt SeaTable ebenfalls aggregierte Werte für die einzelnen Gruppen.

Schließlich wurde die Rating Spalte für die Nutzung auf mobilen Geräten optimiert. Sie lassen sich mit der neusten Version problemlos auf einem Mobiltelefon anlegen. In der Vergangenheit hat sich SeaTable bei diesem Vorgang verweigert. Darüber hinaus wurden die Icons der Rating Spalte etwas vergrößert, was deren Nutzung auf kleinen Bildschirmen komfortabler macht.

Eine weitere Entwicklung für die Rating Spalte hat es leider nicht mehr in die Version 2.5 geschafft. Daher hier die Ankündigung: Ab SeaTable 2.6 werden Rating Spalten auch einen Standardwert haben können.

## Weitere Verbesserungen

Die neue Funktion countitems zählt die Elemente in Spaltentypen, die mehrere Werte enthalten können. Dazu gehören die Spaltentypen Datei, Bild, Mitarbeiter und Mehrfachauswahl. Sie ist das Gegenstück zur Funktion “countlinks” für nicht-verknüpfte Elemente.

Die Excel Export- und Importfunktion wurde an mehreren Stellen überarbeitet. Der Export von Formelspalten funktioniert mit SeaTable 2.5 nun problemlos, auch wenn in der Formel verwendete Spalten versteck sind. Eine Neuigkeit ist auch, dass neue Daten gleichermaßen aus CSV- wie aus XLSX-Dateien importiert werden können und dass sich neue Tabellen aus XLSX-Dateien erzeugen lassen. Benutzer, die Daten von SeaTable zu Excel übertragen, werden sich freuen zu hören, dass die Exportroutine nun auch Mehrfachauswahlfelder korrekt handhabt.

Die Einstellungen des Galerie Plugins wurden um eine Einstellungsoption erweitert. Über den Schalter “Spaltennamen anzeigen” lassen sich die Überschriften über den Spaltenwerten ein- und ausblenden. Auch wenn dies in vielen Fällen nicht notwendig ist, so verhindert sich Verwirrung in Fällen, in denen Spalten vom selben Typ unmittelbar untereinander stehen.
