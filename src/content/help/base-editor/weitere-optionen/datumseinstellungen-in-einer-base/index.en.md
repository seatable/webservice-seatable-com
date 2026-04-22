---
title: 'Date settings in a base'
date: 2025-07-02
lastmod: '2025-07-02'
categories:
    - 'arbeiten-mit-bases'
author: 'kgr'
url: '/help/date-settings-in-base'
aliases:
    - '/help/datumseinstellungen-in-einer-base'
seo:
    title: 'Adjusting date settings in your SeaTable base easily'
    description: 'Change the first day of the week for each SeaTable base. Set Monday, Saturday or Sunday to match your calendar needs. All changes are saved automatically.'

---

As is common in Europe and many other regions, SeaTable uses **Monday** as the first day of the week by default. However, depending on which country you live in, Saturday or Sunday may be the **first day of the week**. You can therefore adapt SeaTable to your regional circumstances: In the **Date settings**, the first day of the week can be set individually for each base.

{{< warning type="warning" headline="Important note" >}}
Only **owners** and **administrators** can edit the date settings of a base that belongs to a group. Simple group members will **not** see the date settings.
{{< /warning >}}

## Change the first day of the week in a base

![Date settings in a base](images/date-settings-of-a-base.gif)

1. Open the **base** whose date settings you want to edit.
2. Click on the **three dots** in the base header.
3. Go to **Settings** and then to **Date settings**.
4. In the new window, select which day of the week should be the **first day of the week**.
5. Then **close** the window. The settings you have made are automatically **saved**.

## Scope of the date settings

An adjustment in the date settings causes the selected day to move to the first column in the calendar control of [date columns]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}). This applies to the currently open base and all apps based on it.

In the [Calendar plugin]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}) and on [Calendar pages in apps]{{< relref "help/app-builder/seitentypen-in-universellen-apps/kalenderseiten-in-universellen-apps" >}}), however, you can still configure the first day of the week individually and independently of the setting in the base.