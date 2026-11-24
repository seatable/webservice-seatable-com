---
title: 'Unterstützte KI-Modelle'
description: 'Das KI-Chat-Plugin unterstützt Modelle von Anthropic, OpenAI und Mistral. Erfahren Sie, welches Modell für welchen Einsatzzweck geeignet ist.'
weight: 3
url: '/de/hilfe/ki-chat-plugin-unterstuetzte-modelle'
seo:
    title: 'Unterstützte KI-Modelle im SeaTable Chat-Plugin'
    description: 'Übersicht der unterstützten KI-Modelle im SeaTable Chat-Plugin: Claude, GPT, Mistral. Vergleich, Empfehlungen und Kosten.'
---

Das KI-Chat-Plugin nutzt standardmäßig die bereits installierte **SeaTable AI**. Zudem unterstützt es Sprachmodelle von drei externen Anbietern: **Anthropic**, **OpenAI** und **Mistral**. Sie wählen selbst, welches Modell Sie nutzen möchten. Die anfallenden Token-Kosten werden entweder direkt mit Ihrem SeaTable-Abonnement verrechnet oder Sie zahlen an den jeweiligen externen Anbieter Ihres Modells.

## SeaTable AI

Hinter der vorinstallierten SeaTable AI verbirgt sich **Qwen 3.8 27B**, ein Open-Weights-Modell mit 27 Milliarden Parametern aus dem Hause Alibaba. Das KI-Modell wird in deutschen Rechenzentren von Exoscale gehostet – demselben Anbieter, der auch die Server von SeaTable Cloud bereitstellt. Es ist auf anspruchsvolles logisches Denken, Programmierung, Recherche, Dokumentenverarbeitung sowie komplexe mehrstufige Aufgaben ausgelegt und steht unter der Apache-2.0-Lizenz.

Darüber hinaus können Sie für das KI-Chat-Plugin Ihren eigenen **API-Schlüssel** mitbringen, um ein **externes Cloud-KI-Modell** anzubinden.

## Modellübersicht der externen Anbieter

Jeder Anbieter stellt zwei Modelle bereit: ein schnelles, günstiges Modell für einfache Aufgaben und ein leistungsstärkeres Modell für anspruchsvolle Analysen.

| Anbieter | Modell | Stärken | Kostentendenz |
|---|---|---|---|
| **Anthropic** | Claude Haiku | schnell, effizient, gut für einfache Abfragen | günstig |
| **Anthropic** | Claude Sonnet | leistungsstark, präzise bei komplexen Analysen | mittel |
| **OpenAI** | GPT-6 Luna | schnell, kosteneffizient, vielseitig einsetzbar | günstig |
| **OpenAI** | GPT-6.1 Sol | sehr leistungsfähig, hohe Antwortqualität | höher |
| **Mistral** | Mistral Small | schnell, günstig, gute Basisleistung | günstig |
| **Mistral** | Mistral Large | leistungsstark, gut für komplexe Aufgaben | höher |

## API-Schlüssel einrichten

Um ein externes Modell im KI-Chat-Plugin nutzen zu können, benötigen Sie einen **API-Schlüssel** des jeweiligen Anbieters. Diesen erstellen Sie direkt auf der Website des Anbieters:

- **Anthropic**: Erstellen Sie einen API-Schlüssel unter [console.anthropic.com](https://console.anthropic.com/).
- **OpenAI**: Erstellen Sie einen API-Schlüssel unter [platform.openai.com](https://platform.openai.com/).
- **Mistral**: Erstellen Sie einen API-Schlüssel unter [v2.auth.mistral.ai/login](https://v2.auth.mistral.ai/login).

Bei allen drei Anbietern müssen Sie ein **Zahlungsmittel** hinterlegen. Die Kosten richten sich nach der Anzahl der verbrauchten Tokens und werden direkt vom Anbieter abgerechnet.

## Empfehlungen nach Einsatzzweck

### Einfache Abfragen und schnelle Antworten

Für das Nachschlagen einzelner Werte, kurze Zusammenfassungen oder einfache Filterfragen eignen sich die günstigen Modelle: **Claude Haiku**, **GPT-6 Luna** oder **Mistral Small**. Diese liefern schnelle Antworten bei niedrigen Kosten.

### Komplexe Analysen und Datenauswertungen

Wenn Sie umfangreiche Datensätze auswerten, Muster erkennen oder mehrstufige Berechnungen durchführen möchten, greifen Sie zu **Claude Sonnet**, **GPT-6.1 Sol** oder **Mistral Large**. Diese Modelle liefern präzisere Ergebnisse bei anspruchsvollen Aufgaben.

### Texterstellung und Schreibaufgaben

Für das Verfassen von E-Mails, Berichten oder Beschreibungen auf Basis Ihrer Daten empfehlen sich **Claude Sonnet** oder **GPT-6.1**. Beide Modelle erzeugen sprachlich hochwertige Texte.

## Kosten und Abrechnung

### Bei SeaTable AI

Die von der KI verbrauchten Tokens werden in **KI-Credits** umgerechnet und von Ihrem Guthaben abgezogen: 1 Million Input-Tokens entsprechen 500 KI-Credits, 1 Million Output-Tokens 1.500 KI-Credits. 

Je nach [SeaTable-Abonnement]({{< relref "pages/prices" >}}) Ihres Teams haben Sie unterschiedlich viele KI-Credits zur Verfügung. Bei SeaTable Plus sind es monatlich **50 KI-Credits pro Benutzer** und bei SeaTable Enterprise **500 KI-Credits pro Benutzer**. 

Wie viel von Ihrem Guthaben noch übrig ist und wie viel Sie verbraucht haben, können Sie jederzeit an dem **Balken in der linken Seitenleiste** des KI-Chat-Plugins ablesen.

![Verbrauchte und übrige KI-Credits bei SeaTable AI](images/seatable-ai-credits.png)

### Bei externen KI-Modellen

Alle Token-Kosten werden direkt zwischen Ihnen und dem jeweiligen KI-Anbieter abgerechnet. SeaTable erhebt keine zusätzlichen Gebühren für die Nutzung des KI-Chat-Plugins. Die genauen Preise pro Token finden Sie auf der Preisseite des jeweiligen Anbieters.
