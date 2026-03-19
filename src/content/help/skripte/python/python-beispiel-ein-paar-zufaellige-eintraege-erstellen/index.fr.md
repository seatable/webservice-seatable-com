---
title: 'Exemple Python : Créer quelques entrées aléatoires'
date: 2023-03-02
lastmod: '2023-03-22'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/python-exemples-aleatoires-seatable'
aliases:
  - '/fr/aide/python-beispiel-ein-paar-zufaellige-eintraege-erstellen'
seo:
    title: 'Python : générer des exemples aléatoires sur SeaTable'
    description: 'Ajoutez rapidement des lignes aléatoires à une base SeaTable grâce à un script Python : tests, remplissage automatique et gain de temps pour vos démos et essais.'

---


Parfois, on souhaite générer quelques exemples d'entrées dans une base. Avec ce script Python, vous pouvez générer très rapidement de quelques entrées à plusieurs milliers.

Cet article vous guide à travers les différentes sections du script afin que vous puissiez comprendre son fonctionnement et l'adapter à vos besoins si nécessaire. Vous trouverez le script complet à la fin de cet article.

## 1) Charger les modules

Chaque script Python commence par le chargement des modules Python utilisés. Nous utiliserons _Base_ et _context_ de la classe _seatable_api_. Vous n'avez besoin du module _random_ de la deuxième ligne que si vous voulez générer des nombres aléatoires.

```python
from seatable_api import Base, context
import random
```

## 2) Authentification

Les deux lignes suivantes sont nécessaires pour établir la connexion avec la base actuelle. Après cette authentification, nous pouvons soit lire, soit supprimer, soit manipuler des informations via l'_objet base_.

```python
base = Base(context.api_token, context.server_url)
base.auth()
```

## 3) Définir de nouveaux contenus de ligne

Maintenant que nous avons accès au tableau actuel, nous pouvons définir les enregistrements à créer. Le code suivant part du principe que vous avez des colonnes nommées _Name_, _single_, _random_, _rating_. Si vos colonnes s'appellent autrement, vous devez adapter les noms en conséquence.

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

## 4) Écrire de nouvelles lignes

Avec le dernier bloc de code, le contenu des nouvelles lignes a certes été défini et enregistré dans la variable _rows_data_, mais il n'a pas encore été écrit dans la base. Nous le faisons maintenant avec l'appel suivant.

```python
# append the two rows
  base.batch_append_rows(context.current_table, rows_data)
```

## 5) Si vous voulez plus de lignes

Vous pouvez bien entendu écrire plus de deux lignes. Pour ce faire, il vous suffit de définir d'autres contenus de ligne ou d'exécuter plusieurs fois le processus d'écriture à l'aide d'une boucle.

```python
# execute batch append 10 times
for i in range(10):

  # define the data for two new rows
  ...

  # append the two rows
  ...
```

{{< warning  headline="Respecter les indentations en Python"  text="En Python, l'indentation des lignes est utilisée pour structurer le code. Cela permet de garder un code court et clair, mais en même temps, vous devez faire attention à l'indentation, car elle détermine où la _boucle for_ se termine." />}}

## Le script complet

Le script complet devrait pouvoir être exécuté immédiatement chez vous sans grandes adaptations. Modifiez les quatre noms de colonnes et le script devrait pouvoir créer de nouvelles lignes dans votre tableau.

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

Le script peut être lancé manuellement, via un bouton ou par automatisation. Pour en savoir plus, [cliquez ici]({{< relref "help/skripte/allgemein/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren" >}}).
