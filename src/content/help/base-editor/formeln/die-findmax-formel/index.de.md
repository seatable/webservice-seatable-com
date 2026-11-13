---
title: 'Die Findmax-Formel'
date: 2023-02-13
lastmod: '2026-11-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/de/hilfe/die-findmax-formel'
seo:
    title: 'Die Findmax-Formel von SeaTable: Maximalwerte aus Verknüpfungen bestimmen'
    description: 'Lernen Sie, wie Sie mit der Findmax-Formel in SeaTable den größten Wert aus mehreren verknüpften Einträgen ziehen – mit Praxisbeispielen & mehr.'
---

Die **Findmax-Formel** sucht unter den Einträgen der verknüpften Spalte den **Maximalwert** und gibt diesen wieder. Dies ist nützlich, wenn es in der verknüpften Tabelle **mehrere Einträge** gibt, die sich auf denselben Datensatz (z. B. einer Person oder Kategorie) in einer anderen Tabelle beziehen.

## Wofür Sie die Findmax-Formel nutzen können

Die Findmax-Formel können Sie bei allen alphanumerischen Werten zur Bestimmung des **Maximalwerts** verwenden. Nehmen wir an, Sie verwenden SeaTable zur [Budgetplanung]({{< relref "templates/finance/budget-plan" >}}), wobei in einer Tabelle die Ausgaben und in einer anderen Tabelle die Kategorien gespeichert sind. Jede Ausgabe können Sie dann mit einer Kategorie verknüpfen. Um nun festzustellen, was **die höchste Ausgabe pro Kategorie** war, können Sie mithilfe der **Findmax-Formel** den größten Wert aus den gesamten verknüpften Ausgaben darstellen.

![findmax-Formel](images/findmax.png)

## So verwenden Sie die Findmax-Formel

### Eine Tabellenverknüpfung hinzufügen

Informieren Sie sich im Artikel über die [Verknüpfungsspalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), wie Sie eine Spalte des Typs **Verknüpfung zu anderen Einträgen** erstellen. Dies ist eine Grundvoraussetzung, um die Findmax-Formel verwenden zu können.

{{< warning headline="Mehrere verknüpfte Zeilen notwendig" >}}

Die Verwendung der Findmax-Formel ergibt nur Sinn, wenn die Option **Verknüpfung auf maximal eine Zeile beschränken** in den Einstellungen einer Verknüpfungsspalte deaktiviert ist. Wäre die Option eingeschaltet, würde die Findmax-Formel immer den gleichen Wert wie in der einzigen verknüpften Zeile anzeigen.

{{< /warning >}}

### Eine Spalte mit Findmax-Formel hinzufügen

![findmax-Formel](images/findmax.gif)

1. Erstellen Sie eine neue Spalte des Typs **Formel für Verknüpfungen**.
2. Legen Sie als Formel die Option **Findmax** fest.
3. Wählen Sie die zuvor erstellte Spalte des Typs **Verknüpfung zu anderen Einträgen** in dieser Tabelle aus.
4. Legen Sie nun die **Nachschlagespalte in der verknüpften Tabelle** fest, die in der Findmax-Spalte den Datensatz mit dem Maximalwert anzeigen soll.
5. Wählen Sie die **Größenvergleichsspalte in der verknüpften Tabelle** aus, in der Sie den Maximalwert bestimmen wollen.
6. Klicken Sie auf **Abschicken**.
