---
title: 'Seitenberechtigungen in einer App'
date: 2023-05-03
lastmod: '2023-11-30'
categories:
    - 'universelle-apps'
author: 'nsc2'
url: '/de/hilfe/seitenberechtigungen-in-einer-universellen-app'
seo:
    title: 'Seitenberechtigungen in der App – Anleitung'
    description: 'Lernen Sie, wie Sie Seitenberechtigungen in SeaTable Apps festlegen, bearbeiten und Rollen präzise steuern.'
---

{{< required-version "Enterprise" >}}

Um den **Zugriff auf Ihre Daten** genau zu steuern, können Sie für jede Seite, die Sie in einer App angelegt haben, **individuelle Seitenberechtigungen** festlegen. Die Bearbeitung der Berechtigungen erfolgt über die Seiteneinstellungen.

{{< warning  type="warning" headline="Standard-Seitenberechtigung"  text="Wenn Sie **neue Seiten** in Ihrer App anlegen, gewähren diese zunächst allen Benutzern alle verfügbaren Rechte. Wollen Sie jedoch die Nutzungsrechte einschränken, ist die Anpassung der Seitenberechtigungen erforderlich." />}}

## Seitenberechtigungen festlegen und bearbeiten

1. Öffnen Sie eine **Base**, der Sie bereits eine App hinzugefügt haben.
2. Klicken Sie im Base-Header auf **Apps**.
   ![Klicken Sie im Base-Header auf Apps](images/click-apps-in-the-base-header.jpg)
3. Fahren Sie mit der Maus über die App und klicken Sie auf das **Stift-Symbol** {{< seatable-icon icon="dtable-icon-rename" >}}.
   ![Klicken Sie auf das Bearbeitungs-Symbol](images/add-page-to-universal-app-1.png)
4. Wählen Sie aus der Navigation am linken Seitenrand die gewünschte **Seite** aus und klicken Sie auf das **Zahnrad-Symbol** {{< seatable-icon icon="dtable-icon-set-up" >}}.
   ![Klick auf das Bearbeitungs-Symbol](images/page-permissions-universal-app.png)
5. Legen Sie in den am rechten Seitenrand erschienenen **Seiteneinstellungen** die gewünschten **Berechtigungen** fest.
   ![Festlegung der Seitenberechtigungen](images/page-permissions.png)
6. Die definierten Seitenberechtigungen werden **automatisch** gespeichert und **unmittelbar** übernommen.

## Welche Seitenberechtigungen es gibt

Folgende Seitenberechtigungen können Sie einstellen:

- Wer darf Zeilen hinzufügen?
- Wer darf Zeilen bearbeiten?
- Wer darf Zeilen löschen?
- Wer kann die Seite sehen?

Nicht alle Berechtigungen sind für alle [Seitentypen]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) verfügbar. Hier ein Überblick:

| Seitentyp           | Zeilen hinzufügen                                             | Zeilen bearbeiten                                             | Zeilen löschen                                                | Seite sehen                                                   |
| ------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| Tabelle             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Formular            | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Galerie             | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Kalender            | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Dashboard           | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Kanban              | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Zeitstrahl          | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Abfrage             | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Einzelner Datensatz | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} | {{< icon "circle-xmark" >}}                                   | {{< icon icon="circle-check" class="text-seatable-orange" >}} |

## Welche Benutzergruppen Sie berechtigen können

Für jede Berechtigung stehen Ihnen folgende Optionen zur Auswahl, mit denen Sie den Personenkreis eingrenzen können: **Niemand**, **Administratoren**, **Bestimmte Rollen** und **Jeder**.

![Verfügbare Optionen der Seitenberechtigung Wer kann die Seite sehen?](images/page-permission-who-can-add-records.png)

Wählen Sie die Option **Bestimmte Rollen** aus, um selbst definierte Rollen festzulegen. Dazu erstellen Sie zuvor in der [Benutzer- und Rollenverwaltung]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}) neue **Rollen** für einzelne Nutzergruppen, denen Sie auf jeder Seite der App individuell Berechtigungen zuweisen können.

![Definition von bestimmten Rollen, die über eine entsprechende Berechtigung verfügen](images/define-roles.png)
