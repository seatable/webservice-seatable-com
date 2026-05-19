---
title: 'Die Lookup-Formel'
date: 2022-10-13
lastmod: '2023-04-06'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/de/hilfe/die-lookup-funktion'
seo:
    title: 'Lookup-Spalte in SeaTable: Werte verknüpfter Tabellen holen'
    description: 'Mit der Lookup-Spalte zeigen Sie Daten aus verknüpften Tabellen direkt an, vermeiden Doppeleingaben und verknüpfen Informationen effizient.'

---

Die Lookup-Funktion ermöglicht es Ihnen, zusätzliche Werte aus einer bereits verknüpften Tabelle in Ihrer aktuellen Tabelle darzustellen. So wird verhindert, dass Sie die Daten doppelt erfassen müssen, und Sie können gleichzeitig die Daten miteinander in Beziehung setzen. In Excel kennt man diese Funktion als _VLOOKUP_ oder _SVERWEIS_.

## Wann braucht man die Lookup-Formel?

Die Lookup-Funktion sollte immer dann zum Einsatz kommen, wenn Sie Querverweise zu Informationen herstellen möchten, die in verschiedenen Tabellen gespeichert sind. Nehmen wir an, Sie verwenden SeaTable für das Projektmanagement, wobei die Projekte in einer Tabelle und die mit dem Projekt verbundenen Aufgaben in einer anderen Tabelle gespeichert sind. Jedes Projekt ist dann mit einer Reihe von Aufgaben verknüpft.

![Verknüpfung von Projektaufgaben mit einem Projekt](images/linked-tables-seatable.png)

Als Projektmanager möchten Sie vielleicht Informationen über die mit jedem Projekt verbundenen Aufgaben anzeigen. Die Lookup-Formel kann verwendet werden, um eine Spalte in der verknüpften Tabelle auszuwählen und deren Werte anzuzeigen. So können Sie z. B. automatisch die Projektmitarbeiter anzeigen lassen, die für die jeweiligen Aufgaben verantwortlich sind.

![Lookup-Column](images/lookup-columns.png)

Dies kann für den einfachen Zugriff auf tabellenübergreifende Informationen, die Einrichtung von Automatisierungen, Formeln etc. hilfreich sein. Im Folgenden erfahren Sie mehr über die Verwendung der Lookup-Funktion.

## So verwenden Sie die Lookup-Spalte

### Eine Tabellenverknüpfung hinzufügen

Die Lookup-Funktion kann nur verwendet werden, wenn bereits eine Spalte des Typs _Verknüpfung zu anderen Einträgen_ existiert. Wenn Sie bisher keine solche Spalte haben, legen Sie zuerst eine an. Wie das funktioniert, erfahren Sie [hier]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}).

### Eine Lookup-Formel hinzufügen

Anfangs mag die Lookup-Formel Sie vielleicht noch verwirren. Doch Sie werden sehen, dass Sie in Kürze diese unglaublich vielseitige und leistungsfähige Spaltenfunktion lieben werden. So fügen Sie eine Spalte mit der Lookup-Formel hinzu:

![Einrichten einer Lookup-Spalte](images/setup-of-lookup-column.gif)

1. Erstellen Sie eine neue Spalte des Typs **Formel für Verknüpfungen**.
2. Legen Sie als Formel die Option **Lookup** fest.
3. Wählen Sie eine **Verknüpfungsspalte** aus. Dieses Feld ist automatisch richtig ausgefüllt, wenn Sie nur eine Verknüpfungsspalte haben.
4. Mit der **Nachschlagespalte in der verknüpften Tabelle** legen Sie fest, aus welcher Spalte der anderen Tabelle die Werte übernommen werden sollen.
5. Klicken Sie auf **Abschicken**.

## Häufige Fragen zur Lookup-Spalte

{{< faq "Kann man mehrere Werte per Lookup in eine Tabelle holen?" >}}Definitiv. Erzeugen Sie einfach eine weitere Spalte und nutzen Sie wieder die Lookup-Funktion. So können Sie beliebig viele Informationen aus der verlinkten Tabelle auslesen und anzeigen lassen.
{{< /faq >}}
{{< faq "Können Lookups nachträglich geändert werden?" >}}Das ist natürlich möglich. Klicken Sie auf das **Dreieck-Symbol** rechts neben dem Spaltennamen und dann auf **Spaltentyp anpassen**. Passen Sie die Einstellungen der Spalte an und sofort werden Ihnen die gewünschten Informationen angezeigt.
{{< /faq >}}
{{< faq "Funktionieren Lookups bei mehreren Verlinkungen?" >}}Jede Lookup-Formel kann nur die Informationen aus **einer** Spalte Ihrer verlinkten Tabellen holen. Aber natürlich können Sie über Verknüpfungsspalten mehrere Tabellen verlinken und weitere Lookup-Spalten anlegen, um noch mehr Informationen auszulesen und anzuzeigen.
{{< /faq >}}
{{< faq "Können Einträge, die per Lookup nachgeschlagen werden, gefiltert werden?" >}}Ja, Sie können die Einträge beliebig filtern. Aktivieren Sie dazu den entsprechenden **Regler** in den _Spalten-Einstellungen_ und wählen Sie die **Spalte(n)** aus, deren Einträge nachgeschlagen werden sollen. Sie können dabei beliebig viele **Filter-Bedingungen** definieren.

{{< /faq >}}
