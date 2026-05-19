---
title: 'Step 2: Registration form'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/help/step-2-registration-form'
aliases:
    - '/help/schritt-2-anmeldeformular'
seo:
    title: 'Step 2: Registration Form in the SeaTable Course'
    description: 'Learn in step 2 of the SeaTable online course how the built‑in registration form works and shows only available courses.'
---

Next, we will focus on the web form. As you have already learned how to create a web form with SeaTable in the first online course, you do not need to do this again. The web form is already integrated into the template.

Now open the web form in edit mode and we will briefly discuss the most important points.

## The web form and course selection

The web form is deliberately kept simple and only asks for three values:

- Name
- E-mail
- Course

All three fields are defined as mandatory fields. The **Name** and **E-mail** fields do not require any further explanation.

The special feature is the course selection: Here you can only select courses that still have places available. Try it out for yourself: If you click on the selection field, only three courses are displayed, although there are a total of five courses in the table.

![Web form with course selection limited to available courses](images/lvl2-limited-course-selection.png)

Why is that? We have changed the selection in the link column to the view `{{< seatable-icon icon="dtable-icon-main-view" >}} Available Courses` which only shows courses with free places. This means that you will only see the courses that are available in this view in the web form.

SeaTable takes this restriction into account and ensures that only courses that are not yet fully booked are offered in the web form.

## Help article with further information

- [How to link tables in SeaTable]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}})
- [Configuration options for a web form]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}})
