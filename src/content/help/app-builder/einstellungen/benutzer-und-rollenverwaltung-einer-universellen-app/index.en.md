---
title: 'User and role management of an app'
date: 2023-05-02
lastmod: '2024-12-13'
categories:
    - 'universelle-apps'
author: 'nsc2'
url: '/help/user-and-role-management-universal-app'
aliases:
    - '/help/benutzer-und-rollenverwaltung-einer-universellen-app'
seo:
    title: 'User and role management in SeaTable apps – guide'
    description: 'Manage users, assign roles, generate invite links and control permissions effectively in SeaTable’s apps. Complete overview.'
---

Whether it's adding **new users**, assigning **roles** or creating **invitation links** – you can perform various administrative tasks in the user and role management of an app. You can access the **user and role management** via the edit mode of your app.

{{< warning  headline="Permission required in the group"  text="To be able to edit an app, you must be the **owner** or an **administrator of the group** in which the underlying **base** is located. Regular **group members** can only view and use the apps." />}}

## User and role management of the app

1. Open a **base** to which you have already added an app.
2. Click **Apps** in the base header.
   ![Click Apps in the base header](images/click-apps-in-the-base-header.jpg)
3. Hover your mouse over the app and click the **pencil icon** {{< seatable-icon icon="dtable-icon-rename" >}}.
   ![Click the pencil icon](images/add-page-to-universal-app-1.png)
4. Open the **user and role management** at the top left of the page.
   ![Icon for user and role management](images/Symbol-fuer-Benutzer-und-Rollenverwaltung.png) 
5. Make the desired **settings**.

## The settings in detail

### Users

In the first section, you will find an overview of all **users** who have access to your app. You will also find the **role** and **status** of each user here.

![Overview of the Users tab in the user and role management of an app](images/user-and-role-management-overview-1.png)

This section also provides you with various options for **managing the current users** of your app.

Use the **search function** to find a specific user. This function can be especially helpful if you have a large number of app users.

![Search function for app users](images/search-function-app-users.png)

To add a user to the app, click **Import users**, search for the user using the input field and then assign a role to them.

![Click Import users](images/import-user-to-app.jpg)

![Importing a user to your app](images/import-users-to-app.png)

Click **Sync users to base** to automatically collect the **app users** in a table of your base.

![Click Sync users to base](images/click-sync-users-to-base-1.jpg) ![Table in which the app users are automatically collected](images/table-with-app-users.png)

If you add more users this way in the future, you can always click **Sync users to base** again to add the **new users** to the table.

![If you add more users to your app in the future, ...](images/if-you-add-more-users-to-your-app.png)

![... you can always click Sync users to base again to automatically add the new users to the table.](images/added-imported-app-users-to-table.png)

To **delete** a user from the app, simply click the **X icon** to the right of the respective user's status.

![Delete user](images/delete-user.jpg)

By clicking the **pencil icons** {{< seatable-icon icon="dtable-icon-rename" >}} that you will find for each user, you can edit their **role** and **status**.

{{< warning  headline="Important note"  text="Please note that the **user** who added the app to the base is automatically registered as **Admin**. Neither the role nor the status of this user can be edited, and this user can **not** be removed from the app either." />}}

![Edit icons for each user](images/edit-icons-users.jpg)

For a **user's role**, the drop-down menu offers all the roles that you can define in the next section of the user and role management.

![Selecting the role of a user](images/select-role-of-user.png)

The **status** of a user can be set to **Active** or **Inactive**. While **active** users have access to the app and its content, **inactive** users lose this access.

![Editing the status of an app user](images/edit-status-of-app-user.png)

Users who do not have access to your app will see this message:

![Access to the app denied for inactive users](images/no-permission-for-inactive-users.png)

### Roles

In this section, you can define any number of **roles** that you can assign to the various app users in the section above.

![Defining different roles for the app users](images/define-roles-for-app-users.jpg)

Here, you only specify the **names** of the roles at first. You can define which **permissions** users with the different roles have individually for each page of the app.

[Learn more about page permissions here.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

### Invitation link

In the third section of the user and role management, you can generate an individual **invitation link** for the app.

First, specify the **role** of the users who will access the app via the invitation link.

![Selecting the role that users who access the app via the invitation link will receive](images/select-role-for-invite-link.png)

You then have the option to set a **password** that must be entered after opening the invitation link in order to gain access to the app.

![Adding a password to the invitation link](images/add-password-protection.png)

Optionally, you can also add an automatic **expiration time** to the invitation link that determines how long it remains valid.

![Adding an automatic expiration time to the invitation link](images/add-auto-expiration.png)

Click **Generate** to create the invitation link. The link will then be displayed below, and you have the option to **copy** or **delete** it.

![Generated invitation link with the available options to copy and delete it](images/copy-and-delete-link-universal-app.png)

Alternatively, you have the option to generate a **QR code** for opening and sharing the app.

![Displaying the QR code for opening and sharing the app](images/show-qr-code-universal-app.png)

Scan the displayed **QR code** to open your app, or share it with other users to give them **access** to your app.

![QR code for opening and sharing the app](images/qr-code-to-share-universal-app.png)
