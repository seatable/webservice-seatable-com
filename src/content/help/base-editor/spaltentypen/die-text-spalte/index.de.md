---
title: 'Die Text-Spalte'
date: 2023-05-03
lastmod: '2024-03-11'
categories:
    - 'text-und-zahlen'
author: 'nsc2'
url: '/de/hilfe/die-text-spalte'
aliases:
    - '/de/hilfe/validierung-der-eingabe-bei-textfeldern'
seo:
    title: 'Die Text-Spalte in SeaTable'
    description: 'Lernen Sie einen der elementarsten Spaltentypen von SeaTable kennen: die Text-Spalte. Mit ihr können Sie unstrukturierte Zeichenfolgen ohne Zeilenumbrüche erfassen – Verwendung, Validierung und Standardwerte einfach erklärt.'
weight: 1
---

Die Text-Spalte gehört zu den elementarsten **Spaltentypen** in SeaTable und wird Ihnen auch im Auswahl-Menü des Spaltentyps an erster Stelle angezeigt.

![Die reguläre Textspalte](images/select-regular-text-column.png)

Standardmäßig fügt SeaTable jeder neu erstellten Tabelle automatisch eine **Text-Spalte** als erste Spalte hinzu. Darüber hinaus können Sie beliebig viele Text-Spalten manuell zu Ihrer Tabelle hinzufügen. Wie das geht, erfahren Sie [hier]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![Die Text-Spalte](images/text-column-new.png)

Die **erste Spalte** einer Tabelle weist mehrere [Besonderheiten]({{< relref "help/base-editor/spalten/die-besonderheiten-der-ersten-spalte" >}}) auf, wie Sie im verlinkten Artikel nachlesen können.

## Verwendung der Text-Spalte

Die Text-Spalte eignet sich besonders gut zur Erfassung und [Sortierung]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) kurzer alphanumerischer Zeichenfolgen, beispielsweise **Begriffe**, **Namen**, **Passwörter**, **Kfz-Kennzeichen** oder **IBAN**.

![Anwendungsbeispiel der regulären Textspalte](images/regular-text-example.png)

{{< warning  headline="UTF-8"  text="SeaTable unterstützt alle Zeichen nach UTF-8-Standard, da UTF-8 die weltweit am weitesten verbreitete Zeichencodierung für das Internet ist." />}}

Bei der Verwendung der Spalte ist es sinnvoll, die Einträge möglichst **kurz** zu halten, da nur eine **begrenzte Anzahl an Zeichen** angezeigt werden kann, ohne dass die Spaltenbreite vergrößert werden muss.

![Zu lange Einträge können in einer Textspalte nicht gänzlich angezeigt werden, ohne die Spaltenbreite zu vergrößern](images/use-short-entries.png)

## Weitere textbasierte Spaltentypen

Beachten Sie, dass für Einträge in der Text-Spalte **keine Formatierungsoptionen** zur Verfügung stehen. Wenn Sie strukturierte Texte mit Zeilenumbrüchen, Listen, Bildern etc. erfassen möchten, sollten Sie die Spalte [Formatierter Text]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) nutzen.

Es gibt in SeaTable drei weitere textbasierte Spaltentypen für spezielle Anwendungsfälle: 
- die [E-Mail-Spalte]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}})
- die [URL-Spalte]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})
- die [Telefonnummer-Spalte]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

{{< warning  headline="Hinweis" >}}
Es gibt zahlreiche Textfunktionen für [Formel-Spalten]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}), die sich wie Text-Spalten verhalten, wenn die Ergebnisse **Strings** sind.
{{< /warning >}}

## Standardwert festlegen

Sie können für jede Text-Spalte einen voreingestellten [Standardwert]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) festlegen. Dieser wird automatisch in jede neue Zeile der Tabelle eingetragen.

Wenn Sie als Standardwert die Referenz **{creator.name}** oder **{creator.id}** festlegen, wird automatisch der **Name** oder die **ID des Benutzers** eingetragen, der die Zeile hinzugefügt hat.

![Mit einem Standardwert auf den Benutzernamen referenzieren](images/Set-creator-name-as-default-value.png)

## Eingaben validieren

Bei der Verwendung von Text-Spalten in Ihren Tabellen haben Sie die Möglichkeit, Eingaben zu validieren. Mithilfe einer Validierung, bei der reguläre Ausdrücke unterstützt werden, können Sie **Zellwerte überprüfen** und Zellen mit einem vom gültigen Format abweichenden Inhalt hervorheben.

Sie können den Formatcheck bereits beim Anlegen einer Text-Spalte einrichten, indem Sie den Regler aktivieren.

![Aktivierung der Validierung der Eingabe von Text-Spalten](images/activate-validation-1.png)

Falls Sie eine Validierung der Eingaben in einer bereits angelegten Text-Spalte durchführen möchten, klicken Sie zunächst auf das **Dreieck-Symbol** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} der entsprechenden Spalte und wählen im Drop-down-Menü **Spaltentyp anpassen** aus.

1. Aktivieren Sie den Regler **Eingabe validieren**
2. Definieren Sie ein **Zielformat**.
![Definition des Zielformats](images/define-specific-format-2.png)
3. Bestätigen Sie mit **Abschicken**.

### Folge der Validierung

Nach erfolgreicher Validierung werden die **Zellen** mit einem vom Zielformat **abweichenden Inhalt** rot hervorgehoben.

![In Rot hervorgehobene Zellen mit einem vom Zielformat abweichenden Inhalt](images/marked-entries-which-not-match-the-format.png)

### Reguläre Ausdrücke

Für die Validierung Ihrer Eingaben in Text-Spalten unterstützt SeaTable **reguläre Ausdrücke**. In der folgenden Tabelle finden Sie einige Beispiele:

| Regulärer Ausdruck              | Funktion                                                                     |
| ------------------------------- | ---------------------------------------------------------------------------- |
| \[123456\]                      | Prüfen, ob eine Eingabe einer Schulnote von 1 bis 6 entspricht.              |
| \[1-9\]\[0-9\]?\[0-9\]?\[a-z\]? | Format einer deutschen Hausnummer überprüfen (3 Ziffern + 1 Buchstabe)       |
| \[0-9\]{5}                      | Prüfung des Formats deutscher Postleitzahlen (5x eine Zahl zwischen 0 und 9) |
| \[0-9/. \\-\]+                  | Prüfung des Formats einer Telefonnummer                                      |
| Max.\*Mustermann                | Suche nach einem möglichen zweiten Vornamen eines Autors                     |

{{< warning  headline="Tipp"  text="Ein ausführliches **Tutorial** für die Nutzung von regulären Ausdrücken zur Prüfung von Zeichenketten finden Sie [hier (Deutsch)](https://danielfett.de/2006/03/20/regulaere-ausdruecke-tutorial/) und [hier (Englisch)](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)." />}}
