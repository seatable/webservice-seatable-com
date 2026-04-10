---
title: 'What is the user ID and how can you filter with it?'
date: 2023-04-25
lastmod: '2023-05-12'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/help/user-id-filter-seatable'
aliases:
    - '/help/was-ist-die-id-des-users-und-warum-kann-man-danach-filtern'
seo:
    title: 'User ID: filter SeaTable rows dynamically'
    description: 'Use user IDs for dynamic filtering in SeaTable tables. Flexible task assignment and granular control for better teamwork.'
weight: 23
---

The ID of the user is best described as a **personal identification number**. The user's ID is unique within the team and always belongs to one team member.

With the help of User ID you can set **dynamic filters** in SeaTable, which in certain situations is more suitable than filtering by the [creator column]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) or [collaborator column]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}). In this article we will present you the advantages and disadvantages of filters with User ID.

If you want to know how to change the user ID of a team member, [you can find the answer in this help article]({{< relref "help/teamverwaltung/team/aenderung-der-id-des-users-in-der-teamverwaltung" >}}).

{{< warning  headline="Typical use of the User ID"  text="The ID of the user is set by the **team administrator** for the members and typically follows a certain logic. In companies, the individual **employee or personnel number** is often used as the ID of the user." />}}

## Filter with the User ID

In SeaTable you can use the filter **"is current user's ID"** for each text column. This creates a **dynamic filter** that only shows entries where the **own user**'s ID is stored in the corresponding [text column]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}).

![Example filter by user ID](images/filter-user-ID-example-1.png)

### Application example

Suppose you have **three employees** and they have the following **IDs**:

- Markus with the ID **20**
- Helmut with ID **23**
- Sven with ID **56**

Now, for example, if you maintain a table in which you enter the open tasks of your three employees and define such a **filter**, ...

![Defined filter according to the user ID in the use case](images/filter-user-ID-in-the-example-case.png)

... will ...

-  ... Markus will **only** see the entries where his individual **User-ID 20** is entered in the corresponding column.

![Table view of Markus in concrete use case](images/example-table-markus.png)

-  ... Helmut will **only** see the entries where his individual **user ID 23** is entered in the corresponding column.
-  ... Sven will **only** see the entries where his individual **user ID 56** is entered in the corresponding column.

## When is such a filter useful?

The alternative would be to filter by the [Creator]({{< relref "help/base-editor/spaltentypen/die-spalten-ersteller-und-erstelldatum" >}}) or [Collaborator]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) column, which also offer dynamic filtering options. However, these two columns have the following disadvantages:

- The **value in the creator column** _cannot_ be **changed** later. Once set, the value always remains the same. This would be problematic in the above example because the creator of the tasks is _not_ the employee.
- The **collaborator column** can only be filled if a team member has at least **read access** to base. Especially when using the [app]({{< relref "help/app-builder/app-verwaltung/universelle-app" >}}), this may _not_ be desired.
- The collaborator column _cannot_ be **filled automatically via web form**. However, the ID of the user can be set as default value by assigning _{creator.id}_.

You can adjust the **user ID** entered in the text column at any time. So if you want to change the assignment of a row **afterwards**, filtering by the user ID is very helpful.

### Example: Assignment of tasks

Imagine a to-do list that you use to enter tasks in SeaTable. The **creator column** is _out of_ the question for assigning the responsible person, because then the team members could only create tasks and assign them to themselves. The **collaborator column** is the most obvious solution, but only if all team members have at least read access to base. If the team members should not be able to see the tasks of their colleagues under any circumstances, it is recommended to use the user ID to assign the responsible person.

If you assign the open task _"plan next meeting"_ of _Markus_ to another employee, i.e. if you change the **ID of the user** in this row for example from _20 (Markus)_ to _23 (Helmut_ ), the corresponding row will automatically be **filtered out of** the table view of Markus and added to the table view of Helmut.

![Subsequent change of the user ID and consequent removal of the entry from the employee's table.](images/record-gets-deleted-after-user-ID-was-changed.gif)

If you want the task to be displayed not only to the user with the corresponding ID, but also to the creator of row , you can set **two filter rules** with an [either-or link]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}}).

![The alternative: the filter by the Creator column](images/filter-creator.png)

## ID of the user in web forms

In [web forms]({{< relref "help/base-editor/webformulare/webformulare" >}}), you can automatically capture the **identity of logged in users**. To do this, set **{creator.id}** or **{creator.name}** as the **default value** in the page settings of your web form and activate the option that this _cannot_ be changed. Once you have made these settings, the **ID of the logged-in** user is **automatically** inserted in the web form and can no longer be entered or changed manually.

![Definition of user ID as default value in web forms](images/set-default-value-user-ID-in-webformulars.png)
