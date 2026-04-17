---
title: "Afficher l'historique d'exécution d'une automatisation"
date: 2023-01-26
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/fr/aide/journal-execution-automatisation'
aliases:
    - '/fr/aide/ausfuehrungslog-einer-automation-anzeigen'
seo:
    title: "Historique d’exécution des automatisations SeaTable : suivez statut, temps et alertes"
    description: "Apprenez à consulter l'historique d’exécution des automatisations SeaTable Enterprise : temps d’exécution, conditions, succès et messages d’alerte inclus."
weight: 8
---

Pour vérifier **la bonne exécution d'une automatisation**, vous avez la possibilité de consulter **l'historique d'exécution**. SeaTable y consigne les informations suivantes pour chaque exécution d'automatisation : heure d'exécution, condition d'exécution, état et avertissements éventuels. En outre, il existe une **statistique globale** de tous les cycles d'automatisation.

{{< warning  headline="Remarque importante"  text="Chaque exécution d'un automatisme est appelée **cycle d'automatisation**." />}}

## Pour jeter un coup d'œil à l'historique d'exécution

![Afficher l'historique d'exécution](images/open-automation-log.jpg)

1. Cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}} dans l'en-tête de base, puis sur **Règles d'automatisation**.
2. Passez le curseur de la souris sur la **règle d'automatisation** dont vous souhaitez consulter le log.
3. Cliquez sur les **trois points** et ensuite sur {{< seatable-icon icon="dtable-icon-journal" >}} **Ouvrir l'historique**.

## Structure de l'historique d'exécution

![Structure de l'historique d'exécution](images/structure-of-an-automation-log.jpg)

Vous pouvez consulter les informations suivantes dans l'historique d'exécution d'une automatisation :

**Heure d'exécution**  
SeaTable enregistre ici l'heure exacte à laquelle le déclencheur a déclenché l'automation.

**Condition d'exécution**  
Si l'automation est déclenchée par la modification ou l'ajout d'une entrée, le message **per_update** apparaît. En revanche, si l'automatisation est déclenchée périodiquement, le message **per_day/week/month** apparaît.

**Statut**  
Le statut indique si l'automatisation a été exécutée avec succès. Si c'est le cas, le message **Succès** s'affiche ici.

**Avertissements**  
S'il y a eu des problèmes lors de l'exécution d'une automatisation, un message d'avertissement correspondant apparaît ici.

## Statistique de tous les cycles d'automatisation

Vous pouvez également consulter les statistiques sur **le nombre total d'exécutions d'automation dans la base**, indépendamment des règles d'automation individuelles. Vous pouvez ainsi savoir à quelle fréquence vos règles d'automatisation sont déclenchées et combien de cycles d'automatisation disponibles dans votre abonnement mensuel vous avez déjà utilisés.

1. Dans l'éditeur d'automatisation ouvert, cliquez sur **Statistique** en haut à droite.
![ouvrez les statistiques d'automatisation](images/open-automation-statistic.png)
2. Une fenêtre s'ouvre alors, dans laquelle vous pouvez voir le **nombre d'automations exécutées par jour**.
![statistiques d'exécution des automatismes](images/automation-statistic.png)