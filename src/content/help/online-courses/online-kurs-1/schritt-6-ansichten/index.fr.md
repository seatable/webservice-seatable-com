---
title: 'Étape 6 : Créer des vues'
date: 2024-08-30
lastmod: '2024-09-19'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/fr/aide/etape-6-vues'
aliases:
    - '/fr/aide/schritt-6-ansichten'
seo:
    title: 'Étape 6 : Créer et filtrer des vues pour mieux gérer vos données SeaTable'
    description: 'Découvrez comment créer, filtrer, trier et regrouper des vues dans SeaTable pour ne voir que les données importantes et optimiser votre gestion.'
---

Vous avez créé une solide gestion des dépenses, qui calcule déjà automatiquement le total des dépenses par catégorie. Vous allez maintenant découvrir une autre fonctionnalité de SeaTable : **les vues**.

Les vues vous permettent de déterminer quelles données d'un tableau doivent être affichées en utilisant des filtres, des tris, des regroupements et en masquant des informations. Les vues s'appliquent toujours par tableau et vous pouvez créer autant de vues que vous le souhaitez. Vous obtenez ainsi toujours les informations qui vous intéressent.

Un exemple : vous pourriez créer une vue qui n'affiche que les dépenses supérieures à 100 euros et les trie par date. Cela vous permettra de garder une trace des dépenses importantes.

{{< warning  headline="Les modifications apportées aux données s'appliquent à toutes les vues"  text="Il est important de garder à l'esprit qu'une vue n'est qu'une représentation différente des mêmes données. Les modifications apportées aux enregistrements d'une vue se répercutent sur toutes les vues du même tableau, car elles accèdent toutes au même enregistrement." />}}

## Créer une vue supplémentaire avec un regroupement

Passez au tableau `Expenses` et créez une nouvelle vue. Choisissez un nom qui indique clairement l'objectif de la vue, comme par exemple `Group by date and category`.

Au départ, chaque nouvelle vue créée ne contient pas de regroupements, de tris ou de filtres. Nous voulons maintenant changer cela :

1. Regroupez les données dans la colonne `Date` par année.
2. Regroupez ensuite les données par `Category-Link`.

![Vue « Group by date and category » avec regroupement par année et lien de catégorie](images/lvl1-view-groups.png)

## Créer une vue avec un filtre et un regroupement

Maintenant que vous maîtrisez le regroupement de vos données, passons au filtrage des données à l'aide d'une vue.

Créez une nouvelle vue nommée `Clothing Expenses by Year` pour représenter les dépenses annuelles en vêtements :

1. Ajoutez un filtre : `Category-Link` contient `Clothing` pour n'afficher que les entrées de cette catégorie.
2. Regroupez les données filtrées par année.

Maintenant, en quelques clics, vous avez créé une vue qui vous présente clairement les dépenses en vêtements, regroupées par année.

## Expérimentez d'autres vues

C'est la fin de ce cours en ligne, qui marque aussi le début de votre parcours avec SeaTable. Prenez quelques minutes pour expérimenter d'autres vues – les comprendre est l'un des aspects les plus importants de l'utilisation de SeaTable.

Nous vous encourageons à mieux connaître SeaTable. Vous avez déjà créé un outil puissant, mais il y a encore beaucoup de choses à découvrir !

Lorsque vous aurez fait suffisamment d'expériences, essayez de terminer le quiz et gagnez votre récompense sur notre forum communautaire.

## Article d'aide avec plus d'informations

- [Qu'est-ce qu'une vue ?]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}})
- [Regroupement, tri et filtre]({{< relref "help/base-editor/ansichten/gruppierung-sortierung-und-filter" >}})
- [Créer une nouvelle vue]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}})
- [Épingler les vues]({{< relref "help/base-editor/ansichten/ansichten-pinnen" >}})
- [La barre d'état et ses fonctions]({{< relref "help/base-editor/ansichten/die-status-zeile-und-ihre-funktionen" >}})
