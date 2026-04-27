---
title: 'Farbliche Markierung von Zeilen'
date: 2022-11-16
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'vge'
url: '/de/hilfe/farbliche-markierung-von-zeilen'
seo:
    title: 'Zeilen farblich markieren in SeaTable: Regeln & Tipps'
    description: 'Markieren Sie Zeilen schnell farbig: mit Einzelauswahl, Regeln oder zur Duplikatsprüfung. Ideal für Status, Prioritäten und visuelle Übersicht in Tabellen.'
weight: 27
---

Das **farbliche Markieren von Zeilen** dient der schnellen Identifikation bestimmter Datensätze. Dies ist nicht zu verwechseln mit dem [Einfärben von Zellen]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}), wodurch Sie einzelne Zellen farblich hervorheben können.

## Das Zeilenfarben-Werkzeug

In den Ansichtsoptionen über einer Tabelle finden Sie folgendes Symbol:

![Farbliche-Markierungs-Werkzeug](images/Farbliche-Markierung-von-Zellen-1.png)

Nach einem Klick auf das Zeilenfarben-Werkzeug können Sie zwischen **drei Optionen** für die farbliche Markierung wählen:

- Einfachauswahl-Spalte verwenden
- Regeln verwenden
- Duplikate hervorheben

![Farbliche Markierung von Zellen](images/Farbliche-Markierung-von-Zellen-2.png)

Das Zeilenfarben-Werkzeug steht nicht nur in Tabellenansichten, sondern auch in [Kalender-]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}) und [Zeitleisten-Ansichten]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}) zur Verfügung. Allerdings können Sie bei den Letzteren nur Einfachauswahl-Spalten verwenden, um die Zeilenfarbe zu definieren.

## Einfachauswahl-Spalte verwenden

Für die Option **Einfachauswahl-Spalte verwenden** benötigen Sie in Ihrer Tabelle eine Spalte dieses Typs. So können Sie jede Zeile am **Zeilenanfang** mit der Farbe der jeweiligen Option markieren, die in dieser Spalte eingetragen ist.

![Farbliche Markierung von Zellen](images/Farbliche-Markierung-von-Zellen-3.png)

{{< warning  headline="Anlegen einer Einfachauswahlspalte" >}}

Erfahren Sie [hier]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}), wie Sie neue Einfachauswahlspalten anlegen.

{{< /warning >}}

## Regeln verwenden

Die Option **Regeln verwenden** erlaubt es Ihnen, Bedingungen für die farbliche Markierung festzulegen.

- Klicken Sie auf das **farbig hinterlegte Dreieck-Symbol**, um die Farbe der Markierung zu ändern.
  ![Farbliche Markierung von Zellen](images/Farbliche-Markierung-von-Zellen-5.png)
- Legen Sie fest, auf welche Ihrer **Spalten** sich die Bedingung beziehen soll.
  ![Farbliche Markierung von Zellen](images/Farbliche-Markierung-von-Zellen-6.png)
- Entscheiden Sie sich für die **Art der Bedingung**.
  ![Farbliche Markierung von Zellen](images/Farbliche-Markierung-von-Zellen-7.png)

{{< warning  headline="Auswahl der Bedingungsarten abhängig vom Spaltentyp"  text="Bitte beachten Sie, dass vom Typ der ausgewählten Spalte abhängt, welche Optionen Sie bei den Bedingungen zur Auswahl haben." />}}

### Beispiel für Regel verwenden

In diesem Beispiel sollen alle Zeilen in einem Redaktionsplan markiert werden, die in der [Checkbox-Spalte]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}}) als erledigt markiert sind. Hierfür wurde die **Spalte "Published"** ausgewählt, die Bedingung **"ist"** verwendet und festgelegt, dass die **mit einem Haken versehenen** Zeilen markiert werden sollen.

![Farbliche Markierung von Zeilen](images/Farbliche-Markierung-von-Zellen-9.png)

### Beispiel für eine Regel mit mehreren Bedingungen

In diesem Beispiel möchten wir nur Zeilen des Redaktionsplans farblich hervorheben, wenn der **Status** des Posts nicht "fertig" ist, das **Veröffentlichungsdatum** in der Zukunft liegt und bereits ein **Bild** vorhanden ist.

![Regel mit mehreren Bedingungen für die farbliche Zeilenmarkierung](images/Regel-mit-mehreren-Bedingungen-fuer-die-farbliche-Zeilenmarkierung.png)

## Duplikate hervorheben

Zeilen mit einem oder mehreren identischen Spaltenwerten können Sie mit der Option **Duplikate hervorheben** farblich markieren. Wählen Sie hierzu die Spalte aus, die Sie auf Duplikate prüfen möchten. So können Sie Duplikate in Ihrer Tabelle leicht identifizieren und ggf. korrigieren oder löschen.

![Farbliche Markierung von Zellen-Duplikate hervorheben](images/Farbliche-Markierung-von-Zellen-9-1.png)
