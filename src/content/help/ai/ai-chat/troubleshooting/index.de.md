---
title: 'Fehlerbehebung'
description: 'Lösungen für häufige Probleme mit dem KI-Chat-Plugin in SeaTable.'
weight: 6
url: '/de/hilfe/ki-chat-plugin-fehlerbehebung'
seo:
    title: 'KI-Chat-Plugin: Fehlerbehebung und häufige Probleme'
    description: 'Lösungen für häufige Probleme mit dem KI-Chat-Plugin: API-Key-Fehler, fehlende Antworten und Plugin-Probleme.'
---

Wenn das KI-Chat-Plugin nicht wie erwartet funktioniert, finden Sie hier Lösungen für die häufigsten Probleme. Allgemeine Informationen zur Einrichtung finden Sie im Artikel [KI-Chat-Plugin einrichten]({{< relref "help/ai/ai-chat/setup" >}}).

## API-Key-Probleme

### Ungültiger API-Key

Wenn die Fehlermeldung auf einen ungültigen API-Key hinweist, prüfen Sie Folgendes:

- Stellen Sie sicher, dass der Key korrekt eingegeben wurde und keine versehentlichen Leerzeichen enthält.
- Überprüfen Sie, ob der API-Key noch aktiv ist. Einige Anbieter deaktivieren Keys nach einer bestimmten Inaktivitätsdauer.
- Vergewissern Sie sich, dass der gewählte **Provider** in den Plugin-Einstellungen zum API-Key passt. Ein OpenAI-Key funktioniert beispielsweise nicht mit dem Anbieter Anthropic.

### Guthaben oder Kontingent aufgebraucht

Die meisten KI-Anbieter arbeiten mit einem Prepaid-Guthaben. Wenn keine Antworten mehr generiert werden, prüfen Sie Ihr Guthaben im Dashboard des jeweiligen Anbieters:

- [Anthropic Console](https://console.anthropic.com/)
- [OpenAI Platform](https://platform.openai.com/)
- [Mistral Console](https://console.mistral.ai/)

## Keine oder falsche Antworten

### Die KI findet die Daten nicht

Stellen Sie sicher, dass die angefragten Daten tatsächlich in der Base vorhanden sind. Nennen Sie in Ihrer Frage den genauen Tabellen- und Spaltennamen, damit die KI die richtigen Daten identifizieren kann.

### Ungenaue oder fehlerhafte Ergebnisse

Formulieren Sie Ihre Frage möglichst präzise. Vermeiden Sie vage Formulierungen und geben Sie konkret an, welche Tabelle und welche Spalten relevant sind. Bei komplexen Aufgaben kann es helfen, die Anfrage in mehrere einfache Schritte aufzuteilen.

### Zeitüberschreitung oder keine Antwort

Sehr umfangreiche Abfragen können zu einer Zeitüberschreitung führen. Vereinfachen Sie die Anfrage oder beschränken Sie sich auf eine einzelne Tabelle. Beachten Sie auch, dass kleinere Modelle wie Haiku, GPT-4o mini oder Mistral Small bei komplexen, mehrstufigen Aufgaben an ihre Grenzen stoßen können.

## Plugin-Probleme

### Das Plugin wird nicht angezeigt

Prüfen Sie, ob das Plugin im Plugin-Manager installiert und aktiviert ist. Öffnen Sie dazu im Base-Header den Bereich **Plugins** und suchen Sie nach **AI Chat**.

### Das Plugin lädt nicht

Laden Sie die Seite im Browser neu. Falls das Problem weiterhin besteht, versuchen Sie es in einem anderen Browser oder leeren Sie den Browser-Cache.

### Einstellungen werden nicht gespeichert

Achten Sie darauf, dass Sie nach der Eingabe des API-Keys die Einstellungen mit **Save** bestätigt haben. Ohne Speichern gehen die Eingaben beim Schließen des Einstellungsdialogs verloren.

## Allgemeine Tipps

- Starten Sie mit einer einfachen Frage wie "Welche Tabellen gibt es?", um die Verbindung zum KI-Anbieter zu überprüfen.
- Wenn die KI unerwartete Ergebnisse liefert, bitten Sie sie, ihren Lösungsweg zu erklären.
- Teilen Sie komplexe Aufgaben in mehrere kleine Schritte auf, um bessere Ergebnisse zu erzielen.
