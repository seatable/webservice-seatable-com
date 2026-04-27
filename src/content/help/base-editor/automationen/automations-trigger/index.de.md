---
title: 'Automations-Trigger'
date: 2023-01-27
lastmod: '2025-11-11'
categories:
    - 'automationen'
author: 'kgr'
url: '/de/hilfe/automations-trigger'
seo:
    title: 'Automations-Trigger in SeaTable: alle Möglichkeiten'
    description: 'Diese Übersicht zeigt, welche Trigger-Ereignisse SeaTable für Automationen bietet – inkl. Einstellungen und unterstützter Aktionen.'
weight: 5
---

**Trigger-Ereignisse** stellen eine der beiden wesentlichen Komponenten von Automationen dar. Die Ereignisse lösen dabei verschiedene Arten von [Aktionen]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) aus, die Sie für jede Automation individuell festlegen können. Dieser Artikel bietet Ihnen einen **Überblick** über die verschiedenen Arten von Auslösern.

## Verfügbare Automations-Trigger

In der aktuellsten Version von SeaTable stehen ingesamt **vier** verschiedene Auslöser zur Auswahl:

![Momentan zur Verfügung stehende Trigger-Ereignisse](images/automation-triggers.jpg)

- Wenn eine Zeile geändert wird
- Wenn eine Zeile hinzugefügt wird
- Zu einer geplanten Zeit
- Zu einer geplanten Zeit für Einträge, die bestimmte Bedingungen erfüllen

## Trigger-Einstellungen

Um einen Trigger anzulegen oder zu bearbeiten, klicken Sie auf den entsprechenden Kasten im zentralen Bereich des Automations-Editors. Anschließend erscheinen rechts die Trigger-Einstellungen.

![Trigger-Einstellungen](images/automation-trigger-settings.jpg)

- Mithilfe des Drop-down-Menüs können Sie zuerst den **Auslöser** ändern. Wählen Sie dazu das gewünschte Trigger-Ereignis aus.
- Definieren Sie anschließend die **Tabelle** und die **Ansicht**, in der die Automation wirken soll.
- Je nach Art des Triggers können Sie noch weitere Einstellungen vornehmen, z. B. **überwachte Spalten**, **Bedingungen** für die Auslösung oder den **Zeitpunkt** der Auslösung.

![Trigger-Einstellungen im Detail](images/automation-trigger-settings.gif)

{{< warning headline="Änderungen speichern" text="Vergessen Sie nicht, die Trigger-Einstellungen zu **speichern**! Ansonsten gehen beim Schließen des Fensters alle Änderungen verloren." />}}

## Automations-Trigger: Wenn eine Zeile geändert wird

Wenn Sie dieses Ereignis als Trigger auswählen, wird die entsprechende Automation jedes Mal ausgelöst, wenn ein Wert in einer der überwachten Spalten geändert wird und eine Zeile in der ausgewählten Ansicht nach der Bearbeitung bestimmte Bedingungen erfüllt. Wenn der Trigger bei jeder Änderung auslösen soll, dann fügen Sie keine Bedingungen hinzu.

Bei den **Bedingungen** können Sie individuell für jede Spalte festlegen, wie der entsprechende Wert nach der Bearbeitung aussehen muss, damit die Automation in Gang kommt. Im Zuge dessen können Sie entscheiden, ob alle oder lediglich ausgewählte Spalten der Ansicht auf das Eintreten des Trigger-Ereignisses hin überwacht werden sollen.

![Trigger-Einstellungen, wenn eine Zeile geändert wird](images/automation-trigger-when-a-row-is-updated.jpg)

Wenn Sie dieses Ereignis als Trigger einer Automation auswählen, stehen Ihnen folgende **automatische Aktionen** zur Auswahl:

- Benachrichtigung versenden
- App-Benachrichtigung versenden
- E-Mail versenden
- Zeile hinzufügen
- Eintrag sperren
- Eintrag bearbeiten
- Links hinzufügen
- Neuen Eintrag in anderer Tabelle hinzufügen
- Python-Skript ausführen
- KI aufrufen

## Automations-Trigger: Wenn eine Zeile hinzugefügt wird

Wenn Sie dieses Ereignis als Trigger auswählen, wird die entsprechende Automation jedes Mal ausgelöst, wenn in der ausgewählten Ansicht eine **neue Zeile** hinzugefügt wird. Darüber hinaus können Sie das Eintreten des Ereignisses weiter einschränken, indem Sie **Bedingungen** festlegen, welche die neue Zeile erfüllen muss.

![Trigger-Einstellungen, wenn eine Zeile hinzugefügt wird](images/automation-trigger-when-a-row-is-added.jpg)

Bei den Bedingungen können Sie individuell für jede Spalte festlegen, wie der entsprechende Wert aussehen muss, damit die Automation in Gang kommt. Wenn Sie möchten, dass jede neue Zeile die Automation auslöst, dann fügen Sie keine Bedingungen hinzu.

{{< warning headline="Tipp" text="Dieser Auslöser ist zum Beispiel besonders nützlich, wenn Sie neue Datensätze importieren oder über Formulare erfassen." />}}

Wenn Sie dieses Ereignis als Trigger einer Automation auswählen, stehen Ihnen folgende **automatische Aktionen** zur Auswahl:

- Benachrichtigung versenden
- App-Benachrichtigung versenden
- E-Mail versenden
- Zeile hinzufügen
- Eintrag sperren
- Eintrag bearbeiten
- Links hinzufügen
- Neuen Eintrag in anderer Tabelle hinzufügen
- Python-Skript ausführen
- KI aufrufen

## Automations-Trigger: Zu einer geplanten Zeit

Wenn Sie diesen Auslöser wählen, können Sie anschließend einen **Zeitpunkt** definieren, zu dem die Automation **täglich**, **wöchentlich** oder **monatlich** abläuft. 

![Einstellungsoptionen für einen täglichen Trigger zu einer geplanten Zeit](images/automation-trigger-at-scheduled-time.jpg)

Während Sie für eine tägliche Automation nur die **Uhrzeit** festlegen können, können Sie für eine wöchentliche Automation auch den **Wochentag** bzw. für eine monatliche Automation den **Kalendertag** angeben.

![Einstellungsoptionen für einen wöchentlichen Trigger zu einer geplanten Zeit](images/automation-trigger-at-scheduled-time-weekly.jpg)

Wenn Sie diesen Auslöser für eine Automation festlegen, stehen Ihnen folgende **automatische Aktionen** zur Auswahl:

- Benachrichtigung versenden
- App-Benachrichtigung versenden
- E-Mail versenden
- Zeile hinzufügen
- Links hinzufügen
- Python-Skript ausführen
- KI aufrufen
- Datenverarbeitungsoperation ausführen
- PDF auf Basis eines Dokuments erzeugen und versenden

## Automations-Trigger: Zu einer geplanten Zeit für Einträge, die bestimmte Bedingungen erfüllen

Bei diesem Trigger geben Sie kongruent zum zuvor genannten Trigger einen **Zeitpunkt** an, zu dem die Automation **täglich**, **wöchentlich** oder **monatlich** ausgelöst wird. Darüber hinaus können Sie die Zeilen eingrenzen, die von diesem Trigger-Ereignis betroffen sind. 

Bei den **Bedingungen** können Sie individuell für jede Spalte festlegen, wie der entsprechende Wert aussehen muss, damit die Automation zum festgelegten Zeitpunkt vollzogen wird.

![Trigger zu einer geplanten Zeit für Einträge, die bestimmte Bedingungen erfüllen](images/automation-trigger-at-scheduled-time-for-records-that-match-condition.jpg)

Wenn Sie diesen Auslöser für eine Automation auswählen, stehen Ihnen folgende **automatische Aktionen** zur Auswahl:

- Benachrichtigung versenden
- App-Benachrichtigung versenden
- E-Mail versenden
- Eintrag sperren
- Eintrag bearbeiten
- Seite in PDF umwandeln
