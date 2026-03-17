---
title: 'Permissions and Data Privacy'
description: 'Learn how the AI chat plugin handles your data and what security mechanisms protect your information.'
weight: 5
url: '/help/ai-chat-plugin-permissions-data-privacy'
seo:
    title: 'AI Chat Plugin: Permissions and Data Privacy'
    description: 'How the AI chat plugin protects your data: confirmation dialogs, data flow transparency, and control over the AI provider.'
---

The AI Chat Plugin connects your SeaTable data with an external language model. This article explains how the data flow works, what protection mechanisms are in place, and how you maintain control over your data.

## How does your data flow?

When you ask a question in the AI Chat, the data flow proceeds in four steps:

1. **Your question** is sent to the selected AI provider.
2. The plugin queries the relevant data from your base.
3. **The query results** are transmitted to the AI provider so that the language model can evaluate them.
4. The model formulates a response and sends it back to the plugin.

This means: the data that the plugin queries for your question is transmitted to the external AI provider. This is technically necessary because a language model can only process data that it receives.

## Choice of AI provider

You decide which provider and which model you use. The available options are Anthropic (Claude), OpenAI, and Mistral. Each provider has its own data privacy policies. The major providers contractually commit that data processed through their API **is not used to train models**. Nevertheless, review the current terms of use of your chosen provider.

## Confirmation before changes

The plugin clearly distinguishes between read and write operations. Before a destructive action is executed (e.g., modifying or deleting rows), the plugin displays a **confirmation dialog**. This informs you about what changes will be made and how many rows are affected.

You have three options:

- **Approve once**: Only this single action is executed.
- **Approve for the entire session**: Further actions of this type are executed without additional confirmation.
- **Decline**: The action is not executed.

The plugin also asks for confirmation before processing large result sets with thousands of rows. This way, you maintain control at all times.

## Maximum control through self-hosting

If you want to prevent data from being transmitted to external providers, you can self-host SeaTable and combine it with a local language model. In this configuration, your data never leaves your own network.

## Further information

A detailed discussion of data security when using AI with SeaTable can be found in the article [Permissions and data privacy for AI agents]({{< relref "help/ai/ai-agents/data-security" >}}). Among other topics, it covers API token permissions, strategies for minimizing data exposure, and self-hosting in detail.
