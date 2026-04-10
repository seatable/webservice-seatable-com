---
title: 'Pages de la galerie dans les applications de SeaTable'
date: 2023-12-04
lastmod: '2024-08-02'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/fr/aide/pages-galerie-apps-seatable'
aliases:
    - '/fr/aide/galerieseiten-in-universellen-apps'
    - '/fr/aide/pages-galerie-apps-universelles'
seo:
    title: 'Pages galerie dans SeaTable Apps : mode d’emploi'
    description: 'Présentez images & données en galerie dans SeaTable Apps : filtres, droits d’accès et liens de tables personnalisables.'
weight: 4
---

Ce type de page vous permet d'afficher **des images** et d'autres données que vous avez enregistrées dans votre tableau sous la forme d'une **galerie** au sein d'une application. Vous pouvez par exemple utiliser une page de galerie pour **créer des fiches d'information** claires sur **vos collaborateurs**.

![Représentation de vos collaborateurs dans une page de galerie](images/page-type-gallery-example.png)

## Paramètres de la page

Si vous souhaitez modifier les paramètres d'une page, cliquez dans la navigation sur le **symbole de la roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondant.

![Modifier les paramètres du site de la galerie](images/Einstellungen-der-Galerieseite-aendern.png)

Dans les **paramètres de la page**, vous pouvez sélectionner le **tableau**, la **colonne d'images** et la **colonne de titres** à partir desquels la galerie est alimentée.

![Paramètres de la page de la galerie dans les applications](images/Seiteneinstellungen-der-Galerieseite-in-Universellen-Apps.png)

## Filtres prédéfinis, tris et colonnes masquées

En outre, vous pouvez définir des filtres prédéfinis, des tris et des colonnes masquées afin de limiter et d'organiser les données affichées pour les utilisateurs. Pour filtrer ou trier, cliquez sur **Ajouter un filtre** ou **Ajouter un tri**, sélectionnez la **colonne** et la **condition** souhaitées et confirmez en cliquant sur **Envoyer**.

![Ajouter un filtre sur les pages de la galerie dans les applications](images/Add-filter-on-gallery-pages-in-Universal-Apps.png)

Les utilisateurs peuvent afficher plus d'informations sur une fiche dans la galerie en cliquant sur une entrée.

![Ouvrir l'entrée sur la page de la galerie](images/Eintrag-auf-der-Galerieseite-oeffnen.gif)

Décidez donc quelles données doivent être **visibles** et affichez ou masquez les colonnes correspondantes à l'aide des **curseurs**.

![Hide columns on gallery pages](images/Hide-columns-on-gallery-pages-in-Universal-Apps-1.png)

{{< warning  headline="Remarque importante"  text="Les utilisateurs de l'application ne peuvent **pas modifier les filtres prédéfinis**, les **tris** et les **colonnes masquées**. Ils n'obtiennent donc, comme ils le souhaitent, que les entrées filtrées dans un ordre fixe." />}}

## Paramètres de la colonne des liens

Dans les **paramètres de la colonne des liens**, vous pouvez définir pour chaque tableau lié quelles données sont visibles et quelles opérations sont autorisées.

![Paramètres de colonne de lien sur les pages de tableau](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Autoriser l'ajout de nouvelles entrées**: si vous activez ce curseur, les utilisateurs peuvent ajouter de nouvelles entrées dans le tableau lié. Les paramètres des champs permettent de définir quelles colonnes sont **visibles** et quelles colonnes sont **obligatoires**, c'est-à-dire qu'elles doivent être remplies.
- **Autoriser la liaison d'entrées existantes**: si vous activez ce curseur, les utilisateurs peuvent lier des entrées existantes du tableau lié. Vous pouvez définir quelles colonnes sont **visibles** via les paramètres de champ.
- **Limiter les liens à une ligne maximum**: Si vous activez ce curseur, les utilisateurs ne pourront plus lier qu'une seule ligne du tableau lié à la fois dans les cellules de la colonne des liens.
- **Filtres prédéfinis**: si vous ajoutez un filtre ici, seules les options qui remplissent les conditions du filtre seront affichées lors de la création de liens vers des entrées.
- **Activer la fonction Big Data**: Lorsque la fonction Big Data est activée, les utilisateurs peuvent effectuer des recherches sur plus de 20.000 enregistrements, à condition qu'il y ait autant d'entrées dans le tableau lié.

## Autorisations des pages

Vous pouvez définir les [autorisations de page]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) suivantes pour les pages de la galerie :

![Autorisations des pages de la galerie](images/Seitenberechtigungen-von-Galerieseiten.png)

Décidez qui peut voir la page de la galerie, y ajouter des lignes, la modifier et la supprimer. Grâce aux options d'autorisation différenciées de ce type de page, vous pouvez régler cela avec précision.
