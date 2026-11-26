---
title: 'Bedingte Anzeige von einzelnen Formularfeldern'
date: 2023-01-08
lastmod: '2024-02-14'
categories:
    - 'webformulare'
author: 'vge'
url: '/de/hilfe/bedingte-anzeige-von-einzelnen-formularfeldern'
seo:
    title: "Bedingte Anzeige von Formularfeldern in SeaTable: So funktioniert's"
    description: 'Erfahren Sie, wie Sie in SeaTable Webformularen Felder nur bei erfüllter Bedingung anzeigen – für dynamische Umfragen und bessere Datenqualität.'
weight: 4
---

Bei der Erstellung von **Webformularen** können Sie einstellen, dass bestimmte **Felder** erst sichtbar werden, wenn eine **Bedingung** in einem vorherigen Feld erfüllt wurde. Dadurch können Sie die **Benutzerführung** beim Ausfüllen des Formulars verbessern.

## Bedingung für ein Formularfeld festlegen

1. Öffnen Sie ein bestehendes **Webformular**.
2. Klicken Sie auf ein Feld, um die **Feldeinstellungen** zu öffnen.
3. Gehen Sie zu **Feld nur anzeigen, wenn Bedingungen erfüllt sind** und klicken Sie auf die Schaltfläche mit dem Plus-Symbol, über die Sie eine **Bedingung hinzufügen** können.
4. Wählen Sie das **vorherige Feld** aus, auf das sich die Bedingung beziehen soll.
5. Legen Sie anschließend die **Bedingung** fest. Je nach zugrundeliegendem Spaltentyp haben Sie unterschiedliche Optionen zur Auswahl.

{{< warning  headline="Hinweis"  text="Sie haben die Möglichkeit einer bedingten Anzeige nur, wenn es mindestens ein vorheriges Feld gibt." />}}

## Anwendungsbeispiel

![Bedingte Anzeige von Feldern in Webformularen](images/Bedingte-Anzeige-von-Feldern-in-Webformularen.gif)

Angenommen Sie möchten eine Umfrage zur Mitarbeiterzufriedenheit in Ihrem Unternehmen durchführen. Dabei wollen Sie beispielsweise die Frage stellen "Wie zufrieden sind Sie mit unserem Firmenwagen-Leasing?", aber Sie wissen, dass nur Mitarbeiter in leitender Position einen Firmenwagen angeboten bekommen. Deshalb möchten Sie diese Frage nur Ihren Führungskräften stellen.

Zunächst sollten Sie eine [Rating-Spalte]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}}) in Ihrer Tabelle anlegen und diese als **Feld** in Ihr Webformular einbauen. Fügen Sie anschließend die **Bedingung** hinzu, dass das Rating-Feld nur angezeigt wird, wenn im vorherigen **Auswahlfeld "Position"** die Option "Head of" oder "Team lead" ausgewählt wurde. Dabei sollte das Auswahlfeld eine **verpflichtende Eingabe** erfordern, da sonst auch Führungskräfte, die dieses Feld frei lassen, die Frage nach dem Firmenwagen-Leasing nicht angezeigt bekommen.

Damit die Teilnehmer ausgeblendete Formularfelder nicht einfach, indem sie die Bedingungen durchprobieren, angezeigt bekommen, können Sie **Seitenumbrüche** einfügen. So müssen die Teilnehmer nach dem Ausfüllen des Pflichtfelds erst auf **Nächste Seite** klicken und bekommen die bedingten Felder dort entweder angezeigt oder nicht.