---
title: 'Texte zusammenfassen (Summarize)'
description: 'Mit der KI-Funktion Summarize fassen Sie lange Texte in Ihrer SeaTable-Base automatisch zusammen.'
weight: 3
url: '/de/hilfe/ki-automation-texte-zusammenfassen'
seo:
    title: 'KI-Automation: Texte automatisch zusammenfassen in SeaTable'
    description: 'So fassen Sie Texte in SeaTable automatisch zusammen: KI-Automation mit der Funktion Summarize einrichten — Länge, Ton und Sprache per Prompt steuern.'
---

Die KI-Funktion **Summarize** fasst den Inhalt einer oder mehrerer Spalten automatisch zusammen. Das ist besonders nützlich, wenn in Ihrer Tabelle lange Beschreibungen, Berichte oder Notizen stehen und Sie in einer weiteren Spalte eine kompakte Zusammenfassung benötigen.

## Typische Anwendungsfälle

- **Supportanfragen**: Ausführliche Problembeschreibungen von Kunden auf zwei bis drei Sätze komprimieren.
- **Meetingnotizen**: Umfangreiche Protokolle zu einer kurzen Zusammenfassung verdichten.
- **Produktbewertungen**: Lange Rezensionen auf die wesentlichen Punkte reduzieren.
- **Bewerbungen**: Anschreiben oder Lebensläufe in Kurzform zusammenfassen.

## Voraussetzungen

- Eine Tabelle mit mindestens einer **Text-Spalte** oder **Formatierter-Text-Spalte**, die als Eingabe dient.
- Eine **Text-Spalte** oder **Formatierter-Text-Spalte** für das Ergebnis (die Zusammenfassung).

## Schritt-für-Schritt-Anleitung

### 1. Automation anlegen und Trigger wählen

Erstellen Sie eine neue Automationsregel wie im Artikel [KI-Automation einrichten]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}) beschrieben. Wählen Sie einen passenden Trigger — zum Beispiel **Wenn eine Zeile hinzugefügt wird**, damit jeder neue Eintrag automatisch zusammengefasst wird.

### 2. Aktion "KI aufrufen" hinzufügen

Klicken Sie auf **Aktion hinzufügen** und wählen Sie **KI aufrufen**.

### 3. Funktion "Summarize" auswählen

Wählen Sie in den Aktionseinstellungen:

- **Tabelle**: Die Tabelle, in der die KI arbeiten soll.
- **Funktion**: **Summarize**

![Aktionseinstellungen für die KI-Funktion Summarize](images/ai-automation-summarize.png)

### 4. Input-Spalten festlegen

Wählen Sie eine oder mehrere Spalten, deren Inhalt zusammengefasst werden soll. Wenn Sie mehrere Spalten auswählen, kombiniert die KI die Inhalte aller Spalten zu einer Zusammenfassung.

### 5. Prompt anpassen

Im Feld **Summary prompt** können Sie steuern, wie die Zusammenfassung aussehen soll. Wenn Sie das Feld leer lassen, erstellt die KI eine Standardzusammenfassung. Mit einem Prompt können Sie Länge, Ton, Format und Sprache beeinflussen.

**Beispiel-Prompts:**

| Prompt | Ergebnis |
|---|---|
| *Die Zusammenfassung soll maximal 50 Wörter umfassen.* | Kurze, knappe Zusammenfassung |
| *Fasse den Text in drei Stichpunkten zusammen.* | Stichpunktartige Übersicht |
| *Erstelle eine formelle Zusammenfassung auf Deutsch.* | Förmlicher Ton, deutsche Sprache |
| *Fasse das Wichtigste in einem Satz zusammen.* | Ein-Satz-Zusammenfassung |

{{< warning headline="Tipp" text="Schreiben Sie den Prompt in der Sprache, in der Sie das Ergebnis erwarten. Ein deutscher Prompt liefert in der Regel eine deutsche Zusammenfassung." />}}

### 6. Ergebnisspalte festlegen

Wählen Sie die Spalte, in die die Zusammenfassung geschrieben werden soll. Diese muss vom Typ **Text** oder **Formatierter Text** sein.

### 7. Speichern und testen

Klicken Sie auf **Speichern**. Testen Sie die Automation, indem Sie das Trigger-Ereignis auslösen — zum Beispiel eine neue Zeile mit einem längeren Text anlegen. Die Zusammenfassung sollte nach wenigen Sekunden in der Ergebnisspalte erscheinen.

## Anwendungsbeispiel: Supportanfragen zusammenfassen

Stellen Sie sich eine Tabelle vor, in der Supportanfragen per Webformular eingehen. Jede Anfrage enthält eine ausführliche **Problembeschreibung** in einer Textspalte. Für den Teamleiter soll automatisch eine **Kurzbeschreibung** erzeugt werden, damit er die Anfragen schneller überblicken kann.

**Konfiguration:**

- **Trigger**: Wenn eine Zeile hinzugefügt wird
- **Funktion**: Summarize
- **Input-Spalte**: Problembeschreibung
- **Prompt**: *Fasse die Supportanfrage in maximal zwei Sätzen zusammen. Nenne das Hauptproblem und die betroffene Funktion.*
- **Ergebnisspalte**: Kurzbeschreibung

Sobald ein Kunde das Formular abschickt und eine neue Zeile entsteht, schreibt die KI automatisch eine Kurzbeschreibung in die Ergebnisspalte.

## Tipps für gute Ergebnisse

- **Geben Sie die gewünschte Länge an.** Ohne Vorgabe kann die Zusammenfassung unterschiedlich lang ausfallen. Ein Prompt wie "maximal 50 Wörter" sorgt für einheitliche Ergebnisse.
- **Nutzen Sie mehrere Input-Spalten**, wenn der Kontext auf verschiedene Spalten verteilt ist. Die KI berücksichtigt alle Eingaben.
- **Testen Sie mit echten Daten.** Legen Sie ein paar Testzeilen mit realistischen Texten an, um die Qualität zu beurteilen, bevor Sie die Automation produktiv einsetzen.

## Nächste Schritte

- [Einträge klassifizieren (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Informationen extrahieren (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Benutzerdefinierte KI-Aktion (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
