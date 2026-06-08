---
title: 'Formelbeispiel: Zusammenführen von Text-Spalten mit Hilfe einer Formel'
date: 2023-01-28
lastmod: '2023-09-18'
categories:
    - 'formeln'
author: 'nsc2'
url: '/de/hilfe/formelbeispiel-zusammenfuehren-von-text-spalten-mit-hilfe-einer-formel'
seo:
    title: 'Formelbeispiel: Text-Spalten in SeaTable zusammenführen'
    description: 'Lernen Sie, wie Sie mit SeaTable-Formeln Inhalte mehrerer Text-Spalten einfach zu einem vollständigen Textstring kombinieren.'
---

SeaTable Formeln bieten Ihnen verschiedene Möglichkeiten, mit den Daten in Ihren Tabellen zu arbeiten. Eine davon ist das Zusammenführen von Inhalten aus verschiedenen [Text-Spalten]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}). Mithilfe einer entsprechenden Formel können Sie beliebig viele Inhalte aus unterschiedlichen Spalten in einer Formel-Spalte zusammenführen.

## Zusammenführen von Text-Spalten

Im konkreten Beispiel ist das Ziel, mithilfe einer Formel die Inhalte (Name, Vorname und Titel) der ersten drei Spalten zu einem **vollständigen Namen** zusammenzuführen.

![Beispiel-Tabelle für das Zusammenführen von verschiedenen Inhalten in eine Formel-Spalte](images/example-table-zusammenfuehren-von-inhalten-mit-Formel.png)

Hierfür fügen Sie der Tabelle zunächst eine **Formel-Spalte** hinzu, in deren Editor Sie anschließend die Formel einfügen können.

![Hinzufügen einer Formel in das hierfür vorgesehene Textfeld](images/insert-formular-example-1.png)

Um Inhalte aus verschiedenen Text-Spalten in einer Spalte zusammenzuführen, müssen Sie stets auf die **Namen der Spalten** verweisen, in denen die entsprechenden Inhalte in Ihrer Tabelle zu finden sind. Besonders wichtig ist dabei, dass die Spaltennamen mit **geschweiften Klammern** umrahmt sind, da SeaTable ansonsten **nicht** erkennen kann, welche Inhalte zusammengeführt werden sollen.

{{< warning  type="warning" headline="Tipp"  text="Die **Spaltennamen** in der geöffneten Tabelle werden Ihnen links im **Formeleditor** angezeigt und können mit einem **Doppelklick** in die Formel eingefügt werden." />}}

![Wenn Sie auf Spalten-Namen in Ihren Tabellen verweisen, umrahmen Sie diese stets mit geschweiften Klammern](images/verweis-auf-spaltennamen-in-formel-beispiel-2.png)

Um die Inhalte der Text-Spalten in einer Formel-Spalte zusammenzuführen, ordnen Sie die Spaltennamen zunächst in der gewünschten **Reihenfolge** in der Formel an und trennen diese jeweils mit einem **&-Symbol**, das Sie im Formeleditor bei den **Operanden** finden.

![Ordnen Sie die verschiedenen Spalten-Namen in gewünschter Reihenfolge in der Formel an und trennen Sie diese mit einem &-Symbol](images/insert-symbols.png)

Damit die verschiedenen Inhalte jeweils durch ein **Leerzeichen** getrennt werden, fügen Sie jeweils **hinter** den ersten beiden Spaltennamen zusätzlich noch ein **&-Symbol** und zwei **Anführungszeichen (oben)** hinzu.

![Hinzufügen eines zusätzlichen &-Symbols und zwei Anführungszeichen hinter die ersten beiden Spalten-Namen](images/insert-and-22-22-to-the-formular.png)

Nach Bestätigung der eingegebenen Formel werden die Inhalte der Text-Spalten automatisch zusammengeführt und das **Ergebnis** erscheint automatisch in der Formel-Spalte.

![Formel-Spalte nach der Bestätigung der eingegebenen Formel.](images/table-example-2-after-formular.png)

{{< warning  headline="Profi-Tipp" >}}

Immer wenn Sie Text-Spalten in einer Formel verwenden und diese Spalten auch leer sein können, empfiehlt sich der Einsatz der Funktion _trim( )_. Mit dieser werden Leerzeichen am Anfang und Ende eines Textes entfernt. Die komplette Formel lautet dann z. B.

```
trim( {Title} & " " & {Surname} & " " & {Name} )
```

{{< /warning >}}
