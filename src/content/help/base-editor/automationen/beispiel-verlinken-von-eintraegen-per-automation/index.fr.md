---
title: 'Lier des entrées par automatisation'
date: 2023-01-30
lastmod: '2023-04-06'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/fr/aide/lier-entrees-automatisation'
aliases:
    - '/fr/aide/verlinken-von-eintraegen-per-automation'
seo:
    title: 'Lier des entrées dans SeaTable par automatisation : guide'
    description: 'Automatisez vos liens dans SeaTable : définissez les déclencheurs, champs et reliez automatiquement les enregistrements entre tables.'


---

Grâce aux automatisations, vous ne devez plus relier manuellement les entrées de vos tableaux entre elles, mais vous pouvez exécuter ces étapes automatiquement. Il suffit de définir une automatisation pour n'importe quelle vue du tableau.

## Liens vers des entrées par automatisation

![Bloquer et archiver des lignes avec une automatisation](images/how-to-use-automations-for-locking-rows-3.png)

1. Cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}} dans l'en-tête de base, puis sur **Règles d'automatisation**.
2. Cliquez sur **Ajouter une règle**.
3. **Nommez** l'automatisation et définissez le **tableau** et la **vue** dans lesquels elle doit agir.
4. Définir un **événement déclencheur** qui déclenchera l'automatisation.
5. Cliquez sur **Ajouter une action** et sélectionnez **Ajouter des liens** comme action automatisée.
6. Confirmez en cliquant sur **Envoyer**.

## Création de l'automation

Définissez d'abord un **événement déclencheur** pour l'automatisation.

![Événements déclencheurs pour le blocage et l'archivage des lignes](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Remarque importante" >}}

L'action automatisée **Ajouter des liens** est à votre disposition **exclusivement** est disponible pour les événements déclencheurs suivants :

- "Les entrées remplissent certaines conditions après traitement"
- "Une nouvelle entrée est ajoutée"
- "Déclencheur périodique"

{{< /warning >}}

Sélectionnez ensuite **"Ajouter des liens"** comme action automatisée.

![Ajout de l'action automatisée](images/add-an-action.png) ![Ajout de l'action automatisée : "Ajouter des liens"](images/add-action-add-links.png)

Sélectionnez enfin une **colonne** qui doit être liée au tableau sélectionné et définissez une **condition spécifique** qui doit être remplie pour que l'automatisation soit exécutée.

![Définition de l'action automatisée](images/automated-actions-add-links.png)

Confirmez finalement l'automatisation en cliquant sur **Envoyer**.

![Confirmation de l'automatisation](images/confirm-the-automation.jpg)

## Exemple d'application

Un **cas d'utilisation** concret de ce type d'automatisation pourrait par exemple se présenter si vous travaillez dans le service comptabilité d'une entreprise. Vous souhaitez tenir à jour à la fois un tableau avec tous les paiements qui arrivent sur un compte de l'entreprise (**Payments**) et un tableau avec toutes les factures qui doivent être payées à l'entreprise (**Invoices**).

Dans le tableau **Payments**, outre les **numéros de transaction** des paiements (P-0001, etc.), vous enregistrez déjà les **montants** des différents paiements (colonne **"Value"**).

![Tableau d'exemple Payments](images/Table-Payments-1.png)

Votre tableau **Invoices** contient quant à lui les **numéros de facture** (colonne **"Invoice-No"**) ainsi que les **montants respectifs des factures** (colonne **"Price Total"**).

![Tableau d'exemple "Invoices"](images/Table-Invoices.png)

À l'aide d'une **automatisation**, vous souhaitez maintenant **relier** les deux tableaux **Payments** et **Invoices** afin de pouvoir automatiquement attribuer les **paiements** reçus à une **facture** sur la base de leurs numéros de facture.

### Préparation de l'automatisation

Avant de pouvoir créer l'automatisation, vous devez d'abord ajouter deux colonnes supplémentaires au tableau **Payments**. Dans la colonne **"Inv-No"**, vous saisissez manuellement les numéros de facture qui correspondent aux paiements respectifs — c'est ce qui **déclenchera** ultérieurement l'automatisation. Dans la colonne **"Invoices"**, les **entrées liées** du tableau **Invoices** seront ajoutées automatiquement une fois l'automatisation en place.

![Extension manuelle du tableau "Payments" de deux colonnes](images/Manuelle-Erweiterung-der-Tabelle-22Payments22.png)

Dans le tableau **Invoices**, vous avez également besoin d'une colonne supplémentaire (**"Collected Payments"**) dans laquelle les entrées liées du tableau **Payments** seront ajoutées lors de l'exécution de l'automatisation.

![](images/Hinzufuegen-der-Spalte-22Collected-PAyments22.png)

Vous pouvez ensuite créer une **automatisation** pour le tableau **Payments**.

### Création de l'automatisation

Tout d'abord, donnez un nom à l'automatisation et sélectionnez le tableau **Payments** ainsi que la vue du même nom dans laquelle l'automatisation doit agir.

![Définition de l'automatisation du cas d'utilisation](images/definition-of-the-automation-1.png)

Comme **événement déclencheur** de l'automatisation, sélectionnez l'option **"Les entrées remplissent certaines conditions après traitement"**. Comme condition de filtre, ajoutez que les deux colonnes **"Inv-No"** et **"Value"** du tableau "Payments" **ne sont pas vides**. Cette condition est judicieuse, car l'automatisation doit être déclenchée dès qu'il y a des entrées dans ces colonnes.

![Définition de l'événement déclencheur du cas d'utilisation ](images/trigger-example-1-1.png) ![Définition de l'événement déclencheur du cas d'utilisation ](images/trigger-example-2-1.png)

Comme **action automatisée** de l'automatisation, définissez enfin l'action **"Ajouter une colonne liée au tableau"**.

![Ajout de l'action automatisée : "Ajouter des liens"](images/add-action-add-links.png)

La colonne **"Invoices"** est la colonne dans laquelle les entrées liées seront ajoutées lors de l'exécution de l'automatisation.

![Sélection de la colonne dans laquelle les entrées liées sont ajoutées](images/automated-action-example-1.png)

Dans la dernière étape de la définition de l'automatisation, vous devez définir une autre **condition** qui doit être remplie pour qu'une entrée liée soit ajoutée à la colonne. Dans cet exemple, il est défini que chaque **entrée** ajoutée dans la colonne **"Inv-No"** doit également se trouver dans la colonne **"Invoice-No"** du tableau **Invoices**.

Concrètement, cela signifie que chaque **numéro de facture** que vous attribuez manuellement à un paiement dans le tableau **Payments** doit déjà exister dans le tableau **Invoices** pour que les **entrées** correspondantes des deux tableaux puissent être **liées** entre elles.

![Définition de la condition finale pour le déclenchement de l'automatisation](images/automated-action-example-2-1.png)

### Tester l'automatisation

Si vous saisissez ensuite dans la colonne **"Inv-No"** du tableau **Payments** un numéro de facture qui existe déjà dans le tableau **Invoices**, l'**entrée liée** correspondante sera automatiquement ajoutée au tableau dans la colonne **"Invoices"**.

![Ajout des entrées liées par le déclenchement de l'automatisation](images/Ausloesen-der-Automation-Beispiel-1-1-1.png)

{{< warning  type="warning" headline="Remarque importante"  text="Si vous ajoutez dans la colonne **\\"Inv-No\\"** des numéros de facture qui ne figurent **pas encore** dans le tableau **Invoices**, l'automatisation ne sera **pas** déclenchée et, par conséquent, **aucune** entrée liée ne sera ajoutée à la colonne, puisque l'entrée correspondante n'existe tout simplement pas encore dans le tableau **Invoices**." />}}

En cliquant sur l'entrée liée, une fenêtre s'ouvre dans laquelle vous pouvez consulter le contenu de l'**entrée liée** du tableau **Invoices**.

![En cliquant sur l'entrée liée, vous pouvez consulter le contenu de la colonne liée dans l'autre tableau.](images/Informationen-der-verlinkten-Spalte.png)

En outre, le déclenchement de l'automatisation ajoute également les **entrées liées** du tableau **Payments** au tableau **Invoices**. Dans la colonne **"Collected Payments"**, chaque numéro de facture se voit automatiquement attribuer le **numéro de paiement (P-000X)** correspondant. Grâce à l'**automatisation**, vous pouvez donc consulter le **paiement** correspondant à chaque facture et déterminer rapidement quelles factures sont réglées et lesquelles restent en attente.

![Ajout des entrées liées par le déclenchement de l'automatisation](images/Ausloesen-der-Automation-Beispiel-2.png)

Dans ce tableau aussi, en cliquant sur l'entrée liée, vous pouvez ouvrir une fenêtre dans laquelle vous pouvez consulter le contenu de l'**entrée liée** du tableau **Payments**.

![En cliquant sur une entrée liée, vous pouvez consulter le contenu de la colonne liée dans l'autre tableau.](images/Informationen-der-verlinkten-Spalte-2.png)

### Autres articles utiles dans la rubrique Automatisations :

- [Vue d'ensemble des automatisations]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}})
- [Fonctionnement des automatisations]({{< relref "help/base-editor/automationen/funktionsweise-von-automationen" >}})
- [Créer une automatisation]({{< relref "help/base-editor/automationen/anlegen-einer-automation" >}})
- [Gérer et regrouper les automatisations]({{< relref "help/base-editor/automationen/automationen-verwalten-und-gruppieren" >}})
- [Arrêter les automatisations]({{< relref "help/base-editor/automationen/automationen-stoppen" >}})
- [Supprimer les automatisations]({{< relref "help/base-editor/automationen/automationen-loeschen" >}})
- [Afficher le journal d'exécution d'une automatisation]({{< relref "help/base-editor/automationen/ausfuehrungslog-einer-automation-anzeigen" >}})
- [Déclencheurs d'automatisation]({{< relref "help/base-editor/automationen/automations-trigger" >}})
- [Actions d'automatisation]({{< relref "help/base-editor/automationen/automations-aktionen" >}})
- [Verrouiller des lignes par automatisation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})

### Autres exemples intéressants d'automatisations :

- [Verrouiller des lignes par automatisation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Ajouter des lignes par automatisation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Ajouter des entrées à d'autres tableaux par automatisation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Envoyer des notifications par automatisation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
- [Envoyer des e-mails par automatisation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
