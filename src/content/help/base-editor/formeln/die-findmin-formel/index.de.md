---
title: 'Die Findmin-Formel'
date: 2023-02-13
lastmod: '2026-11-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/de/hilfe/die-findmin-formel'
seo:
    title: 'Findmin‑Formel in SeaTable – kleinsten verknüpften Wert ermitteln'
    description: 'Mit der Findmin‑Formel finden Sie den Minimalwert aus verknüpften Einträgen. Ideal für Analysen über mehrere Tabellen und numerische Werte.'
---

Die **Findmin-Formel** sucht unter den Einträgen der verknüpften Spalte den **Minimalwert** und gibt diesen wieder. Dies ist nützlich, wenn es in der verknüpften Tabelle **mehrere Einträge** gibt, die sich auf denselben Datensatz (z. B. einer Person oder Kategorie) in einer anderen Tabelle beziehen.

## Wofür Sie die Findmin-Formel nutzen können

Die Findmin-Formel können Sie bei allen alphanumerischen Werten zur Bestimmung des **Minimalwerts** verwenden. Nehmen wir an, Sie verwenden SeaTable zur [Budgetplanung]({{< relref "templates/finance/budget-plan" >}}), wobei in einer Tabelle die Ausgaben und in einer anderen Tabelle die Kategorien gespeichert sind. Jede Ausgabe können Sie dann mit einer Kategorie verknüpfen. Um nun festzustellen, was **die niedrigste Ausgabe pro Kategorie** war, können Sie mithilfe der **Findmin-Formel** den kleinsten Wert aus den gesamten verknüpften Ausgaben darstellen.

![findmin-Formel](images/findmin.png)

## So verwenden Sie die Findmin-Formel

### Eine Tabellenverknüpfung hinzufügen

Informieren Sie sich im Artikel über die [Verknüpfungsspalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), wie Sie eine Spalte des Typs **Verknüpfung zu anderen Einträgen** erstellen. Dies ist eine Grundvoraussetzung, um die Findmin-Formel verwenden zu können.

{{< warning headline="Mehrere verknüpfte Zeilen notwendig" >}}

Die Verwendung der Findmin-Formel ergibt nur Sinn, wenn die Option **Verknüpfung auf maximal eine Zeile beschränken** in den Einstellungen einer Verknüpfungsspalte deaktiviert ist. Wäre die Option eingeschaltet, würde die Findmin-Formel immer den gleichen Wert wie in der einzigen verknüpften Zeile anzeigen.

{{< /warning >}}

### Eine Spalte mit Findmin-Formel hinzufügen

![findmin-Formel](images/findmin.gif)

1. Erstellen Sie eine neue Spalte des Typs **Formel für Verknüpfungen**.
2. Legen Sie als Formel die Option **Findmin** fest.
3. Wählen Sie die zuvor erstellte Spalte des Typs **Verknüpfung zu anderen Einträgen** in dieser Tabelle aus.
4. Legen Sie nun die **Nachschlagespalte in der verknüpften Tabelle** fest, die in der Findmin-Spalte den Datensatz mit dem Minimalwert anzeigen soll.
5. Wählen Sie die **Größenvergleichsspalte in der verknüpften Tabelle** aus, in der Sie den Minimalwert bestimmen wollen.
6. Klicken Sie auf **Abschicken**.
