---
title: 'Automation Actions'
date: 2023-01-27
lastmod: '2025-11-11'
categories:
    - 'automationen'
author: 'kgr'
url: '/help/automation-actions-seatable'
aliases:
    - '/help/automations-aktionen'
seo:
    title: 'Automation actions in SeaTable: full list and options'
    description: 'See every automation action in SeaTable Enterprise: send emails, add or lock rows, notifications, scripts, data processing and useful use cases.'
weight: 6
---

**Automated actions** represent one of the two essential components of automations. The actions are triggered by defined **trigger events**. Depending on the [trigger]({{< relref "help/base-editor/automationen/automations-trigger" >}}), SeaTable can perform different automation actions. This article provides you with an **overview of** the different types of automated actions.

## Available automation actions

The latest version of SeaTable offers a total of 15 different automation actions to choose from:

- Send notification
- Send app notification
- Send e-mail
- Add record
- Lock record
- Modify record
- Add links
- Add record to another table
- Run Python script
- Run AI
- Manage events in Google Calendar
- Run data processing
- Convert page to PDF
- Generate PDF from document and send
- Archive

## Add, duplicate, move and delete automation actions

To add an action, click on **the large button with the plus symbol** and select the corresponding action from the drop-down list. Please note that the available actions differ depending on the trigger.

![Add automation actions](images/automated-actions.jpg)

If you have already set up more complex actions, such as sending e-mails, data processing or AI functions, you can also duplicate these. Simply click on the **three dots** and then on **Duplicate**. This means you only have to make minor adjustments to these actions and saves you a lot of time.

![duplicate automation actions](images/duplicate-automated-actions.jpg)

The order of the actions can be easily changed **by drag-and-drop**. Move the mouse pointer over an action box, hold down the left mouse button on the **six-point drag area** and move the action to the desired position. This allows you to flexibly adapt the automation sequence.

![Move automation actions](images/move-automated-actions.gif)

Of course, you can also delete actions that are no longer required. To do this, click on the **three dots** and then on **Delete**. Please note that the automated actions are removed **immediately and permanently** and cannot be restored.

![Delete automated actions](images/delete-automated-actions.gif)

## Automation action: Send notification

By defining "Send notification" as an automated action, you can set a notification to one or more users. The selected users will receive a **notification** each time the corresponding trigger is triggered. This automation action is available **for all automation triggers**.

You can edit the **recipients** and **content** of the notifications at any time in the **settings** of the action. For the recipients, you can specifically select **individual users** or users in a specific column of the type [Collaborator]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}), [Creator]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) or [Last modifier]({{< relref "help/base-editor/spaltentypen/die-spalten-letzter-bearbeiter-und-bearbeitungsdatum" >}}). Write the desired message in the text field and work with column references in curly brackets to insert specific values.

![Send notification via automation](images/send-notification-action-settings.jpg)

Users can check their notifications via the {{< seatable-icon icon="dtable-icon-notice" >}} **bell icon** next to their avatar in the top right corner.

![Incoming notification](images/example-action-notification.png)

The article [Send notifications via automation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}}) goes through this automation using a specific use case.

## Automation action: Send app notification

By defining "Send app notification" as an automated action, you can set a notification to one or more users of an app. The selected users will receive a **notification** in the app each time the corresponding trigger is triggered. This automation action is available **for all automation triggers**.

In the **settings** of the action, you can define which **app** and which **recipients** the notifications should be sent to. For the recipients, you can specifically select **individual app users** or notify users in a specific column of the type **Collaborator, Creator or Last modifier**. Write the desired **content** of the notification in the text field. Use column references in curly brackets to insert specific values.

![Send app notification via automation](images/send-app-notification-action-settings.jpg)

The users of the respective app can check their notifications via the {{< seatable-icon icon="dtable-icon-notice" >}} **bell icon** next to their avatar in the top right-hand corner.

![Check notifications in the app](images/check-app-notifications.jpg)

## Automation action: Send email

By defining "Send email" as an automated action, you can send predefined e-mails to one or more users. SeaTable sends an **e-mail** to each selected user as soon as the corresponding trigger is triggered. This automation action is available **for all automation triggers**.

You can edit the **e-mail account**, **subject**, **recipient**, **message** and **attachments** of the e-mail at any time in the **settings** of the action. Use column references in curly brackets to insert certain values into text fields.

![definition of the automation action: Send email](images/send-email-action-settings.jpg)

The article [Sending e-mails via automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}) runs through this automation using a specific use case.

## Automation action: Add record

If you define "Add record" as an automated action, a **new row** is inserted into the table each time the corresponding trigger is triggered. You can define the exact values for each column individually in advance.

![Automation action: Add row](images/add-record-action-settings.jpg)

The "Add record" automation action is currently available for the following **automation triggers**:
- When a row is updated
- When a row is added
- At a scheduled time

The article [Add rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}}) runs through this automation using a specific use case.

## Automation action: Lock record

If you define "Lock record" as an automated action, the **row** that triggered the automation is locked for editing. You cannot make any further settings for this action – you configure the conditions for the row lock in the **trigger settings**. Please note that you cannot **unlock** locked rows without administrator rights.

![definition of the automation action: Locking a record in the table](images/lock-record-action.jpg)

![Locking a record in a table triggered by an automation](images/example-locked-records.jpg)

The "Lock record" automation action is currently available for the following **automation triggers**:
- When a row is updated
- When a row is added
- At a scheduled time for records that match conditions

The article [Lock rows via automation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}) runs through this automation using a specific use case.

## Automation action: Modify record

If you select "Modify record" as an automated action, **rows** in the table are adjusted according to the previously defined **settings** after the trigger is triggered. You can define a value for each column that the rows automatically adopt after the modification.

![Automation action: Modify record](images/modify-record-action-settings.jpg)

The "Modify record" automation action is currently available for the following **automation triggers**:
- When a row is updated
- When a row is added
- At a scheduled time for records that match conditions

## Automation action: Add links

If you select "Add links" as an automated action, a [link to other records]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) is created in the corresponding column when the trigger is triggered. In the **settings** of the action, you can specify exactly under which conditions which link is added to the table.

![Automation action: Adding links](images/add-links-action-settings.jpg)

The "Add links" automation action is currently available for the following **automation triggers**:
- When a row is updated
- When a row is added
- At a scheduled time

The article [Link records via automation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}}) runs through this automation using a specific use case.

## Automation action: Add record to another table

If you select "Add record to another table" as an automated action, a **row is created in another table** when the trigger is triggered. In the **settings** of the action, you can define individual values for each column that will be assigned to the rows in the selected table as part of the automation. You can also select columns of the same type in the source table to copy row entries to the other table.

![Automation action: Add a row in another table](images/add-record-to-other-table-action-settings.jpg)

The "Add record to another table" automation action is currently available for the following **automation triggers**:
- When a row is updated
- When a row is added

The article [Adding records to other tables via automation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) runs through this automation using a specific use case.

## Automation action: Run Python script

If you select the execution of a Python script as an automated action, the trigger sets a previously defined **Python script** in motion. You can create or edit the script at any time in the [script editor]({{< relref "help/skripte/allgemein/anlegen-und-loeschen-eines-skriptes" >}}) and then select it in the **settings** of the action.

![Automation action: Run Python script](images/run-python-script-action-settings.jpg)

The "Run Python script" automation action is currently available for the following **automation triggers**:
- When a row is updated
- When a row is added
- At a scheduled time

## Automation action: Run AI

If you select the execution of an AI function as an automated action, the trigger calls up an **AI model** that executes a predefined action in the table. You can configure the exact action to be executed in the **settings**. Depending on the type of AI function, **input columns**, **output columns** and a **prompt** may be required.

![definition of an automation action: Run AI](images/run-ai-action-settings.jpg)

You can have the following **AI functions** executed with an automation:

- **Summarize**: Summarizes the text from one or more columns. You can control the length, tone, format and language of the summary by customizing the prompt.
- **Classify**: Classifies records from one or more columns. You can customize the categories and rules through the prompt. The result ends up in a [single select]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) or [multiple select column]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}).
- **OCR**: Extracts text from an [image column]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}). The recognized content is written to the result column of type [Text or Long text]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}).
- **Extract**: Extracts specific information from a column of type text or number according to your requirement. The extracted information is written to the result columns.
- **Custom**: Generates content based on your prompt. Use {column name} in curly brackets to insert the column value of a row.

![actions executable using an AI model](images/run-ai-functions.jpg)

The "Run AI" automation action is currently available for the following **automation triggers**:
- When a row is updated
- When a row is added
- At a scheduled time

## Automation action: Manage events in Google Calendar

If you select "Manage events in Google Calendar" as an automated action, an appointment from SeaTable is created or updated in a Google calendar when the trigger is triggered. There are a few requirements that must be met for this action to work smoothly:
- First, you must [synchronize your Google Calendar account with SeaTable.]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/google-calender-synchronisieren" >}})
- [Two date columns]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) must exist in a table, which define the **start** and **end** of the dates.
- You also need a [text column]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) in which Google can write the **event ID** so that the appointments can be synchronized.

![Requirements for managing events in Google Calendar](images/manage-events-in-google-calendar-part-1.png)

You can also make further settings. Add a **title**, a **description**, a **location** and **attendees** to the event. To do this, write the details in the **text fields** or work with **column references in curly brackets** to insert specific values from the table. By activating the **controllers**, you can decide whether you want to send notifications, whether it is a video conference and whether guests can modify the event, see the guest list and invite other guests.

![more settings for events in Google Calendar](images/manage-events-in-google-calendar-part-2.png)

The automation action "Manage events in Google Calendar" is currently available for the following **automation triggers**:
- When a row is updated
- When a row is added

## Automation action: Run data processing

If you select the execution of a data processing operation as an automated action, the trigger initiates a predefined [data processing operation]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) in the table. You can configure the exact action to be performed in the **settings**. Depending on the type of operation, **certain input and output columns** may be required.

![definition of an automation action: Run data processing operation](images/run-data-processing-action-settings.jpg)

You can have the following **data processing operations** executed with an automation:

- [Calculate delta]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calculate percentage]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})
- [Calculate rank]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Extract user name]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})
- [Compare and copy]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})

![Data processing operations that can be executed using automation](images/run-data-processing-available-operations.jpg)

The automation action "Run data processing" is currently available for the following **automation trigger**:
- At a scheduled time

## Automation action: Convert page to PDF

If you select "Convert page to PDF" as an automated action, SeaTable will **create a PDF document from the record** when the trigger is triggered and save it in a [file column]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}). To do this, select a **template** that you have previously created in the [Page design plugin]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}). You can also define the **file name** in the action settings.

![Create PDF via automation](images/convert-page-to-pdf-action-settings.jpg)

The "Convert page to PDF" automation action is currently available with the following **automation trigger**:
- At a scheduled time for records that match conditions

## Automation action: Generate PDF from document and send

If you select "Generate PDF from document and send" as an automated action, SeaTable will **create a PDF document** when the trigger is triggered and save it in the [file management of the base]({{< relref "help/base-editor/dateien/das-dateimanagement-einer-base" >}}). SeaTable can also send it directly by e-mail.

In the **settings** of the action, select a **template** that you have previously created in the **Report design plugin** and assign a **file name**. Then activate the slider to select an **own folder** in which you would like to save the file. If you only want to generate the document, you can end the configuration at this point.

![create and send PDF from a report design using automation](images/generate-pdf-from-document-action-settings.jpg)

If you then want to send the generated document, activate the "Send to e-mail" slider. You can edit the **e-mail account**, **recipient**, **subject** and **message** of the email at any time in the **settings** of the action.

![create and send PDF from a report design using automation](images/generate-pdf-from-document-and-send-action-settings.jpg)

The automation action "Generate PDF from document and send" is currently available with the following **automation trigger**:
- At a scheduled time

## Automation action: Archive

You can use the archive action to automatically [move rows to the big data storage]({{< relref "help/base-editor/big-data/zeilen-ins-big-data-backend-verschieben" >}}). The big data function must of course be activated in the respective base. As you have already defined the **view** and any filter conditions for the rows to be archived in the trigger settings, you cannot make any settings for the action itself.

![Archive rows via automation](images/automated-action-archive.png)

The "Archive" automation action is currently available for the following **automation triggers**:
- At a scheduled time
- At a scheduled time for records that match conditions