---
title: 'Schritt 5: Auswertungen mit Hilfe der Verknüpfungen'
date: 2024-08-30
lastmod: '2024-09-05'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/de/hilfe/schritt-5-auswertungen-verknuepfungen'
seo:
    title: 'Schritt 5: Auswertungen mit Verknüpfungen erstellen'
    description: 'Lernen Sie, wie Sie mit SeaTable Verknüpfungen statistische Auswertungen erstellen und damit Ihre Daten effektiv analysieren und zusammenfassen.'

---

Nun haben wir die Datensätze aus beiden Tabellen miteinander verknüpft. Wichtig ist, dass diese Verknüpfung nicht einseitig ist. Wenn Sie zur Tabelle `Categories` wechseln, sehen Sie, dass auch dort eine neue Spalte hinzugefügt wurde, die die Verknüpfungen anzeigt. In unserem Fall bedeutet das: Eine Ausgabe ist mit einer Kategorie verknüpft, und eine Kategorie kann mit vielen Ausgaben verknüpft sein.

Durch die Verknüpfung haben wir bisher noch keinen direkten Nutzen erzielt, aber das wird sich jetzt ändern: Mithilfe der Verknüpfungen können wir in Sekundenschnelle statistische Auswertungen erstellen. So lässt sich zum Beispiel leicht ermitteln, wie hoch die Summe aller Ausgaben der Kategorie `Travel` ist.

## Vergrößern der Zeilenhöhe

Erhöhen Sie als Erstes die Zeilenhöhe in der Tabelle `Categories`, um mehr von den Verlinkungen sehen zu können. Sie finden die entsprechende Option `{{< seatable-icon icon="dtable-icon-row-height-default" >}}` in der Zeile über den Spaltennamen. Auch können Sie einzelne Spalten breiter ziehen, um mehr Inhalte zu sehen.

![Tabellenansicht mit geänderter Zeilenhöhe für bessere Sicht auf Verknüpfungen](images/level1-row-height.png)

## Auswertungen der Kategorien

Legen Sie jetzt eine neue Spalte in der Tabelle `Categories` an.

> Name: `Sum`
>
> Spaltentyp: `{{< seatable-icon icon="dtable-icon-link-formulas" >}} Formel für Verknüpfungen`
> Formel: `rollup`
>
> Verknüpfungsspalte in dieser Tabelle: `Expenses`
>
> Zusammenzufassende Spalte: `{{< seatable-icon icon="dtable-icon-number" >}} Amount`
>
> Auswertungsmethode: `Summe`

![Link-Formelspalte „Sum“ mit Rollup-Einstellung zur Summierung verknüpfter Beträge](images/lvl1-rollup.png)

Als Nächstes können Sie noch das Format der Spalte `Sum` auf Euro umstellen, damit die dargestellten Summen entsprechend in Euro formatiert werden.

## Automatische Berechnung bei jeder Änderung

Ist das nicht fantastisch? In der Spalte `Sum` werden automatisch immer die Gesamtausgaben für jede Kategorie angezeigt. Auch wenn Sie in weitere Ausgaben in der Tabelle `Expenses` erfassen, wird die Summe sofort aktualisiert.

Selbstverständlich ist das noch nicht alles. Sie könnten die Auswertung auf einzelne Jahre einschränken oder zusätzliche Bedingungen hinzufügen. Wenn Sie etwas mehr Erfahrung mit SeaTable sammeln, werden Sie solche Auswertungen mit wenigen Klicks erstellen können.

Damit sind wir auch schon am Ende dieses Abschnitts. Scrollen Sie bis zum Ende und springen Sie zum sechsten und vorletzten Thema dieses Online-Kurses.

{{< warning  type="warning" headline="Statistische Auswertungen wie ein Profi"  text="SeaTable bietet noch viele weitere Möglichkeiten der statistischen Auswertung Ihrer Daten. Freuen Sie sich also auf den zweiten Online Kurs, in dem wir dieses Thema mit Sicherheit intensiver beleuchten werden." />}}

## Hilfeartikel mit weiteren Informationen

- [Zeilenhöhe in Tabellenansichten anpassen]({{< relref "help/base-editor/ansichten/zeilenhoehe-anpassen" >}})
- [Die Rollup-Formel]({{< relref "help/base-editor/formeln/die-rollup-formel" >}})
