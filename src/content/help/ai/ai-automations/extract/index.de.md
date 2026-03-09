---
title: 'Informationen extrahieren (Extract)'
description: 'Mit der KI-Funktion Extract lesen Sie gezielt Informationen aus Texten heraus und schreiben sie in separate Spalten.'
weight: 6
url: '/de/hilfe/ki-automation-informationen-extrahieren'
seo:
    title: 'KI-Automation: Informationen automatisch extrahieren in SeaTable'
    description: 'So extrahieren Sie Daten aus Texten in SeaTable: KI-Automation mit der Funktion Extract einrichten — Rechnungsnummern, Daten und Beträge automatisch auslesen.'
---

Die KI-Funktion **Extract** liest gezielt bestimmte Informationen aus unstrukturiertem Text heraus und schreibt sie in einzelne Spalten. So verwandeln Sie Fließtext in strukturierte Daten — zum Beispiel Rechnungsnummer, Datum und Betrag aus einem Rechnungstext.

## Typische Anwendungsfälle

- **Rechnungen**: Rechnungsnummer, Datum, Betrag und Empfänger aus Rechnungstexten herauslesen.
- **E-Mails**: Absendername, Betreff und Kernanliegen aus eingehenden Nachrichten extrahieren.
- **Verträge**: Vertragslaufzeit, Kündigungsfrist und Vertragspartner aus Vertragstexten erfassen.
- **Bestellungen**: Artikelnummer, Menge und Lieferadresse aus Bestelltexten auslesen.
- **Visitenkarten** (nach OCR): Name, Firma, Telefonnummer und E-Mail aus dem erkannten Text herauslesen.

## Voraussetzungen

- Eine Tabelle mit mindestens einer **Text-Spalte**, die den zu analysierenden Text enthält.
- Eine oder mehrere **Ergebnisspalten**, in die die extrahierten Informationen geschrieben werden.

## Schritt-für-Schritt-Anleitung

### 1. Automation anlegen und Trigger wählen

Erstellen Sie eine neue Automationsregel wie im Artikel [KI-Automation einrichten]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}) beschrieben. Wählen Sie einen passenden Trigger — zum Beispiel **Wenn eine Zeile hinzugefügt wird**, damit neue Einträge sofort verarbeitet werden.

### 2. Aktion "KI aufrufen" hinzufügen

Klicken Sie auf **Aktion hinzufügen** und wählen Sie **KI aufrufen**.

### 3. Funktion "Extract" auswählen

Wählen Sie in den Aktionseinstellungen:

- **Tabelle**: Die Tabelle, in der die KI arbeiten soll.
- **Funktion**: **Extract**

![Aktionseinstellungen der ausgewählten Funktion Extract](images/ai-automations-extract.png)

### 4. Input-Spalte festlegen

Wählen Sie die Spalte, deren Inhalt die KI analysieren soll. Das ist typischerweise eine **Text-Spalte** mit unstrukturiertem Text — zum Beispiel der Volltext einer Rechnung oder einer E-Mail.

### 5. Prompt definieren

Der Prompt ist bei der Extract-Funktion besonders wichtig. Beschreiben Sie genau, **welche Informationen** die KI herauslesen soll. Seien Sie so präzise wie möglich.

**Beispiel-Prompts:**

| Prompt | Extrahierte Informationen |
|---|---|
| *Extrahiere die Rechnungsnummer, das Rechnungsdatum und den Gesamtbetrag.* | Drei einzelne Werte |
| *Lies den Namen, die Firma und die E-Mail-Adresse aus dem Text heraus.* | Kontaktdaten |
| *Finde das Startdatum, das Enddatum und die Kündigungsfrist.* | Vertragsinformationen |
| *Extrahiere die Artikelbezeichnung und die Bestellmenge.* | Bestelldetails |

### 6. Ergebnisspalten festlegen

Ordnen Sie jede zu extrahierende Information einer eigenen **Ergebnisspalte** zu. Wählen Sie den Spaltentyp passend zum erwarteten Inhalt — die KI erkennt das Format und schreibt die Werte direkt in den richtigen Spaltentyp. So landen Datumsangaben zuverlässig in einer Datums-Spalte und Texte in einer Text-Spalte.

![Mehrere Ergebnisspalten konfigurieren](images/ai-automation-extract-output-mapping.png)

### 7. Speichern und testen

Klicken Sie auf **Speichern** und testen Sie die Automation mit einem Eintrag, der die zu extrahierenden Informationen enthält. Prüfen Sie, ob die Werte korrekt in den Ergebnisspalten landen.

## Anwendungsbeispiel: Rechnungsdaten auslesen

In Ihrer Tabelle speichern Sie eingehende Rechnungen als Fließtext (oder nach OCR-Erkennung). Sie möchten automatisch die wichtigsten Rechnungsdaten in einzelne Spalten extrahieren.

**Konfiguration:**

- **Trigger**: Wenn eine Zeile hinzugefügt wird
- **Funktion**: Extract
- **Input-Spalte**: Rechnungstext
- **Prompt**: *Extrahiere aus dem Rechnungstext folgende Informationen: Rechnungsnummer, Rechnungsdatum (im Format TT.MM.JJJJ), Nettobetrag, MwSt-Betrag und Bruttobetrag.*
- **Ergebnisspalten**: Rechnungsnummer, Rechnungsdatum, Nettobetrag, MwSt, Bruttobetrag

Sobald ein neuer Eintrag mit einem Rechnungstext erstellt wird, extrahiert die KI die relevanten Daten und schreibt sie in die jeweiligen Spalten.

## Tipps für gute Ergebnisse

- **Seien Sie im Prompt spezifisch.** Statt "Extrahiere die wichtigen Informationen" schreiben Sie genau, welche Felder Sie brauchen. Je präziser der Prompt, desto zuverlässiger das Ergebnis.
- **Geben Sie das gewünschte Format an.** Wenn Sie ein Datum im Format TT.MM.JJJJ brauchen, schreiben Sie das in den Prompt. Gleiches gilt für Beträge mit oder ohne Währungssymbol.
- **Testen Sie mit verschiedenen Texten.** Rechnungen unterschiedlicher Absender haben unterschiedliche Formate. Prüfen Sie, ob die KI auch bei abweichenden Layouts die richtigen Informationen findet.
- **Kombinieren Sie Extract mit OCR.** Wenn Ihre Quelldaten als Bilder vorliegen (z. B. eingescannte Rechnungen), nutzen Sie zuerst die [OCR-Funktion]({{< relref "help/ai/ai-automations/ocr" >}}) und dann Extract in einer zweiten Aktion.

## Nächste Schritte

- [Texterkennung aus Bildern (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
- [Texte zusammenfassen (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Benutzerdefinierte KI-Aktion (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
