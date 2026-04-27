---
title: "Exemple Python : lire la métastructure d'une base"
date: 2023-03-22
lastmod: '2023-07-25'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/exemple-python-lire-metastructure-base'
aliases:
    - '/fr/aide/python-beispiel-die-metastruktur-einer-base-auslesen'
seo:
    title: 'Exemple Python : lire la métastructure d’une base'
    description: 'Apprenez à lire et organiser la métastructure d’une base SeaTable avec un script Python – liens, colonnes et sortie détaillée.'
weight: 4
---

Cet article vous présente un script Python qui permet d'afficher la métastructure complète d'une base. Ceci est par exemple utile si vous avez une question sur une base dans le [forum de la communauté](https://forum.seatable.com/) et que vous souhaitez décrire la structure de votre base de manière simple et rapide sans avoir recours à des captures d'écran.

![Sortie de la métastructure dans SeaTable](base-metadata.png)

{{< dtable-download name="Base Metadata" file="/downloads/python-examples/base-metadata.dtable" text="Base avec plusieurs tables et liens pour essayer." />}}

## La métastructure d'une base

La métastructure d'une base décrit les tableaux, les colonnes et les vues d'une base. Les entrées et les enregistrements dans les lignes ne sont pas inclus dans la métastructure. La structure JSON suivante décrit une base relativement simple avec seulement un tableau, deux colonnes et une vue.

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

Ce code n'est évidemment pas pratique si vous demandez de l'aide sur le forum de la communauté, c'est pourquoi la structure de ce tableau doit être réduite aux lignes suivantes.

```bash
--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---
Table: Table1 (ID: 0000)
--> Name (text)
```

Vous découvrirez dans cet article comment cela fonctionne exactement.

{{< warning  headline="Si vous voulez en savoir plus sur Python"  text="Sur Internet, il existe d'innombrables instructions, tutoriels et aides concernant Python. Un bon premier point de départ est toutefois certainement le [site](https://www.python.org/about/gettingstarted/) officiel de [Python](https://www.python.org/about/gettingstarted/), qui propose également une collection de [tutoriels pour débutants](https://wiki.python.org/moin/BeginnersGuide/Programmers)." />}}

## Le code Python pour lire la métastructure

Dans SeaTable, quelques lignes de code Python suffisent pour obtenir la métastructure d'une base. Concrètement, quelques lignes suffisent pour l'authentification et une ligne pour la métastructure.

```python
from seatable_api import Base, context
base = Base(context.api_token, context.server_url)
base.auth()
metadata = base.get_metadata()
print(metadata)

```

Le résultat ou la sortie de la métastructure est toutefois loin d'être convivial.

```python
{'tables': [{'_id': '0000', 'name': 'Table1', 'columns': [{'key': '0000', 'name': 'Name', 'type': 'text', 'width': 200, 'editable': True, 'resizable': True}], 'views': [{'_id': '0000', 'name': 'Default View', 'type': 'table', 'is_locked': False, 'rows': [], 'formula_rows': {}, 'summaries': [], 'filter_conjunction': 'And', 'filters': [], 'sorts': [], 'hidden_columns': [], 'groupbys': [], 'groups': []}]}], 'version': 13, 'format_version': 9, 'scripts': [{'name': 'Untitled', 'url': '/scripts/zkon.py', '_id': 'zkon', 'type': 'Python'}]}
```

## Donner une autre forme à la métastructure

La variable **metadata** contient maintenant toute la métastructure et tous ses éléments au format JSON. SeaTable ou Python offrent bien entendu des possibilités de parcourir et d'interagir avec ces structures.  
Les lignes suivantes permettent de mettre la métastructure sous la forme souhaitée.

```python
print("--- COMPLETE BASE STRUCTURE WITH ALL BASES AND COLUMNS ---")
for table in metadata['tables']:
  print('.')
  print("Table: "+table['name']+" (ID: "+table['_id']+")")
  for column in table['columns']:
    print("  --> "+column['name']+" ("+column['type']+")")
```

Que se passe-t-il exactement ? Tout d'abord, vous demandez à Python d'enregistrer tous les tableaux avec un **for**\-pour passer à travers la boucle. Ensuite, utilisez **print** le nom du tableau et son ID. Vous voyez également ici comment accéder aux différents éléments à l'aide des crochets.

Répétez la même chose pour les colonnes. Grâce à la **for**\-Toutes les colonnes du tableau correspondant sont éditées dans la boucle d'affichage de l'état.

{{< warning  headline="Respecter les indentations en Python"  text="En Python, l'indentation des lignes est utilisée pour structurer le code. Cela permet de garder un code court et clair. C'est pourquoi il faut faire très attention aux indentations, car elles déterminent où la _boucle for_ se termine." />}}

## Ajout de liens

Vous y êtes presque. On pourrait déjà très bien utiliser la métastructure, mais l'une des faiblesses du script actuel est que les colonnes de liens ne permettent pas de savoir vers quoi elles renvoient exactement. C'est pourquoi vous remplacez les deux dernières colonnes par le code suivant :

```python
  for column in table['columns']:
    link_target = ""
    if column['type'] == "link":
      link_target = " --> "+column['data']['other_table_id']
      if column['data']['other_table_id'] == table['_id']:
        link_target = " --> "+column['data']['table_id']
    print("  --> "+column['name']+" ("+column['type']+")")
```

## Le script complet

Le script complet peut être exécuté directement dans n'importe quelle base SeaTable sans aucune adaptation. Il vous rendra de grands services si vous souhaitez décrire la structure de votre base sur le forum de la communauté.

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
