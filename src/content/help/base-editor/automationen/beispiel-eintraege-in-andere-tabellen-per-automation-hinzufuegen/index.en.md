---
title: 'Add entries to other tables via automation'
date: 2023-03-03
lastmod: '2023-04-12'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/help/add-entries-to-other-tables-automation-seatable'
aliases:
    - '/help/eintraege-in-andere-tabellen-per-automation-hinzufuegen'
seo:
    title: 'Add entries across tables automatically in SeaTable'
    description: 'Use automation to add rows to any table in SeaTable when triggers fire – streamline onboarding and cross-table processes.'
---

With the help of automations, you no longer have to make entries in other tables manually, but can have these steps performed automatically. The big advantage of this is that the trigger does not have to be in the same table as the action that is triggered.

## Add entries to other tables via automation

![Add entries to other tables via automation](images/how-to-use-automations-for-locking-rows-3.png)

1. In the base header, click {{< seatable-icon icon="dtable-icon-rule" >}} and then click **Automation Rules**.
2. Click **Add Rule**.
3. **Name** the automation and specify the **table** and **view** in which it should be triggered.
4. Define a **trigger event that triggers** the automation.
5. Click **Add action** and select **Add new entry in other table** as automated action.
6. Define the **table** where the entry should be inserted and the pre-filled **fields**.
7. Confirm with **Submit**.

## Creating the automation

Define a **trigger event** for automation after first defining in which **table** and **view** it will occur.

![Trigger events basically available for selection](images/trigger-options-for-archivating-rows.png)

{{< warning headline="Important note" >}}

The automated action **Add new entry in other table** is available to you **exclusively** available for the following trigger events:

- [Entries meet certain conditions after editing]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_eintraege_erfuellen_nach_bearbeitung_bestimmte_bedingungen)
- [A new entry is added]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_ein_neuer_eintrag_wird_hinzugefuegt)

{{< /warning >}}

Then select **Add new entry in other table** as the automated action.

![Adding the automated action](images/add-an-action.png) ![Selection of the automated action](images/add-action-example2.png)

In the next step, select the **table** into which the entry should be added once the trigger fires.

![Selection of the table into which the entry will be added when the automation is triggered](images/select-table.png)

Then click on **Add field** to select the columns for which you want to define preset values in the new entry.

![Click on Add field](images/add-field.png)

Now select a corresponding **column** from the drop-down menu and define the pre-filled **value** in the input field. Depending on the selected [column type]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}
), you have different **options** to choose from.

![Definition of the entry and the column to which it should be added](images/set-table-and-entry.png)

Finally, confirm the automation by clicking on **Submit**.

![Confirmation of the automation](images/confirm-the-automation.jpg)

## Example use case

A concrete **use case** for this type of automation could, for example, occur if, as a manager in a company, you are responsible for new employees joining your team. As part of the onboarding process, it might be defined that on the employee's first day you have to request their **salary payment** and document the **handover of a company car**.

When you add the new employee to your table, you want to automatically inform the HR department that you have handed over the company car and that they can prepare the payroll for the first month. To do this, SeaTable should **add a new entry to the HR department's table**.

On your side, this can be implemented with a table in which you maintain various employee data. In this context, you could record, among other things, the names of the employees or new hires, their department and their start date.

![Example table of the use case](images/example-table.3.png)

Now, with the help of an automation, a new entry should automatically be added to another table — used by the HR department to manage salary payments and company cars — whenever you add a new employee to your table.

### Creating the automation

First, give the automation a **name** and select both the **table** (employee lists) and the **view** (new employees) in which the automation should be triggered.

![Naming the automation and selecting the table and view in which the automation should act](images/set-table-and-view-example-3.png)

As the **trigger event** of the automation, select the option **Entries meet certain conditions after editing**.

![Selection of the trigger event](images/trigger-condition.png)

To ensure that **only** new entries are added to the HR department's table once you have entered the **name** of a new employee **in your table**, select as a **filter condition** that the "employee" column must **not be empty** after editing.

![Adding a filter condition](images/set-condition-example-3.png)

As the **automated action**, define the action **Add new entry in other table**.

![Selection of the automated action](images/add-action-example2.png)

In the next step, select the "Payments" table as the **table** into which an entry will be added once the automation is triggered.

![Selection of the table into which the entry is added when the automation is triggered](images/select-table-example3.png)

Then define the **values** with which certain fields should be pre-filled. To quote the name of a new employee in the new entry in the HR department's table, write the **name** of the column in your table that contains this value — surrounded by curly braces — into the text field: {employee}

![Definition of the entries to be added to the selected table](images/define-the-entrys-in-the-second-table.png)

### Testing the automation

If, after confirming the automation, you enter the name of a new employee into your table, ...

![Adding a new employee to your table](images/example-after-trigger-3.1.png)

... the defined entries will automatically be added to the HR department's table.

![HR department's table after the automation has been triggered](images/example-after-trigger-3.2.png)

### More interesting examples of automations:

- [Locking rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Linking entries via automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Adding rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Sending notifications via automation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Sending emails via automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
