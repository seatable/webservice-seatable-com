---
title: 'Kartenseiten in Apps'
date: 2026-04-07
lastmod: '2026-04-07'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/de/hilfe/kartenseiten-in-apps'
seo:
    title: 'Kartenseiten in Apps: Orte auf Weltkarte visualisieren'
    description: 'Erstellen Sie Kartenseiten in SeaTable Apps: Geopositionsdaten und Adressen flexibel auf einer Weltkarte visualisieren.'
weight: 9
---

Mithilfe dieses Seitentyps können Sie **Orte**, die Sie anhand von **Geopositionsdaten oder Adressen** in Ihrer Tabelle gespeichert haben, auf einer **Weltkarte** innerhalb der App anzeigen lassen.

![Darstellung von Orten auf einer Karte](images/map-page-app-builder.png)

## Seiteneinstellungen

Wenn Sie die Einstellungen einer Seite ändern möchten, klicken Sie in der Navigation auf das entsprechende {{< seatable-icon icon="dtable-icon-set-up" >}} **Zahnrad-Symbol**.

![Einstellungen der Kartenseite ändern](images/access-page-settings.png)

In den **Seiteneinstellungen** können Sie den **Kartentyp** (Standard oder Bilder), die **Tabelle** und eine Spalte für die **Adresse** und die **Pin-Farbe** auswählen. Bitte beachten Sie, dass nur bestimmte Spaltentypen für diese Informationen in Frage kommen.

![Seiteneinstellungen der Kartenseite in Apps](images/map-page-settings.png)

Wenn Sie eine **anzuzeigende Spalte** festlegen, wird dauerhaft eine Beschriftung der Orte auf der Karte angezeigt.

![Anzuzeigende Spalte der Kartenseite in Apps](images/map-page-display-field.png)

Sie können aber auch flexibel anzuzeigende Spalten festlegen, die erst durch einen **Hover-Effekt** sichtbar werden. Aktivieren Sie die Regler der Spalten, die zu sehen sein sollen, wenn Sie mit der Maus über einen Pin fahren.

![Hover-Effekt der anzuzeigenden Spalten auf der Kartenseite](images/map-page-hover-display.gif)

## Voreingestellte Filter und ausgeblendete Spalten

Darüber hinaus können Sie voreingestellte Filter und ausgeblendete Spalten definieren, um die angezeigten Daten einzugrenzen. Zum Filtern klicken Sie auf **Filter hinzufügen**, wählen die gewünschte **Spalte** und **Bedingung** aus und bestätigen mit **Abschicken**.

![Filter auf Kartenseiten](images/map-page-filters.png)

Blenden Sie die Spalten, die nicht für die Kartenseite zur Verfügung stehen sollen, mithilfe der **Regler** aus.

![Spalten bei Kartenseiten ausblenden](images/hide-columns-on-map-pages.png)

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="**Voreingestellte Filter** und **ausgeblendete Spalten** können die App-Nutzer **nicht verändern**. Sie bekommen also, wie von Ihnen gewünscht, nur die gefilterten Einträge angezeigt." />}}

## Seitenberechtigungen

Für Kartenseiten können Sie lediglich eine [Seitenberechtigung]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) festlegen – nämlich, wer die Kartenseite sehen darf. Dies liegt daran, dass Sie auf Kartenseiten **keine Zeilen hinzufügen, bearbeiten oder löschen** können.
