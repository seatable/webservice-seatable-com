---
title: 'Was sind KI-Automationen?'
description: 'KI-Automationen verarbeiten Daten in Ihrer Base automatisch — vom Kategorisieren bis zur Zusammenfassung.'
weight: 1
url: '/de/hilfe/ki-automationen-in-seatable'
seo:
    title: 'KI-Automationen in SeaTable: Daten automatisch verarbeiten'
    description: 'SeaTable KI-Automationen kategorisieren, übersetzen und fassen Ihre Daten automatisch zusammen — DSGVO-konform auf Servern in Deutschland.'
star: true
---

SeaTable bietet seit Version 6.0 KI-gestützte Automationsaktionen, die Ihre Daten automatisch verarbeiten können. Texte zusammenfassen, Supportanfragen kategorisieren, Rechnungsdaten extrahieren oder Inhalte übersetzen — all das passiert direkt in Ihrer Base, ausgelöst durch die Automationsregeln, die Sie bereits aus SeaTable kennen. Keine externe KI-Plattform nötig, keine manuelle Nacharbeit.

{{< youtube uCE6JeR_7Uo >}}

## Wie funktionieren KI-Automationen?

KI-Automationen sind Aktionen innerhalb des SeaTable-Automationssystems. Sie funktionieren nach dem gleichen Prinzip wie alle anderen Automationen: Ein **Trigger** löst eine oder mehrere **Aktionen** aus. Der Unterschied ist, dass KI-Aktionen ein Sprachmodell nutzen, um Inhalte zu verstehen und zu verarbeiten.

Ein typischer Ablauf sieht so aus:

1. Ein neuer Eintrag wird in einer Tabelle angelegt (Trigger).
2. Eine KI-Aktion liest den Inhalt einer bestimmten Spalte — zum Beispiel den Text einer Supportanfrage.
3. Das Sprachmodell analysiert den Text und schreibt das Ergebnis in eine andere Spalte — zum Beispiel die Kategorie "Technisches Problem" oder eine Zusammenfassung in drei Sätzen.

Das passiert vollautomatisch im Hintergrund. Sie müssen nicht eingreifen und keine Fragen formulieren — die KI arbeitet regelbasiert mit den Vorgaben, die Sie in der Automation festgelegt haben.

## Was kann die KI automatisieren?

In SeaTable erstellen Sie eine Automation mit der Aktion Run AI und wählen eine der fünf verfügbaren Funktionen:

- **Summarize**: Längere Texte, Berichte oder Notizen werden automatisch auf das Wesentliche komprimiert. Nützlich, wenn in einer Spalte ausführliche Beschreibungen stehen und Sie in einer weiteren Spalte eine kurze Zusammenfassung brauchen.
- **Classify**: Eingehende Texte werden analysiert und einer Kategorie zugeordnet. Typisches Beispiel: Supportanfragen werden automatisch als "Technisch", "Rechnung" oder "Allgemein" eingestuft und in einer Single-Select-Spalte abgelegt.
- **OCR**: Texte werden aus Bildern oder gescannten Dokumenten erkannt und ausgelesen — zum Beispiel aus einem Foto einer Visitenkarte oder einem eingescannten Lieferschein.
- **Extract**: Aus unstrukturiertem Text werden gezielt Informationen herausgelesen — zum Beispiel Rechnungsnummer, Datum und Betrag aus einer Rechnung.
- **Custom**: Für alle Fälle, die nicht in die vier Standardfunktionen passen, definieren Sie einen eigenen Prompt. So können Sie die KI zum Beispiel Texte übersetzen, Antwortvorschläge formulieren oder Inhalte nach Ihren eigenen Kriterien bewerten lassen.

## KI-Automationen vs. KI-Agenten

SeaTable bietet zwei Wege, KI mit Ihren Daten arbeiten zu lassen. Beide ergänzen sich, funktionieren aber grundlegend unterschiedlich:

**KI-Automationen** laufen automatisch im Hintergrund, ausgelöst durch Regeln. Sie eignen sich für wiederkehrende Aufgaben, die bei jedem neuen Eintrag gleich ablaufen sollen — zum Beispiel jede eingehende Supportanfrage kategorisieren oder jede neue Notiz zusammenfassen.

**KI-Agenten** arbeiten interaktiv. Sie stellen eine Frage, der Agent antwortet. Das eignet sich für Ad-hoc-Analysen, flexible Abfragen und einmalige Aufgaben — zum Beispiel "Welche Kunden hatten diesen Monat keinen Umsatz?"

| | KI-Automationen | KI-Agenten |
|---|---|---|
| **Auslöser** | Automatisch (Regel/Ereignis) | Manuell (Ihre Frage) |
| **Interaktion** | Keine — läuft im Hintergrund | Dialog in natürlicher Sprache |
| **Typischer Einsatz** | Kategorisieren, Zusammenfassen, Extrahieren | Abfragen, Analysieren, Bearbeiten |
| **KI-Modell** | SeaTable-eigener KI-Server (EU) | Externer Anbieter (z.B. Anthropic) |
| **Datenverarbeitung** | Komplett in der EU | Daten werden an KI-Anbieter übertragen |

Mehr zu KI-Agenten erfahren Sie im Artikel [Was sind KI-Agenten?]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}).

## Datenschutz: KI made in Europe

Ein wesentlicher Vorteil der KI-Automationen gegenüber externen KI-Diensten: **Ihre Daten verlassen die EU nicht.** SeaTable betreibt einen eigenen KI-Server mit dem Open-Source-Modell Gemma-3-12B auf GPU-Infrastruktur bei Hetzner in Deutschland.

Das bedeutet konkret:

- Ihre Daten werden nicht an OpenAI, Google oder andere US-Anbieter übertragen.
- Es findet kein Training mit Ihren Daten statt — das Modell ist vortrainiert und lernt nicht aus Ihren Eingaben.
- Die Verarbeitung ist DSGVO-konform und unterliegt ausschließlich europäischem Recht.

Für Unternehmen, die mit personenbezogenen Daten, vertraulichen Dokumenten oder sensiblen Geschäftsinformationen arbeiten, ist das ein entscheidender Unterschied zu KI-Lösungen, bei denen Daten in die USA fließen.

## Verfügbarkeit

KI-Automationen stehen ab SeaTable Version 6.0 zur Verfügung. Enterprise-Kunden können die Funktionen ohne Zusatzkosten nutzen. Für Free- und Plus-Pläne wird ab Version 6.1 ein begrenztes Kontingent verfügbar sein.

## Nächste Schritte

- [KI-Automation einrichten — Schritt-für-Schritt-Anleitung]({{< relref "help/ai/ai-automations/setup-ai-automation" >}})
- [Texte zusammenfassen (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Einträge klassifizieren (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Texterkennung aus Bildern (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
- [Informationen extrahieren (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Benutzerdefinierte KI-Aktion (Custom)]({{< relref "help/ai/ai-automations/custom" >}})