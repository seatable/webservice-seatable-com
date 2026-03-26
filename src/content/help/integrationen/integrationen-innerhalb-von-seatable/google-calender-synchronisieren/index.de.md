---
title: 'Termine in SeaTable mit einem Google Kalender synchronisieren'
date: 2026-03-23
lastmod: '2026-03-23'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'rdb'
url: '/de/hilfe/termine-mit-google-kalender-synchronisieren'
seo:
    title: 'Termine in SeaTable mit einem Google Kalender synchronsieren'
    description: 'Schritt-für-Schritt-Anleitung zur Synchronisation von Daten in SeaTable mit einem Google Kalender.'
---

Termine in einer SeaTable Base lassen sich automatisch mit einem oder mehreren **Google Kalendern** synchronisieren. So haben Sie Ihre aktuellen Termine immer in Ihrem Google Kalender auf Ihrem Android (und auch anderen) Mobilgeräten.

Bevor Sie die Terminsynchronisation konfigurieren, müssen Sie das Google Kontos des Kalenders, in den Sie Termine übertragen wollen, in SeaTable einrichten. Dies erfolgt in zwei Schritten: Zunächst erzeugen Sie in der Google Cloud Console OAuth Zugangsdaten. Dann legen Sie in SeaTable mit den Zugangsdaten ein Drittanbieterkonto an und verbinden es mit Google. Mit dieser Schritt-für-Schritt-Anleitung ist dies für jedermann gut machbar.

### Erstellung der Zugangsdaten in der Google Cloud Console

Als Platform für Entwickler wirkt die Cloud Console für normale Benutzer unübersichtlich. Lassen Sie sich davon nicht beeindrucken. Mit der folgenden Schritt-für-Schritt-Anleitung ist die Einrichtung für jedermann machbar.

1. Öffnen Sie die [Google Cloud Console](https://console.cloud.google.com/) und loggen Sie sich in Ihr **Google Konto** ein, wenn Sie dazu aufgefordert werden.
   ![Projektauswahl in Google Cloud](images/GoogleConsole_CreateNewProject_723.png)
2. Erstellen Sie zunächst ein neues Projekt. In diesem werden alle nachfolgend erläuterten Einstellungen vorgenommen. Geben Sie einen Projektnamen ein (z.B. 'SeaTable') und wählen Sie den Speicherort aus. (Wenn keine Organisationen definiert sind, behalten Sie "Keine Organisation" bei.)
   ![Neues Projekt in Google Cloud Console erstellen](images/GoogleConsole_NewProject_723.png)
3. Erlauben Sie dem erstellten Projekt die Nutzung der Google Kalender API. Klicken Sie dafür mit der Maus in das Suchfeld am oberen Bildschirmrand, geben 'Google Calendar API' ein und klicken dann auf das entsprechende Suchergebnis. Aktivieren Sie die Google Calendar API.
   ![Google Calendar API aktivieren](images/GoogleConsole_EnableCalendarAPI_722.gif)
4. Alle weiteren Schritte erfolgen in der **Google Auth Platform**. Klicken Sie auf das Sandwich-Icon in der linken oberen Ecke und wählen dann "Alle Produkte" in der Rubrik "Lösungen". Auf der Produkteseite klicken Sie auf "Google Auth Platform".
   ![Google Auth Plattform aufrufen](images/GoogleConsole_SwitchAuthPlatform_722.gif)
5. Nehmen Sie die **notwendigen Konfigurationen** an der Google Auth Platform vor: Geben Sie einen Anwendungsnamen, eine Support- und eine Kontakt-E-Mail-Adresse ein (z.B. Ihre Gmail Adresse). Als Zielgruppe wählen Sie "Extern" aus. Akzeptieren Sie die Nutzungsbedingungen und schließen Sie die Konfiguration ab.
6. Klicken Sie in der Seitennavigation der Google Auth Platform auf **Zielgruppe**. Fügen Sie Ihre Google E-Mail-Adresse als Testnutzer hinzu.
7. Klicken Sie in der Seitennavigation der Google Auth Platform auf **Clients** und erstellen einen OAuth 2.0-Client. Wählen Sie als Anwendungstyp für den OAuth-Client "Webanwendung" und geben Sie einen Namen ein (z.B. 'SeaTable'). Überspringen Sie die "Autorisierte JavaScript-Quellen" und fügen Sie als "Autorisierte Weiterleitungs-URI" folgende URI ein:

    ```
    https://cloud.seatable.io/oauth/google-calendar/callback/
    ```

    Wenn Sie nicht SeaTable Cloud verwenden, dann ersetzen Sie cloud.seatable.io durch den Hostname Ihrer SeaTable Instanz. Scrollen Sie ans Ende der Seite und bestätigen Sie die Erstellung des OAuth-Clients.

![OAuth-Client erstellen](images/GoogleConsole_CreateClient_722.gif)

8. Der neu angelegte Client wird nun in der Liste der OAuth 2.0 Clients angezeigt. Die Einstellungen des Clients lassen sich mit einem Klick auf dessen Namen anzeigen. Die angezeigte Client-ID und der Clientschlüssel sind für die folgende Einrichtung in SeaTable essentiell.

Wenn Sie während der Konfiguration verklickt haben und nicht mehr wissen, wo Sie sind, dann klicken Sie auf das Sandwich-Icon oben rechts. Von dort können Sie wieder zur Google Auth Platform navigieren.

### Anlage des Google Kontos in SeaTable

Nun müssen Sie Ihr Google Mail-Konto als Drittanbieterkonto in Ihrer SeaTable Base hinzufügen. Dazu sind die folgenden Schritte notwendig:

1. Öffnen Sie die erweiterten Base-Optionen mit einem Klick auf das **Drei-Punkte-Icon** {{< seatable-icon icon="dtable-icon-more-level" >}} in der rechten oberen Ecke.
2. Wählen Sie die Option **Integration von Drittanbietern** aus.
3. Klicken Sie in der Navigation links auf **Google Calendar**.
4. Klicken Sie auf **Google Kalender-Konto hinzufügen**.
5. Geben Sie die folgenden Informationen ein:

    - **Kontoname**: ein beliebiger Name für das Konto, z.B. 'Gmail'
    - **Client-ID**: die Client-ID des erstellten OAuth-Clients
    - **Clientschlüssel**: der Clientschlüssel des erstellten OAuth-Clients

6. Klicken Sie auf **Weiter**, wenn Sie darauf hingewiesen werden, dass diese App nicht überprüft wurde und erlauben Sie den Zugriff auf das Google Konto.

## Termine automatisch in Google Kalender übertragen

Wenn Sie das Google Konto eingerichtet haben, dann können Sie automatisch Termine aus SeaTable in Ihren Google Cloud Kalender übertragen und aktualisieren lassen. Die Konfiguration der Datenübertragung von SeaTable in Google Kalender erfolgt über eine entsprechende Aktion in einer Automatisierungsregel.
