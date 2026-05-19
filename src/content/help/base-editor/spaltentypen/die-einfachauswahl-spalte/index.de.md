---
title: 'Die Einfachauswahl-Spalte'
date: 2022-10-10
lastmod: '2025-07-15'
categories:
    - 'spalten'
author: 'kgr'
url: '/de/hilfe/die-einfachauswahl-spalte'
aliases:
    - '/de/hilfe/anlegen-einer-einfachauswahl-spalte'
    - '/de/hilfe/hinzufuegen-von-optionen-zu-einer-einfachauswahl-spalte'
    - '/de/hilfe/einfachauswahl-optionen-exportieren-und-importieren'
    - '/de/hilfe/aendern-der-reihenfolge-von-einfachauswahl-optionen'
    - '/de/hilfe/kaskadierung-einer-einfachauswahl'
seo:
    title: 'Die Einfachauswahl-Spalte in SeaTable: Optionen, Farben & Kaskadierung'
    description: 'Einfachauswahl-Spalte in SeaTable: Optionen anlegen, Farben anpassen, Kaskadierung nutzen und Abhängigkeiten logisch definieren.'
---

Eine Einfachauswahl-Spalte ist ideal, wenn Sie Ihren Zeilen **genau eine Option** aus einer zu definierenden Liste von Optionen zuweisen möchten. Die Optionen erhalten bunte **Labels**, mit denen Sie Ihre Datensätze in **Kategorien** einordnen und Tabellen übersichtlich gestalten können.

![Einfachauswahl-Feld in SeaTable.](images/single-select-column.png)

## Anlegen einer Einfachauswahl-Spalte

Das Anlegen einer Einfachauswahl-Spalte ist kinderleicht und mit wenigen Klicks erledigt. Ausführliche Informationen finden Sie unter [Hinzufügen einer Spalte]({{< relref "help/base-editor/spalten/hinzufuegen-einer-spalte" >}}).

![Anlegen einer Einfachauswahl-Spalte](images/define-single-select-column.png)

1. Klicken Sie auf das **Plus-Symbol** rechts neben der letzten Spalte einer Tabelle.
2. Geben Sie der neuen Spalte einen **Namen**.
3. Wählen Sie als Spaltentyp **Einfachauswahl**.
4. Bestätigen Sie mit **Abschicken**.

## Auswahl-Optionen hinzufügen

In einer Einfachauswahl-Spalte können Sie diverse Optionen anlegen, aus denen Sie im Anschluss beim Befüllen der Zellen wählen können. **Neue Optionen** können Sie der Spalte auf mehreren Wegen hinzufügen:

- Optionen über die Spalteneinstellungen hinzufügen
- Optionen über die Zellen der Einfachauswahl-Spalte hinzufügen
- Optionen importieren

{{< warning headline="Gleiches Prinzip bei Mehrfachauswahl-Spalten" >}} 
Alle in diesem Abschnitt vorgestellten Funktionen gelten genauso für die [Mehrfachauswahl-Spalte]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}).
{{< /warning >}}

### Optionen über die Spalteneinstellungen hinzufügen

![Hinzufügen von Optionen zu einer Einfachauswahl-Spalte](images/add-options-to-a-single-select-column.gif)

1. Klicken Sie auf den **Drop-down-Pfeil** rechts neben dem Namen einer Einfachauswahl-Spalte.
2. Gehen Sie auf **Einfachauswahl bearbeiten**.
3. Erstellen Sie beliebig viele Optionen, indem Sie auf **Option hinzufügen** klicken.
4. Bestätigen Sie jede Eingabe mit der **Enter-Taste**.
5. Bei Bedarf können Sie die den Optionen zugewiesenen **Farben** anpassen.

### Optionen über die Zellen der Einfachauswahl-Spalte hinzufügen

![Hinzufügen von Optionen über die Zeilen der Einfachauswahl-Spalte](images/Hinzufuegen-von-Optionen-ueber-die-Zeilen.png)

1. Machen Sie einen Doppelklick auf eine **Zelle** der Einfachauswahl-Spalte.
2. Geben Sie in das **Suchfeld** einen passenden Begriff ein, den Sie als **neue Option** definieren möchten.
3. Klicken Sie auf **Option hinzufügen**.
4. Der eingegebene Begriff wird anschließend der ausgewählten Zelle zugewiesen und zu den verschiedenen **Auswahl-Optionen** der Spalte hinzugefügt.

{{< warning headline="Einfachauswahl oder Verknüpfung zu anderen Einträgen?" >}}
Wenn Sie sich wünschen, **zusätzliche Daten** zu jeder Auswahloption speichern zu können, sollten Sie in Erwägung ziehen, statt einer Einfachauswahl-Spalte eine [Verknüpfungsspalte]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) zu verwenden. Dazu legen Sie in einer separaten Tabelle die Einfachauswahl als erste Spalte an. So können Sie für alle Optionen vollständige Datensätze erfassen, die Sie in verknüpften Tabellen beliebig vielen Zeilen zuordnen können.
{{< /warning >}}

## Optionen exportieren und importieren

Sie können die Optionen nicht nur **manuell eingeben**, sondern auch bequem aus einer bestehenden Spalte **exportieren** und in eine andere Spalte **importieren**. Dies erspart Ihnen viel Arbeit, wenn Sie die gleichen Optionen – auch über verschiedene Bases hinweg – für mehrere **Einfach-** und **Mehrfach-Auswahlspalten** verwenden möchten.

### Optionen aus einer Auswahlspalte exportieren

![Einfachauswahl-Optionen exportieren](images/export-options-of-a-single-select-column-new-1.png)

1. Klicken Sie auf den **Drop-down-Pfeil** rechts neben dem Namen einer Einfach- oder Mehrfach-Auswahlspalte.
2. Wählen Sie **Einfachauswahl bearbeiten** bzw. **Mehrfachauswahl bearbeiten**.
3. Klicken Sie auf **Optionen exportieren**.

Die Optionen werden nun als JSON-Datei **exportiert**. Je nach Browser-Einstellungen wurde der Download entweder direkt auf Ihrem Gerät gespeichert oder Sie müssen noch einen Speicherort angeben. Im nächsten Schritt können Sie die Optionen in eine andere Einfach- oder Mehrfach-Auswahlspalte **importieren**.

### Optionen in eine Auswahlspalte importieren

![Exportierte Optionen in eine neue Einfachauswahl-Spalte importieren](images/import-options-of-a-single-select-column-new-3.png)

1. Klicken Sie auf den **Drop-down-Pfeil** rechts neben dem Namen einer Einfach- oder Mehrfach-Auswahlspalte.
2. Wählen Sie **Einfachauswahl bearbeiten** bzw. **Mehrfachauswahl bearbeiten**.
3. Klicken Sie auf **Optionen importieren**.
4. Wählen Sie die **JSON-Datei** von Ihrem Gerät aus und bestätigen Sie den Upload.

Die Optionen werden anschließend in die ausgewählte Spalte **importiert** und stehen zum Befüllen der entsprechenden Zellen bereit. Sie können natürlich weiterhin Optionen ergänzen, löschen und nach Belieben bearbeiten.

## Farben der Auswahl-Optionen

Um die Ansicht innerhalb einer Tabelle optisch zu gestalten, ordnet SeaTable jeder Option in einer Einfachauswahl- oder Mehrfachauswahl-Spalte eine **Farbe** zu. Über den oben genannten Weg zu den Optionen können Sie diese zufällig zugewiesene Farbe nachträglich **anpassen**. 

Sie öffnen den **Farbwähler**, indem Sie auf das farbig hinterlegte **Dreieck-Symbol vor dem Namen der Option** klicken.

![Farben der Einfachauswahl-Spalte](images/farben-einfachauswahl.png)

Aktuell stehen Ihnen **24 Farben** zur Verfügung, um die jeweiligen Optionen visuell hervorzuheben. Mit einem [Enterprise-Abo]({{< relref "help/teamverwaltung/abonnement/abo-pakete" >}}) haben Sie zudem die Möglichkeit, [eigene Farben]({{< relref "help/base-editor/weitere-optionen/eigene-farben-in-einer-base-hinzufuegen" >}}) für Ihre Auswahl-Optionen anzulegen.

## Reihenfolge der Optionen ändern

Die Reihenfolge der Optionen ist von entscheidender Bedeutung, wenn Sie nach einer Einfachauswahl-Spalte [sortieren]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) oder [gruppieren]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) möchten. SeaTable ordnet die Optionen nämlich **nicht alphabetisch**, sondern richtet sich flexibel nach der **Reihenfolge der Optionen**, die Sie nach Ihren Wünschen festlegen können.

![Sortierung einer Einfachauswahl-Spalte ändern](images/Sortierung-einer-Einfachauswahl-Spalte-aendern.gif)

1. Klicken Sie auf den **Drop-down-Pfeil** rechts neben dem Namen der Einfachauswahl-Spalte.
2. Gehen Sie auf **Einfachauswahl bearbeiten**.
3. **Ziehen** Sie eine Option per **Drag-and-Drop** an die gewünschte Stelle. Nutzen Sie dafür die Greiffläche mit den **sechs Punkten**, die sich links vor jeder Option befindet.

## Standardwert festlegen

Bei jeder Einfachauswahl-Spalte haben Sie die Möglichkeit, einen voreingestellten [Standardwert festzulegen]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}). Der Standardwert wird jeder neuen Zeile **automatisch** als Option zugewiesen.

1. Klicken Sie auf den **Drop-down-Pfeil** rechts neben dem Namen der Einfachauswahl-Spalte.
2. Gehen Sie auf **Standardwert festlegen**.
3. Wählen Sie aus der Liste die **Option**, die als Standardwert dienen soll.

![Standard-Wert bei einer Einfachauswahlspalte](images/default-value-single-select.png)

Wenn Sie den Standardwert wieder löschen möchten, klicken Sie auf das **Papierkorb-Symbol** {{< seatable-icon icon="dtable-icon-delete" >}}.

## Kaskadierung einer Einfachauswahl

Mithilfe der Kaskadierungsfunktion können Sie für jede Einfachauswahl-Spalte eine übergeordnete Spalte desselben Typs festlegen, welche die zur Verfügung stehenden Optionen der untergeordneten Einfachauswahl-Spalte einschränkt. Dies bietet folgende Vorteile:

- Mithilfe einer Kaskadierung können Sie die **Anzahl an Optionen reduzieren**, die in einer anderen Einfachauswahl-Spalte zur Verfügung stehen.
- Indem Sie Abhängigkeiten definieren, können Sie **logische Zusammenhänge** zwischen zwei Einfachauswahl-Spalten herstellen.
- Besonders bei einer großen Anzahl an Optionen, kann dies sehr hilfreich sein, um **Fehler zu minimieren**, die beim Einpflegen von Daten entstehen können.
- Darüber hinaus können Kaskadierungen von Einfachauswahl-Spalten auch dabei helfen, **Arbeitsprozesse zu beschleunigen**.

![Definierung einer Kaskadierung](images/Definierung-einer-Kaskadierung-1.png)

1. Klicken Sie auf den **Drop-down-Pfeil** einer Einfachauswahl-Spalte.
2. Klicken Sie auf **Kaskadierung definieren**.
3. Wählen Sie eine **Einfachauswahl-Spalte** aus, die als übergeordnete Spalte fungieren soll.
4. Weisen Sie den **übergeordneten Optionen** dieser Spalte beliebig viele **untergeordnete Optionen in der aktuellen Spalte** zu.

![Zuweisung der Optionen der übergeordneten Einfachauswahl-Spalte](images/Zuweisung-der-Optionen-bei-einer-Kaskadierung-1.png)

{{< warning  headline="Wichtiger Hinweis"  text="Als übergeordnete Einfachauswahl-Spalten können ausschließlich Spalten fungieren, die sich in **derselben Tabelle** befinden wie die Spalte, für die eine Kaskadierung definiert werden soll." />}}

### Beispiel für eine sinnvolle Kaskadierung

![Definition einer Kaskadierung anhand eines Beispiels](images/Beispiel-fuer-eine-Kaskadierung-Bild-1.png)

In diesem Beispiel enthält die Tabelle Daten über verschiedene Fortbildungs-/Trainingseinheiten von Mitarbeitern. Neben der ersten Spalte, die verschiedene **Trainings** erfasst, existiert bereits eine Einfachauswahl-Spalte, die den jeweiligen **Standort** des Trainings angibt. Für eine weitere Einfachauswahl-Spalte, welche das genaue **Gebäude** erfasst, wird in diesem Beispiel eine **Kaskadierung** definiert.

![Zuordnung von Optionen der ausgewählten Spalte zu den Optionen der übergeordneten Einfachauswahl-Spalte.](images/Beispiel-fuer-eine-Kaskadierung-Bild-2.png)

Als **übergeordnete Einfachauswahl-Spalte** dient in diesem Beispiel die Spalte **"Location"**, welche die Stadt angibt, in der das jeweilige Training stattfindet. Im nächsten Schritt weist man nun den drei Städten in dieser Spalte **untergeordnete Optionen** aus der neu angelegten Einfachauswahl-Spalte **"Building"** zu. Konkret werden den drei Optionen **London**, **Paris** und **Berlin** die Gebäude zugewiesen, die sich in der jeweiligen Stadt befinden.

![In der Einfachauswahl-Spalte zur Verfügung stehende Optionen, nach der Definition einer Kaskadierung.](images/Beispiel-fuer-eine-Kaskadierung-Bild-3.png)

Welche Optionen bzw. Gebäude in einer Zelle der untergeordneten Spalte "Building" auswählbar sind, hängt nun von der Stadt ab, welche in derselben Zeile bei der Einfachauswahl-Spalte "Location" ausgewählt ist. Dadurch können Sie **ausschließlich** die Gebäude auswählen, die sich wirklich in der entsprechenden Stadt befinden.