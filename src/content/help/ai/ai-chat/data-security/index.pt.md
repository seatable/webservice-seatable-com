---
title: 'Permissões e privacidade de dados'
description: 'Saiba como o plugin de chat IA gere os seus dados e que mecanismos de segurança protegem as suas informações.'
weight: 5
url: '/pt/ajuda/plugin-chat-ia-permissoes-privacidade'
seo:
    title: 'Plugin de chat IA: permissões e privacidade de dados'
    description: 'Como o plugin de chat IA protege os seus dados: diálogos de confirmação, transparência do fluxo de dados e controlo do fornecedor de IA.'
---

O plugin de chat IA conecta os seus dados do SeaTable a um modelo de linguagem externo. Este artigo explica como funciona o fluxo de dados, que mecanismos de proteção existem e como mantém o controlo sobre os seus dados.

## Como fluem os seus dados?

Quando faz uma pergunta no chat IA, o fluxo de dados processa-se em quatro etapas:

1. **A sua pergunta** é enviada ao fornecedor de IA selecionado.
2. O plugin consulta os dados relevantes da sua base.
3. **Os resultados da consulta** são transmitidos ao fornecedor de IA para que o modelo de linguagem os possa avaliar.
4. O modelo formula uma resposta e envia-a de volta ao plugin.

Isto significa que os dados que o plugin consulta para a sua pergunta são transmitidos ao fornecedor de IA externo. Tal é tecnicamente necessário porque um modelo de linguagem só pode processar dados que recebe.

## Escolha do fornecedor de IA

É o utilizador que decide qual fornecedor e qual modelo utiliza. As opções disponíveis são Anthropic (Claude), OpenAI e Mistral. Cada fornecedor tem as suas próprias políticas de privacidade de dados. Os principais fornecedores comprometem-se contratualmente a que os dados processados através da sua API **não sejam utilizados para treinar modelos**. Ainda assim, consulte os termos de utilização atuais do fornecedor escolhido.

## Confirmação antes de alterações

O plugin distingue claramente entre operações de leitura e de escrita. Antes de uma ação destrutiva ser executada (p. ex., modificar ou eliminar linhas), o plugin apresenta um **diálogo de confirmação**. Este informa-o sobre as alterações que serão efetuadas e quantas linhas são afetadas.

Tem três opções:

- **Aprovar uma vez**: Apenas esta ação individual é executada.
- **Aprovar para toda a sessão**: Outras ações deste tipo são executadas sem confirmação adicional.
- **Recusar**: A ação não é executada.

O plugin também solicita confirmação antes de processar grandes conjuntos de resultados com milhares de linhas. Desta forma, mantém o controlo em todos os momentos.

## Máximo controlo através do auto-alojamento

Se pretende impedir que os dados sejam transmitidos a fornecedores externos, pode auto-alojar o SeaTable e combiná-lo com um modelo de linguagem local. Nesta configuração, os seus dados nunca saem da sua própria rede.

## Informações adicionais

Uma discussão detalhada sobre a segurança de dados ao utilizar IA com o SeaTable pode ser encontrada no artigo [Permissões e privacidade de dados para agentes de IA]({{< relref "help/ai/ai-agents/data-security" >}}). Entre outros temas, aborda permissões de tokens API, estratégias para minimizar a exposição de dados e o auto-alojamento em detalhe.
