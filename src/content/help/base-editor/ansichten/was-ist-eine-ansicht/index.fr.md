---
title: "Qu'est-ce qu'une vue ?"
date: 2023-01-13
lastmod: '2025-12-03'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/fr/aide/quest-ce-quune-vue-seatable'
aliases:
    - '/fr/aide/was-ist-eine-ansicht'
seo:
    title: 'Qu’est-ce qu’une vue dans SeaTable ?'
    description: 'Découvrez le fonctionnement des vues dans SeaTable et personnalisez simplement l’affichage de vos données.'
star: true
weight: 1
---

Chaque fois que vous consultez vos données dans une table, vous les visualisez via une **vue**. Même si vous avez créé une toute nouvelle table, vous la visualisez déjà dans la vue **"Default View"** fournie par défaut.

## À quoi servent les vues ?

Dans un tableau traditionnel, vous voyez toujours les données de la même manière. Vous pouvez ajouter ou supprimer des lignes et des colonnes, mais vous ne pouvez pas voir les mêmes données sous des angles différents.

SeaTable vous permet de créer des vues et d'utiliser **des filtres, des tris, des regroupements, des masquages, des couleurs et des hauteurs de ligne** pour déterminer quelle partie de vos données vous souhaitez voir et de quelle manière. Vous pouvez ainsi afficher exactement les données qui vous intéressent, sans avoir à modifier ou à supprimer des enregistrements.

Vous pouvez également choisir des modes d'affichage spécifiques pour visualiser les données de manière attrayante. Voici des exemples de **types de vues** que vous pouvez créer :

![Types de vues](images/create-table-view.jpg)

- Vue de tableau
- Vue Kanban
- Vue de calendrier
- Vue de galerie
- Vue de ligne de temps
- Vue arborescente
- Vue de Big Data

Il est important de comprendre qu'une vue n'est qu'une façon différente de **considérer les mêmes données sous-jacentes** ! Cela signifie que si vous modifiez les données d'une table dans une vue, ces données changent dans toutes les vues de la table, car toutes les vues représentent le même ensemble de données.

{{< warning type="warning" headline="Conseil" >}}

Vous pouvez utiliser d'autres formes de représentation comme un organigramme ou une carte géographique sous la forme de [plugins]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}}).

{{< /warning >}}

## La vue de tableau

La **vue de tableau** est le mode d'affichage par défaut dans une base SeaTable. Elle est très similaire à une feuille de calcul, car les enregistrements sont organisés en lignes et en colonnes.

![vue tableau](images/table-view.jpg)

Si vous créez une vue filtrée ou si vous masquez des colonnes, vous ne verrez que la quantité de données dont vous avez besoin. En triant ou en regroupant selon des principes d'organisation spécifiques, vous pouvez également rendre la vue plus claire.

## La vue Kanban

Si vous avez **des colonnes avec un nombre limité d'options** dans votre tableau, vous pouvez regrouper vos lignes. La vue **Kanban** est une forme d'affichage spéciale. Elle est particulièrement adaptée à la représentation de **processus avec différentes phases**.

![la vue Kanban](images/kanban-view.jpg)

Pour en savoir plus, consultez l'article sur la [vue Kanban]({{< relref "help/base-editor/ansichten/die-kanban-ansicht" >}}).

## La vue de calendrier

Si vous avez une table avec des **colonnes de dates**, vous pouvez créer une vue de calendrier qui organise tous vos enregistrements **chronologiquement**.

![La vue Calendrier](images/calendar-view.jpg)

Pour en savoir plus, consultez l'article sur la [vue de calendrier]({{< relref "help/base-editor/ansichten/die-kalender-ansicht" >}}).

## La vue de galerie

Si vous avez une table avec une **colonne d'images**, vous pouvez créer une vue de galerie pour illustrer les enregistrements avec des vignettes.

![La vue galerie](images/gallery-view.jpg)

Pour en savoir plus, consultez l'article sur la [vue de galerie]({{< relref "help/base-editor/ansichten/die-galerie-ansicht" >}}).

## La vue de ligne de temps

Si vous avez une table avec **deux colonnes de dates**, vous pouvez créer une vue chronologique qui visualise différentes périodes sur une **ligne de temps**. Elle est particulièrement adaptée pour représenter la séquence de processus ou vérifier si des périodes **se chevauchent** – par exemple pour la planification des congés, les plans de projet ou la réservation de salles.

![La vue chronologique](images/timeline-view.jpg)

Pour en savoir plus, consultez l'article sur la [vue chronologique]({{< relref "help/base-editor/ansichten/die-zeitleisten-ansicht" >}}).

## La vue arborescente

Si vous avez une base avec **au moins deux tables liées**, vous pouvez créer une vue arborescente pour afficher les enregistrements liés de manière **hiérarchique**. Elle est particulièrement adaptée pour visualiser des structures complexes telles que des portefeuilles de projets ou des hiérarchies organisationnelles – avec jusqu'à trois niveaux dans le diagramme arborescent.

![La vue arborescente](images/tree-view.jpg)

Pour en savoir plus, consultez l'article sur la [vue arborescente]({{< relref "help/base-editor/ansichten/die-baum-ansicht" >}}).

## La vue de Big Data

Si vous avez activé le **stockage Big Data** dans votre base, vous pouvez **archiver de grandes quantités de données** qui ne sont pas immédiatement visibles par tous les utilisateurs. Pour accéder aux données du stockage Big Data, une vue Big Data spéciale est nécessaire.

![la vue Big Data](images/create-big-data-view.jpg)

Pour en savoir plus, consultez l'article sur la [vue de Big Data]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}).

## Autres articles sur le thème des vues

- [Créer une nouvelle vue]({{< relref "help/base-editor/ansichten/anlegen-einer-neuen-ansicht" >}})
- [Renommer une vue]({{< relref "help/base-editor/ansichten/umbenennen-einer-ansicht" >}})
- [Supprimer une vue]({{< relref "help/base-editor/ansichten/loeschen-einer-ansicht" >}})
- [La duplication de vues]({{< relref "help/base-editor/ansichten/das-duplizieren-von-ansichten" >}})
- [Différences entre les vues privées et les vues normales]({{< relref "help/base-editor/ansichten/unterschiede-zwischen-privaten-und-normalen-ansichten" >}})
- [L'impression d'une vue]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})
- [Modifier l'ordre des vues]({{< relref "help/base-editor/ansichten/die-reihenfolge-von-ansichten-aendern" >}})
- [Regrouper les vues dans des dossiers]({{< relref "help/base-editor/ansichten/ansichten-in-ordnern-gruppieren" >}})
- [Filtrer les entrées d'une vue]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}})
- [Relier les règles de filtrage avec ET et OU]({{< relref "help/base-editor/ansichten/filter-regeln-mit-und-und-oder-verknuepfen" >}})
- [Trier les entrées d'une vue]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}})
- [Regrouper des entrées dans une vue]({{< relref "help/base-editor/ansichten/gruppieren-von-eintraegen-in-einer-ansicht" >}})
- [Coloration de cellules]({{< relref "help/base-editor/ansichten/einfaerben-von-zellen" >}})
- [Marquage par couleur des lignes]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Ajuster la hauteur des lignes]({{< relref "help/base-editor/ansichten/zeilenhoehe-anpassen" >}})
- [Ajuster le nombre de colonnes épinglées]({{< relref "help/base-editor/spalten/anzahl-der-fixierten-spalten-anpassen" >}})
- [Masquer et déplacer des colonnes]({{< relref "help/base-editor/ansichten/ausblenden-und-verschieben-von-spalten" >}})
- [Verrouiller les vues]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Partage d'une vue avec un membre de l'équipe]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Créer un lien externe pour une vue]({{< relref "help/startseite/freigaben/externen-link-fuer-eine-ansicht-erstellen" >}})
