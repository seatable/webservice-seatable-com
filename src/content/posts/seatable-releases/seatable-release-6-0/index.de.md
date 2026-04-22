---
title: 'SeaTable 6.0: No-Code wird intelligent'
description: 'SeaTable 6.0 vereint No‑Code und KI: neue KI‑Funktionen, überarbeiteter Automations‑Editor, Kalender‑, Kanban‑, Galerie‑Ansichten und Telefonnummernspalte.'
date: 2025-11-04
author: 'rdb'
url: '/de/seatable-release-6-0'
color: '#ff9831'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 6.0: No-Code wird intelligent'
    description:
register:
   show: true    
---

SeaTable 6.0 vereint die Stärken von No-Code und künstlicher Intelligenz (KI). **Mit den neuen KI-Funktionen** lassen sich Datensätze analysieren, modifizieren und erweitern, Dokumente auswerten und relevante Informationen präzise extrahieren. Und das ganz ohne Sorgenfalten in Sachen Datenschutz und Vertraulichkeit: SeaTable unterstützt eine Vielzahl von KI-Anbietern und -Modellen. Natürlich ist auch das **Selbsthosting von KI-Modellen** möglich. Diesen Weg gehen wir im Interesse des Schutzes Ihrer Daten.

**Der komplett überarbeitete Editor für Automationsregeln** macht die Nutzung der neuen KI-Funktionen spielend einfach. Aber auch alle anderen Automationen profitieren von der Workflow-orientierten Benutzeroberfläche des Regel-Editors und dessen erweiterten Funktionen.

Ein Mehr an Übersichtlichkeit und Funktionen bieten auch **die neuen Ansichtstypen Kalender, Kanban und Galerie**, welche die gleichnamigen Plugins ablösen. Wie schon die bekannte Tabellenansicht unterstützen die drei neuen Ansichtstypen die Zusammenarbeit auf höchstem Niveau mit Funktionen wie Ansichtsfreigaben, privaten Ansichten und kollaborativer Datenbearbeitung in Echtzeit.

Zahlreiche Verbesserungen im App Builder und im Base Editor, wie z. B. die universelle Verfügbarkeit komplexer Filter und **der neue Spaltentyp Telefonnummer**, optimieren bestehende Funktionalitäten und tragen Kundenwünschen Rechnung.

SeaTable Cloud haben wir heute Morgen auf Version 6.0 aktualisiert. Selbsthoster, die seit dem 30. September eine Beta-Version nutzen konnten, können nun das Stable Release aus dem bekannten [Docker Repository](https://hub.docker.com/r/seatable/seatable-enterprise) von SeaTable Server herunterladen. Die vollständige Liste der Änderungen findet sich wie immer im [Changelog](https://cloud.seatable.io/dtable/view-external-links/c9124bcd934b47bc8f30/).

## KI-ready mit KI-Automationen (beta)

Texte auswerten, Manuskripte übersetzen, Informationen aus Dokumenten extrahieren, Entwürfe auf Basis von Stichwörtern erstellen und vieles mehr – SeaTables neue KI-Funktionen bringen die Leistungsfähigkeit moderner KI direkt in SeaTable.

Für Standardaufgaben gibt es **dedizierte KI-Funktionen**. Funktionen wie *Summarize*, *OCR*, *Extract* und *Classify* machen die Nutzung von KI in Unternehmensprozessen so einfach wie nur vorstellbar. Sie wählen nur die Funktion und definieren die Input- und Output-Spalten. Detailinstruktionen, sofern nötig, können Sie über einen Prompt an das KI-Modell übergeben.

![Neue KI-Funktionen](new-ai-function.png)

Passt keine dedizierte KI-Funktion, dann hilft die **Custom-Funktion** aus. Bei dieser wird das KI-Modell allein auf Basis Ihres individuellen Prompts tätig. Informationen aus dem Datensatz übergeben Sie einfach, indem Sie in geschweiften Klammern eine Spalte referenzieren, z. B. „Schreibe eine Geschichte mit 1000 Wörtern basierend auf den Stichwörtern in {Keywords}.“

Die neuen KI-Funktionen sind in SeaTables Automationen integriert und lassen sich genauso einfach – dank des überarbeiteten Editors vermutlich sogar noch einfacher – anlegen, nutzen und verwalten. Natürlich können Sie auch bestehende Automationsregeln um KI-Funktionen erweitern und damit noch leistungsfähiger machen.

### KI-Einsatz ohne Kompromisse beim Datenschutz

SeaTable Cloud verwendet als KI-Modell ein **Gemma3** mit 12 Milliarden Parametern. Dieses multimodale Large Language Modell (LLM) aus dem Hause Google läuft **auf einem deutschen Server** der Hetzner Online GmbH und wird durch die Administratoren von SeaTable Cloud betreut. Der Datenaustausch zwischen SeaTable Cloud und dem Sprachmodell erfolgt **verschlüsselt**. Ihre Daten wandern somit nicht zu einem anderen KI-Anbieter und auch nicht ins Ausland.

Alle Abonnenten von SeaTable Cloud Enterprise erhalten **500 KI-Credits pro Teammitglied**. Die KI-Credits sind so bemessen, dass sie umfangreiche Tests ermöglichen. Für produktive Workloads sind zusätzliche Credits nötig. Diese können während der Beta-Phase auf Nachfrage kostenlos bereitgestellt werden.

**Selbsthoster von SeaTable Server** können ihr LLM ebenfalls selbst hosten, müssen dies aber nicht. **SeaTable AI**, eine neue Komponente von SeaTable Server, basiert auf LiteLLM und unterstützt dadurch die Anbindung einer Vielzahl von Modellen und Anbietern – darunter alle LLM-Dienste mit einer OpenAI-kompatiblen API. Das Deployment von SeaTable AI erfolgt, ebenso wie bei allen anderen Komponenten von SeaTable Server, per Docker bzw. Docker Compose. Im [Admin-Handbuch](https://admin.seatable.com/) finden Sie Beispielkonfigurationen für zahlreiche populäre LLMs.

### Ausblick auf die weitere KI-Entwicklung

Die KI-Funktionen in SeaTable 6.0 sind beta und werden in den kommenden Monaten dynamisch verbessert und erweitert. Die Arbeiten an einem **KI-Assistenten** und einem **MCP-Server** sind in vollem Gange. In Kürze werden in SeaTable Cloud weitere KI-Modelle zur Auswahl stehen. Neben dem von SeaTable selbst gehosteten LLM werden dann auch Modelle der bekannten Anbieter **OpenAI, Anthropic, Meta und xAI** ebenso wie die des europäischen Anbieters **Mistral** zur Verfügung stehen. SeaTable Server Administratoren werden ebenfalls mehrere KI-Modelle konfigurieren können. So können Sie für jeden Anwendungsfall das optimale Modell verwenden. 

**Nutzungstracking** und **Berechtigungsmanagement** sind weitere Schwerpunkte in der Entwicklung. Unser Ziel: ein Maximum an Transparenz und Kontrolle über die Verwendung von KI-Credits in SeaTable.

## Automatisierung so einfach wie noch nie

In SeaTable 6.0 wird **das Anlegen und Verwalten von Automationsregeln** noch leichter und komfortabler. Ein komplett überarbeiteter Editor bietet mehr Übersichtlichkeit und zusätzliche Funktionen.

![Neu designter Automations-Editor](new-automation-editor.png)

Der Editor von SeaTable 6.0 erstreckt sich über die gesamte Bildschirmbreite und ermöglicht so **ein neues Layout**: Auf der linken Seite finden sich – analog zu den Ansichten – alle bestehenden Regeln. Ein **Wechsel zwischen zwei Regeln** ist damit nur noch eine Sache von einem Klick. Im zentralen Bereich befindet sich die aktive Automationsregel. Die **Konfiguration des Triggers bzw. der Aktionen** wird auf der rechten Seite dynamisch eingeblendet. Ein weiterer Komfortfaktor ist die **variable Höhe des Editor-Panels**. So bleiben die Spaltennamen und Beispieldaten sichtbar, während man an einer Automationsregel arbeitet.

Der neue Editor trägt auch dem vielfach geäußerten Wunsch Rechnung, **Automationsregeln gruppieren und verschieben zu können**. Darüber hinaus lassen sich Aktionen in einer Regel duplizieren.

## Aus drei Plugins werden Ansichten

Die drei Plugins [Kalender]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}), [Galerie]({{< relref "help/base-editor/ansichten/die-galerie-ansicht" >}}) und [Kanban]({{< relref "help/base-editor/ansichten/die-kanban-ansicht" >}}) sind seit der Version 1.0 fester Bestandteil von SeaTable. Nach nun 5 Jahren erhalten Sie eine neue Form: Aus den Kalender-, Kanban- und Galerie-Plugins werden **Kalender-, Kanban- und Galerie-Ansichten**. In SeaTable 6.1 wird das [Timeline-Plugin]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}) folgen.

Die Reimplementierung der Plugins als Ansichten bietet mehrere Vorteile: Einerseits wird die Nutzung deutlich vereinfacht. **Die Installation der Plugins in einer Base entfällt**, denn die Ansichten stehen unmittelbar zur Verfügung. Auch SeaTable Server Admins werden die Integration zu schätzen wissen: Das separate Update der Plugins entfällt zukünftig ebenfalls.

![Neue Kalender-Ansicht](new-view-list-pinned.png)

Darüber hinaus sind die neuen Ansichten den bisherigen Plugins funktional weit überlegen: Die Kalender-, Kanban- und Galerie-Ansichten lassen sich individuell im Rahmen einer [Ansichtsfreigabe]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}}) oder einer [benutzerdefinierten Freigabeberechtigung]({{< relref "help/startseite/freigaben/benutzerdefinierte-freigabe-erstellen" >}}) teilen. Die bisherige Notwendigkeit, [die gesamte Base freizugeben]({{< relref "help/startseite/freigaben/eine-base-an-eine-gruppe-freigeben" >}}), um gemeinsam an einem Kalender oder einem Kanban-Board zu arbeiten, fällt weg. Ansichten aller Typen bieten optional auch **private Ansichten**, die nur der Ersteller sehen kann. Alle Ansichten, mit Ausnahme der Big-Data-Ansicht, unterstützen zudem **die gemeinsame Bearbeitung in Echtzeit**. Eine Änderung durch einen Benutzer wird unmittelbar anderen Benutzern angezeigt.

{{< warning headline="Beachten Sie bitte" text="Mit SeaTable 6.0 werden sich die drei Plugins nicht mehr in Bases installieren lassen. In Bases, in denen die Plugins bereits in Verwendung sind, stehen sie bis auf Weiteres zur Verfügung und können uneingeschränkt genutzt werden. Unsere Empfehlung ist jedoch eine andere: Nutzen Sie die Vorteile der neuen Ansichten! Der Wechsel könnte kaum einfacher sein. Alle drei Plugins bieten die **Migration mit nur einem Klick**. Diese konvertiert einen Tab in einem Plugin ohne weiteren Aufwand in eine Ansicht vom gleichen Typ." />}}

## Mehr Flexibilität im App Builder

Im [App Builder]({{< relref "help/app-builder" >}}) von SeaTable 6.0 fällt **die neue orangefarbene Plus-Schaltfläche** auf. Mit ihr können Sie, egal wo Sie sich gerade in Ihrer App befinden, ein neues Element in der Navigation hinzufügen. Eine funktionale Neuerung zeigt sich bei einem Klick auf die Schaltfläche: Neben Seiten und Ordnern können Sie nun auch **Direktlinks zu externen Webseiten** in die Navigation einfügen. Ein Link zu einer Datenschutzerklärung oder einem externen Wiki muss also nicht mehr in eine Seite eingebettet werden, sondern kann prominent direkt in der Navigation erscheinen. Mehrere Kunden hatten uns um diese Gestaltungsoption gebeten.

![Direktlink einfügen](new-direct-link-in-apps.gif)

Auch die weiteren Verbesserungen im App Builder drehen sich um das Thema Flexibilität: Die Seiteneinstellungen der [Seitentypen]({{< relref "help/app-builder/seitentypen-in-universellen-apps" >}}) Kalender, Kanban, Galerie und Zeitleiste erlauben es nun auch, **einzelne Spalten vor Änderungen zu schützen**. Damit bieten nun alle relevanten Seitentypen diese Funktionalität.

In der Base gibt es sie schon seit Version 5.2, nun gibt es sie auch im App Builder: **komplexe Filter**. Sowohl die Dateneinstellungen als auch die Einstellungen für Verknüpfungsspalten unterstützen nun Filtergruppen. Auch Benutzer einer Tabellenseite können nun Suchmuster mit logischen UND- und ODER-Operatoren verwenden.

## Mehr Funktionen in der Teamverwaltung

Die [Teamverwaltung]({{< relref "help/teamverwaltung" >}}) von SeaTable Cloud erfährt mit dem Major Release eine umfangreiche Überarbeitung. Zuerst fällt die Angleichung des Designs der Teamverwaltung an das der Webseite ins Auge. Von größerer Bedeutung für die Nutzung sind jedoch die neuen Funktionen:

- Konfiguration von SSO mittels SAML (nur für Enterprise Abonnenten)
- Integration eines Logs für Teamaktivitäten (nur für Enterprise Abonnenten)
- Integration eines Logs der Teamlogins
- Versand von Rechnungen per E-Mail
- Verwaltung mehrerer Zahlungsmittel


## Weitere Verbesserungen

Version 6.0 führt SeaTables 26. Spaltentyp ein. **Der neue Spaltentyp Telefonnummer** macht die Kommunikation noch einfacher. Ein Klick auf das Telefon-Icon in einer Zelle überträgt die Telefonnummer in Ihre Telefonie-Anwendung. Bei Mobiltelefonen funktioniert das ohne jede weitere Konfiguration. Auf dem Desktop ebenso, wenn im Browser eine Verknüpfung mit einer Telefoniesoftware eingerichtet ist.

![Spaltentyp Telefonnummer](new-column-type-phone-number.gif)

Die [Exportfunktion]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}) unterstützt mit SeaTable 6.0 den **Export der im Big-Data-Speicher archivierten Daten**. Wenn Sie die Option beim Export aktivieren, erstellt SeaTable zunächst die Exportdatei im DTABLE-Format und informiert Sie nach Abschluss des Vorgangs mittels Benachrichtigung. Der Download der Datei erfolgt dann über die Dateiverwaltung der Base. Die Daten aus dem Big-Data-Speicher werden in einem Binärformat im Ordner „archive“ in der DTABLE-Datei gespeichert. Selbstverständlich lässt sich eine DTABLE-Datei mit Big Data wie jede andere DTABLE-Datei einfach wieder in SeaTable importieren.

Die Eingabe von Daten in [Datum-Spalten]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) wird komfortabler. Bisher verlangte SeaTable die Eingabe eines vollständigen Datums. Wurde ein Teil, z. B. das Jahr oder eine führende Null weggelassen, war dies eine ungültige Eingabe. Nun nicht mehr. „25-11-4“ wird korrekt als 2025-11-04 interpretiert. Und das funktioniert logischerweise nicht nur bei Datumsangaben im ISO-Format.

Probieren Sie SeaTable 6.0 aus! Wir sind sicher, dass auch Sie begeistert sein werden.

{{< newsletter title="Bleiben Sie informiert" subtitle="" submit="Jetzt abonnieren" >}}

Abonnieren Sie unseren **Newsletter** und verpassen Sie nie wieder Neuigkeiten über SeaTable!

{{< /newsletter >}}
