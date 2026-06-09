---
title: 'Datenverarbeitung: Benutzernamen übertragen'
date: 2023-03-17
lastmod: '2023-03-17'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/de/hilfe/datenverarbeitung-benutzernamen-uebertragen'
seo:
    title: 'Benutzernamen per Datenverarbeitung in SeaTable übertragen'
    description: 'Übertragen Sie Benutzernamen automatisiert aus Mitarbeiter- oder Systemspalten in Textspalten – für Listen, Workflows und Filter.'
---

Mithilfe der Datenverarbeitungsfunktion können Sie diverse Operationen über eine Spalte hinweg durchführen. Die **Übertragung von Benutzernamen** stellt dabei eine Operation dar, bei der Daten aus Spalten vom Typ [Mitarbeiter]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), [Ersteller]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) oder [Letzter Bearbeiter]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}) in eine [Text-Spalte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}) kopiert werden können.

## Anlegen der Operation

![Anlegen einer Datenverarbeitungsaktion](images/create-an-data-processing-action-1.jpg)

1. Öffnen Sie eine beliebige **Tabelle** und klicken Sie auf die **drei Punkte** in den Ansichtsoptionen.
2. Klicken Sie auf **Datenverarbeitung** und im Anschluss auf **Datenverarbeitungsoperation hinzufügen**.
3. Geben Sie der Operation einen **Namen** und wählen Sie **Benutzernamen übertragen** aus.
   ![Benennung der Datenverarbeitungsaktion und Auswahl des Operationstyps](images/select-operation-and-name-example-name.jpg)5. Definieren Sie **Tabelle**, **Ansicht**, **Quellspalte** und **Ergebnisspalte**.
   ![Definition von Tabelle, Ansicht, Quellspalte und Ergebnisspalte der Operation](images/define-table-view-and-columns-example-name.png)7. Klicken Sie auf **Speichern**, um die Aktion zu speichern und später auszuführen, oder auf **Ausführen**, um die Aktion direkt auszuführen.
   Bei der ersten erfolgreichen Ausführung erscheint am unteren linken Rand ein kleiner **grüner Haken**. ![Bei erfolgreicher erster Ausführung der Datenverarbeitungsaktion erscheint ein grüner Haken](images/gruener-haken-zur-bestaetigung-der-ersten-ausfuehrung.jpg)

## Ausführung der Operation

Wenn Sie beispielsweise eine Tabelle mit zu erledigenden Aufgaben pflegen, in der Ihre **Teammitglieder** als zuständige Ansprechpersonen in einer [Mitarbeiter-Spalte]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) erfasst sind, können Sie die Benutzernamen einfach in eine [Text-Spalte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}) kopieren, z. B. um diese für eine Mitarbeiterliste zu verwenden.

Befolgen Sie dazu die oben beschriebenen Schritte und wählen Sie die Mitarbeiter-Spalte als **Quellspalte** sowie die Text-Spalte als **Ergebnisspalte** aus.

![Definition der Datenverarbeitungsaktion](images/name-operation-and-define-columns-example-name-1.png)

Bei erfolgreicher Ausführung der Operation werden die **ausgewählten Benutzernamen** aus der Mitarbeiter-Spalte extrahiert und durch ein Komma getrennt in die Text-Spalte übertragen.

![Übertragene Benutzernamen in eine Text- bzw. Ergebnis-Spalte](images/table-after-operation-example-user-name.png)

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="Bitte beachten Sie, dass mit jeder erneuten Ausführung dieser Operation die bestehenden Einträge in der Ergebnisspalte **überschrieben** werden, sofern sich die Benutzernamen in der Quellspalte verändert haben." />}}
