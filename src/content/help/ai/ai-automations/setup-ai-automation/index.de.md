---
title: 'KI-Automation einrichten'
description: 'Erstellen Sie Schritt für Schritt eine KI-Automation in SeaTable — vom Trigger bis zur fertigen KI-Aktion.'
weight: 2
url: '/de/hilfe/ki-automation-einrichten'
seo:
    title: 'KI-Automation in SeaTable einrichten — Schritt-für-Schritt-Anleitung'
    description: 'So erstellen Sie eine KI-Automation in SeaTable: Trigger wählen, KI-Funktion konfigurieren, Input- und Ergebnisspalten festlegen und die Automation testen.'
---

In dieser Anleitung erstellen Sie eine Automation mit der Aktion **KI aufrufen**. Nach der Einrichtung verarbeitet SeaTable Ihre Daten automatisch mit einem KI-Modell — zum Beispiel um Texte zusammenzufassen, Einträge zu kategorisieren oder Informationen zu extrahieren.

## Voraussetzungen

- Mindestens SeaTable (Cloud oder Server) **Version 6.0**
- Eine Base mit einer Tabelle, die Textdaten enthält

{{< warning headline="Hinweis für Self-Hosted-Kunden" >}}

In der **SeaTable Cloud** ist der KI-Server bereits integriert. SeaTable betreibt ein eigenes Sprachmodell (Gemma 3) auf GPU-Infrastruktur in Deutschland — Sie können KI-Automationen sofort nutzen.

Wenn Sie SeaTable **selbst hosten**, müssen Sie entweder einen eigenen KI-Server betreiben oder eine Verbindung zu einem Cloud-KI-Anbieter konfigurieren. Weitere Informationen finden Sie in der [Installationsanleitung für SeaTable AI](https://admin.seatable.com/installation/components/seatable-ai/).

{{< /warning >}}

## Schritt 1: Automationsregel anlegen

1. Öffnen Sie Ihre Base und klicken Sie im Base-Header auf {{< seatable-icon icon="dtable-icon-rule" >}}, dann auf **Automatisierungsregeln**.
2. Klicken Sie auf **Regel oder Ordner hinzufügen** und wählen Sie **Regel hinzufügen**.
3. Geben Sie der Automation einen aussagekräftigen **Namen**, zum Beispiel "Supportanfragen zusammenfassen".

![Übersichtsseite Automationsregeln](images/ai-automation-overview.png)

## Schritt 2: Trigger wählen

Klicken Sie auf **Trigger hinzufügen** und wählen Sie einen Auslöser. Für KI-Automationen stehen zwei Trigger zur Verfügung:

- **Wenn eine Zeile geändert wird** — die KI verarbeitet die geänderte Zeile sofort
- **Wenn eine Zeile hinzugefügt wird** — die KI verarbeitet jeden neuen Eintrag automatisch

Wählen Sie anschließend die **Tabelle** und die **Ansicht**, in der die Automation wirken soll. Optional können Sie **Bedingungen** festlegen, um die Automation nur für bestimmte Einträge auszulösen.

![Trigger-Auswahl](images/automation-trigger-selection.png)

{{< warning headline="Hinweis" text="Die zeitgesteuerten Trigger (**Zu einer geplanten Zeit** und **Zu einer geplanten Zeit für Einträge, die bestimmte Bedingungen erfüllen**) unterstützen aktuell keine KI-Aktionen." />}}

## Schritt 3: KI-Aktion hinzufügen

1. Klicken Sie auf **Aktion hinzufügen**.
2. Wählen Sie in der Liste der verfügbaren Aktionen ganz unten **KI aufrufen** aus.

![Aktionsliste mit Option Run AI](images/automation-action-run-ai.png)

## Schritt 4: KI-Funktion konfigurieren

Nachdem Sie die Aktion **KI aufrufen** ausgewählt haben, öffnen sich rechts die **Aktionseinstellungen**. Konfigurieren Sie dort:

### Tabelle
Wählen Sie die Tabelle aus, in der die KI arbeiten soll. In der Regel ist das die gleiche Tabelle wie im Trigger.

### Funktion
Wählen Sie eine der fünf verfügbaren KI-Funktionen:

| Funktion | Beschreibung | Typischer Einsatz |
|---|---|---|
| **Summarize** | Fasst Texte zusammen | Lange Beschreibungen komprimieren |
| **Classify** | Ordnet Kategorien zu | Supportanfragen einstufen |
| **OCR** | Erkennt Text in Bildern | Visitenkarten, Rechnungen auslesen |
| **Extract** | Extrahiert gezielt Informationen | Rechnungsnummer, Datum herauslesen |
| **Custom** | Eigener Prompt | Übersetzen, Bewerten, Umformulieren |

![Dropdown mit den fünf KI-Funktionen](images/automation-select-ai-function.png)

### Input-Spalten
Wählen Sie eine oder mehrere Spalten, deren Inhalt die KI verarbeiten soll. Das ist der Text (oder das Bild bzw. die Datei bei OCR), den die KI als Eingabe erhält.

### Prompt
Bei allen Funktionen außer OCR können Sie einen **Prompt** eingeben, um das Ergebnis zu steuern. Zum Beispiel: "Die Zusammenfassung soll maximal zwei Sätze lang sein und auf Deutsch verfasst werden." Bei OCR ist kein Prompt nötig — die KI erkennt den Text im Bild automatisch.

### Ergebnisspalte(n)
Wählen Sie die Spalte, in die das KI-Ergebnis geschrieben werden soll. Der Spaltentyp muss zur gewählten Funktion passen — zum Beispiel eine Text-Spalte für Zusammenfassungen oder eine Einfachauswahl-Spalte für Klassifizierungen.

## Schritt 5: Speichern und aktivieren

1. Klicken Sie auf **Speichern**, um die Aktionseinstellungen zu sichern.
2. Die Automation ist nun aktiv und wird beim nächsten Trigger-Ereignis automatisch ausgeführt.

## Automation testen

Um die Automation sofort zu testen, lösen Sie das Trigger-Ereignis manuell aus:

- Bei **Wenn eine Zeile hinzugefügt wird**: Legen Sie eine neue Zeile mit Testdaten an.
- Bei **Wenn eine Zeile geändert wird**: Ändern Sie einen Wert in einer überwachten Spalte.

Prüfen Sie anschließend, ob die KI das Ergebnis in die Ergebnisspalte geschrieben hat. Im [Ausführungslog]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}}) können Sie den Status und eventuelle Fehler einsehen.

![Ausführungslog einer KI-Automation](images/automation-open-log.png)

## Häufige Probleme

| Problem | Lösung |
|---|---|
| Die Ergebnisspalte bleibt leer | Prüfen Sie, ob die Input-Spalte tatsächlich einen Wert enthält. Leere Eingaben liefern kein Ergebnis. |
| Falscher Spaltentyp | Die Ergebnisspalte muss zum Ergebnis passen. Klassifizierungen brauchen eine Einfachauswahl-Spalte, Zusammenfassungen eine Text-Spalte. |
| Automation wird nicht ausgelöst | Prüfen Sie, ob die Automation aktiviert ist und ob die Änderung in der richtigen Tabelle und Ansicht stattfindet. |

## Nächste Schritte

Detaillierte Anleitungen zu den einzelnen KI-Funktionen finden Sie in diesen Artikeln:

- [Texte zusammenfassen (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Einträge klassifizieren (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Texterkennung aus Bildern (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
- [Informationen extrahieren (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Benutzerdefinierte KI-Aktion (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
