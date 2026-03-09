---
title: 'O que são automatizações de IA?'
description: 'As automatizações de IA processam dados na sua base automaticamente — desde categorizar até resumir.'
weight: 1
url: '/pt/ajuda/automatizacoes-ia-no-seatable'
seo:
    title: 'Automatizações de IA no SeaTable: processar dados automaticamente'
    description: 'As automatizações de IA do SeaTable categorizam, traduzem e resumem os seus dados automaticamente — em conformidade com o RGPD em servidores na Alemanha.'
star: true
---

Desde a versão 6.0, o SeaTable oferece ações de automatização baseadas em IA que podem processar os seus dados automaticamente. Resumir textos, categorizar pedidos de suporte, extrair dados de faturas ou traduzir conteúdo — tudo isto acontece diretamente na sua base, acionado pelas regras de automatização que já conhece do SeaTable. Sem plataforma de IA externa, sem acompanhamento manual.

{{< youtube A1_LWaFWveM >}}

## Como funcionam as automatizações de IA?

As automatizações de IA são ações dentro do sistema de automatização do SeaTable. Seguem o mesmo princípio que todas as outras automatizações: um **gatilho** inicia uma ou mais **ações**. A diferença é que as ações de IA utilizam um modelo de linguagem para compreender e processar conteúdo.

Um fluxo de trabalho típico é o seguinte:

1. Uma nova entrada é criada numa tabela (gatilho).
2. Uma ação de IA lê o conteúdo de uma coluna específica — por exemplo o texto de um pedido de suporte.
3. O modelo de linguagem analisa o texto e escreve o resultado noutra coluna — por exemplo a categoria "Problema técnico" ou um resumo em três frases.

Isto acontece de forma totalmente automática em segundo plano. Não precisa de intervir nem de formular perguntas — a IA trabalha com base em regras segundo as especificações que definiu na automatização.

## O que pode a IA automatizar?

No SeaTable, cria uma automatização com a ação Run AI e escolhe uma das cinco funções disponíveis:

- **Summarize**: Textos longos, relatórios ou notas são automaticamente condensados ao essencial. Útil quando uma coluna contém descrições detalhadas e precisa de um breve resumo noutra coluna.
- **Classify**: Os textos recebidos são analisados e atribuídos a uma categoria. Exemplo típico: os pedidos de suporte são automaticamente classificados como "Técnico", "Faturação" ou "Geral" e armazenados numa coluna de seleção única.
- **OCR**: O texto é reconhecido e extraído de imagens ou documentos digitalizados — por exemplo de uma foto de um cartão de visita ou de uma guia de remessa digitalizada.
- **Extract**: Informações específicas são extraídas de texto não estruturado — por exemplo número de fatura, data e montante de uma fatura.
- **Custom**: Para todos os casos que não se enquadram nas quatro funções padrão, define o seu próprio prompt. Isto permite-lhe fazer a IA traduzir textos, redigir sugestões de resposta ou avaliar conteúdo segundo os seus próprios critérios.

## Automatizações de IA vs. agentes de IA

O SeaTable oferece duas formas de permitir que a IA trabalhe com os seus dados. Ambas complementam-se mas funcionam de forma fundamentalmente diferente:

**As automatizações de IA** executam-se automaticamente em segundo plano, acionadas por regras. São adequadas para tarefas recorrentes que devem decorrer da mesma forma para cada nova entrada — por exemplo categorizar cada pedido de suporte recebido ou resumir cada nova nota.

**Os agentes de IA** trabalham de forma interativa. Faz uma pergunta, o agente responde. Isto é adequado para análises pontuais, consultas flexíveis e tarefas únicas — por exemplo "Que clientes não tiveram faturação este mês?"

| | Automatizações de IA | Agentes de IA |
|---|---|---|
| **Gatilho** | Automático (regra/evento) | Manual (a sua pergunta) |
| **Interação** | Nenhuma — executa-se em segundo plano | Diálogo em linguagem natural |
| **Uso típico** | Categorizar, resumir, extrair | Consultar, analisar, editar |
| **Modelo de IA** | Servidor de IA próprio do SeaTable (UE) | Fornecedor externo (p. ex. Anthropic) |
| **Processamento de dados** | Inteiramente na UE | Os dados são transmitidos ao fornecedor de IA |

Saiba mais sobre agentes de IA no artigo [O que são agentes de IA?]({{< relref "help/ai/ai-agents/what-are-ai-agents" >}}).

## Proteção de dados: IA feita na Europa

Uma vantagem essencial das automatizações de IA em relação aos serviços de IA externos: **os seus dados não saem da UE.** O SeaTable opera o seu próprio servidor de IA com o modelo open source Gemma-3-12B em infraestrutura GPU na Hetzner na Alemanha.

Em termos concretos, isto significa:

- Os seus dados não são transmitidos à OpenAI, Google ou outros fornecedores dos EUA.
- Não é realizado treino com os seus dados — o modelo é pré-treinado e não aprende com as suas entradas.
- O processamento está em conformidade com o RGPD e sujeito exclusivamente ao direito europeu.

Para organizações que trabalham com dados pessoais, documentos confidenciais ou informações comerciais sensíveis, esta é uma diferença decisiva em comparação com soluções de IA onde os dados fluem para os EUA.

## Disponibilidade

As automatizações de IA estão disponíveis a partir do SeaTable versão 6.0. Os clientes Enterprise podem utilizar as funcionalidades sem custo adicional. Uma quota limitada estará disponível para os planos Free e Plus a partir da versão 6.1.

## Próximos passos

- Configurar automatizações de IA — guia passo a passo