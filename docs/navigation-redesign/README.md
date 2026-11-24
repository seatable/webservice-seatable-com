# Umbau der Navigation

Stand: 2026-11-24. Noch nichts in Hugo umgesetzt, bisher nur Mockup.
`navigation-mockup.html` ist die einzige Quelle für Design, Texte, Icons und Linkziele
(direkt bearbeiten, es gibt keinen Generator; Schriften und Bilder sind eingebettet).
Ansehen: Datei im Browser öffnen. Menülinks zeigen auf http://localhost:1313.

## Vorgehen
1. Erst nur Deutsch, Desktop und mobil. Andere Sprachen behalten vorerst die alte Navigation (Weiche nötig).
2. Abnahme durch Christoph auf localhost:1313.
3. Danach (Vorschlag: zweiter PR) die fünf weiteren Sprachen und der Hilfe-Header.

## Entschieden
- Vorbild airtable.com, in SeaTable-Optik. Hauptpunkte: Plattform, KI, Airtable-Alternative, Lösungen, Ressourcen, Preise.
- Fünf Panels, "Preise" ist ein Direktlink. Keine zweite Ebene.
- Öffnen per Klick. Schließen per Klick, Esc oder Klick auf den abgedunkelten Hintergrund.
- Panel links, feste Breite (Liste 620 px, Teaser 520 px), volle Höhe, einspaltige Liste, scrollt intern.
- Ein fester, optionaler Teaser pro Panel.
- Abstände "mittel": Titel 20 px, Beschreibung 15 px. Icons immer an.
- Header 100 % Breite, Hauptpunkte links am Logo, rechts unverändert Login, Registrierung, Sprachwahl.
- Header oben transparent, bei offenem Panel oder nach dem Scrollen weiß.
- Smart sticky: blendet erst ab 500 px aus und nach 200 px Abwärtsscrollen am Stück, beim Hochscrollen sofort wieder ein.
- Dezente Animationen, bei "prefers-reduced-motion" keine.
- Mobil (unter 1280 px): Drill-down mit "Zurück", ohne Teaser.

## Offen
- Teaser-Hintergrund: "Hell + Schein" (gefällt, Empfehlung) oder Beige.
- Icon-Farbe: Orange stört. Empfehlung Grau, Alternativen Blau und Kachel (im Mockup umschaltbar).
- Einträge ohne Ziel beim Livegang: Empfehlung ausblenden.
  Betrifft KI-Funktionen im Überblick (/de/ki), Hochschulen & Forschung, Video-Tutorials, Feature Requests, Newsletter.
- "Zugriffsrechte bis auf Zeilenebene" ist zu pauschal (laut eigenem Vergleichsartikel Zeilenrechte nur über Apps).
  Vorschlag: "Rollen, Freigaben und Single Sign-on".
- Teaser-Texte und Icons sind Vorschläge, vier Teaser-Bilder fehlen.
- "Alle Alternativen im Vergleich" gehört in den Footer, nicht ins Menü.
- Übergangsziele: KI-App-Builder (kommt mit Release 7.0) und Rechteverwaltung & SSO führen in die Hilfe.

## Hinweise für die Umsetzung
- Betroffen: `src/themes/seatable/layouts/partials/header/` (basic, navigation-desktop, navigation-mobile) und `src/config/_default/menus.de.toml`.
- `basic-docs.html` (Hilfe) ist ein eigener Header und bleibt vorerst unverändert.
- Mehrere Heroes ziehen ihren Hintergrund mit `top-[-120px]` unter den Header: Headerhöhe beachten, alle Seitentypen prüfen.
- `/de/funktionen` hat nur generische IDs (`content-9`). Für No-Code-Datenbank, Workflow-Automatisierung und Teamwork stabile Anker ergänzen.
- Der fixierte Lesefortschritt (`baseof.html`) muss über dem Header bleiben. Sprungmarken brauchen Abstand nach oben.
- PostHog-Attribute an Login und Registrierung erhalten.
- Bei 1280 px ist der Header schon auf Deutsch knapp, andere Sprachen prüfen.
- Scrollsperre bei offenem Panel: den weißen Streifen rechts (scrollbar-gutter) sauberer lösen.
