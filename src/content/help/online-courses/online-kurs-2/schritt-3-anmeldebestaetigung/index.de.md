---
title: 'Schritt 3: Anmeldebestätigung'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/de/hilfe/schritt-3-anmeldebestaetigung'
seo:
    title: 'Schritt 3: Anmeldebestätigung per E-Mail'
    description: 'Erfahren Sie, wie Sie mit SeaTable Anmeldebestätigungen und Zahlungsaufforderungen per E-Mail an Kursteilnehmer versenden.'
---

Nun fügen wir die Funktion hinzu, dass Teilnehmer, die sich für einen Kurs angemeldet haben, eine Anmeldebestätigung sowie eine Zahlungsaufforderung per E-Mail erhalten.

## E-Mailversand mit SeaTable

Um E-Mails mit SeaTable zu verschicken, müssen Sie zunächst ein E-Mail-Konto in der Base hinterlegen. Da die Konfiguration je nach Anbieter unterschiedlich ist, empfehlen wir die Nutzung von [mailtrap](https://mailtrap.io). _Mailtrap_ ermöglicht es Ihnen, E-Mails in ein virtuelles Postfach zu senden, was den Vorteil hat, dass keine E-Mails an reale oder fiktive Kunden versendet werden – Sie können jedoch den E-Mail-Versand realitätsnah simulieren.

{{< warning type="warning" headline="Welcher E-Mail-Anbieter ist der richtige für mich" text="Es gibt keinen _richtigen_ oder _falschen_\> E-Mail-Anbieter. Wenn Sie nur wenige E-Mails pro Tag versenden, reicht Ihr bestehendes E-Mail-Konto wahrscheinlich aus. Bei steigendem E-Mail-Volumen sollten Sie jedoch einen professionellen Anbieter wie [Brevo.com](https://brevo.com) in Betracht ziehen, der es Ihnen ermöglicht, die Zustellung der E-Mails besser nachzuverfolgen." />}}

### Ein Mailtrap-Konto erstellen

Um loszulegen, besuchen Sie die [Registrierungsseite von Mailtrap](https://mailtrap.io/register/signup) und erstellen Sie ein kostenloses Konto.

![Mailtrap-Registrierungsseite mit Formular zur Kontoerstellung](images/lvl2-mailtrap.png)

Bestätigen Sie Ihre E-Mail-Adresse und loggen Sie sich ein. Nach einigen Fragen zu Ihren Interessen – diese sind für den weiteren Verlauf nicht relevant – gelangen Sie zur Startseite von _Mailtrap_.

![Mailtrap-Startseite mit vorkonfigurierter Inbox „My Inbox“](images/lvl2-mailtrap-inbox.png)

Klicken Sie im linken Menü auf `E-Mail Testing > Inboxes`. Dort finden Sie bereits eine vorkonfigurierte Inbox mit dem Namen `My Inbox`. Die dazugehörigen SMTP-Zugangsdaten benötigen Sie für die Konfiguration in SeaTable.

![SMTP-Zugangsdaten der Inbox „My Inbox“ für die Verwendung in SeaTable](images/lvl2-mailtrap-smtp-credentials.png)

### E-Mail-Versand in SeaTable konfigurieren

Mit den SMTP-Zugangsdaten von Mailtrap können Sie nun den [E-Mail-Versand in SeaTable]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}) einrichten.

![Dialog in SeaTable mit eingetragenen Mailtrap-SMTP-Daten für den E-Mail-Versand](images/lvl2-mailtrap-in-seatable.png)

Die E-Mails werden nicht wirklich versendet, sondern erscheinen in Ihrem Mailtrap-Postfach. Testen Sie dies, indem Sie eine E-Mail an einen beliebigen Empfänger schicken – sie landet ausschließlich in Ihrem virtuellen Mailpostfach.

![Beispiel-E-Mail im Mailtrap-Postfach zur Kontrolle des SeaTable-Versands](images/lvl2-mailtest.gif)

## E-Mail an den Kunden senden

Jetzt können wir in der Tabelle `Registrations` eine neue Spalte für den E-Mail-Versand anlegen. Verwenden Sie die folgenden Einstellungen:

> Name: beliebig Spaltentyp: `{{< seatable-icon icon="dtable-icon-button" >}} Button`
>
> Label: `Send`
>
> Action: `{{< seatable-icon icon="dtable-icon-email" >}} Send email`
>
> Betreff: `Confirmation: Course {Registered for}`
>
> Empfänger: `customer@example.com`

![SeaTable-Tabelle mit Button-Spalte „Send“ für den E-Mail-Versand an Teilnehmer](images/lvl2-create-button.png)

Für den Nachrichtentext können Sie folgende Textvorlage verwenden:

> Hey, Thank you for registering for the course {Registered for} on {Date}.
>
> To complete your registration, please transfer the course fee using the details below:
>
> Amount: {Price} Bank: Example Bank LTD IBAN: XYZ
>
> We appreciate your prompt payment!
>
> Best regards

Beim einfachen Texteditor werden die Platzhalter in geschweiften Klammern automatisch ersetzt. Wenn Sie den Rich-Text-Editor verwenden, müssen Sie die Platzhalter manuell über die Funktion `{{< seatable-icon icon="dtable-icon-choose-column " >}} Insert column` einfügen.

![Rich-Text-Editor in SeaTable mit Platzhaltern für Kurs- und Datumsangaben](images/lvl2-rich-text-editor.png)

Klicken Sie anschließend auf d0ie Schaltfläche und prüfen Sie, ob die E-Mail in Ihrem Mailtrap-Postfach erscheint.

Glückwunsch! Sie haben soeben Ihre erste E-Mail über SeaTable verschickt – auch wenn sie nur in das virtuelle Postfach von Mailtrap ging.

{{< warning  type="warning" headline="E-Mails automatisch versenden"  text="Derzeit wird der E-Mail-Versand noch per Klick auf eine Schaltfläche ausgelöst. Das kann auch eine Automation übernehmen: Automationen sind Thema von Kurs 4." />}}

## Hilfeartikel mit weiteren Informationen

- [Einrichten eines E-Mail-Kontos in einer Base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}})
- [Gmail für den Versand von e-Mails per SMTP einrichten]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}})
- [Die Schaltfläche]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
- [Eine E-Mail per Schaltfläche verschicken]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [E-Mail per Automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
