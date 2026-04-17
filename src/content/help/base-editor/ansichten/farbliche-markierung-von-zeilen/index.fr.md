---
title: 'Marquage des lignes par des couleurs'
date: 2022-11-16
lastmod: '2025-02-25'
categories:
    - 'ansichtsoptionen'
author: 'vge'
url: '/fr/aide/couleur-lignes-seatable'
aliases:
  - '/fr/aide/farbliche-markierung-von-zeilen'
seo:
    title: 'Couleur des lignes dans SeaTable : méthode & exemples'
    description: 'Colorez des lignes pour la gestion des statuts ou des doublons : sélection unique, règles personnalisées ou surbrillance automatique pour vos bases SeaTable.'
weight: 27
---

Le **marquage des lignes en couleur** sert à identifier rapidement certains enregistrements. Il ne faut pas confondre cela avec le [coloriage des cellules]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}}), qui permet de mettre en évidence certaines cellules.

## L'outil de couleurs de ligne

Dans les options de vue au-dessus d'un tableau, vous trouverez l'icône suivante :

![Outil de maculage coloré](images/Farbliche-Markierung-von-Zellen-1.png)

Après avoir cliqué sur l'outil de couleurs de ligne, vous pouvez choisir entre **trois options** pour le marquage en couleur :

- Utiliser une colonne de sélection unique
- Utiliser des règles
- Mettre en évidence les doublons

![Marquage couleur des cellules](images/Farbliche-Markierung-von-Zellen-2.png)

L'outil de couleurs de ligne est disponible non seulement dans les vues de tableau, mais aussi dans les [vues de calendrier]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}) et de [chronologie]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}). Cependant, pour ces dernières, vous ne pouvez utiliser que des colonnes de sélection unique pour définir la couleur des lignes.

## Utiliser une colonne de sélection unique

Pour l'option **Utiliser une colonne de sélection unique**, vous avez besoin d'une colonne de ce type dans votre tableau. Vous pouvez ainsi marquer chaque ligne en **début de ligne** avec la couleur de l'option correspondante inscrite dans cette colonne.

![Marquage couleur des cellules](images/Farbliche-Markierung-von-Zellen-3.png)

{{< warning  headline="Création d'une colonne de sélection unique" >}}

Apprenez [ici]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) comment créer de nouvelles colonnes de sélection unique.

{{< /warning >}}

## Utiliser des règles

L'option **Utiliser des règles** vous permet de définir des conditions pour le marquage en couleur.

- Cliquez sur le **symbole triangulaire à fond coloré**pour modifier la couleur du marqueur.
  ![Marquage couleur des cellules](images/Farbliche-Markierung-von-Zellen-5.png)
- Déterminez à laquelle de vos **Colonnes** la condition doit se référer.
  ![Marquage couleur des cellules](images/Farbliche-Markierung-von-Zellen-6.png)
- Optez pour la **Type de condition**.
  ![Marquage couleur des cellules](images/Farbliche-Markierung-von-Zellen-7.png)

{{< warning  headline="Sélection des types de conditions en fonction du type de colonne"  text="Veuillez noter que le type de colonne sélectionné détermine les options que vous pouvez choisir pour les conditions." />}}

### Utiliser un exemple de règle

Dans cet exemple, toutes les lignes d'un plan de rédaction qui sont cochées comme étant terminées dans la [colonne des cases à cocher]({{< relref "help/base-editor/spaltentypen/die-checkbox-spalte" >}}) doivent être marquées. Pour cela, la **colonne "Published"** a été sélectionnée, la condition **"est"** a été utilisée et il a été défini que les lignes marquées **d'une coche** doivent être sélectionnées.

![Marquage des lignes en couleur](images/Farbliche-Markierung-von-Zellen-9.png)

### Exemple de règle avec plusieurs conditions

Dans cet exemple, nous souhaitons mettre en couleur uniquement les lignes du plan éditorial lorsque le **statut** du post n'est pas "terminé", que la **date de publication** est dans le futur et qu'une **image** est déjà disponible.

![Règle avec plusieurs conditions pour le marquage des lignes en couleur](images/Regel-mit-mehreren-Bedingungen-fuer-die-farbliche-Zeilenmarkierung.png)

## Mettre en évidence les doublons

Vous pouvez mettre en couleur les lignes avec une ou plusieurs valeurs de colonne identiques à l'aide de l'option **Mettre en évidence les doublons**. Pour ce faire, sélectionnez la colonne dont vous souhaitez vérifier les doublons. Vous pouvez ainsi facilement identifier les doublons dans votre tableau et les corriger ou les supprimer le cas échéant.

![Mise en évidence des doublons de cellules par un marquage de couleur](images/Farbliche-Markierung-von-Zellen-9-1.png)
