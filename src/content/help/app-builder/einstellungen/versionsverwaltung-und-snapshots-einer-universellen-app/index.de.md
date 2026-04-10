---
title: 'Versionsverwaltung und Snapshots einer App'
date: 2023-11-29
lastmod: '2024-02-16'
categories:
    - 'universelle-apps'
author: 'kgr'
url: '/de/hilfe/versionsverwaltung-und-snapshots-einer-universellen-app'
seo:
    title: 'Versionsverwaltung & Snapshots in der App'
    description: 'Erfahren Sie, wie Sie mit Snapshots Versionen Ihrer App speichern, anzeigen, wiederherstellen und verwalten, um Änderungen sicher nachzuvollziehen.'
---

Mithilfe von **Snapshots** können Sie die aktuelle Version einer App speichern. Snapshots können Sie in der Versionsverwaltung des SeaTable App Builders **erstellen**, **ansehen**, **wiederherstellen** und **löschen**. Zudem können Sie **Hinweise** zu den einzelnen Snapshots notieren, um Informationen zu einer Version festzuhalten.

{{< warning  type="warning" headline="Berechtigung in der Gruppe erforderlich"  text="Um App Snapshots nutzen zu können, müssen Sie **Eigentümer** oder **Administrator der Gruppe** sein, in der sich die zugrundeliegende **Base** befindet. Einfache **Gruppenmitglieder** haben keinen Zugriff auf die Versionsverwaltung." />}}

## Wann App Snapshots sinnvoll sind

App Snapshots sind **Momentaufnahmen** vom Zustand einer App und funktionieren ähnlich wie [Base Snapshots]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}}). Mithilfe von App Snapshots können Sie die aktuelle Version einer App als Sicherheitskopie speichern, was zum Beispiel sinnvoll sein kann, wenn Sie umfangreiche Änderungen vornehmen und eventuell einen früheren Zustand wiederherstellen möchten.

{{< warning  type="warning" headline="Achtung vor Datenverlust"  text="Im Gegensatz zu Base Snapshots speichern App Snapshots **keine Datensätze**, sondern nur die **Struktur** und **Einstellungen** der App. Das heißt: Wenn Sie über die App bestimmte Einträge in der zugrundeliegenden Base verändern oder löschen, können Sie diese nicht über die App Snapshots wiederherstellen." />}}

### Was ein App Snapshot speichert

Ein App Snapshot speichert folgende Elemente und Einstellungen:

- [Einstellungen]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) wie **Name**, **Icon** und **Farbschema** der App
- [Seiten und Ordner]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) der App
- Einstellungen und [Berechtigungen]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) für die einzelnen Seiten

### Was ein App Snapshot nicht speichert

Ein App Snapshot speichert nicht:

- die **benutzerdefinierte URL** einer App
- die **Daten** der zugrundeliegenden Base
- die **Kommentare** zu einzelnen Datensätzen
- die [Benutzerrollen und Einladungslinks]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}) der App

## App Snapshot erstellen

1. Öffnen Sie eine **App** im [Bearbeitungsmodus]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}).
   ![SeaTable App Builder im Bearbeitungsmodus mit geöffneter App-Liste](images/Apps-bearbeiten.png)3. Klicken Sie am oberen linken Seitenrand auf {{< seatable-icon icon="dtable-icon-history" >}} **Versionsverwaltung**.
   ![Versionsverwaltung einer App mit Liste vorhandener Snapshots](images/Version-management-in-Universal-App-Builder.png)5. Ein Fenster öffnet sich. Erstellen Sie dort einen **neuen Snapshot**.
2. Optional können Sie dem Snapshot einen **Hinweis** hinzufügen.
3. Bestätigen Sie mit **Abschicken**.

![Erstellung eines neuen App-Snapshots in der Versionsverwaltung mit optionalem Hinweistext](images/Version-management-in-Universal-Apps.gif)

{{< warning  headline="Nummerierung der Versionen"  text="Für jeden Snapshot wird die genaue **Erstellungszeit** und eine **Versionsnummer** erfasst. Wundern Sie sich nicht, wenn Ihre Snapshots keine aufeinanderfolgenden Nummern (1, 2, 3 …) erhalten. SeaTable zählt jede Änderung, die Sie in einer App vornehmen, als eigene Version. Dadurch können schnell Dutzende Versionen zwischen zwei Snapshots liegen." />}}

Sobald Sie einen Snapshot angelegt haben, stehen Ihnen vier Operationen zur Auswahl:

- **Version anschauen**
- **Version wiederherstellen**
- **Hinweis**
- **Version löschen**

## App Snapshot anschauen

Bevor Sie einen Snapshot wiederherstellen und voreilig zu einer anderen Version zurückspringen, sollten Sie sich diese Version zunächst anschauen. Dazu nehmen Sie den gleichen Weg wie oben: Klicken Sie auf die **drei Punkte** am rechten Ende eines Snapshots und wählen Sie im Drop-down-Menü die Operation **Version anschauen** aus.

![Vorschau einer gespeicherten App-Version im SeaTable App Builder](images/Preview-version-of-app-snapshot.png)

## App Snapshot wiederherstellen

Um einen App Snapshot wiederherzustellen, klicken Sie auf die **drei Punkte** und wählen im Drop-down-Menü die entsprechende Operation aus.

![Dialog zur Wiederherstellung eines App-Snapshots als aktuelle Version](images/Restore-version-of-app-snapshot.png)

{{< warning  type="warning" headline="Achtung"  text="Die Snapshot-Wiederherstellung im SeaTable App Builder funktioniert anders als in der Base, wo der Snapshot in einer neuen Base wiederhergestellt wird und die aktuelle Version erhalten bleibt. **Im SeaTable App Builder hingegen wird die aktuelle Version verworfen, wenn Sie einen Snapshot wiederherstellen.**" />}}

Sobald Sie einen Snapshot wiederherstellen, wird die App auf den Speicherstand dieser früheren Version zurückgesetzt. Alle **Änderungen**, die Sie seitdem an Seiten, Ordnern und Einstellungen der App vorgenommen haben, **gehen verloren**. Daher ist es ratsam, vor der Wiederherstellung eines Snapshots auch die aktuelle Version in einem Snapshot zu speichern. So können Sie zwischen verschiedenen Versionen hin- und herspringen.

## Hinweis bearbeiten

Falls Sie den Hinweis zu einer Version nachträglich hinzufügen, ändern oder löschen möchten, können Sie dies jederzeit tun. Sie öffnen das entsprechende Textfeld, indem Sie auf die **drei Punkte** am rechten Ende eines Snapshots klicken und im Drop-down-Menü **Hinweis** auswählen. Speichern Sie Ihre Änderungen mit **Abschicken**.

![Dialog zum Bearbeiten oder Hinzufügen eines Hinweises zu einem App-Snapshot](images/Modify-notes-of-app-snapshot.png)

## App Snapshot löschen

Einen Snapshot, den Sie nicht mehr benötigen, können Sie jederzeit löschen. Klicken Sie auf die **drei Punkte** am rechten Ende eines Snapshots und wählen Sie im Drop-down-Menü die Operation **Version löschen** aus.

![Bestätigungsdialog zum endgültigen Löschen eines App-Snapshots](images/Delete-version-of-app-snapshot.png)

{{< warning  type="warning" headline="Achtung"  text="Die Löschung eines App Snapshots ist endgültig. Der Speicherstand der früheren Version geht unwiderruflich verloren und kann nicht wiederhergestellt werden." />}}
