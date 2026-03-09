---
title: 'Automations-Aktionen'
date: 2023-01-27
lastmod: '2025-11-11'
categories:
    - 'automationen'
author: 'kgr'
url: '/de/hilfe/automations-aktionen'
seo:
    title: 'Automations-Aktionen in SeaTable: Alle Optionen erklärt'
    description: 'Übersicht: Diese Aktionen können Sie mit SeaTable Automationen auslösen – E-Mail-Versand, Links hinzufügen, Skripte, Datenverarbeitung oder KI ausführen, und vieles mehr.'
weight: 6
---

{{< required-version "Enterprise" >}}

**Automatisierte Aktionen** stellen eine der beiden wesentlichen Komponenten von Automationen dar. Die Aktionen werden dabei von definierten **Trigger-Ereignissen** ausgelöst. Je nach [Auslöser]({{< relref "help/base-editor/automationen/automations-trigger" >}}) kann SeaTable unterschiedliche Automations-Aktionen ausführen. Dieser Artikel bietet Ihnen einen **Überblick** über die verschiedenen Arten von automatisierten Aktionen.

## Verfügbare Automations-Aktionen

In der aktuellsten Version von SeaTable stehen ingesamt 13 verschiedene Automations-Aktionen zur Auswahl:

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
- Datenverarbeitungsoperation ausführen
- Seite in PDF umwandeln
- PDF auf Basis eines Dokuments erzeugen und versenden

## Automations-Aktionen hinzufügen, duplizieren, verschieben und löschen

Um eine Aktion hinzuzufügen, klicken Sie auf **die große Schaltfläche mit dem Plus-Symbol** und wählen in der Drop-down-Liste die entsprechende Aktion aus. Beachten Sie dabei, dass sich die verfügbaren Aktionen je nach Trigger unterscheiden.

![Automations-Aktionen hinzufügen](images/automated-actions.jpg)

Wenn Sie bereits aufwändigere Aktionen, wie zum Beispiel E-Mail-Versand, Datenverarbeitung oder KI-Funktionen, eingerichtet haben, können Sie diese auch duplizieren. Klicken Sie einfach auf die **drei Punkte** und dann auf **Duplizieren**. Dadurch müssen Sie diese Aktionen nur geringfügig anpassen und sparen sich eine Menge Zeit. 

![Automations-Aktionen duplizieren](images/duplicate-automated-actions.jpg)

Die Reihenfolge der Aktionen lässt sich ganz einfach **per Drag-and-Drop** ändern. Fahren Sie mit dem Mauszeiger über einen Aktionskasten, halten Sie die linke Maustaste an der **Sechs-Punkte-Greiffläche** gedrückt und verschieben Sie die Aktion an die gewünschte Stelle. So können Sie den Ablauf der Automation flexibel anpassen.

![Automations-Aktionen verschieben](images/move-automated-actions.gif)

Natürlich können Sie nicht mehr benötigte Aktionen auch löschen. Klicken Sie dazu auf die **drei Punkte** und dann auf **Löschen**. Beachten Sie, dass die automatisierten Aktionen **sofort und endgültig** entfernt werden und nicht wiederhergestellt werden können.

![Automations-Aktionen löschen](images/delete-automated-actions.gif)

## Automations-Aktion: Benachrichtigung versenden

Indem Sie "Benachrichtigung versenden" als automatisierte Aktion definieren, können Sie eine Benachrichtigung an einen oder mehrere Benutzer einstellen. Die ausgewählten Benutzer erhalten jedes Mal eine **Benachrichtigung**, wenn der entsprechende Trigger ausgelöst wird. Diese Automations-Aktion steht Ihnen **bei allen Automations-Triggern** zur Verfügung.

**Empfänger** und **Inhalt** der Benachrichtigungen können Sie jederzeit in den **Einstellungen** der Aktion bearbeiten. Bei den Empfängern können Sie konkret **einzelne Nutzer** auswählen oder Nutzer in einer bestimmten Spalte vom Typ [Mitarbeiter]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), [Ersteller]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) oder [Letzter Bearbeiter]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}) benachrichtigen. Schreiben Sie die gewünschte Nachricht in das Textfeld und arbeiten Sie mit Spaltenreferenzen in geschweiften Klammern, um bestimmte Werte einzufügen.

![Benachrichtigung per Automation versenden](images/send-notification-action-settings.jpg)

Die Nutzer können ihre Benachrichtigungen über das {{< seatable-icon icon="dtable-icon-notice" >}} **Glocken-Symbol** neben ihrem Avatar in der rechten oberen Ecke abrufen.

![Eingegangene Benachrichtigung](images/example-action-notification.png)

Der Artikel [Benachrichtigungen per Automation versenden]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}}) spielt diese Automation anhand eines konkreten Anwendungsfalls durch.

## Automations-Aktion: App-Benachrichtigung versenden

Indem Sie "App-Benachrichtigung versenden" als automatisierte Aktion definieren, können Sie eine Benachrichtigung an einen oder mehrere Benutzer einer App einstellen. Die ausgewählten Benutzer erhalten jedes Mal eine **Benachrichtigung** in der App, wenn der entsprechende Trigger ausgelöst wird. Diese Automations-Aktion steht Ihnen **bei allen Automations-Triggern** zur Verfügung.

In den **Einstellungen** der Aktion können Sie definieren, an welche **App** und welche **Empfänger** die Benachrichtigungen gesendet werden sollen. Bei den Empfängern können Sie konkret **einzelne App-Nutzer** auswählen oder Nutzer in einer bestimmten Spalte vom Typ **Mitarbeiter, Ersteller oder Letzter Bearbeiter** benachrichtigen. Schreiben Sie den gewünschten **Inhalt** der Benachrichtigung in das Textfeld. Nutzen Sie dabei Spaltenreferenzen in geschweiften Klammern, um bestimmte Werte einzufügen.

![App-Benachrichtigung per Automation senden](images/send-app-notification-action-settings.jpg)

Die Nutzer der jeweiligen App können ihre Benachrichtigungen über das {{< seatable-icon icon="dtable-icon-notice" >}} **Glocken-Symbol** neben ihrem Avatar in der rechten oberen Ecke abrufen.

![Benachrichtigung in der App abrufen](images/check-app-notifications.jpg)

## Automations-Aktion: E-Mail versenden

Indem Sie "E-Mail versenden" als automatisierte Aktion definieren, können Sie vordefinierte E-Mails an einen oder mehrere Benutzer versenden. Dabei schickt SeaTable an jeden ausgewählten Benutzer eine **E-Mail**, sobald der entsprechende Trigger ausgelöst wird. Diese Automations-Aktion steht Ihnen **bei allen Automations-Triggern** zur Verfügung.

**E-Mail-Konto**, **Betreff**, **Empfänger**, **Nachricht** und **Anhänge** der E-Mail können Sie jederzeit in den **Einstellungen** der Aktion bearbeiten. Nutzen Sie dabei Spaltenreferenzen in geschweiften Klammern, um bestimmte Werte in Textfelder einzufügen.

![Definition der Automations-Aktion: E-Mail versenden](images/send-email-action-settings.jpg)

Der Artikel [E-Mail-Versand per Automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}) spielt diese Automation anhand eines konkreten Anwendungsfalls durch.

## Automations-Aktion: Zeile hinzufügen

Wenn Sie "Zeile hinzufügen" als automatisierte Aktion definieren, wird jedes Mal, sobald der entsprechende Trigger ausgelöst wird, eine **neue Zeile** in die Tabelle eingefügt. Die genauen Werte können Sie im Vorhinein für jede Spalte individuell bestimmen.

![Automations-Aktion: Zeile hinzufügen](images/add-record-action-settings.jpg)

Die Automations-Aktion "Zeile hinzufügen" steht Ihnen derzeit bei folgenden **Automations-Triggern** zur Verfügung:
- Wenn eine Zeile geändert wird
- Wenn eine Zeile hinzufügt wird
- Zu einer geplanten Zeit

Der Artikel [Zeilen per Automation hinzufügen]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}}) spielt diese Automation anhand eines konkreten Anwendungsfalls durch.

## Automations-Aktion: Eintrag sperren

Wenn Sie "Eintrag sperren" als automatisierte Aktion definieren, wird die **Zeile**, welche die Automation ausgelöst hat, für die Bearbeitung gesperrt. Sie können bei dieser Aktion keine weiteren Einstellungen vornehmen – die Bedingungen für die Zeilensperrung müssen Sie beim **Trigger** konfigurieren. Beachten Sie dabei, dass Sie gesperrte Zeilen ohne Administratorrechte nicht mehr **entsperren** können.

![Definition der Automations-Aktion: Sperren eines Eintrags in der Tabelle](images/lock-record-action.jpg)

![Durch eine Automation ausgelöste Sperrung eines Eintrag in einer Tabelle ](images/example-locked-records.jpg)

Die Automations-Aktion "Eintrag sperren" steht Ihnen derzeit bei folgenden **Automations-Triggern** zur Verfügung:
- Wenn eine Zeile geändert wird
- Wenn eine Zeile hinzufügt wird
- Zu einer geplanten Zeit für Einträge, die bestimmte Bedingungen erfüllen

Der Artikel [Zeilen per Automation sperren]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}) spielt diese Automation anhand eines konkreten Anwendungsfalls durch.

## Automations-Aktion: Eintrag bearbeiten

Wenn Sie "Eintrag bearbeiten" als automatisierte Aktion auswählen, werden **Zeilen** in der Tabelle nach Auslösung des Triggers gemäß den im Vorhinein definierten **Einstellungen** angepasst. Dabei können Sie für jede Spalte einen Wert festlegen, den die Zeilen nach der Änderung automatisch annehmen.

![Automations-Aktion: Eintrag anpassen](images/modify-record-action-settings.jpg)

Die Automations-Aktion "Eintrag bearbeiten" steht Ihnen derzeit bei folgenden **Automations-Triggern** zur Verfügung:
- Wenn eine Zeile geändert wird
- Wenn eine Zeile hinzufügt wird
- Zu einer geplanten Zeit für Einträge, die bestimmte Bedingungen erfüllen

## Automations-Aktion: Links hinzufügen

Wenn Sie "Links hinzufügen" als automatisierte Aktion auswählen, wird in der entsprechenden Spalte bei Auslösung des Triggers eine [Verknüpfung zu anderen Einträgen]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) hergestellt. In den **Einstellungen** der Aktion können Sie dabei genauestens festlegen, unter welchen Bedingungen welcher Link in der Tabelle hinzugefügt wird.

![Automations-Aktion: Hinzufügen von Verlinkungen](images/add-links-action-settings.jpg)

Die Automations-Aktion "Links hinzufügen" steht Ihnen derzeit bei folgenden **Automations-Triggern** zur Verfügung:
- Wenn eine Zeile geändert wird
- Wenn eine Zeile hinzufügt wird
- Zu einer geplanten Zeit

Der Artikel [Verlinken von Einträgen per Automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}}) spielt diese Automation anhand eines konkreten Anwendungsfalls durch.

## Automations-Aktion: Neuen Eintrag in anderer Tabelle hinzufügen

Wenn Sie "Neuen Eintrag in anderer Tabelle hinzufügen" als automatisierte Aktion auswählen, wird bei Auslösung des Triggers eine **Zeile in einer anderen Tabelle** erstellt. In den **Einstellungen** der Aktion können Sie dabei für jede Spalte individuelle Werte definieren, die den Zeilen in der ausgewählten Tabelle im Zuge der Automation zugewiesen werden. Ebenso können Sie Spalten des gleichen Typs in der Ursprungstabelle auswählen, um Zeileneinträge in die andere Tabelle zu kopieren.

![Automations-Aktion: Hinzufügen einer Zeile in einer anderen Tabelle](images/add-record-to-other-table-action-settings.jpg)

Die Automations-Aktion "Neuen Eintrag in anderer Tabelle hinzufügen" steht Ihnen derzeit bei folgenden **Automations-Triggern** zur Verfügung:
- Wenn eine Zeile geändert wird
- Wenn eine Zeile hinzufügt wird

Der Artikel [Einträge in andere Tabellen per Automation hinzufügen]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) spielt diese Automation anhand eines konkreten Anwendungsfalls durch.

## Automations-Aktion: Python-Skript ausführen

Wenn Sie die Ausführung eines Python-Skripts als automatisierte Aktion auswählen, setzt der Trigger ein im Vorhinein definiertes **Python-Skript** in Gang. Das Skript können Sie jederzeit im [Skript-Editor]({{< relref "help/skripte/allgemein/anlegen-und-loeschen-eines-skriptes" >}}) anlegen oder bearbeiten und dann in den **Einstellungen** der Aktion auswählen.

![Automations-Aktion: Python-Skript ausführen](images/run-python-script-action-settings.jpg)

Die Automations-Aktion "Python-Skript ausführen" steht Ihnen derzeit bei folgenden **Automations-Triggern** zur Verfügung:
- Wenn eine Zeile geändert wird
- Wenn eine Zeile hinzufügt wird
- Zu einer geplanten Zeit

## Automations-Aktion: KI aufrufen

Wenn Sie die Ausführung einer KI-Funktion als automatisierte Aktion auswählen, ruft der Trigger ein **KI-Modell** auf den Plan, das eine im Vorhinein definierte Aktion in der Tabelle ausführt. Die auszuführende Aktion können Sie in den **Einstellungen** genau konfigurieren. Je nach Art der KI-Funktion können dabei **Input-Spalten**, **Output-Spalten** und ein **Prompt** erforderlich sein.

![Definition einer Automations-Aktion: KI ausführen](images/run-ai-action-settings.jpg)

Folgende **KI-Funktionen** können Sie mit einer Automation ausführen lassen:

- **Zusammenfassen**: Fasst den Text aus einer oder mehreren Spalten zusammen. Sie können die Länge, den Ton, das Format und die Sprache der Zusammenfassung durch Anpassen des Prompts steuern.
- **Klassifizieren**: Klassifiziert Datensätze aus einer oder mehreren Spalten. Sie können die Kategorien und die Regeln durch den Prompt anpassen. Das Ergebnis landet in einer [Einfachauswahl-]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) oder [Mehrfachauswahl-Spalte]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}).
- **OCR**: Extrahiert Text aus einer [Bild-Spalte]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}). Der erkannte Inhalt wird in die Ergebnisspalte vom Typ [Text oder Formatierter Text]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) geschrieben.
- **Extrahieren**: Extrahiert bestimmte Informationen aus einer Spalte vom Typ Text oder Zahl entsprechend Ihrer Anforderung. Die extrahierten Informationen werden in die Ergebnisspalten geschrieben.
- **Benutzerdefiniert**: Erzeugt Inhalte basierend auf Ihrem Prompt. Verwenden Sie {Spaltennamen} in geschweiften Klammern, um den Spaltenwert einer Zeile einzufügen.

![Mithilfe eines KI-Modells ausführbare Aktionen](images/run-ai-functions.jpg)

Die Automations-Aktion "KI aufrufen" steht Ihnen derzeit bei folgenden **Automations-Triggern** zur Verfügung:
- Wenn eine Zeile geändert wird
- Wenn eine Zeile hinzufügt wird

Ausführliche Anleitungen zu den einzelnen KI-Funktionen mit Schritt-für-Schritt-Beispielen finden Sie im Bereich [KI-Automationen]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}).

## Automations-Aktion: Datenverarbeitungsoperation ausführen

Wenn Sie die Ausführung einer Datenverarbeitungsoperation als automatisierte Aktion auswählen, löst der Trigger eine im Vorhinein definierte [Datenverarbeitungsoperation]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) in der Tabelle aus. Die auszuführende Aktion können Sie in den **Einstellungen** genau konfigurieren. Je nach Art der Operation können **bestimmte Input- und Output-Spalten** notwendig sein.

![Definition einer Automations-Aktion: Datenverarbeitungsoperation ausführen](images/run-data-processing-action-settings.jpg)

Folgende **Datenverarbeitungsoperationen** können Sie mit einer Automation ausführen lassen:

- [Veränderungen berechnen]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Prozentualen Anteil berechnen]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})
- [Rangliste berechnen]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Benutzernamen übertragen]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})
- [Vergleichen und kopieren]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})

![Mithilfe einer Automation ausführbare Datenverarbeitungsoperationen](images/run-data-processing-available-operations.jpg)

Die Automations-Aktion "Datenverarbeitungsoperation ausführen" steht Ihnen derzeit bei folgendem **Automations-Trigger** zur Verfügung:
- Zu einer geplanten Zeit

## Automations-Aktion: Seite in PDF umwandeln

Wenn Sie "Seite in PDF umwandeln" als automatisierte Aktion auswählen, wird SeaTable bei Auslösung des Triggers **ein PDF-Dokument aus dem Datensatz erzeugen** und dieses in einer [Datei-Spalte]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) speichern. Wählen Sie dafür eine **Vorlage** aus, die Sie zuvor im [Seitendesign-Plugin]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}) erstellt haben. In den Einstellungen der Aktion können Sie auch den **Dateinamen** definieren.

![PDF per Automation erstellen](images/convert-page-to-pdf-action-settings.jpg)

Die Automations-Aktion "Seite in PDF umwandeln" steht Ihnen derzeit bei folgendem **Automations-Trigger** zur Verfügung:
- Zu einer geplanten Zeit für Einträge, die bestimmte Bedingungen erfüllen

## Automations-Aktion: PDF auf Basis eines Dokuments erzeugen und versenden

Wenn Sie "PDF auf Basis eines Dokuments erzeugen und versenden" als automatisierte Aktion auswählen, wird SeaTable bei Auslösung des Triggers **ein PDF-Dokument erzeugen** und dieses in der [Dateiverwaltung]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}) speichern. Darüber hinaus kann SeaTable es direkt per E-Mail verschicken.

In den **Einstellungen** der Aktion wählen Sie dafür eine **Vorlage** aus, die Sie zuvor im **Berichtsdesign-Plugin** erstellt haben, und vergeben einen **Dateinamen**. Aktivieren Sie dann den Regler, um einen **eigenen Ordner** auszuwählen, in den Sie die Datei speichern möchten. Wenn Sie das Dokument nur generieren möchten, können Sie die Konfiguration an dieser Stelle beenden.

![PDF per Automation aus einem Berichtsdesign erstellen und versenden](images/generate-pdf-from-document-action-settings.jpg)

Wenn Sie das generierte Dokument anschließend versenden möchten, aktivieren Sie den Regler "An E-Mail senden". **E-Mail-Konto**, **Empfänger**, **Betreff** und **Nachricht** der E-Mail können Sie jederzeit in den **Einstellungen** der Aktion bearbeiten.

![PDF per Automation aus einem Berichtsdesign erstellen und versenden](images/generate-pdf-from-document-and-send-action-settings.jpg)

Die Automations-Aktion "PDF auf Basis eines Dokuments erzeugen und versenden" steht Ihnen derzeit bei folgendem **Automations-Trigger** zur Verfügung:
- Zu einer geplanten Zeit
