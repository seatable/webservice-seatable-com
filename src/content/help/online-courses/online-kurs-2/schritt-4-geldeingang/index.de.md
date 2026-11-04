---
title: 'Schritt 4: Geldeingang'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/de/hilfe/schritt-4-geldeingang'
seo:
    title: 'Schritt 4 im SeaTable Kurs 2: Geldeingang per Button'
    description: 'Im vierten Kursschritt erstellen Sie mit SeaTable eine Schaltfläche, die Zahlungseingänge dokumentiert und eine Bestätigungs­mail automatisiert versendet.'
---

Nachdem Ihre Kursteilnehmer die Zahlungsaufforderung per E-Mail erhalten haben, überweisen diese die Kursgebühr auf Ihr Bankkonto. Die Überprüfung des Geldeingangs werden wir an dieser Stelle nicht weiter automatisieren. Dennoch wäre es sinnvoll, eine zusätzliche Schaltfläche in Ihrer Base zu integrieren, die zwei Aufgaben übernimmt:

1. Bestätigung des Geldeingangs und damit die vollständige Registrierung des Teilnehmers für den Kurs.
2. Dokumentation des Zahlvorgangs in der Base.

## Mehrere Aktionen in einer Schaltfläche

Das ist in SeaTable einfach umsetzbar. Fügen Sie in der Tabelle `Registrations` eine neue Schaltfläche hinzu, die zwei Aktionen ausführt:

- Eine E-Mail mit einer Zahlungsbestätigung an den Teilnehmer senden.
- Den `Payment Status` auf `Paid` setzen.

Mit Ihrem neu erworbenen Wissen sollte dies kein Problem darstellen. Den folgenden Text können Sie für Ihre E-Mail verwenden:

> Subject: Payment Confirmation and Online Meeting Details
>
> Hey,
>
> Thank you for your payment! We're excited to confirm that we've successfully received it.
>
> You can join the online meeting using the link below: - https://meet.jit.si/{Course-ID}
>
> We look forward to seeing you there! Best regards

## Hilfeartikel mit weiteren Informationen

- [Einrichtung eines E-Mail-Kontos in einer Base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}})
- [Gmail für den Versand von E-Mails per SMTP einrichten]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}})
- [Die Schaltfläche]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
- [Eine E-Mail per Schaltfläche verschicken]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [E-Mail-Versand per Automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
