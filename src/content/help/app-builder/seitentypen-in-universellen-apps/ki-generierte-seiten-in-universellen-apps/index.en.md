---
title: 'AI-generated pages in SeaTable apps'
date: 2026-11-20
lastmod: '2026-11-20'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/help/ai-generated-pages-in-seatable-apps'
seo:
    title: 'Adding AI-Generated Pages to SeaTable Apps'
    description: 'Let an AI generate fully customized user interfaces based on HTML, JavaScript and CSS in your app – without writing any code.'
weight: 15
---

AI-generated pages are a groundbreaking feature of SeaTable that completes the no-code approach to app development. The AI enables you to create custom user interfaces based on HTML, JavaScript and CSS without having to write a single line of code.

## How do AI-generated pages in apps work?

For your apps in SeaTable, you can have custom pages created exactly as you envision them by chatting with an AI. You describe in natural language what the page should do and how it should look, and the AI builds it for you. To do so, the AI uses the Software Development Kit (SDK) for HTML pages. Technically speaking, the result is therefore an [HTML page]({{< relref "help/app-builder/seitentypen-in-universellen-apps/html-seiten-in-universellen-apps" >}}).

{{< warning headline="Data protection and AI infrastructure in Germany" >}}

For page generation, SeaTable relies on **Qwen 3.8 27B**, an open-weights model with 27 billion parameters developed by Alibaba. The AI model is hosted in German data centers by Exoscale – the same provider that also supplies the servers of SeaTable Cloud. The data in your bases never reaches the AI model in the first place, as it only processes your prompts and base schemas.

{{< /warning >}}

## How to create an AI-generated page

To create pages in SeaTable apps, you must have already [added an app to a base]({{< relref "help/app-builder/app-verwaltung/apps-zu-einer-base-hinzufuegen" >}}) and opened it in [editing mode]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}). If you now want the AI to build a tailor-made page, proceed as follows:

1. Click the **AI icon** on the left side of the page.
   ![Open the AI page generator in an app](images/open-ai-generator-in-apps.png)
2. Click the orange **Add project** button.
   ![Add a project to build a page with AI](images/add-project-to-build-app-page-via-ai.png)
3. Give the project a **name**, which the AI-generated page will later bear as well. Optionally, you can add further **project notes**.
   ![Add name and project notes](images/name-ai-generated-app-page-project.png)
4. Confirm with **Submit** and the AI page generator opens.
5. First, choose a **UI style** that defines the visual appearance of the page.
   ![Choose a UI style for the AI-generated page](images/choose-ui-style-for-ai-generated-app-page.png)
6. Click **Next**. Now define the **data sources** of the page. To do so, check the required **tables** and configure their **permissions**.
   ![Configure the data sources of the AI-generated page](images/data-source-setup-for-ai-generated-app-page.png)
7. Click **Next**. Now enter a **prompt** that describes the page you want to create. Then click **Generate page**.
   ![The AI creates the desired page based on the prompt](images/ai-generates-app-page.gif)
8. As soon as the AI has finished the first draft, it displays a **preview**. You can then refine the page with further prompts in the **chat**.
9. When you are satisfied with the result, click **Publish** in the top right. If you like, you can adjust the **page name** and select an **icon** before publishing the page.
   ![Publish the AI-generated page](images/publish-ai-generated-app-page.gif)
10. Click the **exit icon** at the bottom left of the page to leave the AI page generator and view the **AI-generated page in the app**.
   ![Leave the AI generator and view the app page](images/leave-ai-generator-to-view-app-page.gif)

## Settings of the AI-generated page

To open the **page settings**, hover your mouse over the page name in the navigation bar and click the **gear icon** that appears.

![Open the page settings of the AI-generated page](images/open-page-settings-in-apps.png)

### Configure available tables

As a rule, an AI-generated page is **dynamic** – that is, it adapts when the data in the underlying tables changes. Conversely, you can also allow data in the tables to be changed via the AI-generated page.

To edit the permissions of the available tables, click the **gear icon** of the respective table in the page settings.

![Open the permissions of the available tables](images/open-table-permissions-of-ai-generated-pages.png)

There are five permissions available, which you can enable or disable using the sliders:
- **Can add records**
- **Can list records**
- **Can modify records**
- **Can delete records**
- **Can query records**

![Adjust the permissions of the available tables](images/table-permissions-of-ai-generated-pages.png)

By **hiding columns**, you can control at a granular level which fields may be added, viewed, edited or queried.

{{< warning headline="Note" >}}

You have the same options when setting up the data sources while creating the AI-generated page.

{{< /warning >}}

### Allow button actions

You can also have the AI add [buttons]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) to your page. This allows you, for example, to send an email or run scripts at the click of a button on AI-generated pages. However, the email accounts and scripts you want to use must already be set up in the base.

You can allow the following actions separately using a slider:
- **Send notifications**
- **Send emails**
- **Run scripts**

![Allow button actions on AI-generated pages](images/action-permissions-on-ai-generated-app-page.png)

### Page permission

Last but not least, you can define who may see the AI-generated page. You can find out more about the various page permissions in the app [here]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}).

## Manage AI projects in the app

As soon as you have created a **project** for an AI-generated page, it appears as a new **tile** on the overview page, which you can access via the **AI icon** on the left side of the page. Hover your mouse over the tile and click the **three dots** that appear. Here you can **modify details** (name and project notes) or **delete** the project.

![Change the details or delete the project for an AI-generated page](images/modify-details-or-delete-project-for-ai-generated-app-page.png)

### Continue working on a project

It is not uncommon to want to revise or further develop an AI-generated page, for example because you have ideas for additional functions or elements. Fortunately, SeaTable **saves the entire chat and all versions of the page**. This means you can pick up where you left off at any time or jump back to an earlier version if a change does not meet your expectations.

{{< warning headline="Retention period" >}}

Conversations and unpublished pages are retained for 365 days.

{{< /warning >}}

Click the **tile** to open the desired project and then click **Continue**.

![Continue a project for creating an AI-generated page](images/continue-ai-generated-app-page.png)

You now have various options:
- **Clock icon**: view or delete your previous chats with the AI.
- **Versions icon**: return to, view or delete older page versions.
- **Gear icon**: adjust the UI style, the data sources or the action permissions.
- **Input field**: try out further prompts in the chat with the AI.

![Options for continuing with the AI-generated page](images/options-to-continue-with-ai-generated-app-page.png)

If you want to know what happened behind the scenes when a page version was created, click **Thought process** in the chat.

![Open the thought process behind creating an AI-generated page](images/thought-process-when-ai-generating-app-page.png)

For each step, the expandable elements show you the system prompt, your input and the result returned by the AI. The **statistics** add how long the step took and how many tokens it consumed.

![Statistics of the thought process behind creating an AI-generated page](images/statistics-for-thought-process-when-ai-generating-app-page.png)

## Further develop an AI-generated page yourself

You can **display the HTML code of an AI-generated page** at any time. To do so, click the **code icon** in the top left of the preview window. You can return to the visual preview via the **eye icon**.

![Display the HTML code of an AI-generated page](images/show-html-code-of-an-ai-generated-app-page.gif)

If you have programming skills, you can use the HTML code to develop the page further yourself. To do so, you can **download the page as an HTML file**. Simply click the **download icon** in the top right corner – and the HTML file is saved on your device.

![Download the AI-generated page as an HTML file](images/download-ai-generated-app-page.png)

As soon as you have finished programming the HTML page outside of SeaTable, you can **upload a zip file** that contains the HTML, JavaScript and CSS files.

![Upload the HTML page as a zip file and replace the AI-generated page](images/upload-zip-file-to-ai-generated-app-page.gif)

1. Hover your mouse over the name of the AI-generated page and click the **three dots** that appear.
2. Select the **Update page file** option.
3. Click the field with the **plus icon** and upload a **file for the HTML page**.
4. Confirm with **Submit**.

You can find further information in the [article on HTML pages]({{< relref "help/app-builder/seitentypen-in-universellen-apps/html-seiten-in-universellen-apps" >}}).
