---
title: 'Connect SeaTable with Claude Desktop'
description: 'Connect Claude Desktop to your SeaTable base via the MCP server — explained step by step.'
weight: 2
url: '/en/help/connect-ai-agent-with-claude-desktop'
seo:
    title: 'Connect SeaTable with Claude Desktop — Setup in 5 Minutes'
    description: 'How to connect Claude Desktop to your SeaTable base via MCP server: create an API token, add the configuration, and ask your first question.'
---

In this guide, you will connect Claude Desktop to your SeaTable base. Once set up, you can ask Claude questions about your data and have it edit entries directly from the chat. The setup takes about five minutes.

## Prerequisites

- A SeaTable Cloud account with at least one base
- Claude Desktop (available for free at [claude.ai/download](https://claude.ai/download/))
- A Anthropic account (required to use Claude)

{{< warning headline="The free plan is sufficient but requires special configuration" >}}

The free Anthropic account currently supports connections to custom MCP servers, but they need to be configured manually through configuration files.

{{< /warning >}}

## Step 1: Create an API token in SeaTable

The API token gives Claude access to a specific base. You decide whether Claude can only read or also write data.
For instructions on creating an API token, see the article [Creating an API Token]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}).

{{< warning headline="Keep your token safe" >}}

An API token is valid indefinitely and should be treated like a password. If you lose it or it is accidentally exposed, you can delete the API token at any time and create a new one.

{{< /warning >}}

## Step 2: Configure Claude Desktop

Claude Desktop uses a JSON configuration file to integrate MCP servers.

1. Open Claude Desktop.
2. Go to **Settings** → **Developer**

![Adding a custom MCP server in Claude Desktop](images/claude-add-custom-mcp.png)

3. The file `claude_desktop_config.json` opens in your text editor.
4. Add the following configuration:

```json
{
  "mcpServers": {
    "seatable": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": [
        "C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx-cli.js",
        "mcp-remote",
        "https://mcp.seatable.com/mcp",
        "--header",
        "Authorization: Bearer INSERT-YOUR-API-TOKEN-HERE"
      ]
    }
  }
}
```

5. Replace `INSERT-YOUR-API-TOKEN-HERE` with the token from Step 1.
6. Save the file and restart Claude Desktop.

You can connect multiple bases at the same time. Create a separate entry under `mcpServers` for each base with a unique name, for example `seatable-crm` and `seatable-projects`.

## Step 3: Verify the connection

After restarting, you will see the connection to **SeaTable** under `Tools` in Claude Desktop. This indicates that the MCP server is connected. Click on it to see the available tools — you should find SeaTable tools such as `list_tables`, `list_rows`, or `query_sql`.

Alternatively, you can check the connection status in the settings.

![MCP server connection status](images/claude-mcp-connected.png)

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