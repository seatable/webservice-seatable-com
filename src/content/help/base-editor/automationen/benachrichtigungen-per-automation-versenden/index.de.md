---
title: 'Benachrichtigungen per Automation versenden'
date: 2023-02-27
lastmod: '2023-03-31'
categories:
    - 'benachrichtigungen'
author: 'nsc2'
url: '/de/hilfe/benachrichtigungen-per-automation-versenden'
seo:
    title: 'Benachrichtigungen per Automation in SeaTable versenden'
    description: 'Automatisiere Benachrichtigungen – so richtest du in SeaTable eine Regel ein, die automatisch Mitteilungen an Deutsch, Englisch, Spanisch, Französisch, Portugiesisch, Russisch und Chinesisch sprechende Nutzer versendet.'

---


Wenn Sie über ein Enterprise-Abo verfügen, können Sie Benachrichtigungen auch per Automation an ausgewählte Benutzer versenden. Definieren Sie hierfür einfach eine entsprechende Automatisierungsregel für eine beliebige Tabellenansicht.

## Benachrichtigungen per Automation versenden

![E-Mails versenden per Automation](images/how-to-use-automations-for-locking-rows-3.png)

1. Klicken Sie im Base-Header auf {{< seatable-icon icon="dtable-icon-rule" >}} und im Anschluss auf **Automatisierungsregeln**.
2. Klicken Sie auf **Regel hinzufügen**.
3. Geben Sie der Automation einen **Namen** und legen Sie die **Tabelle** und die **Ansicht** fest, in der diese wirken soll.
4. Definieren Sie ein **Trigger-Ereignis**, welches die Automation auslöst.
5. Klicken Sie auf **Aktion hinzufügen** und wählen Sie als automatisierte Aktion **Benachrichtigung versenden** aus.
6. Bestätigen Sie mit **Abschicken**.

## Anlegen der Automation

Definieren Sie für die Automation zunächst ein **Trigger-Ereignis**.

![Grundsätzlich zur Auswahl stehende Trigger-Ereignisse](images/trigger-options-for-archivating-rows.png)

Die **vier Optionen** sind:

- Einträge erfüllen nach Bearbeitung bestimmte Bedingungen
- Ein neuer Eintrag wird hinzugefügt
- Periodischer Trigger
- Periodischer Trigger für Einträge, die eine bestimmte Bedingung erfüllen

Wählen Sie anschließend als automatisierte Aktion **Benachrichtigung versenden** aus. Diese steht Ihnen bei allen vier Trigger-Optionen als Aktion zur Verfügung.

![Hinzufügen der automatisierten Aktion](images/add-an-action.png) ![Hinzufügen der automatisierten Aktion](images/send-notification.png)

Im nächsten Schritt wählen Sie die **Benutzer** aus, die benachrichtigt werden sollen, wenn das Trigger-Ereignis eintritt. Beachten Sie dabei, dass Sie hier ausschließlich Benutzer auswählen können, die mindestens **Lesezugriff** auf die Tabelle oder Ansicht haben.

![Auswahl der Benutzer, die benachrichtigt werden sollen ](images/select-users-to-get-notified.png)

Im letzten Schritt fügen Sie den **Inhalt** der Benachrichtigung in das vorgesehene **Textfeld** ein. Um auf Einträge in der Tabelle zu verweisen, schreiben Sie einfach den Namen der Spalten in geschweiften Klammern in den Text.

![Hinzufügen des Inhalts der zu versendeten Benachrichtigungen ](images/content-of-the-notification.png)

Speichern Sie die Automation mit einem Klick auf **Abschicken**.

## Anwendungsbeispiel

Ein konkreter **Anwendungsfall** für diese Art von Automation könnte beispielsweise auftreten, wenn Sie als Führungskraft in einem Unternehmen arbeiten und für Ihre Mitarbeiter die Buchung von diversen Schulungen in Auftrag geben möchten. Dabei möchten Sie die Personalabteilung, welche die Schulungen letztlich bucht, automatisch darüber informieren, welche Schulung Ihre Mitarbeiter besuchen möchten.

Konkret umsetzen lässt sich dies mithilfe einer Tabelle, in der verschiedene **Daten** der Mitarbeiter Ihres Unternehmens gepflegt werden. Erheben könnten Sie in diesem Zusammenhang unter anderem die **Namen** der Mitarbeiter, die **Abteilung** und die letzte von ihnen gebuchte Schulung.

![Beispieltabelle des konkreten Anwendungsfalls der Automation](images/beispieltabelle-anwendungsfall.png)

Mithilfe einer Automation soll nun automatisch bei jeder neu beantragten Buchung in der Tabelle eine **Benachrichtigung** an ausgewählte Mitarbeiter der Personalabteilung versandt werden, damit diese die Buchung der beantragten Schulung für den entsprechenden Mitarbeiter in die Wege leiten.

### Anlegen der Automation

Als Erstes geben Sie der Automation einen **Namen** (z. B. notification if training is booked) und wählen sowohl die Tabelle (hier: employees & trainings) als auch die Ansicht aus, in der die Automation wirken soll.

![Benennung der Automation und Definition der Tabelle und  Ansicht, in welcher diese wirken soll](images/definition-of-the-automation-1.png)

Als **Trigger-Ereignis** der Automation wählen Sie die Option "Einträge erfüllen nach Bearbeitung bestimmte Bedingungen".

![Auswahl des Trigger-Ereignisses](images/trigger-condition.png)

Damit die Benachrichtigungen ausschließlich im Falle der Beantragung einer neuen Schulung versandt werden, fügen Sie als **Filter-Bedingung** hinzu, dass der Eintrag in der Spalte "last training booked" auf eine der möglichen **Auswahloptionen** in dieser Spalte geändert werden muss.

![Hinzufügen einer Filterbedingung](images/set-filter-condition.png)

Als **automatisierte Aktion** definieren Sie anschließend die Aktion "Benachrichtigung versenden".

![Hinzufügen der automatisierten Aktion](images/send-notification.png)

Im nächsten Schritt wählen Sie im Drop-down-Feld die **Mitarbeiter** der Personalabteilung aus, an welche die **Benachrichtigung** bei Auslösung des Triggers gesendet werden soll.

![Auswahl der zu benachrichtigenden Benutzer ](images/select-users-to-get-notified-example.png)

Im letzten Schritt können Sie den **Inhalt** der zu versendenden Benachrichtigung in das vorgesehene Textfeld schreiben.

![Hinzufügen des Inhalts der Benachrichtigung ](images/content-of-the-notification-example.png)

{{< warning  headline="Tipp"  text="Mithilfe von geschweiften Klammern können Sie die **Inhalte der Tabellenspalten** in der Benachrichtigung zitieren. Nutzen Sie diese Funktion, um die **Namen** der Mitarbeiter sowie den Namen des beantragten **Trainings** der Benachrichtigung hinzuzufügen." />}}

### Testen der Automation

Wenn Sie im Anschluss in der ausgewählten Tabelle eine neue Schulung für einen Mitarbeiter beantragen, d.h. den Eintrag in der Spalte "**last training booked**" auf die zuletzt beantragte Schulung ändern, wird die vorgefertigte **Benachrichtigung** automatisch an die ausgewählten Benutzer der Personalabteilung versandt.

Die Mitarbeiter in der Personalabteilung erhalten in der Benachrichtigung, die sie über das Glocken-Symbol {{< seatable-icon icon="dtable-icon-notice" >}} erreichen, die Information, dass eine Schulung beantragt wurde, und können die ausgewählte Schulung für den entsprechenden Mitarbeiter in die Wege leiten.

![An die ausgewählten Benutzer versendete Benachrichtigung nach Auslösung des Trigger-Ereignisses](images/notification-after-trigger.png)

### Weitere interessante Beispiele für Automationen:

- [Zeilen per Automation sperren]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Verlinken von Einträgen per Automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Zeilen per Automation hinzufügen]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Einträge in andere Tabellen per Automation hinzufügen]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [E-Mail-Versand per Automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
