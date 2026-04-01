---
title: 'La vue arborescente'
date: 2026-04-01
lastmod: '2026-04-01'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/fr/aide/la-vue-arborescente'
seo:
    title: 'Vue arborescente : afficher la hiérarchie des enregistrements liés'
    description: 'Utilisez la vue arborescente de SeaTable pour visualiser la hiérarchie des enregistrements liés et présenter des données complexes de manière structurée.'
weight: 16
---

La vue **Arbre** permet une **représentation hiérarchique** compacte des enregistrements liés. Cela signifie que vous pouvez visualiser les données qui se trouvent dans différentes **tables liées** à différents niveaux dans un diagramme en arborescence. Cette vue offre une vue d'ensemble structurée, en particulier pour les grandes quantités de données telles que les données financières ou les données de projet.

![la vue en arborescence](images/tree-view.png)

{{< warning type="warning" headline="Conditions" >}}

Pour que la vue arborescente soit utile, vous devez disposer d'une base avec **au moins deux tables** reliées entre elles par une [colonne de liens]({{< relref "help/base-editor/tabellen/wie-man-tabellen-in-seatable-miteinander-verknuepft" >}}).

{{< /warning >}}

## Fonctionnement de la vue arborescente

Avant de créer une vue arborescente, vous devez réfléchir à la **arborescence** (c'est-à-dire la hiérarchie d'enregistrements liés dans votre base) qui a du sens : Par exemple, pour un [portefeuille de projets]({{< relref "templates/projects/project-portfolio" >}}), cela pourrait être les départements au premier niveau, les projets au deuxième niveau et les tâches au troisième niveau. En conséquence, les départements, les projets et les tâches doivent être saisis dans trois tables différentes, qui sont liées entre elles. Chaque tâche est associée à un projet, qui est lui-même subordonné à un service.

![exemple d'arborescence](images/example-for-tree-view.png)

Vous définissez comment les enregistrements dépendent les uns des autres ou quelles tables se trouvent à quel niveau à l'aide des **niveaux**. Actuellement, vous pouvez afficher jusqu'à trois niveaux dans l'arborescence, c'est-à-dire les données de trois tables.

## Comment créer une vue arborescente

1. Cliquez sur le **nom de la vue actuelle**.
2. Cliquez sur **Ajouter une vue ou un dossier** et choisissez le **type de vue** souhaité.

![Créer une vue arborescente](images/create-tree-view.png)

3. Donnez un **nom** à la nouvelle vue.
4. Activez le curseur si vous souhaitez que la nouvelle vue ne soit pas visible par tous, mais **privée**.
5. Confirmez en cliquant sur **Envoyer**.

![nommer la vue arborescente](images/name-tree-view.png)

6. Cliquez sur l'icône de **roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}} dans le coin supérieur droit et ajustez les **paramètres**.
7. Déterminez quel **tableau** doit être affiché à chaque niveau. Pour cela, cliquez dans le champ pour **Niveau 2** et **Niveau 3** pour sélectionner le tableau souhaité dans la liste déroulante. **Niveau 1** est toujours occupé par la table dans laquelle se trouve la vue.

![Définir la hiérarchie dans la vue arborescente](images/tree-view-settings.jpg)

Les enregistrements liés aux deuxième et troisième niveaux du graphique en arborescence sont ensuite regroupés sous leurs enregistrements parents respectifs.

## Afficher ou masquer les informations

Les **paramètres**, accessibles en cliquant sur l'icône de **roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}}, vous permettent de définir les colonnes visibles pour chaque niveau de l'arborescence. Pour ce faire, sélectionnez d'abord le **niveau** sur lequel vous souhaitez afficher ou masquer des colonnes. Si vous désactivez ensuite les **règles** correspondantes sur le bord droit, les colonnes ne seront pas visibles dans le diagramme en arbre.

![masquer ou déplacer des colonnes dans l'arborescence](images/hide-and-move-columns-in-tree-view.png)

### Déplacer des colonnes

De plus, à chaque niveau, vous avez la possibilité d'organiser les colonnes différemment que dans la vue tableau. Pour cela, maintenez le bouton gauche de la souris enfoncé sur la **zone de préhension à six points** devant le nom de la colonne et déplacez la colonne **par glisser-déposer** à l'endroit souhaité.

## Options de vue

Vous pouvez utiliser les options suivantes dans une vue arborescente :
- [Verrouiller la vue]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrer]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [trier]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) 
- **Réduire tout** ou **Déployer tout**

## Déployer et réduire les enregistrements liés

Pour réduire tous les enregistrements liés sous une entrée, cliquez sur la **flèche déroulante** à gauche de la ligne. Pour déployer à nouveau les enregistrements, procédez de la même manière.

![réduire les enregistrements dans l'arborescence](images/collapse-records-in-tree-view.gif)

## Ajuster la largeur des colonnes

Pour éviter les entrées tronquées ou les grands espaces entre les valeurs, vous pouvez à votre guise **ajuster la largeur des colonnes**. Pour ce faire, maintenez le bouton gauche de la souris enfoncé sur la ligne de démarcation entre deux colonnes et faites glisser le curseur vers la gauche ou la droite.

![ajuster la largeur des colonnes dans l'arborescence](images/adjust-column-width-in-tree-view.gif)

## Ajouter et modifier des enregistrements dans la vue arborescente

Pour ajouter un nouvel enregistrement au premier niveau de la vue arborescente, cliquez sur le **cercle orange avec l'icône +** dans le coin inférieur droit. Les **Détails de la ligne** s'ouvrent alors. Remplissez-les comme vous le souhaitez et fermez la fenêtre pour enregistrer l'enregistrement.

Pour ajouter un nouvel enregistrement au deuxième ou au troisième niveau de la vue arborescente, cliquez sur **\+ Ajouter un enregistrement**. La ligne créée est automatiquement liée à l'enregistrement de niveau supérieur et regroupée en conséquence. Vous pouvez remplir les autres champs directement dans la ligne.

![ajouter et modifier des enregistrements dans la vue arborescente](images/add-record-in-tree-view.png)

De même, les enregistrements existants peuvent être modifiés directement dans la vue arborescente. De plus, en cliquant sur **Afficher**, vous pouvez ouvrir les détails de la ligne et effectuer des modifications.

![ajouter et modifier des enregistrements dans la vue arborescente](images/expand-record-in-tree-view.png)

Bien entendu, les données sont également enregistrées dans les tables sous-jacentes.