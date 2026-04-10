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

Whether it is adding **new users**, assigning **roles** or creating **invitation links** - you can perform various administrative activities in the user and role administration of an app. You can access the **user and role administration** via the edit mode of your app.

{{< warning  headline="Authorization required in the group"  text="To be able to edit an app, you must be the **owner** or **administrator of the group** in which the underlying **base** is located. Simple **group members** can only view and use the apps." />}}

## User and role management of the app

1. Open a **base** to which you have already added an app.
2. Click **Apps** in the base header.

![Click Apps in the base header](images/click-apps-in-the-base-header.jpg)

4. Hover your mouse over the app and click the **pencil icon** {{< seatable-icon icon="dtable-icon-rename" >}}.

![Click on the edit icon](images/add-page-to-universal-app-1.png)

6. Open the **user and role administration** at the top left of the page.

![Icon for user and role administration](images/Symbol-fuer-Benutzer-und-Rollenverwaltung.png)

8. Make the desired **settings**.

## The settings in detail

### User

In the first section you will find an overview of all **users** who have access to your app. In addition, you will also find the **role** and **status of** the respective user.

![Overview of the Users tab of the User and Role Management of an app](images/user-and-role-management-overview-1.png)

This section also provides you with various options for **managing the current users of** your app.

Use the **search function to** find a specific user. This feature can be especially helpful if you have a large number of app users.

![Search function for app users](images/search-function-app-users.png)

To add a user to the app, click **Import User**, search for the **user** using the input field, and then assign a role to the user.

![Click Import User ](images/import-user-to-app.jpg)

![Import a user to your app](images/import-users-to-app.png)

Click **Synchronize users with base** to automatically collect the **app users** in a table of your base.

![Click Synchronize user with base](images/click-sync-users-to-base-1.jpg)  
![Table in which app users are automatically collected](images/table-with-app-users.png)

If you add more users this way in the future, you can always click **Synchronize users with base** again to add the **new users** to the table.

![If you add more users to your app in the future, ...](images/if-you-add-more-users-to-your-app.png)

![... you can always click Synchronize users with base again to add the new users to the table automatically.](images/added-imported-app-users-to-table.png)

To **delete** a user from the app, simply click on the **X icon**, which you can find to the right of the status of the respective user.

![Delete user](images/delete-user.jpg)

By clicking on the **pen icons** {{< seatable-icon icon="dtable-icon-rename" >}}, which you can find for each user, you can edit their **role** and **status**.

{{< warning  headline="Important note"  text="Please note that the **user** who added the app to base is automatically registered as **Admin**. Both role and status of this user **cannot** be edited and the user cannot **be** removed from the app." />}}

![Editing icons for each user ](images/edit-icons-users.jpg)

For the **role of a user you** can choose from all roles in the drop-down menu, which you can define in the next section of the user and role administration.

![Selection of the role of a user ](images/select-role-of-user.png)

The **status of** a user can be set to **Active** or **Inactive**. While **active** users have access to the app and its content, **inactive** users lose this access.

![Editing the status of an app user](images/edit-status-of-app-user.png)

Users who do not have access to your app will see this message:

![Denied access to the app for inactive users ](images/no-permission-for-inactive-users.png)

### Rollers

In this section you can define any number of **roles**, which you can assign to different app users in the section above.

![Definition of different roles for the app users ](images/define-roles-for-app-users.jpg)

Here you initially define only the **names of** the roles. You can define which **permissions** users with the different roles have individually for each page of the app.

[Learn more about page permissions here.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

### Invitation link

In the third section of User and Role Management, you can generate an individual **invitation link** for the app.

First, define the **role of** the users who will access the app using the invitation link.

![Selection of the role that will be given to the user who will use the app using the invitation link.](images/select-role-for-invite-link.png)

Afterwards, you have the option to set a **password** that must be entered after opening the invitation link in order to gain access to the app.

![Adding a password to the invitation link](images/add-password-protection.png)

Optionally, you can also add an automatic **expiration time to** the invitation link, how long it is valid.

![Add automatic expiration time to invitation link ](images/add-auto-expiration.png)

With a click on **Generate** you can have the invitation link created. The link will be displayed below and you have the option to **copy** or **delete** it.

![Generated invitation link along with available options to copy and delete the invitation link.](images/copy-and-delete-link-universal-app.png)

Alternatively, you have the option to generate a **QR code** to open and share the app.

![Display the QR code to open and share the app.](images/show-qr-code-universal-app.png)

Scan the displayed **QR code** to open your app or share it with other users to give them **access to** your app.

![QR code to open and share the app](images/qr-code-to-share-universal-app.png)
