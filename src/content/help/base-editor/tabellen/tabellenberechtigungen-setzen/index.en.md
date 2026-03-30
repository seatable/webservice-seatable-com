---
title: 'Set table permissions'
date: 2022-11-16
lastmod: '2023-08-09'
categories:
    - 'arbeiten-in-tabellen'
author: 'vge'
url: '/help/set-table-permissions-seatable'
aliases:
    - '/help/tabellenberechtigungen-setzen'
seo:
    title: 'Table permissions in SeaTable: set access rights'
    description: 'Define who can view, edit, add or delete rows in a SeaTable table. Flexible options per table for admins, users or groups. Easy rights management.'

---

{{< required-version "Plus" "Enterprise" >}}

With an appropriate subscription you have the possibility in SeaTable to restrict the use and editing of your tables or to block them for certain users.

## Set permissions within tables

![table permission set](images/Tabellenberechtigung-setzen-1.gif)

1. Click the **triangular drop-down icon** next to the table name.
2. Select the **Edit table permission** option.
3. You can now select in the following rows whether you want to use the authorization for **Administrators**, **Nobody**, **Specific user** or **Any** would like to issue.
    - Who may add rows ?
    - Who may delete rows ?
    - Who may edit rows ?
    - Who is allowed to see rows ?

## Frequently asked questions

{{< faq "What does only **administrators** mean?" >}}
By **administrators** here we do not mean the general team admins, but the administrators and owners of a group.
{{< /faq >}}

{{< faq "What happens if you create rows but are not allowed to see it?" >}}
This combination does not work. Only those who can see rows can also edit them or add new rows .
{{< /faq >}}
