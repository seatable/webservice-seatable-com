---
title: 'Instructions pour le plugin de relations entre les tableaux'
date: 2024-07-29
lastmod: '2024-08-01'
categories:
    - 'plugins'
author: 'kgr'
url: '/fr/aide/guide-plugin-relations-tables'
aliases:
    - '/fr/aide/anleitung-zum-tabellenbeziehungen-plugin'
seo:
    title: 'Guide du plugin de relations entre tables SeaTable'
    description: 'Découvrez comment utiliser le plugin de relations entre tables dans SeaTable pour visualiser et gérer les liens dans vos bases.'

---

Surtout lorsque de nombreux tableaux avec des dizaines de colonnes se trouvent dans une base, on perd rapidement la vue d'ensemble de la manière dont ils sont reliés entre eux. Le plug-in Relations entre les tableaux permet de voir quels tableaux sont reliés entre eux et par quelles colonnes.

Pour savoir comment activer le plugin dans une base, [cliquez ici]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

![Plugin de relations entre les tableaux](images/Table-Relationships-Plugin.png)

## Fonctionnement du plugin

Lorsque vous avez configuré et ouvert le plug-in Relations entre les tableaux, vous voyez d'abord **tous les tableaux** qui se trouvent dans la base. Sous les noms de tableau en couleur sont listées **toutes les colonnes** qui ont été créées dans les tableaux respectives.

Pour visualiser les liens des tableaux, vous verrez non seulement **des lignes pleines** pour les liens _directs_ via les [colonnes de liens]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), mais aussi des **lignes en pointillés** pour les liens _indirects_ via les colonnes de formules de liens (par exemple [les lookups]({{< relref "help/base-editor/formeln/die-lookup-funktion" >}}).

## Gestion d'un diagramme de relations

Par défaut, un diagramme avec toutes les relations entre les tableaux est déjà créé lors de la première ouverture du plugin Relations entre les tableaux. Si vous souhaitez créer un autre diagramme de relations, cliquez sur {{< seatable-icon icon="dtable-icon-add-table" >}} **Ajouter un diagramme de relations**. Un champ de saisie s'ouvre alors, dans lequel vous tapez le **nom** souhaité.

![Options de gestion d'un diagramme de relations](images/table-relationship-plugin-management-options.png)

Lorsque vous passez le curseur de la souris sur le nom d'un diagramme, trois icônes apparaissent. Pour **modifier l'ordre des diagrammes**, maintenez le bouton gauche de la souris enfoncé sur la **zone de préhension** {{< seatable-icon icon="dtable-icon-drag" >}} et **glissez-déposez** un diagramme à l'endroit souhaité.

![Options d'un diagramme de relations](images/Options-of-Table-Relationship-Chart.png)

En outre, vous pouvez cliquer sur les **trois points** pour gérer le diagramme. Vous disposez des options suivantes :
- **renommer**
- **dupliquer**
- **supprimer**
- **réinitialiser**
- **exporter en tant qu'image**.

{{< warning  type="warning" headline="Remarque"  text="Si un seul diagramme est créé dans le plugin, vous ne pouvez **pas** le **supprimer**." />}}

## Paramètres d'un diagramme de relations

Les **paramètres**, auxquels vous accédez en cliquant sur l'**icône en forme de roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}}, vous permettent de définir les éléments suivants pour un diagramme en **(dés)activant** les **curseurs** :

- Souhaitez-vous afficher **les liens vers d'autres tableaux** (liens directs) ?
- Souhaitez-vous afficher **les liens au sein d'un tableau** (liens directs) ?
- Souhaitez-vous afficher **des formules pour les liens** (liens indirects) ? Si oui, quels types de formules de liens ?
- Souhaitez-vous afficher **toutes les colonnes indépendamment des vues** ?
- Souhaitez-vous afficher **des tableaux sans liens** ?
- Souhaitez-vous **afficher ou masquer des tableaux** ?

![Options de paramétrage d'un diagramme de relations](images/table-relationship-plugin-settings.png)

## Options d'apparence d'un diagramme de relations

Allez sur l'onglet **Apparence** en haut à droite à côté des paramètres pour modifier le style de certains éléments dans un diagramme. Cliquez sur la **flèche déroulante** devant un élément pour déplier les paramètres disponibles :

- **Tableaux** : couleur de l'en-tête du tableau et taille de police
- **Colonnes de liens** (liens directs) : largeur de ligne, style de ligne et couleur de ligne
- **Formules pour les liens** (liens indirects de premier niveau) : largeur de ligne, style de ligne et couleur de ligne
- **Formules à plusieurs niveaux pour les liens** (liens imbriqués de niveaux supérieurs, par exemple une formule de recherche qui obtient des valeurs via une autre colonne de liens du tableau lié) : largeur de ligne, style de ligne et couleur de ligne
- **Définir la couleur d'arrière-plan pour l'exportation**

![Options de design d'un diagramme de relations](images/table-relationship-plugin-theme.png)

## Déplacer des tableaux dans un diagramme

Vous pouvez **déplacer** les différents tableaux dans un diagramme à votre guise **par glisser-déposer**. Pour ce faire, maintenez le bouton gauche de la souris enfoncé, faites glisser le tableau à l'endroit souhaité et relâchez.

![Déplacer des tableaux dans un diagramme de relations par glisser-déposer](images/Move-tables-in-a-Table-Relationship-Chart.gif)

## Ajouter une note sur un diagramme de relations

Vous pouvez également ajouter une note sur un diagramme de relations en cliquant sur l'icône de la note dans le coin inférieur gauche. Vous disposez ensuite des options suivantes :

- modifier le texte
- masquer l'arrière-plan
- aligner le texte à gauche, au centre ou à droite
- supprimer la note

![Ajouter une note sur un diagramme de relations](images/add-note-on-table-relationship-chart.png)
