---
title: 'Seiten vom Typ Einzelner Datensatz in SeaTable Apps'
date: 2024-07-26
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/de/hilfe/seiten-vom-typ-einzelner-datensatz-in-seatable-apps'
aliases:
    - '/de/hilfe/seiten-vom-typ-einzelner-datensatz-in-universellen-apps'
seo:
    title: 'Einzelner Datensatz in SeaTable Apps – Übersicht'
    description: 'Gestalten Sie detailreiche Einzelseiten für Datensätze in SeaTable: statische Elemente, Filter, Rechte, Anzeige- und Bearbeitungsoptionen.'
weight: 11
---

Mit dem [Seitentyp]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) **Einzelner Datensatz** haben Sie die Möglichkeit, eine Seite mit statischen Elementen, dynamischen Tabellenfeldern, Farben, Rahmen etc. zu designen, um **die in einer Zeile gespeicherten Daten** optisch aufzubereiten.

Die Nutzer der App können auf dieser Seite – mit der jeweiligen Berechtigung – die einzelnen Datensätze sehen, suchen und durchblättern oder sogar bearbeiten. Dieser Seitentyp eignet sich zum Beispiel, um die Daten in einer Mitarbeiterdatenbank als persönliche Steckbriefe anzuzeigen.

![Single Record Page](images/Single-Record-Page-min.gif)

## Seiteneinstellungen

Wenn Sie die Einstellungen einer Seite ändern möchten, klicken Sie in der Navigation auf das entsprechende {{< seatable-icon icon="dtable-icon-set-up" >}} **Zahnrad-Symbol**.

![Einstellungen der Galerieseite ändern](images/Einstellungen-der-Galerieseite-aendern.png)

In den **Seiteneinstellungen** können Sie die **Tabelle** auswählen, in der die einzelnen Datensätze gespeichert sind.

### Statische Elemente

Ähnlich wie auf [Dashboard-Seiten]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}) können Sie auch auf Seiten des Typs Einzelner Datensatz **statische Elemente** hinzufügen, die zur Gestaltung der Seite dienen und über alle Datensätze hinweg gleich bleiben. Diese Elemente sind:

- Text
- Formatierter Text
- Horizontale Linie
- Bild
- Container
- Karte

![Statische Elemente des Seitentyps Einzelner Datensatz](images/Statische-Elemente-des-Seitentyps-Einzelner-Datensatz.png)

Für genauere Informationen zu den **Einstellungsmöglichkeiten** dieser Elemente konsultieren Sie bitte [diesen Hilfeartikel]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}).

### Tabellenfelder

Als Tabellenfelder sind alle Spalten der Tabelle aufgelistet, aus denen Sie Daten in die Seite einbauen können. Der Inhalt der Felder hängt von den einzelnen Datensätzen in der Tabelle ab und ändert sich je nach Eintrag.

Ebenso wie die statischen Elemente verfügt auch jedes Tabellenfeld über eigene **Elementeinstellungen**. Wählen Sie zunächst aus, ob Sie den **Feldnamen anzeigen** möchten, der als Überschrift des Eintrags dient. Wenn ja, können Sie die **Ausrichtung**, die **Schriftgröße**, **Schriftstärke** und **Schriftfarbe** exakt einstellen.

Außerdem können Sie für jedes Tabellenfeld eine **Hintergrundfarbe** und einen **Rahmen** festlegen.

![Element settings of a table field on Single Record Pages](images/Element-settings-of-a-table-field-on-Single-Record-Pages-in-the-Universal-App.png)

Bei allen text- und zahlenbasierten Spaltentypen haben Sie auch die Möglichkeit, die **Schriftgröße, Schriftstärke, Schriftfarbe und Ausrichtung der angezeigten Werte** einzustellen.

Zudem gibt es ein paar Besonderheiten bei folgenden Spaltentypen:

- Wenn Sie auf eine E-Mail-Adresse in einer **E-Mail-Spalte** klicken, öffnet sich der auf Ihrem Gerät installierte E-Mail-Client (z. B. Microsoft Outlook oder Mozilla Thunderbird).
- Wenn Sie auf einen Link in einer **URL-Spalte** klicken, öffnet sich die entsprechende Internetseite in einem neuen Tab Ihres Browsers.
- Wenn Sie auf ein Miniatursymbol in einer **Datei-Spalte** klicken, öffnet sich die Datei in einem geeigneten Viewer in einem neuen Tab Ihres Browsers. Auch Office-Dokumente können Sie, sofern ein Online Office Editor konfiguriert ist, direkt im Browser öffnen und bearbeiten.
- Bei **Verknüpfungsspalten** lassen sich alle mit dem Datensatz verknüpften Einträge übersichtlich in einer Tabelle darstellen. Sie können die Spaltenbreite anpassen und über die Elementeinstellungen auch Spalten ausblenden, sodass nur die wesentlichen Informationen der verknüpften Einträge angezeigt werden.

![Link columns on Single Record pages](images/link-columns-on-single-record-pages.png)

## Elemente kopieren, verschieben oder löschen

Wenn Sie ein bestehendes Element auf Ihrer Seite kopieren, verschieben oder löschen möchten, nutzen Sie einfach die drei entsprechenden **Symbole** an der oberen rechten Ecke des Rahmens.

![Copy, move and delete elements on custom pages](images/Copy-move-and-delete-elements-on-custom-pages.gif)

## Voreingestellte Filter und Sortierungen

Darüber hinaus können Sie voreingestellte Filter und Sortierungen definieren, um die anzeigbaren Datensätze für die Nutzer einzugrenzen und zu ordnen. Zum Filtern oder Sortieren klicken Sie auf **Filter hinzufügen** oder **Sortierung hinzufügen**, wählen Sie die gewünschte **Spalte** und **Bedingung** aus und bestätigen mit **Abschicken**.

![Add filters on Single Record pages](images/Add-filters-on-Single-Record-pages-in-Universal-Apps.png)

Die Nutzer können nur die Informationen zu einem einzelnen Datensatz sehen, die Sie über die eingebundenen Tabellenfelder anzeigen lassen.

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="**Voreingestellte Filter** und **Sortierungen** können die App-Nutzer **nicht verändern**. Sie bekommen also, wie von Ihnen gewünscht, nur die gefilterten Einträge in einer festen Reihenfolge angezeigt." />}}

## Grafische Einstellungen des Seitenhintergrunds

Folgende grafische Einstellungen können Sie für die gesamte Seite des Typs Einzelner Datensatz vornehmen:

- Wählen Sie Weiß, Grau oder eine benutzerdefinierte Farbe als **Hintergrundfarbe** der Seite.
- Stellen Sie die **Seitenränder** (oben, unten, links, rechts) ein.
- Entscheiden Sie, ob Sie die **Titelleiste ausblenden** möchten.
- Entscheiden Sie, ob Sie die **Toolbar ausblenden** möchten, mit der die Nutzer zwischen den Einträgen wechseln können.

![Seitenhintergrund-Einstellungen von Seiten des Typs Einzelner Datensatz](images/Seitenhintergrund-Einstellungen-von-Seiten-des-Typs-Einzelner-Datensatz.png)

## Zwischen den Einträgen wechseln

Wenn Sie die Toolbar eingeblendet haben, können die App-Nutzer mit der entsprechenden Seitenberechtigung zwischen den einzelnen Datensätzen wechseln. Klicken Sie dazu auf {{< seatable-icon icon="dtable-icon-left" color="grey" >}} **Vorheriger Eintrag** oder **Nächster Eintrag** {{< seatable-icon icon="dtable-icon-right" color="grey" >}}. Sie können auch gezielt einen {{< seatable-icon icon="dtable-icon-search" color="grey" >}} **Eintrag suchen**.

![Switch between records on single record pages](images/Switch-between-records-on-single-record-pages.gif)

## Eintrag bearbeiten

Mit der entsprechenden Berechtigung können App-Nutzer auf dieser Seite die einzelnen Datensätze bearbeiten.

![Modify record on single record pages](images/Modify-record-on-single-record-pages.gif)

- Klicken Sie in der Toolbar auf **Eintrag bearbeiten**.
- Das Fenster mit den **Zeilendetails** öffnet sich. Nehmen Sie dort die gewünschten Änderungen am Datensatz vor.
- Schließen Sie das Fenster mit einem Klick auf das **x-Symbol**, um die Änderungen zu speichern.

## QR-Code für einzelne Einträge generieren

In der Toolbar finden Sie außerdem einen **QR-Code-Generator**. Der QR-Code enthält den Link auf den aktuell angezeigten Eintrag. Auf einem Gegenstand oder Gerät angebracht, können Sie den QR-Code über ein Tablet oder Smartphone scannen und ohne jede Tastatureingabe alle Daten in der App abrufen. Dadurch wird beispielsweise die [Inventarverwaltung]({{< relref "templates/operations/inventory-list" >}}) noch einfacher.

![More design options on single record page in SeaTable 5.1](images/SingleRecordPage.png)

## Schaltflächen-Aktionen ausführen

Genau wie auf Tabellen- und Abfrageseiten können Sie auch hier Spalten vom Typ [Schaltfläche]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) nutzen. Ob Sie ein PDF-Dokument erstellen, einen Datensatz bearbeiten oder ein Skript ausführen möchten – all diese **Schaltflächen-Aktionen** können Sie per Knopfdruck starten. Eine Bearbeitungsberechtigung ist dafür **nicht** notwendig. Auf diese Weise können App-Admins die Benutzerinteraktionen für diesen Seitentyp auf einige vordefinierte Aktionen beschränken.

## Einstellungen der Verknüpfungsspalte

In den **Einstellungen der Verknüpfungsspalte** können Sie für jede verknüpfte Tabelle festlegen, welche Daten sichtbar und welche Operationen erlaubt sind.

![Link column settings on single record pages](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Feldeinstellungen**: Hier können Sie genau definieren, für welche Spalten die folgenden Berechtigungen gelten.
- **Hinzufügen neuer Einträge erlauben**: Wenn Sie diesen Regler aktivieren, können Nutzer neue Einträge in der verknüpften Tabelle hinzufügen. Über die Feldeinstellungen können Sie definieren, welche Spalten dabei **sichtbar** und welche Spalten **erforderlich** sind, also ausgefüllt werden müssen.
- **Verknüpfen bestehender Einträge erlauben**: Wenn Sie diesen Regler aktivieren, können Nutzer bestehende Einträge der verknüften Tabelle verlinken. Über die Feldeinstellungen können Sie definieren, welche Spalten dabei **sichtbar** sind.
- **Verknüpfungen auf maximal eine Zeile begrenzen**: Wenn Sie diesen Regler aktivieren, können Nutzer in den Zellen der Verknüpfungsspalte nur noch jeweils eine Zeile der verknüpften Tabelle verlinken.
- **Voreingestellte Filter**: Wenn Sie hier einen Filter hinzufügen, werden beim Verlinken von Einträgen nur Optionen angezeigt, die die Filterbedingungen erfüllen.
- **Big-Data-Funktion aktivieren**: Wenn die Big-Data-Funktion aktiviert ist, können Nutzer mehr als 20.000 Datensätze durchsuchen, sofern in der verknüpften Tabelle so viele Einträge vorhanden sind.
- **Verknüpfte Einträge bearbeiten**: Wenn Sie diesen Regler aktivieren, können Nutzer bestehende Einträge der verknüften Tabelle bearbeiten. Über die Feldeinstellungen können Sie definieren, welche Spalten dabei **bearbeitbar** sind.

## Seitenberechtigungen

Für Seiten vom Typ Einzelner Datensatz können Sie folgende [Seitenberechtigungen]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) festlegen:

![Seitenberechtigungen von Kalenderseiten](images/Seitenberechtigungen-von-Kalenderseiten.png)

Entscheiden Sie, wer die einzelnen Datensätze **sehen** und **bearbeiten** darf. Über diese Seite können Sie keine Zeilen in der Tabelle hinzufügen oder löschen.

{{< warning  type="warning" headline="Achtung bei Schaltflächen" >}}

[Schaltflächen]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) können unabhängig von den Seitenberechtigungen **immer** betätigt werden. Dadurch kann jeder App-Nutzer bestimmte Änderungen an den Datensätzen ausführen, die Sie zuvor definiert haben, auch wenn die betroffenen Spalten ansonsten für ihn gesperrt sind oder der Nutzer nicht zur Bearbeitung der Seite berechtigt ist.

{{< /warning >}}

## Schreibgeschützte Spalten

Zusätzlich zur Seitenberechtigung “Wer darf Zeilen bearbeiten?” können Sie mithilfe von schreibgeschützten Spalten präzise festlegen, welche Spaltenwerte eines Datensatzes die Benutzer ändern können und welche nicht.

![Read-only columns on single record pages](images/Read-only-columns-on-single-record-pages.png)

Gehen Sie in die **Seiteneinstellungen** und klicken Sie die **Kästchen** der Spalten an, die für die Nutzer **nur lesbar** sein sollen. Schreibgeschützte Spalten erkennen Sie daran, dass sie in den Zeilendetails **grau** hinterlegt sind.
