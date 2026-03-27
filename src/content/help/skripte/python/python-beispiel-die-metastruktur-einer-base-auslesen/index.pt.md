---
title: 'Exemplo Python: Leitura da infra-estrutura de uma base'
date: 2023-03-22
lastmod: '2023-07-25'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/pt/ajuda/exemplo-python-ler-metastrutura-base'
aliases:
    - '/pt/ajuda/python-beispiel-die-metastruktur-einer-base-auslesen'
seo:
    title: 'Exemplo Python: ler metastrutura da base SeaTable'
    description: 'Saiba ler e organizar a metastrutura completa de uma base SeaTable com Python—script, saída estruturada e colunas de ligação.'
weight: 4
---

Este artigo apresenta-lhe um script Python que produz a meta-estrutura completa de uma base. Isto é útil, por exemplo, se tiver uma pergunta sobre uma base no [fórum da comunidade](https://forum.seatable.com/) e quiser descrever a estrutura da sua base de forma rápida e fácil sem capturas de ecrã.

## A infra-estrutura de uma base

A meta-estrutura de uma base descreve as tabelas, colunas e vistas de uma base. As entradas e os registos nas linhas não estão incluídos na meta-estrutura. A seguinte estrutura JSON descreve uma base comparativamente simples com apenas uma tabela, duas colunas e uma vista.

```json
{
    "metadata": {
        "tables": [
            {
                "_id": "0000",
                "name": "Table1",
                "columns": [
                    {
                        "key": "0000",
                        "name": "Name",
                        "type": "text",
                        "width": 200,
                        "editable": true,
                        "resizable": true
                    },
                    {
                        "key": "BydO",
                        "type": "date",
                        "name": "Date",
                        "editable": true,
                        "width": 200,
                        "resizable": true,
                        "draggable": true,
                        "data": {
                            "format": "YYYY-MM-DD"
                        },
                        "permission_type": "",
                        "permitted_users": []
                    }
                ],
                "views": [
                    {
                        "_id": "0000",
                        "name": "Default View",
                        "type": "table",
                        "is_locked": false,
                        "rows": [],
                        "formula_rows": {},
                        "summaries": [],
                        "filters": [],
                        "sorts": [],
                        "hidden_columns": [],
                        "groupbys": [],
                        "groups": []
                    }
                ]
            }
        ],
        "version": 482,
        "format_version": 7,
        "settings": {
            "securities": {
                "table_settings": {
                    "can_copy": false,
                    "can_export": false,
                    "can_print": false
                },
                "share_user_settings": {
                    "can_copy": false,
                    "can_export": false,
                    "can_print": false
                }
            }
        }
    }
}
```

É claro que este código não é prático quando se pede ajuda no fórum da comunidade, pelo que a estrutura desta tabela deve ser reduzida às linhas seguintes.

```bash
--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---
Table: Table1 (ID: 0000)
--> Name (text)
```

Pode descobrir exactamente como isto funciona neste artigo.

{{< warning  headline="Se quiser saber mais sobre Python"  text="Existem inúmeras instruções, tutoriais e ajuda na Internet sobre Python. No entanto, um bom ponto de partida é certamente o sítio Web oficial do [Python](https://www.python.org/about/gettingstarted/), que também oferece uma coleção de [tutoriais para principiantes](https://wiki.python.org/moin/BeginnersGuide/Programmers)." />}}

## O código Python para a leitura da infra-estrutura

Em SeaTable, apenas algumas linhas de código Python são suficientes para obter a infra-estrutura de uma base. Especificamente, algumas linhas são suficientes para autenticação e uma linha para a infra-estrutura de metragem.

```python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
metadata = base.get_metadata()
print(metadata)

```

No entanto, o resultado ou a produção da infra-estrutura é tudo menos fácil de utilizar.

```python
{'tables': [{'_id': '0000', 'name': 'Table1', 'columns': [{'key': '0000', 'name': 'Name', 'type': 'text', 'width': 200, 'editable': True, 'resizable': True}], 'views': [{'_id': '0000', 'name': 'Default View', 'type': 'table', 'is_locked': False, 'rows': [], 'formula_rows': {}, 'summaries': [], 'filter_conjunction': 'And', 'filters': [], 'sorts': [], 'hidden_columns': [], 'groupbys': [], 'groups': []}]}], 'version': 13, 'format_version': 9, 'scripts': [{'name': 'Untitled', 'url': '/scripts/zkon.py', '_id': 'zkon', 'type': 'Python'}]}
```

## Transformar a infra-estrutura em outra forma

A variável **metadados** armazena agora toda a meta-estrutura com todos os seus elementos em formato JSON. O SeaTable e o Python oferecem, naturalmente, possibilidades para percorrer estas estruturas e interagir com elas.  
Com as linhas seguintes, a meta-estrutura pode ser colocada na forma desejada.

```python
print("--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---")
for table in metadata['tables']:
  print('.')
  print("Table: "+table['name']+" (ID: "+table['_id']+")")
  for column in table['columns']:
    print("  --> "+column['name']+" ("+column['type']+")")
```

O que acontece aqui exatamente? Primeiro, damos instruções ao Python para criar todas as tabelas com um **for**\-loop. De seguida, introduz-se o número com **print** o nome da tabela e o seu ID. Aqui também pode ver como aceder aos elementos individuais com os parênteses rectos.

Repetir o mesmo para as colunas. Através das **for**\-loop, todas as colunas da respectiva tabela são produzidas.

{{< warning  headline="Indentações de notas em Python"  text="Em Python, a indentação de linha é usada para estruturar o código. Isto mantém o código curto e claro. Portanto, você deve prestar muita atenção às indentações, pois elas determinam onde o _loop for_ termina." />}}

## Adição de links

Agora está quase lá. Já podia utilizar a meta-estrutura tão bem, mas uma fraqueza do guião anterior é que, com as colunas de ligação, não é óbvio para onde se ligam exatamente. Por isso, substitua as duas últimas colunas pelo seguinte código:

```python
  for column in table['columns']:
    link_target = ""
    if column['type'] == "link":
      link_target = " --> "+column['data']['other_table_id']
      if column['data']['other_table_id'] == table['_id']:
        link_target = " --> "+column['data']['table_id']
    print("  --> "+column['name']+" ("+column['type']+")")
```

## O guião completo

O script completo pode ser executado diretamente em qualquer base SeaTable sem quaisquer ajustes. Servir-lhe-á bem se quiser descrever a estrutura da sua base no fórum da comunidade.

```python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()

metadata = base.get_metadata()

print("--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---")
for table in metadata['tables']:
  print('.')
  print("Table: "+table['name']+" (ID: "+table['_id']+")")
  for column in table['columns']:
    link_target = ""
    if column['type'] == "link":
      link_target = " --> "+column['data']['other_table_id']
      if column['data']['other_table_id'] == table['_id']:
        link_target = " --> "+column['data']['table_id']
    print("  --> "+column['name']+" ("+column['type']+link_target+")")

```
