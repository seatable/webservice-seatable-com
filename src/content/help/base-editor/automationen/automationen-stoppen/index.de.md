---
title: 'Automationen stoppen'
date: 2023-01-27
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/de/hilfe/automationen-stoppen'
seo:
    title: 'Automationen in SeaTable pausieren und wieder aktivieren: Anleitung & Hinweise'
    description: 'So stoppen Sie Automationen in SeaTable vorübergehend: Automatisierungen einfach pausieren, wieder aktivieren und Datensicherheit im Enterprise-Abonnement gewährleisten.'
weight: 9
---

Wenn Sie Automationen für einen bestimmten Zeitraum nicht mehr ausführen wollen, können Sie sie **pausieren**, anstatt sie zu [löschen]({{< relref "help/base-editor/automationen/automationen-loeschen" >}}). Dies bringt den Vorteil mit sich, dass Sie pausierte Automationen einfach **wieder starten** können, wohingegen Sie gelöschte Automationen nochmals gänzlich neu anlegen müssen.

## Automation vorübergehend anhalten

1. Öffnen Sie eine **Base**, in der Sie eine aktive Automation pausieren möchten.
2. Klicken Sie im Base-Header auf {{< seatable-icon icon="dtable-icon-rule" >}} und im Anschluss auf **Automatisierungsregeln**.
3. Fahren Sie mit dem Mauszeiger über die entsprechende Automatisierungsregel, klicken Sie auf die drei Punkte und dann auf {{< seatable-icon icon="dtable-icon-paused" >}} **Regel pausieren** .

![Automatisierungsregel pausieren](images/pause-automation-rule.gif)

Die ausgewählte Automatisierungsregel ist anschließend **pausiert**. Sie erkennen dies am Hinweis **(pausiert)**, der in Rot an den Namen der Automation angefügt wird.

{{< warning  type="warning" headline="Wichtiger Hinweis"  text="Pausierte Automationen sind **nicht** mehr aktiv, bis sie wieder gestartet werden. Dies bedeutet, dass definierte Trigger-Ereignisse **keine** automatisierten Aktionen mehr auslösen." />}}

## Automation wieder starten

Um pausierte Automationen wieder zu **aktivieren**, folgen Sie einfach den oben bereits beschriebenen Schritten und klicken Sie auf {{< seatable-icon icon="dtable-icon-implement" >}} **Regel starten** .

![Automatisierungsregel wieder starten](images/start-automation-rule.gif)

Der Hinweis **(pausiert)** rechts neben dem Namen der Automation verschwindet anschließend wieder.
