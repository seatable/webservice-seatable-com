---
title: 'Übersicht über alle Integrationen in und mit SeaTable'
date: 2023-03-22
lastmod: '2023-07-19'
categories:
    - 'skripte-api-integrationen'
author: 'cdb'
url: '/de/hilfe/integrationen-seatable'
seo:
    title: 'Integrationen mit SeaTable: API, Webhooks & Automatisierung im Überblick'
    description: 'Lernen Sie alle SeaTable-Integrationen: REST-API, Webhooks, JS/Python, E-Mail, Zapier, Make & eigene Plugins für effiziente Workflows.​'
---

Integrationen erweitern die Möglichkeit, wie Sie mit SeaTable arbeiten und interagieren können. Integrationen erlauben beispielsweise, dass Sie mit anderen Tools und Softwarelösungen auf die Ihre Daten innerhalb von SeaTable zugreifen, oder Sie können Arbeitsabläufe designen, die gewisse Arbeitsschritte automatisieren. Alternativ könnten Sie auch eigenen Apps oder Programme entwickeln, die SeaTable als Backend verwenden.

Sie merken es vielleicht schon. Es gibt nicht "die Eine" SeaTable-Integration, sondern je nach Anwendungsgebiet bieten sich jeweils andere Integrationen an. Dieser Artikel soll Ihnen eine Übersicht über die verschiedenen Integrationen und Möglichkeiten geben.

## Übersicht über die verfügbaren Integrationen

Aktuell bietet SeaTable fünf verschiedene Integrationsmöglichkeiten an, welche anschließend etwas umfangreicher vorgestellt werden sollen.

- Javascript und Python
- Integrationen innerhalb von SeaTable
- SeaTable-API
- Webhooks
- Automatisierungsplattformen

## Scripte in SeaTable

SeaTable ermöglicht es Ihnen, individuelle JavaScript- und Python-Skripte in einer Base auszuführen. So können Anwender, die über etwas Programmiererfahrung verfügen, Arbeitsschritte oder wiederkehrende Aufgaben automatisieren. Die Skripte können entweder manuell, mithilfe einer Schaltfläche oder durch eine Automation gestartet werden.

## Integrationen innerhalb von SeaTable

In einer Base bietet SeaTable die Möglichkeit eine **Integrationen von Drittanbietern** zu aktivieren. Aktuell steht im Rahmen dieser Integration nur die Integration mit einem E-Mailkonto zur Verfügung. Diese E-Mail-Integration ermöglicht es, E-Mails mithilfe von Automationen oder Schaltflächen aus SeaTable heraus zu verschicken. Eine weitere Möglichkeit ist die Aktivierung einer E-Mail-Synchronisation, wodurch sämtliche E-Mails des E-Mailkontos in SeaTable zur Verfügung stehen.

## SeaTable-API

Die SeaTable-API bildet eine universelle Schnittstelle, durch die Sie mit jeder beliebigen Software oder Programmiersprache mit den Daten innerhalb von SeaTable interagieren können. Mithilfe der SeaTable-API können etwa Daten, die in einer anderen Software erfasst werden, automatisch in SeaTable geschrieben werden. Oder Sie möchten ein individuelles Frontend für einige SeaTable Daten bauen, dann können Sie über die API direkt und ohne das Webinterface auf die Daten zugreifen.

## Webhooks

Webhooks werden innerhalb von SeaTable jeweils für eine Base eingerichtet. Sobald ein Webhook eingerichtet ist, schickt SeaTable bei jeder Änderung in dieser Base eine Nachricht an eine von Ihnen gewählte URL. Unter dieser URL empfängt eine Software die Webhooks und verarbeitet diese. Je nachdem, welche Änderung in der Base vorgenommen wurde, können Sie eine entsprechende Folgeaktivität ausführen.

Ein typisches Beispiel für einen Webhook wäre die Überwachung des Bezahlstatus einer Rechnung oder eines Abos. Sobald Sie in SeaTable eine Rechnung auf den Status _Bezahlt_ setzen, soll eine andere Software eine entsprechende Aktion durchführen. Dies könnten Sie ganz einfach mit einem Webhook umsetzen. Jede Änderung an den Rechnungen in SeaTable wird per Webhook an die andere Software geschickt und diese reagiert nur auf die für Sie relevante Statusmeldung.

Webhooks werden typischerweise dann eingesetzt, wenn Sie nicht regelmäßig den Status einer Information abfragen wollen, sondern wenn Sie proaktiv bei Änderungen informiert werden wollen. Für die regelmäßige Statusabfrage bietet sich typischerweise die SeaTable-API an.

## Automatisierungsplattformen

Im Alltag arbeitet man häufig nicht nur mit einer Software, sondern mit vielen Lösungen gleichzeitig. Geschäftskontakte speichert man in einem CRM wie Hubspot oder Pipedrive, Termine und E-Mails liegen bei Google, Newsletter verschickt man mit [Mailchimp](https://mailchimp.com/) oder [Brevo](https://www.brevo.com/). Häufig wünscht man sich dabei, dass ein Ereignis in einer Software zu einer Aktivität in einer anderen Software führt. Also wenn Sie einen neuen Newsletter mit Brevo verschicken, dass Sie dann automatisch auch einen Facebook-Post absetzen. Oder wenn jemand auf Ihrer Webseite eine Terminanfrage abschickt, dass dann die Kontaktdaten automatisch in Ihr CRM übertragen werden.

Genau in diesen Fällen kann Ihnen eine der vielen Automatisierungsplattformen weiterhelfen. Diese helfen Ihnen ohne Programmiererfahrung zwei oder mehrere Softwarelösungen miteinander zu verbinden und auf gewisse Auslöser mit gewissen Aktionen zu reagieren.

Aktuell bieten die folgenden Automatisierungsplattformen eine Unterstützung für SeaTable an:

- [Zapier](https://zapier.com/apps/seatable/integrations)
- [Make (formerly Integromat)](https://www.make.com/en/integrations/seatable)
- [n8n](https://n8n.io/integrations/seatable/)
- [Locoia](https://www.locoia.com/connector-integrations/)
- [Integrately](https://integrately.com/integrations/seatable)

## Eigenentwicklung

Sie haben an SeaTable Gefallen gefunden, Ihnen fehlt aber die eine oder andere Funktionen? Sie wollen bestimmte Aufgaben automatisieren und Sie wollen SeaTable in bestehende Systeme integrieren? Mit SeaTable haben Sie alle diese Möglichkeiten! Die Integrationsfähigkeit und Erweiterbarkeit ist ein Teil der SeaTable DNA.

Die Plugins des SeaTable Markets basieren auf der Realtime SDK von SeaTable. Mit dieser können Sie mit wenig Aufwand Ihre eigenen Plugins entwickeln. In der [Entwicklerdokumentation finden Sie alle Details zum SeaTable SDK](https://developer.seatable.com). Der Import eigener Plugins erfolgt über den Plugin Manager.

Der Integration von SeaTable in andere Systeme ist dank SeaTables leistungsfähiger REST-API nahezu keine Grenzen gesetzt. Alle Informationen zur SeaTable API finden Sie in [SeaTables API-Dokumentation](https://api.seatable.com).

Sowohl für die Plugins wie für die Integration nutzen Sie bekannte Programmiersprachen wie JavaScript und Python. Ihre Entwickler können sofort loslegen.
