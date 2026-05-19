---
title: 'La formule du rollup'
date: 2023-01-24
lastmod: '2023-01-24'
categories:
    - 'verknuepfungen'
author: 'vge'
url: '/fr/aide/formule-rollup-seatable'
aliases:
    - '/fr/aide/die-rollup-formel'
seo:
    title: 'Formule rollup SeaTable : lier et agréger des données'
    description: 'Agrégez les valeurs liées : total, moyenne, minimum, maximum ou concaténation de données reliées, réglages de formats et multiples relations.'
---

À l'aide de la formule de rollup du type de colonne **Formule pour les relations**, vous pouvez établir un rapport entre plusieurs valeurs numériques d'une colonne liée et effectuer des calculs statistiques simples.

## Champ d'application de la formule du rollup

La **formule du rollup** permet de déterminer des relations entre des valeurs numériques. Par exemple, lors de la planification budgétaire, vous pouvez **additionner** les dépenses d'une catégorie, calculer la **valeur** **maximale** ou **minimale** dépensée ou encore la **moyenne**.

Vous avez d'abord besoin d'une colonne de type [Lien vers d'autres entrées]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Assurez-vous que l'option **Autoriser les liens vers plusieurs lignes** est activée, car c'est la seule façon de déterminer les relations entre les nombres.

![La formule du rollup](images/rollup-1.png)

La colonne **Formule de lien** affiche ensuite la relation sélectionnée entre les valeurs numériques dans la colonne de lien à l'aide de la formule de rollup. Dans cet exemple, nous avons choisi la méthode d'évaluation **Somme**:

![La formule du rollup](images/rollup-2-1.png)

## Ajouter un lien de tableau

Consultez l'[article de la colonne des liens]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) pour savoir comment créer une colonne de type **Lien vers d'autres entrées**. C'est une condition de base pour pouvoir utiliser la formule de rollup.

L'utilisation de la formule de rollup n'a de sens que si vous activez l'option **Autoriser la liaison à plusieurs lignes** lors de la création d'une colonne de lien. Si cette option était désactivée, le champ de la formule de rollup contiendrait toujours la même valeur de la colonne de jointure.

## Créer une colonne avec la formule de rollup

![La formule du rollup.](images/rollup-Formel.gif)

1. Créez une nouvelle colonne de type **Formule pour les liens**.
2. Définissez l'option **Rollup** comme formule.
3. Sélectionnez la **colonne de lien** qui renvoie au tableau souhaité.
4. Décidez maintenant, dans le champ **Sélectionner la colonne à résumer dans le tableau lié**, quelle colonne du tableau vous souhaitez lier et évaluer.
5. Définissez la **méthode d'évaluation**. Vous avez le choix entre moyenne, minimum, maximum, somme et concaténation.
6. Cliquez sur **Envoyer**.

## Paramètres de format

Vous pouvez définir précisément le **format** dans lequel les valeurs numériques seront affichées. Pour ce faire, cliquez sur l'**icône** triangulaire **déroulante** de la colonne "Formule pour les raccourcis" et sélectionnez l'option **Paramètres de format**. Outre les chiffres, vous pouvez également prendre comme format **les devises**, les **pourcentages** et **les durées**.
