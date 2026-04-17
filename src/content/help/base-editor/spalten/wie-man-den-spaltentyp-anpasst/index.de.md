---
title: 'Wie man den Spaltentyp anpasst'
date: 2022-10-10
lastmod: '2024-03-15'
categories:
    - 'arbeiten-mit-spalten'
author: 'nsc2'
url: '/de/hilfe/wie-man-den-spaltentyp-anpasst'
seo:
    title: 'Spaltentyp in SeaTable flexibel ändern – so funktioniert es'
    description: 'Passen Sie den Spaltentyp nachträglich an: Spaltenmenü öffnen, neuen Typ auswählen und speichern. Warnhinweise erscheinen bei drohendem Datenverlust.'

---

Je nachdem, welche **Werte** Sie in SeaTable erfassen möchten, können Sie diesen verschiedene **Spaltentypen** zuordnen. Eine Übersicht über alle 26 Spaltentypen in SeaTable finden Sie [hier]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}
).

Es ist möglich, den Spaltentyp im Nachhinein noch zu ändern. Hier erfahren Sie, wie Sie den Spaltentyp **nachträglich anpassen** können.

## Wie Sie den Spaltentyp anpassen

![Wie man den Spaltentyp anpasst](images/how-to-costumize-a-coloumn-type.gif)

1. Klicken Sie auf das dreieckige **Drop-down-Symbol** {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} rechts neben dem Namen der Spalte, deren Typ Sie anpassen möchten.
2. Wählen Sie die Option **Spaltentyp anpassen**.
3. Weisen Sie der Spalte einen neuen **Spaltentyp** zu und nehmen Sie ggf. weitere spezifische **Einstellungen** vor.
4. Bestätigen Sie den Vorgang mit einem Klick auf **Abschicken**.

{{< warning  type="warning" headline="Hinweis"  text="Nicht alle Spaltentypen können Sie nachträglich anpassen. Beispielsweise sind die automatisch ausgefüllten Spaltentypen **Erstellt**, **Ersteller**, **Letzter Bearbeiter** und **Zuletzt bearbeitet** unveränderlich." />}}

## Anpassen der ersten Spalte

Die **erste Spalte** in einer Tabelle unterstützt **nur 6 der 26 Spaltentypen**. Diese sind:

- [Text]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}})
- [Zahl]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
- [Datum]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- [Einfachauswahl]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
- [Automatische Nummer]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- [Formel]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

## Warnung vor Datenverlust

Die **Konvertierung** von bestimmten Spaltentypen führt in der Regel zu unerwünschtem **Datenverlust**. Dies ist beispielsweise bei [Datei-]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) der Fall oder wenn Sie [Textspalten]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) in numerische Spalten umwandeln. SeaTable blendet Ihnen in diesen Fällen die **Warnmeldung** ein, ob Sie den Spaltentyp wirklich ändern möchten.
