---
title: 'Schritt 1: Import der Base'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/de/hilfe/schritt-1-import-der-base'
seo:
    title: 'Schritt 1 im SeaTable Kurs 2: Base importieren und verstehen'
    description: 'Beginnen Sie den Onlinekurs 2: Importieren Sie die vorbereitete Base, lernen Sie Struktur, Formelspalten und Ansichten für den Geschäftsprozess kennen.'
---

Bevor Sie in SeaTable einen neuen Geschäftsprozess abbilden können, müssen Sie zunächst die passende Tabellenstruktur erstellen. Nur so können Sie die benötigten Daten für den Prozess sinnvoll erfassen und später effizient verarbeiten. Sie können sich zwar von den zahlreichen Vorlagen inspirieren lassen, doch in der Regel ist es notwendig, den Prozess genau zu durchdenken und die relevanten Daten klar zu definieren.

Da es in diesem Kurs um die Verwaltung von Online-Dienstleistungen geht, benötigen wir zwei zentrale Tabellen:

- Eine Tabelle zur Erfassung der Kursangebote
- Eine Tabelle für die Teilnehmer

Im ersten Kurs haben Sie bereits gelernt, wie Sie eine Base mit verschiedenen Spaltentypen erstellen. Daher überspringen wir diesen Schritt und beginnen direkt mit einer vorbereiteten Grundlage.

Laden Sie die folgende Datei auf Ihren PC herunter und importieren Sie diese auf der Startseite von SeaTable als neue Base:

[SeaTable Course Level 2.dtable](/SeaTable-Course-Level-2.dtable)

Auch wenn Sie die Base nicht selbst erstellen müssen, ist es wichtig, dass Sie sich intensiv mit der Struktur vertraut machen. Es wurden neue Spaltentypen verwendet, die Sie eventuell aus dem vorherigen Kurs noch nicht kennen.

## Die Komponenten der Base

Auf den ersten Blick wirkt die Base recht übersichtlich. Sie besteht lediglich aus:

- 2 Tabellen
- 18 Spalten
- 3 Ansichten
- 1 Webformular

Doch lassen Sie sich von der Einfachheit nicht täuschen: Diese Struktur ist erstaunlich leistungsfähig. Im Folgenden erkläre ich, warum wir die Base auf diese Weise gestaltet haben.

### Ihr Kursangebot im Überblick

In der Tabelle `Courses` finden Sie alle wichtigen Informationen zu Ihren Angeboten. Jede Zeile repräsentiert einen Kurs oder eine Dienstleistung, die Sie anbieten. Die einzelnen Spalten liefern detaillierte Angaben, wie z. B.:

- Kursname
- Datum und Ort des Kurses
- Anzahl der angemeldeten Teilnehmer
- Status des Kurses (ausgebucht oder noch Plätze frei)

Diese strukturierte Übersicht ermöglicht es Ihnen, jederzeit den Überblick über Ihre Kurse und Teilnehmerzahlen zu behalten.

![Tabelle „Courses“ mit Kursdaten, Teilnehmerzahl und Status pro Kurs](images/lvl2-table-courses.png)

{{< warning  headline="Termine liegen in der Vergangenheit"  text="Sie werden feststellen, dass alle Kurstermine in der Vergangenheit liegen. Dies lässt sich ganz einfach damit begründen, dass wir diesen Onlinekurs nicht regelmäßig aktualisieren wollten. Ignorieren Sie somit diese Tatsache für diesen Online-Kurs." />}}

### Alles Wichtige zu Ihren Kursteilnehmern

In der Tabelle `Registrations` werden alle Daten zu den Personen erfasst, die sich für Ihre Kurse angemeldet haben. Jede Zeile steht für einen Teilnehmer und enthält folgende Informationen:

- Name des Teilnehmers
- E-Mail-Adresse
- Der Kurs, für den sich die Person angemeldet hat
- Zahlungsstatus (ob bereits bezahlt wurde)

Diese Tabelle gibt Ihnen jederzeit einen klaren Überblick über den aktuellen Anmeldestand und den Status der Zahlungen.

![Tabelle „Registrations“ mit Namen, E-Mail und gebuchten Kursen der Teilnehmer](images/lvl2-table-registrations.png)

{{< warning  headline="Ausgeblendete Spalten"  text="Für eine bessere Übersichtlichkeit wurden zwei Spalten ausgeblendet. Sie werden später sehen, dass wir diese Spalten sowieso nur für den Seriendruck benötigen." />}}

## Weitere Besonderheiten

Einige Funktionen dieser Base werden erst durch bestimmte Konfigurationen verständlich. Bitte lesen Sie die folgenden Erklärungen aufmerksam durch, damit Sie die nachfolgenden Abschnitte besser nachvollziehen können.

### Formelspalten

In der Tabelle `Courses` finden Sie zwei wichtige Formelspalten, deren Nutzen ich Ihnen gerne erläutern möchte:

- `{{< seatable-icon icon="dtable-icon-formula" >}} Title and Date`
- `{{< seatable-icon icon="dtable-icon-formula" >}} Status`

`{{< seatable-icon icon="dtable-icon-formula" >}} Title and Date` ist eine Hilfsspalte, die die Werte aus den Spalten „Title“ und „Date“ miteinander verknüpft. Die verwendete Formel ist sehr einfach und fügt lediglich den Kurstitel und das Kursdatum zusammen.

![Formelspalte „Title and Date“, die Kurstitel und Datum zu einer Anzeige kombiniert](images/lvl2-formula-title-date.png)

Auf den ersten Blick scheint diese Spalte überflüssig zu sein, da sie nur vorhandene Daten kombiniert. Aber vertrauen Sie mir: Wenn wir gleich das Anmeldeformular analysieren, werden Sie verstehen, warum diese Spalte äußerst nützlich ist.

---

Die Formelspalte `{{< seatable-icon icon="dtable-icon-formula" >}} Status` ermittelt automatisch, ob in einem Kurs noch Plätze verfügbar sind oder ob der Kurs bereits ausgebucht ist. Die Logik dahinter ist relativ simpel, könnte jedoch bei einem produktiven Einsatz auch das Veranstaltungsdatum berücksichtigen.

![Formelspalte „Status“, die automatisch freie Plätze oder Ausgebucht für jeden Kurs berechnet](images/lvl2-formula-status.png)

{{< warning  headline="Der Nutzen von Formelspalten"  text="Formelspalten spielen eine zentrale Rolle bei der Entwicklung leistungsfähiger Bases in SeaTable. Sie dienen dazu, Informationen zu verknüpfen oder bestimmte Zustände zu definieren. Der volle Nutzen dieser Spalten zeigt sich oft erst bei der Arbeit mit anderen Funktionen." />}}

### Ansicht zur Auswahl von verfügbaren Kursen

In der Tabelle `Courses` gibt es eine spezielle Ansicht namens `{{< seatable-icon icon="dtable-icon-main-view" >}} Available Courses`. Diese Ansicht filtert die Formelspalte `{{< seatable-icon icon="dtable-icon-formula" >}} Status` und zeigt ausschließlich Kurse an, bei denen noch Plätze frei sind. Ausgebuchte Kurse werden automatisch ausgeblendet.

Diese Ansicht ist gegen weitere Bearbeitung gesperrt {{< seatable-icon icon="dtable-icon-unlock" >}}, um sicherzustellen, dass sie unverändert bleibt. Sie spielt eine wichtige Rolle, da sie die Auswahlmöglichkeiten in der Link-Spalte `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Registered for` begrenzt.

Wenn wir uns gleich das Anmeldeformular genauer anschauen, wird deutlich, warum diese Ansicht so hilfreich ist.

![Einstellungen der Link-Spalte „Registered for“, begrenzt auf Ansicht „Available Courses“](images/lvl2-link-column-limit-to-view.png)

### Farbige Markierung von Zeilen und Spalten

SeaTable bietet die Möglichkeit, Zeilen, Spalten und Zellen farblich hervorzuheben. In diesem Template sind zwei solcher Effekte bereits integriert:

- Die Zeilen der Kurse werden je nach Status markiert: Kurse mit freien Plätzen sind grün hervorgehoben, während ausgebuchte Kurse rot gekennzeichnet sind.
- Die Kurspreise sind je nach Höhe farblich abgestuft: Je teurer der Kurs, desto dunkler die Markierung.

## Machen Sie sich vertraut mit der Base

Nehmen Sie sich ausreichend Zeit, um die Base im Detail zu erkunden. Sollten Ihnen bestimmte Funktionen noch unbekannt sein, zögern Sie nicht, die verlinkten Hilfeartikel zu lesen.

## Hilfeartikel mit weiteren Informationen

- [Erstellen einer Base aus einer DTABLE-Datei]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei" >}})
- [Grundlagen von SeaTable Formeln]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}})
- [Farbliche Markierung von Zeilen]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Ansichten sperren]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
