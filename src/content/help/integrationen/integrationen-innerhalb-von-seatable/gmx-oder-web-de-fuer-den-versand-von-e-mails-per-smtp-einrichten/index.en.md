---
title: 'Set up GMX or WEB.DE to send emails via SMTP'
date: 2023-03-10
lastmod: '2025-02-14'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'cdb'
url: '/help/setup-gmx-or-web-de-smtp-email-sending'
aliases:
    - '/help/gmx-oder-web-de-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Set up GMX or WEB.DE for SMTP email sending in SeaTable'
    description: 'How to configure GMX or WEB.DE email accounts in SeaTable for sending emails via SMTP securely with detailed setup instructions.'
---

The email services GMX and WEB.DE are very popular in German-speaking countries. You can use GMX and WEB.DE accounts to send emails from a SeaTable bases.

This article explains how to set up a **GMX** or **WEB.DE** e-mail account in a SeaTable base and what preparatory measures are necessary.

{{< warning headline="Identical procedure for GMX and WEB.DE" text="**GMX** and **WEB.DE** are offers from the German telecommunications provider 1&1. The procedure for integrating an email account in a SeaTable base is demonstrated in this help article using GMX as an example. If you want to use a WEB.DE account, follow the instructions in the same way. The preparatory step must be carried out in the WEB.DE account settings." />}}

**In this how-to video, we'll show you how to set up your email account in SeaTable.**

{{< youtube 5AcQzZiwCx0 >}}

## Allow POP3/IMAP retrieval

By default, GMX and WEB.DE accounts can only be used via the webmailers or apps of the two providers. The retrieval and sending of emails with a third-party program such as Outlook, Thunderbird and SeaTable must be explicitly approved. You can do this in your account settings.

1. Log in to your **GMX e-mail account**.
2. Call up the **settings** for your account.

![Settings within GMX](images/gmx-free-email-smtp-versand-mit-seatable.jpg)

4. Click on **POP3/IMAP retrieval** in the e-mail settings.
5. Activate **Allow POP3 and IMAP access**.

![Allow SMTP for GMX and WEB.De.](images/activate_smtp_for_gmx.png)

7. **Save** your change.

You have now made all the preparations to be able to use this email account in SeaTable for sending emails.

## Creation of the e-mail account in SeaTable

Now add your e-mail account as a **third-party provider** in your SeaTable base. The following steps are necessary for this:

![Third-party integration via the advanced base options](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)

1. Open the extended base options by clicking on the **three-dot icon** {{< seatable-icon icon="dtable-icon-more-level" >}}.
2. Select the option **Integration of third-party providers**.
3. Click on **Add e-mail account**.

4. Enter the following information:
    - **Account name**: any name for the account, e.g. 'GMX'
    - **Sender**: Your GMX address, e.g. 'seatable@gmx.de'
    - **SMTP server**: 'mail.gmx.net'
    - **SMTP port**: '587'
    - **Username**: Your GMX address, e.g. 'seatable@gmx.de'
    - **Password**: the password of your GMX account

The IMAP host and IMAP port fields can remain empty. The SMTP server data for WEB.DE can be found in [the WEB.DE help section.](https://hilfe.web.de/pop-imap/imap/imap-serverdaten.html)

An example configuration for a GMX account looks like this:  
![SMTP settings from GMX](images/smtp-settings-gmx.jpg)

## Send emails via automation

After that, you can use the email account created in your SeaTable base to send emails via automation or [button.]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})

If you want to learn more about this useful automation, read the article [Email Sending by Automation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}).
