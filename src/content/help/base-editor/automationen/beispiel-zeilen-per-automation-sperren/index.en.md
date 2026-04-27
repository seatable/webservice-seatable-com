---
title: 'rows lock by automation'
date: 2023-01-27
lastmod: '2023-03-31'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/help/lock-rows-automation'
aliases:
    - '/help/zeilen-per-automation-sperren'
seo:
    title: 'Lock SeaTable Rows Automatically: Automation Guide'
    description: 'Learn to lock table rows via automation: choose triggers, set rules, and restrict editing rapidly for efficient team workflows.'
---

With the help of automations, you no longer have to manually lock rows in your tables, but can have [rows perform the]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) automatically. This is very useful if you always want to prevent a row from being processed further from a certain point in time (e.g. when a process has been completed).

![Lock a row with an automation](images/lock-row-with-an-automation.png)

{{< warning  headline="Unlocking only possible manually"  text="You **cannot** **unlock** rows locked with an automation in the same way. This is only possible manually and with the necessary **administrator rights**." />}}

## Creating the automation

1. In the base options, click {{< seatable-icon icon="dtable-icon-rule" >}} and then click **Automation Rules**.
2. Click **Add Rule**.
3. **Name** the automation and specify the **table** and **view** in which it should act.
4. Define a **trigger event that triggers** the automation.
5. Click **Add Action** and select **Lock Entry** as the automated action.

![Selection of the automated action: "Lock entry".](images/lock-record.png)

7. Confirm with **Submit**.

{{< warning headline="Important note" >}}

The automated action **Lock entry** is only available for the following trigger events:

- Entries meet certain conditions after editing
- A new entry is added
- Execute periodically when entries meet certain conditions

{{< /warning >}}

## Application example

For example, if you want to**lock** any row in one of your tables where a certain entry reaches a specific **value**, define the event: **Entries meet certain conditions after editing** as the automation trigger.

![Definition of the automation trigger event](images/trigger-example-1.png)

Then set the **value** and the **column** in which it must be reached.

![Definition of the automation trigger event](images/trigger-example-2.png)

Finally, set **Lock Entry** as the automated action.

![Definition of the automated action](images/automated-action-example.png)

From this moment on, the created automation will lock **all rows** where **entries** change in such a way that they fulfill the automation rule.

![Defined automated action: "Lock entry".](images/automated-action-example-2.png)

{{< warning  headline="Please note"  text="With an automation you can only lock the rows in which the trigger of the automation has occurred. An automation rule according to the scheme **Event in row X triggers blocking of row Y** is not possible." />}}

## Lock multiple rows at the same time

Automations are extremely useful if you want to lock several rows at the same time. To do this, select the **Execute Periodically** trigger for **entries that meet the conditions** and set the appropriate conditions. Instead of setting the execution frequency and time, click **Execute Now** below to immediately lock all the desired rows .

For more information on blocking rows , see the article [Blocking a row.]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}})

### More helpful articles in the Automations section:

- [Overview of automations]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [How automation works]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Create an automation]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Manage and edit automations]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Stop automations]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Delete automations]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Show execution log of an automation]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Automation trigger]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Automation actions]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Linking entries via automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

### Other interesting examples of automations:

- [Linking entries via automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [rows Add via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Add entries to other tables via automation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Send notifications via automation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [E-mail dispatch via automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
