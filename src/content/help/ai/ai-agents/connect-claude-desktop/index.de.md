---
title: 'SeaTable mit Claude Desktop verbinden'
description: 'Verbinden Sie Claude Desktop über den MCP Server mit Ihrer SeaTable-Base — Schritt für Schritt erklärt.'
weight: 2
url: '/de/hilfe/ki-agent-mit-claude-desktop-verbinden'
seo:
    title: 'SeaTable mit Claude Desktop verbinden — Einrichtung in 5 Minuten'
    description: 'So verbinden Sie Claude Desktop per MCP Server mit Ihrer SeaTable-Base: API-Token erstellen, Konfiguration einfügen und die erste Frage stellen.'
---

In dieser Anleitung verbinden Sie Claude Desktop mit Ihrer SeaTable-Base. Nach der Einrichtung können Sie Claude Fragen zu Ihren Daten stellen und Einträge direkt aus dem Chat heraus bearbeiten lassen. Die Einrichtung dauert etwa fünf Minuten.

## Voraussetzungen

- Ein SeaTable Cloud Account mit mindestens einer Base
- Claude Desktop (kostenlos verfügbar unter [claude.ai/download](https://claude.ai/download/))
- Ein Anthropic-Konto (für die Nutzung von Claude)

{{< warning headline="Das Free Abo reicht, erfordert aber eine spezielle Konfiguration" >}}

Das kostenlose Free-Konto von Anthropic unterstützt aktuell zwar Verbindungen zu eigenen MCP Servern, diese müssen aber etwas umständlich über eine Konfigurationsdateien konfiguriert werden.

{{< /warning >}}

## Schritt 1: API-Token in SeaTable erstellen

Der API-Token gibt Claude Zugriff auf eine bestimmte Base. Sie entscheiden dabei, ob Claude nur lesen oder auch schreiben darf.
Wie Sie einen API-Token erstellen, erfahren Sie im Artikel [Erzeugen eines API-Tokens]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}). 

{{< warning headline="Token sicher aufbewahren" >}}

Ein API-Token ist unlimitiert gültig und ist wie ein Passwort zu behandeln. Falls Sie ihn verlieren oder er versehentlich veröffentlich wird, können Sie den API-Token jederzeit entfernen und einen neuen Token erstellen.

{{< /warning >}}

## Schritt 2: Claude Desktop konfigurieren

Claude Desktop verwendet eine JSON-Konfigurationsdatei, um MCP Server einzubinden. 

1. Öffnen Sie Claude Desktop.
2. Gehen Sie zu **Settings** → **Developer**

![Anlegen eines eigenen MCP Servers in Claude Desktop](images/claude-add-custom-mcp.png)

3. Die Datei `claude_desktop_config.json` öffnet sich in Ihrem Texteditor.
4. Fügen Sie folgende Konfiguration ein:

```json
{
  "mcpServers": {
    "seatable": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": [
        "C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx-cli.js",
        "mcp-remote",
        "https://mcp.seatable.com/mcp",
        "--header",
        "Authorization: Bearer HIER-IHREN-API-TOKEN-EINFUEGEN"
      ]
    }
  }
}
```

5. Ersetzen Sie `HIER-IHREN-API-TOKEN-EINFUEGEN` durch den Token aus Schritt 1.
6. Speichern Sie die Datei und starten Sie Claude Desktop neu.

Sie können mehrere Bases gleichzeitig anbinden. Erstellen Sie für jede Base einen eigenen Eintrag unter `mcpServers` mit einem eindeutigen Namen, zum Beispiel `seatable-crm` und `seatable-projekte`.

## Schritt 3: Verbindung prüfen

Nach dem Neustart sehen Sie in Claude Desktop unter `Tools` die Verbindung zu **SeaTable**. Das zeigt an, dass der MCP Server verbunden ist. Klicken Sie darauf, um die verfügbaren Tools zu sehen — Sie sollten SeaTable-Werkzeuge wie `list_tables`, `list_rows` oder `query_sql` finden. 

Alternativ können Sie den Status der Verbindung in den Einstellungen einsehen.

![Status der Verbindung zum MCP Server](images/claude-mcp-connected.png)

Stellen Sie nun eine erste Testfrage:

> *"Welche Tabellen gibt es in meiner Base?"*

Claude fragt daraufhin über den MCP Server die Tabellenstruktur ab und listet Ihnen alle Tabellen mit ihren Spalten auf. Wenn das funktioniert, ist die Verbindung hergestellt.

## Erste Fragen stellen

Sie können Claude jetzt Fragen zu Ihren Daten stellen, als würden Sie mit einem Kollegen sprechen. Ein paar Beispiele zum Ausprobieren:

- *"Wie viele Einträge hat die Tabelle Kontakte?"*
- *"Zeig mir alle Einträge, bei denen der Status auf 'Offen' steht."*
- *"Fasse die Daten in der Tabelle Umsätze nach Monat zusammen."*

Ihre Fragen sollten sich auf Tabellen und Spalten beziehen, die tatsächlich in Ihrer Base existieren. Wenn Sie unsicher sind, fragen Sie Claude einfach zuerst nach der Struktur der Base. Er kennt Ihre Tabellen und Spalten und kann Sie darauf hinweisen, was verfügbar ist.

Sie müssen Tabellen- und Spaltennamen nicht exakt schreiben. Claude erkennt kleine Tippfehler und korrigiert sie automatisch. Schreiben Sie ruhig "Kontakte" statt "kontakte" oder "Projekte" statt "Projects". Claude findet die richtige Tabelle.

## Nächste Schritte

- [Anwendungsbeispiele für KI-Agenten]({{< relref "help/ai/ai-agents/use-cases" >}})
- [Gute Fragen stellen: So bekommen Sie die besten Antworten]({{< relref "help/ai/ai-agents/good-questions" >}})
- [Fehlerbehebung bei KI-Agenten]({{< relref "help/ai/ai-agents/troubleshooting" >}})
- [Berechtigungen und Datenschutz bei KI-Agenten]({{< relref "help/ai/ai-agents/data-security" >}})