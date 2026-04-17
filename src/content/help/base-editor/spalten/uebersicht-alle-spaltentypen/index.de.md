---
title: 'Übersicht über alle Spaltentypen'
date: 2022-08-25
lastmod: '2024-03-18'
categories:
    - 'arbeiten-mit-spalten'
author: 'cdb'
url: '/de/hilfe/uebersicht-alle-spaltentypen'
seo:
    title: 'Übersicht aller Spaltentypen in SeaTable – Funktionen'
    description: 'Lernen Sie alle 26 Spaltentypen von SeaTable kennen: von Text und Zahl bis Datei, Auswahlfeldern, Formeln und relationalen Spalten. Kompakt erklärt.'
star: true
weight: 1
---

In SeaTable können Sie Informationen und Daten in den unterschiedlichsten Formaten abspeichern.

- Neben einfachen, textbasierten Informationen (z. B. Wörter, Zahlen, Geldbeträge) unterstützt SeaTable auch die Speicherung komplexer Informationen (z. B. Dateien, Bilder, formatierter Text inkl. eingefügter Elemente).
- Mit Auswahlfeldern können Sie Ihre Daten in definierte Kategorien einteilen und integrierte Validierungsfunktionen (z. B. URL, Positionsdaten) stellen sicher, dass Ihre Eingaben in einem einheitlichen, direkt auswertbaren Format vorliegen.
- Mit Formeln können Sie Rechenoperationen ausführen und mit Verknüpfungen erstellen Sie Relationen zwischen Einträgen unterschiedlicher Tabellen, die leistungsfähige Datenbankoperationen erlauben.

Lernen Sie hier SeaTables 26 unterschiedliche Spaltentypen kennen!

## Spalten mit manueller Dateneingabe

Jeder Tabellenspalte ist ein Typ zugeordnet. Der Spaltentyp entscheidet, welche Daten Sie in die Zellen der Spalte eingeben können. In ein Textfeld können Sie beispielsweise keine Dateien einfügen. Die Datum-Spalte wiederum erzwingt die Eingabe eines Datums im gewählten Format.

### Text

Symbol: {{< seatable-icon icon="dtable-icon-single-line-text" >}} **Text**

Dieser Spaltentyp speichert **Text** ohne Formatierung und gehört zu den grundlegendsten Spaltentypen in SeaTable. Textinhalte bestehen aus **Buchstaben**, **Zahlen** und **Sonderzeichen** sowie **Leerzeichen**. Deswegen werden Text-Spalten häufig für Namen und (Kurz-)Beschreibungen verwendet.

[Mehr zur Text-Spalte]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})

### Formatierter Text

Symbol: {{< seatable-icon icon="dtable-icon-long-text" >}} **Formatierter Text**

In diesem Spaltentyp können Sie **längere Texte** mit eingefügten Elementen, wie **Bildern** und **Tabellen** speichern. Für Ihre Texte stehen Ihnen zudem diverse Formatierungs- und Strukturierungsoptionen mithilfe der Auszeichnungssprache Markdown zur Verfügung. Daher wird die Spalte _Formatierter Text_ häufig für Beschreibungen und Dokumentationen verwendet. Wenn es für die Informationserfassung hilfreich ist, dass Texte strukturierende Elemente beinhalten und/oder Text und Bilder nahe beieinander stehen, dann ist dieser Spaltentyp ideal.

[Mehr zur Spalte Formatierter Text]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})

### Zahl

Symbol: {{< seatable-icon icon="dtable-icon-number" >}} **Zahl**

Zahlen-Spalten speichern **numerische Informationen** und können vielseitig genutzt werden, um mit Zahlen jeder Art zu arbeiten. Eine numerische Information kann dabei eine **Zahl**, ein **Prozentsatz** oder ein **Geldbetrag** sein. Weiterhin ermöglichen Zahlen-Spalten Ihnen die **Berechnung von Werten**, die Sie mit Formeln und [Statistiken]({{< relref "help/base-editor/statistiken" >}}) visualisieren können. Zum Speichern von beliebig langen Zeichenfolgen eignen sich Zahlen-Spalten jedoch nicht und die Eingabe von Buchstaben wird in diesem Spaltentyp von SeaTable verweigert.

[Mehr zur Zahlen-Spalte]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})

### Datum

Symbol: {{< seatable-icon icon="dtable-icon-calendar-alt-solid" >}} **Datum**

Mithilfe der Datum-Spalte können Sie **Zeitpunkte** und **Termine** bis auf die Minute genau in Ihren Tabellen erfassen. Beachten Sie dabei, dass Datumspalten die eingegebenen Informationen stets als Datum interpretieren, sodass nicht als Datum interpretierbare Eingaben immer als ungültig verworfen werden.

[Mehr zur Datum-Spalte]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})

### Dauer

Symbol: {{< seatable-icon icon="dtable-icon-duration" >}} **Dauer**

Die Dauer-Spalte ist ein spezialisierter Zahl-Spaltentyp für die Speicherung von **Zeitmessungen, -spannen und -intervallen** und kann dabei einen Zeitraum auf die Minute oder gar auf die Sekunde genau erfassen. Aus diesem Grund eignet sich die Spalte unter anderem besonders gut, um die Dauer von verschiedenen Ereignissen festzuhalten. Beachten Sie bei der Verwendung der Spalte jedoch, dass nicht-numerische Eingaben stets als ungültig verworfen werden.

[Mehr zur Dauer-Spalte]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})

### Einfachauswahl

Symbol: {{< seatable-icon icon="dtable-icon-single-election" >}} **Einfachauswahl**

In einer Zelle einer Einfachauswahl-Spalte können Sie **einen Wert** aus einer Liste definierter Optionen auswählen. Die Liste der definierten Optionen erstellen Sie pro Einfachauswahl-Spalte selbst und können diese jederzeit an wechselnde Umstände anpassen. Die Einfachauswahl eignet sich somit besonders zur Kategorisierung und Gruppierung Ihrer Daten.

[Mehr zur Einfachauswahl-Spalte]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}} )

### Mehrfachauswahl

Symbol: {{< seatable-icon icon="dtable-icon-multiple-selection" >}} **Mehrfachauswahl**

Bei einer Mehrfachauswahl können Sie eine **beliebige Anzahl an Werten** aus einer Liste definierter Optionen auswählen. Wie bei der Einfachauswahl erstellen Sie die Liste der möglichen Werte selbst und passen diese Ihren individuellen Anforderungen an. Die Mehrfachauswahl bietet sich daher ideal für die Verschlagwortung – auch Tagging genannt – an.

[Mehr zur Mehrfachauswahl-Spalte]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}})

### Bild

Symbol: {{< seatable-icon icon="dtable-icon-picture" >}} **Bild**

Der Spaltentyp Bild speichert eine beliebige Anzahl an **Bilddateien** in den Dateiformaten **BMP**, **GIF**, **ICO**, **JPG**, **PNG**, **SVG** und **TIF**. Die Bild-Spalte ist damit eine auf Bilddateiformate eingeschränkte Datei-Spalte.

[Mehr zur Bild-Spalte]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}})

### Datei

Symbol: {{< seatable-icon icon="dtable-icon-file" >}} **Datei**

Der Spaltentyp Datei speichert eine beliebige Anzahl an Dateien **jedes Dateityps**. Für zahlreiche Bilddateiformate bietet SeaTable eine Vorschaufunktion.

[Mehr zur Datei-Spalte]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}})

### E-Mail

Symbol: {{< seatable-icon icon="dtable-icon-email" >}} **E-Mail**

E-Mail-Spalten sind spezialisierte Text-Spalten für die Erfassung und Speicherung von **E-Mail-Adressen** und erlauben die direkte Verwendung per Mausklick. Die E-Mail-Spalte ist insbesondere für Webformulare praktisch. Die Verwendung eines E-Mail-Feldes an Stelle einer Text-Spalte stellt sicher, dass die Eingabe die Syntax einer gültigen E-Mail-Adresse hat. Zudem können E-Mail-Spalten über [Schaltflächen]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) und [Automationen]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}) zum Versand von E-Mails genutzt werden.

Falls Sie detailliertere Informationen zur E-Mail-Spalte benötigen, werfen Sie einen Blick in diesen [Artikel]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}).

### URL

Symbol: {{< seatable-icon icon="dtable-icon-url" >}} **URL**

URL-Spalten interpretieren die eingegebene Information als eine **Ressource** im lokalen Netzwerk bzw. im Internet und erlauben den direkten Aufruf per Klick. Da Eingaben in diesem Spaltentyp nicht validiert werden, können in einer Zelle eine Internetadresse (z.B. https://seatable.com) oder eine IP-Adressen (z.B. 192.168.178.1) gespeichert werden.

[Mehr zur URL-Spalte]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})

### Checkbox

Symbol: {{< seatable-icon icon="dtable-icon-check-square-solid" >}} **Checkbox**

Checkboxen erlauben die Erfassung **binärer Informationen**: Ja oder Nein bzw. _Haken gesetzt_ vs. _Haken nicht gesetzt_. Weitere Eingaben sind nicht möglich. Daher eignen sie sich gut, um beispielsweise Aufgaben als erledigt zu markieren – also für den Überblick, ob Zeilen eine bestimmte Ja/Nein-Bedingung erfüllen. Aus diesem Grund können Sie Checkbox-Spalten auch hervorragend zum [Filtern]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}), [Sortieren]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) oder [Gruppieren]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) nutzen.

[Mehr zur Checkbox--Spalte]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}})

### Rating

Symbol: {{< seatable-icon icon="dtable-icon-rate" >}} **Rating**

Eine Rating-Spalte ermöglicht die **Einstufung** Ihrer Datensätze, um ein **Ranking** oder eine **Qualitätsbewertung** vorzunehmen. Sie können eine Bewertungsskala von 1 bis 10 auswählen sowie zwischen verschiedenen Farben und Formen wählen. Damit können Daten schnell und unkompliziert für jeden verständlich eingeschätzt und bewertet werden.

[Mehr zur Rating-Spalte]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})

### Telefonnummer

Symbol: {{< seatable-icon icon="dtable-icon-telephone" >}} **Telefonnummer**

Es gibt in SeaTable einen eigenen Spaltentyp für Telefonnummern. Im Vergleich zu einer normalen Text-Spalte bietet die Telefonnummer-Spalte den Vorteil, dass Sie per Mausklick **eine Telefonnummer anrufen** können.

[Mehr zur Telefonnummer-Spalte]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

### Formel

Symbol: {{< seatable-icon icon="dtable-icon-formula" >}} **Formel**

Mithilfe von Formeln können Sie unterschiedliche Spaltenwerte einer Zeile **verknüpfen** und basierend auf dem Inhalt dieser Spalten verschiedene **Funktionen** erstellen. Sie können unter anderem mit Werten in Ihren Tabellen rechnen, Werte verändern oder Werte aus der gleichen Zeile miteinander in Beziehung setzen.

Sie benötigen weitere Infos zur Formel-Spalte? Dann werfen Sie einen Blick in diesen [Artikel]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}). Da es sich bei Formeln um ein sehr komplexes Feature handelt, finden Sie zahlreiche weitere Hilfeartikel in unserem Handbuch. Klicken Sie [hier]({{< relref "help/base-editor/formeln" >}}) und Sie werden zur Übersichtsseite weitergeleitet.

### Verknüpfung zu anderen Einträgen

Symbol: {{< seatable-icon icon="dtable-icon-link-other-record" >}} **Verknüpfung zu anderen Einträgen**

In Zellen dieses Spaltentyps können Sie eine beliebige Anzahl an **Verweisen auf Einträge in anderen Tabellen** der Base erfassen. Die Verknüpfungsspalte ist dafür gedacht, Relationen zwischen Einträgen unterschiedlicher Tabellen abzubilden. Mit der Verknüpfungsspalte lassen sich 1:n und n:1 Relationen ebenso abbilden wie n:m Relationen.

Weitere Informationen zum Spaltentyp Verknüpfung zu anderen Einträgen finden Sie [hier]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}).

### Formel für Verknüpfungen

Symbol: {{< seatable-icon icon="dtable-icon-link-formulas" >}} **Formel für Verknüpfungen**

Mit der Formel für Verknüpfungen können Sie Daten aus **verknüpften Tabellen** in Ihrer aktuellen Tabelle **darstellen** und miteinander **in Beziehung setzen**. Für den Spaltentyp stehen insgesamt fünf verschiedene Formeln zur Verfügung, mit denen Sie auch statistische Berechnungen durchführen können. Voraussetzung für die Verwendung der Spalte ist das Vorhandensein von mindestens einer Spalte des Typs **Verknüpfung zu anderen Einträgen** in Ihrer Tabelle.

[Mehr zur Spalte Formel für Verknüpfungen]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}})

### Mitarbeiter

Symbol: {{< seatable-icon icon="dtable-icon-collaborator" >}} **Mitarbeiter**

In einer Mitarbeiter-Spalte können Sie eine beliebige Anzahl an **Benutzern**, die mindestens Lesezugriff auf die Base haben, erfassen. SeaTable Benutzer ohne Zugriff können nicht in der Spalte als Mitarbeiter erfasst werden. Andere Eingaben sind ebenfalls nicht erlaubt. Die Mitarbeiter-Spalte ist insbesondere für das Projektmanagement sinnvoll. Wenn Sie in einer Tabelle beispielsweise zu erledigende Aufgaben erfassen, dann können Sie in Spalten des Typs Mitarbeiter die ausführenden Personen und den Verantwortlichen festhalten.

[Mehr zur Mitarbeiter-Spalte]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}})

### Schaltfläche

Symbol: {{< seatable-icon icon="dtable-icon-button" >}} **Schaltfläche**

Mit Schaltflächen können Sie die Bearbeitung von Daten oder die Ausführung bestimmter Aktionen **automatisieren**. Beachten Sie dabei jedoch, dass Sie Schaltflächen stets **manuell** bedienen müssen. Mithilfe des Buttons, den Sie in dieser Spalte Ihren Zeilen hinzufügen können, lösen Sie bestimmte im Vorhinein definierte Aktionen aus. Aus diesem Grund eignet sich dieser Spaltentyp besonders gut für die Automatisierung von Prozessschritten.

Weitere Informationen zur Schaltfläche und den in Spalten dieses Typs auslösbaren Aktionen finden Sie in diesem [Artikel]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}).

### Geoposition

Symbol: {{< seatable-icon icon="dtable-icon-location" >}} **Geoposition**

In dieser Spalte können Sie **Orte** festhalten und später mit dem [Karten-Plugin]({{< relref "help/base-editor/plugins/anleitung-zum-karten-plugin" >}}) visualisieren. Dafür können Sie entweder die Angabe mit Land und Region oder mit Breiten- und Längengrad auswählen. Zusätzlich haben Sie die Möglichkeit, ein Land bzw. eine Region mithilfe der Suchfunktion zu finden und als Eintrag hinzuzufügen.

[Mehr zur Geopositions-Spalte]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}})

### Digitale Signatur

Symbol: {{< seatable-icon icon="dtable-icon-rename" >}} **Digitale Signatur**

In einer Signatur-Spalte können Sie **digitale Unterschriften** hinterlegen, die automatisch in der Dateiverwaltung Ihrer Base gespeichert werden. Digitale Unterschriften eignen sich sehr gut für die Datenerfassung mithilfe von **Webformularen**, um beispielsweise Anträge bequem online unterschreiben zu lassen.

[Mehr zur Signatur-Spalte]({{< relref "help/base-editor/spaltentypen/die-signatur-spalte" >}})

## Spaltentypen mit automatischer Datenerfassung

Neben den Spaltentypen, in denen Sie als Anwender Daten erfassen, gibt es in SeaTable fünf weitere Spaltentypen, deren Inhalte SeaTable automatisch erzeugt. Diese Spalten lassen sich nicht durch Benutzer manuell bearbeiten. Sie dienen primär Dokumentationszwecken.

### Ersteller

Symbol: {{< seatable-icon icon="dtable-icon-creator" >}} **Ersteller**

SeaTable dokumentiert in der Ersteller-Spalte automatisch den **Namen des Benutzers**, der die Zeile erstellt hat.

[Mehr zur Ersteller-Spalte]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})

### Erstellt

Symbol: {{< seatable-icon icon="dtable-icon-creation-time" >}} **Erstellt**

SeaTable dokumentiert in der Erstellt-Spalte automatisch das **Datum und die Uhrzeit der Erstellung der Zeile**. Datum und Uhrzeit werden im Format JJJJ-MM-TT HH:MM angezeigt.

[Mehr zur Erstellt-Spalte]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})

### Letzter Bearbeiter

Symbol: {{< seatable-icon icon="dtable-icon-creator" >}} **Letzter Bearbeiter**

SeaTable dokumentiert in der Spalte Letzter Bearbeiter automatisch den **Namen des Benutzers**, der die **letzte Änderung** an einem Eintrag vorgenommen hat. Da die Spalte automatisch Änderungen an Einträgen erfasst, eignet sie sich zum Beispiel gut als Trigger für Automationen sowie für Filter und Sortierungen.

[Mehr zur Spalte Letzter Bearbeiter]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})

### Zuletzt bearbeitet

Symbol: {{< seatable-icon icon="dtable-icon-creation-time" >}} **Zuletzt bearbeitet**

SeaTable dokumentiert in der Spalte Zuletzt bearbeitet das **Datum und die Uhrzeit der letzten Änderung eines Eintrags**. Datum und Uhrzeit werden im Format JJJJ-MM-TT HH:MM angezeigt. Da die Spalte automatisch Änderungen an Einträgen erfasst, eignet sie sich gut als Trigger für Automationen sowie für Filter und Sortierungen.

[Mehr zur Spalte Zuletzt bearbeitet]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})

### Automatische Nummer

Symbol: {{< seatable-icon icon="dtable-icon-autonumber" >}} **Automatische Nummer**

Der Spaltentyp Automatische Nummer erzeugt eine **automatisch ansteigende Nummer** für jede neue Zeile. Dieser Spaltentyp kommt immer dann zum Einsatz, wenn Sie für jeden Datensatz eine eindeutige Kennung benötigen.

[Mehr zur Spalte Automatische Nummer]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}}).
