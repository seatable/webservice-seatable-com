---
title: "Filtrer les entrées d'une vue"
date: 2022-11-16
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'kgr'
url: '/fr/aide/filtrer-entrees-vue-seatable'
aliases:
    - '/fr/aide/filtern-von-eintraegen-in-einer-ansicht'
seo:
    title: 'Filtrer les entrées dans une vue SeaTable : guide rapide et options avancées'
    description: 'Découvrez comment filtrer efficacement les données d’une vue SeaTable, appliquer de multiples critères par colonne et utiliser des groupes de filtres personnalisés.'
weight: 21
---

La fonction de filtre de SeaTable permet de filtrer les entrées souhaitées d'un tableau à l'aide de **règles de filtrage** et de n'afficher que les entrées qui répondent à certains critères. Le filtre défini se rapporte uniquement à **la vue active**.

{{< warning headline="Remarque importante" text="Avec les filtres, vous modifiez uniquement le nombre d'enregistrements affichés dans votre vue ! Le filtrage ne modifie pas la base de données et ne supprime pas les lignes invisibles. Par conséquent, si des enregistrements ont disparu, vérifiez si vous êtes dans la bonne vue ou si vous avez masqué des enregistrements à l'aide d'un filtre." />}}

## Filtrer les entrées d'une vue

![Filtrer les entrées](images/Filtern-von-Eintraegen-1.gif)

1. Sélectionnez la **vue** dans laquelle vous souhaitez définir un filtre.
2. Cliquez sur **Filtrer** dans les options d'affichage au-dessus du tableau.
3. Allez sur **Ajouter un filtre** ou **Ajouter un groupe de filtres**.
4. Dans le premier champ, sélectionnez la **colonne** pour laquelle vous souhaitez définir une règle de filtrage.
5. Dans le champ central, déterminez la **condition** selon laquelle les entrées doivent être filtrées.
6. Dans le dernier champ, décidez à quelle **option** ou **valeur** la condition doit se référer.

## Les différentes conditions de filtrage

SeaTable prend en charge le filtrage sur tous les [types de colonnes]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) sauf les boutons.

Selon le **type de colonne** que vous souhaitez filtrer, les conditions que vous pouvez sélectionner s'adaptent également.

### Voici quelques exemples

Voici les options de conditions dont vous disposez en cas de [Colonne de texte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}): 

![Filtrer la colonne de texte](images/filtern-von-eintraegen-5.png)

Voici les options de conditions dont vous disposez en cas de [Colonne de sélection unique]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}): 

![Filtre colonne de sélection unique](images/filtern-von-eintraegen-6.png)

Voici les options de conditions dont vous disposez en cas de [Colonne d'images]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}): 

![Filtrer la colonne d'images](images/filtern-von-eintraegen-7.png)

Les lignes **avec des cellules vides** dans la colonne de filtrage ne sont en principe pas affichées, à moins que vous ne recherchiez explicitement "est vide".

## Supprimer un filtre

Vous pouvez **supprimer** les filtres créés en cliquant sur le bouton **x**.

![Suppression d'un filtre d'une vue](images/filtern-von-eintraegen.png)

## Appliquer plusieurs filtres

Vous pouvez créer un ou plusieurs filtres qui restreignent davantage la première condition. Pour en savoir plus, consultez l'article [Lier les règles de filtrage avec ET et OU]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}}).

## Réorganiser les filtres

Vous pouvez déplacer et réorganiser les filtres en déplaçant la souris sur le **surface de préhension de six points**, maintenir enfoncé, tirer et relâcher.

![Filtrer les entrées Trier](images/Filtern-von-Eintraegen-2.gif)
