---
title: 'Ligar o SeaTable ao Claude Desktop'
description: 'Ligue o Claude Desktop à sua base SeaTable através do servidor MCP — explicado passo a passo.'
weight: 2
url: '/pt/ajuda/ligar-agente-ia-ao-claude-desktop'
seo:
    title: 'Ligar o SeaTable ao Claude Desktop — Configuração em 5 minutos'
    description: 'Como ligar o Claude Desktop à sua base SeaTable através do servidor MCP: criar um token API, adicionar a configuração e fazer a sua primeira pergunta.'
---

Neste guia, vai ligar o Claude Desktop à sua base SeaTable. Após a configuração, pode fazer perguntas ao Claude sobre os seus dados e pedir-lhe que edite entradas diretamente a partir do chat. A configuração demora cerca de cinco minutos.

## Pré-requisitos

- Uma conta SeaTable Cloud com pelo menos uma base
- Claude Desktop (disponível gratuitamente em [claude.ai/download](https://claude.ai/download/))
- Uma conta Anthropic (necessária para utilizar o Claude)

{{< warning headline="O plano gratuito é suficiente, mas requer uma configuração especial" >}}

A conta gratuita da Anthropic suporta atualmente ligações a servidores MCP personalizados, mas estes precisam de ser configurados manualmente através de ficheiros de configuração.

{{< /warning >}}

## Passo 1: Criar um token API no SeaTable

O token API dá ao Claude acesso a uma base específica. Pode decidir se o Claude apenas pode ler ou também escrever dados.
Para instruções sobre como criar um token API, consulte o artigo [Criar um token API]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens" >}}).

{{< warning headline="Guarde o seu token em segurança" >}}

Um token API é válido indefinidamente e deve ser tratado como uma palavra-passe. Se o perder ou se for acidentalmente exposto, pode eliminar o token API a qualquer momento e criar um novo.

{{< /warning >}}

## Passo 2: Configurar o Claude Desktop

O Claude Desktop utiliza um ficheiro de configuração JSON para integrar servidores MCP.

1. Abra o Claude Desktop.
2. Vá a **Settings** → **Developer**

![Adicionar um servidor MCP personalizado no Claude Desktop](images/claude-add-custom-mcp.png)

3. O ficheiro `claude_desktop_config.json` abre-se no seu editor de texto.
4. Adicione a seguinte configuração:

```json
{
  "mcpServers": {
    "seatable": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": [
        "C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx-cli.js",
        "mcp-remote",
        "https://mcp.seatable.com/mcp",
        "--header",
        "Authorization: Bearer INSIRA-O-SEU-TOKEN-API-AQUI"
      ]
    }
  }
}
```

5. Substitua `INSIRA-O-SEU-TOKEN-API-AQUI` pelo token do passo 1.
6. Guarde o ficheiro e reinicie o Claude Desktop.

Pode ligar várias bases ao mesmo tempo. Crie uma entrada separada em `mcpServers` para cada base com um nome único, por exemplo `seatable-crm` e `seatable-projetos`.

## Passo 3: Verificar a ligação

Após reiniciar, verá a ligação ao **SeaTable** em `Tools` no Claude Desktop. Isto indica que o servidor MCP está ligado. Clique nele para ver as ferramentas disponíveis — deverá encontrar ferramentas do SeaTable como `list_tables`, `list_rows` ou `query_sql`.

Em alternativa, pode verificar o estado da ligação nas definições.

![Estado da ligação ao servidor MCP](images/claude-mcp-connected.png)

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
