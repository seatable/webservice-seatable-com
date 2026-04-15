---
title: 'rows Add via automation'
date: 2023-03-02
lastmod: '2023-03-31'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/help/add-rows-via-automation-seatable'
aliases:
    - '/help/zeilen-per-automation-hinzufuegen'
seo:
    title: 'Add rows automatically in SeaTable via automation'
    description: 'Use SeaTable automations to add rows on schedule or by trigger – no more manual entries and fully dynamic lists.'
---

With the help of automations, you no longer have to manually add rows with certain entries to your tables, but can have these steps performed automatically. To do this, simply define an appropriate automation for any table view.

## How to add rows with automation

![Add entries via automation](images/how-to-use-automations-for-locking-rows-3.png)

1. In the base header, click {{< seatable-icon icon="dtable-icon-rule" >}} and then click **Automation Rules**.
2. Click **Add Rule**.
3. **Name** the automation and specify the **table** and **view** in which it should act.
4. Define a **trigger event that triggers** the automation.
5. Click **Add Action** and select **Addrow** as the automated action.
6. Confirm with **Submit**.

## Creating the automation

First define a **trigger event** for the automation.

![Trigger events basically available for selection](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Important note" >}}

The automated action **row add** is available to you **exclusively** available after the following trigger events:

- "A new entry is added"
- "Entries meet certain conditions after editing"
- "Periodic trigger"

{{< /warning >}}

Then select **Add row** as the automated action.

![Adding the automated action](images/add-an-action.png) ![Selection of the automated action](images/action-add-records.png)

In the next step, define the **entries** that should appear in a row after the automation is triggered. By clicking on **Add field** you can define any entry you like.

![Click on Add field to define entries](images/add-field.png)

First, select the **column** into which the entry should be inserted.

![Selection of the column into which the entry is added](images/select-column-to-add-record.jpg)

Then you can define the **entry**. Depending on the selected [column type]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}
), different **options** are available to you.

![Define the entry you want to add to the table](images/define-record-to-add.png)

Finally, activate the automation with a click on **Submit**.

![Confirmation of the automation](images/confirm-the-automation.jpg)

## Example use case

A concrete **use case** for this type of automation could occur, for example, when you record your weekly team meetings in a table. You want a row with certain entries to be added automatically every week before the meeting starts, so that you only have to enter the remaining information manually.

In this context, you could predefine, among other things, the **date** of the meeting, the **meeting room** and the fixed **topics**.

![Example table for the concrete use case](images/example-table-case-record-to-table.png)

### Creating the automation

First, give the automation a **name** and select both the **table** (here: Team Meetings) and the **view** (here: Weekly Team Meeting) in which the automation should act.

![Naming the automation and selecting the table and view in which the automation should act](images/basic-settings-automation-example.png)

As the **trigger event** of the automation, select the option **Periodic trigger**.

![Selection of the trigger event](images/select-trigger.png)

Then define at what intervals the automation should be executed. To have the row with the corresponding entries added to the table every week, select **weekly**.

![Selection of the time intervals at which the automation should be executed](images/run-frequency.png)

You can also select a specific **day of the week** and a specific **time** at which the automation should be triggered. In our use case, it makes sense to choose an hour before the weekly meeting on Monday morning as the trigger time.

![Selection of the specific execution time of the automation](images/set-weekday-and-hour.png)

In the next step, define **Add row** as the **automated action**.

![Selection of the automated action](images/select-add-record-as-a-action.png)

By clicking on **Add field**, you can define as many **entries** as you like that will automatically appear in the row.

![Click on Add field to define entries](images/add-field.png)

To automatically record the respective date of the team meeting scheduled on the same day in the row, select the **date column** and the value **The day of execution**.

![Definition of the entries](images/definiton-of-the-records.png)

By clicking on **Add field** you can define any number of additional **entries** that fill the row once the automation is triggered. Simply select a corresponding **column** of your table from the drop-down menu and define a value in the adjacent input field.

![Define any number of entries ](images/other-records.jpg)

If, for example, the team meeting usually takes place in a specific room, you can define that room as a fixed value. And if certain topics (such as new hires, departures, anniversaries) are on the agenda of every team meeting, you can have them automatically entered in the row as well.

### Testing the automation

If the automation works as desired, SeaTable will automatically add a row with the previously defined **entries** to your table after the periodic trigger fires (here: every Monday at 7 a.m.). This saves you some keystrokes, and you can then enter the remaining open data manually.

![Table after the defined automation has been triggered ](images/table-after-automation-new-record-to-current-table.png)

{{< warning  type="warning" headline="Tip"  text="To really save yourself work and **not** have to make changes to automatically entered values, it makes sense to **only** define values that are already fixed and that you will **not** have to adjust manually afterwards. Adjustments to the automatically added entries are possible at any time, but significantly limit the benefit of the automation." />}}

### More interesting examples of automations:

- [Locking rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Linking entries via automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

- [Adding entries to other tables via automation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Sending notifications via automation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Sending emails via automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
