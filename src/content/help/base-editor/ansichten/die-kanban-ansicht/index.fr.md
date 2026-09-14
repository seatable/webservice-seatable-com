---
title: 'La vue Kanban'
date: 2025-12-03
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/fr/aide/la-vue-kanban'
aliases:
    - '/fr/aide/tutoriel-plugin-kanban'
    - '/fr/aide/anleitung-zum-kanban-plugin'
seo:
    title: 'Créer et utiliser la vue Kanban dans SeaTable'
    description: "Apprenez à configurer la vue Kanban dans SeaTable et à l'utiliser au mieux pour visualiser les processus."
weight: 14
---

Une **vue Kanban** est prédestinée à la représentation de processus dynamiques avec différentes phases. Dans ce sens, elle vous permet par exemple de visualiser les **flux de travail** et les **avancées des projets**. Elle est particulièrement utile pour la [planification de projet]({{< relref "templates/projects/project-plan" >}}), le [développement de logiciel]({{< relref "templates/it-engineering/bug-tracker" >}}) ou la répartition des tâches au sein d'une équipe.

{{< warning type="warning" headline="Conditions préalables" >}}

Pour pouvoir utiliser la vue Kanban de manière judicieuse, vous avez besoin d'au moins une colonne dans votre tableau qui permette une affectation claire des options. Par exemple, les types de colonnes [Sélection unique]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) ou [Collaborateur]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) conviennent pour cela.

{{< /warning >}}

**Dans cette vidéo tutoriel, nous allons vous montrer en quelques minutes seulement comment créer une vue Kanban dans SeaTable (avec des sous-titres en français).**
{{< youtube C19DWHZzTbg >}}

## Construction d'une vue Kanban

Une vue Kanban est composée de **colonnes** qui représentent différentes étapes ou phases dans un processus. Dans le cas d'un workflow, il peut s'agir par exemple de "idée", "planifié", "en cours" et "terminé".

![Vue Kanban](images/kanban-view.jpg)

Vous munissez les colonnes de **cartes mobiles** que vous pouvez **déplacer** aussi bien à l'intérieur d'une colonne que d'une colonne à l'autre. Une carte Kanban peut par exemple représenter un lot de travaux ou une tâche.

![Déplacements Kanban](images/move-records-in-kanban-view.gif)

## Pour créer une vue Kanban

![Créer une vue Kanban](images/create-kanban-view.jpg)

1. Cliquez sur le **nom de la vue actuelle**.
2. Cliquez sur **Ajouter une vue ou un dossier** et sélectionnez le **type de vue** souhaité.

![nommer une vue Kanban](images/name-kanban-view.jpg)

3. Donnez un **nom** à la nouvelle vue.
4. Activez le curseur si vous souhaitez que la nouvelle vue ne soit pas visible par tous, mais **privée**.
5. Confirmez en cliquant sur **Envoyer**.

![Regrouper une vue Kanban](images/group-kanban-view.jpg)

6. Cliquez sur **Ajouter un regroupement** et définissez la **colonne** que vous souhaitez utiliser pour le regroupement, c'est-à-dire la définition des colonnes. La vue Kanban est ensuite générée automatiquement.

![Paramétrer une vue Kanban](images/kanban-view-settings.jpg)

7. Allez dans les **paramètres** et indiquez dans le champ **Titre** la colonne avec laquelle vous souhaitez étiqueter les cartes Kanban.
8. Vous pouvez également activer des **régulateurs** pour activer certaines fonctions.

Si vous souhaitez modifier quelque chose ultérieurement, cliquez sur **l'icône de la roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}} dans le coin supérieur droit et ajustez les paramètres.

## Paramètres de la vue Kanban

Les options du curseur vous permettent de modifier la représentation visuelle de la vue Kanban.

- Le curseur **Ne pas afficher les valeurs vides** vous permet de supprimer les espaces réservés grisés sur les cartes Kanban.
- Le curseur **Afficher les noms des colonnes** affiche les noms des colonnes au-dessus de toutes les informations activées.
- Le curseur **Rompre le texte** formate les textes de manière à ce qu'ils soient entièrement lisibles sur les cartes du tableau Kanban.

![Paramètres de la vue Kanban](images/show-other-fields-in-kanban-view.gif)

## Options de vue

Vous pouvez utiliser les options suivantes dans une vue Kanban :
- [Verrouiller la vue]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrer]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [trier]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) selon n'importe quelle valeur
- [Regrouper]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}}) selon une seule colonne
- [Masquer des colonnes]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Partager la vue]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})

## Afficher ou masquer d'autres colonnes

![Masquer des colonnes dans la vue Kanban](images/hide-columns-in-kanban-view.jpg) 

Si vous souhaitez afficher moins d'informations sur les cartes, cliquez sur **Masquer** et désactivez les **régulateurs** des colonnes concernées. En réactivant les régulateurs, les entrées de ces colonnes redeviennent visibles sur les cartes.

{{< warning  headline="Note"  text="Si les régulateurs ne sont **pas activés**, vous ne pouvez pas non plus voir ni modifier les valeurs des colonnes masquées lorsque vous ouvrez les **Détails de la ligne**." />}}

## Ajouter un nouvel enregistrement dans la vue Kanban

![Ajouter un nouvel enregistrement dans la vue Kanban](images/add-record-in-kanban-view.jpg)

En bas d'une colonne, cliquez sur **Ajouter une ligne**. Une nouvelle fenêtre s'ouvre. Créez un nouvel enregistrement dans les **Détails de la ligne** et ajoutez les informations souhaitées. Les modifications sont automatiquement enregistrées lorsque vous fermez la fenêtre.

## Modifier les enregistrements dans la vue Kanban

Cliquez sur une **carte Kanban** et une fenêtre avec les **Détails de la ligne** s'ouvre. Apportez les modifications souhaitées à l'enregistrement. Les modifications sont automatiquement enregistrées lorsque vous fermez la fenêtre.
