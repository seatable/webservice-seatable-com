---
title: 'Supported AI Models'
description: 'The AI chat plugin supports models from Anthropic, OpenAI, and Mistral. Learn which model is best suited for your use case.'
weight: 3
url: '/help/ai-chat-plugin-supported-models'
seo:
    title: 'Supported AI Models in the SeaTable Chat Plugin'
    description: 'Overview of supported AI models in the SeaTable chat plugin: Claude, GPT-4o, Mistral. Comparison, recommendations, and costs.'
---

The AI Chat Plugin in SeaTable supports language models from three providers: **Anthropic**, **OpenAI**, and **Mistral**. You choose which model you want to use and bring your own API key. The resulting token costs are paid directly to the respective provider, not to SeaTable.

## Model overview

Each provider offers two models: a fast, affordable model for simple tasks and a more powerful model for demanding analyses.

| Provider | Model | Strengths | Cost tendency |
|---|---|---|---|
| **Anthropic** | Claude Haiku | Fast, efficient, good for simple queries | low |
| **Anthropic** | Claude Sonnet | Powerful, precise for complex analyses | medium |
| **OpenAI** | GPT-4o mini | Fast, cost-efficient, versatile | low |
| **OpenAI** | GPT-4o | Very capable, high response quality | higher |
| **Mistral** | Mistral Small | Fast, affordable, good baseline performance | low |
| **Mistral** | Mistral Large | Powerful, good for complex tasks | higher |

## Setting up an API key

To use a model in the AI Chat Plugin, you need an API key from the respective provider. You create this directly on the provider's website:

- **Anthropic**: Create an API key at [console.anthropic.com](https://console.anthropic.com/).
- **OpenAI**: Create an API key at [platform.openai.com](https://platform.openai.com/).
- **Mistral**: Create an API key at [console.mistral.ai](https://console.mistral.ai/).

All three providers require you to add a payment method. Costs are based on the number of tokens processed and are billed directly by the provider.

## Recommendations by use case

### Simple queries and quick answers

For looking up individual values, short summaries, or simple filter questions, the affordable models are well suited: **Claude Haiku**, **GPT-4o mini**, or **Mistral Small**. These deliver fast answers at low cost.

### Complex analyses and data evaluations

If you want to evaluate large datasets, identify patterns, or perform multi-step calculations, choose **Claude Sonnet**, **GPT-4o**, or **Mistral Large**. These models deliver more precise results for demanding tasks.

### Text generation and writing tasks

For composing emails, reports, or descriptions based on your data, **Claude Sonnet** or **GPT-4o** are recommended. Both models produce linguistically high-quality text.

## Costs and billing

All token costs are billed directly between you and the respective AI provider. SeaTable does not charge any additional fees for using the AI Chat Plugin. You can find the exact per-token pricing on the pricing page of the respective provider.
