---
title: 'Exemplo Python: Adicionar linhas automaticamente'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/python-adicionar-linhas'
seo:
    title: 'Python: Adicionar linhas automaticamente no SeaTable'
    description: 'Use este script Python para adicionar automaticamente entradas recorrentes na sua base SeaTable com verificação de duplicados.'
---


Este script cria automaticamente entradas mensais recorrentes numa tabela. Verifica através de uma consulta SQL se já existem entradas para o mês atual e só cria as que faltam. Desta forma pode configurá-lo como automação agendada (por ex. no 1.º de cada mês) sem criar duplicados.

![Monthly Expenses in SeaTable](monthly-expenses.png)

{{< dtable-download name="Monthly Expenses" file="/downloads/python-examples/monthly-expenses.dtable" text="Base com dados de exemplo e script pronto para experimentar diretamente." />}}

## Pré-requisitos

A tabela necessita de pelo menos as seguintes colunas:

- **Category** (Seleção simples) — tipo de entrada
- **Description** (Texto) — descrição
- **Amount** (Número) — montante
- **Month** (Data) — mês de faturação
- **Type** (Seleção simples) — por ex. Expense ou Income

## O script

Adapte `TABLE_NAME` e as entradas em `ENTRIES` à estrutura da sua tabela. Os valores das colunas de seleção simples são automaticamente criados como novas opções se ainda não existirem.

```python
from seatable_api import Base, context, dateutils
from datetime import datetime

base = Base(context.api_token, context.server_url)
base.auth()

TABLE_NAME = "Ledger"

today = datetime.today()
this_month = today.month
this_year = today.year
first_of_this_month = dateutils.date(this_year, this_month, 1)

# Define recurring monthly entries
ENTRIES = [
    {"Category": "Office supplies", "Description": "Monthly office supplies", "Amount": 150.00, "Type": "Expense"},
    {"Category": "Software licenses", "Description": "Monthly software licenses", "Amount": 500.00, "Type": "Expense"},
]

for entry in ENTRIES:
    rows = base.query(f"SELECT _id FROM `{TABLE_NAME}` WHERE `Month` = '{first_of_this_month}' AND `Category` = '{entry['Category']}'")
    if len(rows) == 0:
        entry['Month'] = first_of_this_month
        base.append_row(TABLE_NAME, entry)
        print(f"Added: {entry['Category']}")
    else:
        print(f"Skipped (already exists): {entry['Category']}")
```

Para a referência completa das funções, visite o [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
