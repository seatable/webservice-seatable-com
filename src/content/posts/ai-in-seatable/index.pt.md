---
title: 'IA no SeaTable: processamento automático ou perguntar diretamente'
description: 'O SeaTable oferece duas vias para integrar a IA no seu trabalho: automações que leem faturas, classificam tickets e resumem textos, em conformidade com o RGPD no nosso servidor na Alemanha. E um chatbot de IA que compreende os seus dados e responde a perguntas em linguagem natural.'
date: 2026-03-17
lastmod: '2026-03-17'
url: '/pt/ia-no-seatable-automacoes-e-chatbot'
seo:
    title: 'IA no SeaTable: automações e chatbot para os seus dados'
    description: 'O SeaTable oferece duas vias para a IA: automações em conformidade com o RGPD no nosso servidor na Alemanha e um chatbot de IA que compreende os seus dados e responde às suas perguntas.'
categories:
    - 'low-code-no-code'
tags:
    - 'Processos informáticos'
    - 'Inteligência artificial'
    - 'No Code & Low Code'
    - 'Segurança informática e proteção de dados'
color: '#ff3d33'
---

Imagine que abre a sua base SeaTable com 2.000 registos de projetos. Mas, em vez de definir filtros, configurar vistas e escrever fórmulas, escreve:

> "Quais são os projetos em atraso? Agrupa-os por responsável."

E a IA responde. Não com uma suposição vaga, mas com os dados reais da sua base. Em poucos segundos. Isto não é ficção científica. É possível agora, com o novo plugin de chat de IA no SeaTable.

Mas comecemos pelo início. Porque a IA no SeaTable é muito mais do que um chatbot.

## Até agora: automações de IA, os assistentes invisíveis

Com o SeaTable 6.0, introduzimos as automações de IA. O princípio: define uma tarefa e a IA executa-a automaticamente em segundo plano. Linha a linha, sem que precise de esperar ativamente.

![Anlage einer neuen KI-Automationen in SeaTable](images/ai-automation-overview.png)

Estão disponíveis quatro funções: **Summarize, OCR, Extract e Classify**. A estas junta-se uma **Custom Function**, com a qual pode definir os seus próprios prompts.

![KI Funktionen in Seatable Automationen](images/automation-select-ai-function.png)

### O que significa isto na prática?

- **Processamento de faturas:** As faturas recebidas são lidas por OCR. Número da fatura, data, montante e remetente são automaticamente colocados nas colunas corretas — sem digitação manual.
- **Tickets de suporte:** Os pedidos recebidos são analisados, categorizados e atribuídos à equipa correta. Antes de alguém ver o pedido, este já está organizado.
- **Resumo de documentos:** Um relatório de 20 páginas é condensado nos pontos essenciais em poucos segundos.
- **Classificação multilingue:** Seja em alemão, inglês ou francês — a IA reconhece o idioma e classifica o conteúdo corretamente.

### Onde são executadas estas automações?

No **nosso próprio servidor de IA na Alemanha**, no centro de dados da Hetzner. Operamos um modelo de linguagem próprio que realiza o processamento. Os seus dados nunca abandonam a nossa infraestrutura europeia.

Para organizações que valorizam a conformidade com o RGPD e a soberania dos dados (universidades, instituições de investigação, setor público), isto é decisivo. Nenhum dado é enviado para a OpenAI, Google ou outros fornecedores norte-americanos.

Os clientes Enterprise recebem créditos de IA incluídos na subscrição.

## A partir de agora: o chatbot de IA. Converse com os seus dados

As automações são poderosas, mas funcionam segundo regras fixas: uma linha entra, um resultado sai. Mas e se tiver uma pergunta aberta? Se não souber que filtro deve aplicar, ou se precisar de uma análise sobre toda a sua base de dados?

Para isso existe, a partir do SeaTable 6.1, o **plugin de chat de IA** (Beta).

![AI Chat Plugin SeaTable](images/ai-chat-plugin.png)

### Como funciona

Abre o chat na sua base e faz a sua pergunta em linguagem natural. A IA conhece a estrutura da sua base (tabelas, colunas, ligações) e consulta de forma direcionada os dados relevantes. Sem exportação, sem copiar e colar, sem explicar a estrutura das tabelas.

Alguns exemplos:

- *"Quantos negócios abertos temos acima de 10.000 euros que não tiveram contacto nos últimos 30 dias?"*
- *"Resume os pedidos de suporte da última semana e mostra os temas mais frequentes."*
- *"Cria um registo de follow-up na tabela de atividades para cada tarefa em atraso."*

Sim, o chatbot não só pode ler, como também **escrever**: criar linhas, atualizar, ligar e eliminar. Tudo diretamente na sua base.

### Como é isto possível?

Por detrás do chatbot está o **SeaTable MCP Server**. MCP significa Model Context Protocol — um padrão aberto que permite aos modelos de IA interagir ativamente com fontes de dados. Em vez de copiar os seus dados para o chat, a IA consulta autonomamente, via MCP, aquilo de que precisa. Em tempo real, sempre atualizado.

Isto diferencia fundamentalmente a nossa abordagem de soluções em que se exportam dados como CSV e se colam numa janela do ChatGPT. O chatbot trabalha diretamente com a sua base — sem desvios e sem perda de informação.

### Que modelos são suportados?

O chatbot utiliza modelos de IA potentes, capazes de responder a perguntas complexas e de trabalhar com os seus dados em vários passos. Atualmente suportamos:

- **Anthropic Claude** (Haiku e Sonnet)
- **OpenAI** (GPT-4o e GPT-4o mini)
- **Mistral** (Mistral Large e Mistral Small)

Utiliza a sua própria chave de API e paga os custos de tokens diretamente ao respetivo fornecedor. Isto é transparente: vê exatamente quanto custa cada interação e mantém o controlo total.

## Porquê duas vias em vez de uma?

Uma pergunta legítima. Porque não fazer tudo simplesmente através do chatbot?

A resposta: porque tarefas diferentes têm requisitos diferentes.

| | Automações de IA | Chatbot de IA |
|---|---|---|
| **Tarefa** | Definida: OCR, resumo, classificação | Aberta: perguntas, análises, pesquisa exploratória |
| **Interação** | Em segundo plano, automática | Diálogo em tempo real |
| **Dados** | Uma linha como input | Toda a base como fundamento |
| **Modelo de IA** | O nosso servidor na Alemanha | O seu modelo (Claude, OpenAI ou Mistral) |
| **Soberania dos dados** | Máxima: os dados permanecem na nossa infraestrutura | O utilizador decide: os dados são enviados para o fornecedor de IA escolhido |
| **Custos** | Incluídos na subscrição Enterprise | Custos de tokens junto do fornecedor de IA |

Ambas as vias complementam-se. Utilize as automações para tarefas recorrentes que devem funcionar de forma fiável em segundo plano. Utilize o chatbot quando tiver perguntas que não consegue responder com um filtro.

## Os seus dados permanecem sob o seu controlo

Independentemente da via que escolher: o controlo e a segurança estão em primeiro lugar.

**Nas automações**, os seus dados nunca abandonam a nossa infraestrutura europeia. O modelo de linguagem funciona no nosso próprio servidor na Alemanha.

**No chatbot**, os dados são transmitidos ao fornecedor de IA que escolheu. Isso é tecnicamente necessário para que o modelo possa responder às suas perguntas. Mas é o utilizador que decide qual é o fornecedor.

![Fluxo de dados no chatbot de IA](images/dataflow-ai-agent.png)

E não é só isso: o plugin de chat de IA distingue automaticamente entre operações de leitura e ações destrutivas como eliminações ou atualizações. Antes de os dados serem alterados, o plugin pede a sua confirmação — indicando exatamente o que será alterado e quantas linhas serão afetadas. Pode aprovar uma única vez, autorizar para toda a sessão ou recusar. Também no caso de conjuntos de resultados particularmente grandes, é pedida confirmação antes de a IA processar milhares de linhas.

## Como começar

### Automações de IA

Disponíveis para todos os clientes Enterprise no SeaTable Cloud e para instalações self-hosted a partir da versão 6.0. Crie uma nova automação na sua base, selecione uma função de IA (Summarize, OCR, Extract, Classify ou Custom) e defina a coluna de entrada e de saída. A automação passa a funcionar automaticamente a cada novo registo.

Com o SeaTable 6.1, disponibilizaremos as automações (e, consequentemente, também as automações de IA) em menor escala para os clientes Free e Plus.

Encontrará instruções detalhadas na nossa [área de ajuda]({{< relref "help/ai/ai-automations" >}}).

### Chatbot de IA

A partir do SeaTable 6.1, pode instalar o plugin de chat de IA (Beta) na sua base. Introduza a sua chave de API (Claude, OpenAI ou Mistral) nas definições do plugin. Faça a sua primeira pergunta. O chatbot reconhece automaticamente a estrutura da sua base e responderá à sua pergunta.

## Perspetivas futuras

Estamos a trabalhar continuamente na expansão das funcionalidades de IA no SeaTable:

- **Gestão melhorada de chaves de API:** Atualmente, a chave de API é armazenada nas definições do plugin. Para uma versão futura, estamos a desenvolver uma solução central e mais segura para a gestão de chaves de API.
- **AI Usage Tracking:** Visão transparente do seu consumo de tokens.
- **Assistente de IA geral:** Um assistente que permite conversar com várias bases em simultâneo.

As possibilidades de integrar a IA no seu trabalho diário crescem rapidamente. Com o SeaTable, tem as ferramentas para tirar partido disso — sem comprometer o controlo sobre os seus dados.

{{< newsletter />}}
