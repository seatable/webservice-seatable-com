---
title: 'Ligar o SeaTable ao Claude Code'
description: 'Ligue o Claude Code à sua base SeaTable através do servidor MCP — explicado passo a passo.'
weight: 3
url: '/pt/ajuda/ligar-agente-ia-ao-claude-code'
seo:
    title: 'Ligar o SeaTable ao Claude Code — Configuração em 5 minutos'
    description: 'Como ligar o Claude Code à sua base SeaTable através do servidor MCP: criar um token API, adicionar o servidor MCP via CLI e fazer a sua primeira pergunta.'
---

Neste guia, vai ligar o Claude Code à sua base SeaTable. Após a configuração, pode fazer perguntas ao Claude sobre os seus dados e pedir-lhe que edite entradas diretamente a partir do terminal. A configuração demora cerca de cinco minutos.

## Pré-requisitos

- Uma conta SeaTable Cloud com pelo menos uma base
- Claude Code (instalável via `npm install -g @anthropic-ai/claude-code`, detalhes em [docs.anthropic.com](https://code.claude.com/docs/en/overview))
- Uma conta Anthropic (necessária para utilizar o Claude)

## Passo 1: Criar um token API no SeaTable

O token API dá ao Claude acesso a uma base específica. Pode decidir se o Claude apenas pode ler ou também escrever dados.
Para instruções sobre como criar um token API, consulte o artigo [Criar um token API]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}).

{{< warning headline="Guarde o seu token em segurança" >}}

Um token API é válido indefinidamente e deve ser tratado como uma palavra-passe. Se o perder ou se for acidentalmente exposto, pode eliminar o token API a qualquer momento e criar um novo.

{{< /warning >}}

## Passo 2: Adicionar o servidor MCP via CLI

O Claude Code é configurado através da linha de comandos. Abra um terminal e execute o seguinte comando:

```bash
claude mcp add seatable \
  --transport http \
  https://mcp.seatable.com/mcp \
  -H "Authorization: Bearer INSIRA-O-SEU-TOKEN-API-AQUI"
```

Substitua `INSIRA-O-SEU-TOKEN-API-AQUI` pelo token do passo 1.

Pode ligar várias bases ao mesmo tempo. Execute o comando novamente para cada base usando um nome único, por exemplo `seatable-crm` e `seatable-projetos` em vez de `seatable`.

## Passo 3: Verificar a ligação

Inicie o Claude Code e escreva o comando `/mcp`. Serão apresentados todos os servidores MCP configurados juntamente com o seu estado. Se a ligação for bem-sucedida, verá **Status: connected** e **Auth: authenticated**.

![Ligação bem-sucedida ao servidor MCP do SeaTable no Claude Code](images/claude-code-connected-to-mcp-seatable-com.png)

A partir do menu `/mcp`, também pode realizar outras ações, como ver as ferramentas disponíveis, restabelecer a ligação (**Reconnect**) ou desativar o servidor.

Faça agora uma primeira pergunta de teste:

> *«Que tabelas existem na minha base?»*

O Claude irá então consultar a estrutura das tabelas através do servidor MCP e listar todas as tabelas com as suas colunas. Se isto funcionar, a ligação está estabelecida.

## Fazer as suas primeiras perguntas

Agora pode fazer perguntas ao Claude sobre os seus dados como se estivesse a falar com um colega. Aqui estão alguns exemplos para experimentar:

- *«Quantas entradas tem a tabela Contactos?»*
- *«Mostra-me todas as entradas em que o estado é "Aberto".»*
- *«Resume os dados da tabela Receitas por mês.»*

As suas perguntas devem referir-se a tabelas e colunas que realmente existam na sua base. Se não tiver a certeza, pergunte primeiro ao Claude sobre a estrutura da base. Ele conhece as suas tabelas e colunas e pode indicar-lhe o que está disponível.

Não precisa de escrever os nomes de tabelas e colunas de forma exata. O Claude reconhece pequenos erros de digitação e corrige-os automaticamente. Escreva à vontade «Contactos» em vez de «contactos» ou «Projetos» em vez de «projects». O Claude encontrará a tabela correta.

## Próximos passos

- [Exemplos de utilização de agentes de IA]({{< relref "help/ai/ai-agents/use-cases" >}})
- [Fazer boas perguntas: como obter as melhores respostas]({{< relref "help/ai/ai-agents/good-questions" >}})
- [Resolução de problemas de agentes de IA]({{< relref "help/ai/ai-agents/troubleshooting" >}})
- [Permissões e proteção de dados para agentes de IA]({{< relref "help/ai/ai-agents/data-security" >}})
