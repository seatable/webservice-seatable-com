---
title: 'Die Spalte Formatierter Text'
date: 2023-02-21
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'kgr'
url: '/de/hilfe/die-spalte-formatierter-text'
aliases:
    - '/de/hilfe/die-spalten-text-und-formatierter-text'
seo:
    title: 'Der Spaltentyp Formatierter Text in SeaTable'
    description: 'Nutzen Sie formatierte Text-Spalten, um längere Inhalte zu strukturieren: Formatierungsmöglichkeiten und Unterschiede zur Text-Spalte im Überblick.'
weight: 2
---

Für das **Erfassen strukturierter Texte jeglicher Länge** steht Ihnen in SeaTable der Spaltentyp *Formatierter Text* zur Verfügung. Erfahren Sie in diesem Artikel, was die Unterschiede zur Text-Spalte sind und in welchen Fällen es sinnvoll ist, auf die formatierte Text-Spalte zurückzugreifen.

## Verwendung der Spalte Formatierter Text

Der Spaltentyp **Formatierter Text** erfasst im Gegensatz zur Text-Spalte keine unstrukturierten Zeichenfolgen, sondern formatierte Texte mit Zeilenumbrüchen, Listen, Bildern etc.

![Die Spalte Formatierter Text](images/formatted-text-column.png)

Formatierte Text-Spalten eignen sich besonders zum Festhalten von **längeren Texten**, zum Beispiel Produktbeschreibungen, Checklisten oder Social Media Posts.

{{< warning  headline="UTF-8"  text="SeaTable unterstützt alle Zeichen nach UTF-8-Standard, da UTF-8 die weltweit am weitesten verbreitete Zeichencodierung für das Internet ist." />}}

Sie verfassen Ihre Einträge dabei **nicht** direkt in der Zelle, sondern in einem per Klick aufrufbaren **Editor**, welcher verschiedene **Formatierungsoptionen** bietet. So können Sie im Gegensatz zur Text-Spalte auch längere Texte strukturieren.

![Anwendungsbeispiel einer Formatierten Textspalte](images/long-text-example.png)

Unter anderem können Sie ein **Absatzformat** wählen, die **Schrift** kursiv oder fett setzen sowie **Links**, **Zitate**, **Listen**, **Tabellen** und **Bilder** einfügen.

{{< warning  type="warning" headline="Zeichenlimit"  text="Für einzelne Zellen vom Typ Formatierter Text gilt ein Limit von 100.000 Zeichen. Dies entspricht ungefähr 25 DIN-A4-Seiten Text. Das Zeichenlimit sollte sich also nur in Ausnahmefällen auf Ihre Arbeit auswirken." />}}

## Weitere textbasierte Spaltentypen

Wenn Sie **kurze Zeichenfolgen ohne Formatierung** (z. B. Namen, Passwörter, Kfz-Kennzeichen) erfassen möchten, sollten Sie die [Text-Spalte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}) nutzen.

Neben der formatierten Text-Spalte gibt es in SeaTable noch drei weitere textbasierte Spaltentypen für spezielle Anwendungsfälle: 
- die [E-Mail-Spalte]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}})
- die [URL-Spalte]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})
- die [Telefonnummer-Spalte]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

## Standardwert festlegen

Sie können für jede formatierte Text-Spalte einen voreingestellten [Standardwert]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) festlegen. Dieser Text wird automatisch bei jeder neu erstellten Zeile in die Zelle eingetragen.

1. Klicken Sie auf den **Drop-down-Pfeil** rechts neben dem Spaltennamen.
2. Gehen Sie auf **Standardwert festlegen**.
3. Wenn Sie auf **Text bearbeiten** klicken, öffnet sich der Editor, wo Sie den Text verfassen können, der als Standardwert dienen soll.

## Einschränkungen bei Filtern, Sortierung und Gruppierung

Es ist nicht möglich, die Einträge in einer Tabelle nach formatierten Text-Spalten zu sortieren oder zu gruppieren. Bei Filtern haben Sie lediglich die Optionen "ist leer" und "ist nicht leer" zur Auswahl.