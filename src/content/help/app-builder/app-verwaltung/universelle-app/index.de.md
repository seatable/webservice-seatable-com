---
title: 'Apps in SeaTable'
date: 2023-05-04
lastmod: '2026-11-17'
categories:
    - 'apps'
author: 'nsc2'
url: '/de/hilfe/apps-in-seatable'
aliases:
    - '/de/hilfe/universelle-app'
    - '/de/hilfe/welche-apps-gibt-es'
seo:
    title: 'Apps in SeaTable: Funktionen & Anleitung'
    description: 'Alles zu Apps in SeaTable: Seitentypen, Dashboards, Rechte, Nutzerverwaltung, Teilen, Kopieren, Löschen & Tipps zur Gestaltung.'
star: true
weight: 1
---

**Apps** in SeaTable sind individuelle **Frontends** bzw. Webanwendungen für spezifische Benutzergruppen, die unterschiedliche Informationsbedürfnisse haben (z. B. Mitarbeiter, Abteilungsleiter, Geschäftsführer). Das **Backend** einer App bildet dabei immer eine [Base]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}). Für jede Base können Sie beliebig viele Apps erstellen. Als Faustregel gilt: eine App pro Benutzergruppe und Anwendungsfall.

## Wie funktionieren Apps in SeaTable?

Um Apps zu bauen, gibt es den sogenannten **App Builder**, in dem man verschiedene Benutzeroberflächen anlegen und eine ganze Menge Einstellungen vornehmen kann. Dabei können Sie Ihrer Kreativität freien Lauf lassen und (mit oder ohne KI) komplett individuelle Seiten auf Basis von HTML, JavaScript und CSS zu Ihrer App hinzufügen. 

Der App Builder verfügt außerdem über eine Reihe vorgefertigter [Seitentypen]({{< relref "help/app-builder/seitentypen-in-universellen-apps" >}}), mit denen Sie Ihre Daten unter anderem in Form von **Tabellen**, **Galerien** oder **Kalendern** darstellen und diese mit anderen Nutzern teilen können. Zudem können Sie **Formulare** für die Dateneingabe und **Dashboards** mit aussagekräftigen Statistiken erstellen. 

Über die **Seitenberechtigungen** können Sie granular steuern, wer Seiten sehen, Zeilen hinzufügen, bearbeiten und löschen darf. Durch den offenen Zugang zu Apps können Sie Ihre Daten auch für **externe Nutzer ohne SeaTable Konto** nutzbar machen.

{{< warning  type="warning" headline="Berechtigung in der Gruppe erforderlich"  text="Um eine App erstellen, bearbeiten, kopieren oder löschen zu können, müssen Sie **Eigentümer** oder **Administrator der Gruppe** sein, in der sich die zugrundeliegende **Base** befindet. Einfache **Gruppenmitglieder** können lediglich bestehende Apps ansehen und nutzen." />}}

## Anlegen der App

Um eine App in Ihrer Base nutzen zu können, müssen Sie diese zunächst zu Ihrer Base **hinzufügen**.

![Die App anlegen](images/universal-app-preview.png)

[Erfahren Sie hier, wie Sie eine App zu Ihrer Base hinzufügen.]({{< relref "help/app-builder/app-verwaltung/apps-zu-einer-base-hinzufuegen" >}})

## Gestaltung der App

Nachdem Sie Ihre App erfolgreich angelegt haben, können Sie mit der Gestaltung beginnen. Achten Sie dabei darauf, stets das **Stift-Symbol** {{< seatable-icon icon="dtable-icon-rename" >}} zu nutzen, um in den [Bearbeitungsmodus]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}) der App zu gelangen.

![Apps bearbeiten](images/Apps-bearbeiten.png)

Eine App besteht aus mehreren **Seiten**, die Sie in **Ordnern** zusammenfassen können.

[Erfahren Sie hier, wie Sie neue Seiten und Ordner zu Ihrer App hinzufügen]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}).

Um die Daten in Ihrer Base ansprechend aufzubereiten, bietet die App eine Vielzahl an Seitentypen mit unterschiedlichen Gestaltungselementen.

## Vorschau einer App

Bei der Gestaltung einer App wollen Sie sicher zwischendurch testen, wie die App für die Nutzer aussieht. Dazu können Sie sich im Bearbeitungsmodus einfach die [App-Vorschau anzeigen lassen]({{< relref "help/app-builder/app-verwaltung/die-vorschau-einer-app-anzeigen-lassen" >}}).

## Einstellungen einer App ändern

Innerhalb einer App können Sie verschiedene **globale Einstellungen** vornehmen. Sie können beispielsweise den **Namen**, die **Farbe** und die **URL** Ihrer App ändern. Die gewünschten Anpassungen können Sie mit nur wenigen Klicks über die **App-Einstellungen** vornehmen.

![Öffnen der App-Einstellungen der App](images/global-settings-universal-app.png)

[Erfahren Sie hier mehr zu den globalen Einstellungen der App.]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}})

## Versionen einer App speichern

Die **Versionsverwaltung** jeder App bietet Ihnen die Möglichkeit, Momentaufnahmen von der Struktur einer App zu speichern. Wie Sie einen **App Snapshot** anlegen können, erfahren Sie [hier]({{< relref "help/app-builder/einstellungen/versionsverwaltung-und-snapshots-einer-universellen-app" >}}). Beachten Sie dabei, was ein App Snapshot speichert – und was nicht.

## Seitenberechtigungen in einer App

Um den Zugriff auf Ihre Daten genau zu steuern, können Sie für **jede Seite**, die Sie zu einer App hinzugefügt haben, **individuelle Seitenberechtigungen** festlegen. Die Bearbeitung der Seitenberechtigungen erfolgt stets über die **Seiteneinstellungen**, die Sie über das Zahnrad-Symbol {{< seatable-icon icon="dtable-icon-set-up" >}} erreichen.

![Öffnen der Seiteneinstellungen](images/page-permissions-universal-app.png)

[Erfahren Sie hier mehr zu den verschiedenen Seitenberechtigungen in der App.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

## Benutzer- und Rollenverwaltung einer App

Neue Benutzer hinzufügen, Rollen anlegen und zuweisen – in der **Benutzer- und Rollenverwaltung** einer App können Sie diverse administrative Tätigkeiten durchführen.

![Benutzer- und Rollenverwaltung einer App](images/open-user-and-role-management-1.png)

[Erfahren Sie hier mehr zur Benutzer- und Rollenverwaltung der App.]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}})

## Eine App teilen

Eine App können Sie ebenfalls über die [Benutzer- und Rollenverwaltung]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}) mit anderen Nutzern teilen. Generieren Sie hierzu einfach einen individuellen **Einladungslink** oder nutzen Sie einen **QR-Code**.

## Eine App kopieren

Sie haben eine App gebaut, die Sie in ähnlicher Form für eine weitere Nutzergruppe verwenden möchten? Dann kopieren Sie einfach die bestehende App und passen Sie die Kopie nach Belieben an. Wie Sie eine App kopieren, erfahren Sie [hier]({{< relref "help/app-builder/app-verwaltung/apps-kopieren" >}}).

## Eine App deaktivieren

Wenn Sie eine App erstellt haben, deren Nutzung Sie zeitweise unterbinden möchten, können Sie diese mit wenigen Klicks deaktivieren, um allen Nutzergruppen den Zugriff zu entziehen. Wie das geht, erfahren Sie [hier]({{< relref "help/app-builder/app-verwaltung/apps-zeitweise-deaktivieren" >}}).

## Eine App löschen

Eine App, die Sie nicht mehr benötigen, können Sie jederzeit **löschen**. Beachten Sie dabei, welche Konsequenzen die Löschung hat.

[Erfahren Sie hier mehr zur Löschung einer App.]({{< relref "help/app-builder/app-verwaltung/apps-loeschen" >}})

## Kein kollaboratives Arbeiten in Apps

Während die App viele Vorteile gegenüber der [Arbeit in der Base]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}) hat, gibt es einen großen Unterschied, wenn Sie gemeinsam im Team an den Daten arbeiten wollen. In einer Base wird Ihnen jede Änderung, die von anderen Anwendern ausgeführt wird, unmittelbar angezeigt. Die Einträge verändern sich in Echtzeit. Bei der App wird diese Art der kollaborativen Zusammenarbeit nicht unterstützt.

## Kommentare in Apps

Dennoch haben Sie die Möglichkeit, auch in einer App mit anderen Teammitgliedern zu kommunizieren. Nutzen Sie dazu die [Kommentarfunktion]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), die Sie bereits in gleicher Form aus der Base kennen. Halten Sie Ihr Feedback oder zusätzliche Informationen zu den Datensätzen für die anderen App-Nutzer fest und führen Sie Diskussionen an Ort und Stelle.

![Kommentarfunktion in Apps](images/Kommentarfunktion-in-Universellen-Apps.png)

{{< warning  headline="Gut zu wissen"  text="Die Kommentare in der App sind komplett **unabhängig** von den Kommentaren in der Base. Das heißt: Jeder Kommentar in der App ist nur dort zu sehen, wo er gepostet wurde – nicht in der Base und auch nicht in anderen Apps, selbst wenn es sich um den gleichen Datensatz handelt." />}}
