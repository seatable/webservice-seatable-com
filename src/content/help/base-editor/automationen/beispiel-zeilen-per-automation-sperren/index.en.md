---
title: 'Lock rows via automation'
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

With the help of automations, you no longer have to manually lock rows in your tables, but can have the [locking of rows]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) performed automatically. This is very useful if you always want to prevent a row from being edited further from a certain point in time (e.g. when a process has been completed).

![Lock a row with an automation](images/lock-row-with-an-automation.png)

{{< warning  headline="Unlocking only possible manually"  text="Rows locked by an automation **cannot** be **unlocked** in the same way. This is only possible manually and with the necessary **administrator rights**." />}}

## Creating the automation

1. In the base options, click {{< seatable-icon icon="dtable-icon-rule" >}} and then click **Automation rules**.
2. Click **Add rule**.
3. **Name** the automation and specify the **table** and **view** in which it should take effect.
4. Define a **trigger event** that triggers the automation.
5. Click **Add action** and select **Lock record** as the automated action.

![Selection of the automated action: "Lock record"](images/lock-record.png)

6. Confirm with **Submit**.

{{< warning headline="Important note" >}}

The automated action **Lock record** is only available to you for the following trigger events:

- When a row is updated
- When a row is added
- At scheduled time for records that match conditions

{{< /warning >}}

## Application example

For example, if you want to **lock** every row in one of your tables where a certain entry reaches a specific **value**, define the event **When a row is updated** as the automation trigger.

![Definition of the automation trigger event](images/trigger-example-1.png)

Then set the **value** and the **column** in which it must be reached.

![Definition of the automation trigger event](images/trigger-example-2.png)

Finally, set **Lock record** as the automated action.

![Definition of the automated action](images/automated-action-example.png)

From this moment on, the created automation will lock **all rows** where **entries** change in such a way that they fulfill the automation rule.

![Defined automated action: "Lock record"](images/automated-action-example-2.png)

{{< warning  headline="Please note"  text="With an automation you can only ever lock the rows in which the trigger of the automation has occurred. An automation rule according to the scheme **Event in row X triggers locking of row Y** is not possible." />}}

## Lock multiple rows at the same time

Automations are extremely useful if you want to lock several rows at the same time. To do this, select the trigger **At scheduled time for records that match conditions** and set the appropriate conditions. Instead of setting the execution frequency and time, click **Run now** at the bottom to immediately lock all the desired rows.

For more information on locking rows, see the article [Locking a row]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}).

### More helpful articles in the Automations section:

- [Overview of automations]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [How automations work]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Create an automation]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Manage and group automations]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Stop automations]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Delete automations]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Show execution log of an automation]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Automation triggers]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Automation actions]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Linking entries via automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

### Other interesting examples of automations:

- [Linking entries via automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Add rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Add entries to other tables via automation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Send notifications via automation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Sending e-mails via automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
