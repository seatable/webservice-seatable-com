---
title: 'Automation Triggers'
date: 2023-01-27
lastmod: '2025-11-11'
categories:
    - 'automationen'
author: 'kgr'
url: '/help/automation-triggers-seatable'
aliases:
    - '/help/automations-trigger'
seo:
    title: 'Automation triggers: SeaTable options at a glance'
    description: 'Find out which triggers can start automations in SeaTable – conditions, new records, schedules, or advanced periodic actions.'
weight: 5
---

**Trigger events** are one of the two essential components of automations. The events trigger different types of [actions]({{< relref "help/base-editor/automationen/automations-aktionen" >}}), which you can define individually for each automation. This article provides you with an **overview** of the different types of triggers.

## Available automation triggers

In the latest version of SeaTable, there are a total of **four** different triggers to choose from:

![Currently available trigger events](images/automation-triggers.jpg)

- When a row is updated
- When a row is added
- At scheduled time
- At scheduled time for records that match conditions

## Trigger settings

To create or edit a trigger, click on the corresponding box in the central area of the automation editor. The trigger settings then appear on the right.

![Trigger settings](images/automation-trigger-settings.jpg)

- You can first change the **trigger** using the drop-down menu. To do this, select the desired trigger event.
- Then define the **table** and the **view** in which the automation should take effect.
- Depending on the type of trigger, you can make further settings, e.g. **monitored columns**, **conditions** for triggering or the **time** of triggering.

![trigger settings in detail](images/automation-trigger-settings.gif)

{{< warning headline="Save changes" text="Don't forget to **save** the trigger settings! Otherwise, all changes will be lost when you close the window." />}}

## Automation trigger: When a row is updated

If you select this event as a trigger, the corresponding automation is triggered each time a value is changed in one of the monitored columns and a row in the selected view meets certain conditions after editing. If you want the trigger to fire every time a change is made, do not add any conditions.

For the **Conditions**, you can define individually for each column what the corresponding value must look like after editing in order for the automation to start. As part of this, you can decide whether all or only selected columns in the view should be monitored for the occurrence of the trigger event.

![Trigger settings when a row is changed](images/automation-trigger-when-a-row-is-updated.jpg)

If you select this event as the trigger for an automation, you can choose from the following **automated actions**:

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
  
## Automation trigger: When a row is added

If you select this event as a trigger, the corresponding automation will be triggered every time a **new row** is added in the selected view. In addition, you can further restrict the occurrence of the event by defining **conditions** that the new row must fulfill.

![Trigger settings when a row is added](images/automation-trigger-when-a-row-is-added.jpg)

In the conditions, you can specify individually for each column what the corresponding value must be for the automation to start. If you want each new row to trigger the automation, do not add any conditions.

{{< warning headline="Advice" text="This trigger is particularly useful, for example, when you import new data records or enter them via forms." />}}

If you select this event as the trigger for an automation, you can choose from the following **automated actions**:

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

## Automation trigger: At scheduled time

If you select this trigger, you can then define a **time** at which the automation runs **daily**, **weekly** or **monthly**.

![Setting options for a daily trigger at a scheduled time](images/automation-trigger-at-scheduled-time.jpg)

While you can only specify the **time** for a daily automation, you can also specify the **day of the week** for a weekly automation or the **calendar day** for a monthly automation.

![Setting options for a weekly trigger at a scheduled time](images/automation-trigger-at-scheduled-time-weekly.jpg)

If you set this trigger for an automation, you can choose from the following **automated actions**:

- Send notification
- Send app notification
- Send e-mail
- Add record
- Add links
- Run Python script
- Run AI
- Run data processing
- Generate PDF from document and send

## Automation trigger: At scheduled time for records that match conditions

With this trigger, you specify a **time** congruent to the previously mentioned trigger at which the automation is triggered **daily**, **weekly** or **monthly**. You can also limit the rows that are affected by this trigger event.

For the **conditions**, you can specify individually for each column what the corresponding value must look like for the automation to be executed at the specified time.

![Trigger at a scheduled time for records that meet certain conditions](images/automation-trigger-at-scheduled-time-for-records-that-match-condition.jpg)

If you select this trigger for an automation, you can choose from the following **automated actions**:

- Send notification
- Send app notification
- Send e-mail
- Lock record
- Modify record
- Convert page to PDF
