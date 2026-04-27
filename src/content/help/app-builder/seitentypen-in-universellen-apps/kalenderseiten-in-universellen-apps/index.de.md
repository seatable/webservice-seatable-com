---
title: 'Kalenderseiten in SeaTable Apps'
date: 2023-12-04
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/de/hilfe/kalenderseiten-in-seatable-apps'
aliases:
    - '/de/hilfe/kalenderseiten-in-universellen-apps'
seo:
    title: 'Kalenderseiten in SeaTable Apps: Meetings & Planung'
    description: 'Kalenderseiten in SeaTable Apps: Termine & Projekte im Kalender verwalten, filtern & bearbeiten.'
weight: 5
---

Dieser Seitentyp ermöglicht es Ihnen, die Einträge aus einer oder zwei [Datum-Spalten]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) Ihrer Tabelle in einem **Kalender** anzeigen zu lassen. Ein konkreter Anwendungsfall könnte beispielsweise die kalendarische Darstellung von bevorstehenden **Meetings** sein.

![Bevorstehende Meetings in einer Kalenderansicht der Kalenderseite](images/calendar-page-example.png)

## Seiteneinstellungen

Wenn Sie die Einstellungen einer Seite ändern möchten, klicken Sie in der Navigation auf das entsprechende {{< seatable-icon icon="dtable-icon-set-up" >}} **Zahnrad-Symbol**.

![Einstellungen der Kalenderseite ändern](images/Einstellungen-auf-der-Kalenderseite-aendern.png)

In den **Seiteneinstellungen** können Sie unter anderem den **Titel**, das **Startdatum** und die **Farbe** der im Kalender angezeigten **Einträge** auswählen sowie den **Tag des Wochenstarts** festlegen.

![Seiteneinstellungen des Seitentyps: Kalender ](images/page-settings-calendar-page.png)

## Voreingestellte Filter und ausgeblendete Spalten

Sie können **voreingestellte Filter** und **ausgeblendete Spalten** definieren, um die angezeigten Daten für die Nutzer einzugrenzen.

![Add filter on calendar pages](images/Add-filter-on-calendar-pages-in-Universal-Apps.png)

Klicken Sie dazu auf **Filter hinzufügen**, wählen Sie die gewünschte **Spalte** und **Bedingung** aus und bestätigen Sie mit **Abschicken**.

Die Nutzer können sich mehr Informationen zu einem Termin anzeigen lassen, indem sie auf einen Kalendereintrag klicken.

![Kalendereinträge in der App öffnen](images/Kalendereintraege-in-der-Universellen-App-oeffnen.gif)

Entscheiden Sie daher, welche Daten **sichtbar** sein sollen, und blenden Sie die entsprechenden Spalten mithilfe der **Regler** ein oder aus.

![Hide columns on calendar pages](images/Hide-columns-on-calendar-pages-in-Universal-Apps.png)

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="**Voreingestellte Filter** und **ausgeblendete Spalten** können die App-Nutzer **nicht verändern**. Sie bekommen also, wie von Ihnen gewünscht, nur die gefilterten Daten angezeigt." />}}

## Kalendereintrag hinzufügen

Wenn Sie die entsprechende Berechtigung besitzen, können Sie direkt auf einer Kalenderseite **neue Einträge hinzufügen**. In der Monatsansicht klicken Sie dazu auf das kleine **Plus-Symbol** in der oberen rechten Ecke einer Kachel. Das **Datum** dieses Tages ist dann bereits vorausgefüllt.

Unabhängig vom Datum können Sie ebenso auf das große **kreisförmige Plus-Symbol** in der unteren rechten Seitenecke klicken. Anschließend öffnet sich ein Fenster mit den **Zeilendetails**. Erfassen Sie dort alle gewünschten Daten und speichern Sie den Eintrag, indem Sie auf **Abschicken** klicken.

![Kalendereintrag in einer App hinzufügen](images/Kalendereintrag-hinzufuegen.gif)

## Kalendereinträge bearbeiten und verschieben

Sie können Kalendereinträge kinderleicht bearbeiten, indem Sie **auf einen Eintrag klicken** und in den sich öffnenden **Zeilendetails** die gewünschten Änderungen vornehmen. Zusätzlich können Sie Einträge im Kalender komfortabel **per Drag-and-Drop verschieben**. Dabei passt SeaTable automatisch die Werte in den jeweiligen [Datum-Spalten]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) an.

![Einträge auf Kalenderseiten verschieben und bearbeiten](images/Eintraege-auf-Kalenderseiten-verschieben-und-bearbeiten.gif)

## Einstellungen der Verknüpfungsspalte

In den **Einstellungen der Verknüpfungsspalte** können Sie für jede verknüpfte Tabelle festlegen, welche Daten sichtbar und welche Operationen erlaubt sind.

![Link column settings on calendar pages](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Feldeinstellungen**: Hier können Sie genau definieren, für welche Spalten die folgenden Berechtigungen gelten.
- **Hinzufügen neuer Einträge erlauben**: Wenn Sie diesen Regler aktivieren, können Nutzer neue Einträge in der verknüpften Tabelle hinzufügen. Über die Feldeinstellungen können Sie definieren, welche Spalten dabei **sichtbar** und welche Spalten **erforderlich** sind, also ausgefüllt werden müssen.
- **Verknüpfen bestehender Einträge erlauben**: Wenn Sie diesen Regler aktivieren, können Nutzer bestehende Einträge der verknüften Tabelle verlinken. Über die Feldeinstellungen können Sie definieren, welche Spalten dabei **sichtbar** sind.
- **Verknüpfungen auf maximal eine Zeile begrenzen**: Wenn Sie diesen Regler aktivieren, können Nutzer in den Zellen der Verknüpfungsspalte nur noch jeweils eine Zeile der verknüpften Tabelle verlinken.
- **Voreingestellte Filter**: Wenn Sie hier einen Filter hinzufügen, werden beim Verlinken von Einträgen nur Optionen angezeigt, die die Filterbedingungen erfüllen.
- **Big-Data-Funktion aktivieren**: Wenn die Big-Data-Funktion aktiviert ist, können Nutzer mehr als 20.000 Datensätze durchsuchen, sofern in der verknüpften Tabelle so viele Einträge vorhanden sind.
- **Verknüpfte Einträge bearbeiten**: Wenn Sie diesen Regler aktivieren, können Nutzer bestehende Einträge der verknüften Tabelle bearbeiten. Über die Feldeinstellungen können Sie definieren, welche Spalten dabei **bearbeitbar** sind.

## Seitenberechtigungen

Ganz unten in den Seiteneinstellungen können Sie genau eingrenzen, welche Nutzer mit der Seite interagieren dürfen. Legen Sie fest, wer die Seite sehen, Zeilen hinzufügen oder Einträge ändern darf.

![Seitenberechtigungen auf Kalenderseiten](images/Seitenberechtigungen-auf-Kalenderseiten.png)
