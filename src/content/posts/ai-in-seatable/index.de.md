---
title: 'KI in SeaTable: Automatisch verarbeiten oder direkt fragen'
description: 'SeaTable bietet ab sofort zwei Wege, KI inIhre Arbeit zu integrieren: Automationen, die Rechnungen auslesen, Tickets sortieren und Texte zusammenfassen, DSGVO-konform auf unserem Server in Deutschland. Und einen KI-Chatbot, der Ihre Daten versteht und auf Fragen in natürlicher Sprache antwortet. Warum es zwei Wege braucht und wann Sie welchen nutzen, erklären wir hier.'
date: 2026-03-17
lastmod: '2026-03-17'
url: '/de/ki-in-seatable-automationen-und-chatbot'
seo:
    title: 'KI in SeaTable: Automationen & Chatbot für Ihre Daten'
    description: 'SeaTable bietet zwei Wege für KI: DSGVO-konforme Automationen auf unserem Server in Deutschland und einen KI-Chatbot, der Ihre Daten versteht und auf Fragen antwortet.'
categories:
    - 'low-code-no-code'
tags:
    - 'IT Prozesse'
    - 'Künstliche Intelligenz'
    - 'No Code & Low Code'
    - 'IT Sicherheit & Datenschutz'
color: '#ff3d33'
---

Stellen Sie sich vor, Sie öffnen Ihre SeaTable-Base mit 2.000 Projekteinträgen. Doch statt Filter zu setzen, Ansichten zu konfigurieren und Formeln zu schreiben, tippen Sie:

> „Welche Projekte sind überfällig? Gruppiere sie nach Verantwortlichem."

Und die KIantwortet. Nicht mit einer vagen Vermutung, sondern mit den echten Daten aus Ihrer Base. Und das innerhalb von Sekunden. Das ist keine Zukunftsmusik. Das geht jetzt mit dem neuen KI-Chat-Plugin in SeaTable.

Aber fangen wir vorne an. Denn KI inSeaTable ist mehr als ein Chatbot.

## Bisher: KI-Automationen, die unsichtbaren Helfer

Mit SeaTable 6.0 haben wir KI-Automationen eingeführt. Das Prinzip: Sie definieren eine Aufgabe, und die KIerledigt sie automatisch im Hintergrund. Zeile für Zeile, ohne dass Sie aktiv warten müssen.

![Anlage einer neuen KI-Automationen in SeaTable](images/ai-automation-overview.png)

Vier Funktionen stehen bereit: **Summarize, OCR, Extract und Classify**. Dazu kommt eine **Custom Function**, mit der Sie eigene Prompts definieren können.

![KI Funktionen in Seatable Automationen](images/automation-select-ai-function.png)

### Was heißt das konkret?

- **Rechnungsverarbeitung:** Eingehende Rechnungen werden per OCR ausgelesen. Rechnungsnummer, Datum, Betrag und Absender landen automatisch in den richtigen Spalten, ohne manuelles Abtippen.
- **Support-Tickets:** Eingehende Anfragen werden analysiert, kategorisiert und dem richtigen Team zugeordnet. Bevor ein Mensch die Anfrage sieht, ist sie schon sortiert.
- **Dokumenten-Zusammenfassung:** Ein 20-seitiger Bericht wird in wenigen Sekunden auf die wesentlichen Punkte komprimiert.
- **Mehrsprachige Klassifizierung:** Ob Deutsch, Englisch oder Französisch: die KIerkennt die Sprache und ordnet den Inhalt korrekt ein.

### Wo laufen diese Automationen?

Auf **unserem eigenen KI-Server in Deutschland**, im Rechenzentrum von Hetzner. Wir betreiben ein eigenes Sprachmodell, das die Verarbeitung übernimmt. Ihre Daten verlassen zu keinem Zeitpunkt unsere europäische Infrastruktur.

Für Organisationen, die Wert auf DSGVO-Konformität und Datensouveränität legen (Universitäten, Forschungseinrichtungen, öffentlicher Sektor), ist das entscheidend. Keine Daten fließen an OpenAI, Google oder andere US-Anbieter.

Enterprise-Kunden erhalten KI-Credits, die im Abonnement enthalten sind.

## Ab sofort: Der KI-Chatbot. Sprechen Sie mit Ihren Daten

Die Automationen sind leistungsstark, aber sie arbeiten nach festen Regeln: eine Zeile rein, ein Ergebnis raus. Was aber, wenn Sie eine offene Frage haben? Wenn Sie nicht wissen, welchen Filter Sie setzen müssen, oder wenn Sie eine Analyse über Ihre gesamte Datenbasis brauchen?

Dafür gibt es ab SeaTable 6.1 das **KI-Chat-Plugin** (Beta).

![AI Chat Plugin SeaTable](images/ai-chat-plugin.png)

### So funktioniert es

Sie öffnen den Chat in Ihrer Base und stellen Ihre Frage in natürlicher Sprache. Die KIkennt die Struktur Ihrer Base (Tabellen, Spalten, Verknüpfungen) und fragt gezielt die relevanten Daten ab. Kein Export, kein Copy-Paste, kein Erklären der Tabellenstruktur.

Einige Beispiele:

- *„Wie viele offene Deals haben wir über 10.000 Euro, die seit 30 Tagen keinen Kontakt hatten?"*
- *„Fasse die Support-Anfragen der letzten Woche zusammen und zeige die häufigsten Themen."*
- *„Erstelle für jeden überfälligen Task einen Follow-up-Eintrag in der Aktivitäten-Tabelle."*

Ja, der Chatbot kann nicht nur lesen, sondern auch **schreiben**: Zeilen erstellen, aktualisieren, verknüpfen und löschen. Alles direkt in Ihrer Base.

### Wie ist das möglich?

Hinter dem Chatbot steckt der **SeaTable MCP Server**. MCP steht für Model Context Protocol, ein offener Standard, der es KI-Modellen ermöglicht, aktiv mit Datenquellen zu interagieren. Statt der KIIhre Daten in den Chat zu kopieren, fragt die KIüber MCP eigenständig ab, was sie braucht. Live, in Echtzeit, immer aktuell.

Das unterscheidet unseren Ansatz grundlegend von Lösungen, bei denen Sie Daten als CSV exportieren und in ein ChatGPT-Fenster einfügen. Der Chatbot arbeitet direkt mit Ihrer Base, ohne Umwege und ohne Informationsverlust.

### Welche Modelle werden unterstützt?

Der Chatbot nutzt leistungsstarke KI-Modelle, die komplexe Fragen beantworten und mehrstufig mit Ihren Daten arbeiten können. Aktuell unterstützen wir:

- **Anthropic Claude** (Haiku und Sonnet)
- **OpenAI** (GPT-4o und GPT-4o mini)
- **Mistral** (Mistral Large und Mistral Small)

Sie bringen Ihren eigenen API-Key mit und zahlen die Token-Kosten direkt beim jeweiligen Anbieter. Das ist transparent: Sie sehen genau, was jede Interaktion kostet, und behalten die volle Kontrolle.

## Warum zwei Wege statt einem?

Eine berechtigte Frage. Warum nicht einfach alles über den Chatbot laufen lassen?

Die Antwort: Weil unterschiedliche Aufgaben unterschiedliche Anforderungen haben.

| | KI-Automationen | KI-Chatbot |
|---|---|---|
| **Aufgabe** | Definiert: OCR, Zusammenfassung, Klassifizierung | Offen: Fragen, Analysen, explorative Suche |
| **Interaktion** | Im Hintergrund, automatisch | Echtzeit-Dialog |
| **Daten** | Eine Zeile als Input | Ganze Base als Grundlage |
| **KI-Modell** | Unser Server in Deutschland | Ihr Modell (Claude, OpenAI oder Mistral) |
| **Datensouveränität** | Maximal: Daten bleiben auf unserer Infrastruktur | Sie entscheiden: Daten gehen an den gewählten KI-Anbieter |
| **Kosten** | Im Enterprise-Abo enthalten | Token-Kosten beim KI-Anbieter |

Beide Wege ergänzen sich. Nutzen Sie Automationen für wiederkehrende Aufgaben, die zuverlässig im Hintergrund laufen sollen. Nutzen Sie den Chatbot, wenn Sie Fragen haben, die Sie nicht mit einem Filter beantworten können.

## Ihre Daten bleiben unter Ihrer Kontrolle

Unabhängig davon, welchen Weg Sie wählen: Kontrolle und Sicherheit stehen an erster Stelle.

**Bei Automationen** verlassen Ihre Daten nie unsere europäische Infrastruktur. Das Sprachmodell läuft auf unserem eigenen Server in Deutschland.

**Beim Chatbot** werden Daten an den KI-Anbieter übermittelt, den Sie gewählt haben. Das ist technisch notwendig, damit das Modell Ihre Fragen beantworten kann. Aber Sie entscheiden, welcher Anbieter das ist.

![Datenfluss beim KI-Chatbot](images/dataflow-ai-agent.png)

Doch nicht nur das: Das KI-Chat-Plugin unterscheidet automatisch zwischen Leseoperationen und destruktiven Aktionen wie Löschungen oder Updates. Bevor Daten geändert werden, fragt das Plugin um Ihre Bestätigung: was genau geändert wird und wie viele Zeilen betroffen sind. Sie können einmalig zustimmen, für die gesamte Session erlauben oder ablehnen. Auch bei besonders großen Ergebnismengen wird nachgefragt, bevor die KITausende von Zeilen verarbeitet.

## So starten Sie

### KI-Automationen

Verfügbar für alle Enterprise-Kunden in SeaTable Cloud und für Self-Hoster ab Version 6.0. Erstellen Sie eine neue Automation in Ihrer Base, wählen Sie eine KI-Funktion (Summarize, OCR, Extract, Classify oder Custom) und definieren Sie Input- und Output-Spalte. Die Automation läuft ab sofort bei jedem neuen Eintrag.

Mit SeaTable 6.1 werden wir Automationen (und damit auch KI-Automationen) in geringem Umfang auch für Free- und Plus-Kunden zur Verfügung stellen.

Eine detaillierte Anleitung finden Sie in unserem [Hilfebereich]({{< relref "help/ai/ai-automations" >}}).

### KI-Chatbot

Ab SeaTable 6.1 können Sie das KI-Chat-Plugin (Beta) in Ihrer Base installieren. Hinterlegen Sie Ihren API-Key (Claude, OpenAI oder Mistral) in den Plugin-Einstellungen. Stellen Sie Ihre erste Frage. Der Chatbot erkennt die Struktur Ihrer Base automatisch und wird Ihre Frage beanworten.

## Ausblick

Wir arbeiten kontinuierlich an der Erweiterung der KI-Funktionen in SeaTable:

- **Verbessertes API-Key-Management:** Aktuell wird der API-Key in den Plugin-Einstellungen gespeichert. Für eine zukünftige Version arbeiten wir an einer zentralen, sichereren Lösung für die Verwaltung von API-Keys.
- **KI Usage Tracking:** Transparente Übersicht über Ihren Token-Verbrauch.
- **Allgemeiner KI-Assistent:** Ein Assistent, der Sie mit mehreren Bases gleichzeitig sprechen lässt.

Die Möglichkeiten, KI in Ihre tägliche Arbeit zu integrieren, wachsen rasant. Mit SeaTable haben Sie die Werkzeuge, um davon zu profitieren, ohne Kompromisse bei der Kontrolle über Ihre Daten.

{{< newsletter />}}
