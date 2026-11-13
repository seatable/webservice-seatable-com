---
title: 'La formule Findmin'
date: 2023-02-13
lastmod: '2026-11-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/fr/aide/formule-findmin'
aliases:
    - '/fr/aide/die-findmin-formel'
seo:
    title: 'Formule Findmin SeaTable – trouver la plus petite valeur liée'
    description: 'Découvrez comment utiliser la formule Findmin pour obtenir la plus petite valeur issue d’enregistrements liés dans SeaTable.'
---

La **formule Findmin** recherche la **valeur minimale** parmi les entrées de la colonne liée et l'affiche. Cela est utile lorsqu'il y a **plusieurs entrées** dans le tableau lié qui se réfèrent au même enregistrement (par exemple d'une personne ou d'une catégorie) dans un autre tableau.

## À quoi sert la formule Findmin ?

Vous pouvez utiliser la formule Findmin pour toutes les valeurs alphanumériques afin de déterminer la **valeur minimale**. Supposons que vous utilisiez SeaTable pour la [planification budgétaire]({{< relref "templates/finance/budget-plan" >}}), avec un tableau contenant les dépenses et un autre contenant les catégories. Vous pouvez alors lier chaque dépense à une catégorie. Pour savoir quelle a été **la dépense la plus faible par catégorie**, vous pouvez utiliser la **formule Findmin** pour afficher la plus petite valeur parmi toutes les dépenses liées.

![Formule findmin](images/findmin.png)

## Comment utiliser la formule Findmin ?

### Ajouter un lien de tableau

Consultez l'article de la [colonne des liens]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) pour savoir comment créer une colonne de type **lien vers d'autres entrées**. C'est une condition de base pour pouvoir utiliser la formule Findmin.

{{< warning headline="Plusieurs lignes liées nécessaires" >}}

L'utilisation de la formule Findmin n'a de sens que si l'option **Limiter les liens à une ligne maximum** est désactivée dans les paramètres d'une colonne de liens. Si cette option était activée, la formule Findmin afficherait toujours la même valeur que celle de l'unique ligne liée.

{{< /warning >}}

### Ajouter une colonne avec la formule Findmin

![Formule findmin](images/findmin.gif)

1. Créez une nouvelle colonne de type **Formule pour les liens**.
2. Définissez l'option **Findmin** comme formule.
3. Sélectionnez la colonne précédemment créée du type **Lien vers d'autres entrées** de ce tableau.
4. Définissez maintenant la **colonne de référence dans le tableau lié** dont l'enregistrement ayant la valeur minimale doit s'afficher dans la colonne Findmin.
5. Sélectionnez la **colonne de comparaison dans le tableau lié** dans laquelle vous souhaitez déterminer la valeur minimale.
6. Cliquez sur **Envoyer**.
