---
title: 'La formule Findmin'
date: 2023-02-13
lastmod: '2023-02-13'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/fr/aide/formule-findmin'
aliases:
    - '/fr/aide/die-findmin-formel'
seo:
    title: 'Formule Findmin SeaTable – trouver la valeur minimale'
    description: 'Découvrez comment utiliser la formule Findmin pour obtenir la plus petite valeur issue d’enregistrements liés dans SeaTable.'
---

La **formule Findmin** recherche parmi les entrées d'une colonne liée la **valeur minimale** et l'affiche. Ceci est utile lorsqu'il y a **plusieurs entrées** dans le tableau lié qui se réfèrent au même enregistrement (par ex. d'une personne) dans un autre tableau.

La formule Findmin fonctionne uniquement avec **des valeurs numériques**, c'est pourquoi le contenu de la colonne liée doit également être constitué de valeurs numériques. De plus, l'utilisation de la formule Findmin n'a de sens que si le curseur **Autoriser la liaison à plusieurs lignes** est activé lors de la création de la colonne **Lien vers d'autres entrées**. Si cette option était désactivée, la formule Findmin contiendrait toujours le même nombre que celui de la colonne liée.

## Pourquoi utiliser la formule Findmin ?

La **fonction Findmin** doit être utilisée lorsque vous souhaitez **faire des références croisées** à des valeurs numériques stockées dans différents tableaux. Supposons que vous utilisiez SeaTable pour collecter les **heures de travail** de vos employés, un tableau contenant les employés et une autre l'activité quotidienne. Vous pouvez alors lier chaque enregistrement d'employé aux heures de travail enregistrées.

![Formule findmin](images/findmax-1.png)

Pour savoir quand un employé s'est connecté pour la première fois, vous pouvez utiliser la **formule Findmin** pour afficher dans une colonne la **plus petite valeur** - dans ce cas, la première connexion - parmi toutes les heures de connexion.

![Formule findmin](images/findmin.png)

Vous pouvez utiliser la formule Findmin pour toutes les valeurs numériques afin de représenter la **valeur minimale**.

## Comment utiliser la formule Findmin

### Ajouter un lien de tableau

Consultez l'article de la [colonne des liens]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) pour savoir comment créer une colonne de type **lien vers d'autres entrées**. C'est une condition de base pour pouvoir utiliser la formule Findmin.

### Ajouter une colonne avec la formule Findmin

![Formule findmin](images/findmin.gif)

1. Créez une nouvelle colonne de type **Formule pour les liens**.
2. Définissez l'option **Findmin** comme formule.
3. Sélectionnez la colonne précédemment créée du type **Lien vers d'autres entrées** de ce tableau.
4. Dans le champ **Sélectionner une colonne de référence dans le tableau lié "..."**, définissez la colonne de l' que vous souhaitez lier à cette colonne.
5. Cliquez sur **Envoyer**.

{{< warning  headline="Attention"  text="La formule Findmin fonctionne uniquement avec **des valeurs numériques**La colonne liée doit donc contenir des valeurs numériques." />}}
