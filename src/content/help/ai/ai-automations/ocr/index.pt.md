---
title: 'Reconhecimento de texto em imagens (OCR)'
description: 'Com a função de IA OCR, reconheça automaticamente texto em imagens e documentos digitalizados na sua base SeaTable.'
weight: 5
url: '/pt/ajuda/automatizacao-ia-reconhecimento-texto-ocr'
seo:
    title: 'Automatização IA: Reconhecimento de texto (OCR) no SeaTable'
    description: 'Como reconhecer texto em imagens automaticamente no SeaTable: configurar uma automatização IA com a função OCR — ler cartões de visita, faturas e documentos.'
---

A função de IA **OCR** (Optical Character Recognition) reconhece texto em imagens e escreve o conteúdo reconhecido numa coluna de texto. Isto permite converter automaticamente documentos digitalizados, fotos de cartões de visita ou imagens de faturas em texto pesquisável.

## Casos de uso típicos

- **Cartões de visita**: capturar automaticamente fotos de cartões de visita como texto.
- **Faturas e recibos**: converter faturas digitalizadas em texto legível.
- **Guias de remessa**: extrair texto de guias de remessa fotografadas.
- **Notas manuscritas**: digitalizar fotos de notas manuscritas.
- **Documentos**: tornar contratos ou formulários digitalizados disponíveis como texto.

## Pré-requisitos

- Uma tabela com uma [coluna de imagem]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) ou uma [coluna de ficheiro]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) que contenha as imagens ou documentos a serem reconhecidos.
- Uma [coluna de texto ou coluna de texto formatado]({{< relref "help/base-editor/spaltentypen/die-spalten-text-und-formatierter-text" >}}) para o texto reconhecido.

## Guia passo a passo

### 1. Criar uma automatização e escolher um acionador

Crie uma nova regra de automatização conforme descrito no artigo [Configurar automatização IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Um acionador típico é **Quando uma linha é adicionada** — desta forma, cada imagem recém-carregada é processada automaticamente.

Alternativamente, pode usar **Quando uma linha é modificada** e definir a coluna de imagem como coluna monitorizada. Neste caso, o reconhecimento OCR é acionado sempre que uma nova imagem é inserida na coluna.

### 2. Adicionar a ação "Chamar IA"

Clique em **Adicionar ação** e selecione **Chamar IA**.

### 3. Selecionar a função "OCR"

Nas configurações da ação, escolha:

- **Tabela**: a tabela na qual a IA deve trabalhar.
- **Função**: **OCR**

![Definições da ação com a função OCR selecionada](images/ai-automation-ocr.png)

### 4. Definir a coluna de entrada

Selecione a coluna da qual a IA deve reconhecer o texto. Pode usar uma **coluna de imagem** ou uma **coluna de ficheiro** como coluna de entrada. Com uma coluna de ficheiro, pode processar por exemplo PDFs ou documentos digitalizados.

{{< warning headline="Nota" text="Se uma coluna de imagem ou ficheiro contiver vários ficheiros, apenas o **primeiro ficheiro** é processado. Idealmente, carregue apenas uma imagem ou documento por linha na coluna de entrada." />}}

### 5. Definir a coluna de resultado

Selecione a coluna na qual o texto reconhecido deve ser escrito. Esta deve ser do tipo **Texto** ou **Texto formatado**.

### 6. Guardar e testar

Clique em **Guardar** e carregue uma imagem de teste com texto bem legível na coluna de imagem. Após alguns segundos, o texto reconhecido deverá aparecer na coluna de resultado.

## Exemplo de aplicação: digitalizar cartões de visita

A sua equipa de vendas fotografa cartões de visita em feiras e carrega as fotos numa tabela do SeaTable. A IA deve reconhecer automaticamente o texto no cartão de visita para que possa pesquisar os dados de contacto.

**Configuração:**

- **Acionador**: Quando uma linha é adicionada
- **Função**: OCR
- **Coluna de entrada**: Imagem do cartão de visita (coluna de imagem)
- **Coluna de resultado**: Texto reconhecido (coluna de texto)

Assim que uma nova entrada com uma imagem de cartão de visita é criada, a IA lê o texto da imagem e escreve-o na coluna de resultado. A partir daí, pode continuar a processar os dados — por exemplo, com uma ação **Extract** subsequente para extrair especificamente o nome, a empresa e o número de telefone.

{{< warning headline="Dica" text="Combine OCR com a função **Extract** numa segunda ação dentro da mesma automatização. Desta forma, primeiro reconhece o texto e depois extrai as informações relevantes em colunas separadas num segundo passo." />}}

## Dicas para bons resultados

- **A qualidade da imagem conta.** Quanto mais nítida e com maior contraste for a imagem, melhor será o reconhecimento de texto. Fotos desfocadas ou má iluminação podem levar a erros.
- **Texto impresso funciona de forma mais fiável do que escrita à mão.** Texto datilografado é reconhecido quase sem erros. Para escrita à mão, a qualidade depende da legibilidade.
- **Mantenha a imagem direita.** Imagens muito distorcidas ou rodadas podem dificultar o reconhecimento.
- **Use formatos de imagem comuns.** JPG e PNG funcionam de forma fiável.

## Combinar OCR com Extract

A função OCR fornece o **texto reconhecido completo** como texto contínuo. Se pretender extrair informações específicas individuais (por exemplo, nome, morada, número de fatura), pode adicionar uma segunda ação com a função [Extract]({{< relref "help/ai/ai-automations/extract" >}}) na mesma automatização. Desta forma, o texto reconhecido é estruturado em colunas individuais num segundo passo.

## Próximos passos

- [Extrair informações (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Resumir textos (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Ação IA personalizada (Custom)]({{< relref "help/ai/ai-automations/custom" >}})
