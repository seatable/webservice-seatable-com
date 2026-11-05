---
title: 'Estrutura dos dados do Gancho da Web'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/pt/ajuda/estrutura-dos-dados-do-webhook'
aliases:
  - '/pt/ajuda/struktur-der-webhook-daten'
seo:
    title: 'Estrutura dos dados do webhook SeaTable – guia e exemplos'
    description: 'Saiba como funciona o formato JSON dos webhooks no SeaTable – campos, eventos de acionamento e exemplos ilustrativos.'
---

Um gancho da SeaTable tem uma estrutura claramente definida. Isto permite que o evento seja facilmente processado por qualquer linguagem de programação. Este artigo apresenta a estrutura geral e os valores possíveis.

## Que mudanças é que um gancho da web desencadeia

Se for criado um webhook para uma base, é enviado um pedido HTTP para cada alteração ao conteúdo da base. Assim, por exemplo, as seguintes alterações desencadeiam um gancho da web:

- Uma nova fila é acrescentada ou duplicada.
- Uma linha é eliminada.
- O conteúdo de uma linha é alterado.
- É adicionada ou removida uma ligação.

Se uma operação alterar várias linhas ao mesmo tempo, é enviado apenas [um webhook para todas as linhas]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).

{{< warning headline="Isto não acciona um gancho da web" text="Alterações estruturais a uma base como a adição de uma nova coluna, um comentário de coluna, a criação de uma nova vista ou um bloqueio de linha **não acciona um gancho da web**." />}}

## Exemplos de anzóis enviados pela SeaTable

### Exemplo 1: uma nova linha foi adicionada (por exemplo, na interface web SeaTable, via formulário web ou via chamada API)

```
{
  "event": "update",
  "data": {
    "dtable_uuid": "fae0a3a42ba94df88e8303fd385e37de",
    "row_id": "Fk-i7xZGS5iA5aSvaG5HAA",
    "op_user": "4bc9a7c79c5942c5b6238413f2132bea@auth.local",
    "op_type": "insert_row",
    "op_time": 1649922777.279,
    "table_id": "9g8f",
    "table_name": "Opportunities",
    "row_name": "",
    "row_data": []
  }
}

```

Neste exemplo, a nova linha está vazia. Se já contiver valores, estes aparecem em _row\_data_.

### Exemplo 2: foi seleccionado um valor de selecção única

```
{
  "event": "update",
  "data": {
    "dtable_uuid": "fae0a3a42ba94df88e8303fd385e37de",
    "row_id": "QoNno3QiTF26sxmG1sl3_g",
    "op_user": "4bc9a7c79c5942c5b6238413f2132bea@auth.local",
    "op_type": "modify_row",
    "op_time": 1649929622.589,
    "table_id": "9g8f",
    "table_name": "Opportunities",
    "row_name": "",
    "row_data": [{
      "column_key": "589r",
      "column_name": "Prio",
      "column_type": "single-select",
      "column_data": {
        "options": [{
          "name": "++",
          "color": "#F4667C",
          "textColor": "#FFFFFF",
          "id": "381992"
        },
        {
          "name": "+",
          "color": "#FBD44A",
          "textColor": "#FFFFFF",
          "id": "830278"
        }
      ]},
      "value": "381992",
      "old_value": ""
    }]
  }
}

```

### Exemplo 3: uma linha foi eliminada

```
{
  "event": "update",
  "data": {
    "dtable_uuid": "fae0a3a42ba94df88e8303fd385e37de",
    "row_id": "QoNno3QiTF26sxmG1sl3_g",
    "op_user": "4bc9a7c79c5942c5b6238413f2132bea@auth.local",
    "op_type": "delete_row",
    "op_time": 1649929650.668,
    "table_id": "9g8f",
    "table_name": "Opportunities",
    "row_name": "",
    "row_data": []
  }
}

```

### Exemplo 4: foram alteradas várias linhas ao mesmo tempo

```
{
  "event": "update",
  "data": {
    "dtable_uuid": "fae0a3a42ba94df88e8303fd385e37de",
    "row_id": "QoNno3QiTF26sxmG1sl3_g",
    "op_user": "4bc9a7c79c5942c5b6238413f2132bea@auth.local",
    "op_type": "modify_row",
    "op_time": 1649929700.125,
    "table_id": "9g8f",
    "table_name": "Opportunities",
    "row_count": 5,
    "row_name": "",
    "row_data": [{
      "column_key": "0000",
      "column_name": "Name",
      "column_type": "text",
      "column_data": {},
      "value": "Valor novo",
      "old_value": "Valor antigo"
    }]
  }
}

```

### Exemplo 5: foi adicionada uma ligação

As ligações têm uma estrutura própria, sem _row\_id_ nem _row\_data_. Em vez disso, o webhook contém os dados das duas linhas ligadas:

```
{
  "event": "update",
  "data": {
    "dtable_uuid": "fae0a3a42ba94df88e8303fd385e37de",
    "op_user": "4bc9a7c79c5942c5b6238413f2132bea@auth.local",
    "op_type": "add_link",
    "op_time": 1649929800.512,
    "link_id": "x9Tq",
    "table1_id": "9g8f",
    "table1_name": "Opportunities",
    "table1_row_id": "QoNno3QiTF26sxmG1sl3_g",
    "table1_row_name": "",
    "table2_id": "0000",
    "table2_name": "Contactos",
    "table2_row_id": "Fk-i7xZGS5iA5aSvaG5HAA",
    "table2_row_name": "",
    "row_data1": [{ ... }],
    "row_data2": [{ ... }]
  }
}

```

## Possíveis valores que um gancho da web pode assumir

O pedido enviado por um webhook contém sempre os valores "event" e "data". Atualmente, o valor "event" é sempre "update". No futuro, é possível que outros valores sejam adicionados aqui.

O valor "data" contém um objeto com outros elementos. Para alterações em linhas, estes estão listados na tabela seguinte:

| Valor               | Tipo                               | Exemplo                                     |
| ------------------- | ---------------------------------- | ------------------------------------------- |
| **dtable_uuid**     | String (32)                        | fae0a3a42ba94df88e8303fd385e37de            |
| **row_id**          | String (22)                        | QoNno3QiTF26sxmG1sl3_g                      |
| **op_user**         | String (32) + "auth.local"         | 4bc9a7c79c5942c5b6238413f2132bea@auth.local |
| **op_type**         | insert_row, delete_row, modify_row | insert_row                                  |
| **op_time**         | Timestamp                          | 1649929650.668                              |
| **table_id**        | String (4)                         | 9g8f                                        |
| **table_name**      | String                             | Tarefas                                     |
| **row_count**       | Número                             | 5                                           |
| **row_name**        | String                             |                                             |
| **row_name_option** | Objeto ou string vazia             | { "name": "++", "id": "381992", ... }       |
| **row_data**        | Array                              | [ { ... } ]                                 |
| **op_app**          | String                             | Nome do token API                           |

O valor _row\_count_ só é incluído se uma operação for [executada como operação em lote]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}). Isto também pode acontecer em chamadas à API para uma única linha, sendo o valor então 1. O valor _row\_name\_option_ contém a opção selecionada se a primeira coluna da tabela for de seleção única.

Nas ligações, _op\_type_ assume os valores _add\_link_, _remove\_link_, _update\_links_ ou _update\_rows\_links_. Com _update\_rows\_links_, o webhook contém ainda os valores _row\_id\_list_ e _other\_rows\_ids\_map_ com as linhas afetadas.

## Conteúdo truncado

Um webhook não contém uma cópia completa da linha, mas trunca o conteúdo:

- Nas linhas alteradas, _row\_data_ contém no máximo 10 colunas.
- Os textos são cortados após 1.000 caracteres.
- As listas, como os valores de uma seleção múltipla ou as opções em _column\_data_, são cortadas após 10 entradas.

Se precisar dos dados completos, leia depois a linha através da API.

Equipado com esta estrutura, pode agora desenvolver a sua própria interface Webhook.
