---
title: 'Beispiele und Tipps'
description: 'Praktische Beispiele und Tipps für den effektiven Einsatz des KI-Chat-Plugins in SeaTable.'
weight: 4
url: '/de/hilfe/ki-chat-plugin-beispiele-und-tipps'
seo:
    title: 'KI-Chat-Plugin: Beispiele und Tipps für gute Fragen'
    description: 'Lernen Sie anhand konkreter Beispiele, wie Sie das KI-Chat-Plugin in SeaTable optimal nutzen: Daten abfragen, analysieren und bearbeiten.'
---

Das KI-Chat-Plugin versteht natürliche Sprache und arbeitet direkt mit den Daten in Ihrer Base. In diesem Artikel finden Sie konkrete Beispiele für typische Anwendungsfälle sowie Tipps, mit denen Sie bessere Ergebnisse erzielen. Allgemeine Hinweise zur Formulierung guter Fragen finden Sie auch im Artikel [Wie Sie gute Fragen stellen]({{< relref "help/ai/ai-agents/good-questions" >}}).

## Daten abfragen

Der häufigste Einsatzzweck: Sie stellen eine Frage und der Chat liefert die passenden Einträge aus Ihrer Base.

> *"Zeige mir alle offenen Aufgaben, die diese Woche fällig sind."*

> *"Wie viele Kunden haben wir aus Deutschland?"*

> *"Welche Rechnungen sind noch nicht bezahlt?"*

> *"Gibt es Projekte ohne zugewiesenen Verantwortlichen?"*

Je genauer Sie Tabellen- und Spaltennamen nennen, desto präziser fällt die Antwort aus. Wenn Sie unsicher sind, welche Spalten existieren, fragen Sie einfach:

> *"Beschreibe die Struktur meiner Base."*

## Daten analysieren

Der Chat kann Ihre Daten nicht nur anzeigen, sondern auch auswerten, gruppieren und zusammenfassen.

> *"Was war der Gesamtumsatz im letzten Quartal, aufgeschlüsselt nach Vertriebsmitarbeiter?"*

> *"Fasse die Support-Anfragen der letzten Woche zusammen."*

> *"Welche Produkte wurden am häufigsten bestellt?"*

> *"Wie verteilen sich die offenen Tickets nach Priorität?"*

Solche Analysen funktionieren besonders gut, wenn Ihre Base sauber gepflegte Daten enthält. Bei fehlenden oder inkonsistenten Werten weist der Chat in der Regel darauf hin.

## Daten erstellen und bearbeiten

Das KI-Chat-Plugin kann auch Einträge anlegen, ändern, verknüpfen und löschen. Formulieren Sie dabei möglichst eindeutig, welche Tabelle, welche Spalten und welche Werte betroffen sind.

### Neue Einträge erstellen

> *"Erstelle einen neuen Kontakt: Name 'Müller GmbH', Stadt 'Hamburg', Status 'Interessent'."*

> *"Erstelle für jeden offenen Deal einen Follow-up-Eintrag in der Tabelle Aktivitäten."*

### Bestehende Einträge ändern

> *"Setze den Status aller überfälligen Aufgaben auf 'Eskaliert'."*

> *"Ändere die Priorität des Tickets #412 auf 'Hoch'."*

### Einträge verknüpfen und löschen

> *"Verknüpfe alle Rechnungen mit dem zugehörigen Kunden aus der Tabelle Kontakte."*

> *"Lösche alle Testeinträge aus der Tabelle Entwürfe."*

Beim Löschen fragt der Chat vor der Ausführung zur Sicherheit nach. Prüfen Sie trotzdem vorher mit einer Lesefrage, ob die richtigen Einträge betroffen sind.

## Tipps für bessere Ergebnisse

**Starten Sie mit Lesefragen.** Bevor Sie Daten ändern lassen, prüfen Sie zuerst, ob der Chat die richtigen Einträge findet. Fragen Sie also erst *"Welche Aufgaben sind überfällig?"*, bevor Sie sagen *"Setze den Status auf Eskaliert."*

**Teilen Sie komplexe Aufgaben auf.** Bei mehrstufigen Anfragen kommen Sie schneller ans Ziel, wenn Sie Schritt für Schritt vorgehen. Der Chat merkt sich den Kontext des Gesprächs und Sie können auf vorherige Antworten aufbauen.

**Verwenden Sie Tabellen- und Spaltennamen.** Die exakte Schreibweise ist nicht nötig, aber die richtigen Begriffe helfen dem Chat, Ihre Frage korrekt zu interpretieren.

**Nutzen Sie den Kontext.** Nach einer Abfrage können Sie mit "diese", "davon" oder "die gleichen" auf vorherige Ergebnisse verweisen, ohne alles zu wiederholen.

## Was nicht funktioniert

Das KI-Chat-Plugin arbeitet ausschließlich mit den Daten in Ihrer SeaTable-Base. Folgende Dinge sind nicht möglich:

- **Nicht vorhandene Daten abfragen.** Wenn eine Spalte oder Tabelle nicht existiert, kann der Chat keine Antwort liefern. Er erfindet keine Daten.
- **Aktionen außerhalb von SeaTable.** Der Chat kann keine E-Mails versenden, keine externen Systeme ansprechen und keine Dateien öffnen.
- **Sehr große Massenoperationen.** Einzelne Anfragen, die hunderte Einträge gleichzeitig erstellen oder ändern sollen, können an Grenzen stoßen. Teilen Sie solche Aufgaben in kleinere Schritte auf.
