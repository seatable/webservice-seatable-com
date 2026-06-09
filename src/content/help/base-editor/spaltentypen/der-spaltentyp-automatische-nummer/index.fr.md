---
title: 'Le type de colonne Numéro automatique'
date: 2023-01-07
lastmod: '2023-02-10'
categories:
    - 'text-und-zahlen'
author: 'ssc'
url: '/fr/aide/colonne-numerotation-automatique'
aliases:
    - '/fr/aide/der-spaltentyp-automatische-nummer'
seo:
    title: 'Type de colonne Numérotation automatique – SeaTable'
    description: 'Gérez des identifiants uniques avec la colonne Numérotation auto de SeaTable : formats, remise à zéro et astuces pour éviter les doublons.'
weight: 24
---

Le type de colonne **Numéro automatique** génère automatiquement un numéro croissant pour chaque nouvelle ligne. Ce type de colonne est toujours utilisé lorsque vous avez besoin d'un identifiant unique pour chaque enregistrement.

Notez que cette colonne **n'est pas** destinée à compter le nombre d'enregistrements dans un tableau. Si vous [supprimez une ligne]({{< relref "help/base-editor/zeilen/das-loeschen-von-zeilen" >}}), les enregistrements restants **ne sont pas renumérotés**. Cela peut entraîner **des lacunes** dans la numérotation.

Pour **renuméroter** vos enregistrements (par exemple pour éliminer des lacunes), vous pouvez soit supprimer la colonne _Numéro automatique_ et la recréer, soit modifier le type de colonne, puis la transformer à nouveau en _Numéro automatique_.

![Lignes avec un numéro automatique](images/auto-number.gif)

## Trois formats sont disponibles

Lorsque vous créez la colonne _Numéro automatique_, vous déterminez le **format** que doivent prendre les valeurs de cette colonne. Vous pouvez choisir un **nombre** avec un certain nombre de chiffres et faire précéder ce numéro d'une **chaîne** de lettres ou de chiffres (par exemple la **date** du jour).

![SeaTable Possibilités formelles pour la colonne des numéros automatiques](images/Formatmoeglichkeiten-spalten.png)

## Questions fréquentes

Même si le type de colonne _Numéro automatique_ semble relativement simple, il y a quelques particularités dont il faut tenir compte.

{{< faq "Est-il possible d'influencer la prochaine valeur utilisée ?" >}}Oui, la colonne offre la possibilité, dans les options de colonne, de **réinitialiser** le **numéro automatique** à une certaine valeur, qui sera ensuite attribuée à la ligne suivante.
{{< /faq >}}
{{< faq "Les valeurs peuvent-elles apparaître deux fois dans la colonne ?" >}}Oui, cela peut arriver. Si tu réinitialises le numéro automatique, des valeurs peuvent aussi apparaître en double. Les valeurs de cette colonne ne sont donc pas uniques.
{{< /faq >}}
{{< faq "La colonne peut-elle ne contenir que des valeurs uniques ?" >}}Oui. Si vous utilisez un abonnement Plus ou Enterprise de SeaTable, vous pouvez **verrouiller** la **colonne pour qu'elle ne puisse pas être modifiée**. Ainsi, personne ne peut réinitialiser le numéro et chaque valeur reste unique.

{{< /faq >}}
