---
title: 'Die erste Base'
date: 2022-08-25
lastmod: '2023-05-15'
categories:
    - 'kurzanleitungen'
author: 'cdb'
url: '/de/hilfe/erste-base-erstellen-anleitung-seatable'
aliases:
    - '/de/hilfe/die-erste-base'
seo:
    title: 'Erste Base in SeaTable erstellen: Anleitung & Tipps'
    description: 'Erstellen und verwalten Sie Ihre erste SeaTable Base: Tabellen, Spaltentypen, Relationen und praktische Funktionen für den Datenstart.'
---

In SeaTable organisieren Sie Ihre Daten in [Bases]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}). Eine Base ist ein Container für eine oder mehrere Tabellen. Die Tabellen einer Base können unabhängig nebeneinander stehen oder - wie in einer Datenbank - über Relationen miteinander verknüpft werden.

Sie können anderen Teammitgliedern auch Ihre [Bases freigeben]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) oder externe Dritte [einladen]({{< relref "help/startseite/freigaben/unterschiede-zwischen-einladungs-links-und-externen-links" >}}), um gemeinsam daran zu arbeiten.

SeaTable verwaltet im Hintergrund für jede Base eine [Historie]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}), über die Sie Änderungen rückgängig machen und frühere Zustände wiederherstellen können, sofern Sie dies benötigen.

## Die Startseite

Nach dem Login befinden Sie sich auf der **Startseite**. Hier verwalten Sie Ihre Bases. Wenn Sie bei der Registrierung [Templates]({{< relref "templates" >}}) ausgewählt haben, dann werden diese hier angezeigt.

Mit einem Klick auf das **Avatar-Bild** in der oberen rechten Ecke können Sie in die [persönlichen Einstellungen]({{< relref "help/startseite/persoenliche-einstellungen" >}}) wechseln, um zum Beispiel die Systemsprache anzupassen.

Mit einem Klick auf **Base hinzufügen** legen Sie Ihre erste eigene Base an. Geben Sie ihr einen **Namen**, drücken Sie **Enter** und die Base wird auf der Startseite abgelegt. Wenn Sie den Mauszeiger auf den Namen der Base bewegen, erscheinen rechts ein **Stift-Symbol** {{< seatable-icon icon="dtable-icon-rename" >}} und das Drei-Punkte-Symbol {{< seatable-icon icon="dtable-icon-more-vertical" >}} für die erweiterten Funktionen.

Über das Stift-Symbol können Sie die Base umbenennen und ihr ein anderes Icon sowie eine andere Farbe zuweisen. Zu den erweiterten Funktionen gehören z. B. die [Freigabe]({{< relref "help/startseite/freigaben/base-und-ansichtsfreigaben-im-ueberblick" >}}) einer Base oder deren [Export]({{< relref "help/startseite/import-von-daten/datenimport-und-export" >}}). Sie öffnen die Base mit einem Klick auf ihren Namen.

## Tabellenansicht

Die neue Base enthält von Beginn an eine [Tabelle]({{< relref "help/erste-schritte/einfuehrung-funktionen/einfuehrung-in-die-arbeit-mit-bases-und-tabellen" >}}). Die Tabellenansicht ist die zentrale, aber nicht die einzige Ansicht von SeaTable. In der Tabellenansicht verwalten Sie die Tabellen der Base, definieren deren Spaltenstruktur und erfassen oder analysieren Ihre Daten.

SeaTable bietet insgesamt [über 20 Spaltentypen]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}). Aus herkömmlichen Tabellenkalkulationen kennen Sie bestimmt schon Text-, Zahl- und Datum-Spalten. Diese kennt natürlich auch SeaTable. Darüber hinaus bietet SeaTable Spalten für Bilder und Dateien, Schaltflächen und Checkboxen sowie Einfach- und Mehrfachauswahlfelder.

Sie wollen Bilder zu einem Eintrag hinzufügen? Ziehen Sie einfach das Bild in eine Bild-Spalte und SeaTable speichert es direkt in der Tabelle. In SeaTable haben Sie alle Ihre Daten an einem Ort!

Ein weiterer Spaltentyp, den Sie aus einer Tabellenkalkulation nicht kennen, ist die [Verknüpfung zu anderen Einträgen]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Mit Verknüpfungen erstellen Sie Relationen zwischen Zeilen unterschiedlicher Tabellen. Dieses Vorgehen, das der Arbeitsweise relationaler Datenbanken entspricht, vermeidet Doppeleingaben, sichert die Datenkonsistenz und schafft Übersicht.

Hier ein Anwendungsbeispiel: Eine Hausverwaltung erfasst in einer Tabelle die verwalteten Objekte und verknüpft diese mit Mietern, die in einer anderen Tabelle geführt werden. Ändert sich an den Objekteigenschaften etwas, so muss der Verwalter die Anpassung nur in der Objekt-Tabelle ändern. Per Verknüpfung wird die geänderte Information bei allen zugeordneten Mietern automatisch aktualisiert.

[Weitere Tabellen legen Sie über die Tabellentabs an]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}}). Jede Tabelle hat ein individuelles Layout: Gestalten Sie die Spalten nach Ihren eigenen Wünschen und Bedürfnissen.
