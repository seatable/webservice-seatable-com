---
title: 'SeaTable 3.4: Dynamisches Seitendesign, weitere Suchfunktionen und verbesserte Webformulare'
description: 'Dokumente mit flexiblen Layouts, Formulare mit frei benennbaren Feldern und einfacher Vorbefüllung, neue Query-App für Feld-übergreifende Suche und Filter-/Sortierfunktionen in Ansichten – SeaTable 3.4 bietet mehr Individualisierung und Übersicht für Daten, Prozesse und Zusammenarbeit in jeder Organisation.'
date: 2023-03-01
lastmod: '2023-03-01'
author: 'rdb'
url: '/de/seatable-release-3-4'
color: '#f36f22'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 3.4: Dynamisches Design & neue Suche'
    description: 'Dynamische Objekt-Positionierung im Page-Design, verbesserte Suche, Webformen flexibler gestalten: So wird SeaTable 3.4 innovativer und nutzerfreundlicher!'
---

Frühlingserwachen bei SeaTable! Während draußen erste Blüten aus dem Boden sprießen, kommen wir mit SeaTable 3.4 fulminant aus der Winterpause. Machen Sie sich warm für eine verbesserte User Experience und noch mehr Gestaltungsfreiheit! Das Seitendesign-Plugin entfaltet nun ebenso wie der Editor für Webformulare sein volles Potenzial – mit erweiterten Funktionen zur dynamischen Positionierung von Elementen und anderen nützlichen Optionen. Entdecken Sie die neue Suchfunktion beim Filtern, Sortieren und Gruppieren in den Ansichtseinstellungen sowie beim Anlegen von Optionen in Auswahlspalten. Bemerkenswerte Neuerungen gibt es noch dazu bei der Data Query App, die jetzt eine verfeinerte Suche über mehrere Felder erlaubt. Auch das Zeilen-Kontextmenü erhält weitere Optionen und die Einträge im Zeilen-Log erstrahlen in neuem Glanz.

Neugierig geworden? Dann nichts wie los! Heute Morgen haben wir die SeaTable Cloud auf Version 3.4 aktualisiert. Alle Selbsthoster können das ebenfalls tun – und neuerdings sogar das Zeilenlimit pro Base entfesseln. Das Image von SeaTable 3.4 ist [im bekannten Docker Repository](https://hub.docker.com/r/seatable/seatable-enterprise) zum Download verfügbar. Im [Changelog]({{< relref "posts/seatable-releases/seatable-release-3-4" >}}) finden Sie wie immer die vollständige Liste der Änderungen.

## Dynamische Positionierung von Elementen im Seitendesign

Mit dem Seitendesign-Plugin können Sie Daten aus Ihren Bases in anschauliche Dokumente umwandeln. Per Knopfdruck ist ein Serienbrief, eine Urkunde oder eine Bestandsliste erzeugt. Weniger geeignet war das Seitendesign-Plugin bisher für die Erzeugung von Dokumenten mit Inhalten variabler Länge, wie z. B. Angebote oder Rechnungen. Diese Einschränkung heben wir mit SeaTable 3.4 auf.

Das Seitendesign-Plugin in SeaTable 3.4 ermöglicht erstmals die dynamische Positionierung von Elementen auf der Seite. Je nach Länge vorausgehender Elemente wandern nachfolgende Elemente auf einer Seite nach unten. So können Sie die gleiche Vorlage verwenden, egal ob ein Angebot eine oder ein Dutzend Positionen enthält. Seitenumbrüche und neue Seiten werden automatisch eingefügt. Den oberen und unteren Seitenrand können Sie individuell einstellen.

![SeaTable 3.4 - Dynamic Positioning of elements in the page design plugin](SeaTable-3.4-DynamicPositioningElements.png)

Die neue Funktion “Tabelle automatisch an Inhalt anpassen” gibt es für das Ansichtselement “Alle Einträge der Ansicht” sowie die tabellarische Darstellung von Verknüpfungen unter “Tabellenfelder”. Bei Aktivierung der Funktion definiert der Platzhalter für das Tabellenelement (grün umrahmtes Element im Screenshot) die Mindestlänge der einzufügenden Tabelle. Ist die Tabelle länger als der Platzhalter, wird dieser automatisch verlängert.

Die bisherige Funktion “Weitere Seiten hinzufügen, wenn die Größe des Platzhalters nicht für alle Einträge ausreicht”, die in [Version 3.1]({{< relref "posts/seatable-releases/seatable-release-3-1" >}}) eingeführt wurde, gibt es in SeaTable 3.4 nicht mehr und wird mit der leistungsfähigeren Funktion ersetzt. War sie bei einer Vorlage für ein Tabellenelement aktiviert, dann ist automatisch die neue Funktion aktiv.

## Suche über mehrere Felder mit der Data Query App

Über SeaTables externe Apps lassen sich Tabellendaten auf einfache Art und Weise öffentlich zugänglich machen. Insbesondere die Data Query App dient dazu, Datenbestände mit vielen Hunderten oder sogar Tausenden Zeilen (z. B. einen Produktkatalog oder eine Mitgliederliste) schnell und gezielt abzufragen. Mit SeaTable 3.4 haben wir das Manko beseitigt, dass Abfragen nur über ein einzelnes Feld erfolgen konnten.

Nun können Abfragen über eine beliebige Anzahl an Feldern erfolgen. Für jedes Feld können Sie festlegen, ob es sich um ein Pflichtfeld handelt oder die Eingabe optional ist. Für textbasierte Felder können Sie darüber hinaus eine unscharfe Suche aktivieren und die Berücksichtigung von Groß- und Kleinschreibung erzwingen. Durch die Kombination der Optionen lässt sich die Suche in hohem Maße steuern. Unverändert bleiben das Menü zum Ausblenden von einzelnen Spalten in den Suchergebnissen sowie die Sortieroptionen.

![SeaTable 3.4 - Improved data query app](SeaTable-3.4-DataQueryApp.png)

Bei mehreren Abfragefeldern gilt immer eine Boolesche UND-Verknüpfung, d.h. alle eingegebenen Werte müssen in den Suchergebnissen vorkommen. Für vertrauliche Informationen ist die Data Query App natürlich weiterhin ungeeignet, weil sie keine Benutzer-Authentifizierung erfordert. Mit einer weiteren externen App, die wir demnächst vorstellen werden, werden wir diese funktionale Lücke schließen.

## Verbesserte Webformulare

In [SeaTable 3.3]({{< relref "posts/seatable-releases/seatable-release-3-3" >}}) haben wir den Formular-Editor auf das Block-Design umgestellt. Dadurch wurde es möglich, Felder in beliebiger Reihenfolge anzuordnen. Ebenfalls neu eingeführt haben wir die statischen Elemente Anmerkungen und Trennlinie. In der Entwicklung waren tatsächlich noch weitere Verbesserungen, die es aber nicht mehr in das Weihnachtsrelease geschafft haben. Dies holen wir nun nach!

Der Formular-Editor von SeaTable 3.4 bietet die Option, für jedes Formularelement einen Anzeigenamen festzulegen, der dann im Webformular anstelle des Spaltennamens angezeigt wird. Auf diese Weise wird es möglich, die Spalten in der Tabelle losgelöst vom Webformular zu benennen: Die Spaltennamen können kurz und knapp sein, während die Namen der Formularfelder im Sinne der Benutzerfreundlichkeit etwas wortreicher ausfallen dürfen. So haben Sie noch mehr Freiheit bei der Gestaltung Ihrer Webformulare.

![SeaTable 3.4 - New editor for custom form links](SeaTable-3.4-FormLinkEditor.png)

Gleich zwei Verbesserungen betreffen SeaTables Fähigkeit, Webformulare über URL-Parameter vorauszufüllen. Diese Funktion existiert zwar bereits seit geraumer Zeit, aber es fehlte eine benutzerfreundliche Möglichkeit für die Erstellung und Verwaltung individueller Formularlinks sowie die Option, einen vorausgefüllten Wert vor Änderungen durch den Formular-Benutzer zu schützen. Beides haben wir bei SeaTable 3.4 in Angriff genommen und gelöst.

Hinter der Schaltfläche “… Mehr” im Formular-Editor verbirgt sich ein neues Fenster für die Erstellung beliebig vieler Formularlinks. Jeder Link kann einen oder mehrere vorausgefüllte Formularwerte enthalten. Des Weiteren können Sie für jeden Wert festlegen, ob er überschreibbar oder schreibgeschützt sein soll. Ein erstellter Link wird über einen frei wählbaren Namen identifiziert. So lassen sich bestehende Formularlinks auch leicht wieder aufrufen und ggf. ändern.

## Such- und Filterfunktion in den Ansichtseinstellungen

Bei Tabellen mit vielen Spalten können die Auswahllisten in den Ansichtseinstellungen ganz schön lang und unübersichtlich werden. Um den Suchaufwand auf ein Minimum zu reduzieren, gibt es nun in allen Hauptmenüs der Ansichtseinstellungen (Filtern, Sortieren, Gruppieren, Ausblenden und Zeilen formatieren) eine Such- und Filterfunktion. Die Nutzung ist denkbar einfach: Geben Sie den Namen der gesuchten Spalte ein und schon wird nur noch die gewünschte Spalte angezeigt. Natürlich funktioniert dies auch dann, wenn Sie nur einen Teil des Namens eingeben, beispielsweise wenn Sie nicht ganz sicher sind, wie die gesuchte Spalte heißt. Aus der gefilterten Ergebnisliste können Sie dann die benötigte Spalte ohne großen Aufwand auswählen.

![SeaTable 3.4 - Filters in view settings](SeaTable-3.4-FilterInViewSettings.png)

Da diese praktische Suchfunktion bei Einfach- und Mehrfach-Auswahlspalten mit vielen Optionen ebenfalls fehlte, haben wir sie auch dort integriert. So müssen Sie bei der Anlage neuer Optionen nie wieder aufwändig prüfen, ob eine Option bereits existiert oder nicht.

## Und noch vieles mehr

Bei einem Blick in das Changelog finden Sie noch viele weitere Verbesserungen, die wir hier nicht einzeln erläutern können. Nur auf drei weitere Verbesserungen soll hier in aller Kürze hingewiesen werden.

![SeaTable 3.4 - New feature add/duplicate multiple rows](SeaTable-3.4-AddMultipleRows.png)

Über das Zeilen-Kontextmenü, das Sie in Tabellen per Rechtsklick erreichen, lassen sich nun mehrere Leerzeilen einfügen und auch mehrere ausgewählte Zeilen duplizieren.

Die Logs in den Zeilendetails präsentieren sich in SeaTable 3.4 kompakter als bisher. Alle Änderungen, die ein Nutzer zu einem bestimmten Zeitpunkt an einer Zeile vorgenommen hat, werden in einem Sammeleintrag dargestellt. Bisher wurde für jede Änderung ein eigener Logeintrag angezeigt.

Bisher lag das Zeilenlimit pro Base unveränderlich bei 100.000 Zeilen. Wurde das Limit überschritten, ließ sich die Base nur noch im Lesemodus öffnen. Mit SeaTable 3.4 bekommen Selbsthoster mehr Kontrolle über das Zeilenlimit. In bestimmten Nutzungsfällen kann das Limit über die Konfigurationsdateien erhöht werden. Mehr Informationen dazu erhalten Sie im [SeaTable Admin Manual](https://admin.seatable.com/configuration/base-rows-limit/).

## Zwei Funktionseinschränkungen

An Gruppen freigegebene Bases und Ansichten können mit der neuen Version nicht mehr in Ordner verschoben werden. Freigegebene Bases und Ansichten, die in der Vergangenheit in einen Ordner verschoben wurden, werden nun außerhalb des Ordners angezeigt.

Die Zugriffsberechtigung “Bestimmte Gruppen” für Webformulare wurde entfernt. Wenn Sie zu den wenigen Benutzern gehören, die diese genutzt haben, dann müssen Sie die Freigabeberechtigung neu setzen.

## Ankündigung einer maßgeblichen Funktionsänderung

Mit SeaTable 3.5 wird ein Limit von 100.000 Zeichen für einzelne Zellen vom Typ Formatierter Text eingeführt. 100.000 Zeichen entsprechen ungefähr 25 DIN-A4-Seiten Text. Das Zeichenlimit sollte also für sehr wenige Benutzer Auswirkungen haben.

Bildnachweis: wirestock auf Freepik
