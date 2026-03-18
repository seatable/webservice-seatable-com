---
title: 'Examples and Tips'
description: 'Practical examples and tips for effectively using the AI chat plugin in SeaTable.'
weight: 4
url: '/help/ai-chat-plugin-examples-and-tips'
seo:
    title: 'AI Chat Plugin: Examples and Tips for Good Questions'
    description: 'Learn how to get the most out of the AI chat plugin in SeaTable with concrete examples: query, analyze, and edit data.'
---

The AI Chat Plugin understands natural language and works directly with the data in your base. In this article, you will find concrete examples for typical use cases as well as tips for achieving better results. General advice on formulating good questions can also be found in the article [How to ask good questions]({{< relref "help/ai/ai-agents/good-questions" >}}).

## Querying data

The most common use case: you ask a question and the chat returns the matching records from your base.

> *"Show me all open tasks that are due this week."*

> *"How many customers do we have from Germany?"*

> *"Which invoices are still unpaid?"*

> *"Are there any projects without an assigned owner?"*

The more precisely you mention table and column names, the more accurate the answer will be. If you are unsure which columns exist, simply ask:

> *"Describe the structure of my base."*

## Analyzing data

The chat can not only display your data but also evaluate, group, and summarize it.

> *"What was the total revenue last quarter, broken down by sales representative?"*

> *"Summarize the support requests from the last week."*

> *"Which products were ordered most frequently?"*

> *"How are the open tickets distributed by priority?"*

Such analyses work especially well when your base contains cleanly maintained data. If values are missing or inconsistent, the chat will usually point this out.

## Creating and editing data

The AI Chat Plugin can also create, modify, link, and delete records. Be as specific as possible about which table, which columns, and which values are affected.

### Creating new records

> *"Create a new contact: Name 'Müller GmbH', City 'Hamburg', Status 'Prospect'."*

> *"Create a follow-up entry in the Activities table for each open deal."*

### Modifying existing records

> *"Set the status of all overdue tasks to 'Escalated'."*

> *"Change the priority of ticket #412 to 'High'."*

### Linking and deleting records

> *"Link all invoices to the corresponding customer from the Contacts table."*

> *"Delete all test entries from the Drafts table."*

When deleting, the chat asks for confirmation before executing the action. Nevertheless, verify beforehand with a read query whether the correct records are affected.

## Tips for better results

**Start with read queries.** Before having the AI modify data, first check whether the chat finds the correct records. Ask *"Which tasks are overdue?"* before saying *"Set the status to Escalated."*

**Break complex tasks into smaller steps.** For multi-step requests, you will get better results by proceeding step by step. The chat remembers the context of the conversation, and you can build on previous answers.

**Use table and column names.** The exact spelling is not required, but using the correct terms helps the chat interpret your question accurately.

**Leverage the context.** After a query, you can refer to previous results with "these", "of those", or "the same" without repeating everything.

## What does not work

The AI Chat Plugin works exclusively with the data in your SeaTable base. The following things are not possible:

- **Querying non-existent data.** If a column or table does not exist, the chat cannot provide an answer. It does not fabricate data.
- **Actions outside of SeaTable.** The chat cannot send emails, access external systems, or open files.
- **Very large bulk operations.** Individual requests that attempt to create or modify hundreds of records at once may reach their limits. Break such tasks into smaller steps.
