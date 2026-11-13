---
title: 'La formule du rollup'
date: 2023-01-24
lastmod: '2026-11-12'
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

À l'aide de la formule de rollup du type de colonne **Formule pour les liens**, vous pouvez établir un rapport entre plusieurs valeurs numériques d'une colonne liée et effectuer des calculs statistiques simples.

## Champ d'application de la formule du rollup

La **formule du rollup** permet de déterminer des relations entre des valeurs numériques. Par exemple, lors de la [planification budgétaire]({{< relref "templates/finance/budget-plan" >}}), vous pouvez **additionner** les dépenses d'une catégorie, calculer la **valeur** **maximale** ou **minimale** dépensée ou encore la **moyenne**.

Vous avez d'abord besoin d'une colonne de type [Lien vers d'autres entrées]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}). Assurez-vous que l'option **Limiter les liens à une ligne maximum** est désactivée, car c'est la seule façon de lier plusieurs lignes.

La colonne [Formule pour les liens]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen" >}}) affiche ensuite la relation sélectionnée entre les valeurs numériques dans la colonne de lien à l'aide de la formule de rollup. Dans cet exemple, nous avons choisi la méthode d'évaluation **Somme** :

![La formule du rollup](images/rollup-formel.png)

## Créer une colonne avec la formule de rollup

Consultez l'[article de la colonne des liens]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) pour savoir comment créer une colonne de type **Lien vers d'autres entrées**. C'est une condition de base pour pouvoir utiliser la formule de rollup.

{{< warning headline="Plusieurs lignes liées nécessaires" >}}

L'utilisation de la formule de rollup n'a de sens que si l'option **Limiter les liens à une ligne maximum** est désactivée dans les paramètres d'une colonne de liens. Si cette option était activée, la formule de rollup afficherait toujours la même valeur que celle de l'unique ligne liée.

{{< /warning >}}

![La formule du rollup](images/rollup-formel.gif)

1. Créez une nouvelle colonne de type **Formule pour les liens**.
2. Définissez l'option **Rollup** comme formule.
3. Sélectionnez la **colonne de lien** qui renvoie au tableau souhaité.
4. Décidez maintenant, dans le champ **Sélectionner la colonne à résumer dans le tableau lié**, quelle colonne du tableau vous souhaitez lier et évaluer.
5. Définissez la **méthode d'évaluation**. Vous avez le choix entre moyenne, minimum, maximum, somme et concaténation.
6. Cliquez sur **Envoyer**.

## Paramètres de format

Vous pouvez définir précisément le **format** dans lequel les valeurs numériques seront affichées. Pour ce faire, cliquez sur l'**icône déroulante** triangulaire de la colonne rollup et sélectionnez l'option **Paramètres de format**. Outre les nombres, vous pouvez également choisir comme format les **devises**, les **pourcentages** et les **durées**. Vous pouvez en outre définir les **séparateurs décimaux et de milliers** ainsi que le nombre de **décimales**.

## Modifications ultérieures

Vous pouvez bien sûr modifier la formule de rollup ultérieurement, par exemple remplacer la méthode d'évaluation Somme par Moyenne. Cliquez sur l'**icône déroulante** triangulaire à droite du nom de la colonne, puis sur **Personnaliser le type de colonne**. Vous accédez alors aux mêmes paramètres que lors de la création de la colonne.
