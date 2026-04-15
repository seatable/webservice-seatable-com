---
title: 'Funktionsweise von Automationen'
date: 2023-01-31
lastmod: '2025-12-01'
categories:
    - 'automationen'
author: 'kgr'
url: '/de/hilfe/funktionsweise-von-automationen'
seo:
    title: 'So funktionieren Automationen in SeaTable'
    description: 'Erfahren Sie, wie Automationen Prozesse in SeaTable automatisieren: Trigger, Aktionen, Bedingungen und Beispiele für effiziente Workflows.'
weight: 4
---


Automationen sind ein mächtiges Feature von SeaTable, mit dem Sie Prozesse automatisieren können. Durch die Automatisierung von Arbeitsschritten sparen Sie nicht nur Zeit, sondern minimieren auch menschliche Fehler bei der Arbeit mit Daten.

## Grundlegende Informationen

- Automationen werden immer als individuelle Automatisierungsregeln angelegt, die sich auf eine bestimmte **Tabellenansicht** beziehen.
- Die beiden wichtigsten Komponenten einer Automation stellen das **Trigger-Ereignis** und die **automatisierte(n) Aktion(en)** dar.

## Trigger-Ereignisse

Als sogenannter Trigger wird ein Ereignis bezeichnet, das als **Auslöser** der Automation fungiert. Dieses Ereignis legen Sie für jede Automatisierungsregel individuell fest. Als Trigger kann fungieren, dass in einer Tabellenansicht **Zeilen hinzugefügt oder bearbeitet wurden**. Ebenso kann ein bestimmter **Zeitpunkt** in einem festgelegten Intervall (täglich, wöchentlich oder monatlich) eine Automation auslösen.

Für bestimmte Ereignisse, wie zum Beispiel das Hinzufügen von Zeilen, können Sie darüber hinaus noch weitere **Einstellungen** vornehmen. So können Sie beispielsweise festlegen, ob **alle Spalten** in der Tabellenansicht oder lediglich ausgewählte Spalten auf das Eintreten des Trigger-Ereignisses hin **überwacht** werden sollen. Wenn Sie in diesem Zusammenhang einzelne Spalten auswählen, wird die Automation auch nur dann ausgelöst, wenn das Ereignis in den ausgewählten Spalten eintritt.

Zusätzlich können Sie die **Bedingungen** des Trigger-Ereignisses so weit eingrenzen, dass die Automation ausschließlich ausgelöst wird, wenn in bestimmten Spalten **bestimmte Daten** zu finden sind. Zum Beispiel können Sie exakte Werte definieren, die in einer ausgewählten Spalte nach dem Hinzufügen oder Bearbeiten der Zeile vorliegen müssen, damit die Automation ausgelöst wird.

Alles Weitere erfahren Sie im Artikel [Automations-Trigger]({{< relref "help/base-editor/automationen/automations-trigger" >}}).

## Automatisierte Aktionen

Als automatisierte Aktionen werden **Prozesse** bezeichnet, die durch das Eintreten des festgelegten Trigger-Ereignisses angestoßen werden. Automatisierte Aktionen sind daher immer eine **Folge** von Trigger-Ereignissen und treten nur auf, wenn jene Ereignisse unter den festgelegten Bedingungen eintreten.

Je nach ausgewähltem Trigger stehen Ihnen dabei unterschiedliche Aktionen zur Auswahl – vom **Versenden einer E-Mail oder Benachrichtigung** an einen oder mehrere Benutzer über das **Hinzufügen, Ändern oder Sperren einer Zeile** bis hin zur **Ausführung von Python-Skripten oder KI-Funktionen**.

{{< warning  type="warning" headline="Hinweis"  text="Selbstverständlich haben Sie die Möglichkeit, einem einzelnen Trigger-Ereignis **mehrere Aktionen** zuzuweisen." />}}

Für viele Aktionen müssen darüber hinaus weitere **Voraussetzungen** erfüllt sein. So brauchen Sie etwa bestimmte Spaltentypen, ein E-Mail-Konto oder Vorlagen im Seitendesign- oder Berichtsdesign-Plugin, um komplexere Automationen möglich zu machen.

Wenn Sie mehr über automatisierte Aktionen lernen möchten, lesen Sie den Artikel [Automations-Aktionen]({{< relref "help/base-editor/automationen/automations-aktionen" >}}).

## Funktionsweise von Automationen

Die Funktionsweise von Automationen wird im Folgenden anhand eines Beispiels ausführlicher erläutert. 

{{< warning headline="Wichtiger Hinweis" text="Das fiktive Beispiel soll mit reduzierter Komplexität die **grundlegende Funktionsweise** von Automationen beleuchten und enthält daher nur eine relativ geringe Datenmenge. Grundsätzlich gilt, dass Automationen in **umfangreicheren Datensätzen** eine noch viel größere Wirkung entfalten." />}}

![Beispiel-Tabelle](images/example-for-a-simple-automation-1.jpg)

Die im Bild zu sehende Beispiel-Tabelle könnten Sie in der Personalabteilung eines Unternehmens verwenden, um neben den Daten von Mitarbeitern deren **Beschäftigungsstatus** sowie den Status der **Gehaltszahlungen** zu erfassen.

Für die Tabellenansicht erstellen Sie anschließend eine **Automation**, die einen Arbeitsschritt automatisieren soll. Konkret soll im Falle des Ausscheidens eines Mitarbeiters, also immer wenn sich der Eintrag in der Spalte **Status** von "beschäftigt" oder "Freelancer" zu "beendet", "Elternzeit" oder "im Ruhestand" ändert, der Eintrag in der Spalte **Payroll** von "aktiv" auf "inaktiv" gesetzt werden.

![Beispiel-Automation](images/example-for-a-simple-automation-2.jpg)

Um diesen Prozessschritt zu automatisieren, definieren Sie als **Trigger** zunächst das Ereignis "Wenn eine Zeile geändert wird". In den Trigger-Einstellungen wählen Sie die **Tabelle** und **Ansicht** aus und geben als **überwachte Spalte** die Spalte "Status" an. Als konkrete **Bedingung** für die Auslösung der Automation legen Sie fest, dass die bearbeitete Zeile in der entsprechenden Spalte den Wert "beendet", "Elternzeit" oder "im Ruhestand" aufweisen muss.

![Definition des Trigger-Ereignisses](images/example-for-a-simple-automation-3.jpg)

Als **automatisierte Aktion** wählen Sie im Anschluss die Option **Eintrag bearbeiten** aus. Konkret soll nach Auslösung des Trigger-Ereignisses der Eintrag in der Spalte "Payroll" von "aktiv" auf "inaktiv" gesetzt werden.

![Definition der automatischen Aktion der Beispiel-Automation](images/example-for-a-simple-automation-4.jpg)

Nachdem Sie die Automation angelegt haben, löst die manuell vorgenommene Änderung in der Spalte "Status" **automatisch** die gewünschte **Anpassung des Eintrags** in der Spalte "Payroll" aus.

![Ausführung der Beispiel-Automation](images/example-for-a-simple-automation.gif)