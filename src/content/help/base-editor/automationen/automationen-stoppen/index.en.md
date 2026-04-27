---
title: 'Stop automations'
date: 2023-01-27
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/help/pause-stop-automations-seatable'
aliases:
    - '/help/automationen-stoppen'
seo:
    title: 'Pause and Restart Automations in SeaTable: Step-by-Step Enterprise Guide'
    description: 'Learn how to pause and reactivate automations in SeaTable Enterprise without deleting rules—ensure business flexibility and continuity without losing settings.'
weight: 9
---

If you do not want to run automations for a certain period of time, you can **pause** them instead of [deleting]({{< relref "help/base-editor/automationen/automationen-loeschen" >}}) them. This has the advantage that you can simply **restart** paused automations, while you have to create deleted automations from scratch again.

## Temporarily stop automations

1. Open a **Base** in which you want to pause an active automation.
2. In the base header, click on {{< seatable-icon icon="dtable-icon-rule" >}} and then on **Automation rules**.
3. Move the mouse pointer over the corresponding automation rule, click on the three dots and then on {{< seatable-icon icon="dtable-icon-paused" >}} **Pause rule** .

![Pause automation rule](images/pause-automation-rule.gif)

The selected automation rule is then **paused**. You can recognize this by the note **(paused)**, which is added to the name of the automation in red.

{{< warning type="warning" headline="Important note" text="Paused automations are **no longer active** until they are restarted. This means that defined trigger events no longer trigger automated actions." />}}

## Restart automations

To **activate** paused automations again, simply follow the steps described above and click {{< seatable-icon icon="dtable-icon-implement" >}} **Start rule** .

![Restart automation rule](images/start-automation-rule.gif)

The **(paused)** note to the right of the automation name then disappears again.
