---
title: 'Die Findmin-Formel'
date: 2023-02-13
lastmod: '2023-02-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/de/hilfe/die-findmin-formel'
seo:
    title: 'Findmin‑Formel in SeaTable – kleinsten Wert ermitteln'
    description: 'Mit der Findmin‑Formel finden Sie den Minimalwert aus verknüpften Einträgen. Ideal für Analysen über mehrere Tabellen und numerische Werte.'
---

Die **Findmin-Formel** sucht unter den Einträgen einer verknüpften Spalte den **Minimalwert** und gibt diesen wieder. Dies ist nützlich, wenn es in der verknüpften Tabelle **mehrere Einträge** gibt, die sich auf denselben Datensatz (z. B. einer Person) in einer anderen Tabelle beziehen.

Die Findmin-Formel funktioniert ausschließlich mit **Zahlenwerten**, weshalb der Inhalt der verknüpften Spalte auch aus Zahlenwerten bestehen muss. Zudem ergibt die Verwendung der Findmin-Formel nur Sinn, wenn der Regler **Verknüpfung zu mehreren Zeilen erlauben** bei der Erstellung der Spalte **Verknüpfung zu anderen Einträgen** aktiviert ist. Wäre die Option aus, würde bei der Findmin-Formel immer die gleiche Zahl stehen wie in der verknüpften Spalte.

## Wofür Sie die Findmin-Formel brauchen

Die **Findmin-Funktion** sollte zum Einsatz kommen, wenn Sie **Querverweise** zu numerischen Werten herstellen möchten, die in verschiedenen Tabellen gespeichert sind. Nehmen wir an, Sie verwenden SeaTable zur Sammlung der **Arbeitszeiten** Ihrer Mitarbeiter, wobei in einer Tabelle die Mitarbeiter und in einer anderen Tabelle die tägliche Aktivität gespeichert sind. Jeden Mitarbeiter-Datensatz können Sie dann mit den eingetragenen Arbeitszeiten verknüpfen.

![findmin-Formel](images/findmax-1.png)

Um festzustellen, wann sich ein Mitarbeiter das erste Mal eingeloggt hat, können Sie mithilfe der **Findmin-Formel** den **kleinsten Wert** – in diesem Fall den ersten Login – aus den gesamten Login-Zeiten in einer Spalte darstellen.

![findmin-Formel](images/findmin.png)

Die Findmin-Formel können Sie bei allen numerischen Werten zur Darstellung des **Minimalwerts** verwenden.

## So verwenden Sie die Findmin-Formel

### Eine Tabellenverknüpfung hinzufügen

Informieren Sie sich im Artikel über die [Verknüpfungsspalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), wie Sie eine Spalte des Typs **Verknüpfung zu anderen Einträgen** erstellen. Dies ist eine Grundvoraussetzung, um die Findmin-Formel nutzen zu können.

### Eine Spalte mit Findmin-Formel hinzufügen

![findmin-Formel](images/findmin.gif)

1. Erstellen Sie eine neue Spalte des Typs **Formel für Verknüpfungen**.
2. Legen Sie als Formel die Option **Findmin** fest.
3. Wählen Sie die zuvor erstellte Spalte des Typs **Verknüpfung zu anderen Einträgen** in dieser Tabelle aus.
4. Legen Sie nun im Feld **Nachschlagespalte in der verknüpften Tabelle "..." auswählen** die Spalte aus der anderen Tabelle fest, die Sie mit der hiesigen Spalte verknüpfen möchten.
5. Klicken Sie auf **Abschicken**.

{{< warning  type="warning" headline="Achtung"  text="Die Findmin-Formel funktioniert ausschließlich mit **numerischen Werten**, weshalb die verknüpfte Spalte Zahlenwerte enthalten muss." />}}
