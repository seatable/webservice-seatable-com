---
title: 'Formularseiten in SeaTable Apps'
date: 2023-12-04
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/de/hilfe/formularseiten-in-seatable-apps'
aliases:
    - '/de/hilfe/formularseiten-in-universellen-apps'
seo:
    title: 'Formularseiten in SeaTable Apps: Anleitung'
    description: 'Erstellen Sie individuelle Formularseiten in SeaTable Apps – mit Drag-and-Drop, Pflichtfeldern, individuellen Einstellungen & Zugriffskontrolle.'
weight: 3
---

Mithilfe dieses Seitentyps können Sie unterschiedliche **Formulare** bauen, welche die Benutzer im Anschluss einreichen können. Formularseiten in SeaTable Apps eignen sich hervorragend, um Daten von vielen verschiedenen Nutzern erfassen zu lassen. Ein möglicher Anwendungsfall ist die [Arbeitszeiterfassung Ihrer Mitarbeiter]({{< relref "pages/arbeitszeiterfassung" >}}).

![Webformular zur Erfassung der Arbeitszeit Ihrer Mitarbeiter](images/webformular-working-time.png)

{{< warning  type="warning" headline="Tipp" >}}

[Webformulare]({{< relref "help/base-editor/webformulare/webformulare" >}}) gibt es nicht nur im App Builder, sondern auch direkt in der Base.

{{< /warning >}}

## Seiteneinstellungen ändern

Wenn Sie die Einstellungen einer Seite ändern möchten, klicken Sie in der Navigation auf das entsprechende {{< seatable-icon icon="dtable-icon-set-up" >}} **Zahnrad-Symbol**.

![Einstellungen der Formularseite ändern](images/Einstellungen-der-Formularseite-aendern.png)

## Formulare erstellen

Über die **Seiteneinstellungen**, die Sie vielleicht schon aus dem [Webformular-Editor]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}}) kennen, können Sie verschiedene **Elemente** und **Felder** per Drag-and-Drop zum Webformular hinzufügen. Neben den **Tabellenfeldern**, die den Spalten der ausgewählten Tabelle entsprechen, können Sie auch **horizontale Linien** und **Anmerkungen** hinzufügen.

![Seiteneinstellungen der Formularseite](images/Seiteneinstellungen-der-Formularseite.png)

### Feldeinstellungen

Jedes Feld verfügt zudem über individuelle **Feldeinstellungen**, bei denen Sie einen vom Spaltennamen abweichenden **Anzeigenamen** und einen **Hilfetext** im Formular hinzufügen können. Hier können Sie auch einstellen, ob ein Feld ein erforderliches **Pflichtfeld** ist, mit einem **Standardwert** vorbefüllt sein soll oder nur unter bestimmten **Bedingungen** angezeigt wird.

![Feldeinstellungen der Formularseite](images/Feldeinstellungen-der-Formularseite.png)

Wenn Sie die **Reihenfolge** der Felder im Formular verändern möchten, können Sie ein Feld am {{< seatable-icon icon="dtable-icon-drag" >}} **Sechs-Punkte-Symbol** greifen und verschieben. Per Klick auf das {{< seatable-icon icon="dtable-icon-delete" >}} **Papierkorb-Symbol** entfernen Sie ein Feld aus dem Formular.

![Feld auf der Formularseite einer SeaTable App](images/Feld-auf-der-Formularseite-einer-Universellen-App.png)

### Weitere Formularseiten-Einstellungen

Weiter unten können Sie eine **Farbe für die Hilfetexte** festlegen sowie eine **Nachricht**, die den Nutzern nach Einreichung des Formulars angezeigt wird.

![Weitere Einstellungen auf Formularseiten](images/Weitere-Einstellungen-auf-Formularseiten.png)

Des Weiteren können Sie unterbinden, dass Formulare mit bereits existierenden Datensätzen eingereicht werden, indem Sie das **Hinzufügen von Duplikaten verhindern**. Aktivieren Sie dazu den entsprechenden Regler und wählen Sie die Spalten aus, in denen die Werte übereinstimmen müssen, damit ein Formular als Duplikat gilt. Wenn ein Nutzer daraufhin identische Daten eingibt, wird das Einreichen des Formulars blockiert.

Nicht zuletzt können Sie die Nutzer nach Einreichung des Formulars auf eine andere Seite der App oder eine andere Webseite weiterleiten. Klicken Sie dazu auf **Weiterleitung aktivieren** und wählen Sie den entsprechenden Hyperlink aus. Sie können ebenso einstellen, ob der Link in einem neuen oder im aktuellen Tab geöffnet werden soll.

## Seitenberechtigungen

Ganz unten können Sie eingrenzen, wer die Formularseite sehen darf.

![Berechtigung für Formularseiten der SeaTable App](images/Berechtigung-fuer-individuelle-Seiten-der-Universellen-App.png)

Das ist die einzige [Seitenberechtigung]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}), die Sie bei Formularseiten zur Auswahl haben – denn über Formularseiten können keine Zeilen in der Tabelle verändert oder gelöscht werden und jeder, der die Seite sehen kann, darf auch Formulare einreichen, also Zeilen hinzufügen.
