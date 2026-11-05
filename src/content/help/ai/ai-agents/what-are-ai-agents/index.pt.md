---
title: 'O que são agentes de IA?'
description: 'Os agentes de IA acedem diretamente aos seus dados do SeaTable via MCP. Saiba como funciona e o que pode fazer com isso.'
weight: 1
url: '/pt/ajuda/o-que-sao-agentes-de-ia'
seo:
    title: 'O que são agentes de IA e como funcionam com o SeaTable?'
    description: 'Os agentes de IA ligam-se diretamente aos seus dados do SeaTable através do servidor MCP. Leia, escreva e analise os seus dados em linguagem natural — sem conhecimentos de programação.'
---

Os assistentes de IA como Claude, ChatGPT ou Copilot são ferramentas poderosas — mas têm um problema fundamental: não conhecem os seus dados. Se quiser fazer uma pergunta sobre os seus projetos, clientes ou inventário, primeiro tem de exportar os dados, colá-los no chat e explicar à IA o que significam as colunas. Isto é moroso e propenso a erros.

**Os agentes de IA resolvem exatamente este problema.** Um agente de IA é um assistente de IA que pode aceder diretamente aos seus dados através de uma interface padronizada. No SeaTable, isto é feito através do **Model Context Protocol (MCP)** — um padrão aberto suportado por toda a indústria de IA.

## O essencial em resumo

- O **servidor MCP oficial do SeaTable** (`https://mcp.seatable.com/mcp`) liga o ChatGPT, Claude Desktop, Claude Code, Cursor e outros assistentes compatíveis com MCP à sua base.
- O acesso aplica-se por base, apenas leitura ou leitura e escrita, consoante o token.
- O agente trabalha com os dados, não com a estrutura: não cria nem apaga tabelas ou colunas.
- Gratuito e de código aberto (licença MIT), para o SeaTable Cloud e instalações auto-alojadas.

## Como funciona?

Quando liga um agente de IA à sua base SeaTable, acontece o seguinte:

1. Faz uma pergunta em linguagem natural, por exemplo: *"Que tarefas estão atrasadas?"*
2. O agente de IA reconhece que precisa de dados da sua base e consulta-os através do servidor MCP.
3. O servidor MCP lê as linhas relevantes do SeaTable e devolve-as ao agente.
4. O agente avalia os dados e responde — de forma clara e objetiva.

Tudo isto demora apenas alguns segundos. Não nota nada, a não ser que recebe uma resposta precisa.

## O que pode um agente de IA fazer com os meus dados?

Isso depende das permissões que concede. Com um **token de leitura**, o agente pode consultar, pesquisar e analisar os seus dados. Com um **token de leitura e escrita**, pode adicionalmente criar, modificar ou eliminar entradas — mas apenas após a sua confirmação.

Em termos concretos, isto significa:

- **Consultar**: "Mostra-me todos os clientes de Berlim com faturação superior a 5.000 euros."
- **Analisar**: "Quantas tarefas foram concluídas esta semana? Agrupar por colaborador."
- **Criar**: "Cria uma nova entrada na tabela Contactos para Müller GmbH."
- **Modificar**: "Altera o estado de todas as tarefas atrasadas para 'Escalado'."
- **Vincular**: "Vincula o novo contacto ao projeto 'Redesign do Website'."

O agente reconhece automaticamente a estrutura da sua base — tabelas, colunas, tipos de colunas — e utiliza os formatos corretos. Também corrige erros de digitação nos nomes de tabelas ou colunas de forma autónoma na maioria dos casos.

{{< youtube 5T4pWJgfOgc >}}

## Qual é a diferença entre agentes de IA e automatizações de IA?

O SeaTable também oferece **automatizações de IA** — ações automatizadas que envolvem a IA quando determinados eventos ocorrem, por exemplo para resumir textos ou categorizar entradas. Estas executam-se em segundo plano com base em regras, sem qualquer intervenção da sua parte.

Os agentes de IA funcionam de forma diferente: são **interativos**. Faz uma pergunta, o agente responde. Dá uma instrução, o agente executa-a. É um diálogo — como com um colega que conhece a sua base de dados de cor e salteado.

| | Automatizações de IA | Agentes de IA |
|---|---|---|
| **Gatilho** | Automático (regra/evento) | Manual (a sua pergunta) |
| **Interação** | Nenhuma — executa-se em segundo plano | Diálogo em linguagem natural |
| **Uso típico** | Resumir textos, categorizar | Consultar, analisar, editar dados |
| **Configuração** | Configurada no SeaTable | Através de um assistente de IA externo (p. ex. Claude) |

Ambas as abordagens complementam-se: as automatizações para tarefas de rotina recorrentes, os agentes para perguntas pontuais e interação flexível.

## O que preciso para começar?

- Uma **conta SeaTable Cloud** (ou uma instalação auto-alojada)
- Um **assistente de IA** que suporte MCP — por exemplo ChatGPT, Claude Desktop, Claude Code ou Cursor
- Um **token API** para a base à qual o agente deve aceder

A configuração demora apenas alguns minutos. Há guias passo a passo para [ChatGPT]({{< relref "help/ai/ai-agents/connect-chatgpt" >}}), [Claude Desktop]({{< relref "help/ai/ai-agents/connect-claude-desktop" >}}), [Claude Code]({{< relref "help/ai/ai-agents/connect-claude-code" >}}) e [Cursor]({{< relref "help/ai/ai-agents/connect-cursor" >}}).

## É seguro?

O agente de IA apenas acede à base para a qual criou um token API. Não a outras bases, não à sua conta. Através do token, controla se o agente apenas pode ler ou também escrever.

Importante saber: quando o agente consulta os seus dados, os resultados são transmitidos ao fornecedor de IA (por exemplo Anthropic para Claude) para que o modelo de linguagem os possa processar. Os principais fornecedores comprometem-se a não utilizar os dados da API para o treino de modelos. Se necessita do máximo controlo, pode auto-alojar o SeaTable e combiná-lo com um modelo de linguagem local.

Mais informações sobre segurança e permissões no artigo "Permissões e proteção de dados para agentes de IA".