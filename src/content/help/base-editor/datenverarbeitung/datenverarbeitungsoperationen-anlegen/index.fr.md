---
title: 'Créer des opérations de traitement de données'
date: 2023-03-03
lastmod: '2023-03-13'
categories:
    - 'datenverarbeitung'
author: 'nsc2'
url: '/fr/aide/creer-operations-traitement-donnees'
aliases:
    - '/fr/aide/datenverarbeitungsoperationen-anlegen'
seo:
    title: 'Créer des opérations de traitement des données SeaTable'
    description: 'Apprenez à créer des opérations de calcul, liaisons et classements dans SeaTable pour automatiser et comparer vos données pas à pas.'

---

La fonction de traitement des données vous permet d'**effectuer** diverses **opérations**. Vous pouvez effectuer des calculs mathématiques sur toutes les valeurs d'une colonne ou établir une relation entre les valeurs si les entrées de deux tableaux différents sont identiques.

Vous pouvez créer des opérations de traitement des données à tout moment dans vos tableaux via les options d'affichage. Il vous suffit d'enregistrer les résultats d'une opération dans une colonne supplémentaire.

## Création d'une opération de traitement des données

![Création d'une action de traitement des données](images/create-an-data-processing-action-1.jpg)

1. Ouvrez n'importe quel **tableau** dans lequel vous souhaitez créer une opération de traitement des données.
2. Cliquez sur les **trois points** dans les options d'affichage.
3. Cliquez sur **Traitement des données**, puis sur **Ajouter une opération de traitement des données**.
4. Donnez un **nom** à l'opération.
5. Sélectionnez une **opération**.
6. Définissez, selon l'opération, le **tableau**, la **vue**, la **colonne source** et **la colonne résultat** ou les tableaux et colonnes à comparer.
7. Cliquez sur **Enregistrer** pour sauvegarder l'opération et l'exécuter plus tard, ou sur **Exécuter** pour lancer directement l'opération.

![Définition de l'action de traitement des données](images/define-data-processing-action.jpg)

## Opérations de traitement des données

Actuellement, les opérations suivantes sont disponibles :

- Calculer les valeurs cumulées
- Calculer le classement
- Calculer les changements
- Calculer le pourcentage
- Comparer et relier
- Comparer et copier
- Transférer le nom d'utilisateur

## Exigences

Les **conditions préalables** à la création d'une opération de traitement des données **varient** en fonction de l'opération.

Pour les calculs mathématiques, c'est-à-dire pour les opérations **Calculer les valeurs cumulées**, **Calculer le classement**, **Calculer les variations** et **Calculer le pourcentage**, vous avez besoin d'au moins **deux** [colonnes de chiffres]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}) dans la vue de tableau sélectionnée. En règle générale, la **colonne source** existe déjà et est remplie de données, alors que vous créez la **colonne de résultats** et la remplissez de valeurs par l'opération.

Pour les autres opérations, vous avez parfois besoin de [colonnes de liaison]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}})**(Comparer et relier** & **Comparer et copier**) ou [de colonnes de texte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}})**(Transférer le nom d'utilisateur**).
