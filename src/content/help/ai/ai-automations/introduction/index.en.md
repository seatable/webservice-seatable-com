---
title: 'What Are AI Automations?'
description: 'AI automations process data in your base automatically — from categorizing to summarizing.'
weight: 1
url: '/help/ai-automations-in-seatable'
seo:
    title: 'AI Automations in SeaTable: Process Data Automatically'
    description: 'SeaTable AI automations categorize, translate and summarize your data automatically — GDPR-compliant on servers in Germany.'
star: true
---

Since version 6.0, SeaTable offers AI-powered automation actions that can process your data automatically. Summarize texts, categorize support requests, extract invoice data or translate content — all of this happens directly in your base, triggered by the automation rules you already know from SeaTable. No external AI platform needed, no manual follow-up.

{{< youtube A1_LWaFWveM >}}

## How do AI automations work?

AI automations are actions within SeaTable's automation system. They follow the same principle as all other automations: a **trigger** initiates one or more **actions**. The difference is that AI actions use a language model to understand and process content.

A typical workflow looks like this:

1. A new entry is created in a table (trigger).
2. An AI action reads the content of a specific column — for example the text of a support request.
3. The language model analyzes the text and writes the result to another column — for example the category "Technical issue" or a summary in three sentences.

This happens fully automatically in the background. You don't need to intervene or formulate any questions — the AI works rule-based according to the specifications you defined in the automation.

## What can the AI automate?

In SeaTable, you create an automation with the Run AI action and choose one of five available functions:

- **Summarize**: Longer texts, reports or notes are automatically condensed to the essentials. Useful when a column contains detailed descriptions and you need a brief summary in another column.
- **Classify**: Incoming texts are analyzed and assigned to a category. Typical example: support requests are automatically classified as "Technical", "Billing" or "General" and stored in a single-select column.
- **OCR**: Text is recognized and extracted from images or scanned documents — for example from a photo of a business card or a scanned delivery note.
- **Extract**: Specific information is pulled from unstructured text — for example invoice number, date and amount from an invoice.
- **Custom**: For all cases that don't fit the four standard functions, you define your own prompt. This lets you have the AI translate texts, draft reply suggestions or evaluate content according to your own criteria.

## AI automations vs. AI agents

SeaTable offers two ways to let AI work with your data. Both complement each other but work fundamentally differently:

**AI automations** run automatically in the background, triggered by rules. They are suited for recurring tasks that should run the same way for every new entry — for example categorizing every incoming support request or summarizing every new note.

**AI agents** work interactively. You ask a question, the agent answers. This is suited for ad-hoc analyses, flexible queries and one-off tasks — for example "Which customers had no revenue this month?"

| | AI Automations | AI Agents |
|---|---|---|
| **Trigger** | Automatic (rule/event) | Manual (your question) |
| **Interaction** | None — runs in the background | Dialogue in natural language |
| **Typical use** | Categorize, summarize, extract | Query, analyze, edit |
| **AI model** | SeaTable's own AI server (EU) | External provider (e.g. Anthropic) |
| **Data processing** | Entirely within the EU | Data is transmitted to the AI provider |

Learn more about AI agents in the article [What are AI agents?]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}).

## Data privacy: AI made in Europe

A key advantage of AI automations over external AI services: **your data does not leave the EU.** SeaTable operates its own AI server running the open-source model Gemma-3-12B on GPU infrastructure at Hetzner in Germany.

In concrete terms, this means:

- Your data is not transmitted to OpenAI, Google or other US providers.
- No training takes place with your data — the model is pre-trained and does not learn from your inputs.
- Processing is GDPR-compliant and subject exclusively to European law.

For organizations working with personal data, confidential documents or sensitive business information, this is a decisive difference compared to AI solutions where data flows to the US.

## Availability

AI automations are available from SeaTable version 6.0. Enterprise customers can use the features at no additional cost. A limited quota will be available for Free and Plus plans from version 6.1.

## Next steps

- Set up AI automations — step-by-step guide