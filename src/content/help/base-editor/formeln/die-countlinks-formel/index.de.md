---
title: 'Die Countlinks-Formel'
date: 2023-01-11
lastmod: '2023-01-24'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/de/hilfe/die-countlinks-formel'
seo:
    title: 'Countlinks-Formel in SeaTable: Verknüpfungen zählen'
    description: 'Mit Countlinks zählen Sie automatisch die verknüpften Einträge einer Spalte. Ideal für Teilnehmerlisten, Querverweise oder jede Form von Mehrfachverknüpfung.'

---

Die Countlinks-Formel zählt die Anzahl der verknüpften Einträge des Spaltentyps **Verknüpfung zu anderen Einträgen** in der jeweiligen Zeile.

{{< warning  type="warning" headline="Tabellenverknüpfung ist Grundvoraussetzung" >}}

Sie können nur dann eine Spalte mit der Countlinks-Formel anlegen, wenn Sie zwei Tabellen miteinander verknüpft haben. Lesen Sie [hier, wie Sie eine solche Verknüpfung anlegen]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

{{< /warning >}}

## Anwendungsbereich der Countlinks-Formel

Die **Countlinks-Formel** sollte immer dann zur Anwendung kommen, wenn Sie als Querverweis die **Anzahl von Einträgen** einer anderen Tabelle anzeigen möchten.

Beispielsweise können Sie so bei einer Workshop-Planung die Anzahl angemeldeter Teilnehmer aus einer separaten Tabelle abbilden. Die [Verknüpfungsspalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) würde somit die Namen aller Teilnehmer festhalten.

![Die Countlinks-Formel.](images/countlinks-2.png)

Die Verwendung der Countlinks-Formel ergibt nur Sinn, wenn Sie die Option **Verknüpfung zu mehreren Zeilen erlauben** bei der Erstellung einer Spalte des Typs **Verknüpfung zu anderen Einträgen** aktivieren. Wäre die Option ausgeschaltet, würde im Feld der Countlinks-Formel immer eine Eins stehen.

## Erstellen einer Countlinks-Formel

![Die Countlinks-Formel.](images/countlink.gif)

1. Erstellen Sie eine neue Spalte des Typs **Formel für Verknüpfungen**.
2. Geben Sie der Spalte einen passenden **Namen**.
3. Legen Sie als Formel die Option **Countlinks** fest.
4. Wählen Sie nun im Feld **Verknüpfungsspalte in dieser Tabelle auswählen** die Verknüpfungsspalte aus, deren Einträge Sie zählen möchten.
5. Klicken Sie auf **Abschicken**.
