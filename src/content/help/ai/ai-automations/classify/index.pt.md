---
title: 'Classificar entradas (Classify)'
description: 'Com a função de IA Classify, atribua automaticamente categorias às entradas da sua base SeaTable.'
weight: 4
url: '/pt/ajuda/automatizacao-ia-classificar-entradas'
seo:
    title: 'Automatização IA: Classificar automaticamente entradas no SeaTable'
    description: 'Como classificar automaticamente entradas no SeaTable: configurar uma automatização IA com a função Classify — definir categorias e atribuir textos automaticamente.'
---

A função de IA **Classify** analisa o conteúdo de uma ou mais colunas e atribui cada entrada a uma categoria. O resultado é escrito numa coluna de seleção simples ou seleção múltipla. Desta forma, pode classificar automaticamente os textos recebidos sem ter de ler cada entrada manualmente.

## Casos de uso típicos

- **Tickets de suporte**: Classificar automaticamente os pedidos como "Technical", "Billing", "General" ou "Feature Request".
- **Feedback e avaliações**: Categorizar o feedback dos clientes por sentimento (positivo, neutro, negativo).
- **Caixa de entrada de e-mail**: Ordenar as mensagens recebidas por tema ou urgência.
- **Candidaturas**: Classificar as cartas de apresentação por área de especialização ou nível de experiência.

## Pré-requisitos

- Uma tabela com pelo menos uma **coluna de texto** que sirva como entrada.
- Uma **coluna de seleção simples** ou **coluna de seleção múltipla** para o resultado.

{{< warning headline="Importante" text="As categorias nas quais a IA deve classificar já devem estar criadas como **opções de seleção** na coluna de seleção simples ou de seleção múltipla. A IA só pode atribuir opções existentes." />}}

## Guia passo a passo

### 1. Criar categorias na coluna de seleção

Antes de configurar a automatização, crie todas as **categorias** desejadas como opções na coluna de seleção simples (ou seleção múltipla). Por exemplo: "Technical", "Billing", "General", "Feature Request".

![Coluna de seleção simples com categorias configuradas](images/ai-automation-classify-options.png)

### 2. Criar uma automatização e escolher um gatilho

Crie uma nova regra de automatização conforme descrito no artigo [Configurar uma automatização IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Um gatilho típico é **Quando uma linha é adicionada**, para que cada nova entrada seja classificada imediatamente.

### 3. Adicionar a ação «Chamar IA»

Clique em **Adicionar ação** e selecione **Chamar IA**.

### 4. Selecionar a função «Classify»

Nas configurações da ação, escolha:

- **Tabela**: A tabela na qual a IA deve trabalhar.
- **Função**: **Classify**

![Opções de ação para a função Classify](images/ai-automation-classify.png)

### 5. Definir as colunas de entrada

Selecione uma ou mais colunas cujo conteúdo a IA deve analisar para determinar a categoria. A IA lê os textos destas colunas e decide com base no conteúdo qual categoria se ajusta melhor.

### 6. Personalizar o prompt

No campo do prompt, pode dar à IA instruções adicionais sobre como deve classificar. Isto é especialmente útil quando os nomes das categorias por si só não são suficientemente claros.

**Exemplos de prompts:**

| Prompt | Efeito |
|---|---|
| *Classifica o pedido com base no tema principal.* | Atribuição simples por tema |
| *Escolhe "Technical" se se tratar de mensagens de erro ou falhas de funcionamento. Escolhe "Billing" se se tratar de pagamentos ou faturas. Tudo o resto é "General".* | Regras claras para cada categoria |
| *Avalia o sentimento do texto: positivo, neutro ou negativo.* | Análise de sentimento |

{{< warning headline="Dica" text="Quanto mais precisamente descrever no prompt o que cada categoria significa, mais confiavelmente a IA classifica. Especialmente com categorias semelhantes, uma delimitação clara compensa." />}}

### 7. Definir a coluna de resultado

Selecione a [coluna de seleção simples]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) ou a [coluna de seleção múltipla]({{< relref "help/base-editor/spaltentypen/die-mehrfachauswahl-spalte" >}}) na qual o resultado deve ser escrito.

- **Seleção simples**: A IA seleciona exatamente uma categoria.
- **Seleção múltipla**: A IA pode atribuir várias categorias simultaneamente.

### 8. Guardar e testar

Clique em **Guardar** e teste a automatização com uma entrada cuja categoria seja óbvia. Verifique se a IA atribui a categoria esperada.

## Exemplo de aplicação: Categorizar tickets de suporte

No seu helpdesk, os pedidos de suporte chegam diariamente através de um formulário web. Cada pedido contém uma **descrição** do problema. Deseja que cada ticket seja automaticamente atribuído a uma categoria para que os seus colaboradores possam trabalhar com os tickets de forma filtrada.

**Configuração:**

- **Gatilho**: Quando uma linha é adicionada
- **Função**: Classify
- **Coluna de entrada**: Descrição
- **Prompt**: *Classifica o pedido de suporte. Escolhe "Technical" para erros, bloqueios e falhas de funcionamento. Escolhe "Billing" para questões sobre pagamentos, faturas ou subscrições. Escolhe "Feature Request" para sugestões de melhoria. Tudo o resto é "General".*
- **Coluna de resultado**: Categoria (seleção simples com as opções "Technical", "Billing", "Feature Request", "General")

Assim que um novo ticket chega, a IA atribui-o automaticamente à categoria correspondente. Os seus colaboradores podem então filtrar por categoria e priorizar os seus tickets.

## Dicas para bons resultados

- **Mantenha o número de categorias controlável.** Cinco a dez categorias costumam funcionar bem. Com demasiadas categorias semelhantes, a precisão diminui.
- **Descreva cada categoria no prompt.** Especialmente com nomes de categorias ambíguos, uma breve explicação ajuda a IA na atribuição.
- **Use uma seleção simples** quando cada entrada deve ser atribuída a exatamente uma categoria. Use uma seleção múltipla apenas quando uma entrada pode realmente pertencer a várias categorias.
- **Reveja os primeiros resultados.** Ajuste o prompt se a IA classificar incorretamente de forma repetida.

## Próximos passos

- [Resumir textos (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Extrair informações (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Ação IA personalizada (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
