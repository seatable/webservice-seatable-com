---
title: 'Resolução de problemas'
description: 'Soluções para problemas comuns com o plugin de chat IA no SeaTable.'
weight: 6
url: '/pt/ajuda/plugin-chat-ia-resolucao-de-problemas'
seo:
    title: 'Plugin de chat IA: resolução de problemas e questões comuns'
    description: 'Soluções para problemas comuns do plugin de chat IA: erros de chave API, respostas em falta e problemas do plugin.'
---

Se o plugin de chat IA não estiver a funcionar como esperado, encontrará aqui soluções para os problemas mais comuns. Para informações gerais sobre a configuração, consulte o artigo [Configurar o plugin de chat IA]({{< relref "help/ai/ai-chat/setup" >}}).

## Problemas com a chave API

### Chave API inválida

Se a mensagem de erro indicar uma chave API inválida, verifique o seguinte:

- Certifique-se de que a chave foi introduzida corretamente e não contém espaços acidentais.
- Verifique se a chave API ainda está ativa. Alguns fornecedores desativam chaves após um determinado período de inatividade.
- Assegure-se de que o **fornecedor** selecionado nas definições do plugin corresponde à chave API. Por exemplo, uma chave OpenAI não funciona com o fornecedor Anthropic.

### Crédito ou quota esgotados

A maioria dos fornecedores de IA trabalha com crédito pré-pago. Se as respostas deixarem de ser geradas, verifique o seu saldo no painel do respetivo fornecedor:

- [Anthropic Console](https://console.anthropic.com/)
- [OpenAI Platform](https://platform.openai.com/)
- [Mistral Console](https://console.mistral.ai/)

## Respostas ausentes ou incorretas

### A IA não encontra os dados

Certifique-se de que os dados solicitados existem efetivamente na base. Mencione o nome exato da tabela e da coluna na sua pergunta para que a IA possa identificar os dados corretos.

### Resultados imprecisos ou incorretos

Formule a sua pergunta da forma mais precisa possível. Evite formulações vagas e especifique exatamente qual tabela e quais colunas são relevantes. Para tarefas complexas, pode ajudar dividir o pedido em vários passos simples.

### Timeout ou sem resposta

Consultas muito grandes podem originar um timeout. Simplifique o pedido ou limite-se a uma única tabela. Note também que modelos mais pequenos como Haiku, GPT-4o mini ou Mistral Small podem atingir os seus limites com tarefas complexas e de várias etapas.

## Problemas com o plugin

### O plugin não é apresentado

Verifique se o plugin está instalado e ativado no Gestor de Plugins. Para tal, abra a secção **Plugins** no cabeçalho da base e procure por **AI Chat**.

### O plugin não carrega

Recarregue a página no seu navegador. Se o problema persistir, experimente um navegador diferente ou limpe a cache do navegador.

### As definições não são guardadas

Certifique-se de que, após introduzir a chave API, confirmou as definições com **Guardar**. Sem guardar, as entradas perdem-se ao fechar o diálogo de definições.

## Dicas gerais

- Comece com uma pergunta simples como "Que tabelas existem?" para verificar a ligação ao fornecedor de IA.
- Se a IA apresentar resultados inesperados, peça-lhe que explique a sua abordagem.
- Divida tarefas complexas em vários passos pequenos para obter melhores resultados.
