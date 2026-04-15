---
title: 'Automationen löschen'
date: 2022-12-06
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/de/hilfe/automationen-loeschen'
seo:
    title: 'Automatisierungsregeln in SeaTable sicher löschen'
    description: 'Lernen Sie, wie Sie Automationen in SeaTable dauerhaft entfernen. Sehen Sie alle Auswirkungen, Folgen und Schritte zur Löschung.'
weight: 10
---

Bereits angelegte **Automatisierungsregeln** können Sie jederzeit wieder **löschen**. Beachten Sie dabei, welche Auswirkungen die Löschung auf die verschiedenen automatisierten Aktionen hat.

## So löschen Sie eine Automation

![Eine Automation löschen](images/delete-automation-rule.gif)

1. Öffnen Sie eine **Base**, in der Sie eine bereits angelegte Automation löschen möchten.
2. Klicken Sie im Base-Header auf {{< seatable-icon icon="dtable-icon-rule" >}} und im Anschluss auf **Automatisierungsregeln**.
3. Fahren Sie mit dem Mauszeiger über die entsprechende Automatisierungsregel, klicken Sie auf die drei Punkte und dann auf {{< seatable-icon icon="dtable-icon-delete" >}} **Regel löschen** .
4. Bestätigen Sie mit **Löschen**.

{{< warning  type="warning" headline="Löschung ist endgültig"  text="Die gelöschte Automatisierungsregel ist anschließend **endgültig weg und kann nicht wiederhergestellt werden**." />}}

## Auswirkungen

Je nachdem, welche Aktionen Sie für eine Automation definiert hatten, kann die Löschung einer Automatisierungsregel **unterschiedliche Konsequenzen** nach sich ziehen. Grundsätzlich gilt aber, dass das definierte Trigger-Ereignis nach der Löschung **keine Aktionen** mehr auslösen wird – außer es dient noch für eine andere bestehende Automation als Trigger.

Besonders bei aufwändig anzulegenden Aktionen wie E-Mail-Versand, Python-Skripten oder KI-Funktionen sollten Sie in Erwägung ziehen, lediglich die [Automation zu pausieren]({{< relref "help/base-editor/automationen/automationen-stoppen" >}}), anstatt sie endgültig zu löschen.