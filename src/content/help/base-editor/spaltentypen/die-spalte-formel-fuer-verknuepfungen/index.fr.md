---
title: 'La colonne Formule pour les liens'
date: 2025-07-18
lastmod: '2025-07-18'
categories:
    - 'formeln'
author: 'kgr'
url: '/fr/aide/colonne-formule-de-liens'
aliases:
    - '/fr/aide/die-spalte-formel-fuer-verknuepfungen'
seo:
    title: 'Colonne formule de liens dans SeaTable'
    description: 'Découvrez comment utiliser la colonne de formule de liens dans SeaTable pour relier et analyser vos données entre tables.'

---

Une formule pour les liens vous permet **d'afficher, de fusionner ou de mettre en relation des données de tableaux liés** dans votre tableau actuel. C'est là que SeaTable fait valoir ses avantages en tant que [base de données relationnelle]({{< relref "posts/relationale-datenbank" >}}).

Pour le type de colonne, vous disposez au total de **cinq formules différentes**. La condition préalable à l'utilisation de la colonne est la présence d'au moins une colonne de type [lien vers d'autres entrées]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}) dans votre table.

## Création d'une colonne de formule pour les liens

Pour appliquer une formule, vous devez d'abord ajouter une nouvelle colonne de formule pour les liens à votre tableau.

![Sélection d'une formule pour les liens](images/add-a-link-formula.png)

1. Cliquez sur l'icône **Plus** à droite de la dernière colonne.
2. Donnez un **nom** à la colonne.
3. Sélectionnez **Formule pour les liens** comme type de colonne.
4. Choisissez une **formule** (par exemple, un rollup).
5. Sélectionnez la **colonne de lien** du tableau dont vous souhaitez utiliser les données.
6. Indiquez la **colonne du tableau lié** à laquelle la formule doit se référer.
7. Selon la formule choisie, vous pouvez effectuer **d'autres réglages**.
8. Créez la colonne en cliquant sur **Envoyer**.

## 5 Formules pour les liens

Vous trouverez plus d'informations et des exemples sur les cinq différentes formules dans les articles suivants, qui illustrent l'utilité et l'utilisation des formules :
- [Lookup]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}})
- [Countlinks]({{< relref "help/base-editor/formeln/die-countlinks-formel" >}})
- [Rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}})
- [Findmax]({{< relref "help/base-editor/formeln/die-findmax-formel" >}})
- [Findmin]({{< relref "help/base-editor/formeln/die-findmin-formel" >}})

## Mise en forme des résultats

Chaque formule de SeaTable a pour résultat un **nombre**, une **date** ou un **texte/string**. Les résultats dans une colonne de formule pour les liens se voient automatiquement attribuer un **format** spécifique. Si vous n'êtes pas satisfait de ce format, vous pouvez le **re-détecter**. Pour ce faire, cliquez sur la **flèche déroulante** à droite du nom de la colonne, puis sur **Modifier les paramètres de format**.

![Mise en forme des résultats de formules](images/format-settings-of-the-link-formula-column.png)

Pour les colonnes Countlinks et Rollup, vous disposez également de différents **paramètres de format pour les nombres** : Pourcentage, Devises ou Durée, ainsi que Séparateur de décimales, Séparateur de milliers et Chiffres après la virgule.