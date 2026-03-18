---
title: 'Configurar o plugin de chat IA'
description: 'Saiba como instalar e configurar o plugin de chat IA na sua base SeaTable.'
weight: 2
url: '/pt/ajuda/configurar-plugin-chat-ia'
seo:
    title: 'Configurar o plugin de chat IA: guia passo a passo'
    description: 'Instale o plugin de chat IA na sua base SeaTable, introduza a sua chave API e inicie a sua primeira conversa com os seus dados.'
---

Com o plugin de chat IA, pode conversar diretamente com os seus dados no SeaTable. Este guia mostra-lhe como instalar o plugin, introduzir uma chave API e iniciar a sua primeira conversa. Para uma visão geral do plugin, consulte o [artigo de introdução]({{< relref "help/ai/ai-chat/introduction" >}}).

{{< warning headline="Versão beta" text="O plugin de chat IA está disponível como versão beta desde o SeaTable 6.1. As funcionalidades e a interface ainda podem ser alteradas." />}}

## Pré-requisitos

- Uma conta SeaTable com acesso a pelo menos uma base
- Uma **chave API** de um dos fornecedores de IA suportados:
  - [Anthropic](https://console.anthropic.com/) (Claude)
  - [OpenAI](https://platform.openai.com/) (GPT)
  - [Mistral](https://console.mistral.ai/) (Mistral)

## Passo 1: Instalar o plugin na sua base

1. Abra a base onde pretende utilizar o plugin de chat IA.
2. Clique em **Plugins** no cabeçalho da base.
3. Procure por **AI Chat** no Gestor de Plugins e clique em **Adicionar**.

O plugin aparece agora na sua barra de plugins e pode ser aberto a qualquer momento.

![O plugin de chat IA instalado no cabeçalho da base](images/ai-chat-plugin-installed.png)

## Passo 2: Selecionar um modelo de IA e introduzir a chave API

1. Abra o plugin de chat IA.
2. Selecione o modelo pretendido de um dos três fornecedores de IA (Anthropic, OpenAI ou Mistral). Modelos mais potentes geralmente apresentam melhores resultados, mas implicam custos mais elevados por pedido.
3. Introduza a sua **chave API** no campo designado.

![Selecionar modelo de IA e introduzir chave API](images/ai-model-and-api-key.png)

{{< warning headline="Nota" text="Durante a fase beta, a chave API é armazenada na base. Todos os utilizadores da base partilham a mesma chave API. No entanto, o histórico de conversas é individual e não é partilhado entre utilizadores." />}}

## Passo 3: Iniciar a sua primeira conversa

Introduza a sua primeira pergunta no campo de entrada e prima **Enter**.

O plugin analisa a estrutura e os dados da sua base e responde à sua pergunta na janela de chat.

## Dicas para começar

Comece com uma pergunta simples para testar a ligação e familiarizar-se com o plugin. Boas primeiras perguntas incluem:

- "Que tabelas existem na minha base?"
- "Quantos registos tem a tabela [nome da tabela]?"
- "Resume os dados da tabela [nome da tabela]."

Quanto mais precisamente formular a sua pergunta, mais exata será a resposta. Sempre que possível, mencione o nome específico da tabela ou coluna a que a sua pergunta se refere.
