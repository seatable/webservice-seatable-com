---
title: 'Webformulare'
date: 2022-08-25
lastmod: '2026-11-26'
categories:
    - 'webformulare'
author: 'cdb'
url: '/de/hilfe/webformulare'
seo:
    title: 'Webformulare in SeaTable: Einrichten, bearbeiten und freigeben'
    description: 'Webformulare in SeaTable: Erstellen, konfigurieren und testen Sie Formulare, um bequem Daten von internen und externen Nutzern zu erfassen.'
weight: 1
star: true
---

**Webformulare** sind das Mittel der Wahl, um Teammitglieder und externe Dritte neue Datensätze in Ihren Tabellen erfassen zu lassen. Die Nutzer greifen per **Link** auf ein Formular zu, sodass **keine Freigabe** für die Tabelle notwendig ist. Daher eignen sich Webformulare insbesondere für die Datenerfassung durch eine große Anzahl von **Personen innerhalb und außerhalb Ihres Teams**.

Machen Sie sich mit SeaTables Formularfunktion vertraut, um Daten bequem über Webformulare zu erheben!

## Funktionsweise von Formularen

Das klassische Webformular ist ideal für **Online-Umfragen**, **Anträge** und die strukturierte Erfassung neuer Daten. Die Tabellenspalten werden mithilfe von **Formularfeldern** integriert und die Nutzer durch den Ausfüllprozess geleitet. Für den Zugriff erstellen Sie einen Link, über den die Nutzer **ohne SeaTable Benutzerkonto** das Webformular ausfüllen können. Ein ausgefülltes Webformular entspricht dabei **einem neuen Datensatz** bzw. einer hinzugefügten Zeile in der entsprechenden Tabelle.

Formulare beziehen sich immer auf eine **Tabelle** in der geöffneten Base. Daher müssen Sie zunächst die relevante Tabelle auswählen, bevor Sie ein Formular anlegen. In jeder Base können Sie eine **beliebige Anzahl** an Formularen erstellen und speichern.

## Formular erstellen

Öffnen Sie die Formularverwaltung über die Schaltfläche {{< seatable-icon icon="dtable-icon-form" >}} **Formulare** oben rechts im Base-Header. Die Formularverwaltung präsentiert sich Ihnen als leere Liste, wenn in der Base noch keine Formulare angelegt wurden. Ansonsten werden die schon bestehenden Formulare in dem geöffneten Fenster angezeigt.

![Klassisches Formular erstellen](images/create-a-web-form.gif)

Sie erstellen ein [neues Webformular]({{< relref "help/base-editor/webformulare/anlegen-eines-webformulars" >}}), indem Sie am unteren Rand der Formularverwaltung auf **Webformular erstellen** klicken und dann **Klassisches Formular** wählen.

Geben Sie nun den **Namen** des neuen Webformulars ein, der auch in der Formularverwaltung angezeigt werden soll. Verwenden Sie einen prägnanten Namen, um bei vielen Formularen die Übersicht zu behalten. Natürlich können Sie den Namen später noch anpassen.

Wenn Sie auf das **Stift-Icon** {{< seatable-icon icon="dtable-icon-rename" >}} klicken, öffnet sich der **Webformular-Editor** mit seiner zweigeteilten Ansicht: Links wird das Webformular im Entwurfsmodus angezeigt; rechts befinden sich die **Einstellungen**.

Es gibt zahlreiche [Konfigurationsmöglichkeiten]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}}), um ein Webformular schnell und einfach an Ihre Wünsche und Vorstellungen anzupassen.

Über die **Webformular-Einstellungen** rechts können Sie die folgenden Entscheidungen treffen:

- Mit welcher **Tabelle** ist das Formular verknüpft?
- Welche **statischen Elemente** und **Tabellenfelder** möchten Sie in das Formular einbauen?
- Möchten Sie mithilfe von Seitenumbrüchen ein **mehrseitiges Formular** erstellen?
- Soll bei Einreichung des Formulars eine **Benachrichtigung** (an Sie) versandt werden?
- Wer darf auf das Formular **zugreifen**?
- Sollen alle Felder **Pflichtfelder** sein?
- Soll den Ausfüllenden bei mehrseitigen Formularen ein **Fortschrittsbalken** angezeigt werden?
- Soll "Powered by" angezeigt werden?
- Welche **Nachricht** wird dem Teilnehmer nach Einreichung des Formulars angezeigt?
- Möchten Sie den Teilnehmer nach Einreichung des Formulars **auf eine Webseite weiterleiten**?
- Hat das Formular eine **Einreichungsfrist**?
- Hat das Formular ein **Einreichungslimit**?

Die im Formular verfügbaren Felder sind abhängig von den **Spalten** der ausgewählten Tabelle. Wenn Sie Spalten in der Tabelle hinzufügen oder löschen, passen sich die verfügbaren Felder in den Einstellungen automatisch an. Die **Namen** und die **Reihenfolge** der Tabellenfelder werden direkt aus der zugrundeliegenden Tabelle übernommen.

![Felder in einem Webformular hinzufügen und konfigurieren](images/Add-fields-to-a-web-form.gif)

Ziehen Sie die Tabellenfelder per **Drag-and-Drop** in Ihren Entwurf oder klicken Sie auf das **Plus-Symbol** rechts neben dem Spaltennamen. Sie können die Reihenfolge der Felder im Webformular beliebig verändern, indem Sie auf das **Sechs-Punkte-Symbol** {{< seatable-icon icon="dtable-icon-drag" >}} in der rechten Ecke eines Feldes klicken und das Feld per Drag-and-Drop an die gewünschte Stelle ziehen.

{{< warning  type="warning" headline="Nicht wählbare Spaltentypen"  text="Spalten vom Typ Mitarbeiter, Formel, Formel für Verknüpfung, Ersteller, Erstellt, Letzter Bearbeiter, Zuletzt bearbeitet, Automatische Nummer und Schaltfläche können Sie grundsätzlich nicht in ein Webformular einbauen." />}}

Im Entwurf können Sie jedes Feld anklicken, wodurch Sie zu den **Feldeinstellungen** gelangen. Pro Feld können Sie festlegen, ob ...

- ein vom Spaltennamen abweichender **Feldname** im Formular angezeigt werden soll,
- ein Feld einen ergänzenden **Hilfetext** als Ausfüllhinweis erhält,
- ein Feld ein **Pflichtfeld** ist,
- ein Feld einen **Standardwert** enthalten soll,
- die Anzeige des Feldes von einer **Bedingung** abhängt.

{{< warning  headline="Auswahlfelder"  text="Bei Einfach- und Mehrfach-Auswahlfeldern können Sie auch festlegen, ob die Werte als **Liste** oder als **Dropdown** angezeigt werden." />}}

Um zu prüfen, wie das Formular für den Empfänger aussieht, klicken Sie oben rechts auf die Schaltfläche **Webformular Seite**. In einem neuen Tab öffnet sich dann das Formular so, wie es ein anderer Benutzer sehen würde.

## Formular freigeben

Um das Formular anderen zugänglich zu machen, benötigen Sie einen **Link**. Den Link für das Formular erhalten Sie im Webformular-Editor über die Schaltfläche {{< seatable-icon icon="dtable-icon-share" >}} **Freigeben**. Sie können den **automatisch generierten Link** nutzen oder **eigene Links** erstellen und diese mit [vorbefüllten Werten]({{< relref "help/base-editor/webformulare/formularfelder-per-url-vorbefuellen" >}}) erweitern.

![Neuer Formularlink-Dialog in SeaTable 4.3](images/Formularlink-Dialog.gif)

{{< warning  headline="Eigene Links"  text="Der benutzerdefinierte Teil, der an den Link angehängt wird, muss **zwischen 5 und 30 Zeichen** lang sein und darf nur **Buchstaben**, **Zahlen** und **Bindestriche** enthalten. Noch dazu muss jede URL eindeutig sein: Falls eine benutzerdefinierte URL bereits belegt ist, erscheint eine Fehlermeldung." />}}

Bevor Sie den Formularlink nun versenden bzw. öffentlich zugänglich machen, sollten Sie das Formular ausgiebig testen.

## Formular testen

Umfangreiche Tests vermeiden Frustration auf Seiten der Empfänger. Probleme können durch Mehrdeutigkeiten oder Konflikte im Formular verursacht werden. Im schlimmsten Fall lässt sich ein Formular nicht absenden, weil ein Pflichtfeld nicht ausgefüllt werden kann (z. B. wenn für eine Einfachauswahl keine Werte definiert sind).

Öffnen Sie zum Testen das Webformular. Aus dem Webformular-Editor geht dies über die Schaltfläche **Webformular Seite**. Aus der Tabellenansicht rufen Sie zunächst die Formularverwaltung auf und klicken dann auf den Namen des Webformulars. In beiden Fällen öffnet sich das Webformular in einem neuen Browser-Tab.

![Ein Webformular testen](images/Test-a-web-form.gif)

In das Formular eingegebene Werte werden in der verknüpften Tabelle abgespeichert. Vergessen Sie nicht, die Testdaten vor der späteren Datenerhebung wieder aus der Tabelle zu löschen.

## Formular anpassen

Sie können Webformulare jederzeit mithilfe des Webformular-Editors anpassen. Um in den Editor zurückzukehren, rufen Sie die Formularverwaltung auf, bewegen den Mauszeiger auf den Namen des Formulars und klicken dann rechts neben dem Namen auf das **Stift-Icon** {{< seatable-icon icon="dtable-icon-rename" >}}.

## Formular kopieren

Wenn Sie bereits ein Formular erstellt haben, das Sie nur geringfügig für einen weiteren Anwendungsfall abwandeln wollen, können Sie das Formular kopieren. Bewegen Sie dazu den Mauszeiger auf den Namen des Formulars und klicken rechts neben dem Namen auf das **Kopie-Icon** {{< seatable-icon icon="dtable-icon-copy" >}}.

## Formular löschen

Sie können Webformulare jederzeit über die Formularverwaltung löschen. Bewegen Sie den Mauszeiger auf den Namen des Formulars und klicken Sie dann rechts neben dem Namen auf das **Papierkorb-Icon** {{< seatable-icon icon="dtable-icon-delete" >}}.

![Formularverwaltungsoptionen](images/form-management-options.png)