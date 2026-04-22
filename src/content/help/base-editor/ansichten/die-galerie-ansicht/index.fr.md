---
title: 'La vue de galerie'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/fr/aide/vue-de-galerie'
aliases:
    - '/fr/aide/guide-plugin-galerie-seatable'
    - '/fr/aide/anleitung-zum-galerie-plugin'
    - '/fr/aide/ajouter-ligne-plugin-galerie'
    - '/fr/aide/eine-neue-zeile-ueber-das-galerie-plugin-hinzufuegen'
seo:
    title: 'Vue de galerie : affichage clair des images dans SeaTable'
    description: 'La vue galerie vous donne un aperçu vivant de tous les enregistrements contenant des images'
weight: 12
---

La vue **Galerie** utilise les fichiers d'une [colonne d'images]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) pour organiser les enregistrements de manière claire dans des tuiles. Plusieurs images sont ainsi regroupées dans un **album**. Cette présentation convient à de nombreux cas d'utilisation, par exemple [profils des employés]({{< relref "templates/human-resources/employee-directory" >}}), [bibliothèques de produits]({{< relref "templates/product-design/product-library" >}}), [listes d'inventaire]({{< relref "templates/operations/inventory-list" >}}) ou [la gestion des collections]({{< relref "templates/operations/art-gallery-management" >}}).

![La vue de la galerie](images/gallery-view.jpg)

## Pour créer une vue de galerie

1. Cliquez sur le **nom de la vue actuelle**.
2. Cliquez sur **Ajouter une vue ou un dossier** et sélectionnez le **type de vue** souhaité.

![Créer une vue de galerie](images/create-gallery-view.jpg)

3. Donnez un **nom** à la nouvelle vue.
4. Activez le curseur si vous souhaitez que la nouvelle vue ne soit pas visible par tous, mais **privée**.
5. Confirmez en cliquant sur **Envoyer**.
6. Déterminez ensuite dans les paramètres de quelle **colonne d'images** les images doivent provenir. La nouvelle vue est ensuite générée automatiquement.
7. Dans le champ **Titre**, indiquez la colonne dont vous souhaitez utiliser les entrées comme titre d'album.

![créer une vue de la galerie](images/create-gallery-view.gif)

## Options de vue

Vous pouvez utiliser les options suivantes dans une vue de galerie :
- [Verrouiller la vue]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrer]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [trier]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) 
- [Partager la vue]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Afficher ou masquer les informations

Dans les **paramètres de la galerie**, accessibles via **l'icône de la roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}}, vous pouvez afficher plus ou moins d'informations en affichant ou en masquant des colonnes. Activez les **régulateurs** de chaque colonne pour afficher plus d'informations à partir des enregistrements de la galerie.

![Afficher les informations des autres colonnes de la galerie](images/other-fields-shown-in-gallery-view.jpg)

## Plusieurs images dans un album

Le **nombre d'images** par album est affiché dans la galerie avec un **numéro surligné en gris**. Logiquement, ce nombre n'est affiché que lorsqu'il y a plus d'une image dans un album.

![nombre d'images en gris](images/image-number.jpg)

En cliquant sur l'image d'aperçu, vous ouvrez l'album en mode **plein écran**, dans lequel vous pouvez agrandir et réduire les images à l'aide des **loupes** et passer d'une image à l'autre à l'aide des **flèches**.

![mode plein écran dans le plugin de la galerie](images/gallery-image-preview.gif)

## Ajouter un nouvel enregistrement dans la vue de galerie

![Ajouter un nouveau jeu de données dans la vue galerie](images/add-new-record-in-gallery-view.jpg)

Cliquez sur le **cercle violet avec le symbole plus** dans le coin inférieur droit. Une nouvelle fenêtre s'ouvre. Créez un nouvel enregistrement dans les **détails de la ligne** et gérez les informations et les images souhaitées. Les modifications sont automatiquement enregistrées lorsque vous fermez la fenêtre.

## Modifier des enregistrements dans la vue de galerie

![modifier les enregistrements dans la vue galerie](images/modify-records-in-gallery-view.jpg)

Cliquez sur le **titre** d'un album et une fenêtre s'ouvre avec les **détails de la ligne**. Apportez les modifications souhaitées à l'enregistrement. Les modifications sont automatiquement enregistrées lorsque vous fermez la fenêtre.