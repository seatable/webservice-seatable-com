---
title: 'Die Rollup-Formel'
date: 2023-01-24
lastmod: '2023-01-24'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/de/hilfe/die-rollup-formel'
seo:
    title: 'SeaTable Rollup-Formel: Zahlenbeziehungen & Auswertungen'
    description: 'So nutzen Sie die Rollup-Formel: Mehrere Werte verknüpfen, Summen, Durchschnitt, Min/Max oder Verkettung berechnen – inklusive Formatoptionen.'
---

Mithilfe der Rollup-Formel des Spaltentyps **Formel für Verknüpfungen** können Sie mehrere Zahlenwerte einer verknüpften Spalte zueinander ins Verhältnis setzen und einfache statistische Berechnungen durchführen.

## Anwendungsbereich der Rollup-Formel

Mit der **Rollup-Formel** ist es möglich, Relationen zwischen Zahlenwerten zu ermitteln. Beispielsweise können Sie bei der Haushaltsplanung die Ausgaben einer Kategorie **summieren**, den ausgegebenen **Maximal-** oder **Minimal-Wert** oder auch den **Durchschnitt** berechnen.

Zunächst brauchen Sie eine Spalte des Typs [Verknüpfung zu anderen Einträgen]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Stellen Sie dabei sicher, dass die Option **Verknüpfungen zu mehreren Zeilen erlauben** aktiviert ist, denn nur so können Sie Relationen zwischen Zahlen bestimmen.

![Die Rollup-Formel](images/rollup-1.png)

Die Spalte **Formel für Verlinkung** zeigt Ihnen dann mithilfe der Rollup-Formel die ausgewählte Relation der Zahlenwerte innerhalb der Verknüpfungsspalte an. In diesem Beispiel haben wir die Auswertungsmethode **Summe** gewählt:

![Die Rollup-Formel](images/rollup-2-1.png)

## Eine Tabellenverknüpfung hinzufügen

Lesen Sie im Artikel im Artikel über die [Verknüpfungsspalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), wie Sie eine Spalte des Typs **Verknüpfung zu anderen Einträgen** erstellen. Dies ist Grundvoraussetzung, um die Rollup-Formel verwenden zu können.

Die Verwendung der Rollup-Formel ergibt nur Sinn, wenn Sie die Option **Verknüpfung zu mehreren Zeilen erlauben** bei der Erstellung einer Verknüpfungsspalte aktivieren. Wäre die Option ausgeschaltet, würde in dem Feld der Rollup-Formel immer der gleiche Wert der Verknüpfungsspalte stehen.

## Eine Spalte mit der Rollup-Formel anlegen

![Die Rollup-Formel.](images/rollup-Formel.gif)

1. Erstellen Sie eine neue Spalte des Typs **Formel für Verknüpfungen**.
2. Legen Sie als Formel die Option **Rollup** fest.
3. Wählen Sie die **Verknüpfungsspalte** aus, die auf die gewünschte Tabelle verlinkt.
4. Entscheiden Sie nun im Feld **Zusammenzufassende Spalte in der verknüpften Tabelle auswählen**, welche Spalte aus der gewünschten Tabelle Sie verknüpfen und auswerten möchten.
5. Legen Sie die **Auswertungsmethode** fest. Sie haben Durchschnitt, Minimum, Maximum, Summe und Verkettung zur Auswahl.
6. Klicken Sie auf **Abschicken**.

## Formateinstellungen

Sie können das **Format**, in dem die Zahlenwerte angezeigt werden, genau definieren. Klicken Sie hierzu auf das dreieckige **Drop-down-Symbol** der "Formel für Verknüpfungen"-Spalte und wählen Sie die Option **Formateinstellungen**. Neben Zahlen können Sie auch **Währungen**, **Prozent** und **Dauer** als Format nehmen.
