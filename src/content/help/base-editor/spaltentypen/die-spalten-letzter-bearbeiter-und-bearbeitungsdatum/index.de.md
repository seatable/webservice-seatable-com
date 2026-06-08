---
title: 'Die Spalten Letzter Bearbeiter und Zuletzt bearbeitet'
date: 2023-01-20
lastmod: '2023-08-04'
categories:
    - 'datum-dauer-und-personen'
author: 'nsc2'
url: '/de/hilfe/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum'
seo:
    title: 'Letzter Bearbeiter und Bearbeitungsdatum in SeaTable nutzen'
    description: 'Die speziellen SeaTable-Spalten zeigen automatisch an, wer und wann eine Zeile zuletzt verändert hat – ideal für Historie und Tracking im Team.'
weight: 23
---

Die Spalten **Letzter Bearbeiter** und **Zuletzt bearbeitet** werden von SeaTable ausschließlich **automatisch** gefüllt und stellen daher besondere Spaltentypen dar. Sie erweisen sich als äußerst sinnvoll, wenn Sie nachvollziehen möchten, **wann** und **von wem** ein Eintrag **zuletzt bearbeitet** wurde.

Da die beiden Spalten automatisch Änderungen an Einträgen erfassen, eignen sie sich zum Beispiel gut als Trigger für [Automationen]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) und [Sortierungen]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}).

## Die Spalten Letzter Bearbeiter und Zuletzt bearbeitet

Während SeaTable die Spalte **Letzter Bearbeiter** mit dem Namen des Benutzers füllt, der eine Zeile zuletzt bearbeitet hat, wird in der Spalte **Zuletzt bearbeitet** der exakte Zeitpunkt (Datum und Uhrzeit) festgehalten, zu dem die letzte Bearbeitung erfolgte.

![Die Spalten "Letzter Bearbeiter" und "Zuletzt bearbeitet" nach dem Angelegen durch einen Benutzer](images/last-modifiere-and-last-modified-time.png)

## Besonderheiten der beiden Spaltentypen

- Die automatisch erfassten Werte in den Spalten Letzter Bearbeiter und Zuletzt bearbeitet können Sie **nicht** manuell ändern. Die Werte aktualisieren sich von selbst, sobald eine Änderung an einer Zeile vorgenommen wird.
- Bei der **Erstellung** der beiden Spaltentypen stehen Ihnen, abgesehen vom Spaltennamen, **keine** Optionen zur Verfügung.
- Pro Tabelle kann nur **je eine** Spalte vom jeweiligen Typ angelegt werden. Wenn Sie versuchen, eine weitere Spalte desselben Typs anzulegen, erscheint der Hinweis "Eine andere Spalte hat diesen Spaltentyp."

![Fehlermeldung bei weiterer Letzter-Bearbeiter-Spalte](images/Fehlermeldung-bei-weiterer-Letzter-Bearbeiter-Spalte.png)

- Aus diesem Grund können Sie die Letzter-Bearbeiter- und Zuletzt-bearbeitet-Spalte **nicht duplizieren und deren Spaltentyp nicht anpassen**.
