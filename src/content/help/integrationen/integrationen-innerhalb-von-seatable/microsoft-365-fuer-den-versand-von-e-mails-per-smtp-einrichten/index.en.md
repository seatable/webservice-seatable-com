---
title: 'Set up Microsoft 365 to send email via SMTP'
date: 2023-04-28
lastmod: '2025-03-07'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'nsc2'
url: '/help/microsoft-365-smtp-email-integration'
aliases:
    - '/help/microsoft-365-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Microsoft 365 SMTP Setup for SeaTable: Send Secure Emails via OAuth2'
    description: 'Learn to connect your Microsoft 365 account with SeaTable for secure SMTP email sending, covering authentication, app registration, and integration steps.'
---

**Microsoft 365**, the popular online service for Microsoft's Office applications, can be used to **send emails from SeaTable**. Authentication against your Microsoft 365 must be carried out using Microsoft's modern authentication. (Authentication via user name and user password is not possible with Microsoft 365).

{{< warning headline="Outlook email accounts" text="These instructions explain the procedure using a Microsoft 365 account. However, the procedure also applies to free Outlook email accounts." />}}

## Preparation in the Entra Admin Center

To be able to use your Microsoft 365 account in SeaTable for sending emails, you must first create and configure an application in Microsoft's Entra Admin Center.

1. Log in to the [Microsoft Entra Admin Center](https://entra.microsoft.com/). The user needs admin rights for the account that is to be used for sending.
2. Click on **App registrations** in the page navigation.
3. Create a new login by clicking on **\+ New registration**. Enter a name (e.g. 'SeaTable') and select **Any Entra ID Tenant + Personal Microsoft accounts** as the account type. Register the following redirect URI for an app of type **Web**:

    ```
    https://cloud.seatable.io/oauth/third-party-email-accounts/callback/
    ```

    If you are not using SeaTable Cloud, replace cloud.seatable.io with the host name of your SeaTable instance. Complete the creation of the app registration by clicking on **Register**.

4. Note the **Application (client) ID** on the overview page of the app you just registered. This is required to set up the email account in SeaTable.
5. To generate the client key, navigate to **Certificates & secrets** in the navigation of the app. Click **New client secret**. Enter a description and an expiration date for the key.
   ![Creating a client secret for a registered app in Microsoft Entra](images/Creating_Client_Secret_Microsoft_Entra.gif)

6. Copy the value of the created key to the clipboard.

With this, you have made all the preparations to be able to use your Microsoft 365 account as an email account in SeaTable.

## Creation of the email account in SeaTable

Now you need to add your Microsoft 365 account as a third party account in your SeaTable base. To do this, the following steps are necessary:

1. Open the extended base options by clicking on the **three-dot icon** {{< seatable-icon icon="dtable-icon-more-level" >}} in the top right-hand corner.
2. Select the item **Third party integration**.
   ![Third-party integration via the advanced base options](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)
3. Click on **Add email account**.
4. Select **Microsoft (Microsoft 365 and Outlook)** as the service provider.
5. Enter the following information and then click on the **Submit** button in the upper right corner:
    - **Account name**: any name for the account, e.g. 'Microsoft 365'
    - **Application (client) ID**: the application (client) ID of the created app
    - **Client secret**: the client secret of the created app
6. Grant the requested permissions by clicking **Accept**.
   ![Screencast accept permissions requested](images/Accept-Permissions-Requested-Microsoft.gif)

## Send emails via automation or button

After that, you can use the email account created in your SeaTable base to send emails via [automation]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) or button.

If you want to learn more about this useful feature, read the article [Setting up an email account in a base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).
