---
title: 'Troubleshooting'
description: 'Solutions for common problems with the AI chat plugin in SeaTable.'
weight: 6
url: '/help/ai-chat-plugin-troubleshooting'
seo:
    title: 'AI Chat Plugin: Troubleshooting and Common Issues'
    description: 'Solutions for common problems with the AI chat plugin: API key errors, missing responses, and plugin issues.'
---

If the AI Chat Plugin is not working as expected, you will find solutions for the most common problems here. For general information on setup, see the article [Set up the AI Chat Plugin]({{< relref "help/ai/ai-chat/setup" >}}).

## API key problems

### Invalid API key

If the error message indicates an invalid API key, check the following:

- Make sure the key was entered correctly and does not contain any accidental spaces.
- Verify that the API key is still active. Some providers deactivate keys after a certain period of inactivity.
- Ensure that the selected **provider** in the plugin settings matches the API key. For example, an OpenAI key does not work with the Anthropic provider.

### Credit or quota exhausted

Most AI providers work with prepaid credit. If responses are no longer being generated, check your balance in the dashboard of the respective provider:

- [Anthropic Console](https://console.anthropic.com/)
- [OpenAI Platform](https://platform.openai.com/)
- [Mistral Console](https://v2.auth.mistral.ai/login)

## No or incorrect answers

### The AI cannot find the data

Make sure that the requested data actually exists in the base. Mention the exact table and column name in your question so the AI can identify the correct data.

### Inaccurate or incorrect results

Formulate your question as precisely as possible. Avoid vague phrasing and specify exactly which table and which columns are relevant. For complex tasks, it can help to break the request into several simple steps.

### Timeout or no response

Very large queries can lead to a timeout. Simplify the request or limit yourself to a single table. Also note that smaller models such as Haiku, GPT-4o mini, or Mistral Small may reach their limits with complex, multi-step tasks.

## Plugin problems

### The plugin is not displayed

Check whether the plugin is installed and activated in the Plugin Manager. To do so, open the **Plugins** section in the base header and search for **AI Chat**.

### The plugin does not load

Reload the page in your browser. If the problem persists, try a different browser or clear your browser cache.

### Settings are not saved

Make sure that after entering the API key, you confirmed the settings with **Save**. Without saving, the entries are lost when you close the settings dialog.

## General tips

- Start with a simple question like "What tables are there?" to verify the connection to the AI provider.
- If the AI delivers unexpected results, ask it to explain its approach.
- Break complex tasks into several small steps to achieve better results.
