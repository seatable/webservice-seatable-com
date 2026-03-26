---
title: 'Microsoft 365 für den Versand von E-Mails per SMTP einrichten'
date: 2023-04-28
lastmod: '2025-03-07'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'nsc2'
url: '/de/hilfe/microsoft-365-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Microsoft 365 mit SeaTable: E-Mail-Versand per SMTP und OAuth2 einrichten'
    description: 'So richten Sie Microsoft 365 für den sicheren E-Mail-Versand per SMTP in SeaTable ein: Schritt-für-Schritt Anleitung zu Authentifizierung, App-Registrierung und Integration.'
---

**Microsoft 365**, der beliebte Online-Dienst für Microsofts Office-Anwendungen, kann für den **Versand von E-Mails aus SeaTable** verwendet werden. Die Authentifizierung gegenüber Ihrem Microsoft 365 muss mittels Microsofts moderner Authentifizieung erfolgen. (Die Authentifizierung über Benutzername und Benutzer-Passwort ist bei Microsoft 365 nicht möglich.)

{{< warning headline="Outlook E-Mail-Konten" text="Diese Anleitung erklärt das Vorgehen anhand eines Microsoft 365 Kontos. Das Vorgehen gilt aber genauso für kostenlose Outlook E-Mail-Konten." />}}

## Vorbereitung im Entra Admin Center

Um Ihren Microsoft 365 Account in SeaTable für den E-Mail Versand nutzen zu können, müssen Sie im Entra Admin Center von Microsoft zunächst eine Anwendung anlegen und konfigurieren.

1. Melden Sie sich am [Microsoft Entra Admin Center](https://entra.microsoft.com/) an. Der Benutzer braucht Admin-Rechte für das Konto, das für den Versand verwendet werden soll.
2. Klicken Sie in der Seitennavigation auf **App-Registrierungen** .
3. Erstellen sie eine neue Anmeldung durch Klick auf **\+ Neue Registrierung**. Geben Sie einen Namen ein (z.B. 'SeaTable') und wählen Sie **Alle Konten von Entra ID-Mandanten und persönliche Microsoft Konten** als Kontotyp. Registrieren Sie die folgende Umleitungs-URI für eine Anwendung vom Typ **Web**:

    ```
    https://cloud.seatable.io/oauth/third-party-email-accounts/callback/
    ```

    Wenn Sie nicht SeaTable Cloud verwenden, dann ersetzen Sie cloud.seatable.io durch den Hostname Ihrer SeaTable Instanz. Schließen Sie die Anlage der App-Registrierung mit Klick auf **Registrieren** ab.

4. Notieren Sie die **Anwendungs-ID (Client)** auf der Übersichtsseite der gerade registrierten App. Diese wird für die Einrichtung des E-Mail-Kontos in SeaTable benötigt.
5. Um den Clientschlüssel zu erzeugen, navigieren Sie in der Navigation der App zu **Zertifikate und Geheimnisse**. Klicken Sie auf **Neuer geheimer Clientschlüssel**. Vergeben Sie für den Schlüssel eine Beschreibung und ein Ablaufdatum.

    ![Creating a client secret for a registered app in Microsoft Entra](images/Creating_Client_Secret_Microsoft_Entra.gif)

6. Kopieren Sie den Wert des erstellten Schlüssels in die Zwischenablage.

Damit haben Sie alle Vorbereitungen getroffen, um Ihren Microsoft 365 Account als E-Mail-Konto in SeaTable nutzen zu können.

## Anlage des E-Mail-Kontos in SeaTable

Nun müssen Sie Ihren Microsoft 365 Account in Ihrer SeaTable Base hinzufügen. Dazu sind die folgenden Schritte notwendig:

1. Öffnen Sie die erweiterten Base-Optionen mit einem Klick auf das **Drei-Punkte-Icon** {{< seatable-icon icon="dtable-icon-more-level" >}} in der rechten oberen Ecke.
2. Wählen Sie die Option **Integration von Drittanbietern** aus.
   ![Integration von Drittanbietern über die erweiterten Base-Optionen](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)
3. Klicken Sie auf **E-Mail-Konto hinzufügen**.
4. Wählen Sie als Diensteanbieter **Microsoft (Microsoft 365 und Outlook)**.
5. Geben Sie die folgenden Informationen ein und klicken dann auf **Abschicken** in der rechten oberen Ecke:
    - **Kontoname**: Eine kurze Beschreibung des Kontos, z.B. 'Microsoft 365'
    - **Client-ID**: die Anwendungs-ID (Client) der erstellten App
    - **Clientschlüssel**: der geheime Clientschlüssel der erstellten App
6. Erteilen Sie die angeforderten Berechtigungen, indem Sie auf **Akzeptieren** klicken.
   ![Screencast accept permissions requested](images/Accept-Permissions-Requested-Microsoft.gif)

## E-Mails per Automatisierungsregel oder Schaltfläche versenden

Danach können Sie das in Ihrer SeaTable Base angelegte E-Mail-Konto verwenden, um E-Mails per [Automatisierung]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) oder Schaltfläche zu verschicken.

Wenn Sie mehr über diese nützliche Funktion erfahren wollen, lesen Sie den Artikel [Einrichtung eines E-Mail-Kontos in einer Base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).
