---
title: 'Texterkennung aus Bildern (OCR)'
description: 'Mit der KI-Funktion OCR erkennen Sie automatisch Text in Bildern und gescannten Dokumenten in Ihrer SeaTable-Base.'
weight: 5
url: '/de/hilfe/ki-automation-texterkennung-ocr'
seo:
    title: 'KI-Automation: Texterkennung (OCR) in SeaTable'
    description: 'So erkennen Sie Text in Bildern automatisch in SeaTable: KI-Automation mit der Funktion OCR einrichten — Visitenkarten, Rechnungen und Dokumente auslesen.'
---

Die KI-Funktion **OCR** (Optical Character Recognition) erkennt Text in Bildern und schreibt den erkannten Inhalt in eine Textspalte. Damit können Sie gescannte Dokumente, Fotos von Visitenkarten oder Rechnungsbilder automatisch in durchsuchbaren Text umwandeln.

## Typische Anwendungsfälle

- **Visitenkarten**: Fotos von Visitenkarten automatisch als Text erfassen.
- **Rechnungen und Belege**: Eingescannte Rechnungen in lesbaren Text umwandeln.
- **Lieferscheine**: Text aus fotografierten Lieferscheinen auslesen.
- **Handschriftliche Notizen**: Fotos von Notizzetteln digitalisieren.
- **Dokumente**: Gescannte Verträge oder Formulare als Text verfügbar machen.

## Voraussetzungen

- Eine Tabelle mit einer [Bild-Spalte]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) oder einer [Datei-Spalte]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}), die die zu erkennenden Bilder oder Dokumente enthält.
- Eine [Text-Spalte oder Formatierter-Text-Spalte]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) für den erkannten Text.

## Schritt-für-Schritt-Anleitung

### 1. Automation anlegen und Trigger wählen

Erstellen Sie eine neue Automationsregel wie im Artikel [KI-Automation einrichten]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}) beschrieben. Ein typischer Trigger ist **Wenn eine Zeile hinzugefügt wird** — so wird jedes neu hochgeladene Bild automatisch verarbeitet.

Alternativ können Sie **Wenn eine Zeile geändert wird** verwenden und die Bild-Spalte als überwachte Spalte definieren. In diesem Fall wird die OCR-Erkennung jedes Mal ausgelöst, wenn ein neues Bild in die Spalte eingefügt wird.

### 2. Aktion "KI aufrufen" hinzufügen

Klicken Sie auf **Aktion hinzufügen** und wählen Sie **KI aufrufen**.

### 3. Funktion "OCR" auswählen

Wählen Sie in den Aktionseinstellungen:

- **Tabelle**: Die Tabelle, in der die KI arbeiten soll.
- **Funktion**: **OCR**

![Aktionseinstellungen mit ausgewählter Funktion OCR](images/ai-automation-ocr.png)

### 4. Input-Spalte festlegen

Wählen Sie die Spalte, aus der die KI den Text erkennen soll. Als Input-Spalte können Sie eine **Bild-Spalte** oder eine **Datei-Spalte** verwenden. Bei einer Datei-Spalte können Sie zum Beispiel PDFs oder eingescannte Dokumente verarbeiten lassen.

{{< warning headline="Hinweis" text="Wenn eine Bild- oder Datei-Spalte mehrere Dateien enthält, wird nur die **erste Datei** verarbeitet. Laden Sie pro Zeile idealerweise nur ein Bild oder Dokument in die Input-Spalte hoch." />}}

### 5. Ergebnisspalte festlegen

Wählen Sie die Spalte, in die der erkannte Text geschrieben werden soll. Diese muss vom Typ **Text** oder **Formatierter Text** sein.

### 6. Speichern und testen

Klicken Sie auf **Speichern** und laden Sie ein Testbild mit gut lesbarem Text in die Bild-Spalte hoch. Nach wenigen Sekunden sollte der erkannte Text in der Ergebnisspalte erscheinen.

## Anwendungsbeispiel: Visitenkarten digitalisieren

Ihr Vertriebsteam fotografiert auf Messen Visitenkarten und lädt die Fotos in eine SeaTable-Tabelle hoch. Die KI soll den Text auf der Visitenkarte automatisch erkennen, damit Sie die Kontaktdaten durchsuchen können.

**Konfiguration:**

- **Trigger**: Wenn eine Zeile hinzugefügt wird
- **Funktion**: OCR
- **Input-Spalte**: Visitenkartenbild (Bild-Spalte)
- **Ergebnisspalte**: Erkannter Text (Text-Spalte)

Sobald ein neuer Eintrag mit einem Visitenkartenbild erstellt wird, liest die KI den Text aus dem Bild und schreibt ihn in die Ergebnisspalte. Von dort können Sie die Daten weiter verarbeiten — zum Beispiel mit einer anschließenden **Extract**-Aktion, um Name, Firma und Telefonnummer gezielt herauszulesen.

{{< warning headline="Tipp" text="Kombinieren Sie OCR mit der Funktion **Extract** in einer zweiten Aktion derselben Automation. So erkennen Sie zuerst den Text und extrahieren dann in einem zweiten Schritt gezielt die relevanten Informationen in separate Spalten." />}}

## Tipps für gute Ergebnisse

- **Bildqualität zählt.** Je schärfer und kontrastreicher das Bild, desto besser die Texterkennung. Unscharfe Fotos oder schlechte Beleuchtung können zu Fehlern führen.
- **Gedruckter Text funktioniert zuverlässiger als Handschrift.** Maschinenschrift wird nahezu fehlerfrei erkannt. Bei Handschrift hängt die Qualität von der Lesbarkeit ab.
- **Halten Sie das Bild gerade.** Stark verzerrte oder gedrehte Bilder können die Erkennung erschweren.
- **Verwenden Sie gängige Bildformate.** JPG und PNG funktionieren zuverlässig.

## OCR mit Extract kombinieren

Die OCR-Funktion liefert den **gesamten erkannten Text** als Fließtext. Wenn Sie gezielt einzelne Informationen herausholen möchten (z. B. Name, Adresse, Rechnungsnummer), können Sie in derselben Automation eine zweite Aktion mit der Funktion [Extract]({{< relref "help/ai/ai-automations/extract" >}}) hinzufügen. So wird der erkannte Text in einem zweiten Schritt strukturiert in einzelne Spalten aufgeteilt.

## Nächste Schritte

- [Informationen extrahieren (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Texte zusammenfassen (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Benutzerdefinierte KI-Aktion (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
