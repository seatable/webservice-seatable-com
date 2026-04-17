---
title: 'Pages de la chronologie dans les applications de SeaTable'
date: 2023-12-04
lastmod: '2025-02-26'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/fr/aide/pages-chronologie-apps-seatable'
aliases:
    - '/fr/aide/zeitstrahlseiten-in-universellen-apps'
    - '/fr/aide/pages-chronologie-apps-universelles'
seo:
    title: 'Pages de chronologie dans les apps de SeaTable'
    description: 'Visualisez projets, congés ou tâches sur des lignes de temps interactives avec SeaTable Apps.'
weight: 8
---

Ce type de page vous permet d'afficher différentes périodes de temps sous la forme d'une **ligne de temps**. Étant donné que cette vue des données révèle les chevauchements de dates, la **planification des congés dans une entreprise**, par exemple, pourrait être un cas d'application concret.

![Page de chronologie dans les applications](images/Timeline-page-in-Universal-Apps.png)

## Paramètres de la page

Si vous souhaitez modifier les paramètres d'une page, cliquez dans la navigation sur le **symbole de la roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondant.

![Modifier les paramètres de la page de la chronologie](images/Einstellungen-der-Zeitstrahlseite-aendern.png)

Dans les **paramètres de la page**, vous pouvez tout d'abord régler la représentation graphique des lignes de temps. Pour cela, choisissez la [couleur des lignes]({{< relref "help/base-editor/ansichten/farbliche-markierung-von-zeilen" >}}) ou une [colonne de sélection simple]({{< relref "help/base-editor/spaltentypen/die-einfachauswahl-spalte" >}}) qui détermine la **couleur des blocs**. Vous pouvez également définir une colonne pour le **libellé des blocs**.

![Réglage graphique des lignes de temps dans les apps](images/Grafische-Einstellung-der-Zeitleisten.png)

Pour définir la période des entrées, vous avez besoin d'une [colonne de date]({{< relref "help/base-editor/spaltentypen/die-datum-spalte" >}}) pour la **date de début**. Pour la **date de fin**, vous pouvez utiliser une autre colonne de date ou une colonne numérique – [nombre]({{< relref "help/base-editor/spaltentypen/die-zahlen-spalte" >}}), [durée]({{< relref "help/base-editor/spaltentypen/die-dauer-spalte" >}}) ou [formule]({{< relref "help/base-editor/spaltentypen/die-formel-spalte" >}}) – qui indique le nombre de jours. Vous pouvez également sélectionner la **plage temporelle**, c’est-à-dire le nombre d’années que doit couvrir la frise chronologique.

![Paramètres de la page de la chronologie dans les applications](images/Seiteneinstellungen-der-Zeitstrahlseite-in-Universellen-Apps.png)

## Filtres prédéfinis et colonnes masquées

Vous pouvez définir **des filtres prédéfinis** et **des colonnes masquées** afin de limiter les données affichées pour les utilisateurs. Pour ce faire, cliquez sur **Ajouter un filtre**, sélectionnez la **colonne** et la **condition** souhaitées et confirmez en cliquant sur **Envoyer**.

![Ajouter un filtre sur les pages de la chronologie dans les applications](images/Add-filter-on-timeline-pages-in-Universal-Apps.png)

Les utilisateurs peuvent afficher plus d'informations sur une entrée en cliquant sur un bloc de la frise chronologique. Décidez donc quelles données doivent être **visibles** et affichez ou masquez les colonnes correspondantes à l'aide des **curseurs**.

![Cacher les colonnes sur les pages de la chronologie dans les applications](images/Hide-columns-on-timeline-pages-in-Universal-Apps.png)

{{< warning  headline="Remarque importante"  text="Les utilisateurs de l'application ne peuvent **pas modifier les filtres prédéfinis** et les **colonnes masquées**. Ils n'obtiennent donc que les données filtrées, comme ils le souhaitent." />}}

Si vous ajoutez un **regroupement**, l'affichage des barres peut également se faire en **swimlanes**. Pour les activités qui ne se chevauchent pas, cette option d'affichage permet d'obtenir une représentation compacte et claire.

![Regroupement sur les pages de la chronologie](images/Grouping-on-timeline-pages.png)

## Modifier ou déplacer une entrée sur la ligne du temps

Vous pouvez modifier des entrées très facilement en cliquant sur une **barre** et en effectuant les modifications souhaitées dans les **détails de la ligne** qui s'ouvrent.

![Modifier les entrées sur les pages de la chronologie](images/Eintraege-auf-Zeitstrahlseiten-aendern.gif)

De plus, vous pouvez **prolonger** ou **raccourcir** la **période** directement sur la ligne du temps. Pour ce faire, saisissez le **bord** droit ou gauche **de la barre** et faites-la glisser jusqu'à la date souhaitée.

![Déplacer des entrées sur des pages de la chronologie](images/Eintraege-auf-Zeitstrahlseiten-verschieben.gif)

De plus, vous pouvez facilement **déplacer** les entrées sur la ligne du temps **par glisser-déposer**. SeaTable ajuste automatiquement les **dates**.

## Paramètres de la colonne des liens

Dans les **paramètres de la colonne des liens**, vous pouvez définir pour chaque tableau lié quelles données sont visibles et quelles opérations sont autorisées.

![Paramètres de colonne de lien sur les pages de chronologie](images/Link-column-settings-on-table-pages-in-Universal-Apps.png)

- **Paramètres des colonnes** : Ici, vous pouvez définir précisément les colonnes auxquelles s'appliquent les autorisations suivantes.
- **Ajouter et relier de nouveaux enregistrements**: si vous activez ce curseur, les utilisateurs peuvent ajouter de nouvelles entrées dans le tableau lié. Les paramètres des champs permettent de définir quelles colonnes sont **visibles** et quelles colonnes sont **obligatoires**, c'est-à-dire qu'elles doivent être remplies.
- **Relier des enregistrements existants**: si vous activez ce curseur, les utilisateurs peuvent lier des entrées existantes du tableau lié. Vous pouvez définir quelles colonnes sont **visibles** via les paramètres de champ.
- **Limiter les liens à une ligne maximum**: Si vous activez ce curseur, les utilisateurs ne pourront plus lier qu'une seule ligne du tableau lié à la fois dans les cellules de la colonne des liens.
- **Filtres prédéfinis**: si vous ajoutez un filtre ici, seules les options qui remplissent les conditions du filtre seront affichées lors de la création de liens vers des entrées.
- **Activer la fonction Big Data**: Lorsque la fonction Big Data est activée, les utilisateurs peuvent effectuer des recherches sur plus de 20.000 enregistrements, à condition qu'il y ait autant d'entrées dans le tableau lié.
- **Modifier les enregistrements reliés** : Si vous activez ce curseur, les utilisateurs peuvent modifier les entrées existantes du tableau lié. Vous pouvez définir quelles colonnes sont **éditables** dans les paramètres de champ.

## Autorisations des pages

Tout en bas, dans les paramètres de la page, vous pouvez limiter les personnes autorisées à **voir** la page de la chronologie et **à modifier les** entrées. Vous ne pouvez pas ajouter ou supprimer de lignes via les pages de la chronologie.

![Autorisations des pages de la chronologie](images/Seitenberechtigungen-von-Kalenderseiten.png)
