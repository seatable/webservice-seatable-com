---
title: "Étape 5 : Analyses à l'aide des liens"
date: 2024-08-30
lastmod: '2024-09-05'
categories:
    - 'online-kurs'
author: 'cdb'
url: '/fr/aide/etape-5-analyses-avec-liens'
aliases:
    - '/fr/aide/schritt-5-auswertungen-verknuepfungen'
seo:
    title: 'Étape 5 : analyses avec liens dans SeaTable'
    description: 'Maîtrisez les analyses statistiques dans SeaTable grâce aux liens entre tableaux et aux formules rollup pour des synthèses dynamiques.'

---

Les lignes des deux tableaux sont maintenant reliées, et ce lien fonctionne dans les deux sens. Ouvrez le tableau `Categories` : une nouvelle colonne y affiche les liens. Autrement dit, chaque dépense est reliée à une catégorie, et chaque catégorie peut être reliée à de nombreuses dépenses.

Jusqu'ici, ces liens ne vous ont pas encore apporté grand-chose. Cela va changer : ils permettent de réaliser des analyses statistiques en quelques secondes, par exemple de calculer le total des dépenses de la catégorie `Travel`.

## Augmenter la hauteur des lignes

Commencez par augmenter la hauteur des lignes du tableau `Categories`, pour voir davantage de liens. L'option `{{< seatable-icon icon="dtable-icon-row-height-default" >}}` se trouve dans la barre située au-dessus des noms de colonnes. Vous pouvez aussi élargir certaines colonnes pour en voir davantage.

![Vue de tableau avec hauteur de ligne ajustée pour mieux voir les liens](images/level1-row-height.png)

## Analyse des catégories

Ajoutez maintenant une colonne au tableau `Categories` :

> Nom : `Sum`
>
> Type de colonne : `{{< seatable-icon icon="dtable-icon-link-formulas" >}} Link formula`
>
> Formule utilisée : `rollup`
>
> Colonne de lien utilisée : `Expenses`
>
> Colonne utilisée pour le calcul : `{{< seatable-icon icon="dtable-icon-number" >}} Amount`
>
> Méthode de calcul : `Sum`

![Colonne de formule de lien « Sum » avec rollup pour additionner les montants liés](images/lvl1-rollup.png)

Réglez ensuite le format de la colonne `Sum` sur Euro, pour que les totaux s'affichent en euros.

## Un calcul mis à jour à chaque modification

Pratique, non ? La colonne `Sum` affiche en permanence le total des dépenses de chaque catégorie. Saisissez une nouvelle dépense dans le tableau `Expenses` : le total se met à jour aussitôt.

Et ce n'est qu'un début. Vous pourriez limiter le calcul à certaines années, ou ajouter d'autres conditions. Avec un peu plus d'expérience, vous créerez ce genre de rapport en quelques clics.

Cette étape est déjà terminée. Faites défiler la page jusqu'en bas et passez à la sixième et avant-dernière étape du cours.

{{< warning  headline="Des analyses statistiques comme un pro"  text="SeaTable offre bien d'autres façons d'analyser vos données. Le deuxième cours en ligne reviendra plus en détail sur le sujet." />}}

## Article d'aide avec plus d'informations

- [Ajuster la hauteur des lignes]({{< relref "help/base-editor/ansichten/zeilenhoehe-anpassen" >}})
- [La formule du rollup]({{< relref "help/base-editor/formeln/die-rollup-formel" >}})
