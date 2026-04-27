---
title: 'Ajouter des lignes par automatisation'
date: 2023-03-02
lastmod: '2023-03-31'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/fr/aide/ajouter-lignes-automatiques-seatable'
aliases:
    - '/fr/aide/zeilen-per-automation-hinzufuegen'
seo:
    title: 'Ajouter des lignes automatiquement via automation'
    description: 'Automatisez l’ajout de lignes dans vos tableaux SeaTable grâce aux règles, déclencheurs ou périodicité selon vos besoins.'
---

Grâce aux automatisations, vous n'avez plus besoin d'ajouter manuellement des lignes avec certaines entrées dans vos tableaux, mais vous pouvez faire en sorte que ces étapes soient effectuées automatiquement. Il suffit pour cela de définir une automatisation correspondante pour n'importe quelle vue du tableau.

## Comment ajouter des lignes avec une automatisation

![Ajouter des entrées par automatisation](images/how-to-use-automations-for-locking-rows-3.png)

1. Cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}} dans l'en-tête de base, puis sur **Règles d'automatisation**.
2. Cliquez sur **Ajouter une règle**.
3. **Nommez** l'automatisation et définissez le **tableau** et la **vue** dans lesquels elle doit agir.
4. Définir un **événement déclencheur** qui déclenchera l'automatisation.
5. Cliquez sur **Ajouter une action** et sélectionnez **Ajouter une ligne** comme action automatisée.
6. Confirmez en cliquant sur **Envoyer**.

## Création de l'automation

Définissez d'abord un **événement déclencheur** pour l'automatisation.

![Événements déclencheurs à choisir en principe](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Remarque importante" >}}

L'action automatisée **Ajouter une ligne** est à votre disposition **exclusivement** sont disponibles après les événements déclencheurs suivants :

- Une nouvelle entrée est ajoutée
- Les entrées remplissent certaines conditions après traitement
- Déclencheur périodique

{{< /warning >}}

Sélectionnez ensuite **Ajouter une ligne** comme action automatisée.

![Ajout de l'action automatisée](images/add-an-action.png) ![Sélection de l'action automatisée](images/action-add-records.png)

Dans l'étape suivante, définissez les **entrées** qui doivent apparaître dans une ligne après le déclenchement de l'automatisation. En cliquant sur **Ajouter un champ**, vous pouvez définir n'importe quelle entrée.

![Cliquez sur Ajouter un champ pour définir des entrées](images/add-field.png)

Sélectionnez d'abord la **colonne** dans laquelle l'entrée doit être insérée.

![Sélection de la colonne dans laquelle l'entrée est ajoutée](images/select-column-to-add-record.jpg)

Vous pouvez ensuite définir l'**entrée**. Selon le [type de colonne]({{< relref "help/base-editor/spalten/uebersicht-alle-spaltentypen" >}}
) sélectionné, différentes **options** sont à votre disposition.

![Définissez l'entrée que vous souhaitez ajouter au tableau](images/define-record-to-add.png)

Enfin, activez l'automatisation en cliquant sur **Envoyer**.

![Confirmation de l'automatisation](images/confirm-the-automation.jpg)

## Exemple d'application

Un **cas d'utilisation** concret de ce type d'automatisation pourrait par exemple se présenter si vous consignez vos réunions d'équipe hebdomadaires dans un tableau. Vous souhaitez qu'une ligne contenant certaines entrées soit automatiquement créée chaque semaine avant le début de la réunion, afin de n'avoir plus qu'à saisir manuellement les informations restantes.

Dans ce contexte, vous pourriez prédéfinir, entre autres, la **date** de la réunion, la **salle de réunion** et les **sujets** récurrents.

![Tableau d'exemple pour le cas d'utilisation concret](images/example-table-case-record-to-table.png)

### Création de l'automatisation

Tout d'abord, donnez un **nom** à l'automatisation et sélectionnez à la fois le **tableau** (ici : Team Meetings) et la **vue** (ici : Weekly Team Meeting) dans lesquels l'automatisation doit agir.

![Nommage de l'automatisation, sélection du tableau et de la vue dans lesquels l'automatisation doit agir](images/basic-settings-automation-example.png)

Comme **événement déclencheur** de l'automatisation, sélectionnez l'option **Déclencheur périodique**.

![Sélection de l'événement déclencheur](images/select-trigger.png)

Définissez ensuite les intervalles auxquels l'automatisation doit être exécutée. Pour que la ligne contenant les entrées correspondantes soit ajoutée chaque semaine au tableau, sélectionnez **hebdomadaire**.

![Sélection des intervalles auxquels l'automatisation doit être exécutée](images/run-frequency.png)

Vous pouvez également sélectionner un **jour de la semaine** concret ainsi qu'une **heure** concrète à laquelle l'automatisation sera déclenchée. Dans notre cas d'utilisation, il est judicieux de choisir comme moment une heure avant le début de la réunion hebdomadaire du lundi matin.

![Sélection du moment concret d'exécution de l'automatisation](images/set-weekday-and-hour.png)

Comme **action automatisée**, définissez à l'étape suivante l'action **Ajouter une ligne**.

![Sélection de l'action automatisée](images/select-add-record-as-a-action.png)

En cliquant sur **Ajouter un champ**, vous pouvez définir autant d'**entrées** que vous le souhaitez, qui apparaîtront automatiquement dans la ligne.

![Cliquez sur Ajouter un champ pour définir des entrées](images/add-field.png)

Pour que la ligne enregistre automatiquement la date de la réunion d'équipe prévue le même jour, sélectionnez la **colonne de date** et la valeur **Le jour de l'exécution**.

![Définition des entrées](images/definiton-of-the-records.png)

En cliquant sur **Ajouter un champ**, vous pouvez définir autant d'**entrées** supplémentaires que vous le souhaitez, qui rempliront la ligne après le déclenchement de l'automatisation. Il suffit de sélectionner une **colonne** correspondante de votre tableau dans le menu déroulant et de définir une valeur dans le champ de saisie adjacent.

![Définissez autant d'entrées que vous le souhaitez ](images/other-records.jpg)

Si, par exemple, la réunion d'équipe a habituellement lieu dans une salle donnée, vous pouvez définir cette salle comme valeur fixe. Et si certains sujets (tels que les arrivées/départs/anniversaires) sont à l'ordre du jour de chaque réunion d'équipe, vous pouvez également faire en sorte qu'ils soient toujours ajoutés à la ligne.

### Tester l'automatisation

Si l'automatisation fonctionne comme prévu, SeaTable ajoutera automatiquement à votre tableau une ligne avec les **entrées** précédemment définies après le déclenchement du déclencheur périodique (ici : tous les lundis à 7 h). Cela vous économise quelques frappes et vous pouvez ensuite saisir manuellement les données encore ouvertes.

![Tableau après le déclenchement de l'automatisation définie ](images/table-after-automation-new-record-to-current-table.png)

{{< warning  type="warning" headline="Astuce"  text="Pour vous épargner réellement du travail et **ne pas** avoir à modifier les valeurs saisies automatiquement, il est judicieux de définir **uniquement** des valeurs déjà fixes que vous n'aurez **pas** à ajuster manuellement a posteriori. Les ajustements des entrées ajoutées automatiquement sont possibles à tout moment, mais limitent considérablement l'intérêt de l'automatisation." />}}

### Autres exemples intéressants d'automatisations :

- [Verrouiller des lignes par automatisation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Lier des entrées par automatisation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})

- [Ajouter des entrées à d'autres tableaux par automatisation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Envoyer des notifications par automatisation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Envoyer des e-mails par automatisation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
