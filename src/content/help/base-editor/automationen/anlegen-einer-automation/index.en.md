---
title: 'Creating an automation'
date: 2022-12-06
lastmod: '2025-11-04'
categories:
    - 'automationen'
author: 'kgr'
url: '/help/create-an-automation'
aliases:
    - '/help/anlegen-einer-automation'
seo:
    title: 'Create an automation in SeaTable – quick setup guide'
    description: 'Learn to build automations in SeaTable: triggers, actions, advanced logic for error-free and time-saving workflow automation in any base.'
weight: 2
---

With the help of automations, you can **automate processes**. This not only saves you time, but also minimizes the number of human errors. The first step towards automated workflows is to create an automation.

## Create an automation rule

1. Open the **Base** in which you want to create an automation.

![Create automations](images/how-to-use-automations.jpg)

2. In the base header, click on {{< seatable-icon icon="dtable-icon-rule" >}} and then on **Automation rules**.

3. Click on **Add rule or folder** and then on **Rule**.

![Create automation](images/add-automation.jpg)

4. Give the automation rule a **name**.

5. Create the desired automation by defining a **trigger** and various **actions**.

{{< warning headline="Shortcut" text="If no rules exist in the base yet, you can also select a trigger directly **for the very first automation** – and SeaTable will automatically create a rule." />}}

![Shortcut for the first automation](images/shortcut-add-first-automation.gif)

### Create an automation rule in a folder

If you have already created a folder for automation rules, you can also create a rule directly in the folder. To do this, move the mouse pointer over the folder, click on the **three dots** and on **Add rule**.

![Create automation rule in a folder](images/add-automation-in-folder.jpg)

## Further automation steps

### Administration

First, you can manage the new automation rule, for example **rename**, **delete** or **move to a folder**.

{{< button label="More about managing automation rules" link="help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}}

### Triggers

In the next step, you define an event that serves as a trigger and initiates the automation. Here you also specify in which **table** and in which **view** the automation should take effect. The **trigger** can be that a row is added or fulfills certain conditions after a change. You can also set the automation to be triggered daily, weekly or monthly at a specific time.

![trigger settings](images/trigger-settings.jpg)

{{< button label="More about automation triggers" link="help/base-editor/automationen/automations-trigger" >}}

### Actions

Finally, define one or more **actions** that are triggered by the previously defined trigger event. Depending on the type of trigger, possible actions can include sending notifications and emails, adding or locking records or running an AI function.

![Further automation steps](images/steps-for-automation.jpg)

{{< button label="More about automation actions" link="help/base-editor/automationen/automations-aktionen" >}}
