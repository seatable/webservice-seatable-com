---
title: 'Prefill form fields'
date: 2023-01-08
lastmod: '2024-03-18'
categories:
    - 'webformulare'
author: 'vge'
url: '/help/prefill-form-fields-url'
aliases:
    - '/help/formularfelder-per-url-vorbefuellen'
seo:
    title: 'SeaTable Webforms: Prefill Form Fields via URL or Custom Links—Quick Guide'
    description: 'SeaTable Web Forms: Prefill fields via link with default values. Instructions on supported column types and read modes.'
weight: 5
---

To **prefill web forms**, you have the option of defining default values in the form fields. You can do this directly in the URL or using a user-friendly function in SeaTable.

## Generate form link with default values in SeaTable

SeaTable offers a function with which you can easily generate **form links** in which default values are already defined in advance.

1. Create a [web form]({{< relref "help/base-editor/webformulare/webformulare" >}}).
2. In the web form editor, click on the {{< seatable-icon icon="dtable-icon-share" >}} **Share** button in the top right-hand corner.
3. Now click on the **Add form link** button and the following input mask will appear:
   ![Prefilled values in user-defined form links](images/Vorbefuellte-Werte-in-benutzerdefinierten-Formularlinks.png)
4. Give the new link a **name**. Under **Custom URL** you can define part of the URL yourself.
5. To prefill a form field with a default value, click on **Add field**. Select the **form field** from the drop-down menu and enter the desired **default value**.
6. Finally, you can decide whether the default value can be changed when filling out the form. To do this, select **Read and write**. If you select **Read only**, the value in the form cannot be changed.
7. Click on **Create** to generate the link.

![Custom form link with prefilled value](images/Benutzerdefinierter-Formularlink-mit-vorausgefuelltem-Wert.png)

The result, i.e. the extended URL, is the same as with the manual procedure described below.

## Prefilling a web form directly via the URL

![Prefill web form](images/prefill.png)

1. Create a [web form]({{< relref "help/base-editor/webformulare/webformulare" >}}).
2. Click on the {{< seatable-icon icon="dtable-icon-share" >}} **Share** button in the web form editor to get the link to the web form.
3. **Copy** the link and paste it into the **address bar of your browser** in a new tab, where you can edit and test it.
4. To prefill a form field with a default value, append the string **/?prefill_COLUMNNAME=PREFILLVALUE** to the form link.

Instead of **COLUMNNAME**, insert the name of the field you want to fill in; for **PREFILLVALUE**, insert the desired default value. Spaces must be written as **%20**. Pay attention to upper and lower case.

**Example**: If you want to send Joe Smith a personalized web form with his name already filled in, append the string **/?prefill_Name=Joe%20Smith** to the form link.

To use **multiple default values**, chain the prefill entries with an **&** character: /?prefill_COLUMNNAME=PREFILLVALUE**&**prefill_COLUMNNAME=PREFILLVALUE

Once you are done, you can test the link by pressing the **Enter key** and opening the web form. If everything worked, you can see the prefilled default values in this **preview**.

## Prefillable form fields

Depending on which column type a form field is based on, prefilling is not always possible. In the following overview, you can see which column types allow prefilling via URL and which do not.

| Column type        | Supports prefilling                                           |
| ------------------ | ------------------------------------------------------------- |
| Auto number        | {{< icon "circle-xmark" >}}                                   |
| Image              | {{< icon "circle-xmark" >}}                                   |
| Checkbox           | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| File               | {{< icon "circle-xmark" >}}                                   |
| Date               | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Duration           | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Single select      | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Email              | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Creator            | {{< icon "circle-xmark" >}}                                   |
| Created time       | {{< icon "circle-xmark" >}}                                   |
| Long text          | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Formula            | {{< icon "circle-xmark" >}}                                   |
| Link formula       | {{< icon "circle-xmark" >}}                                   |
| Geolocation        | {{< icon "circle-xmark" >}}                                   |
| Last modifier      | {{< icon "circle-xmark" >}}                                   |
| Multiple select    | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Collaborator       | {{< icon "circle-xmark" >}}                                   |
| Rating             | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Button             | {{< icon "circle-xmark" >}}                                   |
| Signature          | {{< icon "circle-xmark" >}}                                   |
| Phone number       | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Text               | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| URL                | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Number             | {{< icon icon="circle-check" class="text-seatable-orange" >}} |
| Last modified time | {{< icon "circle-xmark" >}}                                   |
