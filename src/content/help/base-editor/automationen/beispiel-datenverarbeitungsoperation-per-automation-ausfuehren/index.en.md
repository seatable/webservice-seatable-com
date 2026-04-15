---
title: 'Perform data processing operation by automation'
date: 2023-04-28
lastmod: '2023-05-03'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/help/automate-data-processing-seatable'
aliases:
    - '/help/datenverarbeitungsoperation-per-automation-ausfuehren'
seo:
    title: 'Automate data processing operations in SeaTable'
    description: 'Run data processing operations via automations and save time: calculations, links and more – convenient, recurring and secure.'

---

With the help of automations, you no longer have to perform a data processing operation manually, but can have it performed automatically. The variety of [data processing operations]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}) available - from mathematical calculations to creating links between values in different tables - opens up new possibilities for automating your work processes.

## Perform a data processing operation by automation

![Execute data processing operation via automation](images/how-to-use-automations-for-locking-rows-3.png)

1. In the base header, click {{< seatable-icon icon="dtable-icon-rule" >}} and then click **Automation Rules**.
2. Click **Add Rule**.
3. Give the automation a **name** and specify the **table** and **view in** which it should be triggered.
4. Define a **trigger event that triggers** the automation.
5. Click **Add Action** and select **Run Data Processing Operation** as the automated action.
6. Select any **data processing operation**.
7. Make the necessary **settings** (e.g. table, source column, result column) on the **data processing operation**.
8. Confirm with **Submit**.

## Creating the automation

After you have defined in which **table** and **view the** automation should be triggered, you define the [trigger event]({{< relref "help/base-editor/automationen/automations-trigger" >}}). Currently, only a **periodic trigger** can result in a data processing operation. Therefore, you need to define a **time when** the automation should be triggered daily, weekly or monthly.

![Selection of the automation trigger for the action: Execute data processing operation.](images/select-trigger-for-data-operation-per-automation.png)

{{< warning  headline="Important note"  text="The automated action **Execute data processing operation** is at your disposal **exclusively** available at the following trigger event:" />}}

![Periodic trigger]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_periodischer_trigger)

Then select **Execute data processing operation** as the automated action and choose the desired [data processing operation]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitungsoperationen-in-seatable" >}}).

![Adding the automated action](images/add-an-action.png)

![Selection of the data processing operation to be executed as the automated action of the automation](images/select-data-operation-for-automation.png)

The following **data processing operations** are available for selection:

- [Calculate cumulative values]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}})
- [Calculate changes]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-veraenderungen-berechnen" >}})
- [Calculate percentage share]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-prozentualen-anteil-berechnen" >}})
- [Calculate ranking]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-rangliste-berechnen" >}})
- [Transfer user names]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-benutzernamen-uebertragen" >}})
- [Compare and copy]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-vergleichen-und-kopieren" >}})

In the next step, make specific **settings** for the **data processing operation** that should be triggered by the automation. Depending on the selected operation, you will be asked to define **tables** and/or **columns** (e.g. source and result columns) that you want to use for the mathematical calculations or for establishing relationships between values in different tables.

![Specific settings to be made for the data processing operation](images/specific-settings-for-data-processing-operation.png)

Finally, confirm the automation with **Submit** to save it and have it executed at the defined trigger time, or click on **Run now** to have the automation executed **immediately**.

![Save the automation or run it directly](images/cancel-run-now-or-submit-automation.png)

## Example use case

A concrete use case for this type of automation could, for example, occur if you want to record the number of daily visits to a website in your table. For this, you want to **cumulate** the **visitor numbers** of each individual day, which are recorded in an existing [number column]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}), from row to row in a new column.

Until now, [calculating cumulative visitor numbers with a data processing operation]({{< relref "help/base-editor/datenverarbeitung/datenverarbeitung-kumulierte-werte-berechnen" >}}) was only possible **manually**. With a corresponding automation, it is now possible to have the cumulative visitor numbers calculated **automatically every day** at a fixed time.

To implement this, you first need a table in which the various **days** are recorded in a [date column]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) and the **visitor numbers** to the website in a [number column]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}).

![Example table for the use case of the automation: Calculate cumulative values](images/Beispiel-Tabelle-automation-data-processing-kumulierte-werte-berechnen.png)

Then add a **second number column** to the table, in which the cumulative values will be calculated after each execution of the automation. The new, initially empty _Cumulated Visitors_ column acts as the **result column** for the data processing operation, while the _Unique Visitors_ column is the **source column**.

![Adding a second number column](images/Beispiel-Tabelle-automation-data-processing-kumulierte-werte-berechnen-2.png)

To create the automation, follow the steps described in the section [Creating the automation]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}}). Also select the _Unique Visitors_ column as the **source column** and the newly added _Cumulated Visitors_ column as the **result column**.

![Selection of the source and result column](images/auswahl-quell-und-ergebnisspalte-im-anwendungsfall.png)

After confirming the automation, SeaTable calculates the **cumulative number of website visitors** daily at the selected time and automatically writes it into the result column. Of course, the automatic calculation of cumulative values requires that the **number of website visitors from the previous day** is written into the _Unique Visitors_ column every day, **before** the automation is executed.

Table **before** the automation is triggered:

![Example table before the automation is triggered](images/Beispiel-Tabelle-vor-Ausloesung-der-Auomation-Kumulierte-Werte-Berechnen.png)

Table **after** the automation is triggered:

![Example table after the automation is triggered](images/Beispiel-Tabelle-nach-Ausloesung-der-Automation-Kumulierte-Werte-berechnen.png)
