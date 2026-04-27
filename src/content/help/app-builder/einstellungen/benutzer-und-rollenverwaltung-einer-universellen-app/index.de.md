---
title: 'Benutzer- und Rollenverwaltung einer App'
date: 2023-05-02
lastmod: '2024-12-13'
categories:
    - 'universelle-apps'
author: 'nsc2'
url: '/de/hilfe/benutzer-und-rollenverwaltung-einer-universellen-app'
seo:
    title: 'Benutzer- und Rollenverwaltung in der App'
    description: 'Lernen Sie, wie Sie Benutzer hinzufügen, Rollen vergeben und Einladungslinks verwalten in der App von SeaTable.'
---

Sei es das Hinzufügen von **neuen Benutzern**, die Vergabe von **Rollen** oder das Erstellen von **Einladungslinks** – in der Benutzer- und Rollenverwaltung einer App können Sie diverse administrative Tätigkeiten durchführen. Sie erreichen die **Benutzer- und Rollenverwaltung** über den Bearbeitungsmodus Ihrer App.

{{< warning  type="warning" headline="Berechtigung in der Gruppe erforderlich"  text="Um eine App bearbeiten zu können, müssen Sie **Eigentümer** oder **Administrator der Gruppe** sein, in der sich die zugrundeliegende **Base** befindet. Einfache **Gruppenmitglieder** können die Apps lediglich ansehen und nutzen." />}}

## Benutzer- und Rollenverwaltung der App

1. Öffnen Sie eine **Base**, der Sie bereits eine App hinzugefügt haben.
2. Klicken Sie im Base-Header auf **Apps**.
   ![Klicken Sie im Base-Header auf Apps](images/click-apps-in-the-base-header.jpg)4. Fahren Sie mit der Maus über die App und klicken Sie auf das **Stift-Symbol** {{< seatable-icon icon="dtable-icon-rename" >}}.
   ![Klicken Sie auf das Bearbeitung-Symbol](images/add-page-to-universal-app-1.png)6. Öffnen Sie die **Benutzer- und Rollenverwaltung** am oberen linken Seitenrand.

![Symbol für Benutzer- und Rollenverwaltung](images/Symbol-fuer-Benutzer-und-Rollenverwaltung.png) 8. Nehmen Sie die gewünschten **Einstellungen** vor.

## Die Einstellungen im Detail

### Benutzer

Im ersten Abschnitt finden Sie eine Übersicht aller **Benutzer**, die Zugriff auf Ihre App besitzen. Zusätzlich finden Sie hier auch die **Rolle** und den **Status** des jeweiligen Benutzers.

![Übersicht über den Reiter Benutzer der Benutzer- und Rollenverwaltung einer App](images/user-and-role-management-overview-1.png)

In diesem Abschnitt stehen Ihnen zudem diverse Möglichkeiten zur **Verwaltung der aktuellen Benutzer** Ihrer App zur Verfügung.

Nutzen Sie die **Suchfunktion**, um einen bestimmten Benutzer zu finden. Diese Funktion kann vor allem bei einer großen Zahl an App-Benutzern hilfreich sein.

![Suchfunktion für App-Benutzer](images/search-function-app-users.png)

Um einen Benutzer zur App hinzuzufügen, klicken Sie auf **Benutzer importieren**, suchen ihn über das Eingabefeld und weisen ihm im Anschluss eine Rolle zu.

![Klicken Sie auf Benutzer importieren ](images/import-user-to-app.jpg)

![Import eines Benutzers zu Ihrer App](images/import-users-to-app.png)

Klicken Sie auf **Benutzer mit der Base synchronisieren**, um die **App-Benutzer** automatisch in einer Tabelle Ihrer Base zu erheben.

![Klicken Sie auf Benutzer mit der Basis synchronisieren](images/click-sync-users-to-base-1.jpg) ![Tabelle, in der automatisch die App-Benutzer erhoben werden](images/table-with-app-users.png)

Wenn Sie zukünftig weitere Benutzer auf diese Weise hinzufügen, können Sie stets erneut auf **Benutzer mit der Base synchronisieren** klicken, um die **neuen Benutzer** der Tabelle hinzuzufügen.

![Wenn Sie in Zukunft weitere Benutzer zu Ihrer App hinzufügen, ...](images/if-you-add-more-users-to-your-app.png)

![... können Sie stets erneut auf Benutzer mit der Base synchronisieren klicken, um die neuen Benutzer automatisch der Tabelle hinzuzufügen.](images/added-imported-app-users-to-table.png)

Um einen Benutzer aus der App zu **löschen**, klicken Sie einfach auf das **X-Symbol**, welches Sie rechts neben dem Status des jeweiligen Benutzers finden.

![Benutzer löschen](images/delete-user.jpg)

Durch Klick auf die **Stift-Symbole** {{< seatable-icon icon="dtable-icon-rename" >}}, die Sie für jeden Benutzer finden, können Sie dessen **Rolle** und **Status** bearbeiten.

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="Bitte beachten Sie, dass der **Benutzer**, der die App zur Base hinzugefügt hat, automatisch als **Admin** registriert wird. Sowohl Rolle als auch Status dieses Benutzers können **nicht** bearbeitet werden und der Nutzer kann auch **nicht** aus der App entfernt werden." />}}

![Bearbeitungs-Symbole für jeden Benutzer ](images/edit-icons-users.jpg)

Für die **Rolle eines Benutzers** stehen Ihnen im Drop-down-Menü alle Rollen zur Auswahl, die Sie im nächsten Abschnitt der Benutzer- und Rollenverwaltung definieren können.

![Auswahl der Rolle eines Benutzers ](images/select-role-of-user.png)

Der **Status** eines Benutzers kann jeweils auf **Aktiv** oder **Inaktiv** gesetzt werden. Während **aktive** Nutzer Zugriff auf die App und deren Inhalte besitzen, verlieren diesen **inaktive** Nutzer.

![Bearbeitung des Status eines App-Benutzers](images/edit-status-of-app-user.png)

Nutzer, die keinen Zugriff auf Ihre App haben, sehen diese Meldung:

![Verweigerter Zugriff auf die App für inaktive Benutzer ](images/no-permission-for-inactive-users.png)

### Rollen

In diesem Abschnitt können Sie eine beliebige Anzahl an **Rollen** definieren, die Sie im Abschnitt darüber den verschiedenen App-Nutzern zuweisen können.

![Definition von verschiedenen Rollen für die App-Nutzer ](images/define-roles-for-app-users.jpg)

Hier legen Sie zunächst nur die **Namen** der Rollen fest. Welche **Berechtigungen** Nutzer mit den verschiedenen Rollen haben, können Sie individuell für jede Seite der App definieren.

[Erfahren Sie hier mehr über die Seitenberechtigungen.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

### Einladungslink

Im dritten Abschnitt der Benutzer- und Rollenverwaltung können Sie einen individuellen **Einladungslink** für die App generieren.

Legen Sie dabei zunächst die **Rolle** der Benutzer fest, welche mithilfe des Einladungslinks auf die App zugreifen.

![Auswahl der Rolle, die der Benutzer erhalten wird, der mithilfe des Einladungslinks die App nutzen wird](images/select-role-for-invite-link.png)

Im Anschluss haben Sie die Möglichkeit, ein **Passwort** festzulegen, das nach dem Öffnen des Einladungslinks eingegeben werden muss, um Zugriff auf die App zu erhalten.

![Hinzufügen eines Passworts zum Einladungslink](images/add-password-protection.png)

Optional können Sie dem Einladungslink auch noch eine automatische **Ablaufzeit** hinzufügen, wie lange dieser gültig ist.

![Automatische Ablaufzeit zum Einladungslink hinzufügen ](images/add-auto-expiration.png)

Mit einem Klick auf **Generieren** können Sie den Einladungslink erstellen lassen. Der Link wird Ihnen im Anschluss unten angezeigt und Sie haben die Möglichkeit, diesen zu **kopieren** oder zu **löschen**.

![Generierter Einladungslink samt verfügbarer Optionen zum Kopieren und Löschen des Einladungslinks](images/copy-and-delete-link-universal-app.png)

Alternativ haben Sie die Möglichkeit, sich einen **QR-Code** zum Öffnen und Teilen der App generieren zu lassen.

![Anzeigen des QR-Codes zum Öffnen und Teilen der App](images/show-qr-code-universal-app.png)

Scannen Sie den angezeigten **QR-Code**, um Ihre App zu öffnen, oder teilen Sie ihn mit anderen Nutzern, um ihnen **Zugriff** auf Ihre App zu gewähren.

![QR-Code zum Öffnen und Teilen der App](images/qr-code-to-share-universal-app.png)
