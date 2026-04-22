---
title: 'Datenverarbeitung: Vergleichen und kopieren'
date: 2023-03-17
lastmod: '2023-11-27'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/de/hilfe/datenverarbeitung-vergleichen-und-kopieren'
seo:
    title: 'Daten vergleichen und kopieren in SeaTable'
    description: 'Kopieren Sie mit einer Operation Werte aus einer Tabelle in eine andere, wenn Vergleichswerte übereinstimmen – einfach und sicher.'
---

Mithilfe der Datenverarbeitungsfunktion können Sie diverse Operationen über eine Spalte hinweg durchführen. **Vergleichen und kopieren** stellt dabei eine Operation dar, mit der Sie die Werte einer Spalte von einer Tabelle in die Spalte einer anderen Tabelle kopieren können, sofern ein bestimmter Vergleichswert in beiden Datensätzen identisch ist.

## Anlegen der Operation

![Anlegen einer Datenverarbeitungsaktion](images/create-an-data-processing-action-1.jpg)

1. Öffnen Sie eine beliebige **Tabelle** und klicken Sie auf die **drei Punkte** in den Ansichtsoptionen.
2. Klicken Sie auf **Datenverarbeitung** und im Anschluss auf **Datenverarbeitungsoperation hinzufügen**.
3. Geben Sie der Operation einen **Namen** und wählen Sie **Vergleichen und kopieren** aus.
   ![Benennung der Datenverarbeitungsaktion und Auswahl des Operationstyps](images/name-operation-and-select-operation-type-exmaple-copy.jpg)5. Definieren Sie, **aus welcher Tabelle** die Daten stammen und **in welche Tabelle** Sie die Daten kopieren möchten.
4. Legen Sie eine oder mehrere **Bedingungen** fest, in welchen zwei Spalten der verglichenen Tabellen ein Wert identisch sein muss, damit die Operation ausgeführt wird.
5. Wählen Sie eine oder mehrere **Quellspalten**, aus denen Werte in ebenfalls zu definierende **Ergebnisspalten** kopiert werden, sofern die von Ihnen festgelegten Übereinstimmungsbedingungen erfüllt sind.
   ![Definition der Datenverarbeitungsaktion](images/name-operation-and-define-columns-example-copy-1.png) {{< warning  headline="Hinweis"  text="Mit einem Klick auf **Hinzufügen** können Sie beliebig viele Spalten für weitere **Bedingungen** oder **Kopiervorgänge** auswählen." />}}12. Klicken Sie auf **Speichern**, um die Aktion zu speichern und später auszuführen, oder auf **Ausführen**, um die Aktion direkt auszuführen.
   Bei der ersten erfolgreichen Ausführung erscheint am unteren linken Rand ein kleiner **grüner Haken**. ![Bei erfolgreicher erster Ausführung der Datenverarbeitungsaktion erscheint ein grüner Haken](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Anwendungsfall

Ein konkreter Anwendungsfall für diese Datenverarbeitungs-operation könnte beispielsweise auftreten, wenn Sie die **Mitarbeiterdaten** Ihrer Teammitglieder in einer Tabelle pflegen und die noch zu erledigenden **Aufgaben Ihres Teams** in einer neuen Tabelle anlegen möchten. Durch Hinzufügen einer Spalte mit den **Namen** der für die jeweiligen Aufgaben zuständigen Mitarbeiter wollen Sie eine Übereinstimmung zwischen den Tabellen schaffen.

Anschließend möchten Sie, dass bestimmte Daten der Mitarbeiter, welche bereits in der Mitarbeiter-Tabelle vorhanden sind, in die Aufgaben-Tabelle kopiert werden. Beispielsweise könnten Sie dort auch die **E-Mail-Adresse** brauchen, um direkt Kontakt zur zuständigen Person aufnehmen zu können.

Zur Umsetzung dieser Datenverarbeitungsoperation benötigen Sie **zwei Tabellen in derselben Base**. In der ersten Tabelle werden die **Mitarbeiterdaten** gepflegt, zu denen unter anderem die **E-Mail-Adressen** der Mitarbeiter gehören.

![Beispiel-Tabelle für die Pflege von persönlichen Daten der Mtarbeiter](images/example-table-employees-and-personal-data-1.png)

In der zweiten Tabelle erfassen Sie die **offenen Aufgaben**, für die der jeweils zuständige Mitarbeiter in einer weiteren Spalte eingetragen wird. Außerdem legen Sie eine neue Spalte vom Typ [E-Mail]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}}) an, in die später die E-Mail-Adressen kopiert werden sollen.

![Ziel-Tabelle samt Ergebnis-Spalte vor der Ausführung der Datenverarbeitungsaktion](images/table-open-tasks-before-data-processing-operation-1.png)

Um die Datenverarbeitungsoperation anzulegen, befolgen Sie die oben beschriebenen Schritte. Für den konkreten Anwendungsfall wählen Sie dabei als **Bedingung** aus, dass der Name eines Mitarbeiters in der Spalte **name** in der Tabelle **employees** mit dem Namen in der Spalte **responsible** in der Tabelle **open tasks** übereinstimmen muss. Dieser Schritt ist essenziell, damit bei der Datenverarbeitungsoperation die korrekten Daten der entsprechenden Mitarbeiter kopiert werden.

![Definition der Übereinstimmungs-Bedingung für die Datenverarbeitungsaktion](images/define-condition-for-data-operation-compare-and-copy.png) {{< warning  type="warning" headline="Wichtiger Hinweis"  text="Bei dieser Datenverarbeitungsoperation sollten die zu vergleichenden Spalten **den gleichen Spaltentyp** haben, damit SeaTable identische Werte zuverlässig erkennt." />}}

Im nächsten Schritt können Sie eine beliebige Anzahl an Quellspalten aus der Tabelle **employees** auswählen, deren Inhalte bei Ausführung der Operation und Zutreffen der gerade definierten Übereinstimmungsbedingung in die ausgewählten Ergebnisspalten der Tabelle **open tasks** kopiert werden.

![Auswahl der Spalten aus der Quell-Tabelle, deren Inhalte bei Zutreffen der Übereinstimmungs-Bedingung in die Ziel-Tabelle kopiert werden](images/select-columns-to-copy.png)

{{< warning  type="warning" headline="Achtung vor Datenverlust" >}}

Die Quell- und Ergebnisspalten sollten **den gleichen Spaltentyp** aufweisen, damit beim Kopieren keine Daten verloren gehen. Sie können zwar beispielsweise Daten aus einer [Datum-Spalte]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) in eine [Text-Spalte]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) kopieren, diese eignen sich dann aber nicht mehr für [Kalender]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}). Legen Sie also vor der Ausführung der Operation für jede **Quellspalte**, die Sie kopieren möchten, eine **Ergebnisspalte** des gleichen Typs in der Ziel-Tabelle an."

{{< /warning >}}

Bei erfolgreicher Ausführung der Operation werden die Tabellen **employees** und **open tasks** auf Übereinstimmungen in den definierten Spalten **name** und **responsible** untersucht. Stimmen dabei die **Namen** in den Spalten beider Tabellen überein, wird die **E-Mail-Adresse** des entsprechenden Mitarbeiters aus der definierten Spalte **E-Mail** automatisch in die Ergebnisspalte **contact** kopiert.

![In die Ziel-Tabelle kopierte Inhalte nach der Auslösung der Datenverarbeitungsaktion](images/table-after-data-processing-operation-2.png)

{{< warning  headline="Hinweis" >}}

Um eine leichte Verständlichkeit zu ermöglichen, haben wir uns im Anwendungsfall dazu entschieden, lediglich **eine Spalte** mithilfe der Datenverarbeitungsoperation zu kopieren. Um die Wirkung zu erhöhen, können Sie selbstverständlich auch eine größere Anzahl an Quell- und Ergebnisspalten auswählen.

{{< /warning >}}

## Nicht unterstützte Spaltentypen

Folgende Spaltentypen können Sie mithilfe der Operation _Vergleichen und kopieren_ **nicht** kopieren und stehen Ihnen dementsprechend bei der Definition der Quell- und Ergebnisspalten **nicht** zur Verfügung.

- [Mehrfachauswahl-Spalte]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}})
- [Die Spalte Ersteller]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}})
- [Die Spalte Letzter Bearbeiter]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}})
- [Schaltfläche]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
