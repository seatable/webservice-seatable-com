---
title: 'KI unterstützte Automationen: Das Highlight von SeaTable 6.0'
description: 'Mit SeaTable 6.0 halten KI unterstützte Automationen Einzug in die Cloud. Profitieren Sie von intelligenter Prozessautomatisierung, voller DSGVO-Konformität und maximaler Datensouveränität dank eigenem KI-Server in Deutschland.'
date: '2025-09-30'
lastmod: '2025-10-31'
url: '/ki-automationen-datenschutz'
seo:
    title: 'SeaTable 6.0 – Sichere KI-Automationen made in Europe'
    description: 'Erleben Sie mit SeaTable 6.0 sichere KI-Automationen in der Cloud – modernste Technologie mit deutschem Datenschutz. '
categories:
    - 'product-features'
tags:
    - 'IT Sicherheit & Datenschutz'
    - 'IT Prozesse'
    - 'Digitale Transformation'
    - 'Künstliche Intelligenz'
color: '#f2d1e3'
register:
   show: true
---

Der 1. Oktober 2025 markiert für uns bei SeaTable einen besonderen Moment: Die Veröffentlichung von Version 6.0. Und diese Version hat es in sich. Mit den neuen **KI unterstützten Automationen** schlagen wir ein ganz neues Kapitel auf – eines, das den Arbeitsalltag in Unternehmen spürbar verändern wird.

Denn Automationen waren schon immer ein Kernstück von SeaTable. Sie helfen dabei, wiederkehrende Prozesse zu standardisieren und Abläufe einfacher zu machen. Aber jetzt gehen wir den entscheidenden Schritt weiter: Wir kombinieren unsere Automationen mit künstlicher Intelligenz (=KI). Plötzlich können Prozesse nicht nur _automatisiert_, sondern auch _intelligent_ gesteuert werden. Rechnungen, die automatisch in Tabellen eingetragen werden, E-Mails, die nach Inhalt sortiert und weitergeleitet werden, oder lange Texte, die in Sekundenschnelle auf das Wesentliche reduziert werden – all das wird nun Realität in SeaTable.

## Warum wir unseren eigenen KI-Server betreiben

Natürlich könnte man dafür einfach auf die Dienste bekannter KI-Anbieter zurückgreifen. Viele Softwarelösungen tun genau das: Sie binden ein amerikanisches Modell ein, schicken die Daten ihrer Kunden dorthin – und verschweigen oft, dass diese Daten nicht nur verarbeitet, sondern im Zweifel auch zum Training der nächsten Modellgeneration genutzt werden. Im ersten Moment klingt das bequem, doch aus Sicht des Datenschutzes ist es ein Albtraum: sensible Unternehmensdaten, die irgendwo landen, wo die Kontrolle verloren geht.

Wie real diese Risiken sind, zeigte jüngst ein vielbeachteter Vorfall bei Samsung aus dem Jahre 2023: Mitarbeitende hatten vertraulichen Quellcode und interne Notizen in ChatGPT eingegeben, um Unterstützung bei ihrer Arbeit zu erhalten. Da OpenAI diese Eingaben laut eigenen Nutzungsbedingungen speichert und für das Training nutzen darf, lagen plötzlich sensible Geschäftsgeheimnisse bei einem externen US-Anbieter – ein Kontrollverlust mit unkalkulierbaren Folgen. Samsung stoppte daraufhin die Nutzung von ChatGPT im Unternehmen und prüft nun eigene Lösungen. ([Quelle: HÄRTING Rechtsanwälte](https://haerting.de/wissen/samsungs-chatgpt-leak-ki-risiken-im-berufsalltag/))

{{< warning headline="Dieser Fall macht deutlich" text="Wer Unternehmensdaten leichtfertig in externe KI-Dienste einfließen lässt, riskiert massive Sicherheits- und Rechtsprobleme." />}}

Wir bei SeaTable wollten einen anderen Weg gehen. Einen Weg, der Unternehmen die Sicherheit gibt, sich auf moderne KI zu verlassen, ohne dabei ihre Datenhoheit aufzugeben. Genau deshalb haben wir uns für den Betrieb eines eigenen KI-Servers entschieden – im hochsicheren Rechenzentrum von Hetzner in Deutschland. So garantieren wir: Alle Daten bleiben in Europa, alle Prozesse sind vollständig DSGVO-konform.

Für uns bedeutet das Verantwortung. Für Sie bedeutet es ein Plus an Transparenz, Datenschutz und Vertrauen.

## Technischer Unterbau unseres KI-Servers „made in Europe“ für die SeaTable Cloud

Um diesen Anspruch einzulösen, setzen wir auf eine durchdachte Infrastruktur. Herzstück ist ein GPU-Server bei Hetzner (GEX44, ab 220 € pro Monat), auf dem das Modell Gemma 4 E4B zum Einsatz kommt. Dieses Modell haben wir bewusst gewählt:

- Kleinere Modelle lieferten in unseren Tests nicht die benötigte Qualität – sie waren schlicht zu ungenau, vor allem in mehrsprachigen Szenarien oder bei Aufgaben wie OCR.
- Größere Modelle hätten zwar vielleicht noch mehr Potenzial, erfordern jedoch erheblich leistungsfähigere (und damit teurere) Hardware.

Mit Gemma 4 E4B erreichen wir den idealen Mittelweg: ein leistungsstarkes, etabliertes Modell, das Texte wie auch visuelle Inputs zuverlässig versteht.

Und die Leistung kann sich sehen lassen:

| Parameter          | Erwarteter Wert auf Hetzner GEX44 mit vLLM & Gemma 4 E4B |
| ------------------ | -------------------------------------------------------- |
| Token-Durchsatz    | 1.200-2.000 Tokens/Sekunde                               |
| Parallele Anfragen | 5-10 gleichzeitig                                        |
| Antwortzeiten      | ~5 Sekunden                                              |

Schnell, effizient und stabil genug, um echten Mehrwert im täglichen Betrieb zu bringen.

Sollte sich zeigen, dass dieser GPU-Server nicht die notwendige Leistungsfähigkeit besitzt, werden wir die Hardware bei Bedarf anpassen.

## KI-Automatisierungen in der Praxis

Besonders spannend sind die konkreten Anwendungen, die damit möglich werden – und die Ergebnisse landen immer da, wo sie hingehören: in Ihrer **SeaTable Base**.

- **Rechnungsverarbeitung:** Eingehende Rechnungen per E-Mail werden automatisch erkannt, Inhalte wie Rechnungsnummer, Datum oder Betrag extrahiert und direkt gespeichert.
- **Smartes Support-Management:** Supportanfragen werden analysiert, in Kategorien sortiert und an die richtigen Mitarbeiter übergeben. So werden Tickets schneller bearbeitet.
- **Text- und Dokumentenzusammenfassungen:** Lange Berichte oder Memos verwandeln sich in Sekunden in kompakte Überblickstexte.
- **Mehrsprachige Erkennung:** Inhalte in verschiedenen Sprachen lassen sich problemlos verarbeiten – ein echter Vorteil für international arbeitende Teams.

Alle Funktionen sind so gestaltet, dass sie auch für KI-Neulinge problemlos nutzbar sind.

![Automations-Wizard mit KI-Automationen in SeaTable 6.0](ai-automations-in-seatable.png 'Der neue Automations-Wizard mit KI-Automationen in SeaTable 6.0')

## Verfügbarkeit und Ausblick

Mit **Version 6.0** stehen die _KI unterstützten Automationen_ allen **Enterprise-Kunden** kostenlos zur Verfügung – mit ausreichenden Kontingenten, um die neuen Möglichkeiten intensiv zu testen.

Mit **Version 6.1** öffnen wir die Funktionen auch für Free- und Plus-Pläne in kleinerem Umfang. Darüber hinaus werden wir das **Logging erweitern** und die Möglichkeit schaffen, zusätzliche **AI-Credits** direkt über uns zu beziehen, um auch anspruchsvollere Szenarien abzubilden.

## LLM-Freiheit in SeaTable: Von Hetzner-Hosting bis OpenAI und Co.

Ein weiteres zentrales Feature, das wir für kommende Versionen planen, ist die Möglichkeit für Anwender, neben unserem selbst gehosteten LLM (Large Language Model) bei Hetzner auch andere Modelle aus der Cloud zu nutzen. Bei Automationen, die auf öffentlich verfügbare Daten zugreifen – oder bei denen keine Datenschutzbedenken bestehen – können Sie dann frei wählen, ob Sie beispielsweise Gemma, DeepSeek, Mistral, OpenAI oder ähnliche Anbieter verwenden möchten. Unser Ziel ist es, den Anwendern die Entscheidung zu überlassen, welches KI-Modell am besten zu ihrem Anwendungsfall passt.

## Fazit: Innovation trifft Verantwortung

Mit SeaTable 6.0 bringen wir nicht nur eine neue Version auf den Markt, sondern eröffnen Unternehmen die Chance, ihre Arbeit auf ein neues Niveau zu heben. Intelligente Automatisierung spart Zeit, macht Prozesse effizienter und schafft Freiräume – und mit unserem europäischen Ansatz bleibt dabei das höchste Gut unangetastet: die Hoheit über Ihre Daten.

_KI-gestützte Automationen – ein Versprechen an Innovation, Datenschutz und Zukunftssicherheit. Made in Europe, made for you._

{{< newsletter title="Interessiert an KI, Automationen und Datenschutz?" submit="Jetzt anmelden" >}}

Melden Sie sich zu unserem **Newsletter** an und erhalten Sie regelmäßig die wichtigsten Trends, Tipps und Updates rund um KI, smarte Automationen und Datenschutz – praxisnah und verständlich präsentiert.

{{< /newsletter >}}
