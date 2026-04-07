---
title: 'Modelos de IA suportados'
description: 'O plugin de chat IA suporta modelos da Anthropic, OpenAI e Mistral. Saiba qual modelo é mais adequado para o seu caso de utilização.'
weight: 3
url: '/pt/ajuda/plugin-chat-ia-modelos-suportados'
seo:
    title: 'Modelos de IA suportados no plugin de chat SeaTable'
    description: 'Visão geral dos modelos de IA suportados no plugin de chat SeaTable: Claude, GPT-4o, Mistral. Comparação, recomendações e custos.'
---

O plugin de chat IA no SeaTable suporta modelos de linguagem de três fornecedores: **Anthropic**, **OpenAI** e **Mistral**. É o utilizador que escolhe qual modelo pretende utilizar e fornece a sua própria chave API. Os custos de tokens resultantes são pagos diretamente ao respetivo fornecedor, não ao SeaTable.

## Visão geral dos modelos

Cada fornecedor oferece dois modelos: um modelo rápido e económico para tarefas simples e um modelo mais potente para análises exigentes.

| Fornecedor | Modelo | Pontos fortes | Tendência de custo |
|---|---|---|---|
| **Anthropic** | Claude Haiku | Rápido, eficiente, bom para consultas simples | baixo |
| **Anthropic** | Claude Sonnet | Potente, preciso para análises complexas | médio |
| **OpenAI** | GPT-4o mini | Rápido, económico, versátil | baixo |
| **OpenAI** | GPT-4o | Muito capaz, elevada qualidade de resposta | mais elevado |
| **Mistral** | Mistral Small | Rápido, acessível, bom desempenho de base | baixo |
| **Mistral** | Mistral Large | Potente, bom para tarefas complexas | mais elevado |

## Configurar uma chave API

Para utilizar um modelo no plugin de chat IA, necessita de uma chave API do respetivo fornecedor. Esta é criada diretamente no site do fornecedor:

- **Anthropic**: Crie uma chave API em [console.anthropic.com](https://console.anthropic.com/).
- **OpenAI**: Crie uma chave API em [platform.openai.com](https://platform.openai.com/).
- **Mistral**: Crie uma chave API em [v2.auth.mistral.ai/login](https://v2.auth.mistral.ai/login).

Todos os três fornecedores exigem a adição de um método de pagamento. Os custos baseiam-se no número de tokens processados e são faturados diretamente pelo fornecedor.

## Recomendações por caso de utilização

### Consultas simples e respostas rápidas

Para procurar valores individuais, resumos curtos ou perguntas com filtros simples, os modelos económicos são adequados: **Claude Haiku**, **GPT-4o mini** ou **Mistral Small**. Estes fornecem respostas rápidas a baixo custo.

### Análises complexas e avaliações de dados

Se pretende avaliar grandes conjuntos de dados, identificar padrões ou realizar cálculos em várias etapas, escolha **Claude Sonnet**, **GPT-4o** ou **Mistral Large**. Estes modelos fornecem resultados mais precisos para tarefas exigentes.

### Geração de texto e tarefas de redação

Para compor e-mails, relatórios ou descrições com base nos seus dados, recomenda-se o **Claude Sonnet** ou o **GPT-4o**. Ambos os modelos produzem texto de elevada qualidade linguística.

## Custos e faturação

Todos os custos de tokens são faturados diretamente entre si e o respetivo fornecedor de IA. O SeaTable não cobra quaisquer taxas adicionais pela utilização do plugin de chat IA. Pode consultar os preços exatos por token na página de preços do respetivo fornecedor.
