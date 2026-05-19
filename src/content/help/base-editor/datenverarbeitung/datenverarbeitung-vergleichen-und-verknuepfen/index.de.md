---
title: 'Datenverarbeitung: Vergleichen und verknüpfen'
date: 2023-03-20
lastmod: '2023-03-20'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/de/hilfe/datenverarbeitung-vergleichen-und-verknuepfen'
seo:
    title: 'Daten vergleichen und verknüpfen in SeaTable'
    description: 'Verknüpfen Sie in SeaTable Datensätze automatisch über identische Spaltenwerte in zwei Tabellen mit einer einfachen Operation.'
---

Mithilfe der Datenverarbeitungsfunktion können Sie diverse Operationen über eine Spalte hinweg durchführen. **Vergleichen und verknüpfen** stellt dabei eine Operation dar, mit der Sie Datensätze in zwei verschiedenen Tabellen verlinken können, wenn ein Spaltenwert in beiden Tabellen identisch ist.

## Anlegen der Operation

![Anlegen einer Datenverarbeitungsaktion](images/create-an-data-processing-action-1.jpg)

1. Öffnen Sie eine beliebige **Tabelle** und klicken Sie auf die **drei Punkte** in den Ansichtsoptionen.
2. Klicken Sie auf **Datenverarbeitung** und im Anschluss auf **Datenverarbeitungsoperation hinzufügen**.
3. Geben Sie der Operation einen **Namen** und wählen Sie **Vergleichen und verknüpfen** aus.
   ![Benennung der Datenverarbeitungsaktion und Auswahl des Operationstyps](images/select-operation-type-example-compare-and-link.jpg)5. Definieren Sie **zwei Tabellen**, die Sie vergleichen und verknüpfen möchten, und in welchen **Spalten** die Werte übereinstimmen müssen, damit SeaTable die Datensätze miteinander verlinkt.
   ![Definition der Datenverarbeitungsaktion](images/name-and-define-data-operation-compare-and-link-1.png) {{< warning  headline="Hinweis"  text="Mithilfe eines Klicks auf **Hinzufügen** können Sie eine **beliebige Anzahl an Spalten** definieren, in denen die Werte übereinstimmen müssen." />}}9. Klicken Sie auf **Speichern**, um die Aktion zu speichern und später auszuführen, oder auf **Ausführen**, um die Aktion direkt auszuführen.
   Bei der ersten erfolgreichen Ausführung erscheint am unteren linken Rand ein kleiner **grüner Haken**. ![Bei erfolgreicher erster Ausführung der Datenverarbeitungsaktion erscheint ein grüner Haken](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Anwendungsfall

Ein konkreter Anwendungsfall für diese Datenverarbeitungs-operation könnte beispielsweise auftreten, wenn Sie in der Buchhaltung eines Unternehmens arbeiten und in zwei Tabellen einerseits die **Rechnungen** und andererseits die durchgeführten **Transaktionen** erfassen.

Hierbei möchten Sie, dass eine **Verlinkung** zwischen diesen Tabellen hergestellt wird, wenn der Rechnungsbetrag in der einen Tabelle mit dem Überweisungsbetrag in der anderen Tabelle übereinstimmt. Über die Verlinkung können Sie die zusammengehörigen Datensätze ganz einfach miteinander verknüpfen, sodass die Rechnungen den Überweisungen und die Überweisungen den Rechnungen zugeordnet sind.

Für die Umsetzung benötigen Sie zunächst zwei Tabellen: eine Tabelle, in der die Rechnungsnummern (**Invoice Nr**) und -beträge erfasst werden, und eine Tabelle mit den Transaktionsnummern (**Transaktion Nr**) und -beträgen (**Amount**).

![Beispieltabelle Rechnungen](images/table-invoices.png)

![Beispieltabelle Transaktionen](images/table-transactions.png)

{{< warning  type="warning" headline="Wichtiger Hinweis" >}}

Bei dieser Datenverarbeitungsoperation müssen Sie Ihren Tabellen **keine Spalten** manuell hinzufügen, da bei der ersten Ausführung automatisch eine [Verknüpfungsspalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) in beiden Tabellen angelegt wird.

{{< /warning >}}

Um die Datenverarbeitungsoperation anzulegen, befolgen Sie die oben beschriebenen Schritte. Für den konkreten Anwendungsfall wählen Sie dabei die **Tabellen** _Transactions_ und _Invoices_ sowie die _Amount_\-**Spalten** mit den jeweiligen Beträgen, die übereinstimmen müssen, damit die Datensätze miteinander verknüpft werden.

![Definition der Datenverarbeitungsaktion](images/name-and-define-data-operation-compare-and-link-1.png)

Bei erfolgreicher Ausführung werden die Tabellen _Transactions_ und _Invoices_ auf Übereinstimmungen in den definierten _Amount_\-Spalten untersucht. Stimmen dabei die **Beträge** in diesen Spalten überein, wird eine **Verknüpfung** zwischen den beiden **Tabellen** hergestellt.

In diesem Fall wird auf der einen Seite der entsprechenden **Rechnung** in der Tabelle _Invoices_ eine Verknüpfung mit der dazugehörigen **Transaktion** aus der Tabelle _Transactions_ hinzugefügt.

![Hinzugefügte Verlinkung in der Tabelle Invoices](images/table-invoices-after-operation.png)

Auf der anderen Seite wird gleichzeitig der entsprechenden **Transaktion** in der Tabelle _Transactions_ eine Verknüpfung mit der dazugehörigen **Rechnung** aus der Tabelle _Invoices_ hinzugefügt.

![Hinzugefügte Verlinkung in der Tabelle Transactions](images/table-transactions-after-operation.png)
