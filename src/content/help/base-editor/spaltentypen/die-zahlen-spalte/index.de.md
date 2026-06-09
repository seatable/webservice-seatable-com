---
title: 'Die Zahlen-Spalte'
date: 2023-01-08
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'ssc'
url: '/de/hilfe/die-zahlen-spalte'
seo:
    title: 'Die Zahlen‑Spalte in SeaTable – Formate & Funktionen'
    description: 'Nutzen Sie die Zahlen‑Spalte für Summen, Prozent, Währungen und Validierung. Formate und praxisnahe Tipps zur richtigen Anwendung in SeaTable. '
weight: 3
---

In SeaTable können Sie die **Zahlen-Spalte** vielseitig nutzen, um mit Zahlen jeder Art zu arbeiten, z. B. Anzahl von Gegenständen, prozentuale Anteile oder Preise in verschiedenen Währungen.

## Anwendungsgebiet der Zahlen-Spalte

Die Verwendung von **Zahlen-Spalten** ermöglicht Ihnen beispielsweise die **Berechnung von Werten** mit Formeln und die Erstellung anschaulicher **Diagramme und Statistiken**. Allerdings eignet sie sich nicht zum Speichern beliebig langer Zeichenfolgen (z. B. Kontonummern), da bei über 15 Ziffern gerundet wird. In diesem Fall sollten Sie die [Text-Spalte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}) verwenden.

Darüber hinaus bietet SeaTable andere Spaltentypen an, die manchmal besser zu den zu speichernden Werten passen:

- Dauer und Zeiträume = [Dauer-Spalte]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})
- Datum und Zeitpunkte = [Datum-Spalte]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- Punktzahlen = [Rating-Spalte]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})
- Seriennummern = [Automatische Nummer]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- Telefonnummern = [Telefonnummer-Spalte]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})
- Geo-Informationen = [Geopositions-Spalte]({{< relref "help/base-editor/spaltentypen/die-geopositions-spalte" >}})

## Hinzufügen einer Zahlen-Spalte

![Hinzufügen einer Zahlenspalte](images/hinzufuegen-einer-zahlenspalte.gif)

1. Klicken Sie auf das **Plus-Symbol** rechts neben der letzten Spalte.
2. Geben Sie der Spalte einen **Namen**.
3. Wählen Sie als Spaltentyp **Zahl** aus.
4. Entscheiden Sie sich für ein **Format** (z. B. Zahl, Prozent oder Währung).
5. Mit einem Klick auf **Weitere Einstellungen** können Sie zudem noch Details einstellen.
6. Fügen Sie die Spalte mit **Abschicken** hinzu.

## Formateinstellungen

Das **Zahlenformat** können Sie auch im Nachhinein bearbeiten und feinjustieren. Öffnen Sie hierzu zunächst das Drop-down-Menü mit den **Spalten-Optionen** über das Dreieck {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} im Spaltenkopf und klicken Sie im Anschluss auf {{< seatable-icon icon="dtable-icon-set-up" color="grey" >}} **Formateinstellungen**.

Sie können nun ein anderes **Format** auswählen, **Dezimal-** und **Tausendertrennzeichen** einstellen sowie die Anzahl der **Nachkommastellen** ändern.

### Verfügbare Formate der Zahlen-Spalte

Folgende Zahlenformate stehen Ihnen zur Verfügung:

- **Zahl**

    Verwendung einer einfachen Zahl, beispielsweise für die Anzahl von Gegenständen.

- **Prozent**

    Verwendung von Prozentangaben, beispielsweise für den Fortschritt in der Bearbeitung von Aufgaben.

- **Währungen (Yuan, Dollar & Euro)**

    Verwendung von verschiedenen Währungen, beispielsweise für die Preise von Produkten.

- **Benutzerdefinierte Währung**

    Verwendung einer benutzerdefinierten Währung, bei der das Währungssymbol individuell eingegeben werden kann.

## Standardwert festlegen und Eingabe validieren

Sie können für jede Zahlen-Spalte einen [Standardwert festlegen]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}), der automatisch in jede Zeile eingetragen wird, die Sie Ihrer Tabelle neu hinzufügen.

Um **Fehler** und **Extremwerte** direkt zu identifizieren, können Sie zudem die **Eingabe validieren**. Dazu definieren Sie einen **Zahlenbereich**, in dem die Werte der Spalte liegen sollten; Zellen mit einem höheren oder niedrigeren Wert werden dann farblich hervorgehoben.

Sie können diese Einstellungen beim Anlegen der Zahlen-Spalte oder im Nachhinein vornehmen:

1. Öffnen Sie das Drop-down-Menü mit den **Spalten-Optionen** über das Dreieck {{< seatable-icon icon="dtable-icon-drop-down" color="grey" >}} im Spaltenkopf.
2. Klicken Sie im Anschluss auf **Spaltentyp anpassen**.
3. Klicken Sie auf **Weitere Einstellungen** und aktivieren Sie ganz unten die entsprechenden **Regler**.

![Format settings of number columns](images/Format-settings-of-number-columns.png)
