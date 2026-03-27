---
title: 'Exemplo Python: Criar algumas entradas aleatórias'
date: 2023-03-02
lastmod: '2023-03-22'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-registros-aleatorios-seatable'
aliases:
  - '/pt/ajuda/python-beispiel-ein-paar-zufaellige-eintraege-erstellen'
seo:
    title: 'Python: crie registros aleatórios no SeaTable'
    description: 'Automate a criação de exemplos no SeaTable com um único script Python. Adicione linhas de teste e preencha rapidamente seus bancos de dados e protótipos.'
weight: 5
---


Por vezes pretende-se gerar algumas entradas de amostra numa base. Com este guião Python pode gerar de poucos a muitos milhares de entradas em pouco tempo.

Este artigo irá guiá-lo através das diferentes secções do guião, para que compreenda como funciona e possa adaptá-lo às suas necessidades, se necessário. O guião completo pode ser encontrado no final deste artigo.

## 1) Carregamento dos módulos

Cada script Python começa com o carregamento dos módulos Python utilizados, onde utilizaremos _base_ e _contexto_ da classe _seatable_api_. Só é necessário o módulo _aleatório_ na segunda linha se se quiser gerar números aleatórios.

```python
from seatable_api import Base, context
import random
```

## 2) Autenticação

As duas linhas seguintes são necessárias para estabelecer a ligação com a base actual. Após esta autenticação, podemos ler, apagar ou manipular a informação através do _objecto base_.

```python
base = Base(context.api_token, context.server_url)
base.auth()
```

## 3) Definir novo conteúdo das linhas

Agora que temos acesso à tabela actual, podemos definir os registos a criar. O código seguinte assume que tem colunas com os nomes _Nome_, _único_, _aleatório_, _classificação_. Se as suas colunas tiverem nomes diferentes, terá de ajustar os nomes de acordo.

```python
# define the data for two new rows
rows_data = [
  {
    'Name': "I am new Row",
    'single': "new",
    'random': random.randint(0,100000000),
    'rating': random.randint(0,5)
  },
  {
    'Name': "I am second new row",
    'single': "other value",
    'random': random.randint(0,100000000),
    'rating': random.randint(0,5)
  },
]
```

## 4) Escrever novas linhas

Com o último bloco de código, o conteúdo das novas _linhas_ foi definido e armazenado nas variáveis _linhas_dados_, mas ainda não foi escrito na base. Fazemo-lo agora com a seguinte chamada.

```python
# append the two rows
  base.batch_append_rows(context.current_table, rows_data)
```

## 5) Se quiser mais linhas

Naturalmente, também pode escrever mais de duas linhas. Pode fazê-lo simplesmente definindo conteúdos de linhas adicionais ou fazendo com que o processo de escrita seja executado várias vezes com a ajuda de um laço.

```python
# execute batch append 10 times
for i in range(10):

  # define the data for two new rows
  ...

  # append the two rows
  ...
```

{{< warning  headline="Indentações de notas em Python"  text="Em Python, a indentação da linha é utilizada para estruturar o código. Isto mantém o código curto e claro, mas ao mesmo tempo tem de se prestar muita atenção ao recuo, porque determina onde termina o _para loop_." />}}

## O guião completo

O guião completo deve estar pronto a funcionar imediatamente sem grandes ajustes. Alterar os nomes das quatro colunas e o guião deve ser capaz de criar novas linhas na sua tabela.

```python
from seatable_api import Base, context
import random

base = Base(context.api_token, context.server_url)
base.auth()

# execute batch append multiple times
for i in range(10):

  # define the data for two new rows
  rows_data = [
    {
      'Name': "I am new Row",
      'single': "new",
      'random': random.randint(0,100000000),
      'rating': random.randint(0,5)
    },
    {
      'Name': "I am second new row",
      'single': "more than new",
      'random': random.randint(0,100000000),
      'rating': random.randint(0,5)
    },
  ]

  # append the two rows
  base.batch_append_rows(context.current_table, rows_data)
```

O guião pode ser iniciado manualmente ou através de um botão ou automatização. Pode saber mais sobre isto [aqui]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).
