---
title: "Envoi d'e-mails par automatisation"
date: 2023-03-03
lastmod: '2023-03-03'
categories:
    - 'beispiel-automationen'
author: 'nsc2'
url: '/fr/aide/envoi-emails-automatiques-par-automation'
aliases:
    - '/fr/aide/e-mail-versand-per-automation'
seo:
    title: 'Envoi d’emails automatiques dans SeaTable – tutoriel'
    description: 'Découvrez comment automatiser l’envoi d’e‑mails dans SeaTable grâce à des règles, déclencheurs et comptes SMTP configurés.'
---

Grâce aux automatisations, vous ne devez plus envoyer manuellement des e-mails à des utilisateurs sélectionnés, mais vous pouvez les faire envoyer automatiquement. Il suffit pour cela de définir une automatisation correspondante pour n'importe quelle vue de tableau.

## Envoyer des e-mails par automatisation

![Envoyer des e-mails par automatisation](images/how-to-use-automations-for-locking-rows-3.png)

1. Cliquez sur {{< seatable-icon icon="dtable-icon-rule" >}} dans l'en-tête de base, puis sur **Règles d'automatisation**.
2. Cliquez sur **Ajouter une règle**.
3. **Nommez** l'automatisation et définissez le **tableau** et la **vue** dans lesquels elle doit agir.
4. Définir un **événement déclencheur** qui déclenchera l'automatisation.
5. Cliquez sur **Ajouter une action** et sélectionnez **Envoyer un e-mail** comme action automatisée.
6. Confirmez en cliquant sur **Envoyer**.

## Création de l'automation

Définissez d'abord un **événement déclencheur** pour l'automatisation.

![Événements déclencheurs à choisir en principe](images/trigger-options-for-archivating-rows.png)

{{< warning  headline="Remarque" >}}

L'action automatisée **Envoyer un e-mail** est disponible après tous les événements déclencheurs :

- Les entrées remplissent certaines conditions après traitement
- Une nouvelle entrée est ajoutée
- Déclencheur périodique
- Déclenchement périodique pour les entrées qui remplissent certaines conditions

{{< /warning >}}

Sélectionnez ensuite **Envoyer un e-mail** comme action automatisée.

![Ajout de l'action automatisée](images/add-an-action.png) ![Ajout de l'action automatisée](images/example-send-email-action.png)

Dans l'étape suivante, sélectionnez d'abord un **compte de messagerie** depuis lequel vous souhaitez envoyer les e-mails. Pour pouvoir utiliser votre compte de messagerie pour l'envoi, vous **devez** d'abord **ajouter** celui-ci comme prestataire tiers dans votre base SeaTable. Vous trouverez des instructions détaillées pour cette étape [ici]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}}).

{{< warning  type="warning" headline="Remarque importante"  text="Si vous n'avez **pas** ajouté de compte de messagerie comme prestataire tiers dans votre base SeaTable, **aucun** compte ne s'affichera. L'ajout d'un compte de messagerie constitue donc une **condition préalable** importante pour l'automatisation." />}}

![Sélection d'un compte de messagerie pour l'envoi](images/select-email-account.png)

Après avoir sélectionné le compte de messagerie, définissez l'**objet**, le **destinataire** et le **contenu** de l'e-mail. Vous pouvez saisir **plusieurs adresses e-mail** séparées par des virgules et en CC. Vous avez également la possibilité d'ajouter des **pièces jointes** depuis une [colonne de fichiers]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}).

![Définition de l'e-mail à envoyer par l'automatisation](images/define-email.png)

Confirmez finalement l'automatisation en cliquant sur **Envoyer**.

![Confirmation de l'automatisation](images/confirm-the-automation.jpg)

## Exemple d'application

Un **cas d'utilisation** concret de ce type d'automatisation pourrait par exemple se présenter si vous travaillez au comité d'entreprise d'une société. Vous souhaitez informer automatiquement le service des ressources humaines que vous avez approuvé le licenciement d'un employé.

De votre côté, cela peut être mis en œuvre à l'aide d'un tableau dans lequel sont gérées différentes **données** de tous les employés de votre entreprise. Dans ce contexte, vous pourriez enregistrer, entre autres, les **noms** des employés, leur **statut d'emploi** et l'état de leurs **paiements salariaux**.

![Tableau d'exemple du cas d'utilisation concret](images/example-table-email-automation.png)

À l'aide d'une automatisation, SeaTable doit maintenant envoyer automatiquement un **e-mail** au service des ressources humaines dès que vous avez approuvé au comité d'entreprise le licenciement d'un employé.

### Création de l'automatisation

Tout d'abord, donnez un **nom** à l'automatisation et sélectionnez à la fois le **tableau** (employee list) et la **vue** (employees ressort marketing) dans lesquels l'automatisation doit agir.

![Paramètres de base de l'automatisation](images/basic-settings-automation.png)

Comme **événement déclencheur** de l'automatisation, sélectionnez l'option **Les entrées remplissent certaines conditions après traitement**. Pour que les e-mails soient envoyés **uniquement** en cas de licenciement d'un employé, ajoutez comme **condition de filtre** que l'entrée dans la colonne **status of employment** doive être modifiée en **terminated**.

![Définition de l'événement déclencheur](images/condition-of-the-trigger-event.png)

Comme **action automatisée**, définissez l'action **Envoyer un e-mail**.

![Ajout de l'action automatisée](images/example-send-email-action.png)

Dans l'étape suivante, sélectionnez un **compte de messagerie** depuis lequel vous souhaitez envoyer les e-mails au service des ressources humaines. Pour pouvoir utiliser votre compte de messagerie pour l'envoi, vous **devez** d'abord **ajouter** celui-ci comme prestataire tiers dans votre base SeaTable. Vous trouverez des instructions détaillées pour cette étape [ici]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}}).

{{< warning  type="warning" headline="Remarque importante"  text="Si vous n'avez **pas** ajouté de compte de messagerie comme prestataire tiers dans votre base SeaTable, **aucun** compte ne s'affichera à cette étape. L'ajout d'un compte de messagerie constitue donc une **condition préalable** importante pour l'automatisation." />}}

![Sélection d'un compte de messagerie pour l'envoi](images/select-email-account-1.png)

Après avoir sélectionné votre compte de messagerie, définissez l'**objet**, le **destinataire** et le **contenu** des e-mails. Vous pouvez saisir **plusieurs adresses e-mail** séparées par des virgules et en CC. Enfin, vous avez également la possibilité d'ajouter des **pièces jointes** depuis une [colonne de fichiers]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}).

{{< warning  headline="Astuce"  text="À l'aide d'accolades, vous pouvez citer des **contenus de colonnes du tableau** dans le corps de l'e-mail. Utilisez cette fonctionnalité pour insérer automatiquement les **noms** des employés licenciés dans le texte." />}}

![Définition de l'e-mail pour l'automatisation du cas d'utilisation](images/definition-email-example.png)

Lorsque vous avez terminé l'e-mail à envoyer, confirmez l'automatisation avec **Envoyer**.

### Tester l'automatisation

Si, dans le tableau sélectionné, vous modifiez ensuite le statut d'emploi d'un employé en **terminated**, l'**e-mail** préparé sera automatiquement envoyé au service des ressources humaines pour l'informer du licenciement.

![Une fois le statut d'emploi d'un employé modifié en "terminated", l'e-mail préparé est automatiquement envoyé aux destinataires sélectionnés ](images/test-automation-email.jpg)

### Autres exemples intéressants d'automatisations :

- [Verrouiller des lignes par automatisation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-sperren" >}})
- [Lier des entrées par automatisation]({{< relref "help/base-editor/automationen/beispiel-verlinken-von-eintraegen-per-automation" >}})
- [Ajouter des lignes par automatisation]({{< relref "help/base-editor/automationen/beispiel-zeilen-per-automation-hinzufuegen" >}})
- [Ajouter des entrées à d'autres tableaux par automatisation]({{< relref "help/base-editor/automationen/beispiel-eintraege-in-andere-tabellen-per-automation-hinzufuegen" >}})
- [Envoyer des notifications par automatisation]({{< relref "help/base-editor/automationen/benachrichtigungen-per-automation-versenden" >}})
