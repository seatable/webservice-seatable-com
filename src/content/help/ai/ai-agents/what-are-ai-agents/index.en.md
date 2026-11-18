---
title: 'What Are AI Agents?'
description: 'AI agents access your SeaTable data directly via MCP. Learn how it works and what you can do with it.'
weight: 1
url: '/help/what-are-ai-agents'
seo:
    title: 'What Are AI Agents and How Do They Work with SeaTable?'
    description: 'AI agents connect directly to your SeaTable data via the MCP Server. Read, write and analyze your data in natural language — no programming skills required.'
---

AI assistants like Claude, ChatGPT or Copilot are powerful tools — but they have a fundamental problem: they don't know your data. If you want to ask a question about your projects, customers or inventory, you first have to export the data, paste it into the chat and explain to the AI what the columns mean. This is cumbersome and error-prone.

**AI agents solve exactly this problem.** An AI agent is an AI assistant that can access your data directly through a standardized interface. In SeaTable, this is done via the **Model Context Protocol (MCP)** — an open standard supported by the entire AI industry.

## Key takeaways

- The **official SeaTable MCP Server** (`https://mcp.seatable.com/mcp`) connects ChatGPT, Claude Desktop, Claude Code, Cursor and other MCP-capable assistants to your base.
- Access applies per base, read-only or read and write, depending on the token.
- The agent works with data, not structure: it does not create or delete tables and columns.
- Free and open source (MIT license), for SeaTable Cloud and self-hosted installations.

## How does it work?

When you connect an AI agent to your SeaTable base, the following happens:

1. You ask a question in natural language, for example: *"Which tasks are overdue?"*
2. The AI agent recognizes that it needs data from your base and queries it via the MCP Server.
3. The MCP Server reads the relevant rows from SeaTable and returns them to the agent.
4. The agent evaluates the data and responds — clearly and to the point.

All of this takes just a few seconds. You don't notice any of it, except that you get a precise answer.

## What can an AI agent do with my data?

That depends on the permissions you grant. With a **read token**, the agent can query, search and analyze your data. With a **read-write token**, it can additionally create, modify or delete entries — but only after your confirmation.

In concrete terms, this means:

- **Query**: "Show me all customers from Berlin with revenue over 5,000 euros."
- **Analyze**: "How many tasks were completed this week? Group by employee."
- **Create**: "Create a new entry in the Contacts table for Müller GmbH."
- **Modify**: "Set the status of all overdue tasks to 'Escalated'."
- **Link**: "Link the new contact to the 'Website Relaunch' project."

The agent automatically recognizes the structure of your base — tables, columns, column types — and uses the correct formats. It also corrects typos in table or column names on its own in most cases.

{{< youtube 5T4pWJgfOgc >}}

## What is the difference between AI agents and AI automations?

SeaTable also offers **AI automations** — automated actions that involve AI when certain events occur, for example to summarize texts or categorize entries. These run rule-based in the background without any intervention on your part.

AI agents work differently: they are **interactive**. You ask a question, the agent answers. You give an instruction, the agent carries it out. It's a dialogue — just like with a colleague who knows your database inside and out.

| | AI Automations | AI Agents |
|---|---|---|
| **Trigger** | Automatic (rule/event) | Manual (your question) |
| **Interaction** | None — runs in the background | Dialogue in natural language |
| **Typical use** | Summarize texts, categorize | Query, analyze, edit data |
| **Setup** | Configured in SeaTable | Via external AI assistant (e.g. Claude) |

Both approaches complement each other: automations for recurring routine tasks, agents for ad-hoc questions and flexible interaction.

## What do I need to get started?

- A **SeaTable Cloud account** (or a self-hosted installation)
- An **AI assistant** that supports MCP — for example ChatGPT, Claude Desktop, Claude Code or Cursor
- An **API token** for the base that the agent should access

The setup takes just a few minutes. Step-by-step guides are available for [ChatGPT]({{< relref "help/ai/ai-agents/connect-chatgpt" >}}), [Claude Desktop]({{< relref "help/ai/ai-agents/connect-claude-desktop" >}}), [Claude Code]({{< relref "help/ai/ai-agents/connect-claude-code" >}}) and [Cursor]({{< relref "help/ai/ai-agents/connect-cursor" >}}).

## Is it safe?

The AI agent only accesses the base for which you have created an API token. Not other bases, not your account. Via the token, you control whether the agent can only read or also write.

Important to know: when the agent queries your data, the results are transmitted to the AI provider (for example Anthropic for Claude) so the language model can process them. The major providers commit to not using API data for model training. If you need maximum control, you can self-host SeaTable and combine it with a local language model.

More on security and permissions can be found in the article "Permissions and Data Privacy for AI Agents".