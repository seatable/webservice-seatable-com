---
title: 'Modelos de IA suportados'
description: 'O plugin de chat IA suporta modelos da Anthropic, OpenAI e Mistral. Saiba qual modelo é mais adequado para o seu caso de utilização.'
weight: 3
url: '/pt/ajuda/plugin-chat-ia-modelos-suportados'
seo:
    title: 'Modelos de IA suportados no plugin de chat SeaTable'
    description: 'Visão geral dos modelos de IA suportados no plugin de chat SeaTable: Claude, GPT, Mistral. Comparação, recomendações e custos.'
---

O plugin de chat IA utiliza por predefinição o **SeaTable AI**, que já se encontra instalado. Além disso, suporta modelos de linguagem de três fornecedores externos: **Anthropic**, **OpenAI** e **Mistral**. É o utilizador que escolhe qual modelo pretende utilizar. Os custos de tokens resultantes são debitados diretamente na sua subscrição do SeaTable ou pagos ao respetivo fornecedor externo do seu modelo.

## SeaTable AI

O SeaTable AI pré-instalado baseia-se no **Qwen 3.8 27B**, um modelo de pesos abertos com 27 mil milhões de parâmetros desenvolvido pela Alibaba. O modelo de IA é alojado em centros de dados alemães da Exoscale – o mesmo fornecedor que também disponibiliza os servidores do SeaTable Cloud. Foi concebido para raciocínio avançado, programação, investigação, processamento de documentos e tarefas complexas de vários passos, e é disponibilizado ao abrigo da licença Apache 2.0.

Além disso, pode utilizar a sua própria **chave API** para o plugin de chat IA, de modo a ligar um **modelo de IA externo na nuvem**.

## Visão geral dos modelos dos fornecedores externos

Cada fornecedor oferece dois modelos: um modelo rápido e económico para tarefas simples e um modelo mais potente para análises exigentes.

| Fornecedor | Modelo | Pontos fortes | Tendência de custo |
|---|---|---|---|
| **Anthropic** | Claude Haiku | rápido, eficiente, bom para consultas simples | baixo |
| **Anthropic** | Claude Sonnet | potente, preciso para análises complexas | médio |
| **OpenAI** | GPT-6 Luna | rápido, económico, versátil | baixo |
| **OpenAI** | GPT-6.1 Sol | muito capaz, elevada qualidade de resposta | mais elevado |
| **Mistral** | Mistral Small | rápido, acessível, bom desempenho de base | baixo |
| **Mistral** | Mistral Large | potente, bom para tarefas complexas | mais elevado |

## Configurar uma chave API

Para utilizar um modelo externo no plugin de chat IA, necessita de uma **chave API** do respetivo fornecedor. Esta é criada diretamente no site do fornecedor:

- **Anthropic**: Crie uma chave API em [console.anthropic.com](https://console.anthropic.com/).
- **OpenAI**: Crie uma chave API em [platform.openai.com](https://platform.openai.com/).
- **Mistral**: Crie uma chave API em [v2.auth.mistral.ai/login](https://v2.auth.mistral.ai/login).

Todos os três fornecedores exigem a adição de um **método de pagamento**. Os custos baseiam-se no número de tokens consumidos e são faturados diretamente pelo fornecedor.

## Recomendações por caso de utilização

### Consultas simples e respostas rápidas

Para procurar valores individuais, resumos curtos ou perguntas com filtros simples, os modelos económicos são adequados: **Claude Haiku**, **GPT-6 Luna** ou **Mistral Small**. Estes fornecem respostas rápidas a baixo custo.

### Análises complexas e avaliações de dados

Se pretende avaliar grandes conjuntos de dados, identificar padrões ou realizar cálculos em várias etapas, escolha **Claude Sonnet**, **GPT-6.1 Sol** ou **Mistral Large**. Estes modelos fornecem resultados mais precisos para tarefas exigentes.

### Geração de texto e tarefas de redação

Para compor e-mails, relatórios ou descrições com base nos seus dados, recomenda-se o **Claude Sonnet** ou o **GPT-6.1**. Ambos os modelos produzem texto de elevada qualidade linguística.

## Custos e faturação

### Com o SeaTable AI

Os tokens consumidos pela IA são convertidos em **créditos de IA** e deduzidos do seu saldo: 1 milhão de tokens de entrada corresponde a 500 créditos de IA e 1 milhão de tokens de saída a 1500 créditos de IA.

O número de créditos de IA disponíveis depende da [subscrição do SeaTable]({{< relref "pages/prices" >}}) da sua equipa. Com o SeaTable Plus, são **50 créditos de IA por utilizador** por mês e, com o SeaTable Enterprise, **500 créditos de IA por utilizador**.

Pode consultar a qualquer momento o saldo restante e o consumo na **barra situada no painel lateral esquerdo** do plugin de chat IA.

![Créditos de IA consumidos e restantes no SeaTable AI](images/seatable-ai-credits.png)

### Com modelos de IA externos

Todos os custos de tokens são faturados diretamente entre si e o respetivo fornecedor de IA. O SeaTable não cobra quaisquer taxas adicionais pela utilização do plugin de chat IA. Pode consultar os preços exatos por token na página de preços do respetivo fornecedor.
