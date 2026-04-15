---
title: 'Aperçu des automatisations'
date: 2023-01-31
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/fr/aide/automatisations-guide-seatable'
aliases:
    - '/fr/aide/uebersicht-ueber-automationen'
    - '/fr/aide/automatisations-pas-de-disponibles-seatable'
    - '/fr/aide/warum-finde-ich-in-meiner-base-die-automationen-nicht'
seo:
    title: 'Automatisations SeaTable : guide, fonctions et usages'
    description: 'Structurez et automatisez vos tâches dans SeaTable : déclencheurs, actions, gestion, logs et exemples d’automatisations réussir vos workflows.'
star: true
weight: 1
---

L'automatisation est une fonction utile de SeaTable qui vous aide à **automatiser les processus de travail**. Les automatisations vous permettent non seulement de **gagner du temps**, mais aussi de **réduire le nombre d'erreurs humaines** dans la gestion de vos données, car les étapes du processus exécutées automatiquement ne doivent plus être effectuées manuellement par un utilisateur.

En conséquence, les automatisations déploient un effet particulièrement important dans les **ensembles de données volumineux**, dans lesquels elles peuvent traiter un grand nombre de processus de travail.

L'article suivant a pour but de vous donner une vue d'ensemble sur le thème des automatisations dans SeaTable et contient des liens vers les différents articles d'aide concernant cette fonctionnalité.

## L'éditeur d'automatisation de SeaTable

Vous pouvez accéder à l'éditeur d'automatisation d'une base en cliquant sur l'icône correspondante dans l'en-tête de la base.

![accès à l'éditeur d'automatisation](images/access-automation-editor.jpg)

L'éditeur d'automatisation s'étend sur toute la largeur de la fenêtre et permet donc une mise en page claire : sur le côté gauche se trouve la **liste de toutes les règles d'automatisation existantes**. Passer d'une règle à l'autre se fait donc en un seul clic. Vous pouvez également y ajouter de nouvelles règles et gérer les règles existantes.

![éditeur d'automatisation en action](images/automation-editor-in-action.gif)

Dans la zone centrale, vous voyez la configuration de l'automation actuellement sélectionnée. Celle-ci se compose d'un **déclencheur** et d'une ou plusieurs **actions**. Les paramètres du déclencheur ou des actions s'affichent dynamiquement sur la droite, en fonction de l'élément sur lequel vous avez cliqué.

Vous pouvez également réduire la liste des règles d'automatisation afin de libérer de l'espace dans la zone centrale. Un autre facteur de confort est la **hauteur variable du tableau de bord de l'éditeur**. Vous pouvez ainsi voir la vue, les noms des colonnes et les enregistrements pendant que vous travaillez sur une automatisation.

## Créer une automatisation

La première étape vers l'automatisation des processus de travail est la création d'une automatisation. Pour que tout se déroule comme prévu et que les règles d'automatisation créées aient l'effet souhaité, nous avons résumé pour vous dans cet article l'essentiel à savoir.

Apprenez [ici]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}}) comment créer une automatisation.

## Gérer des automatisations

Vous pouvez bien sûr modifier après coup les automatisations actives déjà créées. Dans cet article, nous vous présentons les réglages que vous pouvez effectuer lors de l'automatisation de vos processus de travail.

Apprenez-en plus sur la gestion des automatisations [ici]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}}).

## Fonctionnement des automatisations

Cet article explique de manière basique comment fonctionnent les automations dans SeaTable et est donc approprié pour **débuter dans le domaine des automations**.

Apprenez-en plus sur le fonctionnement des automatismes [ici]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}}).

## Déclencheur d'automatisation

Les déclencheurs d'automatisation représentent le premier des deux composants essentiels des automatisations. Les déclencheurs, que vous pouvez définir individuellement pour chaque automation, déclenchent différents types d'actions automatisées.

Apprenez-en plus sur les déclencheurs d'automatisation [ici]({{< relref "help/base-editor/automationen/automations-trigger" >}}).

## Actions d'automatisation

Les actions automatisées représentent la deuxième des deux composantes essentielles des automatisations. Les actions sont alors déclenchées par les événements déclencheurs définis. Selon le déclencheur, SeaTable peut exécuter différentes actions d'automatisation.

Apprenez-en plus sur les actions d'automatisation [ici]({{< relref "help/base-editor/automationen/automations-aktionen" >}}).

## Afficher l'historique d'exécution d'une automatisation

Pour vérifier l'exécution des automatisations, vous avez la possibilité d'afficher l'historique d'exécution pour chaque règle d'automatisation. Celui-ci vous permet de consulter des informations sur chaque exécution d'automatisation.

Apprenez-en plus [ici]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}}) sur le log d'exécution d'une automatisation.

## Arrêter les automatisations

Les automatisations actives dont vous n'avez plus besoin pendant un certain temps peuvent être simplement mises en pause et réactivées si nécessaire.

Apprenez [ici]({{< relref "help/base-editor/automationen/automationen-stoppen" >}}) comment arrêter les automatisations.

## Supprimer des automatisations

Vous pouvez également supprimer complètement les automatisations qui ne sont plus nécessaires de manière durable. Notez que vous ne pouvez pas restaurer les automatismes supprimés.

Apprenez [ici]({{< relref "help/base-editor/automationen/automationen-loeschen" >}}) comment supprimer des automatisations.

## Verrouiller des lignes par automatisation

Grâce aux automatisations, vous ne devez plus bloquer manuellement des lignes dans vos tableaux, mais vous pouvez faire en sorte que ce blocage s'effectue automatiquement. C'est très utile si vous voulez toujours empêcher qu'une ligne puisse être traitée à partir d'un certain moment (par exemple lorsqu'une opération est terminée).

Apprenez [ici]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}}) comment bloquer des lignes avec une automatisation.

## Ajouter des lignes par automatisation

Grâce à l'automatisation, vous ne devez plus ajouter manuellement des lignes avec certaines entrées dans vos tableaux, mais vous pouvez faire en sorte que ces étapes soient effectuées automatiquement. Cela est particulièrement avantageux si vous souhaitez automatiser diverses étapes de processus dans vos tableaux.

Apprenez [ici]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}}) comment ajouter des lignes par automatisation.

## Ajouter des entrées dans d'autres tableaux par automatisation

Grâce à l'automatisation, vous ne devez plus effectuer manuellement des entrées dans d'autres tableaux, mais vous pouvez faire en sorte que ces étapes soient exécutées automatiquement. Le grand avantage est que le déclencheur ne doit pas se trouver dans le même tableau que l'action déclenchée. Cette automatisation est particulièrement avantageuse si vous utilisez différents tableaux dont les contenus sont en relation les uns avec les autres.

Apprenez [ici]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}}) comment ajouter des entrées dans d'autres tableaux par automatisation.

## Envoi d'e-mails par automatisation

Grâce à l'automatisation, vous ne devez plus envoyer manuellement des e-mails à des utilisateurs sélectionnés, mais vous pouvez les envoyer automatiquement. Cela s'avère particulièrement utile si vous souhaitez par exemple informer immédiatement les utilisateurs des modifications apportées aux données de certains tableaux.

Découvrez [ici]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}) comment envoyer des e-mails par automatisation.

## Liens vers des entrées par automatisation

Grâce à l'automatisation, vous ne devez plus relier manuellement les entrées de vos tableaux entre elles, mais vous pouvez faire en sorte que ces étapes soient effectuées automatiquement. Cela s'avère utile lorsque vous avez besoin de certaines données dans plusieurs tableaux.

Apprenez [ici]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}}) comment lier des entrées par automatisation.
