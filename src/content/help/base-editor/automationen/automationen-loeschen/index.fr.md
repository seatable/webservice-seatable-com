---
title: 'Supprimer des automatisations'
date: 2022-12-06
lastmod: '2025-11-05'
categories:
    - 'automationen'
author: 'nsc2'
url: '/fr/aide/supprimer-automatisations-seatable'
aliases:
    - '/fr/aide/automationen-loeschen'
seo:
    title: 'Supprimer des automatisations dans SeaTable facilement'
    description: 'Mode d’emploi pour effacer une automatisation dans SeaTable, éviter les erreurs, connaître l’impact sur les règles et actions.'
weight: 10
---

Vous pouvez **supprimer** à tout moment les **règles d'automatisation** déjà créées. Attention aux conséquences de la suppression sur les différentes **actions automatisées**.

## Comment supprimer une automatisation

![Supprimer une automatisation](images/delete-automation-rule.gif)

1. Ouvrez une **Base** dans laquelle vous souhaitez supprimer une automatisation déjà créée.
2. Cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}} dans l'en-tête de la base, puis sur **Règles d'automatisation**.
3. Passez le curseur de la souris sur la règle d'automatisation correspondante, cliquez sur les trois points, puis sur {{< seatable-icon icon="dtable-icon-delete" >}} **Supprimer la règle** .
4. Confirmez en cliquant sur **Supprimer**.

{{< warning type="warning" headline="La suppression est définitive" text="La règle d'automatisation supprimée est ensuite **définitivement disparue et ne peut pas être restaurée**." />}}

## Effets

Selon les actions que vous aviez définies pour une automatisation, la suppression d'une règle d'automatisation peut avoir **différentes conséquences**. En principe, l'événement déclencheur défini **ne déclenchera plus aucune action** après la suppression, sauf s'il sert encore de déclencheur pour une autre automatisation existante.

En particulier pour les actions complexes à créer, comme l'envoi d'e-mails, les scripts Python ou les fonctions d'intelligence artificielle, vous devriez envisager de simplement [suspendre l'automatisation]({{< relref "help/base-editor/automationen/automationen-stoppen" >}}) plutôt que de la supprimer définitivement.