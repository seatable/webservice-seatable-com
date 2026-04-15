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

Termine in einer SeaTable Base lassen sich automatisch mit einem oder mehreren **Google Kalendern** synchronisieren. So haben Sie Ihre aktuellen Termine immer in Ihrem Google Kalender auf Ihrem PC und Ihren Mobilgeräten parat.

Bevor Sie die Terminsynchronisation konfigurieren, müssen Sie das **Google Konto** des Kalenders, in den Sie Termine übertragen wollen, in SeaTable einrichten. Dies erfolgt in zwei Schritten: Zunächst erzeugen Sie in der Google Cloud Console **OAuth-Zugangsdaten**. Dann legen Sie in SeaTable mit den Zugangsdaten ein Drittanbieterkonto an und verbinden es mit Google. Mit dieser Schritt-für-Schritt-Anleitung ist dies ganz leicht.

## Erstellung der Zugangsdaten in der Google Cloud Console

Als Plattform für Entwickler wirkt die Google Cloud Console für normale Benutzer zunächst unübersichtlich. Lassen Sie sich davon nicht beeindrucken. Mit der folgenden Schritt-für-Schritt-Anleitung schaffen Sie die Einrichtung ohne Kopfzerbrechen.

1. Öffnen Sie die [Google Cloud Console](https://console.cloud.google.com/) und loggen Sie sich in Ihr **Google Konto** ein, wenn Sie dazu aufgefordert werden.
2. Klicken Sie oben neben dem Google Cloud-Logo auf **Projekt auswählen** und erstellen Sie ein **neues Projekt**. In diesem werden alle nachfolgend erläuterten Einstellungen vorgenommen. 
   ![Projektauswahl in Google Cloud](images/GoogleConsole_CreateNewProject_723.png)
3. Geben Sie einen **Projektnamen** ein (z. B. SeaTable Base XY) und wählen Sie den **Speicherort** aus. Wenn keine Organisationen definiert sind, behalten Sie "Keine Organisation" bei. Bestätigen Sie mit **Erstellen**.
   ![Neues Projekt in Google Cloud Console erstellen](images/GoogleConsole_NewProject_723.png)
4. Erlauben Sie dem erstellten Projekt die Nutzung der Google Kalender API. Klicken Sie dafür mit der Maus in das **Suchfeld** am oberen Seitenrand, geben Sie **Google Calendar API** ein und klicken Sie auf das entsprechende Suchergebnis. Aktivieren Sie dann die Google Calendar API.
   ![Google Calendar API aktivieren](images/GoogleConsole_EnableCalendarAPI_722.gif)
5. Klicken Sie auf das Burger-Menü-Icon in der linken oberen Ecke, um die Navigation einzublenden, und wählen Sie dann in der Rubrik "Lösungen" die Option **Alle Produkte**. Auf der Produktseite klicken Sie auf **Google Auth Platform**.
   ![Google Auth Plattform aufrufen](images/GoogleConsole_SwitchAuthPlatform_722.gif)
6. Nehmen Sie die notwendigen Konfigurationen an der Google Auth Platform vor, indem Sie auf **Erste Schritte** klicken: Geben Sie einen **Anwendungsnamen** und eine **Support-E-Mail-Adresse** (z. B. Ihre Gmail Adresse) an. Als Zielgruppe wählen Sie **Extern** aus. Tragen Sie eine **Kontakt-E-Mail-Adresse** (z. B. Ihre Gmail Adresse) ein. Akzeptieren Sie die **Nutzungsbedingungen** und schließen Sie die Konfiguration ab.
7. Klicken Sie in der Seitennavigation der Google Auth Platform auf **Zielgruppe**. Fügen Sie Ihre Google E-Mail-Adresse als **Testnutzer** hinzu.
8. Klicken Sie in der Seitennavigation der Google Auth Platform auf **Clients** und erstellen Sie einen OAuth 2.0-Client. Wählen Sie als **Anwendungstyp** für den OAuth-Client die Option "Webanwendung" und geben Sie einen **Namen** ein (z. B. SeaTable). Überspringen Sie "Autorisierte JavaScript-Quellen" und fügen Sie als **Autorisierte Weiterleitungs-URI** folgende URI ein, bevor Sie auf **Erstellen** klicken:

    ```
    https://cloud.seatable.io/oauth/google-calendar/callback/
    ```

    Wenn Sie statt SeaTable Cloud ein eigenes System verwenden, dann ersetzen Sie cloud.seatable.io durch den Hostnamen Ihrer SeaTable Instanz.

   ![OAuth-Client erstellen](images/GoogleConsole_CreateClient_722.gif)

9. Der neu angelegte Client wird nun in der Liste der OAuth 2.0 Clients angezeigt. Die Einstellungen des Clients lassen sich mit einem Klick auf dessen Namen anzeigen. Die angezeigte **Client-ID** und der **Clientschlüssel** sind für die folgende Einrichtung in SeaTable essentiell.

{{< warning headline="Keine Panik" text="Wenn Sie sich während der Konfiguration verklickt haben und nicht mehr wissen, wo Sie sind, dann klicken Sie auf das Burger-Menü-Icon oben links. Von dort aus können Sie über **Kürzlich aufgerufen** wieder zur Google Auth Platform navigieren." />}}

## Anlegen des Google Kontos in SeaTable

Nun müssen Sie Ihr Google Konto als **Drittanbieterkonto in Ihrer SeaTable Base** hinzufügen. Dazu sind die folgenden Schritte notwendig:

1. Öffnen Sie die erweiterten Base-Optionen mit einem Klick auf das **Drei-Punkte-Icon** {{< seatable-icon icon="dtable-icon-more-level" >}} in der rechten oberen Ecke.
   ![Menü für die Drittanbieterintegration öffnen](images/third-party-integration.png)
2. Wählen Sie die Option **Integration von Drittanbietern** aus.
3. Klicken Sie links in der Navigation auf **Google Calendar** und dann rechts oben auf **Google Kalender Konto hinzufügen**.
   ![Google Calendar Konto hinzufügen](images/add-google-calendar-account-in-seatable.png)
4. Geben Sie die folgenden Informationen ein:
    - **Kontoname**: ein beliebiger Name für das Konto, z. B. Google
    - **Client-ID**: die Client-ID des erstellten OAuth-Clients
    - **Clientschlüssel**: der Clientschlüssel des erstellten OAuth-Clients
5. Nachdem Sie auf **Abschicken** geklickt haben, öffnet sich ein Browser-Fenster. Klicken Sie auf **Weiter**, wenn Sie darauf hingewiesen werden, dass diese App nicht überprüft wurde, und erlauben Sie den Zugriff auf das Google Konto.
6. Das erstellte Konto finden Sie über denselben Weg unter **Google Kalender Konten**.

## Termine automatisch in Google Kalender übertragen

Wenn Sie das Google Konto eingerichtet haben, können Sie automatisch Termine von SeaTable in Ihren Google Cloud Kalender übertragen und aktualisieren lassen. Die Konfiguration der Datenübertragung von SeaTable in Google Kalender erfolgt über eine entsprechende [Aktion]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) in einer Automatisierungsregel.
