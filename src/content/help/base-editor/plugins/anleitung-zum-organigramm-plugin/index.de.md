---
title: 'Anleitung zum Organigramm-Plugin'
date: 2024-07-18
lastmod: '2025-02-28'
categories:
    - 'plugins'
author: 'kgr'
url: '/de/hilfe/anleitung-zum-organigramm-plugin'
seo:
    title: 'Organigramm-Plugin: Hierarchien und Teams visualisieren'
    description: 'Organigramm-Plugin: Visualisieren Sie Hierarchien, Abteilungen, Aufgaben und Teams als übersichtliche Baumstruktur in SeaTable.'
---

Mithilfe des Organigramm-Plugins können Sie **Hierarchien** zwischen den Datensätzen in einer Tabelle darstellen. Das ist zum Beispiel nützlich, um die Positionen in einem Unternehmen oder [über- und untergeordnete Aufgaben in einem Projekt]({{< relref "templates/projects/work-breakdown-structure" >}}) zu visualisieren.

{{< youtube SbGzg9jOZ9A >}}

Wie Sie das Plugin in einer Base aktivieren, erfahren Sie [hier]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}
).

![Organigramm-Plugin](images/Organigramm-Plugin.png)

## Voraussetzungen und Funktionsweise des Organigramm-Plugins

Um zu definieren, welche Datensätze voneinander abhängen, brauchen Sie eine [Verknüpfung, die auf ein und dieselbe Tabelle referiert]({{< relref "help/base-editor/tabellen/verknuepfungen-innerhalb-einer-tabelle" >}}). Der Eintrag, den Sie in dieser Spalte mit einer anderen Zeile derselben Tabelle verlinken, wird als **übergeordneter Datensatz** dargestellt.

![Verknüpfungsspalte für ein Organigramm](images/Verknuepfungsspalte-fuer-ein-Organigramm.png)

> Im Anwendungsbeispiel mit den Positionen in einem Unternehmen würden Sie also den jeweiligen Vorgesetzten des Mitarbeiters in der Verknüpfungsspalte verlinken. Daraus resultieren die Ebenen des Organigramms: In der zweiten Ebene stünden die Abteilungsleiter und ganz oben der Geschäftsführer.

Wenn Sie die Datensätze im Organigramm mit Bildern illustrieren möchten, benötigen Sie in der Tabelle zudem eine [Bild-Spalte]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}), in der Sie Fotos und Grafiken hochladen können.

## Einstellungsmöglichkeiten eines Organigramms

Standardmäßig ist beim ersten Öffnen des Organigramm-Plugins bereits ein leeres Organigramm angelegt. Wenn Sie ein weiteres Organigramm erstellen möchten, klicken Sie auf {{< seatable-icon icon="dtable-icon-add-table" >}} **Organigramm hinzufügen**. Daraufhin öffnet sich ein Eingabefeld, in das Sie den gewünschten **Namen** tippen.

![Optionen für Organigramme](images/Optionen-fuer-Organigramme.png)

Um die **Reihenfolge der Organigramme zu ändern**, halten Sie die linke Maustaste an der **Greiffläche** {{< seatable-icon icon="dtable-icon-drag" >}} gedrückt und ziehen das Organigramm **per Drag-and-Drop** an die gewünschte Stelle. Darüber hinaus können Sie Organigramme **umbenennen**, **duplizieren** oder **löschen**.

{{< warning  type="warning" headline="Hinweis"  text="Wenn nur ein einziges Organigramm im Plugin angelegt ist, können Sie dieses **nicht löschen**." />}}

Über die **Einstellungen**, die Sie per Klick auf das **Zahnrad-Symbol** {{< seatable-icon icon="dtable-icon-set-up" >}} erreichen, können Sie Folgendes für das Organigramm festlegen:

- **Tabelle**: Wählen Sie die Tabelle, aus der SeaTable das Organigramm erzeugen soll.
- **Ansicht**: Wählen Sie die Ansicht mit den Datensätzen, die im Organigramm zu sehen sein sollen.
- **Beziehung**: Wählen Sie die Verknüpfungsspalte, auf der die Hierarchie basiert.
- **Titel**: Wählen Sie eine Spalte, deren Werte als Titel angezeigt werden sollen.
- **Titelbild**: Wählen Sie eine Bild-Spalte, um die Datensätze zu illustrieren.
- **Weitere Spalten**: Wählen Sie weitere Spalten aus, deren Werte angezeigt werden sollen.

![Einstellungen eines Organigramms](images/Einstellungen-eines-Organigramms.png)

{{< warning  type="warning" headline="Hinweis"  text="Aktuell kann das Organigramm in der obersten Hierarchie-Ebene nur **einen Kopf** haben. Besitzt Ihr Unternehmen beispielsweise mehrere Geschäftsführer, sollten Sie den Firmennamen an die Spitze setzen." />}}
