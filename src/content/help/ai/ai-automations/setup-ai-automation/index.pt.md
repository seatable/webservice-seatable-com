---
title: 'Configurar uma automatização IA'
description: 'Crie uma automatização IA no SeaTable passo a passo — do acionador à ação IA concluída.'
weight: 2
url: '/pt/ajuda/configurar-automatizacao-ia'
seo:
    title: 'Configurar uma automatização IA no SeaTable — Guia passo a passo'
    description: 'Como criar uma automatização IA no SeaTable: escolher um acionador, configurar a função IA, definir colunas de entrada e resultado, e testar a automatização.'
---

Neste guia, irá criar uma automatização com a ação **Executar IA**. Depois de configurada, o SeaTable processará os seus dados automaticamente com um modelo de IA — por exemplo, para resumir textos, categorizar entradas ou extrair informações.

## Pré-requisitos

- SeaTable (Cloud ou Server) **versão 6.0** ou superior
- Uma base com uma tabela que contenha dados de texto

{{< warning headline="Nota para clientes auto-hospedados" >}}

No **SeaTable Cloud**, o servidor de IA já está integrado. O SeaTable opera o seu próprio modelo linguístico (Gemma 3) em infraestrutura GPU na Alemanha — pode utilizar as automatizações IA imediatamente.

Se **auto-hospedar** o SeaTable, precisa de operar o seu próprio servidor de IA ou configurar uma ligação a um fornecedor de IA na nuvem. Para mais informações, consulte o [guia de instalação do SeaTable AI](https://admin.seatable.com/installation/components/seatable-ai/).

{{< /warning >}}

## Passo 1: Criar uma regra de automatização

1. Abra a sua base e clique em {{< seatable-icon icon="dtable-icon-rule" >}} no cabeçalho da base e depois em **Regras de automatização**.
2. Clique em **Adicionar regra ou pasta** e selecione **Adicionar regra**.
3. Dê à automatização um **nome** descritivo, por exemplo «Resumir pedidos de suporte».

![Página de visão geral das regras de automatização](images/ai-automation-overview.png)

## Passo 2: Escolher um acionador

Clique em **Adicionar acionador** e selecione um acionador. Para as automatizações IA, estão disponíveis dois acionadores:

- **Quando uma linha é modificada** — a IA processa a linha alterada imediatamente
- **Quando uma linha é adicionada** — a IA processa cada nova entrada automaticamente

Em seguida, selecione a **tabela** e a **vista** na qual a automatização deve funcionar. Opcionalmente, pode definir **condições** para acionar a automatização apenas para determinadas entradas.

![Seleção do acionador](images/automation-trigger-selection.png)

{{< warning headline="Nota" text="Os acionadores baseados em tempo (**A uma hora agendada** e **A uma hora agendada para registos que correspondem a condições**) não suportam atualmente ações de IA." />}}

## Passo 3: Adicionar a ação IA

1. Clique em **Adicionar ação**.
2. Selecione **Executar IA** na parte inferior da lista de ações disponíveis.

![Lista de ações com a opção Executar IA](images/automation-action-run-ai.png)

## Passo 4: Configurar a função IA

Após selecionar a ação **Executar IA**, as **definições da ação** abrem-se à direita. Configure o seguinte:

### Tabela
Selecione a tabela na qual a IA deve trabalhar. Normalmente, é a mesma tabela do acionador.

### Função
Escolha uma das cinco funções IA disponíveis:

| Função | Descrição | Utilização típica |
|---|---|---|
| **Summarize** | Resume textos | Condensar descrições longas |
| **Classify** | Atribui categorias | Categorizar pedidos de suporte |
| **OCR** | Reconhece texto em imagens | Ler cartões de visita, faturas |
| **Extract** | Extrai informações específicas | Extrair número de fatura, data |
| **Custom** | Prompt personalizado | Traduzir, avaliar, reformular |

![Menu pendente com as cinco funções IA](images/automation-select-ai-function.png)

### Colunas de entrada
Selecione uma ou mais colunas cujo conteúdo a IA deve processar. Trata-se do texto (ou da imagem/ficheiro no caso de OCR) que a IA recebe como entrada.

### Prompt
Para todas as funções exceto OCR, pode introduzir um **prompt** para controlar o resultado. Por exemplo: «O resumo não deve exceder duas frases e deve ser escrito em português.» Para OCR, não é necessário nenhum prompt — a IA reconhece o texto na imagem automaticamente.

### Coluna(s) de resultado
Selecione a coluna na qual o resultado da IA deve ser escrito. O tipo de coluna deve corresponder à função escolhida — por exemplo, uma coluna de texto para resumos ou uma coluna de seleção simples para classificações.

## Passo 5: Guardar e ativar

1. Clique em **Guardar** para guardar as definições da ação.
2. A automatização está agora ativa e será executada automaticamente na próxima vez que o evento acionador ocorrer.

## Testar a automatização

Para testar a automatização imediatamente, acione o evento manualmente:

- Para **Quando uma linha é adicionada**: crie uma nova linha com dados de teste.
- Para **Quando uma linha é modificada**: altere um valor numa coluna monitorizada.

Em seguida, verifique se a IA escreveu o resultado na coluna de resultado. Pode consultar o estado e eventuais erros no [registo de execução]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}}).

![Registo de execução de uma automatização IA](images/automation-open-log.png)

## Problemas frequentes

| Problema | Solução |
|---|---|
| A coluna de resultado permanece vazia | Verifique se a coluna de entrada contém efetivamente um valor. Entradas vazias não produzem resultado. |
| Tipo de coluna incorreto | A coluna de resultado deve corresponder ao resultado. Classificações precisam de uma coluna de seleção simples; resumos de uma coluna de texto. |
| A automatização não é acionada | Verifique se a automatização está ativada e se a alteração ocorre na tabela e vista corretas. |

## Próximos passos

Encontrará guias detalhados para cada função IA nestes artigos:

- [Resumir textos (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Classificar entradas (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Reconhecimento de texto em imagens (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
- [Extrair informações (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Ação IA personalizada (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
