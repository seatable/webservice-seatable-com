---
title: 'Affichage conditionnel de champs de formulaire individuels'
date: 2023-01-08
lastmod: '2024-02-14'
categories:
    - 'webformulare'
author: 'vge'
url: '/fr/aide/affichage-conditionnel-champs-formulaire'
aliases:
    - '/fr/aide/bedingte-anzeige-von-einzelnen-formularfeldern'
seo:
    title: 'Affichage conditionnel des champs de formulaire SeaTable : guide pratique'
    description: 'Découvrez comment afficher des champs de formulaires web SeaTable uniquement si une condition est remplie – pour des enquêtes dynamiques et des données fiables.'
weight: 4
---

Lors de la création de **formulaires web**, vous pouvez faire en sorte que certains **champs** ne soient visibles que lorsqu'une **condition** a été remplie dans un champ précédent. Cela vous permet d'améliorer le **guidage de l'utilisateur** lors du remplissage du formulaire.

## Définir une condition pour un champ de formulaire

1. Ouvrez un **formulaire web** existant.
2. Cliquez sur un champ pour ouvrir les **paramètres du champ**.
3. Allez à **Afficher le champ uniquement si les conditions sont remplies** et cliquez sur le bouton avec le symbole plus, qui vous permet d'**ajouter une condition**.
4. Sélectionnez le **champ précédent** auquel la condition doit se référer.
5. Définissez ensuite la **condition**. Selon le type de colonne sous-jacent, vous avez le choix entre différentes options.

{{< warning  headline="Remarque"  text="L'affichage conditionnel n'est possible que s'il existe au moins un champ précédent." />}}

## Exemple d'application

![Affichage conditionnel des champs dans les formulaires web](images/Bedingte-Anzeige-von-Feldern-in-Webformularen.gif)

Supposons que vous souhaitiez réaliser une enquête sur la satisfaction des employés de votre entreprise. Vous souhaitez par exemple poser la question suivante : "Dans quelle mesure êtes-vous satisfait de notre leasing de voitures de société ?", mais vous savez que seuls les employés occupant un poste de direction se voient proposer une voiture de société. Vous souhaitez donc poser cette question uniquement à vos cadres.

Tout d'abord, vous devez créer une [colonne d'évaluation]({{< relref "help/base-editor/spaltentypen/die-rating-spalte" >}}) dans votre tableau et l'intégrer comme **champ** dans votre formulaire web. Ajoutez ensuite la **condition** que le champ d'évaluation ne s'affiche que si l'option "Head of" ou "Team lead" a été sélectionnée dans le **champ de sélection "Position"** précédent. Le champ de sélection devrait exiger une **saisie obligatoire**, sinon les cadres qui laissent ce champ vide ne verront pas non plus la question sur le leasing de voitures de société.

Pour éviter que les participants ne fassent apparaître des champs masqués simplement en testant les conditions, vous pouvez insérer des **sauts de page**. Ainsi, après avoir rempli le champ obligatoire, les participants doivent d'abord cliquer sur **Page suivante** et les champs conditionnels s'y affichent ou non.
