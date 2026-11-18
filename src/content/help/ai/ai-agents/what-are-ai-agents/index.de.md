---
title: 'Was sind KI-Agenten?'
description: 'KI-Agenten greifen per MCP direkt auf Ihre SeaTable-Daten zu. Erfahren Sie, wie das funktioniert und was Sie damit machen können.'
weight: 1
url: '/de/hilfe/was-sind-ki-agenten'
seo:
    title: 'Was sind KI-Agenten und wie funktionieren sie mit SeaTable?'
    description: 'KI-Agenten verbinden sich per MCP Server direkt mit Ihren SeaTable-Daten. Lesen, schreiben und analysieren Sie Ihre Daten in natürlicher Sprache — ohne Programmierkenntnisse.'
---

KI-Assistenten wie Claude, ChatGPT oder Copilot sind leistungsfähige Werkzeuge — aber sie haben ein grundlegendes Problem: Sie kennen Ihre Daten nicht. Wenn Sie eine Frage zu Ihren Projekten, Kunden oder Lagerbeständen stellen wollen, müssen Sie die Daten erst exportieren, in den Chat einfügen und der KI erklären, was die Spalten bedeuten. Das ist umständlich und fehleranfällig.

**KI-Agenten lösen genau dieses Problem.** Ein KI-Agent ist ein KI-Assistent, der über eine standardisierte Schnittstelle direkt auf Ihre Daten zugreifen kann. Bei SeaTable geschieht das über das **Model Context Protocol (MCP)** — einen offenen Standard, der von der gesamten KI-Branche unterstützt wird.

## Das Wichtigste in Kürze

- Der **offizielle SeaTable MCP Server** (`https://mcp.seatable.com/mcp`) verbindet ChatGPT, Claude Desktop, Claude Code, Cursor und andere MCP-fähige Assistenten mit Ihrer Base.
- Der Zugriff gilt pro Base, nur lesend oder lesend und schreibend, je nach Token.
- Der Agent bearbeitet Daten, nicht die Struktur: Tabellen und Spalten legt er nicht an und löscht er nicht.
- Kostenlos und Open Source (MIT-Lizenz), für SeaTable Cloud und selbst gehostete Installationen.

## Wie funktioniert das?

Wenn Sie einen KI-Agenten mit Ihrer SeaTable-Base verbinden, passiert Folgendes:

1. Sie stellen eine Frage in natürlicher Sprache, zum Beispiel: *"Welche Aufgaben sind überfällig?"*
2. Der KI-Agent erkennt, dass er dafür Daten aus Ihrer Base braucht, und fragt diese über den MCP Server ab.
3. Der MCP Server liest die relevanten Zeilen aus SeaTable und gibt sie an den Agenten zurück.
4. Der Agent wertet die Daten aus und antwortet Ihnen — verständlich und auf den Punkt.

Das alles dauert wenige Sekunden. Sie merken davon nichts, außer dass Sie eine präzise Antwort bekommen.

## Was kann ein KI-Agent mit meinen Daten machen?

Das hängt davon ab, welche Berechtigungen Sie vergeben. Mit einem **Lese-Token** kann der Agent Ihre Daten abfragen, durchsuchen und analysieren. Mit einem **Lese-/Schreib-Token** kann er zusätzlich Einträge anlegen, ändern oder löschen — allerdings nur nach Ihrer Bestätigung.

Konkret bedeutet das:

- **Abfragen**: "Zeig mir alle Kunden aus Berlin mit einem Umsatz über 5.000 Euro."
- **Auswerten**: "Wie viele Aufgaben sind diese Woche abgeschlossen worden? Gruppiere nach Mitarbeiter."
- **Anlegen**: "Erstelle einen neuen Eintrag in der Kontakte-Tabelle für Firma Müller GmbH."
- **Ändern**: "Setze den Status aller überfälligen Aufgaben auf 'Eskaliert'."
- **Verknüpfen**: "Verknüpfe den neuen Kontakt mit dem Projekt 'Website-Relaunch'."

Der Agent erkennt dabei automatisch die Struktur Ihrer Base, Tabellen, Spalten, Spaltentypen und verwendet die richtigen Formate. Auch Tippfehler in Tabellen- oder Spaltennamen korrigiert er in den meisten Fällen selbstständig.

{{< youtube 5T4pWJgfOgc >}}

## Was unterscheidet KI-Agenten von KI-Automationen?

SeaTable bietet auch **KI-Automationen** — automatisierte Aktionen, die bei bestimmten Ereignissen eine KI einbinden, zum Beispiel um Texte zusammenzufassen oder Einträge zu kategorisieren. Diese laufen regelbasiert im Hintergrund, ohne dass Sie eingreifen.

KI-Agenten funktionieren anders: Sie arbeiten **interaktiv**. Sie stellen eine Frage, der Agent antwortet. Sie geben eine Anweisung, der Agent führt sie aus. Es ist ein Dialog — so wie mit einem Kollegen, der Ihre Datenbank in- und auswendig kennt.

| | KI-Automationen | KI-Agenten |
|---|---|---|
| **Auslöser** | Automatisch (Regel/Ereignis) | Manuell (Ihre Frage) |
| **Interaktion** | Keine — läuft im Hintergrund | Dialog in natürlicher Sprache |
| **Typischer Einsatz** | Texte zusammenfassen, kategorisieren | Daten abfragen, analysieren, bearbeiten |
| **Einrichtung** | In SeaTable konfiguriert | Über externen KI-Assistenten (z.B. Claude) |

Beide Ansätze ergänzen sich: Automationen für wiederkehrende Routineaufgaben, Agenten für ad-hoc-Fragen und flexible Interaktion.

## Was brauche ich, um loszulegen?

- Einen **SeaTable Cloud Account** (oder eine selbst gehostete Installation)
- Einen **KI-Assistenten**, der MCP unterstützt — zum Beispiel ChatGPT, Claude Desktop, Claude Code oder Cursor
- Einen **API-Token** für die Base, auf die der Agent zugreifen soll

Die Einrichtung dauert wenige Minuten. Schritt-für-Schritt-Anleitungen gibt es für [ChatGPT]({{< relref "help/ai/ai-agents/connect-chatgpt" >}}), [Claude Desktop]({{< relref "help/ai/ai-agents/connect-claude-desktop" >}}), [Claude Code]({{< relref "help/ai/ai-agents/connect-claude-code" >}}) und [Cursor]({{< relref "help/ai/ai-agents/connect-cursor" >}}).

## Ist das sicher?

Der KI-Agent greift ausschließlich auf die Base zu, für die Sie einen API-Token erstellt haben. Nicht auf andere Bases, nicht auf Ihren Account. Über den Token steuern Sie, ob der Agent nur lesen oder auch schreiben darf.

Wichtig zu wissen: Wenn der Agent Ihre Daten abfragt, werden die Ergebnisse an den KI-Anbieter übertragen (zum Beispiel Anthropic bei Claude), damit das Sprachmodell sie verarbeiten kann. Die großen Anbieter verpflichten sich, API-Daten nicht zum Modelltraining zu verwenden. Wer maximale Kontrolle braucht, kann SeaTable selbst hosten und mit einem lokalen Sprachmodell kombinieren.

Mehr zum Thema Sicherheit und Berechtigungen finden Sie im Artikel "Berechtigungen und Datenschutz bei KI-Agenten".