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

Vous disposez maintenant d'un vrai outil de suivi des dépenses, qui calcule déjà tout seul le total par catégorie. Découvrons une autre fonctionnalité de SeaTable : **les vues**.

Une vue détermine quelles données d'un tableau s'affichent, et comment : filtres, tris, regroupements, colonnes masquées. Chaque vue appartient à un tableau, et vous pouvez en créer autant que vous le souhaitez. Vous avez ainsi toujours sous les yeux les informations qui vous intéressent.

Un exemple : une vue qui n'affiche que les dépenses de plus de 100 euros, triées par date, vous permet de garder un œil sur les grosses dépenses.

{{< warning  headline="Une modification vaut pour toutes les vues"  text="Gardez à l'esprit qu'une vue n'est qu'une autre façon d'afficher les mêmes données. Si vous modifiez un enregistrement dans une vue, la modification apparaît dans toutes les vues du tableau, puisque les lignes affichées représentent toutes les mêmes enregistrements." />}}

## Créer une vue avec des regroupements

Ouvrez le tableau `Expenses` et créez une nouvelle vue. Donnez-lui un nom qui dit à quoi elle sert, par exemple `Group by date and category`.

Une nouvelle vue ne contient au départ ni regroupement, ni tri, ni filtre. Changeons cela :

1. Regroupez les lignes par année de la colonne `Date`.
2. Regroupez-les ensuite par `Category-Link`.

![Vue « Group by date and category » avec regroupement par année et lien de catégorie](images/lvl1-view-groups.png)

## Créer une vue avec un filtre et un regroupement

Vous savez maintenant regrouper vos données ; passons au filtrage.

Créez une nouvelle vue nommée `Clothing Expenses by Year`, qui affichera les dépenses de vêtements année par année :

1. Ajoutez un filtre `Category-Link` contient `Clothing`, pour n'afficher que les lignes de cette catégorie.
2. Regroupez les lignes filtrées par année.

En quelques clics, vous avez créé une vue qui présente clairement vos dépenses de vêtements, année par année.

## Essayez de créer d'autres vues

Ce cours touche à sa fin, mais votre parcours avec SeaTable ne fait que commencer. Prenez quelques minutes pour essayer d'autres vues : bien les comprendre est essentiel pour tirer parti de SeaTable.

Continuez à explorer SeaTable : vous avez déjà créé un outil puissant, mais il vous reste encore beaucoup à découvrir !

Quand vous aurez assez exploré, tentez le quiz et décrochez votre badge sur notre forum communautaire.

## Article d'aide avec plus d'informations

- [Qu'est-ce qu'une vue ?]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}})
- [Regroupement, tri et filtre]({{< relref "help/base-editor/ansichten/gruppierung-sortierung-und-filter" >}})
- [Créer une nouvelle vue]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}})
- [Épingler les vues]({{< relref "help/base-editor/ansichten/ansichten-pinnen" >}})
- [La barre d'état et ses fonctions]({{< relref "help/base-editor/ansichten/die-status-zeile-und-ihre-funktionen" >}})
