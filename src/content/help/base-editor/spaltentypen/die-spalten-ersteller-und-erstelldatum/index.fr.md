---
title: 'Les colonnes Créateur et Date de création'
date: 2023-01-20
lastmod: '2023-08-04'
categories:
    - 'datum-dauer-und-personen'
author: 'nsc2'
url: '/fr/aide/colonnes-createur-cree-seatable'
aliases:
    - '/fr/aide/die-spalten-ersteller-und-erstelldatum'
seo:
    title: "Types de colonnes SeaTable | Enregistrer automatiquement l'auteur et la date"
    description: "Un contrôle total au sein de l'équipe : découvrez comment ces colonnes enregistrent automatiquement les entrées et assurent la traçabilité des processus"
weight: 21
---

Les colonnes **Créateur** et **Date de création** sont exclusivement remplies **automatiquement** par SeaTable et constituent donc des types de colonnes particuliers. Alors que SeaTable remplit la colonne Créateur avec le **nom de l'utilisateur** qui a créé une ligne, il enregistre dans la colonne Date de création le **moment** (date et heure) où l'utilisateur a créé la ligne.

![Les colonnes "Créateur" et "Créé" après la création d'un utilisateur](images/column-creator-and-created-time.png)

## Particularités des deux types de colonnes

- Les valeurs saisies automatiquement dans les colonnes Créateur et Date de création ne peuvent **pas** être modifiées.
- Lors de la **création** des deux types de colonnes, **aucune** option n'est disponible, hormis le nom de la colonne.
- Il n'est possible de créer qu'**une seule** colonne "créateur" et une seule colonne "date de création" par tableau. Si vous essayez de créer une autre colonne du même type, le message "Une autre colonne a ce type de colonne" apparaît.

![Message d'erreur pour une autre colonne de créateur](images/Fehlermeldung-bei-weiterer-Ersteller-Spalte.png)

- C'est pourquoi vous ne pouvez **pas dupliquer** les colonnes "Créateur" et "Date de création" **ni adapter leur type de colonne**.
