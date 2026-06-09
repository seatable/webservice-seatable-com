---
title: 'Die Status-Zeile und ihre Funktionen'
date: 2023-02-21
lastmod: '2023-02-21'
categories:
    - 'ansichtsoptionen'
author: 'nsc2'
url: '/de/hilfe/die-status-zeile-und-ihre-funktionen'
seo:
    title: 'Status‑Zeile in SeaTable – zählen & berechnen leicht erklärt'
    description: 'Erfahren Sie, wie die Status‑Zeile funktioniert: Zeilenzählung, Berechnung von Summen, Durchschnitten und weiteren Werten pro Spalte.'
weight: 30
---

Die **Status-Zeile** befindet sich am unteren Rand Ihrer Tabellen und erfüllt grundsätzlich zwei verschiedene Funktionen, die in diesem Artikel näher erläutert werden:

- **Funktion 1**: Zählen der Zeilen in einer Ansicht
- **Funktion 2**: Angabe eines aus allen Einträgen berechneten Werts (z. B. Summe, Durchschnitt etc.) bei zahlenbasierten Spalten

Dank der Status-Zeile haben Sie diese **statistischen Basiswerte** immer im Blick, sobald Sie eine Tabelle geöffnet haben.

## Zählen der Zeilen in einer Ansicht

Die Status-Zeile gibt am unteren linken Rand die Anzahl aller **Zeilen** an, die sich in der aktuell geöffneten **Tabellenansicht** befinden. Wenn Sie [in einer Ansicht filtern]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}), zählt die Status-Zeile nur die verbliebenen Tabelleneinträge.

![Die Status-Zeile gibt stets die Anzahl der Zeilen in der aktuell geöffneten Tabellenansicht an](images/status-cell-function-1.jpg)

Zudem können Sie einzelne [Zeilen selektieren]({{< relref "help/base-editor/zeilen/mehrere-zeilen-selektieren" >}}) – dann bezieht sich die Status-Zeile nur auf die ausgewählten Einträge.

## Angabe eines aus allen Einträgen berechneten Werts

Bei **zahlenbasierten Spalten** gibt die Status-Zeile für jede Spalte einen aus allen Einträgen berechneten **Wert** an.

![Berechnete Werte in den Status-Zeilen](images/the-status-cell-function-2-1.png)

## Berechnungsoptionen

Für zahlenbasierte Spalten stehen in der Status-Zeile folgende **Berechnungsoptionen** zur Verfügung:

- Berechnung der **Summe** aus allen Einträgen der Spalte
- Berechnung des **Durchschnittswerts** aus allen Einträgen der Spalte
- Berechnung des **Medians** aus allen Einträgen der Spalte
- Ermittlung des **maximalen Werts** aus allen Einträgen der Spalte
- Ermittlung des **minimalen Werts** aus allen Einträgen der Spalte
- Keine Berechnung

![Berechnungsoptionen der Status-Zeile](images/berechnungsoptionen-status-zeile.png)

## Kompatible Spaltentypen und Formate

Bei den folgenden Spaltentypen gibt die Status-Zeile einen berechneten Wert wieder:

- [Zahlen-Spalten]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}})
    - Zahl
    - Prozent
    - Währung
- [Dauer-Spalten]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}})
- [Rating-Spalten]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}})
- Zahlenwerte in [Formel-Spalten]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})

Bei den folgenden Spaltentypen gibt die Status-Zeile **keinen** berechneten Wert wieder, obwohl sie Zahlen enthalten (können):

- [Datum-Spalten]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}})
- [Erstellt]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) und [Zuletzt bearbeitet]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})
- [Automatische Nummer]({{< relref "help/base-editor/spaltentypen/der-spaltentyp-automatische-nummer" >}})
- Zahlen in [Text-Spalten]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})
