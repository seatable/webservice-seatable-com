---
title: 'Supported AI Models'
description: 'The AI chat plugin supports models from Anthropic, OpenAI, and Mistral. Learn which model is best suited for your use case.'
weight: 3
url: '/help/ai-chat-plugin-supported-models'
seo:
    title: 'Supported AI Models in the SeaTable Chat Plugin'
    description: 'Overview of supported AI models in the SeaTable chat plugin: Claude, GPT, Mistral. Comparison, recommendations, and costs.'
---

The AI Chat Plugin uses the already installed **SeaTable AI** by default. It also supports language models from three external providers: **Anthropic**, **OpenAI**, and **Mistral**. You choose which model you want to use. The resulting token costs are either charged directly against your SeaTable subscription or paid to the external provider of your model.

## SeaTable AI

The preinstalled SeaTable AI is powered by **Qwen 3.8 27B**, an open-weights model with 27 billion parameters developed by Alibaba. The AI model is hosted in German data centers operated by Exoscale – the same provider that also supplies the servers for SeaTable Cloud. It is designed for advanced reasoning, coding, research, document processing, and complex multi-step tasks, and it is released under the Apache 2.0 license.

In addition, you can bring your own **API key** for the AI Chat Plugin to connect an **external cloud AI model**.

## Model overview of external providers

Each provider offers two models: a fast, affordable model for simple tasks and a more powerful model for demanding analyses.

| Provider | Model | Strengths | Cost tendency |
|---|---|---|---|
| **Anthropic** | Claude Haiku | fast, efficient, good for simple queries | low |
| **Anthropic** | Claude Sonnet | powerful, precise for complex analyses | medium |
| **OpenAI** | GPT-6 Luna | fast, cost-efficient, versatile | low |
| **OpenAI** | GPT-6.1 Sol | very capable, high response quality | higher |
| **Mistral** | Mistral Small | fast, affordable, good baseline performance | low |
| **Mistral** | Mistral Large | powerful, good for complex tasks | higher |

## Setting up an API key

To use an external model in the AI Chat Plugin, you need an **API key** from the respective provider. You create this directly on the provider's website:

- **Anthropic**: Create an API key at [console.anthropic.com](https://console.anthropic.com/).
- **OpenAI**: Create an API key at [platform.openai.com](https://platform.openai.com/).
- **Mistral**: Create an API key at [v2.auth.mistral.ai/login](https://v2.auth.mistral.ai/login).

All three providers require you to add a **payment method**. Costs are based on the number of tokens consumed and are billed directly by the provider.

## Recommendations by use case

### Simple queries and quick answers

For looking up individual values, short summaries, or simple filter questions, the affordable models are well suited: **Claude Haiku**, **GPT-6 Luna**, or **Mistral Small**. These deliver fast answers at low cost.

### Complex analyses and data evaluations

If you want to evaluate large datasets, identify patterns, or perform multi-step calculations, choose **Claude Sonnet**, **GPT-6.1 Sol**, or **Mistral Large**. These models deliver more precise results for demanding tasks.

### Text generation and writing tasks

For composing emails, reports, or descriptions based on your data, **Claude Sonnet** or **GPT-6.1** are recommended. Both models produce linguistically high-quality text.

## Costs and billing

### For SeaTable AI

The tokens consumed by the AI are converted into **AI credits** and deducted from your balance: 1 million input tokens correspond to 500 AI credits, and 1 million output tokens to 1,500 AI credits.

The number of AI credits available to you depends on your team's [SeaTable subscription]({{< relref "pages/prices" >}}). With SeaTable Plus, you get **50 AI credits per user** each month, and with SeaTable Enterprise, **500 AI credits per user**.

You can check how much of your balance is left and how much you have used at any time on the **bar in the left sidebar** of the AI Chat Plugin.

![Used and remaining AI credits with SeaTable AI](images/seatable-ai-credits.png)

### For external AI models

All token costs are billed directly between you and the respective AI provider. SeaTable does not charge any additional fees for using the AI Chat Plugin. You can find the exact per-token pricing on the pricing page of the respective provider.
