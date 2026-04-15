---
title: 'Arrêter les automatisations'
date: 2023-01-27
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'kgr'
url: '/fr/aide/suspendre-automatisations-seatable'
aliases:
    - '/fr/aide/automationen-stoppen'
seo:
    title: 'Suspendre et réactiver des automatisations SeaTable : guide pratique pour l’entreprise'
    description: 'Apprenez à suspendre ou relancer les automatisations dans SeaTable Enterprise, garantir la flexibilité sans supprimer ni reconfigurer les flux d’actions.'
weight: 9
---

Si vous ne souhaitez plus exécuter des automatisations pendant une certaine période, vous pouvez les **suspendre** au lieu de les [supprimer]({{< relref "help/base-editor/automationen/automationen-loeschen" >}}). Cela présente l'avantage de pouvoir **réactiver** facilement les automations mises en pause, alors que vous devez recréer entièrement les automations supprimées.

## Suspendre temporairement les automatisations

1. Ouvrez une **Base** dans laquelle vous souhaitez suspendre une automatisation active.
2. Cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}} dans l'en-tête de la base, puis sur **Règles d'automatisation**.
3. Passez le curseur de la souris sur la règle d'automatisation correspondante, cliquez sur les trois points, puis sur {{< seatable-icon icon="dtable-icon-paused" >}} **Suspendre la règle** .

![Suspendre la règle d'automatisation](images/pause-automation-rule.gif)

La règle d'automatisation sélectionnée est ensuite **mise en pause**. Vous le reconnaissez à la mention **(en pause)** qui est ajoutée en rouge au nom de la règle d'automatisation.

{{< warning type="warning" headline="Note importante" text="Les automatismes mis en pause **ne sont plus actifs** jusqu'à ce qu'ils soient relancés. Cela signifie que les événements déclencheurs définis **ne déclencheront plus** d'actions automatisées." />}}

## Relancer l'automatisation

Pour **réactiver** les automatisations mises en pause, il suffit de suivre les étapes déjà décrites ci-dessus et de cliquer sur {{< seatable-icon icon="dtable-icon-implement" >}} **Lancer la règle** .

![relancer la règle d'automatisation](images/start-automation-rule.gif)

La mention **(en pause)** à droite du nom de l'automation disparaît ensuite.