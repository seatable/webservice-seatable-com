---
title: 'Application de consultation des données'
date: 2023-05-02
lastmod: '2024-05-15'
categories:
    - 'apps'
author: 'nsc2'
url: '/fr/aide/application-recherche-donnees'
aliases:
    - '/fr/aide/datenabfrage-app'
seo:
    title: 'Appli de recherche de données : filtrer et partager des résultats'
    description: 'Découvrez comment la recherche de données permet de trouver, filtrer et partager rapidement des ensembles volumineux de données.'
---

Une **application de recherche de données** vous permet de permettre à d'autres utilisateurs de rechercher des **valeurs** spécifiques dans vos ensembles de données à travers certains **champs**. Un tel **masque de recherche** est particulièrement utile pour les ensembles de données volumineux tels que les catalogues de produits ou les bibliothèques.

## Création de l'application de consultation des données

Pour pouvoir utiliser une application de consultation de données dans votre base, vous devez d'abord l'**ajouter** à votre base.

![L'application de consultation des données](images/data-query-app-preview.png)

[Découvrez ici comment ajouter une application à votre base.]({{< relref "help/app-builder/app-verwaltung/apps-zu-einer-base-hinzufuegen" >}})

## Modifier les paramètres d'une application de récupération de données

Une fois que vous avez créé avec succès votre application de consultation des données, vous pouvez sélectionner dans les paramètres de l'application le **tableau** et les **colonnes** dans lesquels la recherche de certaines **valeurs** peut être effectuée. Pour ce faire, il vous suffit d'ouvrir l'appli en [mode édition]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}) via l'**icône du crayon** {{< seatable-icon icon="dtable-icon-rename" >}}.

Comme l'application de consultation des données est basée sur l'App Builder, les options de paramétrage suivantes sont identiques à celles des **pages de consultation de l'application**:

![Paramètres de page de l'application de consultation des données](images/Seiteneinstellungen-der-Datenabfrage-App.png)

[En savoir plus sur les possibilités de paramétrage des pages de requête.]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}})

## Modifier le nom, la couleur et l'icône d'une application de récupération de données

Vous pouvez **renommer** une application de consultation de données à tout moment. Pour ce faire, il suffit d'ouvrir l'application en **mode édition** via l'icône de crayon {{< seatable-icon icon="dtable-icon-rename" >}}. En cliquant sur l'**icône en forme de roue dentée** dans le coin supérieur gauche, vous pouvez modifier le nom, la couleur et l'icône de l'application.

[En savoir plus sur les paramètres globaux de l'application ici.]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}})

## Partager une application de consultation de données

Vous pouvez **partager** vos apps de consultation de données avec d'autres utilisateurs en quelques clics. Pour cela, allez dans la [gestion des utilisateurs et des rôles]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) de l'application.

![Partager l'application de consultation des données](images/Datenabfrage-App-teilen.png)

Lien vers l'application généré par SeaTable

![Lien personnalisé d'une application de consultation de données](images/Benutzerdefinierter-Link-einer-Datenabfrage-App.png)

Lien d'application personnalisé

{{< warning  headline="Accès illimité"  text="Les deux options offrent un **accès ouvert**. Cela signifie que vous pouvez fournir le lien à autant de personnes que vous le souhaitez (avec ou sans compte SeaTable), qui n'auront qu'à cliquer sur le lien pour accéder à l'application et récupérer les données." />}}

## Rechercher une valeur dans l'application de consultation des données

Une fois que vous avez réussi à partager votre application de consultation de données, d'autres utilisateurs peuvent commencer à interroger et à accéder aux données partagées. Pour rechercher des **valeurs** spécifiques dans vos ensembles de données, il suffit de les saisir dans les **champs de requête** et de cliquer sur **Requête**.

![Valeurs trouvées d'une requête dans la Data Query App](images/found-results-data-query.png)

## Représentation des enregistrements trouvés

Après avoir cliqué sur **Interrogation**, les utilisateurs voient immédiatement les enregistrements trouvés dans un tableau. Les utilisateurs de l'application ne peuvent voir que les valeurs des colonnes d'un ensemble de données que vous n'avez **pas masquées**. En outre, ils ne peuvent pas supprimer les **filtres** que vous avez **prédéfinis** et qui vous permettent de limiter la quantité de lignes pouvant faire l'objet d'une recherche.

![Pages de requête dans les applications](images/Abfrageseiten-in-Universellen-Apps.png)

Toutefois, les utilisateurs peuvent **trier** eux-mêmes la liste de résultats consultée et **adapter** la **hauteur des lignes** afin d'obtenir une meilleure vue d'ensemble.

## Copier une application de récupération de données

Vous avez créé une application de consultation de données que vous souhaitez utiliser sous une forme similaire pour un autre groupe d'utilisateurs ? Il vous suffit alors de copier l'appli existante et d'adapter la copie à votre guise. Pour savoir comment copier une app, [cliquez ici]({{< relref "help/app-builder/app-verwaltung/apps-kopieren" >}}).

## Désactiver une application de requête de données

Si vous avez créé une application de récupération de données que vous souhaitez désactiver temporairement, vous pouvez la désactiver en quelques clics pour révoquer l’accès à tous les groupes d’utilisateurs. Pour savoir comment procéder, [cliquez ici]({{< relref "help/app-builder/app-verwaltung/apps-zeitweise-deaktivieren" >}}).

## Supprimer une application de consultation de données

Vous pouvez **supprimer** une application de requête de données dont vous n’avez plus besoin. Ne vous inquiétez pas : la suppression **d’une application de requête de données ne supprime aucune donnée dans la base**. [Pour en savoir plus sur la suppression d’applications, cliquez ici.]({{< relref "help/app-builder/app-verwaltung/apps-loeschen" >}})
