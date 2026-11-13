---
title: 'Die Rollup-Formel'
date: 2023-01-24
lastmod: '2026-11-12'
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

Mit der **Rollup-Formel** ist es möglich, Relationen zwischen Zahlenwerten zu ermitteln. Beispielsweise können Sie bei der [Budgetplanung]({{< relref "templates/finance/budget-plan" >}}) die Ausgaben einer Kategorie **summieren**, den ausgegebenen **Maximal-** oder **Minimal-Wert** oder auch den **Durchschnitt** berechnen.

Zunächst brauchen Sie eine Spalte des Typs [Verknüpfung zu anderen Einträgen]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Stellen Sie dabei sicher, dass die Option **Verknüpfung auf maximal eine Zeile beschränken** deaktiviert ist, denn nur so können Sie mehrere Zeilen verknüpfen.

Die Spalte [Formel für Verknüpfungen]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}}) zeigt Ihnen dann mithilfe der Rollup-Formel die ausgewählte Relation der Zahlenwerte innerhalb der Verknüpfungsspalte an. In diesem Beispiel haben wir die Auswertungsmethode **Summe** gewählt:

![Die Rollup-Formel](images/rollup-formel.png)

## Eine Spalte mit der Rollup-Formel anlegen

Lesen Sie im Artikel über die [Verknüpfungsspalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), wie Sie eine Spalte des Typs **Verknüpfung zu anderen Einträgen** erstellen. Dies ist Grundvoraussetzung, um die Rollup-Formel verwenden zu können.

{{< warning headline="Mehrere verknüpfte Zeilen notwendig" >}}

Die Verwendung der Rollup-Formel ergibt nur Sinn, wenn die Option **Verknüpfung auf maximal eine Zeile beschränken** in den Einstellungen einer Verknüpfungsspalte deaktiviert ist. Wäre die Option eingeschaltet, würde die Rollup-Formel immer den gleichen Wert wie in der einzigen verknüpften Zeile anzeigen.

{{< /warning >}}

![Die Rollup-Formel](images/rollup-formel.gif)

1. Erstellen Sie eine neue Spalte des Typs **Formel für Verknüpfungen**.
2. Legen Sie als Formel die Option **Rollup** fest.
3. Wählen Sie die **Verknüpfungsspalte** aus, die auf die gewünschte Tabelle verlinkt.
4. Entscheiden Sie nun im Feld **Zusammenzufassende Spalte in der verknüpften Tabelle auswählen**, welche Spalte aus der gewünschten Tabelle Sie verknüpfen und auswerten möchten.
5. Legen Sie die **Auswertungsmethode** fest. Sie haben Durchschnitt, Minimum, Maximum, Summe und Verkettung zur Auswahl.
6. Klicken Sie auf **Abschicken**.

## Formateinstellungen

Sie können das **Format**, in dem die Zahlenwerte angezeigt werden, genau definieren. Klicken Sie hierzu auf das dreieckige **Drop-down-Symbol** der Rollup-Spalte und wählen Sie die Option **Formateinstellungen**. Neben Zahlen können Sie auch **Währungen**, **Prozent** und **Dauer** als Format nehmen. Zudem lassen sich **Dezimal- und Tausendertrennzeichen** sowie **Nachkommastellen** festlegen.

## Nachträgliche Änderungen

Natürlich können Sie die Rollup-Formel nachträglich anpassen, zum Beispiel die Auswertungsmethode von Summe auf Durchschnitt ändern. Klicken Sie auf das dreieckige **Drop-down-Symbol** rechts neben dem Spaltennamen und dann auf **Spaltentyp anpassen**. Dort gelangen Sie zu denselben Einstellungen wie beim Erstellen der Spalte.