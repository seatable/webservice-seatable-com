---
title: 'O que é o plugin de chat IA?'
description: 'O plugin de chat IA permite conversar diretamente com os seus dados no SeaTable. Faça perguntas em linguagem natural e a IA responde com dados reais.'
weight: 1
url: '/pt/ajuda/plugin-chat-ia-no-seatable'
seo:
    title: 'Plugin de chat IA no SeaTable: converse com os seus dados'
    description: 'O plugin de chat IA no SeaTable permite uma conversa natural com os seus dados. Faça perguntas, analise e edite dados, diretamente na sua base.'
star: true
---

O plugin de chat IA é uma extensão do SeaTable orientada para o futuro que permite utilizar um chat baseado em IA diretamente na sua base. Faça perguntas em linguagem natural e a IA responde com base nos seus dados reais. Não necessita de software externo, de um assistente de IA separado ou de qualquer configuração técnica. O chat funciona diretamente no SeaTable.

**Neste vídeo explicativo, mostramos-lhe, em apenas alguns minutos, como utilizar o plugin de chat com IA (com legendas em português).**
{{< youtube lihaPreD4J4 >}}

## Como funciona o plugin de chat IA?

O plugin baseia-se no **Model Context Protocol (MCP)**, o mesmo padrão aberto utilizado pelos [agentes de IA]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}). Nos bastidores, o chat acede aos seus dados através do SeaTable MCP Server, lê tabelas, colunas e registos, e fornece respostas precisas.

A diferença fundamental em relação aos agentes de IA: não precisa de instalar uma aplicação externa como o Claude Desktop ou o Cursor. O chat está disponível diretamente como plugin no SeaTable. Abra o plugin, faça a sua pergunta e receba a resposta — tudo dentro da sua base.

## O que pode fazer o plugin de chat IA?

O chatbot pode tanto **ler** como **escrever** os seus dados. Por exemplo, pode:

- **Consultar dados**: "Quais projetos têm um prazo nos próximos 7 dias?"
- **Criar análises**: "Como estão distribuídos os pedidos de suporte por categoria?"
- **Criar registos**: "Cria um novo contacto chamado Müller GmbH."
- **Modificar dados**: "Define o estado de todas as tarefas concluídas como 'Arquivado'."

## Modelos de IA suportados

No SeaTable Cloud, o plugin utiliza por predefinição o **SeaTable AI**, que já se encontra instalado. Este baseia-se no **Qwen 3.8 27B**, um modelo de pesos abertos com 27 mil milhões de parâmetros desenvolvido pela Alibaba. O modelo de IA é alojado em centros de dados alemães da Exoscale – o mesmo fornecedor que também disponibiliza os servidores do SeaTable Cloud. Foi concebido para raciocínio avançado, programação, investigação, processamento de documentos e tarefas complexas de vários passos, e é disponibilizado ao abrigo da licença Apache 2.0.

Além disso, pode utilizar a sua própria **chave API** para o plugin de chat IA, de modo a ligar um **modelo de IA externo na nuvem**. Pode escolher entre os seguintes fornecedores e modelos:

| Fornecedor | Modelos |
|---|---|
| **Anthropic (Claude)** | Haiku, Sonnet |
| **OpenAI** | GPT-6.1 Sol, GPT-6 Luna |
| **Mistral** | Large, Small |

## Três funcionalidades de IA no SeaTable

O SeaTable oferece três funcionalidades de IA diferentes que se distinguem fundamentalmente no seu modo de funcionamento:

| | Automatizações de IA | Agentes de IA | Plugin de chat IA |
|---|---|---|---|
| **Disponível desde** | Versão 6.0 | Versão 6.0 | Versão 6.1 |
| **Acionamento** | Automático (regra/evento) | Manual (a sua pergunta) | Manual (a sua pergunta) |
| **Interação** | Nenhuma, executa em segundo plano | Diálogo numa ferramenta de IA externa | Diálogo diretamente no SeaTable |
| **Utilização típica** | Categorizar, resumir, extrair | Análises ad-hoc, tarefas complexas | Perguntas rápidas, edição de dados |
| **Modelo de IA** | Servidor SeaTable AI (UE) | Fornecedor externo | Servidor SeaTable AI (UE) *ou* fornecedor externo (chave API própria) |
| **Software externo necessário?** | Não | Sim (p. ex., Claude Desktop, Cursor) | Não |

As [automatizações de IA]({{< relref "help/ai/ai-automations/introduction" >}}) são adequadas para tarefas recorrentes que devem ser executadas em segundo plano com base em regras. Os [agentes de IA]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}) oferecem a máxima flexibilidade através de clientes MCP externos. O **plugin de chat IA** preenche a lacuna entre ambos: utilização interativa de IA sem software externo – diretamente onde os seus dados se encontram.
