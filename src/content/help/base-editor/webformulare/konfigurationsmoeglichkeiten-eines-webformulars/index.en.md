---
title: 'Configuration options of a web form'
date: 2023-01-08
lastmod: '2026-11-26'
categories:
    - 'webformulare'
author: 'vge'
url: '/help/configure-webform-options'
aliases:
    - '/help/konfigurationsmoeglichkeiten-eines-webformulars'
seo:
    title: 'Configure SeaTable Webforms: Options, Custom Fields, Design & Submission Rules'
    description: 'Learn how to customize SeaTable web forms visually, in content and functionality: settings, fields, required fields, color scheme and logo.'
weight: 3
---

You can configure the look, content, and functionality of your web form by customizing the **form settings**, the **field settings**, and the **color scheme**. The latter requires an Enterprise subscription.

![Adding and configuring fields in a web form](images/Add-fields-to-a-web-form.gif)

## Form settings

- If your base consists of several tables, you can select the **table** for which you want to create the form.
- **Drag and drop** **static elements** and **table fields** into the form or click the **plus icon** to the right of their names.
- With **page breaks**, you can create a **multi-page form**.
- If you want to insert help texts for filling in the form fields, you can define the **font color of the help texts**.
- You can choose between two **notification rules**: Either no notifications are sent or you specify a recipient (e.g. yourself) who receives a notification when a form is submitted.
- You have the option to restrict **access permissions** to users logged into SeaTable only.
- With one click, you can define that all fields are **mandatory fields** that users must fill in.
- If you create a multi-page form, you can show a **progress bar** to the people filling it in so that they can see at any time how far along they are.
- You can also show and hide "Powered by" via a slider.
- Add a **default message** that users will see after submitting the form.
- After the form has been completed, you can activate a **redirect to a web page** (for example, a thank-you page or homepage).
- With a **submission deadline**, you limit how long the form link is valid.
- With a **submission limit**, you limit the maximum number of submissions.

## Field settings

Click a field to access more setting options on the right side.

- You can specify a **field name** that differs from the column name and is displayed in the form. In this way, it is possible to name the columns in the table completely independently of the web form.
- In the **help text**, write down instructions or explanations on how to fill in the respective field.
- Decide whether the respective field is a **required mandatory field** or not. If you enable this setting using the **slider**, users will have to fill in the field to be able to submit the form.
- Decide whether the respective field should be prefilled with a **default value** or not. Using another **slider**, you can specify that the people filling in the form cannot change this value.
- Specify whether a field should only be displayed if previous fields meet certain **conditions**. This allows for more precise user guidance, as irrelevant fields remain hidden during the filling process.

{{< warning  headline="Selection fields"  text="For single and multiple select fields, you can also specify whether the values are displayed as a **list** or as a **dropdown**." />}}

You can change the order of the fields in the web form as you wish by clicking the **six-dot icon** {{< seatable-icon icon="dtable-icon-drag" >}} in the right corner of a field and dragging and dropping the field to the desired location.

To remove a field from the form again, click the **trash can icon** {{< seatable-icon icon="dtable-icon-delete" >}} in the same place.

## Color scheme and logo

{{< required-version "Enterprise" >}}

Especially for companies and organizations, it can be interesting to customize a web form according to their corporate design.

For this purpose, you can brand your form with your **logo**.

![Change logo in web form](images/webformular.png)

You also have the option to customize the top **color bar**. To do so, click **Color scheme** in the upper right corner next to the settings.

As an alternative to the color bar, you can also add a **cover image**.

![Visual customization options in web forms](images/Optische-Anpassungsmoeglichkeiten-in-Webformularen.png)
