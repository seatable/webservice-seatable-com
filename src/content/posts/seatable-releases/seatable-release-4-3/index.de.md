---
title: 'SeaTable 4.3: Neue Formularlinks, Automationen & App-Features'
description: 'Neue Links für Webformulare, Automatisierung von PDF-Erstellung und App-Benachrichtigungen, Mitarbeiter-Spalte teamübergreifend, Kommentare und neue Card- und Container-Elemente für die Universal App. Rich-Text-Mails, neue Theme-Optionen, feinere Gruppenrechte – und eine intuitivere Migration für Admins.'
date: 2024-02-08
lastmod: '2024-02-16'
author: 'kgr'
url: '/de/seatable-release-4-3'
color: '#fd5d04'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 4.3: Form-Links, Automation & App-Tools'
    description: 'Individuelle Form-Links, PDF-Automation und neue App-Elemente: SeaTable 4.3 macht die Arbeit mit Daten und Apps kreativer, schneller, einfacher!'
---

Die Karnevalszeit in Deutschland nähert sich ihrem Höhepunkt – und auch bei SeaTable knallen die Konfetti-Kanonen! Version 4.3 bringt einige lang ersehnte Funktionen und Verbesserungen mit sich.

Freuen Sie sich auf einen neuen Dialog zur Erstellung von **Formularlinks**, in dem Sie die URLs an Ihre persönlichen Wünsche anpassen können. Nutzen Sie zwei neue **Automationen**, um Dokumente zu erstellen und Benachrichtigungen an App-Nutzer zu senden. Oder probieren Sie die Neuerungen in der **Universellen App** aus: Auf Sie warten unter anderem Kommentare, zwei weitere Elemente für die individuelle Seite und ein verbessertes Customizing der Farbgestaltung.

Heute Morgen haben wir SeaTable Cloud auf Version 4.3 aktualisiert. Alle Selbsthoster können das ebenfalls tun: Das Image von SeaTable 4.3 ist im bekannten [Docker Repository](https://hub.docker.com/r/seatable/seatable-enterprise) zum Download verfügbar. Im [Changelog]({{< relref "pages/changelog" >}}) finden Sie wie immer die vollständige Liste der Änderungen.

Darüber hinaus haben wir ein Upgrade der Plugins auf Webpack 5 durchgeführt sowie ein Upgrade des Frameworks auf React 17.0.2, das künftig mehr Sicherheit und Stabilität gewährleistet und weitere Funktionen ermöglicht.

## Neuer Dialog und benutzerdefinierte Links für Webformulare

Um Ihre [Webformulare]({{< relref "help/base-editor/webformulare" >}}) an andere Nutzer freizugeben, gab es bislang zwei verschiedene Dialogfenster: eines, in dem Sie einen **automatisch generierten Link** kopieren konnten; und eines, in dem Sie diesen Link mit [vorbefüllten Werten]({{< relref "help/base-editor/webformulare/formularfelder-per-url-vorbefuellen" >}}) erweitern konnten. Diese Möglichkeiten haben wir nun in einem einzigen Dialog zusammengeführt, um die Usability zu erhöhen.

Zudem haben wir die brandneue Option ergänzt, **benutzerdefinierte URLs** für Webformulare zu erstellen. Anschließend können Sie diese bearbeiten, als QR-Code speichern, kopieren oder löschen.

![Neuer Formularlink-Dialog in SeaTable 4.3](Formularlink-Dialog.gif)

{{< warning headline="Hinweis" text="Der benutzerdefinierte Teil, der an den Link angehängt wird, muss **zwischen 5 und 30 Zeichen** lang sein und darf nur **Buchstaben**, **Zahlen** und **Bindestriche** enthalten. Noch dazu muss jede URL eindeutig sein: Falls eine benutzerdefinierte URL bereits belegt ist, erscheint eine Fehlermeldung." />}}

## Automatisierte Aktionen: PDF speichern und App-Benachrichtigung senden

Automations-Fans aufgepasst! In SeaTable 4.3 kommen zwei neue Optionen zu den [automatisierten Aktionen]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) hinzu:

1. Erstens haben Sie die Möglichkeit, periodisch PDFs für Einträge zu speichern, die bestimmte Bedingungen erfüllen.
2. Zweitens können Sie neuerdings Benachrichtigungen versenden, die bestimmte Nutzer einer Universellen App erhalten sollen.

Zuvor konnten Sie in SeaTable nur manuell [PDF-Dokumente per Schaltfläche erzeugen]({{< relref "help/base-editor/schaltflaechen/ein-pdf-dokument-per-schaltflaeche-in-einer-spalte-speichern" >}}). Die neue Option, zu einem festgelegten Zeitpunkt **automatisch** Dokumente aus bestimmten Datensätzen zu erstellen, erspart Ihnen Klicks und macht Ihre Abläufe noch reibungsloser.

Durch die **App-Benachrichtigungen** können Sie die Nutzer einer App beispielsweise über Änderungen an relevanten Datensätzen informieren. Diese Aktion kann von allen vier [Trigger-Ereignissen]({{< relref "help/base-editor/automationen/automations-trigger" >}}) ausgelöst werden.

![App-Benachrichtigung senden](App-Benachrichtigung-senden.png)

Die Nutzer der jeweiligen App können ihre Benachrichtigungen über das {{< seatable-icon icon="dtable-icon-notice" >}} Glocken-Symbol neben ihrem Avatar in der rechten oberen Ecke abrufen.

## Teamübergreifende Mitarbeiter-Spalte

In der [Mitarbeiter-Spalte]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) war es bisher nur möglich Personen auszuwählen, die bereits Zugriff auf die jeweilige Base hatten. Ab SeaTable 4.3 können Sie in Mitarbeiter-Spalten **alle Mitglieder Ihres Teams** eintragen, selbst wenn diese keinen Zugriff auf bestimmte Bases haben. Dadurch wird es wesentlich komfortabler, Ihren Mitarbeitern unabhängig von ihrer Zugriffsberechtigung Datensätze zuzuordnen.

Diese Funktionalität ist vor allem in der Universellen App von Vorteil. Sie können die Option, dass die Teammitglieder in der Drop-down-Liste für alle Nutzer zu sehen sind, in den [Einstellungen]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern/" >}}) der Universellen App aktivieren. Wenn Sie nicht möchten, dass die Nutzer die Datensätze der anderen sehen können, legen Sie **voreingestellte Filter** fest: Wird eine Seite per Mitarbeiter-Spalte mit der Bedingung „inkludiert aktuellen Benutzer“ gefiltert, sieht jeder Nutzer der Universellen App nur die Einträge, die ihm in der Tabelle zugeordnet sind.

![Mitarbeiter-Spalte in der Universellen App](Mitarbeiter-Spalte-in-der-Universellen-App.gif)

## Weitere Verbesserungen der Universellen App

Ganz neu in der Universellen App ist die [Kommentarfunktion]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), die Sie bereits in gleicher Form aus der Base kennen. Halten Sie Ihr Feedback oder zusätzliche Informationen zu den Datensätzen für die anderen App-Nutzer fest und führen Sie Diskussionen an Ort und Stelle.

{{< warning headline="Gut zu wissen" text="Die Kommentare in der App sind komplett **unabhängig** von den Kommentaren in der Base. Das heißt: Jeder Kommentar ist nur dort zu sehen, wo er gepostet wird." />}}

Auf der [individuellen Seite]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}) können Sie sich auf zwei neue Elemente freuen: den **Container** und die **Karte**. Der Container gibt ein Raster vor, mit dem Sie andere Elemente (Texte, Bilder, Statistiken) leichter anordnen und in Gruppen zusammenfassen können.

![Container element on custom page in SeaTable 4.3](Container-element-on-custom-page.png)

Für ein schönes Seitenlayout sorgt auch die Karte, die ein Bild, eine Überschrift und einen Text zu einer Design-Vorlage vereint.

![Card element on custom page in SeaTable 4.3](Card-element-on-custom-page.png)

Außerdem lässt sich die **Hintergrundfarbe** von individuellen Seiten ab SeaTable 4.3 beliebig einstellen und die unerwünschte Überlappung von Elementen wurde behoben. Auch das übergreifende Design der Universellen App präsentiert sich nun über alle Seiten hinweg in einer einheitlichen Farbe, die Sie in den [globalen Einstellungen]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern/" >}}) auswählen können.

### Berechtigungen auf Tabellenseiten

Die Vererbung von [Spaltenberechtigungen]({{< relref "help/base-editor/spalten/spaltenberechtigungen-festlegen" >}}) aus der Base wird mit SeaTable 4.3 abgeschafft. Wenn Sie eine Spalte in der Universellen App für die Bearbeitung sperren möchten, können Sie sie stattdessen in den Einstellungen der [Tabellenseite]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}) auf **„nur lesbar“** setzen.

Ebenso werden alle Einschränkungen für [Schaltflächen-Aktionen]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) aufgehoben. Jeder App-Nutzer kann nun vordefinierte Änderungen an den Datensätzen ausführen, auch wenn die betroffenen Spalten ansonsten für ihn gesperrt sind und der Nutzer nicht zur Bearbeitung der Seite berechtigt ist.

## Wichtige Ankündigung: Entfernung der Galerie- und Datenabfrage-App

In Version 4.4 werden die [Galerie-App]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}) und die [Datenabfrage-App]({{< relref "help/app-builder/app-verwaltung/datenabfrage-app" >}}) verschwinden, da man ihre Funktionalität mittlerweile vollständig mit den entsprechenden **Seitentypen** in der Universellen App abbilden kann. Der Universal App Builder wird zukünftig also die einzige Option sein, um Apps in SeaTable zu erstellen.

Wenn Sie die beiden ablaufenden Apps nutzen, empfehlen wir Ihnen, Ihre Anwendungsfälle vor dem nächsten Release mit [Galerieseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}) und [Abfrageseiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}) im App Builder nachzubauen. Auf Abfrageseiten können Sie mittlerweile übrigens Felder hinzufügen, mit denen die Nutzer auch **Link-Spalten** nach bestimmten Werten durchsuchen können.

{{< warning headline="Achtung, Verwechslungsgefahr!" >}}

Die [Galerie]({{< relref "help/base-editor/ansichten/die-galerie-ansicht" >}}) und die [SQL-Abfrage]({{< relref "help/base-editor/plugins/anleitung-zum-sql-abfrage-plugin" >}}) kennen Sie auch als **Plugins**, die Sie zu Ihren Bases hinzufügen können. Diese bleiben natürlich weiterhin bestehen.

{{< /warning >}}

## Und vieles mehr

Wenn Sie [E-Mails per Automation versenden]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}), konnten Sie Ihre Nachricht bisher nur als **Klartext** in das Textfeld eingeben. Ab SeaTable 4.3 ist es wie beim E-Mail-Versand über Schaltflächen möglich, die Nachrichten im **Rich-Text- bzw. HTML-Format** zu verfassen. Aktivieren Sie dazu einfach den Regler rechts über dem Textfeld.

![Rich text in automated e-mail messages](Rich-text-in-automated-e-mail-messages.png)

Wenn Sie gerne **Spaltenberechtigungen** nutzen, um Werte vor unerwünschten Änderungen zu schützen, können Sie dies künftig noch genauer definieren. Neben _bestimmten Benutzern_, _Administratoren_ und _Niemandem_ stehen nun auch **bestimmte Gruppen** als Option zur Auswahl.

Es wird künftig die Option geben, Bases ohne die hochgeladenen Anhänge in der Dateiverwaltung zu [exportieren]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}), sofern diese das Exportlimit von 100 MB pro Base überschreiten.

In Sachen API unterstützt SeaTable 4.3 erstmals [JOIN Queries](https://developer.seatable.com/scripts/sql/reference/), mit denen Sie aus unterschiedlichen Tabellen diejenigen Datensätze abfragen können, die eine gemeinsame Schnittmenge an Attributen teilen. Mehr dazu erfahren Sie im Developer Manual.

## Vereinfachte Installation von SeaTable und zusätzlichen Komponenten

Für **On-Premises-Kunden** haben wir zum Schluss noch ein besonderes Schmankerl: Zeitgleich mit der Veröffentlichung von Version 4.3 der SeaTable Cloud haben wir auch die **Installationsanleitung** in unserem [Admin-Handbuch](https://admin.seatable.com) überarbeitet.

Unser zentrales Ziel ist es, die **Installation und zukünftige Updates Ihres eigenen SeaTable Servers** noch einfacher zu gestalten. Zum Beispiel startet der Dienst zukünftig automatisch, wenn Sie den zugehörigen Container starten, und auch Datenbank-Updates müssen Sie nicht mehr händisch anstoßen. Dies sind nur einige der vielen kleinen Verbesserungen, die Ihnen als Administrator das Leben leichter machen und ab sofort im Admin-Handbuch zu finden sind.

Zusätzlich vereinfachen wir die Installation von ergänzenden Komponenten wie der **Python-Pipeline** zum Ausführen von Python-Code in SeaTable und der **Automationsplattform n8n**. Jede dieser Erweiterungen wird fertig von uns zur Verfügung gestellt und lässt sich mit wenigen Befehlen installieren. So können Sie noch mehr aus Ihrem Server herausholen.
