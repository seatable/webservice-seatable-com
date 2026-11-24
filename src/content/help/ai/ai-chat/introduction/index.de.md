---
title: 'Was ist das KI-Chat-Plugin?'
description: 'Das KI-Chat-Plugin ermöglicht es Ihnen, direkt in SeaTable mit Ihren Daten zu chatten. Stellen Sie Fragen in natürlicher Sprache und die KI antwortet mit echten Daten.'
weight: 1
url: '/de/hilfe/ki-chat-plugin-in-seatable'
seo:
    title: 'KI-Chat-Plugin in SeaTable: Chatten Sie mit Ihren Daten'
    description: 'Das KI-Chat-Plugin in SeaTable ermöglicht natürliche Konversation mit Ihren Daten. Fragen stellen, Daten analysieren und bearbeiten, direkt in der Base.'
star: true
---

Das KI-Chat-Plugin ist eine zukunftsweisende Erweiterung in SeaTable, mit der Sie direkt in Ihrer Base einen KI-gestützten Chat nutzen können. Stellen Sie Fragen in natürlicher Sprache, und die KI antwortet auf Basis Ihrer echten Daten. Sie brauchen dafür keine externe Software, keinen separaten KI-Assistenten und keine technische Einrichtung. Der Chat läuft direkt in SeaTable.

**In diesem How-to-Video zeigen wir Ihnen in nur wenigen Minuten, wie Sie das KI-Chat-Plugin nutzen.**
{{< youtube 3O-futjotgU >}}

## Wie funktioniert das KI-Chat-Plugin?

Das Plugin basiert auf dem **Model Context Protocol (MCP)**, dem gleichen offenen Standard, den auch [KI-Agenten]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}) nutzen. Im Hintergrund greift der Chat über den SeaTable MCP Server auf Ihre Daten zu, liest Tabellen, Spalten und Einträge und liefert Ihnen präzise Antworten.

Der entscheidende Unterschied zu KI-Agenten: Sie müssen keine externe Anwendung wie Claude Desktop oder Cursor installieren. Der Chat ist direkt als Plugin in SeaTable verfügbar. Sie öffnen das Plugin, stellen Ihre Frage und erhalten die Antwort, alles innerhalb Ihrer Base.

## Was kann das KI-Chat-Plugin?

Der Chatbot kann sowohl Ihre Daten **lesen** als auch **schreiben**. Damit können Sie zum Beispiel:

- **Daten abfragen**: "Welche Projekte haben eine Deadline in den nächsten 7 Tagen?"
- **Auswertungen erstellen**: "Wie verteilen sich die Supporttickets nach Kategorie?"
- **Einträge anlegen**: "Erstelle einen neuen Kontakt mit dem Namen Müller GmbH."
- **Daten ändern**: "Setze den Status aller erledigten Aufgaben auf 'Archiviert'."

## Unterstützte KI-Modelle

Bei SeaTable Cloud nutzt das Plugin standardmäßig die bereits installierte **SeaTable AI**. Dahinter verbirgt sich **Qwen 3.8 27B**, ein Open-Weights-Modell mit 27 Milliarden Parametern aus dem Hause Alibaba. Das KI-Modell wird in deutschen Rechenzentren von Exoscale gehostet – demselben Anbieter, der auch die Server von SeaTable Cloud bereitstellt. Es ist auf anspruchsvolles logisches Denken, Programmierung, Recherche, Dokumentenverarbeitung sowie komplexe mehrstufige Aufgaben ausgelegt und steht unter der Apache-2.0-Lizenz.

Darüber hinaus können Sie für das KI-Chat-Plugin Ihren eigenen **API-Schlüssel** mitbringen, um ein **externes Cloud-KI-Modell** anzubinden. Hierbei können Sie zwischen folgenden Anbietern und Modellen wählen:

| Anbieter | Modelle |
|---|---|
| **Anthropic (Claude)** | Haiku, Sonnet |
| **OpenAI** | GPT-6.1 Sol, GPT-6 Luna |
| **Mistral** | Large, Small |

## Drei KI-Funktionen in SeaTable

SeaTable bietet drei verschiedene KI-Funktionen, die sich in ihrer Arbeitsweise grundlegend unterscheiden:

| | KI-Automationen | KI-Agenten | KI-Chat-Plugin |
|---|---|---|---|
| **Verfügbar seit** | Version 6.0 | Version 6.0 | Version 6.1 |
| **Auslöser** | Automatisch (Regel/Ereignis) | Manuell (Ihre Frage) | Manuell (Ihre Frage) |
| **Interaktion** | Keine, läuft im Hintergrund | Dialog im externen KI-Tool | Dialog direkt in SeaTable |
| **Typischer Einsatz** | Kategorisieren, Zusammenfassen, Extrahieren | Ad-hoc-Analysen, komplexe Aufgaben | Schnelle Fragen, Daten bearbeiten |
| **KI-Modell** | SeaTable AI-Server (EU) | Externer Anbieter | SeaTable AI-Server (EU) *oder* externer Anbieter (eigener API-Key) |
| **Externe Software nötig?** | Nein | Ja (z. B. Claude Desktop, Cursor) | Nein |

[KI-Automationen]({{< relref "help/ai/ai-automations/introduction" >}}) eignen sich für wiederkehrende Aufgaben, die regelbasiert im Hintergrund ablaufen sollen. [KI-Agenten]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}) bieten maximale Flexibilität über externe MCP-Clients. Das **KI-Chat-Plugin** schließt die Lücke dazwischen: interaktive KI-Nutzung ohne externe Software – direkt dort, wo Ihre Daten liegen.
