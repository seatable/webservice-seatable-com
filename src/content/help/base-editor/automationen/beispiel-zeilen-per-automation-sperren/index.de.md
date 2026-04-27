---
title: 'Zeilen per Automation sperren'
date: 2023-01-27
lastmod: '2023-03-31'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/de/hilfe/zeilen-per-automation-sperren'
seo:
    title: 'Zeilen sperren in SeaTable per Automation: Anleitung'
    description: 'So sperren Sie Tabellenzeilen automatisch – Trigger wählen, Bedingungen festlegen und Kontrolle für alle Teammitglieder sicher automatisieren.'
---

Mithilfe von Automationen müssen Sie Zeilen in Ihren Tabellen nicht mehr manuell sperren, sondern können die [Sperrung von Zeilen]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) automatisch ausführen lassen. Das ist sehr nützlich, wenn Sie immer ab einem bestimmten Zeitpunkt (z. B. wenn ein Vorgang abgeschlossen ist) verhindern wollen, dass eine Zeile weiter bearbeitet werden kann.

![Mit einer Automation eine Zeile sperren](images/lock-row-with-an-automation.png)

{{< warning  type="warning" headline="Entsperren nur manuell möglich"  text="Mit einer Automation gesperrte Zeilen können Sie **nicht** auf die gleiche Weise wieder **entsperren**. Dies ist nur manuell und mit den notwendigen **Administratorrechten** möglich." />}}

## Anlegen der Automation

1. Klicken Sie in den Base-Optionen auf {{< seatable-icon icon="dtable-icon-rule" >}} und im Anschluss auf **Automatisierungsregeln**.
2. Klicken Sie auf **Regel hinzufügen**.
3. **Benennen** Sie die Automation und legen Sie die **Tabelle** und **Ansicht** fest, in der sie wirken soll.
4. Definieren Sie ein **Trigger-Ereignis**, welches die Automation auslöst.
5. Klicken Sie auf **Aktion hinzufügen** und wählen Sie als automatisierte Aktion **Eintrag sperren** aus.

![Auswahl der automatisierten Aktion: "Eintrag sperren"](images/lock-record.png) 7. Bestätigen Sie mit **Abschicken**.

{{< warning type="warning" headline="Wichtiger Hinweis" >}}

Die automatisierte Aktion **Eintrag sperren** steht Ihnen ausschließlich bei folgenden Trigger-Ereignissen zur Verfügung:

- Einträge erfüllen nach Bearbeitung bestimmte Bedingungen
- Ein neuer Eintrag wird hinzugefügt
- Periodisch ausführen, wenn Einträge bestimmte Bedingungen erfüllen

{{< /warning >}}

## Anwendungsbeispiel

Möchten Sie beispielsweise in einer Ihrer Tabellen jede Zeile **sperren**, in der ein bestimmter Eintrag einen spezifischen **Wert** erreicht, definieren Sie als Trigger der Automation das Ereignis: **Einträge erfüllen nach Bearbeitung bestimmte Bedingungen**.

![Definition des Trigger-Ereignisses der Automation](images/trigger-example-1.png)

Legen Sie anschließend den **Wert** fest sowie die **Spalte**, in der dieser erreicht werden muss.

![Definition des Trigger-Ereignisses der Automation](images/trigger-example-2.png)

Legen Sie zum Schluss als automatisierte Aktion **Eintrag sperren** fest.

![Definition der automatisierten Aktion](images/automated-action-example.png)

Ab diesem Moment wird die angelegte Automation **alle Zeilen** sperren, in denen sich **Einträge** so verändern, dass sie die Automatisierungsregel erfüllen.

![Definierte automatisierte Aktion: "Eintrag sperren"](images/automated-action-example-2.png)

{{< warning  headline="Bitte beachten"  text="Mit einer Automation können Sie immer nur die Zeilen sperren, in denen sich der Trigger der Automation ereignet hat. Eine Automatisierungsregel nach dem Schema **Ereignis in Zeile X löst Sperrung von Zeile Y aus** ist nicht möglich." />}}

## Mehrere Zeilen gleichzeitig sperren

Automationen sind äußerst hilfreich, wenn Sie mehrere Zeilen gleichzeitig sperren wollen. Wählen Sie dazu den Trigger **Periodisch für Einträge ausführen, die die Bedingungen erfüllen** und legen Sie die entsprechenden Bedingungen fest. Anstatt die Ausführungshäufigkeit und -zeit einzustellen, klicken Sie unten auf **Jetzt ausführen**, um alle gewünschten Zeilen sofort zu sperren.

Mehr Informationen zur Sperrung von Zeilen erhalten Sie im Artikel [Sperren einer Zeile]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}).

### Weitere hilfreiche Artikel in der Rubrik Automationen:

- [Übersicht über Automationen]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [Funktionsweise von Automationen]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Anlegen einer Automation]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Automationen verwalten und gruppieren]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Automationen stoppen]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Automationen löschen]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Ausführungslog einer Automation anzeigen]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Automations-Trigger]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Automations-Aktionen]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Verlinken von Einträgen per Automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

### Weitere interessante Beispiele von Automationen:

- [Verlinken von Einträgen per Automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Zeilen per Automation hinzufügen]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Einträge in andere Tabellen per Automation hinzufügen]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Benachrichtigungen per Automation versenden]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [E-Mail-Versand per Automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
