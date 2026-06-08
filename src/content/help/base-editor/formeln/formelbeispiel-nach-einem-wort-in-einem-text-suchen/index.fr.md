---
title: 'Exemple de formule : Rechercher un mot dans un texte'
date: 2023-01-28
lastmod: '2023-09-19'
categories:
    - 'formeln'
author: 'nsc2'
url: '/fr/aide/exemple-formule-recherche-mot-texte'
aliases:
    - '/fr/aide/formelbeispiel-nach-einem-wort-in-einem-text-suchen'
seo:
    title: 'Exemple de formule SeaTable : rechercher et signaler des mots dans un texte'
    description: 'Découvrez comment rechercher des mots dans les colonnes texte avec une formule SeaTable, signaler les trouvailles et automatiser vos analyses de contenu.'
---

Les formules de SeaTable vous offrent différentes possibilités de travailler avec les données de vos tableaux. Une possibilité est la **recherche de mots dans un texte**. En saisissant une formule correspondante, vous pouvez rechercher automatiquement n'importe quel mot [dans une colonne de texte]({{< relref "help/base-editor/spaltentypen/die-spalte-formatierter-text" >}}) et faire écrire une note - par exemple "mot trouvé/non trouvé" - comme résultat dans une colonne de formule de votre tableau.

## Rechercher un mot dans un texte

Dans l'exemple concret, l'objectif est de rechercher un **mot** dans la colonne de texte **"Request"** à l'aide d'une formule.

![Exemple de tableau pour la recherche de mots dans un texte à l'aide d'une formule ](images/example-table-search-words-in-text.png)

Pour cela, vous ajoutez d'abord une **colonne de formule** au tableau, dans l'éditeur de laquelle vous pouvez ensuite insérer la **formule**.

![Saisir la formule dans la zone de texte prévue à cet effet](images/input-formula-example-text.jpg)

Pour rechercher un mot dans une colonne de texte, ajoutez d'abord à la formule un **opérateur If**, que vous trouverez dans l'éditeur de formules sous l'onglet **Fonctions logiques**. Il examine si une **condition** définie s'applique ou non et renvoie une certaine **valeur** en fonction du résultat positif ou négatif.

![Ajout de la fonction "if" à la formule.](images/add-if-to-formular.jpg)

L'étape suivante consiste à ajouter à la formule la fonction **find**, qui permet de rechercher un mot spécifique dans la colonne de texte. Vous trouverez cette fonction dans l'éditeur de formules, sous les **fonctions de texte**.

![Ajout de la fonction de texte "find" à la formule](images/add-find-to-formula.jpg)

Après les deux fonctions, la formule contient le **mot spécifique** que vous souhaitez rechercher dans la colonne de texte. Écrivez le mot entre **guillemets** dans la formule.

![Ajouter le mot que vous recherchez dans la colonne de texte](images/add-the-word-searching-for.jpg)

L'élément suivant de la formule est le **nom de la colonne** dont la présence du mot recherché doit être vérifiée. Il est particulièrement important que le nom de la colonne soit entouré d'**accolades**, sinon SeaTable ne pourra **pas** identifier le texte à vérifier à l'aide de la formule.

{{< warning  headline="Conseil"  text="Les **noms de colonne** dans le tableau sont affichés à gauche dans l'**éditeur de formule** et peuvent être insérés dans la formule par un **double-clic**." />}}

![Ajouter le nom de la colonne dont la présence du mot recherché doit être vérifiée.](images/add-reference-column.jpg)

Après le nom de la colonne, insérez l'équation mathématique `1 > 0`. Celle-ci est importante pour la formule, car elle indique qu'une **valeur** spécifique est renvoyée dès que le mot recherché est trouvé **au moins une fois** dans la colonne de texte. Dans la formule, veillez à **fermer** la parenthèse **après** le premier chiffre. Les **caractères de comparaison** ( > , < , = , etc.) se trouvent dans l'éditeur de formules sous **Opérateurs**.

![Ajouter l'équation mathématique pour compléter la condition](images/add-.jpg)

Pour finir, vous définissez dans la formule les **valeurs** qui vous sont renvoyées dans la colonne de formule lorsque le mot recherché a été **trouvé** ou **non** dans le texte. La **première** valeur saisie apparaît toujours dans la colonne de formule si le mot recherché a été **trouvé** dans le texte, la deuxième valeur dans le cas contraire. Placez toujours les valeurs entre **guillemets** et séparez-les par une **virgule**.

![Ajouter les valeurs renvoyées en cas de présence ou d'absence du mot recherché dans la colonne de formule  ](images/add-values.jpg)

Avant de confirmer, il faut encore noter que vous devez **fermer** la **parenthèse** pour que la formule soit acceptée comme valable.

![Terminer la formule en fermant la parenthèse](images/finish-formula.jpg)

Après avoir confirmé la formule saisie, vous pouvez voir si le mot recherché a été trouvé dans la colonne de texte en fonction de la valeur indiquée dans la colonne de **formule**.

![Le résultat de la formule apparaît automatiquement dans la colonne des formules après confirmation de la formule.](images/table-after-formular-search-word.png)
