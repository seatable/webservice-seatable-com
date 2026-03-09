---
title: 'Einträge klassifizieren (Classify)'
description: 'Mit der KI-Funktion Classify ordnen Sie Einträge in Ihrer SeaTable-Base automatisch Kategorien zu.'
weight: 4
url: '/de/hilfe/ki-automation-eintraege-klassifizieren'
seo:
    title: 'KI-Automation: Einträge automatisch klassifizieren in SeaTable'
    description: 'So klassifizieren Sie Einträge automatisch in SeaTable: KI-Automation mit der Funktion Classify einrichten — Kategorien definieren und Texte automatisch zuordnen.'
---

Die KI-Funktion **Classify** analysiert den Inhalt einer oder mehrerer Spalten und ordnet jeden Eintrag einer Kategorie zu. Das Ergebnis wird in eine Einfachauswahl- oder Mehrfachauswahl-Spalte geschrieben. So können Sie eingehende Texte automatisch einstufen, ohne jeden Eintrag manuell zu lesen.

## Typische Anwendungsfälle

- **Supporttickets**: Anfragen automatisch als "Technisch", "Rechnung", "Allgemein" oder "Feature-Wunsch" einstufen.
- **Feedback und Bewertungen**: Kundenfeedback nach Stimmung (positiv, neutral, negativ) kategorisieren.
- **E-Mail-Eingang**: Eingehende Nachrichten nach Thema oder Dringlichkeit sortieren.
- **Bewerbungen**: Anschreiben nach Fachgebiet oder Erfahrungslevel einordnen.

## Voraussetzungen

- Eine Tabelle mit mindestens einer **Text-Spalte**, die als Eingabe dient.
- Eine **Einfachauswahl-Spalte** oder **Mehrfachauswahl-Spalte** für das Ergebnis.

{{< warning headline="Wichtig" text="Die Kategorien, in die die KI klassifizieren soll, müssen als **Auswahloptionen** in der Einfachauswahl- oder Mehrfachauswahl-Spalte bereits angelegt sein. Die KI kann nur bestehende Optionen zuweisen." />}}

## Schritt-für-Schritt-Anleitung

### 1. Kategorien in der Auswahl-Spalte anlegen

Bevor Sie die Automation einrichten, legen Sie in der Einfachauswahl-Spalte (oder Mehrfachauswahl-Spalte) alle gewünschten **Kategorien** als Optionen an. Zum Beispiel: "Technisch", "Rechnung", "Allgemein", "Feature-Wunsch".

![Einfachauswahl-Spalte mit angelegten Kategorien](images/ai-automation-classify-options.png)

### 2. Automation anlegen und Trigger wählen

Erstellen Sie eine neue Automationsregel wie im Artikel [KI-Automation einrichten]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}) beschrieben. Ein typischer Trigger ist **Wenn eine Zeile hinzugefügt wird**, damit jeder neue Eintrag sofort klassifiziert wird.

### 3. Aktion "KI aufrufen" hinzufügen

Klicken Sie auf **Aktion hinzufügen** und wählen Sie **KI aufrufen**.

### 4. Funktion "Classify" auswählen

Wählen Sie in den Aktionseinstellungen:

- **Tabelle**: Die Tabelle, in der die KI arbeiten soll.
- **Funktion**: **Classify**

![Aktionsmöglichkeiten für die Funktion Classify](images/ai-automation-classify.png)

### 5. Input-Spalten festlegen

Wählen Sie eine oder mehrere Spalten, deren Inhalt die KI analysieren soll, um die Kategorie zu bestimmen. Die KI liest die Texte aus diesen Spalten und entscheidet anhand des Inhalts, welche Kategorie am besten passt.

### 6. Prompt anpassen

Im Prompt-Feld können Sie der KI zusätzliche Anweisungen geben, wie sie klassifizieren soll. Das ist besonders hilfreich, wenn die Kategorienamen allein nicht eindeutig genug sind.

**Beispiel-Prompts:**

| Prompt | Wirkung |
|---|---|
| *Klassifiziere die Anfrage anhand des Hauptthemas.* | Einfache Zuordnung nach Thema |
| *Wähle "Technisch", wenn es um Fehlermeldungen oder Funktionsstörungen geht. Wähle "Rechnung", wenn es um Zahlungen oder Rechnungen geht. Alles andere ist "Allgemein".* | Klare Regeln für jede Kategorie |
| *Bewerte die Stimmung des Textes: positiv, neutral oder negativ.* | Sentimentanalyse |

{{< warning headline="Tipp" text="Je genauer Sie im Prompt beschreiben, was jede Kategorie bedeutet, desto zuverlässiger klassifiziert die KI. Besonders bei ähnlichen Kategorien lohnt sich eine klare Abgrenzung." />}}

### 7. Ergebnisspalte festlegen

Wählen Sie die [Einfachauswahl-Spalte]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) oder [Mehrfachauswahl-Spalte]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}), in die das Ergebnis geschrieben werden soll.

- **Einfachauswahl**: Die KI wählt genau eine Kategorie aus.
- **Mehrfachauswahl**: Die KI kann mehrere Kategorien gleichzeitig zuweisen.

### 8. Speichern und testen

Klicken Sie auf **Speichern** und testen Sie die Automation mit einem Eintrag, bei dem die Kategorie offensichtlich ist. Prüfen Sie, ob die KI die erwartete Kategorie zuweist.

## Anwendungsbeispiel: Supporttickets kategorisieren

In Ihrem Helpdesk gehen täglich Supportanfragen über ein Webformular ein. Jede Anfrage enthält eine **Beschreibung** des Problems. Sie möchten, dass jedes Ticket automatisch einer Kategorie zugeordnet wird, damit Ihre Mitarbeiter die Tickets gefiltert bearbeiten können.

**Konfiguration:**

- **Trigger**: Wenn eine Zeile hinzugefügt wird
- **Funktion**: Classify
- **Input-Spalte**: Beschreibung
- **Prompt**: *Klassifiziere die Supportanfrage. Wähle "Technisch" für Fehler, Abstürze und Funktionsstörungen. Wähle "Rechnung" für Fragen zu Zahlungen, Rechnungen oder Abonnements. Wähle "Feature-Wunsch" für Verbesserungsvorschläge. Alles andere ist "Allgemein".*
- **Ergebnisspalte**: Kategorie (Einfachauswahl mit den Optionen "Technisch", "Rechnung", "Feature-Wunsch", "Allgemein")

Sobald ein neues Ticket eingeht, ordnet die KI es automatisch der passenden Kategorie zu. Ihre Mitarbeiter können dann nach Kategorie filtern und ihre Tickets priorisieren.

## Tipps für gute Ergebnisse

- **Halten Sie die Anzahl der Kategorien überschaubar.** Fünf bis zehn Kategorien funktionieren in der Regel gut. Bei zu vielen ähnlichen Kategorien sinkt die Treffgenauigkeit.
- **Beschreiben Sie jede Kategorie im Prompt.** Besonders bei uneindeutigen Kategorienamen hilft eine kurze Erklärung der KI bei der Zuordnung.
- **Verwenden Sie eine Einfachauswahl**, wenn jeder Eintrag genau einer Kategorie zugeordnet werden soll. Nutzen Sie eine Mehrfachauswahl nur, wenn ein Eintrag tatsächlich in mehrere Kategorien fallen kann.
- **Prüfen Sie die ersten Ergebnisse.** Passen Sie den Prompt an, wenn die KI wiederholt falsch klassifiziert.

## Nächste Schritte

- [Texte zusammenfassen (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Informationen extrahieren (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Benutzerdefinierte KI-Aktion (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
