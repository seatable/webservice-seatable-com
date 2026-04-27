---
title: "Ajouter des entrées à d'autres tableaux par automatisation"
date: 2023-03-03
lastmod: '2023-04-12'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/fr/aide/ajouter-donnees-tables-automatiser-seatable'
aliases:
    - '/fr/aide/eintraege-in-andere-tabellen-per-automation-hinzufuegen'
seo:
    title: 'Ajoutez des enregistrements à d’autres tables automatiquement'
    description: 'Automatisez l’ajout de lignes dans d’autres tables SeaTable avec des déclencheurs sans saisie manuelle – processus fluides.'
---

Grâce à l'automatisation, vous ne devez plus effectuer manuellement des entrées dans d'autres tableaux, mais vous pouvez faire en sorte que ces étapes soient exécutées automatiquement. Le grand avantage est que le déclencheur ne doit pas se trouver dans le même tableau que l'action déclenchée.

## Ajouter des entrées dans d'autres tableaux par automatisation

![Ajouter des entrées dans d'autres tableaux par automatisation](images/how-to-use-automations-for-locking-rows-3.png)

1. Cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}} dans l'en-tête de base, puis sur **Règles d'automatisation**.
2. Cliquez sur **Ajouter une règle**.
3. **Nommez** l'automation et définissez le **tableau** et la **vue** dans laquelle elle doit être déclenchée.
4. Définir un **événement déclencheur** qui déclenchera l'automatisation.
5. Cliquez sur **Ajouter une action** et sélectionnez **Ajouter une nouvelle entrée dans un autre tableau** comme action automatisée.
6. Définissez le **tableau** dans lequel l'entrée doit être insérée, ainsi que les **champs** pré-remplis.
7. Confirmez en cliquant sur **Envoyer**.

## Création de l'automation

Définissez un **événement déclencheur** pour l'automatisation, après avoir d'abord déterminé dans quel **tableau** et quelle **vue** il se produira.

![Événements déclencheurs à choisir en principe](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Remarque importante" >}}

L'action automatisée **Ajouter une nouvelle entrée dans un autre tableau** est à votre disposition. **exclusivement** est disponible pour les événements déclencheurs suivants :

- [Les entrées remplissent certaines conditions après traitement]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_eintraege_erfuellen_nach_bearbeitung_bestimmte_bedingungen)
- [Une nouvelle entrée est ajoutée]({{< relref "help/base-editor/automationen/automations-trigger" >}}#automations-trigger_ein_neuer_eintrag_wird_hinzugefuegt)

{{< /warning >}}

Sélectionnez ensuite **Ajouter une nouvelle entrée dans un autre tableau** comme action automatisée.

![Ajout de l'action automatisée](images/add-an-action.png) ![Sélection de l'action automatisée](images/add-action-example2.png)

Dans l'étape suivante, sélectionnez le **tableau** dans lequel l'entrée doit être ajoutée après le déclenchement du trigger.

![Sélection du tableau dans lequel l'entrée sera ajoutée après le déclenchement de l'automatisation](images/select-table.png)

Cliquez ensuite sur **Ajouter un champ** pour sélectionner les colonnes pour lesquelles vous souhaitez définir des valeurs prédéfinies dans la nouvelle entrée.

![Cliquez sur Ajouter un champ](images/add-field.png)

Dans le menu déroulant, sélectionnez maintenant une **colonne** correspondante et définissez la **valeur** pré-remplie dans le champ de saisie. En fonction du [type de colonne]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}
) sélectionné, vous disposez de différentes **options**.

![Définition de l'entrée et de la colonne à laquelle elle doit être ajoutée](images/set-table-and-entry.png)

Confirmez finalement l'automatisation en cliquant sur **Envoyer**.

![Confirmation de l'automatisation](images/confirm-the-automation.jpg)

## Exemple d'application

Un **cas d'utilisation** concret de ce type d'automatisation pourrait par exemple se présenter si, en tant que responsable d'une entreprise, vous êtes en charge des nouveaux employés qui rejoignent votre équipe. Dans le processus d'intégration, il pourrait être défini que, le premier jour de travail, vous devez demander le **versement du salaire** du collaborateur et documenter la **remise d'une voiture de fonction**.

Lorsque vous ajoutez le nouvel employé dans votre tableau, vous souhaitez informer automatiquement le service des ressources humaines que vous avez remis la voiture de fonction et qu'il peut préparer la paie du premier mois. Pour cela, SeaTable doit **ajouter une nouvelle entrée dans le tableau du service des ressources humaines**.

De votre côté, cela peut être mis en œuvre à l'aide d'un tableau dans lequel vous gérez différentes données sur les employés. Dans ce contexte, vous pourriez enregistrer, entre autres, le nom des employés ou des nouveaux arrivants, leur service et leur date d'entrée.

![Tableau d'exemple du cas d'utilisation](images/example-table.3.png)

À l'aide d'une automatisation, une nouvelle entrée doit maintenant être ajoutée automatiquement, lorsque vous ajoutez un nouvel employé dans votre tableau, à un autre tableau utilisé par le service des ressources humaines pour gérer les paiements des salaires et les voitures de fonction.

### Création de l'automatisation

Tout d'abord, donnez un **nom** à l'automatisation et sélectionnez à la fois le **tableau** (employee lists) et la **vue** (new employees) dans lesquels l'automatisation doit être déclenchée.

![Nommage de l'automatisation, sélection du tableau et de la vue dans lesquels l'automatisation doit agir](images/set-table-and-view-example-3.png)

Comme **événement déclencheur** de l'automatisation, sélectionnez l'option **Les entrées remplissent certaines conditions après traitement**.

![Sélection de l'événement déclencheur](images/trigger-condition.png)

Pour que **seules** de nouvelles entrées soient ajoutées au tableau du service des ressources humaines dès que vous avez saisi le **nom** d'un nouvel employé **dans votre tableau**, sélectionnez comme **condition de filtre** que la colonne "employee" **ne soit pas vide** après traitement.

![Ajout d'une condition de filtre](images/set-condition-example-3.png)

Comme **action automatisée**, définissez l'action **Ajouter une nouvelle entrée dans un autre tableau**.

![Sélection de l'action automatisée](images/add-action-example2.png)

Dans l'étape suivante, sélectionnez le tableau "Payments" comme **tableau** dans lequel une entrée sera ajoutée après le déclenchement de l'automatisation.

![Sélection du tableau dans lequel l'entrée est ajoutée au déclenchement de l'automatisation](images/select-table-example3.png)

Définissez ensuite les **valeurs** avec lesquelles certains champs doivent être pré-remplis. Pour reprendre le nom d'un nouvel employé dans la nouvelle entrée du tableau du service des ressources humaines, écrivez le **nom** de la colonne dans laquelle il se trouve dans votre tableau, entouré d'accolades, dans le champ de texte : {employee}

![Définition des entrées à ajouter au tableau sélectionné](images/define-the-entrys-in-the-second-table.png)

### Tester l'automatisation

Si, après avoir confirmé l'automatisation, vous saisissez le nom d'un nouvel employé dans votre tableau, ...

![Ajout d'un nouvel employé dans votre tableau](images/example-after-trigger-3.1.png)

... les entrées définies seront automatiquement ajoutées au tableau du service des ressources humaines.

![Tableau du service des ressources humaines après le déclenchement de l'automatisation](images/example-after-trigger-3.2.png)

### Autres exemples intéressants d'automatisations :

- [Verrouiller des lignes par automatisation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Lier des entrées par automatisation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Ajouter des lignes par automatisation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Envoyer des notifications par automatisation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Envoyer des e-mails par automatisation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
