---
title: 'Step 3: Registration confirmation'
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/help/step-3-registration-confirmation'
aliases:
    - '/help/schritt-3-anmeldebestaetigung'
seo:
    title: 'Step 3: Registration Confirmation Email'
    description: 'Learn how to send registration confirmations and payment requests by email to course participants using SeaTable.'
---

We are now adding the function that participants who have registered for a course will receive a registration confirmation and a request for payment by e-mail.

## Sending e-mails with SeaTable

To send e-mails with SeaTable, you must first create an e-mail account in the base. As the configuration differs depending on the provider, we recommend using [mailtrap](https://mailtrap.io). _Mailtrap_ allows you to send emails to a virtual mailbox, which has the advantage that no emails are sent to real or fictitious customers - but you can simulate sending emails realistically.

{{< warning headline="Which email provider is right for me" text="There is no _right_ or _wrong>_email provider. If you only send a few emails a day, your existing email account will probably suffice. However, as your email volume increases, you should consider a professional provider such as [Brevo.com](https://brevo.com), which allows you to better track the delivery of emails."  />}}

### Create a Mailtrap account

To get started, visit the [Mailtrap registration page](https://mailtrap.io/register/signup) and create a free account.

![Mailtrap registration page with account creation form](images/lvl2-mailtrap.png)

Confirm your e-mail address and log in. After answering a few questions about your interests - these are not relevant for the rest of the process - you will be taken to the _Mailtrap_ homepage.

![Mailtrap home screen with preconfigured “My Inbox”](images/lvl2-mailtrap-inbox.png)

In the left-hand menu, click on `E-Mail Testing > Inboxes`. There you will already find a preconfigured inbox with the name `My Inbox`. You will need the corresponding SMTP access data for the configuration in SeaTable.

![SMTP credentials of “My Inbox” inbox for use in SeaTable](images/lvl2-mailtrap-smtp-credentials.png)

### Configure e-mail dispatch in SeaTable

With the SMTP access data from Mailtrap, you can now set up [e-mail dispatch in SeaTable]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).

![SeaTable dialog with entered Mailtrap SMTP data for email sending](images/lvl2-mailtrap-in-seatable.png)

The emails are not actually sent, but appear in your Mailtrap mailbox. Test this by sending an e-mail to any recipient - it will only end up in your virtual mailbox.

![Example email in Mailtrap inbox to verify SeaTable sending](images/lvl2-mailtest.gif)

## Send e-mail to the customer

Now we can see in the table `Registrations` to create a new column for sending e-mails. Use the following settings:

> Name: any
>
> Column type: `{{< seatable-icon icon="dtable-icon-button" >}} Button`
>
> Label: `Send`
>
> Action: `{{< seatable-icon icon="dtable-icon-email" >}} Send email`
>
> Subject: `Confirmation: Course {Registered for}`
>
> Recipient: `customer@example.com`

![SeaTable table with “Send” button column for sending emails to participants](images/lvl2-create-button.png)

You can use the following text template for the message text:

> Hey,  
> Thank you for registering for the course {Registered for} on {Date}.
>
> To complete your registration, please transfer the course fee using the details below:
>
> Amount: {Price}  
> Bank: Example Bank LTD  
> IBAN: XYZ
>
> We appreciate your prompt payment!
>
> Best regards

In the simple text editor, the placeholders in curly brackets are replaced automatically. If you are using the rich text editor, you must replace the placeholders manually using the `{{< seatable-icon icon="dtable-icon-choose-column" >}} Insert column` insert.

![SeaTable rich text editor with placeholders for course and date information](images/lvl2-rich-text-editor.png)

Then click on the button and check whether the e-mail appears in your Mailtrap mailbox.

Congratulations! You have just sent your first email via SeaTable - even if it only went to Mailtrap's virtual mailbox.

{{< warning  headline="Send e-mails automatically"  text="For now, sending the emails is triggered by clicking a button. An automation can also do this for you: automations are covered in Course 4." />}}

## Help article with further information

- [Setting up an e-mail account in a base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}})
- [Set up Gmail to send e-mails via SMTP]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}})
- [The button]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
- [Sending an e-mail with a button]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [E-mail via automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
