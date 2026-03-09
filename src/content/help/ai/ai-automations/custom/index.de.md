---
title: 'Benutzerdefinierte KI-Aktion (Custom)'
description: 'Mit der KI-Funktion Custom definieren Sie einen eigenen Prompt und lassen die KI beliebige Aufgaben auf Ihren Daten ausführen.'
weight: 7
url: '/de/hilfe/ki-automation-benutzerdefinierte-aktion'
seo:
    title: 'KI-Automation: Benutzerdefinierte KI-Aktion in SeaTable'
    description: 'So erstellen Sie benutzerdefinierte KI-Automationen in SeaTable: Eigenen Prompt schreiben und Texte übersetzen, umformulieren oder bewerten lassen.'
---

Die KI-Funktion **Custom** ist die flexibelste der fünf KI-Aktionen. Sie schreiben einen eigenen Prompt und bestimmen damit frei, was die KI mit Ihren Daten macht. Alles, was nicht in die vier Standardfunktionen (Summarize, Classify, OCR, Extract) passt, lässt sich mit Custom umsetzen.

## Typische Anwendungsfälle

- **Übersetzen**: Texte automatisch in eine andere Sprache übersetzen.
- **Umformulieren**: Texte in einen anderen Ton oder Stil umschreiben (z. B. formell, kundenfreundlich, vereinfacht).
- **Antwortvorschläge**: Basierend auf einer Kundenanfrage einen Antwortentwurf generieren.
- **Bewerten**: Texte nach eigenen Kriterien auf einer Skala einschätzen (z. B. Relevanz, Qualität, Dringlichkeit).
- **Generieren**: Produktbeschreibungen, Social-Media-Posts oder Meta-Texte aus Stichpunkten erzeugen.
- **Korrigieren**: Rechtschreib- und Grammatikfehler in Texten automatisch korrigieren.

## Voraussetzungen

- Eine Tabelle mit mindestens einer Spalte, deren Inhalt die KI verarbeiten soll.
- Eine **Text-Spalte** oder **Formatierter-Text-Spalte** für das Ergebnis.

## Schritt-für-Schritt-Anleitung

### 1. Automation anlegen und Trigger wählen

Erstellen Sie eine neue Automationsregel wie im Artikel [KI-Automation einrichten]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}) beschrieben. Wählen Sie den passenden Trigger für Ihren Anwendungsfall.

### 2. Aktion "KI aufrufen" hinzufügen

Klicken Sie auf **Aktion hinzufügen** und wählen Sie **KI aufrufen**.

### 3. Funktion "Custom" auswählen

Wählen Sie in den Aktionseinstellungen:

- **Tabelle**: Die Tabelle, in der die KI arbeiten soll.
- **Funktion**: **Custom**

![Aktionseinstellungen mit ausgewählter Funktion Custom](images/ai-automation-custom.png)

### 4. Prompt schreiben

Der Prompt ist das Herzstück der Custom-Funktion. Hier formulieren Sie die Anweisung an die KI. Verwenden Sie **{Spaltenname}** in geschweiften Klammern, um den Wert einer Spalte aus der aktuellen Zeile in den Prompt einzufügen.

**Aufbau eines guten Prompts:**

```
Übersetze den folgenden Text ins Englische.
Behalte den Ton und die Formatierung bei.

Text: {Beschreibung}
```

In diesem Beispiel wird `{Beschreibung}` bei jeder Ausführung durch den tatsächlichen Inhalt der Spalte "Beschreibung" ersetzt.

![Prompt-Eingabefeld mit Spaltenreferenz](images/ai-automation-custom-reference-column-by-name.png)

### 5. Ergebnisspalte festlegen

Wählen Sie die Spalte, in die das KI-Ergebnis geschrieben werden soll. Diese muss vom Typ **Text** oder **Formatierter Text** sein.

### 6. Speichern und testen

Klicken Sie auf **Speichern** und testen Sie die Automation mit einem Eintrag. Prüfen Sie, ob das Ergebnis in der Ergebnisspalte Ihren Erwartungen entspricht, und passen Sie den Prompt bei Bedarf an.

## Prompt-Beispiele für häufige Aufgaben

### Texte übersetzen

```
Übersetze den folgenden Text ins Englische.
Behalte Fachbegriffe bei und übersetze sie nicht.

Text: {Produktbeschreibung}
```

### Antwortvorschlag generieren

```
Schreibe eine freundliche und professionelle Antwort
auf die folgende Kundenanfrage. Die Antwort soll maximal
fünf Sätze lang sein.

Anfrage: {Kundenanfrage}
```

### Text umformulieren

```
Formuliere den folgenden Text so um, dass er für eine
Pressemitteilung geeignet ist. Verwende einen sachlichen,
professionellen Ton.

Originaltext: {Notizen}
```

### Inhalt bewerten

```
Bewerte den folgenden Text auf einer Skala von 1 bis 5
hinsichtlich seiner Dringlichkeit. Antworte nur mit der
Zahl und einer kurzen Begründung in einem Satz.

Text: {Supportanfrage}
```

### Produktbeschreibung generieren

```
Erstelle eine ansprechende Produktbeschreibung für einen
Online-Shop basierend auf den folgenden Stichpunkten.
Die Beschreibung soll 50-80 Wörter lang sein.

Produktname: {Name}
Eigenschaften: {Eigenschaften}
Zielgruppe: {Zielgruppe}
```

### Rechtschreibung und Grammatik korrigieren

```
Korrigiere Rechtschreib- und Grammatikfehler im folgenden
Text. Ändere den Inhalt und die Formulierungen nicht.
Gib nur den korrigierten Text zurück.

Text: {Freitext}
```

## Anwendungsbeispiel: Produktbeschreibungen übersetzen

In Ihrer Produkttabelle stehen deutsche Produktbeschreibungen. Für den internationalen Online-Shop benötigen Sie englische Übersetzungen. Statt jede Beschreibung manuell zu übersetzen, soll die KI das automatisch erledigen.

**Konfiguration:**

- **Trigger**: Wenn eine Zeile hinzugefügt wird
- **Funktion**: Custom
- **Prompt**: *Übersetze den folgenden deutschen Text ins Englische. Verwende einen ansprechenden Ton, der für einen Online-Shop geeignet ist. Behalte Produktnamen und Markenbezeichnungen bei. Text: {Beschreibung DE}*
- **Ergebnisspalte**: Beschreibung EN (Text-Spalte)

Sobald ein neues Produkt mit deutscher Beschreibung eingetragen wird, erscheint automatisch die englische Übersetzung in der Ergebnisspalte.

## Tipps für gute Prompts

- **Seien Sie konkret.** "Schreibe einen guten Text" liefert unvorhersehbare Ergebnisse. "Schreibe eine Produktbeschreibung mit 50-80 Wörtern in einem freundlichen Ton" ist deutlich besser.
- **Nutzen Sie Spaltenreferenzen.** Mit `{Spaltenname}` können Sie Werte aus mehreren Spalten in einem Prompt kombinieren und so Kontext liefern.
- **Definieren Sie das Ausgabeformat.** Soll das Ergebnis ein einzelner Satz sein? Eine Liste? Eine Zahl mit Begründung? Geben Sie es im Prompt vor.
- **Testen und iterieren.** Probieren Sie den Prompt mit verschiedenen Einträgen aus. Wenn die Ergebnisse nicht passen, passen Sie die Formulierung an.
- **Schreiben Sie den Prompt in der Zielsprache.** Wenn das Ergebnis auf Englisch sein soll, schreiben Sie den Prompt auf Englisch. Das verbessert die Ergebnisqualität.

## Nächste Schritte

- [Texte zusammenfassen (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Einträge klassifizieren (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Informationen extrahieren (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Texterkennung aus Bildern (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
