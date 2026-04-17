---
title: 'Ausführungslog einer Automation anzeigen'
date: 2023-01-26
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/de/hilfe/ausfuehrungslog-einer-automation-anzeigen'
seo:
    title: 'Ausführungslog von Automationen in SeaTable: Status, Zeit und Warnungen prüfen'
    description: 'Erfahren Sie, wie Sie das Ausführungslog von Automationen in SeaTable Enterprise einsehen: Zeitpunkt, Auslöser, Erfolg und Fehler im Protokoll kontrollieren.'
weight: 8
---

Um die **korrekte Ausführung einer Automation** zu überprüfen, haben Sie die Möglichkeit, das **Ausführungslog** einzusehen. In diesem hält SeaTable für jeden Automationslauf folgende Informationen fest: Ausführungszeit, Ausführungsbedingung, Status und ggf. Warnungen. Zudem gibt es eine übergreifende **Statistik** aller Automationsläufe.

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="Jede Ausführung einer Automation wird als sogenannter **Automationslauf** bezeichnet." />}}

## So werfen Sie einen Blick ins Ausführungslog

![Ausführungslog anzeigen](images/open-automation-log.jpg)

1. Klicken Sie im Base-Header auf {{< seatable-icon icon="dtable-icon-rule" >}} und anschließend auf **Automatisierungsregeln**.
2. Fahren Sie mit dem Mauszeiger über die **Automatisierungsregel**, deren Log Sie einsehen wollen.
3. Klicken Sie auf die **drei Punkte** und dann auf {{< seatable-icon icon="dtable-icon-journal" >}} **Log öffnen**.

## Struktur des Ausführungslogs

![Struktur eines Auführungslogs](images/structure-of-an-automation-log.jpg)

Folgende Informationen können Sie im Ausführungslog einer Automation einsehen:

- **Ausführungszeit**: Hier speichert SeaTable den genauen Zeitpunkt, zu dem der Trigger die Automation ausgelöst hat.

- **Ausführungsbedingung**: Wenn die Automation durch die Änderung oder das Hinzufügen eines Eintrags ausgelöst wird, erscheint die Meldung **per_update**. Bei einem periodisch ausgelösten Automationslauf erscheint hingegen die Meldung **per_day/week/month**.

- **Status**: Der Status gibt an, ob die Automation erfolgreich ausgeführt wurde. Ist dies der Fall, erscheint hier die Meldung **Erfolg**.

- **Warnungen**: Gab es Probleme bei der Ausführung einer Automation, erscheint hier eine entsprechende Warnmeldung.

## Statistik aller Automationsläufe

Zudem können Sie unabhängig von einzelnen Automatisierungsregeln Einsicht in die Statistik nehmen, **wie viele Automationsläufe insgesamt innerhalb der Base stattgefunden haben**. So können Sie herausfinden, wie häufig Ihre Automatisierungsregeln ausgelöst werden und wie viele der Automationsläufe, die Ihnen in Ihrem monatlichen Abonnement zur Verfügung stehen, Sie bereits verbraucht haben.

1. Klicken Sie im geöffneten Automations-Editor oben rechts auf **Statistik**.
![Öffnen Sie die Automationslauf-Statistik](images/open-automation-statistic.png)
2. Daraufhin öffnet sich ein Fenster, in dem Sie die **Anzahl aller ausgeführten Automationen pro Tag** sehen.
![Statistik der Automationsläufe](images/automation-statistic.png)