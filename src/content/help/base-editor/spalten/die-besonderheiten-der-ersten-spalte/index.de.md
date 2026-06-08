---
title: 'Die Besonderheiten der ersten Spalte'
date: 2022-10-13
lastmod: '2024-03-15'
categories:
    - 'arbeiten-mit-spalten'
author: 'nsc2'
url: '/de/hilfe/die-besonderheiten-der-ersten-spalte'
seo:
    title: 'Die Besonderheiten der ersten Spalte in SeaTable erklärt'
    description: 'Erfahren Sie, was die erste Spalte von SeaTable besonders macht, wie Sie deren Typ anpassen und welche Einschränkungen oder Vorteile zu beachten sind.'
---

Die **erste Spalte** einer Tabelle weist in SeaTable im Vergleich zu den anderen Spalten mehrere Besonderheiten und Einschränkungen auf. Hier erfahren Sie, wie Sie die erste Spalte in SeaTable anpassen können.

## Die Besonderheiten der ersten Spalte in SeaTable

- Die erste Spalte einer Tabelle können Sie im Gegensatz zu den anderen Spalten **nicht ausblenden**.
- Die erste Spalte einer Tabelle können Sie im Gegensatz zu den anderen Spalten **nicht verschieben**.
- Die erste Spalte einer Tabelle können Sie im Gegensatz zu den anderen Spalten **nicht löschen**.
- Im Gegensatz zu den anderen Spalten können Sie die erste Spalte aber individuell **fixieren**.
- Für die **erste Spalte** stehen lediglich **sechs Spaltentypen** zur Auswahl:
  - [Text]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})
  - [Zahl]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
  - [Datum]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
  - [Einfachauswahl]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}})
  - [Automatische Nummer]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
  - [Formel]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

## Wie Sie den Typ der ersten Spalte anpassen

![Anpassen der ersten Spalte](images/change-the-first-column.gif)

1. Klicken Sie auf das dreieckige **Drop-down-Symbol** rechts neben dem Namen der ersten Spalte.
2. Gehen Sie auf **Spaltentyp anpassen**.
3. Klicken Sie in das **Feld** des aktuellen Spaltentyps.
4. Wählen Sie einen **neuen Spaltentyp** für die erste Spalte aus.
5. Nehmen Sie ggf. **Format-Einstellungen** vor.
6. Klicken Sie auf **Abschicken**.
7. Bestätigen Sie die Anpassung mit einem Klick auf **Konvertieren**.

## Formeln in der ersten Spalte

Wenn Sie als **erste Spalte** einer Tabelle eine **Formel** definieren, können Sie beispielsweise mit der simplen Formel **{column name}** die Einträge aus fast allen anderen Spalten Ihrer Tabelle **zitieren**. Das geht sogar, wenn der andere Spaltentyp **nicht** in der ersten Spalte unterstützt wird.

![Möglichkeiten mit dem Spaltentyp Formel in der ersten Spalte einer Tabelle](images/formular-in-the-first-column-1.png)

## Häufige Fragen

{{< faq "Welche Einschränkungen hat die erste Spalte?" >}}Die erste Spalte kann weder **ausgeblendet** noch **verschoben** noch **gelöscht** werden.
{{< /faq >}}
{{< faq "Kann man den Typ der ersten Spalte nachträglich ändern?" >}}Ja, dies ist möglich. In manchen Fällen kann es jedoch vorkommen, dass bei der [Änderung des Spaltentyps]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}}), beispielsweise von Text zu Zahl, Informationen **verloren gehen**. Prüfen Sie daher nach einer Konvertierung, ob alle Informationen korrekt und vollständig übernommen wurden.
{{< /faq >}}
{{< faq "Was ist eine automatische Nummer?" >}}Wenn Ihre Zeilen eine **eindeutige Identifikationsnummer** haben sollen, könnte der Spaltentyp [Automatische Nummer]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}}) Ihnen gute Dienste erweisen. Beispiele sind Rechnungsnummern, Testfälle oder Mitarbeiter-IDs. Die Nummer lässt sich zusätzlich um ein beliebiges Präfix ergänzen.

{{< /faq >}}
