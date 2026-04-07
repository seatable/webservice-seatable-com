---
title: 'Pages de carte dans les applications'
date: 2026-04-07
lastmod: '2026-04-07'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/fr/aide/pages-de-carte-dans-les-applications'
seo:
    title: 'Pages de carte dans les applications : visualiser des lieux sur une carte du monde'
    description: 'Créez des pages de cartes dans SeaTable Apps : visualisez les données de géolocalisation et les adresses sur une carte du monde.'
weight: 9
---

Ce type de page vous permet d'afficher des **lieux** enregistrés dans votre tableur à l'aide de **données de géolocalisation ou d'adresses** sur une **carte mondiale** dans l'application.

![représentation de lieux sur une carte](images/map-page-app-builder.png)

## Paramètres de la page

Si vous souhaitez modifier les paramètres d'une page, cliquez sur l'**icône en forme de roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondante dans la navigation.

![modifier les paramètres de la page de carte](images/access-page-settings.png)

Dans les **paramètres de la page**, vous pouvez choisir le **type de carte** (standard ou images), le **tableau** et une colonne pour l'**adresse** et la **couleur du pin**. Veuillez noter que seuls certains types de colonnes sont éligibles pour ces informations.

![Paramètres de la page de la carte dans les applications](images/map-page-settings.png)

Si vous définissez une **colonne à afficher**, une légende des lieux sera affichée en permanence sur la carte.

![colonne d'affichage de la page de carte dans les applications](images/map-page-display-field.png)

Vous pouvez également définir des colonnes à afficher de manière flexible, qui ne seront visibles que par un **effet de survol**. Activez les curseurs des colonnes que vous souhaitez voir apparaître lorsque vous passez la souris sur une épingle.

![effet de survol des colonnes à afficher sur la page de la carte](images/map-page-hover-display.gif)

## Filtres prédéfinis et colonnes cachées

Vous pouvez également définir des filtres prédéfinis et des colonnes masquées afin de limiter les données affichées. Pour filtrer, cliquez sur **Ajouter un filtre**, sélectionnez la **colonne** et la **condition** souhaitées et confirmez en cliquant sur **Envoyer**.

![Filtre sur les pages de la carte](images/map-page-filters.png)

Cachez les colonnes que vous ne souhaitez pas rendre disponibles pour la page de carte en utilisant les **réglages**.

![Masquer les colonnes sur les pages de la carte](images/hide-columns-on-map-pages.png)

{{< warning type="warning" headline="Note importante" text="Les filtres par défaut et les colonnes masquées **ne peuvent pas être modifiés par les utilisateurs de l'application**. Ils ne verront donc, comme vous le souhaitez, que les données filtrées." />}}

## Autorisations de la page

Pour les pages de carte, vous ne pouvez définir qu'une seule [autorisation de page]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) – à savoir, qui peut voir la page de carte. Cela est dû au fait que vous ne pouvez **pas ajouter, modifier ou supprimer des lignes** sur les pages de carte.
