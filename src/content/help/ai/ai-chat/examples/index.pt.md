---
title: 'Exemplos e dicas'
description: 'Exemplos práticos e dicas para uma utilização eficaz do plugin de chat IA no SeaTable.'
weight: 4
url: '/pt/ajuda/plugin-chat-ia-exemplos-e-dicas'
seo:
    title: 'Plugin de chat IA: exemplos e dicas para boas perguntas'
    description: 'Aprenda a tirar o máximo partido do plugin de chat IA no SeaTable com exemplos concretos: consultar, analisar e editar dados.'
---

O plugin de chat IA compreende linguagem natural e trabalha diretamente com os dados da sua base. Neste artigo, encontrará exemplos concretos para casos de utilização típicos, bem como dicas para obter melhores resultados. Conselhos gerais sobre como formular boas perguntas também podem ser encontrados no artigo [Como fazer boas perguntas]({{< relref "help/ai/ai-agents/good-questions" >}}).

## Consultar dados

O caso de utilização mais comum: faz uma pergunta e o chat devolve os registos correspondentes da sua base.

> *"Mostra-me todas as tarefas em aberto com prazo para esta semana."*

> *"Quantos clientes temos da Alemanha?"*

> *"Quais faturas ainda estão por pagar?"*

> *"Existem projetos sem um responsável atribuído?"*

Quanto mais precisamente mencionar os nomes das tabelas e colunas, mais exata será a resposta. Se não tem a certeza de quais colunas existem, basta perguntar:

> *"Descreve a estrutura da minha base."*

## Analisar dados

O chat não apenas apresenta os seus dados, mas também os avalia, agrupa e resume.

> *"Qual foi a receita total do último trimestre, discriminada por representante de vendas?"*

> *"Resume os pedidos de suporte da última semana."*

> *"Quais produtos foram encomendados com mais frequência?"*

> *"Como estão distribuídos os tickets em aberto por prioridade?"*

Estas análises funcionam especialmente bem quando a sua base contém dados bem mantidos. Se faltarem valores ou existirem inconsistências, o chat geralmente assinala esta situação.

## Criar e editar dados

O plugin de chat IA também pode criar, modificar, vincular e eliminar registos. Seja o mais específico possível sobre qual tabela, quais colunas e quais valores são afetados.

### Criar novos registos

> *"Cria um novo contacto: Nome 'Müller GmbH', Cidade 'Hamburgo', Estado 'Prospect'."*

> *"Cria uma entrada de acompanhamento na tabela Atividades para cada negócio em aberto."*

### Modificar registos existentes

> *"Define o estado de todas as tarefas em atraso como 'Escalado'."*

> *"Altera a prioridade do ticket #412 para 'Alta'."*

### Vincular e eliminar registos

> *"Vincula todas as faturas ao cliente correspondente na tabela Contactos."*

> *"Elimina todas as entradas de teste da tabela Rascunhos."*

Ao eliminar, o chat solicita confirmação antes de executar a ação. Ainda assim, verifique previamente com uma consulta de leitura se os registos corretos são afetados.

## Dicas para melhores resultados

**Comece com consultas de leitura.** Antes de a IA modificar dados, verifique primeiro se o chat encontra os registos corretos. Pergunte *"Quais tarefas estão em atraso?"* antes de dizer *"Define o estado como Escalado."*

**Divida tarefas complexas em passos mais pequenos.** Para pedidos com várias etapas, obterá melhores resultados procedendo passo a passo. O chat recorda o contexto da conversa e pode basear-se nas respostas anteriores.

**Utilize os nomes das tabelas e colunas.** A ortografia exata não é obrigatória, mas utilizar os termos corretos ajuda o chat a interpretar a sua pergunta com precisão.

**Aproveite o contexto.** Após uma consulta, pode referir-se a resultados anteriores com "estes", "desses" ou "os mesmos" sem repetir tudo.

## O que não funciona

O plugin de chat IA trabalha exclusivamente com os dados da sua base SeaTable. As seguintes ações não são possíveis:

- **Consultar dados inexistentes.** Se uma coluna ou tabela não existir, o chat não pode fornecer uma resposta. Não inventa dados.
- **Ações fora do SeaTable.** O chat não pode enviar e-mails, aceder a sistemas externos ou abrir ficheiros.
- **Operações em massa muito grandes.** Pedidos individuais que tentem criar ou modificar centenas de registos de uma só vez podem atingir os seus limites. Divida estas tarefas em passos mais pequenos.
