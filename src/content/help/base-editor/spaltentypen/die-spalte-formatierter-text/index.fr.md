---
title: 'La colonne Texte mis en forme'
date: 2023-02-21
lastmod: '2023-11-08'
categories:
    - 'text-und-zahlen'
author: 'kgr'
url: '/fr/aide/colonne-texte-mis-en-forme'
aliases:
    - '/fr/aide/die-spalten-text-und-formatierter-text'
    - '/fr/aide/colonne-texte-ou-texte-formate-seatable'
seo:
    title: 'La colonne de texte mis en forme dans SeaTable'
    description: 'Utilisez la colonne Texte mis en forme pour saisir des textes structurés de toute longueur, avec retours à la ligne, listes, images et autres options de mise en forme.'
weight: 2
---

Pour la **saisie de textes structurés de toute longueur**, SeaTable met à votre disposition le type de colonne *Texte mis en forme*. Découvrez dans cet article quelles sont les différences avec la colonne de texte et dans quels cas il est judicieux de recourir à la colonne de texte mis en forme.

## Utilisation de la colonne de texte mis en forme

Contrairement à la colonne de texte, le type de colonne **Texte mis en forme** ne saisit pas des chaînes de caractères non structurées, mais des textes formatés comportant des retours à la ligne, des listes, des images, etc.

![La colonne Texte mis en forme](images/formatted-text-column.png)

Les colonnes de texte mis en forme sont particulièrement adaptées pour conserver **des textes plus longs**, par exemple des descriptions de produits, des listes de contrôle ou des posts de médias sociaux.

{{< warning  headline="UTF-8"  text="SeaTable prend en charge tous les caractères selon la norme UTF-8, car UTF-8 est l'encodage de caractères le plus répandu au monde pour Internet." />}}

Vous ne rédigez **pas** vos entrées directement dans la cellule, mais dans un **éditeur** accessible en un clic, qui offre différentes **options de formatage**. Ainsi, contrairement à la colonne de texte, vous pouvez également structurer des textes plus longs.

![Exemple d'utilisation d'une colonne de texte mis en forme](images/long-text-example.png)

Vous pouvez, entre autres, choisir un **format de paragraphe**, mettre la **police** en italique ou en gras et insérer **des liens**, des **citations**, des **listes**, des **tableaux** et **des images**.

{{< warning  type="warning" headline="Limite de caractères"  text="Pour les cellules individuelles de type Texte mis en forme, la limite est de 100.000 caractères. Cela correspond à environ 25 pages A4 de texte. La limite de caractères ne devrait donc avoir des répercussions sur votre travail que dans des cas exceptionnels." />}}

## Autres types de colonnes basées sur le texte

Si vous souhaitez saisir de **courtes chaînes de caractères sans mise en forme** (par exemple des noms, des mots de passe, des plaques d'immatriculation), il est préférable d'utiliser la [colonne de texte]({{< relref "help/base-editor/spaltentypen/die-text-spalte" >}}).

Outre la colonne de texte mis en forme, il existe dans SeaTable trois autres types de colonnes basées sur le texte pour des applications spécifiques :
- la [colonne e-mail]({{< relref "help/base-editor/spaltentypen/die-e-mail-spalte" >}})
- la [colonne URL]({{< relref "help/base-editor/spaltentypen/die-url-spalte" >}})
- la [colonne numéro de téléphone]({{< relref "help/base-editor/spaltentypen/die-telefonnummer-spalte" >}})

## Définir la valeur par défaut

Vous pouvez définir une [valeur par défaut]({{< relref "help/base-editor/spalten/standardwert-fuer-eine-spalte-festlegen" >}}) prédéfinie pour chaque colonne de texte mis en forme. Ce texte sera automatiquement inséré dans la cellule de chaque nouvelle ligne créée.

1. Cliquez sur la **flèche déroulante** à droite du nom de la colonne.
2. Allez sur **Définir la valeur par défaut**.
3. Lorsque vous cliquez sur **Modifier le texte**, l'éditeur s'ouvre et vous pouvez y rédiger le texte qui servira de valeur par défaut.

## Restrictions concernant les filtres, le tri et le regroupement

Il n'est pas possible de trier ou de regrouper les entrées d'un tableau selon des colonnes de texte mis en forme. Pour les filtres, vous disposez uniquement des options « est vide » et « n'est pas vide ».
