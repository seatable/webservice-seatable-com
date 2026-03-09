---
title: 'Extrair informações (Extract)'
description: 'Com a função de IA Extract, pode ler informações específicas de textos e escrevê-las em colunas separadas.'
weight: 6
url: '/pt/ajuda/automatizacao-ia-extrair-informacoes'
seo:
    title: 'Automatização IA: Extrair informações automaticamente no SeaTable'
    description: 'Saiba como extrair dados de textos no SeaTable: Configure uma automatização IA com a função Extract — leia automaticamente números de fatura, datas e montantes.'
---

A função de IA **Extract** lê de forma específica determinadas informações de texto não estruturado e escreve-as em colunas individuais. Desta forma, transforma texto corrido em dados estruturados — por exemplo, número de fatura, data e montante de um texto de fatura.

## Casos de uso típicos

- **Faturas**: Ler número de fatura, data, montante e destinatário de textos de faturas.
- **E-mails**: Extrair nome do remetente, assunto e pedido principal de mensagens recebidas.
- **Contratos**: Registar duração do contrato, prazo de rescisão e partes contratantes de textos de contratos.
- **Encomendas**: Ler número de artigo, quantidade e endereço de entrega de textos de encomendas.
- **Cartões de visita** (após OCR): Ler nome, empresa, número de telefone e e-mail do texto reconhecido.

## Pré-requisitos

- Uma tabela com pelo menos uma **coluna de texto** que contenha o texto a analisar.
- Uma ou mais **colunas de resultados** nas quais as informações extraídas serão escritas.

## Guia passo a passo

### 1. Criar uma automatização e escolher um gatilho

Crie uma nova regra de automatização conforme descrito no artigo [Configurar uma automatização IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Escolha um gatilho adequado — por exemplo **Quando uma linha é adicionada**, para que as novas entradas sejam processadas imediatamente.

### 2. Adicionar a ação "Chamar IA"

Clique em **Adicionar ação** e selecione **Chamar IA**.

### 3. Selecionar a função "Extract"

Nas definições da ação, escolha:

- **Tabela**: A tabela na qual a IA deve trabalhar.
- **Função**: **Extract**

![Definições da ação para a função Extract selecionada](images/ai-automations-extract.png)

### 4. Definir a coluna de entrada

Selecione a coluna cujo conteúdo a IA deve analisar. Normalmente trata-se de uma **coluna de texto** com texto não estruturado — por exemplo, o texto completo de uma fatura ou de um e-mail.

### 5. Definir o prompt

O prompt é particularmente importante para a função Extract. Descreva exatamente **que informações** a IA deve extrair. Seja o mais preciso possível.

**Exemplos de prompts:**

| Prompt | Informações extraídas |
|---|---|
| *Extrai o número da fatura, a data da fatura e o montante total.* | Três valores individuais |
| *Lê o nome, a empresa e o endereço de e-mail do texto.* | Dados de contacto |
| *Encontra a data de início, a data de fim e o prazo de rescisão.* | Informações contratuais |
| *Extrai a descrição do artigo e a quantidade da encomenda.* | Detalhes da encomenda |

### 6. Definir as colunas de resultados

Atribua cada informação a extrair à sua própria **coluna de resultados**. Escolha o tipo de coluna adequado ao conteúdo esperado — a IA reconhece o formato e escreve os valores diretamente no tipo de coluna correto. Assim, as datas ficam de forma fiável numa coluna de data e os textos numa coluna de texto.

![Configurar várias colunas de resultado](images/ai-automation-extract-output-mapping.png)

### 7. Guardar e testar

Clique em **Guardar** e teste a automatização com uma entrada que contenha as informações a extrair. Verifique se os valores são registados corretamente nas colunas de resultados.

## Exemplo de aplicação: Leitura de dados de faturas

Na sua tabela, armazena faturas recebidas como texto corrido (ou após reconhecimento OCR). Pretende extrair automaticamente os dados de faturação mais importantes para colunas individuais.

**Configuração:**

- **Gatilho**: Quando uma linha é adicionada
- **Função**: Extract
- **Coluna de entrada**: Texto da fatura
- **Prompt**: *Extrai as seguintes informações do texto da fatura: número da fatura, data da fatura (no formato DD/MM/AAAA), montante líquido, montante de IVA e montante bruto.*
- **Colunas de resultados**: Número da fatura, Data da fatura, Montante líquido, IVA, Montante bruto

Assim que uma nova entrada com um texto de fatura é criada, a IA extrai os dados relevantes e escreve-os nas respetivas colunas.

## Dicas para bons resultados

- **Seja específico no prompt.** Em vez de "Extrai as informações importantes", escreva exatamente quais campos precisa. Quanto mais preciso for o prompt, mais fiável será o resultado.
- **Indique o formato desejado.** Se precisa de uma data no formato DD/MM/AAAA, escreva isso no prompt. O mesmo se aplica a montantes com ou sem símbolo de moeda.
- **Teste com diferentes textos.** Faturas de diferentes remetentes têm formatos diferentes. Verifique se a IA também encontra as informações corretas com layouts diferentes.
- **Combine Extract com OCR.** Se os seus dados de origem estão em forma de imagens (por ex. faturas digitalizadas), utilize primeiro a [função OCR]({{< relref "help/ai/ai-automations/ocr" >}}) e depois Extract numa segunda ação.

## Próximos passos

- [Reconhecimento de texto a partir de imagens (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
- [Resumir textos (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Ação de IA personalizada (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
