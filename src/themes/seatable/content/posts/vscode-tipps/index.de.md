---
title: 'VS Code Tipps'
description: 'Tipps und Tricks für den VS Code Profi'
draft: true
date: 2026-11-22
url: '/de/vscode-tipps'
color: '#085b79'
register:
    show: true
---

## Sprache deaktivieren

In der Datei `src/config/development/hugo.toml` könnt ihr einzelne Sprachen deaktivieren. Diese müssen dann nicht mehr gerendert werden und erscheinen nicht mehr in eurer lokalen Entwicklungsumgebung.

```
disableLanguages = ["ru", "pt", "fr", "es"]
```

Jede Sprache, die Ihr nicht benötigt, beschleunigt eure Arbeit. Deutsch und Englisch können nicht nicht deaktivieren werden.

## Container über das Terminal starten

Mit dem Befehl `docker compose up` kann der Hugo Docker Container schnell und einfach gestartet werden. Dies hat den Vorteil, dass man unmittelbar die Log-Meldungen sieht.

![Starten des Docker Containers über das Terminal in VS Code](images/terminal.png)

Diese Darstellung bedeutet, dass Hugo bereit ist und über den Browser [http://localhost:1313](http://localhost:1313) erreichbar ist:

```
hugo  | [0]                    | EN  | DE
hugo  | [0] -------------------+-----+------
hugo  | [0]   Pages            | 836 | 832
hugo  | [0]   Paginator pages  |   0 |   0
hugo  | [0]   Non-page files   |   0 |   0
hugo  | [0]   Static files     | 197 | 197
hugo  | [0]   Processed images | 701 |   0
hugo  | [0]   Aliases          |   5 |   1
hugo  | [0]   Cleaned          |   0 |   0
hugo  | [0]
hugo  | [0] Built in 2522 ms
hugo  | [0] Environment: "development"
hugo  | [0] Serving pages from disk
hugo  | [0] Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
hugo  | [0] Web Server is available at http://localhost:1313/ (bind address 0.0.0.0)
hugo  | [0] Press Ctrl+C to stop
```

Mit {{< key "STRG" >}} + {{< key "C" >}} kann der Docker Container wieder gestoppt werden.

## Neuesten Main Branch holen

Das Abrufen der neuesten Inhalte für den `main` Branch kann bei umfangreichen Änderungen zu lange dauern und dann in einen Fehler laufen.
Deshalb empfiehlt es sich anstelle auf den runden Pfeil zu klicken, den Pull über das Terminal anzustoßen.

Man wechselt also in den `main` Branch und tippt dann in das Terminal:

```
git pull
```

## Höfliche Ansprache bei der automatischen Übersetzung

Die deepl-Erweiterung bietet die Möglichkeit die Art der Ansprache festzulegen. Auf seatable.com verwenden wir das höfliche Sie, weshalb Ihr in den Einstellungen dieser Erweiterung den folgenden Wert setzen solltet:

![Höfliche Ansprache beim Übersetzen mit deepl erzwingen](images/deepl-ansprache.png)

So kommt Ihr zu der gewünschten Einstellung:

- Wechselt in der linken Leiste auf die VS-Code Erweiterungen - alternativ drückt Ihr {{< key "STRG" >}} + {{< key "UMSCHALTTASTE" >}} + {{< key "X" >}}.
- Sucht die installierte Erweiterung **Translate with DeepL for Visual Studio Code**
- Klickt auf das Zahnrad und dann auf **Einstellungen**
- Ändert den Wert für `Deepl: Formality`

## Öffnen von Dateien

Die Navigation im Verzeichnisbaum bzw. die Suche nach Dateien kann ganz schön nervig sein. Schneller geht es mit {{< key "STRG" >}} + {{< key "C" >}} und der Eingabe des Dateinamens.
Dann wählt man die Datei mit den Pfeiltasten aus und bestätigt mit {{< key "ENTER" >}}.

![Öffnen des Quick-Guides in wenigen Sekunden](images/dateien-oeffnen.png)

## Tabs nebeneinander stellen

Per Drag-and-Drop lassen sich mehrere Tabs in VS Code nebeneinanderstellen.

![Mehrer Tabs nebeneinander](images/tabs.png)

## Mehrere Cursors setzen

Mit gedrückter {{< key "ALT" >}} Taste können mehrere Cursor in einem Dokument gesetzt werden. Alle Vorkommnisse eines Wortes können durch das Markieren und anschließendes Drücken von {{< key "STRG" >}} + {{< key "D" >}} ausgewählt werden. Jedes {{< key "STRG" >}} + {{< key "D" >}} setzt einen zusätzlichen Cursor und markiert das zusätzliche Wort.

## Suchen und Ersetzen

Die **Suchen und Ersetzen** Funktion von VS Code bietet eine leistungsstarke Möglichkeit Änderungen über viele Dateien hinweg durchzuführen. Folgende Dinge sollten dabei beachtet werden:

- Idealerweise legt man vor jeder umfangreichen **Suchen und Ersetzen** Aktionen einen **Commit** an. So kann man die Änderungen mit zwei Mausclicks rückgängig machen.
- Man sollte von Speziell zu Allgemein ersetzen.
    - Also erst `seatable.io/vorlagen/?lang=auto` ersetzen
    - Dann `seatable.io/vorlagen/`
    - Ansonsten bleiben Fragmente wie `?lang=auto` zurück.
- **Einschließende Dateien** erlaubt die Verwendung von `*`oder`**`. Z.B.:
    - `src/content/help/**/index.fr.md` bearbeitet nur französische Hilfeartikel
    - `src/content/templates/events/**/index.*.md` bearbeitet nur Vorlagen im Bereich Events, dafür alle Sprachen
