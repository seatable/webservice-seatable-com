---
title: 'Linking entries via automation'
date: 2023-01-30
lastmod: '2023-04-06'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/help/link-entries-automation'
aliases:
    - '/help/verlinken-von-eintraegen-per-automation'
seo:
    title: 'Link Entries Automatically in SeaTable: Automation Guide'
    description: 'Automatically connect records in SeaTable — configure triggers, choose fields, and let automation seamlessly link related table entries for you.'


---

With the help of automations, you no longer have to link entries in your tables manually, but can have these steps performed automatically. Simply define a corresponding automation for any table view.

## Linking entries via automation

![rows Locking and archiving with automation](images/how-to-use-automations-for-locking-rows-3.png)

1. In the base header, click {{< seatable-icon icon="dtable-icon-rule" >}} and then click **Automation Rules**.
2. Click **Add Rule**.
3. **Name** the automation and specify the **table** and **view** in which it should act.
4. Define a **trigger event that triggers** the automation.
5. Click **Add Action** and select **Add Links** as the automated action.
6. Confirm with **Submit**.

## Creating the automation

First define a **trigger event** for the automation.

![Trigger events for blocking and archiving of rows](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Important note" >}}

The automated action **Add links** is available to you **exclusively** available for the following trigger events:

- "Entries meet certain conditions after editing"
- "A new entry is added"
- "Periodic trigger"

{{< /warning >}}

Then select **"Add links"** as the automated action.

![Adding the automated action](images/add-an-action.png) ![Adding the automated action: "Add links"](images/add-action-add-links.png)

Finally, select a **column** that should be linked to the selected table and define a **specific condition** that must be met for the automation to be executed.

![Definition of the automated action](images/automated-actions-add-links.png)

Finally, confirm the automation with a click on **Submit**.

![Confirmation of the automation](images/confirm-the-automation.jpg)

## Example use case

A concrete **use case** for this type of automation could, for example, occur when you work in the accounting department of a company. You want to maintain both a table with all payments received into a company account (**Payments**) and a table with all invoices that have to be paid to the company (**Invoices**).

In the **Payments** table, alongside the **transaction numbers** of the payments (P-0001 etc.), you already record the **amounts** of the various payments (column **"Value"**).

![Example table Payments](images/Table-Payments-1.png)

Your **Invoices** table, meanwhile, contains the **invoice numbers** (column **"Invoice-No"**) and the respective **invoice amounts** (column **"Price Total"**).

![Example table "Invoices"](images/Table-Invoices.png)

Using an **automation**, you now want to **link** the two tables **Payments** and **Invoices** so that you can automatically assign incoming **payments** to an **invoice** based on their invoice numbers.

### Preparing the automation

Before you can create the automation, you first need to add two more columns to the **Payments** table. In the **"Inv-No"** column you manually enter the invoice numbers that belong to the respective payments — this is what will later **trigger** the automation. In the **"Invoices"** column, the **linked entries** from the **Invoices** table will be added automatically once the automation is in place.

![Manual extension of the "Payments" table with two columns](images/Manuelle-Erweiterung-der-Tabelle-22Payments22.png)

In the **Invoices** table you also need one more column (**"Collected Payments"**) into which the linked entries from the **Payments** table are added when the automation runs.

![](images/Hinzufuegen-der-Spalte-22Collected-PAyments22.png)

After that, you can create an **automation** for the **Payments** table.

### Creating the automation

First, give the automation a name and select the **Payments** table together with the view of the same name in which the automation should act.

![Definition of the automation for the use case](images/definition-of-the-automation-1.png)

As the **trigger event** of the automation, select the option **"Entries meet certain conditions after editing"**. As a filter condition, specify that the two columns **"Inv-No"** and **"Value"** of the "Payments" table are **not empty**. This condition makes sense because the automation should be triggered as soon as there are entries in these columns.

![Definition of the trigger event of the use case ](images/trigger-example-1-1.png) ![Definition of the trigger event of the use case ](images/trigger-example-2-1.png)

As the **automated action** of the automation, finally define the action **"Add a linked column to the table"**.

![Adding the automated action: "Add links"](images/add-action-add-links.png)

The column **"Invoices"** is the column into which the linked entries will be added when the automation runs.

![Selection of the column into which the linked entries are added](images/automated-action-example-1.png)

In the last step of the definition of the automation, you should set another **condition** that must be met before a linked entry is added to the column. In this example it is defined that every **entry** added in the **"Inv-No"** column must also be found in the **"Invoice-No"** column of the **Invoices** table.

Specifically, this means that every **invoice number** you manually assign to a payment in the **Payments** table must already exist in the **Invoices** table so that the corresponding **entries** in both tables can be **linked** with each other.

![Definition of the final condition for triggering the automation](images/automated-action-example-2-1.png)

### Testing the automation

If you then enter an invoice number in the **"Inv-No"** column of the **Payments** table that is already present in the **Invoices** table, the corresponding **linked entry** is automatically added to the table in the **"Invoices"** column.

![Adding the linked entries by triggering the automation](images/Ausloesen-der-Automation-Beispiel-1-1-1.png)

{{< warning  type="warning" headline="Important note"  text="If you add invoice numbers in the **\\"Inv-No\\"** column that are **not yet** present in the **Invoices** table, the automation will **not** be triggered and accordingly **no** linked entry will be added to the column, because the corresponding entry in the **Invoices** table simply does not exist yet." />}}

With a click on the linked entry, a window opens in which you can view the contents of the **linked entry** from the **Invoices** table.

![With a click on the linked entry, the contents of the linked column in the other table can be viewed.](images/Informationen-der-verlinkten-Spalte.png)

In addition, triggering the automation also adds the **linked entries** from the **Payments** table to the **Invoices** table. In the **"Collected Payments"** column, each invoice number is automatically assigned the corresponding **payment number (P-000X)**. Thanks to the **automation**, you can therefore see the corresponding **payment** for each invoice and quickly determine which invoices are settled and which invoices are still open.

![Adding the linked entries by triggering the automation](images/Ausloesen-der-Automation-Beispiel-2.png)

In this table too, a click on the linked entry opens a window in which you can view the contents of the **linked entry** from the **Payments** table.

![With a click on a linked entry, the contents of the linked column in the other table can be viewed.](images/Informationen-der-verlinkten-Spalte-2.png)

### Further helpful articles in the Automations section:

- [Overview of automations]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [How automations work]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Creating an automation]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Managing and grouping automations]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Stopping automations]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Deleting automations]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Display the execution log of an automation]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Automation triggers]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Automation actions]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Locking rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})

### More interesting examples of automations:

- [Locking rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Adding rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Adding entries to other tables via automation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Sending notifications via automation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Sending emails via automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
