---
title: 'Unterschiede zwischen Formeln in Excel und SeaTable'
date: 2023-02-03
lastmod: '2023-02-03'
categories:
    - 'formeln'
author: 'ssc'
url: '/de/hilfe/unterschiede-zwischen-formeln-in-excel-und-seatable'
seo:
    title: 'Unterschiede zwischen Formeln in Excel & SeaTable'
    description: 'Entdecken Sie die wichtigsten Unterschiede zwischen Excel-Formeln und SeaTable: Zellen‑ vs. Spalten‑Logik, Verweise und Tipps für Umsteiger.'
---

Sind Sie ein Excel-Benutzer, der mit dem Schreiben von Formeln vertraut ist und gerade erst mit SeaTable loslegt? Dann ist dieser Artikel genau das Richtige für Sie! Obwohl die Prinzipien der Formelfunktionen in SeaTable ähnlich sind, gibt es einige wichtige Unterschiede, die Sie zu Beginn lernen müssen und die sich auszahlen werden, wenn Sie ein Experte für SeaTable-Formeln werden möchten.

## Zentraler Unterschied

Den zentralen Unterschied in der Formelfunktion von SeaTable und Excel stellt der **Wirkungsbereich** der Formeln dar.

Während Sie in **Excel** in jede beliebige *Zelle* eine Formel eingeben können, die anschließend auf jede andere Zelle im Tabellenblatt verweisen kann, verweisen Formeln in **SeaTable** auf ganze *Spalten* und nicht auf bestimmte Zellen.

Da SeaTable in diesem Zusammenhang als eine [relationale Datenbank]({{< relref "posts/relationale-datenbank" >}}) fungiert, werden Formeln auf die gesamte _Spalte_ einer Tabelle angewendet, sodass für jeden Eintrag in dieser Spalte dieselbe Formel gilt.

## Zeilenreferenzierung

### Excel

Jede bestimmte Zelle kann in einer anderen Zelle referenziert werden. Um zum Beispiel die Quelle jedes Kaufs in einer Tabelle zu ermitteln, würden Sie eine Formel schreiben, die auf jede Zelle - wie A3 - verweist, um die Art der Quelle zu überprüfen.

Die dabei unten verwendete Formel lautet: **\= IF(A3 = "Online","Web","Store")**

![Zellenreferenzierung in Excel](images/table-excel-vs.-seatable-1.png)

Die Formel verweist auf bestimmte _Zellen_, wie z.B. A3.

### SeaTable

Eine Formel wird immer auf eine ganze _Spalte_ und **nicht** auf bestimmte Zellen angewendet. Um zum Beispiel die Quelle jedes Kaufs zu identifizieren, würden Sie eine Formel schreiben, die auf die Spalte {Purchase Type} verweist, und die Formel wird diese Spalte für jeden Eintrag in der Tabelle überprüfen.

Die dabei unten verwendete Formel lautet:

**IF({Purchase Type}= "Online","Web","Store")**

![Spaltenreferenzierung in SeaTable](images/table-excel-vs-seatable-2.png)

Die Formel verweist auf ganze _Spalten_, wie z.B. {Purchase Type}.

## Werte aus anderen Tabellen

SeaTable-Formeln funktionieren innerhalb von _Tabellen_, nicht über _Bases_ hinaus. Ähnlich wie oben beziehen sich SeaTable-Formeln standardmäßig nur auf _Spalten_ innerhalb derselben _Tabelle_. Es gibt jedoch auch Möglichkeiten, einen Wert aus einer anderen Tabelle zu übernehmen, um ihn in einem Formelfeld zu referenzieren. Dieser Ansatz verwendet verknüpfte Datensätze, die [hier]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) ausführlicher behandelt werden.

### Excel

Um auf einen Datensatz in einer anderen Tabelle zu verweisen, müssen Sie spezifische Verweise auf die andere Tabelle in einem Format wie beispielsweise dem folgenden schreiben:

**\=IF(Tasks!B1='Home improvements',Tasks!A1,0).**

Anschließend müssen Sie diese Formel auf jede Zelle anwenden, in der Sie die Formel ausführen möchten (wobei Sie die Zellverweise für jede Zelle ändern müssen, in der Sie die Formel ausführen möchten).

![Verweis auf anderen Datensatz in Excel](images/table-excel-vs-seatable-3.png)

### SeaTable

Um einen Datensatz in einer anderen Tabelle zu referenzieren, können Sie diese zunächst mithilfe des Spaltentyps **"Verknüpfung zu anderen Einträgen"** verknüpfen. Sobald ein Datensatz in einer Tabelle, z.B. "Projects", mit einem Datensatz in einer anderen Tabelle, z.B. "Tasks", verknüpft ist, können Sie auf jede Zeile in beiden Tabellen verweisen, indem Sie eine **lookup-**, **rollup-** oder **count-Spalte** verwenden.

Im folgenden Beispiel wird eine **Rollup-Spalte** verwendet, um auf einfache Weise auf die Kosten der einzelnen mit einem Projekt verbundenen Aufgaben zu verweisen und die Ausgaben zu summieren, um die Gesamtprojektkosten zu ermitteln.

![Rollup-Spalte zum Verweisen auf die Kosten der einzelnen mit einem Projekt verbundenen Aufgaben und zur Summierung der Ausgaben, um die Gesamtprojektkosten zu ermitteln.](images/reference-to-other-bases.gif)

Die Funktion schafft dabei eine Reihe von Möglichkeiten, sowohl einfache als auch komplexe Formeln zu schreiben, um Daten zwischen Tabellen zu referenzieren.
