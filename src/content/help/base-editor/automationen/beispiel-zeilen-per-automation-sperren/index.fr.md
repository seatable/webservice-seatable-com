---
title: 'Verrouiller des lignes par automatisation'
date: 2023-01-27
lastmod: '2023-03-31'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/fr/aide/verrouiller-lignes-automatisation'
aliases:
    - '/fr/aide/zeilen-per-automation-sperren'
seo:
    title: 'Verrouiller des lignes SeaTable par automatisation : guide'
    description: 'Verrouillez des lignes dans SeaTable automatiquement : déclencheurs, conditions et gestion rapide des accès collaboratifs par automatisation.'
---

Grâce aux automatisations, vous n'avez plus besoin de verrouiller manuellement les lignes dans vos tableaux, mais vous pouvez faire en sorte que le [verrouillage des lignes]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) s'effectue automatiquement. C'est très utile si vous voulez toujours empêcher qu'une ligne puisse encore être modifiée à partir d'un certain moment (par exemple lorsqu'une opération est terminée).

![Verrouiller une ligne avec une automatisation](images/lock-row-with-an-automation.png)

{{< warning  headline="Déverrouillage uniquement possible manuellement"  text="Les lignes verrouillées par une automatisation ne peuvent **pas** être **déverrouillées** de la même manière. Cela n'est possible que manuellement et avec les **droits d'administrateur** nécessaires." />}}

## Création de l'automatisation

1. Dans les options de la base, cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}}, puis sur **Règles d'automatisation**.
2. Cliquez sur **Ajouter une règle**.
3. **Nommez** l'automatisation et définissez le **tableau** et la **vue** dans lesquels elle doit agir.
4. Définissez un **événement déclencheur** qui déclenchera l'automatisation.
5. Cliquez sur **Ajouter une action** et sélectionnez **Verrouiller l'enregistrement** comme action automatisée.

![Sélection de l'action automatisée : "Verrouiller l'enregistrement"](images/lock-record.png)

6. Confirmez en cliquant sur **Envoyer**.

{{< warning headline="Remarque importante" >}}

L'action automatisée **Verrouiller l'enregistrement** est disponible uniquement pour les événements déclencheurs suivants :

- Lorsqu'une ligne est mise à jour
- Lorsqu'une ligne est ajoutée
- À une heure programmée pour les enregistrements qui correspondent aux conditions

{{< /warning >}}

## Exemple d'application

Si vous souhaitez par exemple **verrouiller** dans l'un de vos tableaux chaque ligne dans laquelle une certaine entrée atteint une **valeur** spécifique, définissez comme déclencheur de l'automatisation l'événement **Lorsqu'une ligne est mise à jour**.

![Définition de l'événement déclencheur de l'automatisation](images/trigger-example-1.png)

Définissez ensuite la **valeur** ainsi que la **colonne** dans laquelle elle doit être atteinte.

![Définition de l'événement déclencheur de l'automatisation](images/trigger-example-2.png)

Enfin, définissez **Verrouiller l'enregistrement** comme action automatisée.

![Définition de l'action automatisée](images/automated-action-example.png)

À partir de ce moment, l'automatisation créée verrouillera **toutes les lignes** dans lesquelles des **entrées** sont modifiées de manière à satisfaire à la règle d'automatisation.

![Action automatisée définie : "Verrouiller l'enregistrement"](images/automated-action-example-2.png)

{{< warning  headline="À noter" text="Avec une automatisation, vous pouvez uniquement verrouiller les lignes dans lesquelles le déclencheur de l'automatisation s'est produit. Il n'est pas possible d'appliquer une règle d'automatisation selon le schéma **l'événement sur la ligne X déclenche le verrouillage de la ligne Y**." />}}

## Verrouiller plusieurs lignes en même temps

Les automatisations sont extrêmement utiles si vous souhaitez verrouiller plusieurs lignes en même temps. Pour ce faire, sélectionnez le déclencheur **À une heure programmée pour les enregistrements qui correspondent aux conditions** et définissez les conditions correspondantes. Au lieu de définir la fréquence et l'heure d'exécution, cliquez en bas sur **Exécuter maintenant** pour verrouiller immédiatement toutes les lignes souhaitées.

Vous trouverez plus d'informations sur le verrouillage des lignes dans l'article [Verrouiller une ligne]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}).

### D'autres articles utiles dans la rubrique Automatisations :

- [Aperçu des automatisations]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [Fonctionnement des automatisations]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Créer une automatisation]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Gérer et regrouper des automatisations]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Arrêter les automatisations]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Supprimer des automatisations]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Afficher l'historique d'exécution d'une automatisation]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Déclencheurs d'automatisation]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Actions d'automatisation]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Lier des entrées par automatisation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

### Autres exemples intéressants d'automatisations :

- [Lier des entrées par automatisation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Ajouter des lignes par automatisation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Ajouter des entrées à d'autres tableaux par automatisation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Envoyer des notifications par automatisation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Envoi d'e-mails par automatisation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
