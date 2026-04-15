---
title: 'Delete automations'
date: 2022-12-06
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/help/delete-automations-seatable'
aliases:
    - '/help/automationen-loeschen'
seo:
    title: 'Delete automations in SeaTable: steps and impact'
    description: 'Find out how to permanently delete automations in SeaTable. Step-by-step instructions and overview of effects on various actions.'
weight: 10
---

You can **delete automation rules** that have already been created at any time. Please note what effects the deletion has on the various **automated actions**.

## To delete an automation

![Eine Automation löschen](images/delete-automation-rule.gif)

1. Open a **Base** in which you want to delete an automation that has already been created.
2. In the base header, click on {{< seatable-icon icon="dtable-icon-rule" >}} and then on **Automation rules**.
3. Move the mouse pointer over the corresponding automation rule, click on the three dots and then on {{< seatable-icon icon="dtable-icon-delete" >}} **Delete rule** .
4. Confirm with **Delete**.

{{< warning type="warning" headline="Deletion is final" text="The deleted automation rule is then **finally gone and cannot be restored**." />}}

## Effects

Depending on which actions you had defined for an automation, the deletion of an automation rule can have **different consequences**. In principle, however, the defined trigger event will **no longer trigger any actions** after deletion – unless it is still used as a trigger for another existing automation.

Particularly in the case of complex actions such as sending emails, Python scripts or AI functions, you should consider only [pausing the automation]({{< relref "help/base-editor/automationen/automationen-stoppen" >}}) instead of deleting it permanently.