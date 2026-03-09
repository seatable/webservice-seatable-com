---
title: 'Ação de IA personalizada (Custom)'
description: 'Com a função de IA Custom, você define seu próprio prompt e deixa a IA executar qualquer tarefa nos seus dados.'
weight: 7
url: '/pt/ajuda/automatizacao-ia-acao-personalizada'
seo:
    title: 'Automatização IA: Ação de IA personalizada no SeaTable'
    description: 'Como criar automatizações de IA personalizadas no SeaTable: escreva seu próprio prompt e tenha textos traduzidos, reformulados ou avaliados.'
---

A função de IA **Custom** é a mais flexível das cinco ações de IA. Você escreve seu próprio prompt e determina livremente o que a IA faz com seus dados. Tudo o que não se encaixa nas quatro funções padrão (Summarize, Classify, OCR, Extract) pode ser implementado com Custom.

## Casos de uso típicos

- **Traduzir**: Traduzir textos automaticamente para outro idioma.
- **Reformular**: Reescrever textos em outro tom ou estilo (p. ex., formal, orientado ao cliente, simplificado).
- **Sugestões de resposta**: Gerar um rascunho de resposta com base em uma consulta de cliente.
- **Avaliar**: Avaliar textos segundo seus próprios critérios em uma escala (p. ex., relevância, qualidade, urgência).
- **Gerar**: Criar descrições de produtos, publicações em redes sociais ou metatextos a partir de tópicos.
- **Corrigir**: Corrigir automaticamente erros de ortografia e gramática em textos.

## Pré-requisitos

- Uma tabela com pelo menos uma coluna cujo conteúdo a IA deve processar.
- Uma **coluna de Texto** ou **coluna de Texto formatado** para o resultado.

## Guia passo a passo

### 1. Criar uma automatização e escolher um gatilho

Crie uma nova regra de automatização conforme descrito no artigo [Configurar a automatização de IA]({{< relref "help/ai/ai-automations/setup-ai-automation" >}}). Escolha o gatilho adequado para o seu caso de uso.

### 2. Adicionar a ação "Chamar IA"

Clique em **Adicionar ação** e selecione **Chamar IA**.

### 3. Selecionar a função "Custom"

Nas configurações da ação, escolha:

- **Tabela**: A tabela na qual a IA deve trabalhar.
- **Função**: **Custom**

![Definições da ação com a função Custom selecionada](images/ai-automation-custom.png)

### 4. Escrever o prompt

O prompt é o núcleo da função Custom. Aqui você formula a instrução para a IA. Use **{Nome da coluna}** entre chaves para inserir o valor de uma coluna da linha atual no prompt.

**Estrutura de um bom prompt:**

```
Traduza o seguinte texto para o inglês.
Mantenha o tom e a formatação.

Texto: {Descrição}
```

Neste exemplo, `{Descrição}` é substituído a cada execução pelo conteúdo real da coluna "Descrição".

![Campo de entrada do prompt com referência de coluna](images/ai-automation-custom-reference-column-by-name.png)

### 5. Definir a coluna de resultado

Selecione a coluna na qual o resultado da IA deve ser escrito. Esta deve ser do tipo **Texto** ou **Texto formatado**.


### 6. Salvar e testar

Clique em **Salvar** e teste a automatização com uma entrada. Verifique se o resultado na coluna de resultado atende às suas expectativas e ajuste o prompt se necessário.

## Exemplos de prompts para tarefas comuns

### Traduzir textos

```
Traduza o seguinte texto para o inglês.
Mantenha os termos técnicos e não os traduza.

Texto: {Descrição do produto}
```

### Gerar uma sugestão de resposta

```
Escreva uma resposta amigável e profissional
para a seguinte consulta de cliente. A resposta
não deve ultrapassar cinco frases.

Consulta: {Consulta do cliente}
```

### Reformular um texto

```
Reformule o seguinte texto para que seja adequado
para um comunicado de imprensa. Use um tom objetivo
e profissional.

Texto original: {Notas}
```

### Avaliar conteúdo

```
Avalie o seguinte texto em uma escala de 1 a 5
quanto à sua urgência. Responda apenas com o
número e uma breve justificativa em uma frase.

Texto: {Solicitação de suporte}
```

### Gerar uma descrição de produto

```
Crie uma descrição de produto atraente para uma
loja online com base nos seguintes tópicos.
A descrição deve ter entre 50 e 80 palavras.

Nome do produto: {Nome}
Características: {Características}
Público-alvo: {Público-alvo}
```

### Corrigir ortografia e gramática

```
Corrija erros de ortografia e gramática no seguinte
texto. Não altere o conteúdo nem as formulações.
Retorne apenas o texto corrigido.

Texto: {Texto livre}
```

## Exemplo de aplicação: Traduzir descrições de produtos

Sua tabela de produtos contém descrições de produtos em alemão. Para a loja online internacional, você precisa de traduções para o inglês. Em vez de traduzir cada descrição manualmente, a IA deve fazer isso automaticamente.

**Configuração:**

- **Gatilho**: Quando uma linha é adicionada
- **Função**: Custom
- **Prompt**: *Traduza o seguinte texto em alemão para o inglês. Use um tom atraente adequado para uma loja online. Mantenha os nomes de produtos e marcas como estão. Texto: {Descrição DE}*
- **Coluna de resultado**: Descrição EN (coluna de Texto)

Assim que um novo produto com descrição em alemão é inserido, a tradução para o inglês aparece automaticamente na coluna de resultado.


## Dicas para bons prompts

- **Seja específico.** "Escreva um bom texto" produz resultados imprevisíveis. "Escreva uma descrição de produto de 50 a 80 palavras em um tom amigável" é muito melhor.
- **Use referências de colunas.** Com `{Nome da coluna}` você pode combinar valores de várias colunas em um prompt para fornecer contexto.
- **Defina o formato de saída.** O resultado deve ser uma única frase? Uma lista? Um número com justificativa? Especifique no prompt.
- **Teste e itere.** Experimente o prompt com diferentes entradas. Se os resultados não forem adequados, ajuste a formulação.
- **Escreva o prompt no idioma de destino.** Se o resultado deve estar em inglês, escreva o prompt em inglês. Isso melhora a qualidade dos resultados.

## Próximos passos

- [Resumir textos (Summarize)]({{< relref "help/ai/ai-automations/summarize" >}})
- [Classificar entradas (Classify)]({{< relref "help/ai/ai-automations/classify" >}})
- [Extrair informações (Extract)]({{< relref "help/ai/ai-automations/extract" >}})
- [Reconhecimento de texto em imagens (OCR)]({{< relref "help/ai/ai-automations/ocr" >}})
