---
title: 'Exemple Python : Ajouter des lignes automatiquement'
date: 2023-03-02
lastmod: '2026-03-18'
categories:
    - 'javascript-python'
author: 'cdb'
url: '/fr/aide/python-ajouter-lignes'
seo:
    title: 'Python : Ajouter des lignes automatiquement dans SeaTable'
    description: 'Utilisez ce script Python pour ajouter automatiquement des entrées récurrentes dans votre base SeaTable avec vérification des doublons.'
---


Ce script crée automatiquement des entrées mensuelles récurrentes dans une table. Il vérifie par requête SQL si des entrées existent déjà pour le mois en cours et ne crée que les manquantes. Vous pouvez ainsi le configurer comme automation planifiée (par ex. le 1er de chaque mois) sans créer de doublons.

![Monthly Expenses in SeaTable](monthly-expenses.png)

{{< dtable-download name="Monthly Expenses" file="/downloads/python-examples/monthly-expenses.dtable" text="Base avec données d'exemple et script prêt à l'emploi pour essayer directement." />}}

## Prérequis

La table nécessite au moins les colonnes suivantes :

- **Category** (Sélection simple) — type d'entrée
- **Description** (Texte) — description
- **Amount** (Nombre) — montant
- **Month** (Date) — mois de facturation
- **Type** (Sélection simple) — par ex. Expense ou Income

## Le script

Adaptez `TABLE_NAME` et les entrées dans `ENTRIES` à la structure de votre table. Les valeurs des colonnes de sélection simple sont automatiquement créées comme nouvelles options si elles n'existent pas encore.

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

Pour la référence complète des fonctions, consultez le [SeaTable Developer Manual](https://developer.seatable.com/python/objects/).
