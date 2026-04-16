---
title: 'Introduction aux possibilités offertes par les données volumineuses'
date: 2023-05-12
lastmod: '2024-05-13'
categories:
    - 'big-data'
author: 'cdb'
url: '/fr/aide/big-data-fonctionnalites-seatable'
aliases:
    - '/fr/aide/potenzial-big-data'
seo:
    title: 'SeaTable Big Data : stockez des millions de lignes par base'
    description: 'Apprenez à gérer efficacement des millions de lignes dans SeaTable grâce au stockage Big Data pour chaque base.'

---

{{< required-version "Entreprise" >}}

SeaTable offre deux possibilités de stockage des enregistrements dans une base : **Par défaut**, une Base peut contenir un **maximum de 100 000 lignes**, ce qui est suffisant pour la plupart des cas d'utilisation. Si vous avez besoin d'une capacité encore plus grande, vous pouvez activer le **stockage de données volumineuses** avec un [abonnement Enterprise]({{< relref "help/teamverwaltung/abonnement/plus-oder-enterprise-abonnement-buchen" >}}), qui peut contenir un nombre presque illimité de lignes. Le fait que des millions de lignes soient possibles dans une base fait de SeaTable une alternative aux bases de données SQL classiques.

Cet article vous donne un premier aperçu de la fonction Big Data de SeaTable, tandis que vous trouverez des articles d'aide séparés pour les différents détails.

![Le backend Big data en action](images/SeaTable-3.1-Base-Stats-with-Big-Data.png)

## Une solution pour chaque besoin

En tant qu'utilisateur, vous gagnez en flexibilité grâce à l'utilisation de deux solutions de stockage. La solution standard de SeaTable est idéale pour le travail **collaboratif** sur des projets, tandis que le stockage de données volumineuses convient parfaitement aux applications à forte intensité de données avec collecte automatique de données (par ex. fichiers journaux ou valeurs de mesure statiques).

Une fois que vous [avez activé]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}), les deux solutions sont disponibles et vous pouvez déplacer vos ensembles de données entre la solution standard et le stockage des données volumineuses. L'avantage d'un stockage illimité de lignes présente toutefois l'inconvénient [de capacités collaboratives limitées]({{< relref "help/base-editor/big-data/einschraenkungen-in-der-nutzung-von-big-data" >}}).

## Vues séparées pour les deux mémoires

Comme nous l'avons déjà mentionné, la mémoire Big Data doit être activée dans une base. Ensuite, vous pouvez créer une nouvelle vue qui vous permettra d'accéder aux entrées de la mémoire Big Data. Vous trouverez plus de détails sur cette **vue Big Data** dans [cet article d'aide]({{< relref "help/base-editor/big-data/so-erstellen-sie-eine-big-data-ansicht" >}}).

## Des possibilités infinies

Le stockage de données volumineuses est une fonction unique que vous ne trouverez pas dans d'autres solutions sans code ou à code réduit. Alors que d'autres plates-formes et fournisseurs ont des plafonds et des limites sévères pour le nombre maximal de lignes, SeaTable ne vous limite pas dans votre travail.

Grâce à la fonction Big Data, il est possible de mettre en œuvre des processus et des applications qui ne seraient pas réalisables avec [Airtable]({{< relref "pages/landing-pages/alternatives/airtable-alternative" >}}), par exemple. Faites-en l'expérience. Vous serez enthousiasmé par le potentiel et les possibilités que vous offre le stockage de données volumineuses.
