---
title: 'Guide du module Statistiques'
date: 2023-02-06
lastmod: '2024-03-18'
categories:
    - 'statistiken-und-datenanalyse'
author: 'vge'
url: '/fr/aide/statistiques-graphique-module-seatable'
aliases:
    - '/fr/aide/anleitung-zum-statistik-modul'
seo:
    title: 'Statistiques et graphiques : guide SeaTable module'
    description: 'Créez des graphiques et tableaux de bord facilement dans SeaTable, analysez vos données, suivez l’évolution et adaptez la visualisation à vos besoins.'
weight: 1
---

Le **module Statistiques** vous permet de présenter visuellement les données de votre tableau sous la forme de différents **graphiques** et **diagrammes**. Ceci est extrêmement utile pour votre travail dans SeaTable : grâce aux **tableaux de bord**, vous gardez toujours une vue d'ensemble des chiffres et des développements statistiques dans votre base.

![Module de statistiques](images/erweitertes-statistik-plugin-release-notes.gif)

## Ouvrir le module de statistiques

Le module de statistiques est installé par défaut dans chaque base. Vous pouvez toujours y accéder en cliquant sur le bouton "Statistiques" dans l **'en-tête de la base**.

![Module de statistiques dans l'en-tête de base](images/statistic-plugin-in-base-header.jpg)

## Créer un graphique

1. Ouvrez le module Statistiques et cliquez en haut à droite sur le bouton {{< seatable-icon icon="dtable-icon-add-table" >}} **Ajouter un graphique**.

Vous avez la possibilité de choisir parmi différents **types** de graphiques et de diagrammes. Faites défiler la sélection ou cliquez sur les icônes étiquetées dans la barre d'options pour aller directement à l'endroit souhaité.

![Naviguer dans le module Statistiques.](images/Navigieren-im-Statistik-Plugin-1.png)

2. Choisissez le **type** qui convient à vos statistiques et cliquez sur **Soumettre**.

### Paramètres de données

3. Définissez le **tableau** et la **vue** à partir desquels le graphique doit obtenir les données.
4. Selon le graphique, vous pouvez définir différents **paramètres de données** – dans le cas d'un diagramme à colonnes, par exemple, quelles valeurs vous souhaitez afficher sur les **axes X et Y**. Vous pouvez également définir le type de graphique que vous souhaitez utiliser.

![Créer un nouveau graphique dans le module Statistiques.](images/Dateneinstellungen.png)

Vous commencez le travail détaillé sur un diagramme à colonnes en sélectionnant la colonne qui doit fournir les **valeurs pour l'axe des abscisses**. Cliquez sur le champ déroulant correspondant et sélectionnez la **colonne**. Un curseur vous permet de définir si vous souhaitez prendre en compte **les lignes vides** dans le diagramme.

Choisissez ensuite comment les **valeurs** doivent être représentées **sur l'axe des ordonnées**. Vous pouvez choisir entre le **nombre** d'entrées ayant une certaine valeur dans la colonne sélectionnée et l'option **Résumer le champ**, qui vous permet d'évaluer dans des **colonnes numériques** soit la somme, la moyenne, le nombre de valeurs uniques, le maximum ou le minimum. Pour les graphiques **groupés** ou **empilés**, vous pouvez spécifier une colonne d'options en fonction desquelles vous souhaitez grouper.

Toutes les modifications de réglage sont effectuées **en temps réel**, ce qui signifie que le graphique est immédiatement **mis à jour** à chaque modification de réglage. Vous pouvez ainsi voir directement si vous avez obtenu le résultat souhaité ou si vous devez procéder à des ajustements.

### Paramètres de style

5. Donnez un **titre** au graphique. Pour ce faire, cliquez sur l'onglet **Style du graphique** et saisissez le nom souhaité.
6. Si le graphique que vous avez choisi permet des **réglages de style**, vous pouvez par exemple configurer les **titres des axes X et Y**, les **couleurs** ou les **étiquettes de données**.

![Paramètres pour l'ajout d'un nouveau graphique dans le module Statistiques.](images/Stileinstellungen.png)

## Graphiques sur le tableau de bord

7. Après avoir fermé la fenêtre des paramètres, le graphique enregistré apparaît sur votre **tableau de bord**.

Vous pouvez créer **plusieurs tableaux de bord** et créer autant de graphiques que vous le souhaitez sur chaque tableau de bord. Pour modifier l'**ordre des graphiques**, il suffit de les **glisser-déposer** à l'endroit souhaité. Pour ce faire, placez le curseur de la souris sur le **titre** d'un graphique jusqu'à ce qu'une **croix fléchée** apparaisse, puis maintenez le **bouton de la souris** enfoncé.

![Déplacer les graphiques dans le module Statistiques.](images/Dashboard_Sortierung_Statistik-Plugin.gif)

## Options pour un graphique

Lorsque vous passez le curseur de la souris sur un graphique, une **icône** en **forme de double flèche** {{< seatable-icon icon="dtable-icon-open" >}} et une **icône en forme de trois points** {{< seatable-icon icon="dtable-icon-more-level" >}} apparaissent dans le coin supérieur droit. Sélectionnez la double flèche pour afficher un graphique en **mode plein écran**. Vous pouvez accéder à toutes les autres options en cliquant sur les trois points :

- Modifier le graphique
- Copier le graphique
- Exporter en tant qu'image
- Supprimer le graphique

![Module statistique Options graphiques](images/Statistik-Plugin-Grafik-Optionen.gif)

## Autres options d'affichage

En cliquant sur {{< seatable-icon icon="dtable-icon-full-screen" >}}, vous pouvez afficher toute la fenêtre du module Statistiques en **mode plein écran**.

![Module de statistiques Mode plein écran](images/Statistik-Plugin-Vollbildmodus.gif)

Les icônes {{< seatable-icon icon="dtable-icon-night-mode" >}} et {{< seatable-icon icon="dtable-icon-day-mode" >}} permettent de passer du **mode clair au mode sombre**.

![Module de statistiques Mode nuit](images/Statistik-Plugin-dark-mode.png)
