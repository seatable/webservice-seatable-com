---
title: 'Abfrageseiten in SeaTable Apps'
date: 2023-12-08
lastmod: '2025-02-27'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/de/hilfe/abfrageseiten-in-seatable-apps'
aliases:
    - '/de/hilfe/abfrageseiten-in-universellen-apps'
seo:
    title: 'Abfrageseiten in SeaTable Apps nutzen'
    description: 'Durchsuchen und filtern Sie große Datensätze in SeaTable Apps gezielt nach Werten: Filter, Sortierungen und Abfragefelder für individuelle Ergebnisse.'
weight: 9
---

Mithilfe dieses Seitentyps können Sie Ihre Datensätze über bestimmte Felder hinweg nach spezifischen Werten durchsuchen. Der Seitentyp erweist sich besonders bei **umfangreichen Datensätzen** wie Produktkatalogen oder Bibliotheken als hilfreich. Ein konkreter Anwendungsfall könnte beispielsweise die Abfrage eines Mitarbeiterverzeichnisses sein.

![Abfrageseiten in SeaTable Apps](images/Abfrageseiten-in-Universellen-Apps.png)

## Seiteneinstellungen

Wenn Sie die Einstellungen einer Seite ändern möchten, klicken Sie in der Navigation auf das entsprechende {{< seatable-icon icon="dtable-icon-set-up" >}} **Zahnrad-Symbol**.

![Einstellungen der Abfrageseite ändern](images/Einstellungen-der-Abfrageseite-aendern.png)

## Voreingestellte Filter, Sortierungen und ausgeblendete Spalten

In den **Seiteneinstellungen** definieren Sie zuerst die **Tabelle**, die durchsucht werden soll.

Daraufhin können Sie voreingestellte **Filter**, **Sortierungen** und **ausgeblendete Spalten** definieren, um die angezeigten Daten für die Nutzer einzugrenzen und zu ordnen. Zum Filtern oder Sortieren klicken Sie auf **Filter hinzufügen** oder **Sortierung hinzufügen**, wählen Sie die gewünschte **Spalte** und **Bedingung** aus und bestätigen mit **Abschicken**.

![Add filter on query pages](images/Add-filter-on-query-pages-in-Universal-Apps.png)

Die Nutzer können in den **Abfrageergebnissen** alle Informationen der zutreffenden Datensätze sehen, wenn Sie diese nicht einschränken. Entscheiden Sie daher, welche Daten **sichtbar** sein sollen, und blenden Sie die entsprechenden Spalten mithilfe der **Regler** ein oder aus.

![Hide columns on query pages](images/Hide-columns-on-query-pages-in-Universal-Apps.png)

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="**Voreingestellte Filter** und **ausgeblendete Spalten** können die App-Nutzer **nicht verändern**. Sie bekommen also, wie von Ihnen gewünscht, nur die gefilterten Einträge angezeigt. Die **Zeilenhöhe** und die **Sortierung** der abgefragten Datensätze können die Nutzer allerdings individuell anpassen." />}}

## Abfragefelder hinzufügen

Für diesen Seitentyp sind **Abfragefelder** von zentraler Bedeutung. Mit ihnen können die Nutzer die ausgewählten Tabellenspalten nach spezifischen Werten durchsuchen und so **Datensätze finden**. Klicken Sie in den Seiteneinstellungen auf {{< seatable-icon icon="dtable-icon-enlarge" >}} **Feld hinzufügen**, um ein Abfragefeld zu definieren.

![Felder auf Abfrageseiten hinzufügen](images/Felder-auf-Abfrageseiten-hinzufuegen.png)

Anschließend können Sie die gewünschte **Spalte** auswählen und einstellen, ob das Abfragefeld **erforderlich** sein soll, ob eine **unscharfe Suche** möglich ist und ob **Groß- und Kleinschreibung** bei der Eingabe berücksichtigt werden.

## Hinweis hinzufügen

Sie können Ihrer Abfrageseite einen einleitenden **Hinweis** hinzufügen, der zum Beispiel Erklärungen zum Ausfüllen der Abfragefelder enthalten kann. Aktivieren Sie dazu einfach den **Regler** in den Seiteneinstellungen und schreiben Sie den Hinweis in die erscheinende Textbox.

![Hinweis auf Abfrageseiten hinzufügen](images/Hinweis-auf-Abfrageseiten-der-Universellen-App-hinzufuegen.png)

## Abfrageergebnisse bearbeiten

Um diese Funktion nutzen zu können, müssen Sie in den Seiteneinstellungen bei **Ist das Abfrageergebnis bearbeitbar** den Regler **aktivieren**.

![Abfrageergebnis bearbeitbar machen](images/Abfrageergebnis-bearbeitbar-machen.png)

Anschließend können alle Nutzer mit Zugriff auf die Abfrageseite die gesuchten **Datensätze bearbeiten**.

![Abfrageergebnisse bearbeiten auf Abfrageseiten der App](images/Abfrageergebnisse-bearbeiten-auf-Abfrageseiten-der-App.gif)

- Führen Sie eine **erfolgreiche Datenabfrage** durch.
- Bewegen Sie Ihre Maus auf die **Zeilennummerierung** der Trefferliste und klicken Sie auf das **Doppelpfeil-Symbol** vor dem Datensatz, den Sie bearbeiten möchten.
- Nehmen Sie in den geöffneten **Zeilendetails** die gewünschten Änderungen vor.
- Klicken Sie auf das **x-Symbol**, um das Fenster zu schließen und Ihre Änderungen zu speichern.

{{< warning  type="warning" headline="Schreibgeschützte Spalten"  text="Sie können vorab Spalten definieren, die nicht bearbeitet werden können. Gehen Sie dazu in die Seiteneinstellungen und klicken Sie die Kästchen der Spalten an, die für die Nutzer **nur lesbar** sein sollen. Schreibgeschützte Spalten erkennen Sie daran, dass die Felder in den Zeilendetails grau hinterlegt sind." />}}

## Seitenberechtigungen

Ganz unten in den Seiteneinstellungen können Sie eingrenzen, wer die Abfrageseite sehen darf.

![Berechtigung für Abfrageseiten](images/Berechtigung-fuer-individuelle-Seiten-der-Universellen-App.png)

Das ist die einzige [Seitenberechtigung]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}), die Sie hier zur Auswahl haben. Über Abfrageseiten kann man keine Zeilen in der Tabelle hinzufügen oder löschen.

Allerdings können die Nutzer der App nach einer erfolgreichen Datenabfrage [Schaltflächen]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) in der angezeigten Trefferliste betätigen, um bestimmte **Aktionen auszuführen**.

![Schaltflächen auf Abfrageseiten ausführen](images/Schaltflaechen-auf-Abfrageseiten-ausfuehren.gif)

Ein Anwendungsbeispiel ist eine interne Stellenbörse: Die Abfrageseite erlaubt die schnelle Suche nach relevanten Positionen. Ist eine interessante Stelle dabei, dann reicht ein Klick auf die Schaltfläche in den Suchergebnissen, um sich direkt für die Stelle zu bewerben.

{{< warning  type="warning" headline="Achtung bei Schaltflächen" >}}

[Schaltflächen]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) können unabhängig von den Seitenberechtigungen **immer** betätigt werden. Dadurch kann jeder App-Nutzer bestimmte Änderungen an den Datensätzen ausführen, die Sie zuvor definiert haben, auch wenn die betroffenen Spalten ansonsten für ihn gesperrt sind oder der Nutzer nicht zur Bearbeitung der Abfrageergebnisse berechtigt ist.

{{< /warning >}}
