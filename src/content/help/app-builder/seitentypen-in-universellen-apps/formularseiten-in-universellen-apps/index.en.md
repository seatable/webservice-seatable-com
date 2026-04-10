---
title: 'Form pages in SeaTable apps'
date: 2023-12-04
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/help/form-pages-in-seatable-apps'
aliases:
    - '/help/formularseiten-in-universellen-apps'
    - '/help/form-pages-in-universal-apps'
seo:
    title: 'Form Pages in SeaTable Apps: Guide'
    description: 'Create custom form pages in SeaTable Apps: drag-and-drop fields, required fields, help texts & submission controls made easy.'
weight: 3
---

You can use this page type to build different **forms** that users can then submit. Form pages in SeaTable apps are ideal for collecting data from many different users. One possible use case is [recording your employees' working hours]({{< relref "pages/arbeitszeiterfassung" >}}).

![Web form for recording your employees' working hours](images/webformular-working-time.png)

{{< warning  headline="Tipp" >}}

[Web forms]({{< relref "help/base-editor/webformulare/webformulare" >}}) are not only available in the app builder, but also directly in the base.

{{< /warning >}}

## Change Page Settings

If you want to change the settings of a page, click on the corresponding {{< seatable-icon icon="dtable-icon-set-up" >}} **gear icon** in the navigation.

![Change form page settings](images/Einstellungen-der-Formularseite-aendern.png)

## Create Forms

Through the **page settings**, which you may already know from the [web form editor]({{< relref "help/base-editor/webformulare/konfigurationsmoeglichkeiten-eines-webformulars" >}}), you can add various **elements** and **fields** to the web form via drag-and-drop. In addition to the **table fields** that correspond to the columns of the selected table, you can also add **horizontal lines** and **annotations**.

![Page settings of the form page](images/Seiteneinstellungen-der-Formularseite.png)

### Field Settings

Each field also has individual **field settings** where you can add a **display name** that differs from the column name and a **help text** in the form. Here you can also set whether a field is a required **mandatory field**, should be pre-filled with a **default value**, or is only displayed under certain **conditions**.

![Field settings of the form page](images/Feldeinstellungen-der-Formularseite.png)

If you want to change the **order** of the fields in the form, you can grab and move a field using the {{< seatable-icon icon="dtable-icon-drag" >}} **six-dot icon**. By clicking the {{< seatable-icon icon="dtable-icon-delete" >}} **trash can icon**, you remove a field from the form.

![Field on the form page of a SeaTable App](images/Feld-auf-der-Formularseite-einer-Universellen-App.png)

### Additional Form Page Settings

Further down, you can set a **color for the help texts** as well as a **message** that is displayed to users after submitting the form.

![Additional settings on form pages](images/Weitere-Einstellungen-auf-Formularseiten.png)

You can also prevent forms with already existing records from being submitted by **preventing the addition of duplicates**. To do this, activate the corresponding toggle and select the columns in which the values must match for a form to be considered a duplicate. If a user then enters identical data, form submission will be blocked.

Finally, you can redirect users to another page of the app or to another website after submitting the form. To do this, click **Enable redirect** and select the appropriate hyperlink. You can also set whether the link opens in a new or the current tab.

## Page Permissions

At the very bottom, you can restrict who is allowed to see the form page.

![Permission for individual pages](images/Berechtigung-fuer-individuelle-Seiten-der-Universellen-App.png)

This is the only [page permission]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) you can choose for form pages – because form pages cannot be used to change or delete rows in the table, and anyone who can see the page is also allowed to submit forms, i.e., add rows.
