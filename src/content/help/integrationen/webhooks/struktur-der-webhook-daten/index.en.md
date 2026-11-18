---
title: 'Webhook data structure'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/help/webhook-data-structure'
aliases:
  - '/help/struktur-der-webhook-daten'
seo:
    title: 'Webhook data structure in SeaTable – format & examples'
    description: 'Understand SeaTable’s webhook JSON format: full data schema, sample payloads and trigger events like insert_row or modify_row.'
---

A webhook from SeaTable has a uniquely defined structure. This allows easy processing of the event by any programming language. This article presents the general structure and the possible values.

## What changes triggers a webhook

When a webhook is set up for a base, an HTTP request is sent for each change to the contents of the base. Thus, for example, the following changes trigger a webhook:

- A new row is added or duplicated.
- A row will be deleted.
- A line content is changed.
- A link is added or removed.

If one operation changes several rows at the same time, only [one webhook for all rows]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}) is sent.

{{< warning headline="This does not trigger a webhook" text="Structural changes to a base such as adding a new column, a column comment, creating a new view or a row lock **does not trigger a webhook**." />}}

## Examples of webhooks sent by SeaTable

### Example 1: a new row was added (e.g. in the SeaTable web interface, via web form or via API call)

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

In this example, the new row is empty. If it already contains values, they are listed in _row\_data_.

### Example 2: a single-select value was selected

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

### Example 3: a row has been deleted

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

### Example 4: several rows were changed at the same time

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
      "value": "New value",
      "old_value": "Old value"
    }]
  }
}

```

### Example 5: a link was added

Links have their own structure without _row\_id_ and _row\_data_. Instead, the webhook contains the details of both linked rows:

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
    "table2_name": "Contacts",
    "table2_row_id": "Fk-i7xZGS5iA5aSvaG5HAA",
    "table2_row_name": "",
    "row_data1": [{ ... }],
    "row_data2": [{ ... }]
  }
}

```

## Possible values that a webhook can take on

The sent request of a webhook always contains the values "event" and "data". The value "event" is currently always "update". In the future, it is possible that other values will be added here.

The value "data" contains an object with further elements. For changes to rows, these are listed in the following table:

| Value               | Type                               | Example                                     |
| ------------------- | ---------------------------------- | ------------------------------------------- |
| **dtable_uuid**     | String (32)                        | fae0a3a42ba94df88e8303fd385e37de            |
| **row_id**          | String (22)                        | QoNno3QiTF26sxmG1sl3_g                      |
| **op_user**         | String (32) + "auth.local"         | 4bc9a7c79c5942c5b6238413f2132bea@auth.local |
| **op_type**         | insert_row, delete_row, modify_row | insert_row                                  |
| **op_time**         | Timestamp                          | 1649929650.668                              |
| **table_id**        | String (4)                         | 9g8f                                        |
| **table_name**      | String                             | Tasks                                       |
| **row_count**       | Number                             | 5                                           |
| **row_name**        | String                             |                                             |
| **row_name_option** | Object or empty string             | { "name": "++", "id": "381992", ... }       |
| **row_data**        | Array                              | [ { ... } ]                                 |
| **op_app**          | String                             | API token name                              |

The value _row\_count_ is only included if an operation is [executed as a batch operation]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}). This can also be the case for API calls for a single row, in which case the value is 1. The value _row\_name\_option_ contains the selected option if the first column of the table is a single select.

For links, _op\_type_ takes the values _add\_link_, _remove\_link_, _update\_links_ or _update\_rows\_links_. For _update\_rows\_links_, the webhook also contains the values _row\_id\_list_ and _other\_rows\_ids\_map_ with the affected rows.

## Truncated content

A webhook does not contain a complete copy of the row, but truncates the content:

- For changed rows, _row\_data_ contains at most 10 columns.
- Text is cut off after 1,000 characters.
- Lists such as the values of a multiple select or the options in _column\_data_ are cut off after 10 entries.

If you need the complete data, read the row via the API afterwards.

Equipped with this structure, you can now develop your own Webhook interface.
