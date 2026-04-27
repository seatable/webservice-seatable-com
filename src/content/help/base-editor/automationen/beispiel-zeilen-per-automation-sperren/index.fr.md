---
title: 'Verrouiller des lignes par automation'
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

Avec l'aide des automatisations, vous ne devez plus bloquer manuellement les lignes dans vos tableaux, mais vous pouvez faire en sorte que le [blocage des lignes]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}) s'effectue automatiquement. C'est très utile si vous voulez toujours empêcher qu'une ligne puisse être traitée à partir d'un certain moment (par exemple lorsqu'une opération est terminée).

![Bloquer une ligne avec une automation](images/lock-row-with-an-automation.png)

{{< warning  headline="Déverrouillage uniquement possible manuellement"  text="Les lignes bloquées par une automatisation ne peuvent **pas** être **débloquées** de la même manière. Cela n'est possible que manuellement et avec les **droits d'administrateur** nécessaires." />}}

## Création de l'automation

1. Dans les options de base, cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}}, puis sur **Règles d'automatisation**.
2. Cliquez sur **Ajouter une règle**.
3. **Nommez** l'automatisation et définissez le **tableau** et la **vue** dans lesquels elle doit agir.
4. Définir un **événement déclencheur** qui déclenchera l'automatisation.
5. Cliquez sur **Ajouter une action** et sélectionnez **Bloquer l'entrée** comme action automatisée.

![Sélection de l'action automatisée : "Bloquer l'entrée".](images/lock-record.png)

7. Confirmez en cliquant sur **Envoyer**.

{{< warning headline="Remarque importante" >}}

L'action automatisée **Entrée de la serrure** est disponible uniquement pour les événements déclencheurs suivants :

- Les entrées remplissent certaines conditions après traitement
- Une nouvelle entrée est ajoutée
- Exécuter périodiquement si les entrées remplissent certaines conditions

{{< /warning >}}

## Exemple d'application

Si vous souhaitez par exemple **bloquer** dans l'un de vos tableaux chaque ligne dans laquelle une certaine entrée atteint une **valeur** spécifique, vous définissez comme déclencheur de l'automatisation l'événement : **Les entrées remplissent certaines conditions après traitement**.

![Définition de l'événement déclencheur de l'automatisation](images/trigger-example-1.png)

Définissez ensuite la **valeur** ainsi que la **colonne** dans laquelle elle doit être atteinte.

![Définition de l'événement déclencheur de l'automatisation](images/trigger-example-2.png)

Enfin, définissez **Bloquer l'entrée** comme action automatisée.

![Définition de l'action automatisée](images/automated-action-example.png)

A partir de ce moment, l'automatisation créée bloquera **toutes les lignes** dans lesquelles **des entrées** sont modifiées de manière à satisfaire à la règle d'automatisation.

![Action automatisée définie : "Bloquer l'entrée".](images/automated-action-example-2.png)

{{< warning  headline="A noter" text="Avec une automatisation, vous pouvez toujours bloquer uniquement les lignes dans lesquelles le déclencheur de l'automatisation s'est produit. Il n'est pas possible d'appliquer une règle d'automatisation selon le schéma **l'événement sur la ligne X déclenche le blocage de la ligne Y**." />}}

## Verrouiller plusieurs lignes en même temps

Les automatisations sont extrêmement utiles si vous souhaitez bloquer plusieurs lignes en même temps. Pour ce faire, sélectionnez le déclencheur **Exécuter périodiquement les entrées qui remplissent les conditions** et définissez les conditions correspondantes. Au lieu de définir la fréquence et l'heure d'exécution, cliquez sur **Exécuter maintenant** ci-dessous pour verrouiller immédiatement toutes les lignes souhaitées.

Vous trouverez plus d'informations sur le verrouillage des lignes dans l'article [Verrouiller une ligne]({{< relref "help/base-editor/zeilen/sperren-einer-zeile" >}}).

### D'autres articles utiles dans la rubrique Automations :

- [Aperçu des automatisations]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [Fonctionnement des automatisations]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Créer une automatisation]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Gérer et éditer des automatisations]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Arrêter les automatisations]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Supprimer des automatismes]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Afficher le journal d'exécution d'une automatisation]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Déclencheur d'automatisation]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Actions d'automatisation]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Liens vers des entrées par automatisation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

### Autres exemples intéressants d'automatisation :

- [Liens vers des entrées par automatisation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Ajouter des lignes par automatisation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Ajouter des entrées dans d'autres tableaux par automatisation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Envoyer des notifications par automatisation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Envoi d'e-mails par automatisation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
