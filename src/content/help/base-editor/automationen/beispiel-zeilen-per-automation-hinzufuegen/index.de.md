---
title: 'Zeilen per Automation hinzufügen'
date: 2023-03-02
lastmod: '2023-03-31'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/de/hilfe/zeilen-per-automation-hinzufuegen'
seo:
    title: 'Zeilen automatisch mit SeaTable Automation hinzufügen'
    description: 'Fügen Sie Zeilen in Ihren Tabellen automatisch hinzu – mit periodischen oder bedingten SeaTable-Automationen.'
---

Mithilfe von Automationen müssen Sie Zeilen mit bestimmten Einträgen nicht mehr manuell in Ihren Tabellen hinzufügen, sondern können diese Schritte automatisch ausführen lassen. Definieren Sie hierfür einfach eine entsprechende Automation für eine beliebige Tabellenansicht.

## Wie Sie Zeilen mit einer Automation hinzufügen

![Einträge hinzufügen per Automation](images/how-to-use-automations-for-locking-rows-3.png)

1. Klicken Sie im Base-Header auf {{< seatable-icon icon="dtable-icon-rule" >}} und im Anschluss auf **Automatisierungsregeln**.
2. Klicken Sie auf **Regel hinzufügen**.
3. **Benennen** Sie die Automation und legen Sie die **Tabelle** und **Ansicht** fest, in der diese wirken soll.
4. Definieren Sie ein **Trigger-Ereignis**, welches die Automation auslöst.
5. Klicken Sie auf **Aktion hinzufügen** und wählen Sie als automatisierte Aktion **Zeile hinzufügen** aus.
6. Bestätigen Sie mit **Abschicken**.

## Anlegen der Automation

Definieren Sie für die Automation zunächst ein **Trigger-Ereignis**.

![Grundsätzlich zur Auswahl stehende Trigger-Ereignisse](images/trigger-options-for-archivating-rows.png)

{{< warning type="warning" headline="Wichtiger Hinweis" >}}

Die automatisierte Aktion **Zeile hinzufügen** steht Ihnen **ausschließlich** nach folgenden Trigger-Ereignissen zur Verfügung:

- Wenn eine Zeile hinzugefügt wird
- Wenn eine Zeile geändert wird
- Zu einer geplanten Zeit

{{< /warning >}}

Wählen Sie anschließend als automatisierte Aktion **Zeile hinzufügen** aus.

![Hinzufügen der automatisierten Aktion](images/add-an-action.png) ![Auswahl der automatisierten Aktion](images/action-add-records.png)

Im nächsten Schritt definieren Sie die **Einträge**, die nach dem Auslösen der Automation in einer Zeile erscheinen sollen. Mit einem Klick auf **Feld hinzufügen** können Sie jeweils einen beliebigen Eintrag definieren.

![Klicken Sie auf Feld hinzufügen, um Einträge zu definieren](images/add-field.png)

Wählen Sie zunächst die **Spalte**, in welche der Eintrag eingefügt werden soll.

![Auswahl der Spalte, in welche der Eintrag hinzugefügt wird](images/select-column-to-add-record.jpg)

Anschließend können Sie den **Eintrag** definieren. Je nach ausgewähltem [Spaltentyp]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}
) stehen Ihnen dabei unterschiedliche **Optionen** zur Verfügung.

![Definieren Sie den Eintrag, den Sie zur Tabelle hinzufügen möchten](images/define-record-to-add.png)

Aktivieren Sie abschließend die Automation mit einem Klick auf **Abschicken**.

![Bestätigung der Automation](images/confirm-the-automation.jpg)

## Anwendungsbeispiel

Ein konkreter **Anwendungsfall** für diese Art von Automation könnte beispielsweise auftreten, wenn Sie in einer Tabelle Ihre wöchentlichen Team-Meetings erfassen. Dabei möchten Sie, dass jede Woche vor Beginn des Meetings schon automatisch eine Zeile mit bestimmten Einträgen angelegt wird, damit Sie nur noch die restlichen Informationen manuell eintragen müssen.

In diesem Zusammenhang könnten Sie unter anderem das **Datum** des Meetings, den **Besprechungsraum** und die feststehenden **Themen** vorab definieren.

![Beispieltabelle für den konkreten Anwendungsfall](images/example-table-case-record-to-table.png)

### Anlegen der Automation

Als Erstes geben Sie der Automation einen **Namen** und wählen sowohl die **Tabelle** (hier: Team Meetings) als auch die **Ansicht** (hier: Weekly Team Meeting) aus, in der die Automation wirken soll.

![Benennung der Automation, Auswahl der Tabelle und Ansicht, in welcher die Automation wirken soll](images/basic-settings-automation-example.png)

Als **Trigger-Ereignis** der Automation wählen Sie die Option **Zu einer geplanten Zeit**.

![Auswahl des Trigger-Ereignisses](images/select-trigger.png)

Definieren Sie anschließend, in welchen Abständen die Automation ausgeführt werden soll. Damit die Zeile mit den entsprechenden Einträgen jede Woche der Tabelle hinzugefügt wird, wählen Sie **wöchentlich**.

![Auswahl der zeitlichen Abstände, in denen die Automation ausgeführt werden soll](images/run-frequency.png)

Des Weiteren können Sie sowohl einen konkreten **Wochentag** als auch eine konkrete **Uhrzeit** auswählen, zu welcher die Automation ausgelöst wird. In unserem Anwendungsfall bietet es sich an, als Zeitpunkt eine Stunde vor Beginn des wöchentlichen Meetings am Montagmorgen auszuwählen.

![Auswahl des konkreten Ausführungszeitpunktes der Automation](images/set-weekday-and-hour.png)

Als **automatisierte Aktion** definieren Sie im nächsten Schritt die Aktion **Zeile hinzufügen**.

![Auswahl der automatisierten Aktion](images/select-add-record-as-a-action.png)

Mit einem Klick auf **Feld hinzufügen** können Sie beliebig viele **Einträge** definieren, die automatisch in der Zeile erscheinen.

![Klicken Sie auf Feld hinzufügen, um Einträge zu definieren](images/add-field.png)

Damit in der Zeile automatisch das jeweilige Datum des am selben Tag anstehenden Team-Meetings erfasst wird, wählen Sie die **Datum-Spalte** und den Wert **Der Tag der Ausführung** aus.

![Definition der Einträge](images/definiton-of-the-records.png)

Sie können mit einem Klick auf **Feld hinzufügen** beliebig viele weitere **Einträge** definieren, mit denen die Zeile nach Auslösung der Automation gefüllt wird. Wählen Sie hierzu einfach eine entsprechende **Spalte** Ihrer Tabelle aus dem Drop-down-Menü aus und definieren Sie einen Wert im nebenstehenden Eingabefeld.

![Definieren Sie beliebig viele Einträge ](images/other-records.jpg)

Wenn das Team-Meeting zum Beispiel üblicherweise in einem bestimmten Raum stattfindet, können Sie diesen Raum als gesetzten Wert definieren. Auch falls gewisse Themen (wie z. B. Neuzugänge/Austritte/Jubiläen) bei jedem Team-Meeting auf der Agenda stehen, können Sie diese immer in die Zeile eintragen lassen.

### Testen der Automation

Wenn die Automation funktioniert wie gewünscht, fügt SeaTable Ihrer Tabelle nach Auslösung des Triggers zur geplanten Zeit (hier: immer montags um 7 Uhr) automatisch eine Zeile mit den zuvor definierten **Einträgen** hinzu. Dies erspart Ihnen einige Tastenanschläge und Sie können daraufhin die noch offenen Daten manuell eintragen.

![Tabelle nach der Auslösung der definierten Automation ](images/table-after-automation-new-record-to-current-table.png)

{{< warning  type="warning" headline="Tipp"  text="Damit Sie sich wirklich Arbeit sparen und **nicht** noch Änderungen an automatisch eingetragenen Werten vornehmen müssen, ist es sinnvoll, **ausschließlich** bereits feststehende Werte zu definieren, die Sie im Nachhinein **nicht** mehr manuell anpassen müssen. Anpassungen an den automatisch hinzugefügten Einträgen sind zwar jederzeit möglich, schränken jedoch den Nutzen der Automatisierung erheblich ein." />}}

### Weitere interessante Beispiele von Automationen:

- [Zeilen per Automation sperren]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Verlinken von Einträgen per Automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

- [Einträge in andere Tabellen per Automation hinzufügen]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Benachrichtigungen per Automation versenden]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [E-Mail-Versand per Automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
