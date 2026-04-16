---
title: 'SeaTable 2.7: Bedingte Zellformatierung, flexible Spaltenfixierung und praktischer Datumsstandardwert - SeaTable'
description: 'Mit Version 2.7 gibt’s mehr Übersicht im Tabelleneditor: Markierungen für Werte per Regel oder Farbverlauf, Rankings automatisch berechnen, mehrere Spalten fixieren. Neu: Standardwert für Datumsspalten und Passwortschutz für Bases. Verbesserte Suche, 2FA-Option und Links werden beim Wiederherstellen neu gesetzt.'
date: 2022-02-02
lastmod: '2022-02-03'
author: 'rdb'
url: '/de/seatable-release-2-7'
color: '#c29eca'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 2.7: Zellformatierung & Spaltenfixierung'
    description: 'Bedingte Zellformatierung, Spalten einfrieren, Standardwerte für Datumsfelder – SeaTable 2.7 bringt neue Power ins Tabellen- und Zugriffsmanagement!'
---

Heute Morgen wurde [SeaTable Cloud](https://cloud.seatable.io) auf die Version 2.7 aktualisiert. Damit kommen nun auch alle Cloud-Benutzer in den Genuss der neuen Funktionen und Verbesserungen der neuen Version, die bereits seit einigen Tagen für Selbsthoster auf Docker Hub zum Download bereitsteht. Der Tabelleneditor profitierte am meisten von dem Versionswechsel: Die bedingte Zellformatierung, die neue Datenverarbeitungsoperation „Rangliste berechnen“, die erweiterte Spaltenfixierung und die Standardwertfunktion für Datumsspalten bieten eine Menge neuer Funktionalität. Außerhalb des Tabelleneditors sind die passwortgeschützten Bases eine wichtige Verbesserung. Sämtliche Änderungen gibt es – wie immer – im [SeaTable Changelog]({{< relref "pages/changelog" >}}).

## Bedingte Formatierung für Spalten

Wer regelmäßig mit [Excel]({{< relref "pages/landing-pages/alternatives/excel-alternative" >}}) arbeitet, kennt die Funktion bedingte Formatierung. Diese hält mit der Version 2.7 nun auch in SeaTable Einzug. Mit der bedingten Formatierung formatieren bzw. kolorieren Sie Zellen in Abhängigkeit ihres Werts (bzw. der Abwesenheit eines solchen) und können so eine optische Datenstrukturierung und Datenanalyse vornehmen.

Für alle Spalten bietet SeaTable eine regelbasierte, bedingte Formatierung an. Eine Regel ist die Beschreibung eines hypothetischen Inhalts einer Zelle (z.B. Wert > 50 oder Datum nach dem 31.12.2021) sowie eine Formatierungsanweisung. Ist die Regel erfüllt, dann wird die Zelle entsprechend der Anweisung formatiert. Mit geschickt gewählten Regeln lassen sich unter anderem statistische Ausreißer oder ungewöhnliche Werte leicht erkennbar machen. Natürlich können Sie auch mehrere Regeln pro Spalte definieren, um anspruchsvolle Anforderungen abzubilden.

![Bedingte Zellformatierung mit Farbverlauf und Regeln für Werte in einer Spalte](Conditional_cell_formatting2.png)

Hat eine Spalte numerische Zellwerte, dann bietet SeaTable zusätzlich zur regelbasierten Formatierung eine Formatierung nach Werten. Diese bedingte Formatierung färbt die Zellen mit einem Farbverlauf ein. Große Werte werden mit dem oberen Ende des Farbverlaufs eingefärbt, kleine Werte mit dem unteren Ende. So wird auf einen Blick die Größenordnung eines Zellwerts deutlich.

## Reihenfolge von Werten

Wenn Sie nicht nur die Größenordnung der Zellwerte einer Spalte anzeigen lassen wollen, sondern auch das Ranking der Werte benötigen, dann ist die neue Datenverarbeitungsoperation Rangliste berechnen genau das richtige für Sie! Sie berechnet die Rangliste und schreibt das Ergebnis in eine separate Spalte. Der größte Wert erhält das Ranking 1. Wenn zwei oder mehrere Zellwerte den gleichen Betrag haben, dann erhalten alle Zellen das gleiche Ranking und ein bzw. mehrere nachfolgende Ranking-Positionen werden übersprungen. Die Operation funktioniert für Spalten mit numerischen Inhalten, aber auch für die Spaltentypen Datum, Dauer und Rating.

## Fixierung von Spalten

In Tabellen mit vielen Spalten tritt häufiger das Problem auf, dass die ersten Spalten beim Scrollen nach rechts aus der Anzeige verschwinden. Bisher konnte man die erste Spalte fixieren und damit auch bei großen Tabellen dauerhaft anzeigen lassen. Diese Funktion zeigt sich im neuen Release von einer flexibleren Seite: Beginnend mit der Version 2.7 lassen sich weitere Spalten links fixieren. So weiß man auch beim Navigieren in großen Tabellen, in welchem Eintrag man sich befindet.

![Tabellenansicht mit mehreren links fixierten Spalten und verschiebbarem Rest der Tabelle](Freeze-columns.png)

Die Fixierung mehrerer Spalten erledigen Sie einfach mit der Maus: Bewegen Sie den Mauszeiger auf die vertikale Linie, die die Zeilennummerierung von der ersten Spalte trennt. Ziehen Sie nun die Maus nach rechts, um die Anzahl der fixierten Spalten festzulegen. Möchten Sie die Spaltenfixierung wieder auflösen, dann bewegen Sie den Mauszeiger auf den Rahmen zwischen der letzten fixierten und deren nachfolgender Spalte und ziehen Sie die Linie ganz nach links zurück.

## Standardwerte für die Datumsspalte

![Einstellungen einer Datumsspalte mit Auswahl eines statischen oder dynamischen Standarddatums](Default_value_date_column.png)

Wiederholt gewünscht, jetzt erfüllt: Nach Text-, Zahl- und Einfachauswahlspalte erhält mit SeaTable 2.7 auch die Datumsspalte eine Standardwertfunktion. Mit ihr fügen Sie neuen Einträgen automatisch einen statischen oder dynamischen Datumswert hinzu.

Das Veröffentlichungsdatum von SeaTable 2.7, der 2. Februar 2022, ist ein Beispiel für einen statischen Datumswert. Dynamische Datumswerte stellen einen relativen Bezug her und ändern sich im Laufe der Zeit. Neben dem aktuellen Datum (“Heute”) ist auch x Tage vor oder nach dem aktuellen Datum ein dynamischer Datumswert. Beides lässt sich ab sofort in der Datumsspalte mit der Standardwertfunktion abbilden. In Kombination mit den Datumsfunktionen der Formelspalte lassen sich damit quasi beliebige Datumswerte automatisch für neue Einträge erzeugen, die wiederum für Automationen genutzt werden können.

## Passwortgeschützte Bases

Für Bases mit vertraulichen Daten wünschen sich zahlreiche Kunden einen erweiterten Zugriffsschutz. SeaTable 2.7 bietet mit dem optionalen Passwortschutz für Bases einen solchen ab sofort an. Nur nach Eingabe des Passworts wird die Base aufgerufen und die Daten angezeigt. Der Passwortschutz kann von Eigentümern für die eigenen Bases sowie von Gruppenadministratoren für Bases der Gruppe eingerichtet und auch wieder entfernt werden.

Passwortgeschützte Bases lassen sich mit anderen Benutzern teilen. Natürlich müssen diese auch das Passwort beim Aufruf der Base eingeben. Gleiches gilt bei der Kopie einer passwortgeschützten Base. Den zusätzlichen Zugriffsschutz erkauft man sich also nicht mit einer reduzierten Flexibilität.

## … und vieles mehr

Wie die allermeisten neuen Versionen enthält auch das Release 2.7 wieder mehr erwähnenswerte Funktionen als die Release Notes bei akzeptabler Länge verdauen können. Darum hier weitere Neuerungen überblicksartig dargestellt:

Beim Verlinken von Einträgen bietet der Verknüpfungsassistent in SeaTable 2.7 eine bessere Suchfunktion. Bei der Eingabe mehrerer, durch Leerzeichen getrennt eingegebener Suchbegriffe sucht SeaTable in allen Spalten der verknüpften Tabelle. Konkret: Sie suche einen bestimmten Eintrag an einem bestimmten Datum, dann geben Sie einfach das Datum und mit Leerzeichen getrennt eine weitere Eigenschaft des gesuchten Eintrags ein. Der Assistent zeigt dann nur noch die entsprechenden Einträge an und viel manuelle Sucharbeit bleibt Ihnen erspart. Bisher suchte SeaTable die Eingabe als Ganzes in einer Spalte.

Webformulare können nun mit einem Cover-Bild oder einem Farbschema verschönert werden. Zusammen mit einem eingeblendeten Logo lassen sich ansehnliche und individuelle Formulare bauen. (Diese Funktion ist Enterprise Abonnenten vorbehalten.)

Team-Administratoren können ab sofort für Ihre Teammitglieder die 2-Faktor-Authentifizierung erzwingen und auch individuell deaktivieren. Der Team-Administrator kann so individuell auf erhöhte Sicherheitsanforderungen reagieren und Situationen, in denen Benutzer ihren zweiten Faktor verloren haben, leichter entschärfen.

Bisher blieben Verknüpfungen aus gelöschten und dann wiederhergestellten Zeilen verloren. Mit der Version 2.7 werden auch Verknüpfungen bei der Wiederherstellung einer Zeile wieder erzeugt.

Die mit [Version 2.3]({{< relref "posts/seatable-releases/seatable-release-2-3" >}}) eingeführte Archivfunktion hat weitere Schritte in Richtung produktiver Einsatz gemacht: Aus dem Archiv lassen sich jetzt Einträge löschen und auch Einträge bearbeiten. (Verknüpfungen können jedoch noch nicht erzeugt oder geändert werden.)
