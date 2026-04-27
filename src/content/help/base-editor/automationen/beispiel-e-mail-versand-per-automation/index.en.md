---
title: 'Sending e-mails via automation'
date: 2023-03-03
lastmod: '2023-03-03'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/help/send-emails-by-automation'
aliases:
    - '/help/e-mail-versand-per-automation'
seo:
    title: 'Send emails automatically in SeaTable – automation guide'
    description: 'Learn to send automatic SeaTable emails with triggers, conditions and third‑party email accounts via built‑in automation workflows.'
---

With the help of automations, you no longer have to send e-mails manually to selected users, but can have them sent automatically. Simply define a corresponding automation for any table view.

## Send emails via automation

![Send emails via automation](images/how-to-use-automations-for-locking-rows-3.png)

1. In the base header, click {{< seatable-icon icon="dtable-icon-rule" >}} and then click **Automation Rules**.
2. Click **Add Rule**.
3. **Name** the automation and specify the **table** and **view** in which it should act.
4. Define a **trigger event that triggers** the automation.
5. Click **Add Action** and select **Send Email** as the automated action.
6. Confirm with **Submit**.

## Creating the automation

First define a **trigger event** for the automation.

![Trigger events basically available for selection](images/trigger-options-for-archivating-rows.png)

{{< warning headline="Note" >}}

The automated action **Send email** is available after all trigger events:"

- Entries meet certain conditions after editing
- A new entry is added
- Periodic trigger
- Periodic trigger for entries that meet certain conditions

{{< /warning >}}

Then select **Send email** as the automated action.

![Adding the automated action](images/add-an-action.png) ![Adding the automated action](images/example-send-email-action.png)

In the next step, first select an **email account** from which you want to send the emails. To be able to use your email account for sending, you **must** first **add** it as a third party in your SeaTable base. You can find detailed instructions for this step [here]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}}).

{{< warning  type="warning" headline="Important note"  text="If you have **not** added an email account as a third party in your SeaTable base, **no** accounts will be displayed. Adding an email account is therefore an important **prerequisite** for the automation." />}}

![Selection of an email account for sending](images/select-email-account.png)

After selecting the email account, define the **subject**, **recipient** and **content** of the email. You can enter **multiple email addresses** separated by commas and in CC. You also have the option to add **attachments** from a [file column]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}).

![Definition of the email to be sent by the automation](images/define-email.png)

Finally, confirm the automation by clicking on **Submit**.

![Confirmation of the automation](images/confirm-the-automation.jpg)

## Example use case

A concrete **use case** for this type of automation could, for example, occur if you work on the works council of a company. You want to automatically inform the HR department whenever you have approved the dismissal of an employee.

On your side, this can be implemented with a table in which various **data** of all employees of your company are maintained. In this context, you could record, among other things, the **names** of the employees, their **employment status** and the status of their **salary payments**.

![Example table of the concrete use case](images/example-table-email-automation.png)

With the help of an automation, SeaTable should now automatically send an **email** to the HR department as soon as you have approved an employee's dismissal on the works council.

### Creating the automation

First, give the automation a **name** and select both the **table** (employee list) and the **view** (employees ressort marketing) in which the automation should act.

![Basic settings of the automation](images/basic-settings-automation.png)

As the **trigger event** of the automation, select the option **Entries meet certain conditions after editing**. To ensure that the emails are sent **only** when an employee has been dismissed, add as a **filter condition** that the entry in the **status of employment** column must be changed to **terminated**.

![Definition of the trigger event](images/condition-of-the-trigger-event.png)

As the **automated action**, define the action **Send email**.

![Adding the automated action](images/example-send-email-action.png)

In the next step, select an **email account** from which you want to send the emails to the HR department. To be able to use your email account for sending, you **must** first **add** it as a third party in your SeaTable base. You can find detailed instructions for this step [here]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}}).

{{< warning  type="warning" headline="Important note"  text="If you have **not** added an email account as a third party in your SeaTable base, **no** accounts will be displayed in this step. Adding an email account is therefore an important **prerequisite** for the automation." />}}

![Selection of an email account for sending](images/select-email-account-1.png)

After selecting your email account, define the **subject**, **recipient** and **content** of the emails. You can enter **multiple email addresses** separated by commas and in CC. Finally, you also have the option to add **attachments** from a [file column]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}).

{{< warning  headline="Tip"  text="Using curly braces, you can quote **contents from table columns** in the body of the email. Use this feature to automatically insert the **names** of the dismissed employees into the text." />}}

![Definition of the email for the automation of the use case](images/definition-email-example.png)

Once you have finished the email to be sent, confirm the automation with **Submit**.

### Testing the automation

If you then change the employment status of an employee to **terminated** in the selected table, the prepared **email** will automatically be sent to the HR department to inform them about the dismissal.

![Once the employment status of an employee is changed to "terminated", the prepared email is automatically sent to the selected recipients ](images/test-automation-email.jpg)

### More interesting examples of automations:

- [Locking rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Linking entries via automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Adding rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Adding entries to other tables via automation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Sending notifications via automation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
