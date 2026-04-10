---
title: 'Pages de requête dans les applications de SeaTable'
date: 2023-12-08
lastmod: '2025-02-27'
categories:
    - 'seitentypen-in-universellen-apps'
author: 'kgr'
url: '/fr/aide/pages-requete-apps-seatable'
aliases:
    - '/fr/aide/abfrageseiten-in-universellen-apps'
    - '/fr/aide/pages-requete-apps-universelles'
seo:
    title: 'Pages de requête dans les apps de SeaTable'
    description: 'Recherchez et filtrez de grands ensembles de données dans les apps de SeaTable : définissez filtres, tris et champs de requête pour des résultats sur mesure.'
weight: 9
---

Ce type de page vous permet de rechercher des valeurs spécifiques dans vos ensembles de données à travers certains champs. Ce type de page est particulièrement utile pour les **ensembles de données volumineux** tels que les catalogues de produits ou les bibliothèques. Une application concrète pourrait être par exemple la consultation d'un répertoire d'employés.

![Pages de requête dans les applications](images/Abfrageseiten-in-Universellen-Apps.png)

## Paramètres de la page

Si vous souhaitez modifier les paramètres d'une page, cliquez dans la navigation sur le **symbole de la roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}} correspondant.

![Modifier les paramètres de la page de requête](images/Einstellungen-der-Abfrageseite-aendern.png)

## Filtres prédéfinis, tris et colonnes masquées

Dans les **paramètres de la page**, vous définissez d'abord le **tableau** dans lequel la recherche doit être effectuée.

Vous pouvez ensuite définir des **filtres**, des **tris** et **des colonnes masquées** prédéfinis afin de limiter et d'organiser les données affichées pour les utilisateurs. Pour filtrer ou trier, cliquez sur **Ajouter un filtre** ou **Ajouter un tri**, sélectionnez la **colonne** et la **condition** souhaitées et confirmez en cliquant sur **Envoyer**.

![Ajouter un filtre sur les pages de requête dans les applications](images/Add-filter-on-query-pages-in-Universal-Apps.png)

Les utilisateurs peuvent voir toutes les informations des enregistrements applicables dans les **résultats de la requête** si vous ne les limitez pas. Décidez donc quelles données doivent être **visibles** et affichez ou masquez les colonnes correspondantes à l'aide des **curseurs**.

![Hide columns on query pages](images/Hide-columns-on-query-pages-in-Universal-Apps.png)

{{< warning  headline="Remarque importante"  text="Les utilisateurs de l'application ne peuvent **pas modifier les filtres prédéfinis** et les **colonnes masquées**. Ils n'obtiennent donc que les données filtrées, comme ils le souhaitent. Les utilisateurs peuvent toutefois personnaliser la **hauteur des lignes** et le **tri** des enregistrements consultés." />}}

## Ajouter des champs de requête

Les **champs de requête** sont essentiels pour ce type de page. Ils permettent aux utilisateurs de rechercher des valeurs spécifiques dans les colonnes sélectionnées du tableau et de **trouver** ainsi **des enregistrements**. Cliquez sur {{< seatable-icon icon="dtable-icon-enlarge" >}} **Ajouter un** champ dans les paramètres de la page pour définir un champ de requête.

![Ajouter des champs sur les pages de requête](images/Felder-auf-Abfrageseiten-hinzufuegen.png)

Vous pouvez ensuite sélectionner la **colonne** souhaitée et définir si le champ de requête est **nécessaire**, si une **recherche floue** est possible et si les **majuscules et les minuscules sont** prises en compte lors de la saisie.

## Ajouter une remarque

Vous pouvez ajouter une **note** d'introduction à votre page de requête, qui peut par exemple contenir des explications sur la manière de remplir les champs de requête. Pour ce faire, il vous suffit d'activer le **curseur** dans les paramètres de la page et d'écrire la remarque dans la zone de texte qui apparaît.

![Ajouter une remarque aux pages de requête](images/Hinweis-auf-Abfrageseiten-der-Universellen-App-hinzufuegen.png)

## Modifier les résultats de la requête

Pour pouvoir utiliser cette fonction, vous devez **activer** le curseur dans les paramètres de la page sous **Si le résultat de la requête est modifiable**.

![Rendre le résultat de la requête modifiable](images/Abfrageergebnis-bearbeitbar-machen.png)

Ensuite, tous les utilisateurs ayant accès à la page de requête peuvent **traiter** les **enregistrements** recherchés.

![Modifier les résultats de la requête sur les pages de requête](images/Abfrageergebnisse-bearbeiten-auf-Abfrageseiten-der-App.gif)

- Effectuez une **recherche de données réussie**.
- Déplacez votre souris sur la **numérotation des lignes** de la liste de résultats et cliquez sur l'**icône en forme de double flèche** devant l'enregistrement que vous souhaitez modifier.
- Effectuez les modifications souhaitées dans les **détails de la ligne** ouverte.
- Cliquez sur l'**icône x** pour fermer la fenêtre et enregistrer vos modifications.

{{< warning  type="warning" headline="Colonnes en lecture seule" text="Vous pouvez définir à l'avance des colonnes qui ne pourront pas être modifiées. Pour cela, allez dans les paramètres de la page et cochez les cases des colonnes qui doivent être **en lecture seule** pour les utilisateurs. Vous reconnaissez les colonnes en lecture seule au fait que les champs sont grisés dans les détails de la ligne." />}}

## Autorisations des pages

Tout en bas, dans les paramètres de la page, vous pouvez limiter les personnes autorisées à voir la page de requête.

![Autorisation pour les pages de requête](images/Berechtigung-fuer-individuelle-Seiten-der-Universellen-App.png)

C'est la seule [autorisation de page]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) que vous pouvez choisir ici. Les pages de requête ne permettent pas d'ajouter ou de supprimer des lignes dans le tableau.

Toutefois, après une recherche de données réussie, les utilisateurs de l'application peuvent actionner [des boutons]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) dans la liste de résultats affichée afin d'**effectuer** certaines **actions**.

![Exécuter des boutons sur des pages de requête](images/Schaltflaechen-auf-Abfrageseiten-ausfuehren.gif)

Un exemple d'application est une bourse d'emploi interne : la page de requête permet de rechercher rapidement les postes pertinents. Si un poste intéressant y figure, il suffit alors de cliquer sur le bouton dans les résultats de recherche pour postuler directement à l'emploi.

{{< warning  headline="Attention aux boutons" >}}

[Les boutons]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}}) peuvent **toujours** être actionnés, indépendamment des autorisations de la page. Cela permet à tout utilisateur de l'application d'effectuer certaines modifications sur les enregistrements que vous avez définis au préalable, même si les colonnes concernées sont par ailleurs bloquées pour lui ou si l'utilisateur n'est pas autorisé à modifier les résultats de la requête.

{{< /warning >}}
