---
title: 'Structure des données du webhook'
date: 2023-02-28
lastmod: '2026-11-05'
categories:
    - 'webhooks'
author: 'cdb'
url: '/fr/aide/structure-donnees-webhook'
aliases:
  - '/fr/aide/struktur-der-webhook-daten'
seo:
    title: 'Structure des données du webhook SeaTable – guide complet'
    description: 'Découvrez la structure JSON des webhooks SeaTable : champs disponibles, exemples d’événements et types d’opérations pris en charge.'
---

Un webhook de SeaTable a une structure clairement définie. Cela permet de traiter facilement l'événement par n'importe quel langage de programmation. Cet article présente la structure générale et les valeurs possibles.

## Quels changements déclenche un webhook

Lorsqu'un webhook est mis en place pour une base, une requête HTTP est envoyée pour chaque modification du contenu de la base. Ainsi, les modifications suivantes, par exemple, déclenchent un webhook :

- Une nouvelle ligne est ajoutée ou dupliquée.
- Une ligne est supprimée.
- Un contenu de ligne est modifié.
- Un lien est ajouté ou supprimé.

Si une opération modifie plusieurs lignes à la fois, [un seul webhook pour toutes les lignes]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}) est envoyé.

{{< warning headline="Cela ne déclenche pas de webhook" text="Les modifications structurelles d'une base, telles que l'ajout d'une nouvelle colonne, un commentaire de colonne, la création d'une nouvelle vue ou le verrouillage d'une ligne **, ne déclenchent pas de webhook**." />}}

## Exemples de webhooks envoyés par SeaTable

### Exemple 1 : une nouvelle ligne a été ajoutée (par exemple dans l'interface web SeaTable, par formulaire web ou par appel API)

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

Dans cet exemple, la nouvelle ligne est vide. Si elle contient déjà des valeurs, celles-ci figurent dans _row\_data_.

### Exemple 2 : une valeur Single-Select a été sélectionnée

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

### Exemple 3 : une ligne a été supprimée

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

### Exemple 4 : plusieurs lignes ont été modifiées en même temps

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
      "value": "Nouvelle valeur",
      "old_value": "Ancienne valeur"
    }]
  }
}

```

### Exemple 5 : un lien a été ajouté

Les liens ont leur propre structure, sans _row\_id_ ni _row\_data_. À la place, le webhook contient les informations sur les deux lignes liées :

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

## Valeurs possibles qu'un webhook peut prendre

La requête envoyée d'un webhook contient toujours les valeurs "event" et "data". La valeur "event" est actuellement toujours "update". Il se peut qu'à l'avenir, d'autres valeurs soient ajoutées ici.

La valeur "data" contient un objet avec d'autres éléments. Pour les modifications de lignes, ceux-ci sont énumérés dans le tableau suivant :

| Valeur              | Type                               | Exemple                                     |
| ------------------- | ---------------------------------- | ------------------------------------------- |
| **dtable_uuid**     | Chaîne (32)                        | fae0a3a42ba94df88e8303fd385e37de            |
| **row_id**          | Chaîne (22)                        | QoNno3QiTF26sxmG1sl3_g                      |
| **op_user**         | Chaîne (32) + "auth.local"         | 4bc9a7c79c5942c5b6238413f2132bea@auth.local |
| **op_type**         | insert_row, delete_row, modify_row | insert_row                                  |
| **op_time**         | Horodatage                         | 1649929650.668                              |
| **table_id**        | Chaîne (4)                         | 9g8f                                        |
| **table_name**      | Chaîne                             | Tâches                                      |
| **row_count**       | Nombre                             | 5                                           |
| **row_name**        | Chaîne                             |                                             |
| **row_name_option** | Objet ou chaîne vide               | { "name": "++", "id": "381992", ... }       |
| **row_data**        | Tableau                            | [ { ... } ]                                 |
| **op_app**          | Chaîne                             | Nom du jeton API                            |

La valeur _row\_count_ n'est incluse que si une opération est [exécutée sous forme d'opération par lots]({{< relref "help/integrationen/webhooks/webhook-bei-mehreren-gleichzeitigen-aenderungen" >}}). Cela peut aussi être le cas pour des appels API portant sur une seule ligne, la valeur est alors 1. La valeur _row\_name\_option_ contient l'option sélectionnée si la première colonne de la table est une sélection unique.

Pour les liens, _op\_type_ prend les valeurs _add\_link_, _remove\_link_, _update\_links_ ou _update\_rows\_links_. Avec _update\_rows\_links_, le webhook contient en outre les valeurs _row\_id\_list_ et _other\_rows\_ids\_map_ avec les lignes concernées.

## Contenu tronqué

Un webhook ne contient pas une copie complète de la ligne, mais tronque le contenu :

- Pour les lignes modifiées, _row\_data_ contient au maximum 10 colonnes.
- Les textes sont coupés après 1 000 caractères.
- Les listes, comme les valeurs d'une sélection multiple ou les options de _column\_data_, sont coupées après 10 entrées.

Si vous avez besoin des données complètes, lisez ensuite la ligne via l'API.

Muni de cette structure, vous pouvez maintenant développer votre propre interface Webhook.
