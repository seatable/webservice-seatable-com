---
title: 'Was sind Webhooks und wofür setzt man diese ein?'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/de/hilfe/was-sind-webhooks-und-wofuer-setzt-man-diese-ein'
seo:
    title: 'Was sind Webhooks? Funktion & Anwendung erklärt'
    description: 'Lernen Sie, wie Webhooks in SeaTable funktionieren: automatische Benachrichtigungen, Integration externer Systeme und reale Einsatzbeispiele.'
---

{{< required-version "Free" "Plus" "Enterprise" >}}

SeaTable bietet die Möglichkeit für eine Base einen oder sogar mehrere Webhooks einzurichten. Sobald ein Webhook eingerichtet ist, löst jede Änderung an den Inhalten einer Base einen Impuls in Form eines HTTP-Post Requests an eine beliebige URL aus.

Vereinfacht kann man sich einen Webhook wie ein Benachrichtigungssystem vorstellen. Jedes Mal, wenn sich in einer Base etwas ändert, wird ein Datensatz an eine von Ihnen definierte URL geschickt.

- Sie fügen eine neue Zeile hinzu: SeaTable schickt Ihnen eine Nachricht.
- Sie setzen den Haken in einer Checkbox, auch das ist eine Nachricht.
- Sie löschen eine Zeile, wer hätte es gedacht, auch das erzeugt eine Nachricht.

Jede noch so kleine Änderung an den Inhalten einer Base führt dazu, dass ein Webhook verschickt wird. Man spricht deshalb bei Webhooks häufig auch von einer Echtzeit-Benachrichtigung. Verändert ein Vorgang mehrere Zeilen gleichzeitig, wird dafür [nur ein Webhook]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}) verschickt.

{{< warning type="warning" headline="Wichtig" text="Bei Änderungen an der Struktur der Base, wie z.B. die Anlage einer neuen Spalte, wird kein Webhook verschickt." />}}

## Mögliche Einsatzzwecke von Webhooks

Webhooks sind neben REST-APIs eine beliebte Methode, um IT-Systeme miteinander sprechen zu lassen. Ein Webhook ist gewissermaßen eine Art umgedrehter API-Request. Bei der API wartet SeaTable darauf, dass eine Anfrage kommt, die von der API beantwortet wird. Bei einem Webhook hingegen wird automatisch eine Benachrichtigung verschickt, wenn etwas passiert.

So können Sie mit Webhooks dafür sorgen, dass gewisse Änderungen in einer anderen Software verarbeitet werden. SeaTable schickt das Ereignis im JSON-Format an die Ziel-URL. Die URL wird als Webhook-Endpoint bezeichnet.

Webhooks funktionieren somit grundsätzlich nur in eine Richtung. SeaTable teilt einer anderen Anwendung mit, dass etwas passiert ist. Es liegt somit in der Verantwortung der Zielanwendung zu entscheiden, ob diese Änderung relevant ist und welche Folgeaktivitäten ausgelöst werden sollen. Beliebte Einsatzzwecke von Webhooks sind zum Beispiel:

- E-Mail oder Chat-Benachrichtigung, sobald eine neue Zeile in einer Base angelegt wird.
- Automatische Veröffentlichung eines Artikels, sobald der Status auf „jetzt veröffentlichen“ geändert wird.
- Aktualisierung eines Abos, sobald eine Bezahlung erfasst wird.

Im Sinne einer Automation sind Webhooks somit immer der auslösende Trigger, der zu einer gewünschten Folgeaktivität führt.

## Vorteile von Webhooks

Es gibt zwei Möglichkeiten, wie verschiedene Systeme miteinander kommunizieren können, um Informationen auszutauschen:

- Polling (eine zyklische Abfrage, um Informationen, Ereignisse und Wertänderungen zu erhalten).
- Webhooks.

Beim Polling werden Informationen angefragt, was zu einem konstanten Austausch führt, selbst wenn gar keine Ereignisse auftreten.

![Webhooks vs Polling](images/webhooks-vs-polling.png)

Webhooks hingegen müssen nur kommunizieren, wenn ein Ereignis eingetreten ist.

## Grenzen von Webhooks

Webhooks eignen sich gut als Auslöser, aber nicht als vollständiges Protokoll aller Änderungen. Fehlgeschlagene Zustellungen werden nicht wiederholt und ein Webhook kann [nach Fehlern deaktiviert werden]({{< relref "help/integrationen/webhooks/deaktivierung-eines-webhooks-bei-fehlern" >}}). Wenn Sie Daten mit einem anderen System synchron halten möchten, sollten Sie die Daten deshalb zusätzlich [regelmäßig abgleichen]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).
