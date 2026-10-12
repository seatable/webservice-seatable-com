---
title: 'Die Verknüpfungsspalte'
date: 2022-10-11
lastmod: '2026-10-07'
categories:
    - 'verknuepfungen'
author: 'kgr'
url: '/de/hilfe/die-verknuepfungsspalte'
aliases: 
    - '/de/hilfe/wie-man-tabellen-in-seatable-miteinander-verknuepft'
seo:
    title: 'Verknüpfte Datensätze in SeaTable: die Verknüpfungsspalte'
    description: 'Verknüpfte Datensätze ohne Programmierung: Tabellen verknüpfen, Werte per Lookup und Rollup nutzen und Beziehungen als Diagramm sehen.'
weight: 20
---

Mit der Verknüpfungsspalte bauen Sie in SeaTable Beziehungen zwischen Tabellen auf, ganz ohne SQL oder Programmierung. Ein Eintrag in einer Tabelle verweist dabei auf einen oder mehrere Einträge in einer anderen Tabelle, zum Beispiel ein Auftrag auf den Kunden und auf die bestellten Produkte. Solche **verknüpften Datensätze** (englisch: _linked records_) sind die Grundlage der [relationalen Datenbankfunktionen]({{< relref "posts/relationale-datenbank" >}}) von SeaTable. Der Spaltentyp heißt **Verknüpfung zu anderen Einträgen**.

## Welche Beziehungen Sie abbilden können

| Beziehung | Beispiel | So geht es in SeaTable |
|---|---|---|
| **1:1** (eins zu eins) | Eine Rechnung gehört zu genau einer Bestellung. | Verknüpfungsspalte mit der Einstellung [Verknüpfungen auf eine Zeile einschränken](#verknüpfungen-auf-eine-zeile-einschränken) |
| **1:n** (eins zu viele) | Ein Kunde hat viele Aufträge, jeder Auftrag gehört zu einem Kunden. | Verknüpfungsspalte, in der Auftragstabelle auf eine Zeile eingeschränkt, in der Kundentabelle ohne Einschränkung |
| **n:m** (viele zu vielen) | Ein Auftrag enthält mehrere Produkte, ein Produkt kommt in vielen Aufträgen vor. | Verknüpfungsspalte ohne Einschränkung, eine Zwischentabelle ist nicht nötig |
| **Innerhalb einer Tabelle** | Aufgaben und Unteraufgaben, Mitarbeitende und ihre Vorgesetzten | [Verknüpfungen innerhalb einer Tabelle]({{< relref "help/base-editor/tabellen/verknuepfungen-innerhalb-einer-tabelle" >}}) |

Eine Verknüpfung ist in beiden Tabellen sichtbar. Beim Anlegen der Verknüpfungsspalte wählen Sie, ob die Verknüpfung in der anderen Tabelle in einer **vorhandenen Spalte** angezeigt oder dort eine **neue Spalte** angelegt wird.

{{< warning  headline="Tipp: Angaben pro Kombination"  text="Brauchen Sie bei einer n:m-Beziehung Angaben, die zur Kombination gehören, etwa **Menge** und **Preis** eines Produkts in einem bestimmten Auftrag? Dann legen Sie eine eigene Tabelle an, z. B. **Auftragspositionen**, und verknüpfen sie mit den Aufträgen und den Produkten." />}}

### Beispiel: Kunden, Aufträge und Produkte

![Base mit den Tabellen Kunden, Aufträge, Auftragspositionen, Produkte und deren Verknüpfungen](images/verknuepfungsspalten.png)

- Die Tabelle **Kunden** enthält Name, Ansprechpartner und Adresse.
- Jeder Eintrag in **Aufträge** ist mit einem Kunden verknüpft.
- **Auftragspositionen** verknüpfen einen Auftrag mit einem Produkt und enthalten Menge und Preis.
- Die Tabelle **Produkte** enthält Artikelnummer, Bezeichnung und Listenpreis.

Mit einer [Formel für Verknüpfungen](#daten-aus-verknüpften-einträgen-nutzen-lookup-rollup-und-mehr) zeigen Sie in jedem Auftrag den Kundennamen an und berechnen in der Kundentabelle den Umsatz pro Kunde. Das [Tabellenbeziehungen-Plugin](#beziehungen-sichtbar-machen-das-beziehungsdiagramm) zeigt die ganze Struktur als Diagramm.

## So können Sie zwei Tabellen miteinander verknüpfen

![Verknüpfung zwischen zwei Tabellen erstellen](images/how-to-link-different-tables.gif)

1. Legen Sie eine neue Spalte an und wählen Sie den Spaltentyp **Verknüpfung zu anderen Einträgen**.
2. Geben Sie der Spalte einen **Namen**.
3. Wählen Sie unter **Tabelle für die Verknüpfung wählen** die Tabelle aus, deren Einträge Sie mit der aktuellen Tabelle verlinken wollen.
4. Klicken Sie auf **Abschicken**.
5. Der Inhalt der neuen Spalte ist noch leer. Um sie zu füllen, können Sie **bestehende Einträge verlinken** oder **neue Zeilen hinzufügen**.

Sobald Tabellen miteinander verknüpft sind, können Sie über den **Link-Dialog** die Informationen der verknüpften Einträge aufrufen. Dazu klicken Sie in einer **Zelle** der Verknüpfungsspalte auf das **Doppelpfeil-Symbol** oder machen einen **Doppelklick**. In dem sich öffnenden Link-Dialog werden die **verknüpften Einträge** aufgelistet. Klicken Sie auf einen Eintrag, um sich in einem zusätzlichen Fenster die **Zeilendetails** anzusehen.

![Zeilendetailansicht bei verknüpften Einträgen](images/Zeilendetailansicht-bei-verknuepften-Eintraegen-711x225.png)

## Bestehende Einträge verlinken

![Bestehende Einträge verlinken](images/link-existing-entries.gif)

1. Klicken Sie in eine **Zelle** der **Verknüpfungsspalte** und dann auf das erschienene **Plus-Symbol**.
2. Nun werden Ihnen die verfügbaren **Zeilen der verknüpften Tabelle** aufgelistet. Wählen Sie die Zeile(n) aus, die Sie mit der Zeile Ihrer aktuellen Tabelle verlinken möchten.
3. In der Verknüpfungsspalte wird Ihnen jede Zeile sofort **als verlinkter Eintrag** angezeigt.

{{< warning  headline="Umweg über den Link-Dialog"  text="Alternativ können Sie auch erst den Link-Dialog öffnen. Klicken Sie auf eine **Zelle in der Verknüpfungsspalte** und dann auf das blaue **Doppelpfeil-Symbol** oder machen Sie einen **Doppelklick**. Klicken Sie anschließend auf **Bestehende Einträge verlinken** und wählen Sie wie oben die Zeile(n) aus." />}}

Über die **integrierte Suchfunktion** im Link-Dialog können Sie die Einträge der verknüpften Tabelle durchsuchen, um schnell die gewünschte Zeile zu finden.

{{< warning  type="warning" headline="Mehrere Links pro Zelle"  text="Sie können in **einer Zelle** der Verknüpfungsspalte **mehrere Einträge** der verknüpften Tabelle verlinken. Wiederholen Sie dazu die oben beschriebene Anleitung." />}}

## Neue Zeile hinzufügen

Sie können über den Link-Dialog sogar eine **neue Zeile** zu einer **verknüpften Tabelle** hinzufügen, ohne in diese Tabelle wechseln zu müssen. Im Anschluss wird die Zeile in der verknüpften Tabelle unter den bestehenden Datensätzen hinzugefügt und als verlinkter Eintrag in der Verknüpfungsspalte der geöffneten Tabelle angezeigt.

1. Machen Sie einen **Doppelklick** auf die **Zelle** einer **Verknüpfungsspalte** oder klicken Sie auf das blaue **Doppelpfeil-Symbol**, um den Link-Dialog zu öffnen.
   ![Doppelklick in eine Verknüpfungsspalte](images/click-in-linked-column.png)
2. Klicken Sie auf **Zeile hinzufügen**.
   ![Klick auf Zeile hinzufügen](images/click-add-record.jpg)
3. Füllen Sie im sich öffnenden Fenster die verschiedenen **Tabellenspalten** aus.
   ![Ausfüllen der Tabellenspalten](images/fill-columns.png)
4. Klicken Sie auf **Abschicken**, um die neue Zeile anzulegen.
   ![Klick auf Abschicken](images/click-submit.png)
5. Die **neue Zeile** wird automatisch der **verknüpften Tabelle** hinzugefügt und in der aktuell geöffneten Tabelle als **verlinkter Eintrag** in der Verknüpfungsspalte angezeigt.

## Bestehende Einträge einer verknüpften Tabelle bearbeiten

![Bestehende Einträge einer verknüpften Tabelle bearbeiten](images/edit-linked-entries.gif)

1. Klicken Sie in eine **Zelle** der Verknüpfungsspalte.
2. Klicken Sie auf den **verlinkten Eintrag**, den Sie bearbeiten möchten.
3. Die **Zeilendetails** öffnen sich. Nehmen Sie dort die gewünschten **Änderungen** vor.
4. **Schließen** Sie das Fenster, um die Änderungen zu **speichern**.

## Verlinkungen entfernen

In einer Verknüpfungsspalte verlinkte Einträge können Sie mit nur wenigen Klicks wieder entfernen. Öffnen Sie hierzu einfach den **Link-Dialog** der entsprechenden Verknüpfungsspalte und klicken Sie neben dem gewünschten Eintrag rechts auf das **X-Symbol**.

![Verlinkungen entfernen](images/delete-links.png) 

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="Es wird lediglich der **verlinkte Eintrag** aus der entsprechenden Verknüpfungsspalte **gelöscht**. Die **Zeile in der verknüpften Tabelle** bleibt hingegen weiterhin **erhalten**." />}}

## Einstellungen der Verknüpfungsspalte

Eine Verknüpfungsspalte erlaubt Ihnen verschiedene Einstellungen, die Sie ganz leicht vornehmen und ändern können. Klicken Sie dazu im Tabellenkopf auf das dreieckige **Drop-down-Symbol** der Verknüpfungsspalte und dann auf **Einstellungen**.

![Einstellungen einer Link-Spalte öffnen](images/Einstellungen-einer-Link-Spalte-oeffnen-350x200.png)

### Auswahl der verknüpften Spalte aus der verlinkten Tabelle

Im Drop-down-Menü können Sie zunächst die **Spalte der verknüpften Tabelle** auswählen, deren **Einträge** in der Verknüpfungsspalte angezeigt werden sollen.

![Auswahl der verknüpften Spalte aus der verlinkten Tabelle](images/select-column-of-linked-table-to-display.png)

### Verknüpfungen auf eine Zeile einschränken

Durch Aktivieren des entsprechenden Reglers können Sie die Verknüpfung auf **maximal eine Zeile** beschränken. Ist diese Einstellung aktiv, kann in jeder Zelle der Verknüpfungsspalte nur noch jeweils **ein verlinkter Eintrag** hinzugefügt werden.

![Verknüpfungen einschränken](images/limit-linking-to-max-one-row.png)

Wenn Sie einer Zelle bereits einen verknüpften Eintrag hinzugefügt haben, werden die Optionen zum Hinzufügen weiterer Einträge **nicht** mehr angezeigt.

![Wird die Verknüpfung auf maximal eine Zeile beschränkt, stehen einem die Optionen zum Hinzufügen von Verlinkungen im Link-Dialog nicht mehr zur Auswahl, sobald eine Verknüpfung hinzugefügt wurde](images/not-visibble-options-to-add-linked-records.png)

Sinnvoll kann diese Einstellung beispielsweise sein, wenn eine Rechnung mit der dazugehörigen Bestellung aus einer anderen Tabelle verknüpft werden soll – wenn also die verknüpften Datensätze logische **Paare** bilden. In diesem Fall könnte das Hinzufügen von weiteren Verknüpfungen zu Verwirrung führen und Arbeitsprozesse negativ beeinträchtigen.

### Verknüpfungen auf eine Ansicht einschränken

Durch die Aktivierung dieser Einstellung können Sie Verknüpfungen auf **eine Ansicht** der verknüpften Tabelle beschränken. Dazu legen Sie eine zuvor definierte **Ansicht** der verknüpften Tabelle fest. In der Verknüpfungsspalte können Sie anschließend **ausschließlich** die Einträge dieser Ansicht verlinken. Das Verknüpfen von Einträgen anderer Ansichten ist dann **nicht** mehr möglich.

![Verknüpfungen auf eine Ansicht einschränken](images/Verknuepfungen-auf-eine-Ansicht-einschraenken.png)

Diese Einstellung ergibt vor allem bei **gefilterten Ansichten** Sinn und kann Ihnen behilflich sein, wenn Sie gezielt **bestimmte Einträge** in Ihren Tabellen verknüpfen möchten.

### Verlinkung von bestehenden Einträgen verhindern

In den Einstellungen einer Verknüpfungsspalte können Sie durch Aktivieren eines entsprechenden Reglers auch die Verlinkung von bestehenden Einträgen verhindern. Ist der Regler **aktiviert**, unterstützt die entsprechende Verknüpfungsspalte **ausschließlich** das Hinzufügen von **neuen Zeilen** bzw. Einträgen.

Bereits bestehende Einträge in der verknüpften Tabelle können dann in der Spalte **nicht** mehr verlinkt werden. Einträge, die bereits in der Spalte verlinkt wurden, bleiben von der Einstellung jedoch **unberührt**.

![Einstellung zum Verhindern der Verlinkung von bestehenden Einträgen](images/setting-avoid-linking-existing-records.png)

### Verknüpfungen mit einer Filterregel einschränken

Wenn Sie diese Option aktivieren, lässt sich die Auswahl der verknüpfbaren Zeilen auf Basis von Filterregeln einschränken. Die Filter selbst können statisch oder dynamisch sein:
- Bei einem **statischen Filter** nutzen Sie einen einheitlichen Wert, um die Zeilen in der verknüpften Tabelle zu filtern (z. B. nur Zeilen, die nicht den Wert "archiviert" haben, sind verknüpfbar). Der Effekt ist somit ähnlich wie bei der Option **Verknüpfungen auf eine Ansicht einschränken**.
- Bei einem **dynamischen Filter** ist der Wert, der für die Filterung der Zeilen in der verknüpften Tabelle verwendet wird, ein Spaltenwert der aktiven Zeile (z. B. nur Zeilen, deren Status identisch mit dem Status der aktiven Zeile ist, sind verknüpfbar). **Zeilen mit unterschiedlichen Filterwerten** haben somit abweichende verknüpfbare Zeilen.

![Verknüpfungen mit einer Filterregel einschränken](images/limit-row-selection-using-a-filter-rule.png)

## Ansichtsoptionen des Link-Dialogs

Im Link-Dialog einer Verknüpfungsspalte stehen Ihnen zudem verschiedene Ansichtsoptionen zur Verfügung.

### Größe des Fensters anpassen

Um alle verlinkten Einträge auf einen Blick zu haben, können Sie die **Größe** des Link-Dialog-Fensters anpassen. Fahren Sie hierzu einfach mit der Maus über einen der äußeren Ränder, bis sich der Cursor in einen **Doppelpfeil** verwandelt, und ziehen Sie den Rand mit gedrückter Maustaste in die gewünschte Richtung.

![Fenstergröße des Link-Dialogs anpassen](images/adjust-size-of-the-link-dialogue.gif)

### Spaltenbreite anpassen

Damit mehr Spalteneinträge der verlinkten Zeilen in das Fenster passen, können Sie auch die **Breite** der angezeigten **Spalten** im Link-Dialog anpassen. Fahren Sie hierzu mit der Maus über den **Bereich zwischen zwei Spaltennamen**, bis sich der Cursor in einen **Doppelpfeil** verwandelt, und ziehen Sie die unsichtbare Begrenzungslinie mit gedrückter Maustaste nach links oder rechts, bis Sie die gewünschte **Spaltenbreite** erreicht haben.

![Spaltenbreite anpassen](images/adjust-size-of-columns-in-link-dialog.gif)

### Spalten ausblenden

Um den Link-Dialog noch übersichtlicher zu gestalten, können Sie beliebig viele Spalten der verknüpften Einträge mit einem Klick auf das **Augen-Symbol** ausblenden. Es öffnet sich ein Fenster, in dem Sie die einzelnen Spalten mit Reglern **(de-)aktivieren** können. Dementsprechend werden die Spalten in der Übersicht der verlinkten Einträge ausgeblendet oder angezeigt.

![Ausblenden von bestimmten Spalten in der Ansicht der verknüpften Einträge im Dialogfeld einer Verknüpfungsspalte](images/hide-columns.in-link-dialog.jpg)

### Einträge sortieren

Mit einem Klick auf die **Pfeil-Symbole** können Sie die verlinkten Einträge im Link-Dialog **sortieren**. Nutzen Sie diese Funktion beispielsweise, um sich verknüpfte Einträge anhand einer Textspalte in alphabetischer Reihenfolge anzeigen zu lassen oder sie nach einer anderen Spalte zu ordnen.

![Sortierung von Einträgen im Link-Dialog einer Verknüpfungsspalte](images/sort-entries-link-dialog.jpg)

{{< warning  type="warning" headline="Tipp"  text="In **Kombination** entfalten die **Ansichtsoptionen** eine noch größere Wirkung und können Ihnen dabei helfen, bestimmte verknüpfte Einträge noch schneller und bequemer zu finden." />}}

## Daten aus verknüpften Einträgen nutzen: Lookup, Rollup und mehr

Verknüpfte Einträge zeigen zunächst nur einen Wert der anderen Tabelle an, z. B. den Namen. Weitere Werte holen, zählen oder zusammenfassen Sie mit einer Spalte vom Typ [Formel für Verknüpfungen]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}}). Fünf Formeln stehen zur Verfügung:

| Formel | Was sie tut | Beispiel |
|---|---|---|
| [Lookup]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}) | holt die Werte einer Spalte aus den verknüpften Einträgen | Telefonnummer des Kunden im Auftrag anzeigen |
| [Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}}) | fasst die Werte der verknüpften Einträge zusammen, z. B. als Summe oder Durchschnitt | Umsatz pro Kunde aus allen Aufträgen |
| [Countlinks]({{< relref "help/base-editor/formeln/die-countlinks-formel" >}}) | zählt die verknüpften Einträge | Anzahl der Aufträge pro Kunde |
| [Findmax]({{< relref "help/base-editor/formeln/die-findmax-formel" >}}) | findet den verknüpften Eintrag mit dem größten Wert | letzter Auftrag eines Kunden |
| [Findmin]({{< relref "help/base-editor/formeln/die-findmin-formel" >}}) | findet den verknüpften Eintrag mit dem kleinsten Wert | erster Auftrag eines Kunden |

Formeln für Verknüpfungen funktionieren auch über mehrere Ebenen: Ein Lookup kann auf eine Lookup- oder Rollup-Spalte der verknüpften Tabelle zugreifen. So zeigt eine Auftragsposition den Namen des Kunden an: Der Auftrag holt ihn per Lookup aus der Kundentabelle, und die Auftragsposition greift per Lookup auf diese Spalte des Auftrags zu.

## Beziehungen sichtbar machen: das Beziehungsdiagramm

Bei vielen verknüpften Tabellen verliert man schnell den Überblick. Das [Tabellenbeziehungen-Plugin]({{< relref "help/base-editor/plugins/anleitung-zum-tabellenbeziehungen-plugin" >}}) zeigt alle Tabellen einer Base mit ihren Spalten als **Beziehungsdiagramm**. Durchgezogene Linien stehen für direkte Verknüpfungen über Verknüpfungsspalten, gestrichelte Linien für indirekte Verbindungen über Formeln für Verknüpfungen wie Lookup oder Rollup. Das Diagramm können Sie als Bild exportieren.

![Beziehungsdiagramm der Beispiel-Base Kunden, Aufträge, Auftragspositionen, Produkte](images/Beziehungsdarstellung.png)

## Grenzen

- **Spaltentyp nachträglich ändern:** Eine bestehende Spalte lässt sich nicht in eine Verknüpfungsspalte umwandeln. Legen Sie eine neue Spalte an (siehe [Häufige Fragen](#häufige-fragen)).
- **Eine Spalte pro Lookup:** Jede Lookup-Spalte holt die Werte genau einer Spalte der verknüpften Tabelle. Für weitere Werte legen Sie weitere Lookup-Spalten an.

## Häufige Fragen

{{< faq "Kann SeaTable n:m-Beziehungen (viele zu vielen) abbilden?" >}}Ja. Eine Verknüpfungsspalte ohne Einschränkung erlaubt in jeder Zelle beliebig viele verknüpfte Einträge, und ein Eintrag kann mit beliebig vielen Zeilen der anderen Tabelle verknüpft sein. Eine Zwischentabelle brauchen Sie nur, wenn Sie Angaben zur Kombination speichern möchten, z. B. Menge und Preis pro Auftragsposition.
{{< /faq >}}

{{< faq "Brauche ich SQL-Kenntnisse, um Tabellen zu verknüpfen?" >}}Nein. Verknüpfungen, Lookups und Rollups richten Sie vollständig in der Oberfläche ein. Wer möchte, kann verknüpfte Daten zusätzlich per [API](https://developer.seatable.com) oder mit Python- und JavaScript-Skripten bearbeiten.
{{< /faq >}}

{{< faq "Werden Verknüpfungen beim Import aus Airtable übernommen?" >}}Ja. Bei der [Migration von Airtable-Bases]({{< relref "help/startseite/import-von-daten/migration-von-airtable-bases-zu-seatable" >}}) geben Sie die Verknüpfungsspalten im Migrationsskript an, dann kommen sie als Verknüpfungen in SeaTable an. Übernommen werden alle Spalten außer **Button**, **Count**, **Lookup** und **Rollup**. Lookup- und Rollup-Spalten legen Sie nach dem Import als Formel für Verknüpfungen neu an.
{{< /faq >}}

{{< faq "Ich finde diesen Spaltentyp nicht. Kann ich keine Verlinkung erstellen?" >}}Die Link-Spalte steht Ihnen in jedem SeaTable Abonnement zur Verfügung. Wahrscheinlich versuchen Sie jedoch den Spaltentyp einer existierenden Spalte zu ändern. Beim [Ändern des Spaltentyps]({{< relref "help/base-editor/spalten/wie-man-den-spaltentyp-anpasst" >}}) steht Ihnen der Spaltentyp **Verknüpfung zu anderen Einträgen** tatsächlich _nicht_ zur Verfügung. Legen Sie stattdessen eine **neue Spalte** an und schon wird Ihnen der gewünschte Spaltentyp angeboten.

{{< /faq >}}
