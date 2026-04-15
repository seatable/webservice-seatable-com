---
title: 'Send notifications via automation'
date: 2023-02-27
lastmod: '2023-03-31'
categories:
    - 'benachrichtigungen'
author: 'nsc2'
url: '/help/send-notifications-via-automation'
aliases:
    - '/help/benachrichtigungen-per-automation-versenden'
seo:
    title: 'Send Notifications via Automation in SeaTable: Guide'
    description: 'Automate notifications in SeaTable by setting rules that send alerts to users: German, English, Spanish, French, Portuguese, Russian and Chinese included.'

---


If you have an Enterprise subscription, you can also send notifications to selected users via automation. To do this, simply define an appropriate automation rule for any table view.

## Send notifications via automation

![Send emails via automation](images/how-to-use-automations-for-locking-rows-3.png)

1. In the base header, click {{< seatable-icon icon="dtable-icon-rule" >}} and then click **Automation Rules**.
2. Click **Add Rule**.
3. Give the automation a **name** and specify the **table** and the **view in** which it should act.
4. Define a **trigger event that triggers** the automation.
5. Click **Add Action** and select **Send Notification** as the automated action.
6. Confirm with **Submit**.

## Creating the automation

First define a **trigger event** for the automation.

![Trigger events basically available for selection](images/trigger-options-for-archivating-rows.png)

The **four options** are:

- Entries meet certain conditions after editing
- A new entry is added
- Periodic trigger
- Periodic trigger for entries that meet a certain condition

Then select **Send notification** as the automated action. This is available as an action for all four trigger options.

![Adding the automated action](images/add-an-action.png)  
![Adding the automated action](images/send-notification.png)

In the next step, you select the **users** to be notified when the trigger event occurs. Note that you can only select users who have at least **read access to** the table or view.

![Selection of users to be notified ](images/select-users-to-get-notified.png)

In the last step, paste the **content of** the notification into the **text field** provided. To refer to entries in the table, simply write the name of the columns in curly brackets in the text.

![Adding the content of the notifications to be sent out ](images/content-of-the-notification.png)

Save the automation by clicking **Submit**.

## Application example

A concrete **use case** for this type of automation could occur, for example, if you work as a manager in a company and want to order the booking of various training courses for your employees. In doing so, you would like to automatically inform the HR department, which ultimately books the trainings, about which training your employees would like to attend.

In concrete terms, this can be implemented with the help of a table in which various **data on** your company's employees is maintained. In this context, you could collect, among other things, the **names of** the employees, the **department** and the last training booked by them.

![Example table of the concrete use case of automation](images/beispieltabelle-anwendungsfall.png)

With the help of an automation, a **notification** should now be sent automatically to selected employees in the HR department whenever a new booking is requested in the table, so that they can initiate the booking of the requested training for the corresponding employee.

### Creating the automation

First, give the automation a **name** (e.g. notification if training is booked) and select both the table (here: employees & trainings) and the view in which the automation should work.

![Naming the automation and defining the table and view in which it should act](images/definition-of-the-automation-1.png)

As a **trigger event of** the automation, select the option "Entries meet certain conditions after processing".

![Selection of the trigger event](images/trigger-condition.png)

In order to send the notifications only in case of requesting a new training, add as a **filter condition** that the entry in the column "last training booked" must be changed to one of the possible **selection options** in this column.

![Adding a filter condition](images/set-filter-condition.png)

You then define the action "Send notification" as the **automated** action.

![Adding the automated action](images/send-notification.png)

In the next step, in the drop-down field, select the **employees of** the HR department to whom the **notification** should be sent when the trigger is triggered.

![Selection of users to be notified ](images/select-users-to-get-notified-example.png)

In the last step you can write the **content of** the notification to be sent in the provided text field.

![Adding the content of the notification ](images/content-of-the-notification-example.png)

{{< warning  headline="Tip"  text="You can use braces to quote the **contents of the table columns** in the notification. Use this feature to add the **names of** the employees and the name of the requested **training** to the notification." />}}

### Testing the automation

If you subsequently request a new training for an employee in the selected table, i.e. change the entry in the "**last training booked**" column to the last training requested, the prefabricated **notification** is automatically sent to the selected users of the HR department.

The employees in the HR department receive the information that a training has been requested in the notification, which they reach via the bell icon {{< seatable-icon icon="dtable-icon-notice" >}}, and can initiate the selected training for the corresponding employee.

![Notification sent to the selected users after the trigger event has been triggered.](images/notification-after-trigger.png)

### Other interesting examples of automations:

- [rows Lock by automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Linking entries via automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [rows Add via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Add entries to other tables via automation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [E-mail dispatch via automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
