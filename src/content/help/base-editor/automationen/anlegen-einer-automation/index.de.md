---
title: 'Anlegen einer Automation'
date: 2022-12-06
lastmod: '2025-11-04'
categories:
    - 'automationen'
author: 'kgr'
url: '/de/hilfe/anlegen-einer-automation'
seo:
    title: 'Automation in SeaTable anlegen – Schritt für Schritt'
    description: 'Lernen Sie, wie Sie in SeaTable Automationen erstellen: Trigger, Aktionen und Bedingungen für effiziente, fehlerfreie Workflows in Ihrer Base.'
weight: 2
---

Mithilfe von Automationen können Sie **Prozesse automatisieren**. So sparen Sie nicht nur Zeit, sondern minimieren auch die Anzahl menschlicher Fehler. Den ersten Schritt hin zu automatisierten Workflows stellt dabei das Anlegen einer Automation dar.

## Eine Automatisierungsregel anlegen

1. Öffnen Sie die **Base**, in der Sie eine Automation anlegen möchten.

![Automationen anlegen](images/how-to-use-automations.jpg)

2. Klicken Sie im Base-Header auf {{< seatable-icon icon="dtable-icon-rule" >}} und anschließend auf **Automatisierungsregeln**.

3. Klicken Sie auf **Regel oder Ordner hinzufügen** und dann auf **Regel**.

![Automation erstellen](images/add-automation.jpg)

4. Geben Sie der Automatisierungsregel einen **Namen**.

5. Erstellen Sie die gewünschte Automation, indem Sie einen **Trigger** und verschiedene **Aktionen** festlegen.

{{< warning headline="Tipp" text="Wenn in der Base noch keine Regeln existieren, können Sie **für die allererste Automation** auch direkt einen Trigger auswählen – und SeaTable legt automatisch eine Regel an." />}}

![Abkürzung für die erste Automation](images/shortcut-add-first-automation.gif)

### Eine Automatisierungsregel in einem Ordner anlegen

Wenn Sie bereits einen Ordner für Automatisierungsregeln angelegt haben, können Sie auch direkt im Ordner eine Regel anlegen. Bewegen Sie dazu den Mauszeiger auf den Ordner, klicken Sie auf die **drei Punkte** und auf **Regel hinzufügen**.

![Automatisierungsregel in einem Ordner anlegen](images/add-automation-in-folder.jpg)

## Weitere Automationsschritte

### Verwaltung

Zunächst können Sie die neue Automatisierungsregel verwalten, zum Beispiel **umbenennen**, **löschen** oder **in einen Ordner verschieben**.

{{< button label="Mehr zur Verwaltung von Automatisierungsregeln" link="help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}}

### Trigger

Im nächsten Schritt definieren Sie ein Ereignis, welches als Trigger dient und die Automation auslöst. Hier legen Sie auch fest, in welcher **Tabelle** und in welcher **Ansicht** die Automation wirken soll. Der **Auslöser** kann sein, dass eine Zeile hinzugefügt wird oder nach einer Änderung bestimmte Bedingungen erfüllt. Darüber hinaus können Sie auch einstellen, dass die Automation täglich, wöchentlich oder monatlich zu einem bestimmten Zeitpunkt ausgelöst wird.

![Trigger-Einstellungen](images/trigger-settings.jpg)

{{< button label="Mehr zu Automations-Triggern" link="help/base-editor/automationen/automations-trigger" >}}

### Aktionen

Abschließend legen Sie eine oder mehrere **Aktionen** fest, die durch das zuvor definierte Trigger-Ereignis angestoßen werden. Mögliche Aktionen können je nach Art des Auslösers beispielsweise das Versenden von Benachrichtigungen und E-Mails, das Hinzufügen oder Sperren von Einträgen oder die Ausführung einer KI-Funktion sein.

![Weitere Automationsschritte](images/steps-for-automation.jpg)

{{< button label="Mehr zu Automations-Aktionen" link="help/base-editor/automationen/automations-aktionen" >}}