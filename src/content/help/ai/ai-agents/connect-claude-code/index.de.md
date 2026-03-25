---
title: 'SeaTable mit Claude Code verbinden'
description: 'Verbinden Sie Claude Code über den MCP Server mit Ihrer SeaTable-Base — Schritt für Schritt erklärt.'
weight: 3
url: '/de/hilfe/ki-agent-mit-claude-code-verbinden'
seo:
    title: 'SeaTable mit Claude Code verbinden — Einrichtung in 5 Minuten'
    description: 'So verbinden Sie Claude Code per MCP Server mit Ihrer SeaTable-Base: API-Token erstellen, MCP Server per CLI hinzufügen und die erste Frage stellen.'
---

In dieser Anleitung verbinden Sie Claude Code mit Ihrer SeaTable-Base. Nach der Einrichtung können Sie Claude Fragen zu Ihren Daten stellen und Einträge direkt aus dem Terminal heraus bearbeiten lassen. Die Einrichtung dauert etwa fünf Minuten.

## Voraussetzungen

- Ein SeaTable Cloud Account mit mindestens einer Base
- Claude Code (installierbar über `npm install -g @anthropic-ai/claude-code`, Details unter [code.claude.com](https://code.claude.com/docs/en/overview))
- Ein Anthropic-Konto (für die Nutzung von Claude)

## Schritt 1: API-Token in SeaTable erstellen

Der API-Token gibt Claude Zugriff auf eine bestimmte Base. Sie entscheiden dabei, ob Claude nur lesen oder auch schreiben darf.
Wie Sie einen API-Token erstellen, erfahren Sie im Artikel [Erzeugen eines API-Tokens]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}).

{{< warning headline="Token sicher aufbewahren" >}}

Ein API-Token ist unlimitiert gültig und ist wie ein Passwort zu behandeln. Falls Sie ihn verlieren oder er versehentlich veröffentlich wird, können Sie den API-Token jederzeit entfernen und einen neuen Token erstellen.

{{< /warning >}}

## Schritt 2: MCP Server per CLI hinzufügen

Claude Code wird über die Kommandozeile konfiguriert. Öffnen Sie ein Terminal und führen Sie folgenden Befehl aus:

```bash
claude mcp add seatable \
  --transport http \
  https://mcp.seatable.com/mcp \
  -H "Authorization: Bearer HIER-IHREN-API-TOKEN-EINFUEGEN"
```

Ersetzen Sie `HIER-IHREN-API-TOKEN-EINFUEGEN` durch den Token aus Schritt 1.

Sie können mehrere Bases gleichzeitig anbinden. Führen Sie den Befehl für jede Base erneut aus und verwenden Sie dabei einen eindeutigen Namen, zum Beispiel `seatable-crm` und `seatable-projekte` anstelle von `seatable`.

## Schritt 3: Verbindung prüfen

Starten Sie Claude Code und geben Sie den Befehl `/mcp` ein. Daraufhin werden alle konfigurierten MCP Server mit ihrem Status angezeigt. Bei einer erfolgreichen Verbindung sehen Sie **Status: connected** und **Auth: authenticated**.

![Erfolgreiche Verbindung zum SeaTable MCP Server in Claude Code](images/claude-code-connected-to-mcp-seatable-com.png)

Über das `/mcp`-Menü können Sie auch weitere Aktionen ausführen, z. B. die verfügbaren Tools einsehen, die Verbindung neu herstellen (**Reconnect**) oder den Server deaktivieren.

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
