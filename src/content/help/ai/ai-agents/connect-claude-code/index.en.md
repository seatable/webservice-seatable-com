---
title: 'Connect SeaTable with Claude Code'
description: 'Connect Claude Code to your SeaTable base via the MCP server — explained step by step.'
weight: 3
url: '/en/help/connect-ai-agent-with-claude-code'
seo:
    title: 'Connect SeaTable with Claude Code — Setup in 5 Minutes'
    description: 'How to connect Claude Code to your SeaTable base via MCP server: create an API token, add the MCP server via CLI, and ask your first question.'
---

In this guide, you will connect Claude Code to your SeaTable base. Once set up, you can ask Claude questions about your data and have it edit entries directly from the terminal. The setup takes about five minutes.

## Prerequisites

- A SeaTable Cloud account with at least one base
- Claude Code (installable via `npm install -g @anthropic-ai/claude-code`, details at [docs.anthropic.com](https://code.claude.com/docs/en/overview))
- An Anthropic account (required to use Claude)

## Step 1: Create an API token in SeaTable

The API token gives Claude access to a specific base. You decide whether Claude can only read or also write data.
For instructions on creating an API token, see the article [Creating an API Token]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}).

{{< warning headline="Keep your token safe" >}}

An API token is valid indefinitely and should be treated like a password. If you lose it or it is accidentally exposed, you can delete the API token at any time and create a new one.

{{< /warning >}}

## Step 2: Add the MCP server via CLI

Claude Code is configured via the command line. Open a terminal and run the following command:

```bash
claude mcp add seatable \
  --transport http \
  https://mcp.seatable.com/mcp \
  -H "Authorization: Bearer INSERT-YOUR-API-TOKEN-HERE"
```

Replace `INSERT-YOUR-API-TOKEN-HERE` with the token from Step 1.

You can connect multiple bases at the same time. Run the command again for each base using a unique name, for example `seatable-crm` and `seatable-projects` instead of `seatable`.

## Step 3: Verify the connection

Start Claude Code and type the `/mcp` command. This will display all configured MCP servers along with their status. If the connection is successful, you will see **Status: connected** and **Auth: authenticated**.

![Successful connection to the SeaTable MCP server in Claude Code](images/claude-code-connected-to-mcp-seatable-com.png)

From the `/mcp` menu, you can also perform additional actions, such as viewing the available tools, reconnecting (**Reconnect**), or disabling the server.

Now ask a first test question:

> *"What tables are in my base?"*

Claude will then query the table structure via the MCP server and list all tables with their columns. If this works, the connection is established.

## Asking your first questions

You can now ask Claude questions about your data as if you were talking to a colleague. Here are a few examples to try:

- *"How many entries does the Contacts table have?"*
- *"Show me all entries where the status is 'Open'."*
- *"Summarize the data in the Revenue table by month."*

Your questions should refer to tables and columns that actually exist in your base. If you are unsure, simply ask Claude about the structure of the base first. It knows your tables and columns and can point out what is available.

You don't need to type table and column names exactly. Claude recognizes minor typos and corrects them automatically. Feel free to write "Contacts" instead of "contacts" or "Projects" instead of "projects". Claude will find the right table.

## Next steps

- [Use cases for AI agents]({{< relref "help/ai/ai-agents/use-cases" >}})
- [Asking good questions: How to get the best answers]({{< relref "help/ai/ai-agents/good-questions" >}})
- [Troubleshooting AI agents]({{< relref "help/ai/ai-agents/troubleshooting" >}})
- [Permissions and data privacy for AI agents]({{< relref "help/ai/ai-agents/data-security" >}})
