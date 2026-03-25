---
title: 'SeaTable 1.8: more collaboration and a new column type - SeaTable'
description: 'With resizeable row heights SeaTable now visualizes data even better. Button columns trigger scripts, data collection tables gather info from many users, and views can be shared externally. Save mail accounts in bases, use filters, count links, and benefit from enhanced formulas. Many UI tweaks finish a new teamwork release.'
date: 2021-03-18
categories:
    - 'product-features'
url: '/seatable-release-1-8'
color: 'f9c707'
seo:
    title: 'SeaTable 1.8: Row Height & Buttons, More Collab'
    description: 'Adjustable row heights, button column for automation, data collection, external view links and mail sending — SeaTable 1.8 is here!'
---

We have deployed SeaTable 1.8 on [SeaTable Cloud](https://cloud.seatable.io) today, and we are confident that you'll agree with us: SeaTable 1.8 is a great new release! It is packed with new features and extensions of existing features as well as a great number of smaller improvements. As usual, this release note only highlights the most important changes and this time it was particularly difficult to choose those highlights. You'll find the complete list of changes - as always - in SeaTable's Changelog. We'll upload the new Docker images to Docker Hub within the next couple of days.

## Customizable row height

Literally, SeaTable's new height adjustable rows are its most obvious new features. Four row heights are available: Single, double, triple, and quadruple. The inflated rows make room to show larger picture thumbnails and provide more space to display the content in long-text columns. Specifically, the double row height can hold two lines of text, the triple row height can hold 4, and the quadruple row height holds 6 lines.

![Row height is adjustable in SeaTable 1.8](SeaTable1.8_CustomizableRowHeight_1498x646.png)

The old (single) row height is the new default row height. When opening a new base or creating a new table, this will be applied. The row height setting is hidden behind the new icon in the view toolbar, to the right of the formatting options. Try it and find out which row height fits best for your application!

## Column type #21: Button

The new column type "Button" is the odd man out among the nearly two dozen column types in SeaTable. (Spoiler: We'll fill up the two dozen column types very soon. Be curious!) You don't store any information in a column of the Switch Area type; you use the Button column to automate actions. With the introduction of the new column type in this release, you can run a script by button. Very soon, you will also be able to send emails (more below) and chat messages with one click. Over the course of 2021, we will gradually add more actions that can be triggered by a button.

![New column type: Button](SeaTable1.8_ColumnType_Button_1500x708.png)

When creating a button column, the button's look and purpose is specified. This includes the button's label, its color, and its action. Have a look at the [SeaTable Script Manual](https://developer.seatable.com/scripts/) , if you want to write your own scripts.

## Data collection form

Imagine you are head of sales and you want your product managers to update the product information in your product catalog. Until today, you'd have to grant them access to the product catalog base (or a view) and ask them to verify its up-to-dateness. This may end up being a lot of work as you define individual views and share them with individual team members. With SeaTable 1.8, there is a better way! We introduce: The data collection form.

![Save mail account credentials in SeaTable](SeaTable1.8_MailAccount_1500x495.png)

The data collection form is a tabular view of a base that contains only the rows the current user has created. If the current user is the creator of no row in the underlying base, the data collection form is empty. Hence, the user can only create new records, not edit existing ones. Data collection forms are the tool of choice when it comes to bulk updates involving many people, because the data collection form does not require the user to have a sharing permission for the base. The user only needs to have a SeaTable user account.

For you as head of sales, updating the product catalog is short work: Create a data collection form, send the link to your product managers, and have them do the work.

## External links for views (Plus and Enterprise subscribers only)

External links for bases have been a core element of SeaTable's sharing features since version 1.0. The newly introduced external links for views are their logical extension and allow much more fine-grained data sharing. As their name suggests, external links for views grant read-only access to one selected view of a table. The rows and columns, which are not included in the view, as well as the other tables in the base remain concealed from the person using the external link.

You create an external link for a view using the context menu of a view. Click on the three-dot icon next to the name of the view. In the "Share view" dialog you can adapt the link to your needs. Click "Create" to create the link. You can share the link in any way you like: by email, by chat, or by embedding it in a web page (as we did on our [Newsroom]({{< relref "pages/press" >}}) page, for example).

## Sending emails

Talking about extending existing sharing features, SeaTable 1.8 also has one entirely new sharing feature: SeaTable can send emails! Users can save SMTP credentials of one or more email accounts in a base and then employ these mail accounts using the base.sendMail() method in Python and JS scripts.

![SeaTable 1.8 presents: Data collection form](SeaTable1.8_DataCollectionTable_1500x495.png)

The mail accounts are saved in the backend database and encrypted with symmetrical tokens. In one of the next releases, we'll amend the function with a connection test function. Similarly, we'll provide an option to use the email accounts in combination with the new button column.

## SAML support

Finally, we have a special feature for on-premises users of SeaTable: SeaTable 1.8 now supports SAML for single sign-on (SSO). Following authentication via Active Directory and LDAP, SeaTable's new support for the popular SSO protocol drives its operational flexibility to a new level and makes its integration in larger infrastructures a lot simpler and smoother. Broadly speaking, the large majority of identity management systems (e.g., okta, Keycloak, Auth0, OneLogin, SiteMinder, ...) support SAML.

The complete documentation for using SAML authentication with SeaTable is provided in the [SeaTable Admin Manual](https://admin.seatable.com/configuration/authentication/saml/).

## And much more

This release note would grow to an unmanageable length if every new major development got the space it deserves. So we won't. But we want to mention them here at the least in a cursory manner:

- In SeaTable you can now easily calculate with simple operators with date and duration columns: Addition of a date and a duration? Nothing could be simpler! Create a formula column, select the two columns you want and add a "+" between them. Done. Of course, this also works with "-".
- A web form can now be time-limited. Submissions after the deadline are not possible.
- New options in single and multiple select columns can now be created by simply pasting content from the clipboard into them. A new option is created automatically and the pasted string gets saved in the cell.
- When a column permission prevents a user from changing data in a column, the column is highlighted to signal the restricted permission.
- A new function countlinks() returns the number of linked records in a link to other records column.
- Advanced column types, such as the Link to Other Records column, can now be created on mobile devices.
- Notifications can contain content from the row that triggers the notification. Simply insert the column name in curly brackets (e.g. {name}) as a placeholder in the notification template.
- A new filter condition "is the ID of the current user" has been added. In organizations where user IDs are uniquely defined (e.g. student IDs), this filter condition can be used to create a view that displays different information for each user.

Lastly, we have also fixed some bugs:

- The filter conditions of single select columns have been aligned with those of multiple select columns.
- Checkboxes and multiple select columns are now sortable.
- The search function now also includes collaborator as well as single and multiple select columns.
- The FREEZE_USER_ON_LOGIN_FAILED option works again - [thanks to user mtmail for pointing this out.](https://forum.seatable.com/t/v1-7-1-freeze-account-and-fail2ban/296)
