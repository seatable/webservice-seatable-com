---
title: 'Show execution log of an automation'
date: 2023-01-26
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/help/view-automation-run-log'
aliases:
    - '/help/ausfuehrungslog-einer-automation-anzeigen'
seo:
    title: 'Automation Run Log in SeaTable: Monitor Execution Times, Status, and Alerts'
    description: 'Learn how to view and interpret the execution log for SeaTable automations: check times, triggers, warning messages, and ensure reliable, traceable workflows.'
weight: 8
---

To check the **correct execution of an automation**, you have the possibility to view the **execution log**. In this log, SeaTable records the following information for each automation run: execution time, execution condition, status and warnings, if any.

{{< warning  headline="Important note"  text="Each execution of an automation is called an **automation run**." />}}

## To take a look at the execution log

![Show execution log](images/open-automation-log.jpg)

1. Click {{< seatable-icon icon="dtable-icon-rule" >}} in the base header, and then click **Automation Rules**.
2. Move the mouse cursor over the **automation rule** whose log you want to view.
3. Click on the **three dots** and then on {{< seatable-icon icon="dtable-icon-journal" >}} **Open log**.

## Structure of the execution log

![Structure of the execution log](images/structure-of-an-automation-log.jpg)

You can view the following information in the execution log of an automation:

**Execution time**  
Here SeaTable stores the exact time when the trigger initiated the automation.

**Execution condition**  
If the automation is triggered by the change or addition of a record, the message **per_update** appears. On the other hand, if the automation is triggered periodically, the message **per_day/week/month** appears.

**Status**  
The status indicates whether the automation was executed successfully. If this is the case, the message **Success** appears here.

**Warnings**  
If there were problems during the execution of an automation, a corresponding warning message appears here.
