---
title: 'Pages Kanban dans les applications de SeaTable'
date: 2023-12-07
lastmod: '2023-12-07'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/fr/aide/pages-kanban-apps-seatable'
aliases:
    - '/fr/aide/kanbanseiten-in-universellen-apps'
    - '/fr/aide/pages-kanban-apps-universelles'
seo:
    title: 'Pages Kanban dans les apps de SeaTable : Pilotez vos projets visuellement'
    description: 'Maîtrisez l’utilisation des pages Kanban de SeaTable pour organiser vos tâches, personnaliser cartes, appliquer des filtres et définir des autorisations robustes.'
weight: 7
---

Ce type de page vous offre la possibilité d'afficher des entrées sous forme de fiches sur un **tableau Kanban**. Une application concrète pourrait être, par exemple, la **visualisation des workflows et de l'avancement du projet**.

![Pages Kanban dans les applications](images/Kanbanseiten-in-Universellen-Apps.png)

## Modifier les paramètres de la page

Si vous souhaitez modifier les paramètres d'une page, cliquez dans la navigation sur le **symbole de la roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondant.

![Modifier les paramètres de la page Kanban](images/Einstellungen-der-Kanbanseite-aendern.png)

Dans les **paramètres de la page**, déterminez le **tableau** sur lequel le tableau Kanban est basé, la colonne selon laquelle les entrées sont **regroupées** et la colonne d'où proviennent les **titres**.

![Paramètres de la page Kanban dans les applications](images/Seiteneinstellungen-der-Kanbanseite-in-Universellen-Apps.png)

## Filtres prédéfinis, tris et colonnes masquées

En outre, vous pouvez définir des filtres prédéfinis, des tris et des colonnes masquées afin de limiter et d'organiser les données affichées pour les utilisateurs. Pour filtrer ou trier, cliquez sur **Ajouter un filtre** ou **Ajouter un tri**, sélectionnez la **colonne** et la **condition** souhaitées et confirmez en cliquant sur **Envoyer**.

![Ajouter un filtre sur les pages kanban dans les applications](images/Add-filter-on-kanban-pages-in-Universal-Apps.png)

Les utilisateurs peuvent afficher plus d'informations sur une entrée en cliquant sur une fiche. Décidez donc quelles données doivent être **visibles** et affichez ou masquez les colonnes correspondantes à l'aide des **curseurs**.

![Hide columns on gallery pages](images/Hide-columns-on-gallery-pages-in-Universal-Apps-1.png)

{{< warning  headline="Remarque importante"  text="Les utilisateurs de l'application ne peuvent **pas modifier les filtres prédéfinis**, les **tris** et les **colonnes masquées**. Ils n'obtiennent donc, comme ils le souhaitent, que les entrées filtrées dans un ordre fixe." />}}

## Paramètres de la colonne des liens

Dans les **paramètres de la colonne des liens**, vous pouvez définir pour chaque tableau lié quelles données sont visibles et quelles opérations sont autorisées.

![Paramètres de colonne de lien sur les pages de tableau](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Paramètres des colonnes** : Ici, vous pouvez définir précisément les colonnes auxquelles s'appliquent les autorisations suivantes.
- **Ajouter et relier de nouveaux enregistrements**: si vous activez ce curseur, les utilisateurs peuvent ajouter de nouvelles entrées dans le tableau lié. Les paramètres des champs permettent de définir quelles colonnes sont **visibles** et quelles colonnes sont **obligatoires**, c'est-à-dire qu'elles doivent être remplies.
- **Relier des enregistrements existants**: si vous activez ce curseur, les utilisateurs peuvent lier des entrées existantes du tableau lié. Vous pouvez définir quelles colonnes sont **visibles** via les paramètres de champ.
- **Limiter les liens à une ligne maximum**: Si vous activez ce curseur, les utilisateurs ne pourront plus lier qu'une seule ligne du tableau lié à la fois dans les cellules de la colonne des liens.
- **Filtres prédéfinis**: si vous ajoutez un filtre ici, seules les options qui remplissent les conditions du filtre seront affichées lors de la création de liens vers des entrées.
- **Activer la fonction Big Data**: Lorsque la fonction Big Data est activée, les utilisateurs peuvent effectuer des recherches sur plus de 20.000 enregistrements, à condition qu'il y ait autant d'entrées dans le tableau lié.
- **Modifier les enregistrements reliés** : Si vous activez ce curseur, les utilisateurs peuvent modifier les entrées existantes du tableau lié. Vous pouvez définir quelles colonnes sont **éditables** dans les paramètres de champ.

## Autres paramètres de page

Trois autres curseurs permettent de faire en sorte que SeaTable **n'affiche pas les lignes vides**, qu'il **affiche les noms des colonnes** sur les fiches et qu'il **renverse le texte**.

![Autres paramètres de la page Kanban dans les applications](images/Weitere-Seiteneinstellungen-der-Kanbanseite-in-Universellen-Apps.png)

Vous pouvez également afficher sur les fiches d'autres **données** du tableau sous-jacent : Pour ce faire, activez autant de **champs à afficher** que vous le souhaitez.

## Autorisations des pages

Pour les pages Kanban, vous pouvez définir les [autorisations de page]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) suivantes :

![Autorisations des pages de la galerie](images/Seitenberechtigungen-von-Galerieseiten.png)

Décidez qui peut voir la page Kanban, ajouter des lignes, les modifier et les supprimer. Grâce aux options d'autorisation différenciées de ce type de page, vous pouvez régler cela avec précision.
