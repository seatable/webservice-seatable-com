---
title: 'What Is the AI Chat Plugin?'
description: 'The AI chat plugin lets you chat directly with your data in SeaTable. Ask questions in natural language and the AI answers with real data.'
weight: 1
url: '/help/ai-chat-plugin-in-seatable'
seo:
    title: 'AI Chat Plugin in SeaTable: Chat with Your Data'
    description: 'The AI chat plugin in SeaTable enables natural conversation with your data. Ask questions, analyze and edit data, directly in your base.'
star: true
---

The AI Chat Plugin (Beta) is a new extension in SeaTable (from version 6.1) that lets you use an AI-powered chat directly in your base. Ask questions in natural language, and the AI responds based on your actual data. You do not need any external software, a separate AI assistant, or any technical setup. The chat runs directly in SeaTable.

## How does the AI Chat Plugin work?

The plugin is based on the **Model Context Protocol (MCP)**, the same open standard used by [AI agents]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}). Behind the scenes, the chat accesses your data via the SeaTable MCP Server, reads tables, columns, and records, and delivers precise answers.

The key difference from AI agents: you do not need to install an external application such as Claude Desktop or Cursor. The chat is available directly as a plugin in SeaTable. You open the plugin, ask your question, and receive the answer — all within your base.

## What can the AI Chat Plugin do?

The chatbot can both **read** and **write** your data. For example, you can:

- **Query data**: "Which projects have a deadline within the next 7 days?"
- **Create analyses**: "How are the support tickets distributed by category?"
- **Create records**: "Create a new contact named Müller GmbH."
- **Modify data**: "Set the status of all completed tasks to 'Archived'."

## Supported AI models

For the AI Chat Plugin, you bring your own API key. You can choose from the following providers and models:

| Provider | Models |
|---|---|
| **Anthropic (Claude)** | Haiku, Sonnet |
| **OpenAI** | GPT-4o, GPT-4o mini |
| **Mistral** | Large, Small |

## Three AI features in SeaTable

SeaTable offers three different AI features that differ fundamentally in how they work:

| | AI Automations | AI Agents | AI Chat Plugin |
|---|---|---|---|
| **Available since** | Version 6.0 | Version 6.0 | Version 6.1 (Beta) |
| **Trigger** | Automatic (rule/event) | Manual (your question) | Manual (your question) |
| **Interaction** | None, runs in the background | Dialog in an external AI tool | Dialog directly in SeaTable |
| **Typical use** | Categorizing, summarizing, extracting | Ad-hoc analyses, complex tasks | Quick questions, editing data |
| **AI model** | SeaTable's own AI server (EU) | External provider | External provider (own API key) |
| **External software required?** | No | Yes (e.g., Claude Desktop, Cursor) | No |

[AI Automations]({{< relref "help/ai/ai-automations/introduction" >}}) are suited for recurring tasks that should run rule-based in the background. [AI Agents]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}) offer maximum flexibility through external MCP clients. The **AI Chat Plugin** bridges the gap between the two: interactive AI usage without external software, directly where your data lives.

## Beta status

The AI Chat Plugin is currently in beta. Features and the user interface may change in future versions.
