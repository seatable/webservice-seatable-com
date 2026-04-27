---
title: 'La vue Ligne de temps'
date: 2026-03-31
lastmod: '2026-03-31'
categories:
    - 'grundlagen-von-ansichten'
author: 'kgr'
url: '/fr/aide/la-vue-ligne-de-temps'
aliases:
    - '/fr/aide/guide-plugin-timeline'
    - '/fr/aide/anleitung-zum-timeline-plugin'
seo:
    title: 'Vue Ligne de temps : visualiser les périodes dans SeaTable'
    description: 'La vue Ligne de temps vous donne un aperçu clair des périodes et de leurs chevauchements.'
weight: 15
---

La vue **Ligne de temps** vous permet de visualiser différentes périodes de temps sur une **ligne de temps**. Ceci est très utile, par exemple, lorsque vous souhaitez visualiser la séquence de processus ou voir si des périodes se **chevauchent**. En conséquence, vous pouvez utiliser la vue de la ligne de temps pour la [planification des congés]({{< relref "templates/human-resources/holiday-request-management" >}}), les [plans de projet]({{< relref "templates/projects/project-plan" >}}) ou la réservation de salles de conférence, entre autres.

![La vue de la ligne du temps](images/timeline-view.jpg)

{{< warning type="avertissement" headline="conditions" >}}

Ce type de vue affiche **des périodes de temps**. Vous avez donc besoin de **deux** [colonnes de dates]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) dans un tableau qui définissent le **début** et la **fin** des périodes.

{{< /warning >}}

## Pour créer une vue de la ligne de temps

1. Cliquez sur le **nom de la vue actuelle**.
2. Cliquez sur **Ajouter une vue ou un dossier** et sélectionnez le **type de vue** souhaité.

![Créer une vue Ligne de temps](images/create-timeline-view.png)

3. Donnez un **nom** à la nouvelle vue.
4. Activez le curseur si vous souhaitez que la nouvelle vue ne soit pas visible par tous, mais **privée**.
5. Confirmez en cliquant sur **Envoyer**.
6. Définissez ensuite dans les paramètres les **dates de début et de fin** et la **période** que doit couvrir la ligne de temps. La nouvelle vue est ensuite générée automatiquement.
7. Dans le champ de saisie supérieur, indiquez la colonne dont dépend l'**étiquette du bloc**.

![créer une vue de la ligne de temps](images/create-timeline-view.gif)

## Options de vue

Vous pouvez utiliser les options suivantes dans une vue Ligne de temps :
- [Verrouiller la vue]({{< relref "help/base-editor/ansichten/ansicht-sperren" >}})
- [Filtrer]({{< relref "help/base-editor/ansichten/filtern-von-eintraegen-in-einer-ansicht" >}}) ou [trier]({{< relref "help/base-editor/ansichten/sortieren-von-eintraegen-in-einer-ansicht" >}}) 
- [Couleur de la ligne]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}})
- [Partager la vue]({{< relref "help/startseite/freigaben/freigabe-einer-ansicht-an-ein-teammitglied" >}})
- [Imprimer la vue]({{< relref "help/base-editor/ansichten/das-drucken-einer-ansicht" >}})

## Options d'affichage

Il y a en tout 5 options d'affichage pour l'échelle de la ligne de temps : **année**, **trimestre**, **mois**, **semaine** et **jour**. Vous pouvez facilement passer d'une option à l'autre. Pour ce faire, il vous suffit de cliquer sur l'option correspondante dans le **menu déroulant** au-dessus de la barre de temps.

![Options d'affichage de la ligne de temps](images/display-options-timeline-view.jpg)

## Afficher ou masquer les informations

Cliquez sur **Afficher les colonnes** pour afficher plus ou moins d'informations en affichant ou en masquant des colonnes. Activez les **règles** de chaque colonne pour afficher plus d'informations à partir des enregistrements de la ligne de temps.

![afficher les informations des autres colonnes sur la ligne de temps](images/other-fields-shown-in-timeline-view.gif)

## Modifier les enregistrements dans la vue Ligne de temps

Double-cliquez sur un enregistrement et une fenêtre s'ouvre avec les **détails de la ligne**. Apportez les modifications souhaitées à l'enregistrement. Les modifications sont automatiquement enregistrées lorsque vous fermez la fenêtre.

## Prolonger, raccourcir ou déplacer des périodes

Pour prolonger ou raccourcir une période, faites glisser **le bord gauche ou droit d'un enregistrement** en maintenant le bouton de la souris enfoncé. Pour déplacer une période, maintenez le bouton gauche de la souris enfoncé et déplacez l'enregistrement **par glisser-déposer** dans la direction souhaitée. Les valeurs correspondantes dans les colonnes de dates s'adaptent automatiquement.

![modifier les périodes dans la vue Ligne de temps](images/change-records-in-timeline-view.gif)