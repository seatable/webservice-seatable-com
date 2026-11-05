---
title: 'Deaktivierung eines Webhooks bei Fehlern'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/de/hilfe/deaktivierung-eines-webhooks-bei-fehlern'
seo:
    title: 'Webhook deaktivieren bei Fehlern: SeaTable Anleitung'
    description: 'Erfahren Sie, wie Webhooks in SeaTable bei HTTP-Fehlercodes automatisch deaktiviert werden und wie Sie ungültige Webhooks wieder aktivieren.'

---

Wenn für eine SeaTable Base ein Webhook eingerichtet ist, schickt SeaTable bei jeder Änderung einen _POST-Request_ an die Ziel-URL. Normalerweise liefert das empfangende System eine Statusmeldung in Form eines [dreistelligen Status-Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) zurück, welche SeaTable dann verarbeitet und ggf. den Webhook deaktiviert.

## Die häufigsten HTTP-Status Codes

Es gibt eine ganze Reihe von Status Codes, aber es genügt, die häufigsten Rückmeldungen zu kennen:

- **200** - Successful
- **400** - Bad request
- **403** - Forbidden
- **500 - 511** - Server errors

Der mit Abstand wichtigste Status Code ist 200. Dieser besagt, dass die Anfrage empfangen und erfolgreich verarbeitet wurde. SeaTable wertet alle Status Codes von 200 bis 299 als Erfolg.

## SeaTable deaktiviert Webhooks bei Fehlern

Wenn SeaTable einen Webhook verschickt, erwartet SeaTable eine Rückmeldung in Form eines solchen HTTP-Statuscodes. Bei Fehlern wird der Webhook auf den Status _invalid_ gesetzt und die Ausführung unterbrochen. Wann das passiert, hängt von der Art des Fehlers ab:

| Fehler | Beispiele | Deaktivierung |
| ------ | --------- | ------------- |
| **Fehlerhafte oder ausbleibende Antwort** | Status Code außerhalb von 200 bis 299, keine Antwort innerhalb von 30 Sekunden | nach fünf Fehlern in Folge |
| **Keine Zustellung möglich** | Name nicht auflösbar, Verbindung abgelehnt, Zertifikatsfehler, nicht öffentliche Ziel-URL | sofort beim ersten Fehler |

Weiterleitungen werden nicht verfolgt: Ein Status Code wie 301 oder 302 zählt als Fehler. Eine erfolgreiche Zustellung setzt den Fehlerzähler zurück.

![Ungültiger Webhook](images/invalid-webhook.png)

{{< warning headline="Nur öffentliche Ziel-URLs seit Version 7.0.10" text="Seit Version 7.0.10 von SeaTable muss die Ziel-URL auf eine öffentliche Adresse zeigen. Webhooks an interne Adressen werden nicht zugestellt und sofort deaktiviert." />}}

## Fehlgeschlagene Zustellungen werden nicht wiederholt

SeaTable schickt einen Webhook nicht erneut, wenn die Zustellung fehlschlägt. Auch Änderungen, die anfallen, während ein Webhook deaktiviert ist, werden nicht nachgeliefert. Wenn Ihr System lückenlose Daten benötigt, sollten Sie die Daten deshalb [regelmäßig abgleichen]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).

## Einen inaktiven Webhook wieder aktivieren

Ein ungültiger Webhook kann jederzeit wieder aktiviert werden. Wechseln Sie in die Bearbeitung des ungültigen Webhooks mit einem Klick auf {{< seatable-icon icon="dtable-icon-rename" color="grey" >}} und speichern Sie den Webhook erneut, ohne eine Änderung vorzunehmen. Der Webhook wird dadurch sofort wieder aktiv.

Um eine erneute Deaktivierung zu vermeiden, sollte das empfangende System die Webhooks zuverlässig verarbeiten und innerhalb von 30 Sekunden den Status-Code 200 zurückliefern.
