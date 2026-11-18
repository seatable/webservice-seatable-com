---
title: 'Struktur der Webhook-Daten'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/de/hilfe/struktur-der-webhook-daten'
seo:
    title: 'Struktur der Webhook‑Daten in SeaTable – Erklärung & Beispiele'
    description: 'So ist ein SeaTable‑Webhook aufgebaut: Alle JSON‑Felder, Beispiel‑Events und typische Werte für insert_row, modify_row und delete_row erklärt.'
---

Ein Webhook aus SeaTable hat eine eindeutig festgelegte Struktur. Dies ermöglicht die einfache Verarbeitung des Ereignisses durch eine beliebige Programmiersprache. Diese Artikel stellt die allgemeine Struktur und die möglichen Werte vor.

## Welche Änderungen triggert ein Webhook

Wenn für eine Base ein Webhook eingerichtet wird, wird für jede Änderung an den Inhalten der Base ein HTTP-Request verschickt. Somit triggern z.B. die folgenden Änderungen einen Webhook:

- Eine neue Zeile wird hinzugefügt oder dupliziert.
- Eine Zeile wird gelöscht.
- Ein Zeileninhalt wird verändert.
- Eine Verknüpfung wird hinzugefügt oder entfernt.

Verändert ein Vorgang mehrere Zeilen gleichzeitig, wird nur [ein Webhook für alle Zeilen]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}) verschickt.

{{< warning headline="Das triggert keinen Webhook" text="Strukturelle Veränderungen an einer Base wie das Hinzufügen einer neuen Spalte, ein Spaltenkommentar, das Anlegen einer neuen Ansicht oder eine Zeilensperrung **triggert keinen Webhook**." />}}

## Beispiele von Webhooks, die SeaTable verschickt

### Beispiel 1: eine neue Zeile wurde hinzugefügt (z.B. im SeaTable Webinterface, per Webformular oder per API-Call)

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

In diesem Beispiel ist die neue Zeile leer. Enthält sie bereits Werte, stehen diese in _row\_data_.

### Beispiel 2: ein Single-Select Wert wurde ausgewählt

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

### Beispiel 3: eine Zeile wurde gelöscht

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

### Beispiel 4: mehrere Zeilen wurden gleichzeitig geändert

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
      "value": "Neuer Wert",
      "old_value": "Alter Wert"
    }]
  }
}

```

### Beispiel 5: eine Verknüpfung wurde hinzugefügt

Verknüpfungen haben eine eigene Struktur ohne _row\_id_ und _row\_data_. Stattdessen enthält der Webhook die Angaben zu beiden verknüpften Zeilen:

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
    "table2_name": "Kontakte",
    "table2_row_id": "Fk-i7xZGS5iA5aSvaG5HAA",
    "table2_row_name": "",
    "row_data1": [{ ... }],
    "row_data2": [{ ... }]
  }
}

```

## Mögliche Werte, die ein Webhook annehmen kann

Der gesendete Request eines Webhooks enthält immer die Werte "event" und "data". Der Wert "event" ist aktuell immer "update". In der Zukunft kann es sein, dass hier noch weitere Werte hinzukommen.

Der Wert "data" enthält ein Objekt mit weiteren Elementen. Bei Änderungen an Zeilen sind diese in der folgenden Tabelle aufgeführt:

| Wert                | Typ                                | Beispiel                                    |
| ------------------- | ---------------------------------- | ------------------------------------------- |
| **dtable_uuid**     | String (32)                        | fae0a3a42ba94df88e8303fd385e37de            |
| **row_id**          | String (22)                        | QoNno3QiTF26sxmG1sl3_g                      |
| **op_user**         | String (32) + "auth.local"         | 4bc9a7c79c5942c5b6238413f2132bea@auth.local |
| **op_type**         | insert_row, delete_row, modify_row | insert_row                                  |
| **op_time**         | Timestamp                          | 1649929650.668                              |
| **table_id**        | String (4)                         | 9g8f                                        |
| **table_name**      | String                             | Tasks                                       |
| **row_count**       | Zahl                               | 5                                           |
| **row_name**        | String                             |                                             |
| **row_name_option** | Object oder leerer String          | { "name": "++", "id": "381992", ... }       |
| **row_data**        | Array                              | [ { ... } ]                                 |
| **op_app**          | String                             | API token name                              |

Der Wert _row\_count_ ist nur enthalten, wenn ein Vorgang [als Batch-Operation ausgeführt wird]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}). Das kann auch bei API-Aufrufen für eine einzelne Zeile der Fall sein, der Wert ist dann 1. Der Wert _row\_name\_option_ enthält die ausgewählte Option, wenn die erste Spalte der Tabelle eine Einfachauswahl ist.

Bei Verknüpfungen nimmt _op\_type_ die Werte _add\_link_, _remove\_link_, _update\_links_ oder _update\_rows\_links_ an. Bei _update\_rows\_links_ enthält der Webhook zusätzlich die Werte _row\_id\_list_ und _other\_rows\_ids\_map_ mit den betroffenen Zeilen.

## Gekürzte Inhalte

Ein Webhook enthält keine vollständige Kopie der Zeile, sondern kürzt die Inhalte:

- _row\_data_ enthält bei geänderten Zeilen höchstens 10 Spalten.
- Texte werden nach 1.000 Zeichen abgeschnitten.
- Listen wie die Werte einer Mehrfachauswahl oder die Optionen in _column\_data_ werden nach 10 Einträgen abgeschnitten.

Wenn Sie die vollständigen Daten benötigen, lesen Sie die Zeile anschließend über die API aus.

Ausgestattet mit dieser Struktur können Sie nun Ihre eigene Webhook Schnittstelle entwickeln.
