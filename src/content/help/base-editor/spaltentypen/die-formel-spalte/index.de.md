---
title: 'Die Formel-Spalte'
date: 2023-01-28
lastmod: '2023-09-14'
categories:
    - 'formeln'
author: 'ssc'
url: '/de/hilfe/die-formel-spalte'
aliases: 
    - '/de/hilfe/grundlagen-von-seatable-formeln'
seo:
    title: 'Die Formel-Spalte in SeaTable effektiv nutzen'
    description: 'Mit der Formel-Spalte Werte in einer Zeile berechnen, Text zusammenfassen oder Funktionen flexibel nutzen – so geht’s!'
weight: 17
---

SeaTable bietet Ihnen viele verschiedene Funktionen, die Sie zu Ihrer Tabelle hinzufügen können. Eine davon ist die sogenannte **Formel-Spalte**. Mithilfe von Formeln können Sie Werte von unterschiedlichen Spalten verknüpfen und basierend auf den Datentypen dieser Spalten verschiedene Funktionen erstellen. Sie können unter anderem mit Werten in einer Zeile rechnen, sie zusammenführen oder miteinander in Beziehung setzen.

{{< warning  type="warning" headline="SeaTable erlaubt keine freie Referenzierung wie in Excel"  text="In Excel kann man in einer Formel jede beliebige Zelle ansprechen. In SeaTable ist dies **nicht** möglich. Eine Formel kann immer nur mit den **Werten aus der gleichen Zeile** arbeiten." />}}

## Anlegen einer Formel-Spalte

Um eine Formel anzuwenden, müssen Sie zunächst eine neue Formel-Spalte zu Ihrer Tabelle hinzufügen. Wie das geht, erfahren Sie [hier]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![Auswahl einer Formelspalte](images/select-formula-column.png)

SeaTable bietet Ihnen einen **Formeleditor**, um Ihnen die Eingabe von Formeln zu erleichtern.

![Formel-Wizard zur Vereinfachung der Eingabe von vor allem komplexen Formeln](images/Formula.wizard.png)

## Eine erste Formel schreiben

Sobald Ihre Formel-Spalte angelegt ist, können Sie mit dem Schreiben der Formel beginnen. Die folgende Abbildung zeigt eine einfache Formel, um den Durchschnitt von fünf Zahlen zu berechnen.

![Eingabe einer beliebigen Formel in das Textfeld](images/input-formular.jpg)

Diese Formel schreibt als Ergebnis immer den statischen Wert _13.2_ in die Formel-Spalte. Die wahre Stärke der Formel-Spalte kommt aber erst zur Geltung, wenn Sie die Werte anderer Spalten für Ihre Formel nutzen. Mit dem **{Spaltennamen}** in geschweiften Klammern können Sie auf bestehende Spalten in Ihrer Tabelle referenzieren.

{{< warning headline="Spalten der Formel hinzufügen" text="Die Spaltennamen in der geöffneten Tabelle werden links im Formeleditor angezeigt und können mit einem **Doppelklick** in die Formel eingefügt werden." />}}

![Spalten, die im Formeleditor zur Auswahl stehen](images/columns-in-the-formula-editor.jpg)

Anschließend können Sie bestimmte **Konstanten**, **Operanden** und **Funktionen** in Ihre Formel einfügen, um mit den Werten der verschiedenen Spalten zu rechnen, sie zusammenzuführen oder in Beziehung zu setzen.

## Klare Farbsprache

Um die verschiedenen Elemente Ihrer Formel voneinander unterscheiden zu können, werden diese je nach Typ in einer unterschiedlichen **Farbe** markiert:

| Objekt            | Example                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| Funktionen        | ![Functions are always marked blue in a formula](images/example-function.png)                       |
| Text / String     | ![Texts and strings are always marked in red in the formula editor](images/example-text.png)        |
| Zahlen            | ![Numbers are always highlighted in green in the formula editor](images/example-number.png)         |
| Spaltenreferenzen | ![Column references are always marked purple in a formula ](images/example-reference-to-column.png) |

{{< warning headline="Zusammengehörende Klammern werden hervorgehoben" >}}

Wenn Sie im Formeleditor auf eine öffnende oder schließende Klammer klicken, wird die dazugehörige Klammer ebenfalls hervorgehoben. So können Sie einfacher fehlende oder falsche Klammersetzungen erkennen.

![Öffnende und schließende Klammern werden im Formeleditor immer hervorgehoben](images/example-brackets.png)

{{< /warning >}}

## Formelbeispiele

Im Folgenden finden Sie ein paar Beispiele, die den Nutzen und die Nutzung von Formeln verdeutlichen.

- [Formelbeispiel: Einfache Multiplikation mit einer Formel]({{< relref "help/base-editor/formeln/formelbeispiel-einfache-multiplikation-mit-einer-formel" >}})
- [Formelbeispiel: Zusammenführen von Text-Spalten mit Hilfe einer Formel]({{< relref "help/base-editor/formeln/formelbeispiel-zusammenfuehren-von-text-spalten-mit-hilfe-einer-formel" >}})
- [Formelbeispiel: Logische If-Operatoren zum Vergleichen von Werten]({{< relref "help/base-editor/formeln/formelbeispiel-logische-if-operatoren-zum-vergleichen-von-werten" >}})
- [Formelbeispiel: Berechne die Dauer eines Urlaubs]({{< relref "help/base-editor/formeln/formelbeispiel-berechne-die-dauer-eines-urlaubs" >}})
- [Formelbeispiel: Berechne Tage bis zu einem Event]({{< relref "help/base-editor/formeln/formelbeispiel-berechne-tage-bis-zu-einem-event" >}})
- [Formelbeispiel: Nach einem Wort in einem Text suchen]({{< relref "help/base-editor/formeln/formelbeispiel-nach-einem-wort-in-einem-text-suchen" >}})

## Mathematische Konventionen gelten auch in SeaTable

Selbstverständlich können Sie sich darauf verlassen, dass mathematische Konventionen auch in den Formeln von SeaTable Ihre Anwendung finden. Hier die wichtigsten Beispiele:

- **Funktionen** können Sie mit Klammern ineinander **verschachteln**. Beispiel: (( 1 + 2 ) \* 3)
- **Punkt vor Strich**, die **Reihenfolge von Klammern** und andere **mathematische Regeln** werden in SeaTable berücksichtigt.

## Formatierung der Formel-Spalte

Die Ergebnisse in der Formel-Spalte können Sie formatieren. Jede Formel in SeaTable hat eine **Zahl**, ein **Datum** oder einen **Text/String** als Ergebnis. Je nachdem stehen Ihnen daher unterschiedliche **Formateinstellungen** zur Verfügung.

![Formatierung von Formelergebnissen](images/Formatierung-von-Formelergebnissen.jpg)
