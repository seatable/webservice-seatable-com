---
title: 'Scripts Python: Perguntas frequentes'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-perguntas-frequentes'
seo:
    title: 'Scripts Python no SeaTable: Perguntas frequentes'
    description: 'Respostas a perguntas frequentes sobre scripts Python no SeaTable: bibliotecas suportadas, operações em lote, execução local e dicas de depuração.'
weight: 2
star: true
---

## Como posso executar um script tanto localmente como no SeaTable?

Pode escrever o seu script de forma a funcionar em ambos os ambientes sem alterações. O truque é verificar se o objeto `context` está disponível:

```python
from seatable_api import Base

try:
    from seatable_api import context
    base = Base(context.api_token, context.server_url)
except:
    base = Base('your-api-token', 'https://cloud.seatable.io')

base.auth()
```

## Que bibliotecas estão disponíveis?

Uma lista completa de todas as bibliotecas pré-instaladas encontra-se no artigo [Bibliotecas Python suportadas]({{< relref "help/skripte/python/unterstuetzte-python-bibliotheken" >}}). Aí também aprenderá como adicionar bibliotecas personalizadas num servidor auto-hospedado.

## Como processo mais de 1.000 linhas?

O método `base.list_rows()` devolve por defeito um máximo de 1.000 linhas. Para processar mais linhas, utilize uma destas abordagens:

**Opção 1: Ciclo com offset**
```python
all_rows = []
offset = 0
while True:
    rows = base.list_rows(TABLE_NAME, start=offset, limit=1000)
    if not rows:
        break
    all_rows.extend(rows)
    offset += 1000
```

**Opção 2: Consulta SQL**
```python
rows = base.query("SELECT * FROM `Table1` LIMIT 10000")
```

As consultas SQL suportam até 10.000 linhas por pedido.

## Como depuro estruturas de dados complexas?

Utilize `json.dumps()` com indentação para mostrar dicionários e listas de forma formatada:

```python
import json
metadata = base.get_metadata()
print(json.dumps(metadata, indent=2))
```

Para a referência completa das funções, visite o [SeaTable Developer Manual](https://developer.seatable.com/python/).
