---
title: 'Die Mitarbeiter-Spalte'
date: 2023-01-07
lastmod: '2024-02-14'
categories:
    - 'datum-dauer-und-personen'
author: 'ssc'
url: '/de/hilfe/die-spalte-mitarbeiter'
seo:
    title: 'Die Mitarbeiter-Spalte in SeaTable: Personen zuordnen und Benachrichtigungen'
    description: 'Mitarbeiter-Spalte in SeaTable: Aufgaben zuordnen, Benachrichtigungen aktivieren und flexibel für Filter & Automationen nutzen.'
---

In der **Mitarbeiter-Spalte** können Sie einer Zeile eine oder mehrere **Personen** zuordnen. SeaTable erlaubt Ihnen dabei sowohl Personen auszuwählen, die aktuell **Zugriff** auf die **Base** haben, als auch alle anderen Teammitglieder ohne Zugriff.

![Die Mitarbeiter-Spalte in SeaTable](images/employee-column.png)

## Personen mit Zugriff auf die Base auswählen

Wenn Sie in eine Zelle einer Mitarbeiter-Spalte **doppelklicken**, erscheint eine Liste mit allen Nutzern, die derzeit Zugriff auf die Base haben. Wählen Sie eine oder mehrere dieser **Personen** aus. Sie können auch das **Suchfeld** nutzen, um einen bestimmten Nutzer zu finden.

![Personen mit Zugriff auf eine Base in der Mitarbeiter-Spalte auswählen](images/Personen-mit-Zugriff-auf-eine-Base-in-der-Mitarbeiter-Spalte-auswaehlen.png)

{{< warning  headline="Hinweis"  text="Wenn einem Mitarbeiter der Zugriff auf eine Base **entzogen** wird, er aber in einer Mitarbeiter-Spalte eingetragen ist, so bleibt der Wert in der Spalte eingetragen, bis Sie diesen manuell löschen. Der Mitarbeiter steht nach dem Entfernen nicht mehr in der Liste zur Auswahl." />}}

## Teammitglieder ohne Zugriff auf die Base auswählen

Wenn Sie einen Nutzer nicht über das Suchfeld in der Mitarbeiter-Spalte finden können, hat dieser aktuell **keinen Zugriff** auf die Base. Ist er **Mitglied Ihres Team**, können Sie ihn aber trotzdem in die Mitarbeiter-Spalte eintragen.

Klicken Sie auf das Symbol {{< seatable-icon icon="dtable-icon-add\_members" >}}, um Teammitglieder ohne Zugriff hinzuzufügen. Geben Sie den Namen des Nutzers in das **Suchfeld** ein, wählen Sie das gewünschte **Teammitglied** aus und bestätigen Sie mit **Hinzufügen**.

![Teammitglieder ohne Zugriff auf eine Base in die Mitarbeiter-Spalte eintragen](images/Teammitglieder-ohne-Zugriff-auf-eine-Base-in-die-Mitarbeiter-Spalte-eintragen.gif)

## Benachrichtigung des Mitarbeiters beim Hinzufügen

Beim Anlegen einer Mitarbeiter-Spalte können Sie den **Regler aktivieren**, dass Mitarbeiter eine [Benachrichtigung]({{< relref "help/startseite/benachrichtigungen/sinn-und-zweck-von-benachrichtigungen-in-seatable" >}}) erhalten, wenn andere sie in die Spalte eintragen und damit einer Zeile zuordnen.

![Aktivierung von Benachrichtigungen an Mitarbeiter, die zu einer Mitarbeiter-Spalte hinzugefügt werden.](images/turn-on-notification-for-collaborateur-1.png)

Die Mitarbeiter erhalten in der Base anschließend eine entsprechende Benachrichtigung, die sie über das {{< seatable-icon icon="dtable-icon-notice" >}} **Glocken-Symbol** oben rechts abrufen können.

![Benachrichtigung, wenn Mitarbeiter hinzugefügt wird](images/Benachrichtigung-wenn-Mitarbeiter-hinzugefuegt-wird.png)

## Standardwert festlegen

Sie können einen oder mehrere Mitarbeiter als [Standardwert]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) in einer Mitarbeiter-Spalte festlegen. Zur Auswahl stehen die Optionen **Aktueller Benutzer** oder **Bestimmte Benutzer**. Immer wenn jemand eine neue Zeile in der Tabelle hinzufügt, werden dann entweder der Ersteller der Zeile oder die ausgewählten Personen automatisch in die Mitarbeiter-Spalte eingetragen.

![Set default values in collaborator columns](images/Set-default-values-in-collaborator-columns.png)

## Die Mitarbeiter als Empfänger von automatisierten Benachrichtigungen auswählen

Beim Senden von Benachrichtigungen über [Automationen]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) können Sie alle in der Mitarbeiter-Spalte eingetragenen Personen als Empfänger der Nachricht auswählen.

![Collaborator column for automated notifications](images/Collaborator-column-for-automated-notifications.gif)

## Die Mitarbeiter-Spalte in Apps

Die Mitarbeiter-Spalte ist auch in der [App]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}) von Vorteil. Sie können die Option, dass die Teammitglieder in der Drop-down-Liste für alle Nutzer zu sehen sind, in den [Einstellungen]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) der App aktivieren.

Wenn Sie nicht möchten, dass die App-Nutzer die Datensätze von anderen Nutzern sehen können, legen Sie **voreingestellte Filter** fest: Wird eine Seite per Mitarbeiter-Spalte mit der Bedingung „inkludiert aktuellen Benutzer“ gefiltert, sieht jeder Nutzer der App nur die Einträge, die ihm in der Tabelle zugeordnet sind.

![Mitarbeiter-Spalte in der App](images/Mitarbeiter-Spalte-in-der-Universellen-App.gif)
