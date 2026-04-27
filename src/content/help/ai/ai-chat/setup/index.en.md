---
title: 'Set Up the AI Chat Plugin'
description: 'Learn how to install and configure the AI chat plugin in your SeaTable base.'
weight: 2
url: '/help/set-up-ai-chat-plugin'
seo:
    title: 'Set Up the AI Chat Plugin: Step-by-Step Guide'
    description: 'Install the AI chat plugin in your SeaTable base, enter your API key, and start your first conversation with your data.'
---

With the AI Chat Plugin, you can chat directly with your data in SeaTable. This guide shows you how to install the plugin, enter an API key, and start your first conversation. For a general overview of the plugin, see the [introduction article]({{< relref "help/ai/ai-chat/introduction" >}}).

{{< warning headline="Beta version" text="The AI Chat Plugin has been available as a beta version since SeaTable 6.1. Features and the interface may still change." />}}

## Prerequisites

- A SeaTable account with access to at least one base
- An **API key** from one of the supported AI providers:
  - [Anthropic](https://console.anthropic.com/) (Claude)
  - [OpenAI](https://platform.openai.com/) (GPT)
  - [Mistral](https://v2.auth.mistral.ai/login) (Mistral)

## Step 1: Install the plugin in your base

1. Open the base where you want to use the AI Chat Plugin.
2. Click **Plugins** in the base header.
3. Search for **AI Chat** in the Plugin Manager and click **Add**.

The plugin now appears in your plugin bar and can be opened at any time.

![The installed AI Chat Plugin in the base header](images/ai-chat-plugin-installed.png)

## Step 2: Select an AI model and enter your API key

1. Open the AI Chat Plugin.
2. Select the desired model from one of the three AI providers (Anthropic, OpenAI, or Mistral). More powerful models generally deliver better results but incur higher costs per request.
3. Enter your **API key** in the designated field.

![Select AI model and enter API key](images/ai-model-and-api-key.png)

{{< warning headline="Note" text="During the beta phase, the API key is stored in the base. All users of the base share the same API key. However, the chat history is individual and is not shared between users." />}}

## Step 3: Start your first conversation

Enter your first question in the input field and press **Enter**.

The plugin analyzes the structure and data of your base and answers your question in the chat window.

## Tips for getting started

Start with a simple question to test the connection and familiarize yourself with the plugin. Good first questions include:

- "What tables are in my base?"
- "How many records does the table [table name] have?"
- "Summarize the data in the table [table name]."

The more precisely you formulate your question, the more accurate the answer will be. Whenever possible, mention the specific table or column name your question refers to.
