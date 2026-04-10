---
title: 'Apps löschen'
date: 2023-05-02
lastmod: '2024-02-16'
categories:
    - 'apps'
author: 'nsc2'
url: '/de/hilfe/apps-loeschen'
seo:
    title: 'Apps aus Ihrer SeaTable Base endgültig löschen'
    description: 'Entfernen Sie Apps, die Sie nicht mehr benötigen – schnell aus Ihrer Base löschen, mit Gruppenberechtigung. Die Daten im Hintergrund bleiben in Ihrer Tabelle erhalten.'

---

Sie möchten eine App, die Sie nicht mehr benötigen, aus Ihrer Base löschen? Kein Problem! Dies ist jederzeit mit nur wenigen Klicks möglich.

{{< warning  type="warning" headline="Berechtigung in der Gruppe erforderlich"  text="Um eine App löschen zu können, müssen Sie **Eigentümer** oder **Administrator der Gruppe** sein, in der sich die zugrundeliegende **Base** befindet. Einfache **Gruppenmitglieder** sind dazu nicht berechtigt." />}}

## Eine App aus einer Base löschen

1. Öffnen Sie die **Base**, in der Sie eine App löschen möchten.
1. Klicken Sie im Base-Header auf **Apps**.
   ![Klicken Sie im Base-Header auf Apps](images/click-apps-in-the-base-header.jpg)
1. Fahren Sie mit der Maus über die gewünschte App und klicken Sie rechts auf die **drei Punkte**.
1. Wählen Sie **Löschen** aus.
1. Bestätigen Sie mit **Löschen**.
   ![Eine App löschen](images/Delete-an-app.gif)

{{< warning  type="warning" headline="Die Löschung ist endgültig" >}}

Eine gelöschte App können Sie **nicht wiederherstellen**. Wenn Sie sich nicht sicher sind, ob Sie eine App zu einem späteren Zeitpunkt noch gebrauchen können, sollten Sie die App lieber [vorübergehend deaktivieren]({{< relref "help/app-builder/app-verwaltung/apps-zeitweise-deaktivieren" >}}).

{{< /warning >}}

## Folgen der Löschung

Das Wichtigste zuerst: **Durch das Löschen einer App gehen niemals Daten in der zugrundeliegenden Base verloren**. Technisch gesehen löschen Sie also nur eine Benutzeroberfläche und _nicht_ die Datenbank im Hintergrund.

Bitte beachten Sie aber, dass bei der Löschung einer **App** auch alle [Seiten und Ordner]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}), die sich in der App befinden, **unwiderruflich gelöscht** werden und _nicht_ wiederhergestellt werden können.

Bei der Löschung einer **Galerie-App** werden _ausschließlich_ die in der App dargestellten **Galerien** gelöscht, die **Bilder** hingegen bleiben weiterhin in den [Bild-Spalten]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) Ihrer Tabellen erhalten.

Auch bei der Löschung einer **Datenabfrage-App** werden **keinerlei Daten** gelöscht, sondern nur die **Suchmaske**.
