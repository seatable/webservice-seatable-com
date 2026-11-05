---
title: 'Структура данных Webhook'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/ru/pomoshch/struktura-dannykh-webhook-seatable'
aliases:
  - '/ru/pomoshch/struktur-der-webhook-daten'
seo:
    title: 'Структура данных webhook SeaTable – примеры и описание'
    description: 'Узнайте, как устроен webhook SeaTable: JSON‑поля, примеры событий и типы операций — insert_row, modify_row, delete_row.'
---

Webhook от SeaTable имеет четко определенную структуру. Это позволяет легко обрабатывать событие любым языком программирования. В этой статье представлена общая структура и возможные значения.

## Какие изменения вызывает webhook

Если для базы настроен webhook, то при каждом изменении содержимого базы отправляется HTTP-запрос. Так, например, следующие изменения вызывают срабатывание webhook:

- Добавляется или дублируется новый ряд.
- Строка удаляется.
- Содержимое строки изменяется.
- Добавляется или удаляется связь.

Если одна операция изменяет несколько строк одновременно, отправляется только [один webhook для всех строк]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}).

{{< warning headline="Это не приводит к срабатыванию webhook" text="Структурные изменения базы, такие как добавление нового столбца, комментария к столбцу, создание нового представления или блокировка строки, **не вызывают webhook**." />}}

## Примеры webhooks, отправляемых SeaTable

### Пример 1: был добавлен новый ряд (например, в веб-интерфейсе SeaTable, через веб-форму или через вызов API)

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

В этом примере новая строка пуста. Если она уже содержит значения, они указываются в _row\_data_.

### Пример 2: было выбрано значение с единственным выбором

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

### Пример 3: строка была удалена

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

### Пример 4: несколько строк были изменены одновременно

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
      "value": "Новое значение",
      "old_value": "Старое значение"
    }]
  }
}

```

### Пример 5: была добавлена связь

У связей собственная структура без _row\_id_ и _row\_data_. Вместо этого webhook содержит данные обеих связанных строк:

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
    "table2_name": "Контакты",
    "table2_row_id": "Fk-i7xZGS5iA5aSvaG5HAA",
    "table2_row_name": "",
    "row_data1": [{ ... }],
    "row_data2": [{ ... }]
  }
}

```

## Возможные значения, которые может принимать webhook

Запрос, отправляемый webhook, всегда содержит значения "event" и "data". В настоящее время значение "event" всегда равно "update". В будущем здесь могут появиться и другие значения.

Значение "data" содержит объект с другими элементами. При изменении строк они перечислены в следующей таблице:

| Значение            | Тип                                | Пример                                      |
| ------------------- | ---------------------------------- | ------------------------------------------- |
| **dtable_uuid**     | Строка (32)                        | fae0a3a42ba94df88e8303fd385e37de            |
| **row_id**          | Строка (22)                        | QoNno3QiTF26sxmG1sl3_g                      |
| **op_user**         | Строка (32) + "auth.local"         | 4bc9a7c79c5942c5b6238413f2132bea@auth.local |
| **op_type**         | insert_row, delete_row, modify_row | insert_row                                  |
| **op_time**         | Временная метка                    | 1649929650.668                              |
| **table_id**        | Строка (4)                         | 9g8f                                        |
| **table_name**      | Строка                             | Задачи                                      |
| **row_count**       | Число                              | 5                                           |
| **row_name**        | Строка                             |                                             |
| **row_name_option** | Объект или пустая строка           | { "name": "++", "id": "381992", ... }       |
| **row_data**        | Массив                             | [ { ... } ]                                 |
| **op_app**          | Строка                             | Имя токена API                              |

Значение _row\_count_ присутствует только в том случае, если операция [выполняется как пакетная]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}). Это возможно и при вызовах API для одной строки, тогда значение равно 1. Значение _row\_name\_option_ содержит выбранный вариант, если первый столбец таблицы является столбцом с единичным выбором.

Для связей _op\_type_ принимает значения _add\_link_, _remove\_link_, _update\_links_ или _update\_rows\_links_. При _update\_rows\_links_ webhook дополнительно содержит значения _row\_id\_list_ и _other\_rows\_ids\_map_ с затронутыми строками.

## Сокращённое содержимое

Webhook содержит не полную копию строки, а сокращённое содержимое:

- Для изменённых строк _row\_data_ содержит не более 10 столбцов.
- Текст обрезается после 1000 символов.
- Списки, например значения множественного выбора или варианты в _column\_data_, обрезаются после 10 элементов.

Если вам нужны полные данные, затем прочитайте строку через API.

Вооружившись этой структурой, вы теперь можете разработать свой собственный интерфейс Webhook.
