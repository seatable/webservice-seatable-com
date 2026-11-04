---
title: 'Schritt 5: Teilnahmebescheinigung'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/de/hilfe/schritt-5-teilnahmebescheinigung'
seo:
    title: 'Schritt 5: Teilnahmebescheinigung per PDF und E-Mail'
    description: 'Erfahren Sie, wie Sie mit SeaTable eine PDF-Teilnahmebescheinigung generieren und automatisch per E-Mail an Kursteilnehmer versenden.'
---

Nach Abschluss Ihrer Dienstleistung möchten Sie den Prozess abrunden, indem Sie den Teilnehmern eine letzte E-Mail senden. Diese E-Mail kann verschiedene Inhalte haben, wie z. B.:

- Eine Teilnahmebestätigung
- Ein Dankeschön für die Teilnahme
- Eine Bitte um Feedback
- Einen Gutschein-Code für den nächsten Kurs
- ...

## Teilnahmebestätigung erstellen und verschicken

In diesem Abschnitt werden wir mit SeaTable eine Teilnahmebestätigung als PDF generieren und diese per E-Mail an die Teilnehmer senden.

### Serienbrief mit dem Seitendesign-Plugin

SeaTable bietet einige Plugins, mit denen Sie zusätzliche Ansichten und Funktionen zu Ihren Daten hinzufügen können. Das Seitendesign-Plugin ermöglicht es, PDF-Dokumente zu erstellen – ähnlich wie bei einem Serienbrief in Microsoft Word.

Mit diesem Plugin können Sie Vorlagen erstellen, die sowohl statische Inhalte (wie Texte oder Logos) als auch dynamische Daten aus Ihrer Base enthalten. Jede Zeile der Tabelle kann ein individuelles Dokument generieren.

{{< warning  headline="Vielseitige Einsatzmöglichkeiten"  text="Das Seitendesign-Plugin bietet viele Möglichkeiten: Neben Teilnahmebescheinigungen können Sie auch Rechnungen, Urkunden, Rundschreiben und vieles mehr erstellen." />}}

Für diesen Kurs haben wir bereits eine einfache Vorlage vorbereitet, um eine Teilnahmebestätigung zu erstellen. Dabei werden Name, Kurs und Kursdatum automatisch eingefügt, während der restliche Text unverändert bleibt.

Nehmen Sie sich ein paar Minuten Zeit, um die Möglichkeiten des Plugins zu erkunden. Versuchen Sie zum Beispiel, ein Logo oder eine Grafik Ihrer Unterschrift hinzuzufügen.

![](images/lvl2-page-design.png)

Wenn Sie auf `{{< seatable-icon icon="dtable-icon-download" >}} PDF` klicken, wird das generierte PDF auf Ihren PC gespeichert.

{{< warning  headline="Vorlagen beziehen sich immer auf eine Tabelle"  text="Beim Erstellen einer neuen Vorlage können Daten immer nur aus einer Tabelle verwendet werden. Wenn Sie Daten aus einer verlinkten Spalte benötigen, müssen Sie diese über Lookup-Spalten einbinden. Dies ist der Grund, warum in der Tabelle Registrations drei ausgeblendete Lookup-Spalten existieren. Diese Spalten werden nur für das Seitendesign-Plugin benötigt und können daher ausgeblendet bleiben." />}}

### Versand per E-Mail

Natürlich möchten Sie das PDF nicht manuell herunterladen und wieder hochladen, um es per E-Mail zu versenden. Stattdessen können Sie eine Schaltfläche in der Tabelle `Registrations` erstellen, die zwei Aktionen hintereinander ausführt:

- `{{< seatable-icon icon="dtable-icon-pdf" >}} PDF erzeugen und in Spalte speichern`
- `{{< seatable-icon icon="dtable-icon-email" >}} E-Mail versenden`

Die Konfiguration dieser Aktionen sollte mittlerweile vertraut sein. Beim Erstellen des PDFs wählen Sie die gewünschte Vorlage und die Spalte, in der das Dokument gespeichert werden soll. Beim Versand der E-Mail geben Sie an, aus welcher Spalte der Anhang gesendet werden soll.

{{< warning  headline="Aktionen werden nacheinander ausgeführt"  text="Es ist kein Problem, dass die Schaltfläche zuerst die PDF-Datei erstellt und anschließend versendet. SeaTable wartet mit dem Versand der E-Mail, bis das PDF erstellt wurde." />}}

### Ein paar Worte zur Dateiverwaltung

In SeaTable werden Dateien und Bilder nicht direkt in den Zellen gespeichert, sondern im zentralen Datenspeicher der Base. Die Zellen enthalten lediglich Verweise auf die jeweiligen Dateien. Diese zentrale Verwaltung hat einige Vorteile:

- Dateien können mehrfach verwendet werden, ohne sie erneut hochladen zu müssen.
- Auch wenn Sie eine Datei aus einer Zelle löschen, bleibt sie in der zentralen Verwaltung verfügbar, bis Sie sie endgültig löschen.

Nehmen Sie sich ein paar Minuten, um sich mit der Dateiverwaltung von SeaTable vertraut zu machen. Weitere Informationen dazu finden Sie in den verlinkten Hilfeartikeln am Ende dieses Abschnitts.

## Hilfeartikel mit weiteren Informationen

- [Anleitung zum Seitendesign-Plugin]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}})
- [Ein PDF-Dokument per Schaltfläche in einer Spalte speichern]({{< relref "help/base-editor/schaltflaechen/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern" >}})
- [Die Datei-Spalte]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}})
- [Die Dateiverwaltung einer Base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}})
