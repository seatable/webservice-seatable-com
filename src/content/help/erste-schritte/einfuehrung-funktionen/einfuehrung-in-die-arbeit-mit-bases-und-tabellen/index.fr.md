---
title: 'Introduction au travail avec les bases et les tableaux'
date: 2023-01-07
lastmod: '2023-03-24'
categories:
    - 'seatable-nutzen'
author: 'cdb'
url: '/fr/aide/introduction-bases-tableaux-seatable'
aliases:
    - '/fr/aide/einfuehrung-in-die-arbeit-mit-bases-und-tabellen'
seo:
    title: 'Introduction aux bases et tableaux SeaTable – bonnes pratiques'
    description: 'Découvrez comment structurer, relier et gérer bases et tableaux dans SeaTable. Typologie, vues et les étapes clés pour réussir vos projets.'
---

Chacune des icônes carrées sur votre page d'accueil représente une **base**. Il s'agit d'une base de données, comparable à un classeur dans un tableur traditionnel, qui peut contenir plusieurs **tableaux** sur différents thèmes.

![Aperçu de la base dans SeaTable](images/base-overview.png)

Une base représente une **unité** fermée dans SeaTable. Elle doit donc contenir toutes les informations dont vous avez besoin pour un projet ou un processus spécifique.

La base de votre pipeline de vente peut par exemple contenir des tableaux séparés pour les prospects, les entreprises et les opportunités commerciales. De la même manière, vous pouvez utiliser une base pour l'organisation d'un mariage, puis créer des tableaux séparés pour les lieux potentiels, les participants et les listes de choses à faire.

## Créer une nouvelle base

SeaTable offre plusieurs possibilités pour créer une nouvelle base. Si vous êtes nouveau dans SeaTable, nous vous recommandons de commencer par un **modèle** afin de voir comment une base est généralement construite. Vous pouvez choisir un modèle existant, adapté à votre cas d'utilisation, dans notre galerie de modèles et l'adapter ensuite facilement à vos propres besoins.

Si vous êtes familier avec la création de vos propres tableaux, colonnes et vues, vous pouvez commencer avec une base vide.

- [Créer une base à l'aide d'un modèle]({{< relref "help/startseite/bases/anlegen-einer-base-mithilfe-einer-vorlage" >}})
- [Créer une nouvelle base]({{< relref "help/startseite/bases/eine-neue-base-erstellen" >}})
- [Importation de fichiers Excel dans SeaTable]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}})
- [Dupliquer une base existante]({{< relref "help/startseite/bases/duplizieren-einer-bestehenden-base" >}})

## Gérer les bases

Une fois que vous avez maîtrisé les premières étapes et créé vos premières bases, vous pouvez découvrir toute une palette de fonctions supplémentaires sur la page d'accueil et dans vos bases. Tout ce que vous devez savoir sur la gestion de vos bases est expliqué dans le chapitre [Bases]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}).

## Tableaux et vues dans une base

Le tableau est le niveau le plus important auquel vous pouvez organiser vos données dans SeaTable, comparable à une feuille de calcul dans un tableur. En principe, **les tableaux** représentent le niveau suivant dans la structure organisationnelle de SeaTable, en dessous des bases.

Comme SeaTable est une [base de données relationnelle]({{< relref "posts/relationale-datenbank" >}}), vous pouvez relier les informations contenues dans différents tableaux d'une base à l'aide de [liens]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}), d'[automatisations]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) et d'autres fonctions.

Un tableau est composé de lignes et de colonnes. Toutes les entrées d'une **ligne** forment un **ensemble de données** contigu. Les [types de colonnes]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}) de SeaTable définissent les **types de données** que vous pouvez saisir dans une **colonne**.

Chaque fois que vous consultez vos données dans un tableau, vous le faites via une [vue]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}). Les vues vous offrent d'innombrables options pour présenter différemment les données de vos tableaux – filtrer, trier, regrouper, masquer, etc.
