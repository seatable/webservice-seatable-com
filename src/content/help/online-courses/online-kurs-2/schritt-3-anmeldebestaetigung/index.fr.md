---
title: "Étape 3 : Confirmation d'inscription"
date: 2024-09-19
lastmod: '2024-09-24'
categories:
    - 'online-kurs-2'
author: 'cdb'
url: '/fr/aide/etape-3-confirmation-inscription'
aliases:
    - '/fr/aide/schritt-3-anmeldebestaetigung'
seo:
    title: 'Étape 3 : Confirmation d’inscription par email'
    description: 'Découvrez comment envoyer des confirmations d’inscription et demandes de paiement par email aux participants avec SeaTable.'
---

Ajoutons maintenant la possibilité d'envoyer par e-mail, à chaque participant inscrit, une confirmation d'inscription accompagnée d'une demande de paiement.

## Envoyer des e-mails avec SeaTable

Pour envoyer des e-mails depuis SeaTable, il faut d'abord enregistrer un compte e-mail dans la base. Comme le paramétrage varie d'un fournisseur à l'autre, nous vous recommandons d'utiliser [Mailtrap](https://mailtrap.io) dans le cadre de ce cours. _Mailtrap_ dirige vos e-mails vers une boîte aux lettres virtuelle : aucun e-mail ne part vers de vrais destinataires, ni vers des adresses fictives, mais l'envoi est simulé de façon réaliste.

{{< warning headline="Quel fournisseur de messagerie choisir ?" text="Il n'y a pas de _bon_ ni de _mauvais_ fournisseur de messagerie. Si vous n'envoyez que quelques e-mails par jour, votre compte de messagerie actuel suffira sans doute. Si le volume augmente, pensez à un fournisseur professionnel comme [Brevo.com](https://brevo.com), qui vous permettra de mieux suivre la distribution de vos e-mails." />}}

### Créer un compte Mailtrap

Rendez-vous sur la [page d'inscription de Mailtrap](https://mailtrap.io/register/signup) et créez un compte gratuit.

![Page d’inscription Mailtrap avec formulaire de création de compte](images/lvl2-mailtrap.png)

Confirmez votre adresse e-mail et connectez-vous. Après quelques questions sur vos centres d'intérêt, sans importance pour la suite, vous arrivez sur la page d'accueil de _Mailtrap_.

![Page d’accueil Mailtrap avec boîte de réception préconfigurée « My Inbox »](images/lvl2-mailtrap-inbox.png)

Dans le menu de gauche, cliquez sur `E-Mail Testing > Inboxes`. Une boîte de réception, `My Inbox`, est déjà créée : ce sont ses identifiants SMTP que vous allez saisir dans SeaTable.

![Identifiants SMTP de la boîte « My Inbox » pour utilisation dans SeaTable](images/lvl2-mailtrap-smtp-credentials.png)

### Configurer l'envoi d'e-mails dans SeaTable

Avec les identifiants SMTP de Mailtrap, vous pouvez maintenant configurer l'[envoi d'e-mails dans SeaTable]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).

![Boîte de dialogue SeaTable avec données SMTP Mailtrap saisies pour l’envoi d’e-mails](images/lvl2-mailtrap-in-seatable.png)

Les e-mails ne sont pas réellement envoyés : ils arrivent dans votre boîte Mailtrap. Faites l'essai en envoyant un e-mail à n'importe quelle adresse : il n'atterrira que dans votre boîte aux lettres virtuelle.

![E-mail de test dans la boîte Mailtrap pour vérifier l’envoi depuis SeaTable](images/lvl2-mailtest.gif)

## Envoyer un e-mail au participant

Vous pouvez maintenant ajouter au tableau `Registrations` une colonne qui enverra les e-mails, avec les paramètres suivants :

> Nom : au choix
>
> Type de colonne : `{{< seatable-icon icon="dtable-icon-button" >}} Button`
>
> Label : `Send`
>
> Action : `{{< seatable-icon icon="dtable-icon-email" >}} Send email`
>
> Objet : `Confirmation: Course {Registered for}`
>
> Destinataire : `customer@example.com`

![Tableau SeaTable avec colonne de bouton « Send » pour envoyer des e-mails aux participants](images/lvl2-create-button.png)

Pour le corps du message, vous pouvez reprendre ce texte :

> Hey,  
> Thank you for registering for the course {Registered for} on {Date}.
>
> To complete your registration, please transfer the course fee using the details below:
>
> Amount: {Price}  
> Bank: Example Bank LTD  
> IBAN: XYZ
>
> We appreciate your prompt payment!
>
> Best regards

Avec l'éditeur de texte simple, les noms de colonnes entre accolades sont remplacés automatiquement par le contenu correspondant. Avec l'éditeur de texte enrichi, insérez les colonnes vous-même à l'aide de la fonction `{{< seatable-icon icon="dtable-icon-choose-column" >}} Insert column`.

![Éditeur de texte enrichi SeaTable avec espaces réservés pour le cours et la date](images/lvl2-rich-text-editor.png)

Cliquez ensuite sur le bouton et vérifiez que l'e-mail arrive bien dans votre boîte Mailtrap.

Félicitations ! Vous venez d'envoyer votre premier e-mail depuis SeaTable, même s'il n'est allé que dans la boîte virtuelle de Mailtrap.

{{< warning  headline="Envoyer des e-mails automatiquement"  text="Pour l'instant, l'envoi des e-mails est déclenché par un clic sur un bouton. Une automatisation peut aussi s'en charger : les automatisations sont au programme du cours 4." />}}

## Article d'aide avec plus d'informations

- [Configurer un compte de messagerie dans une base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}})
- [Configurer Gmail pour l'envoi d'e-mails via SMTP]({{< relref "help/integrationen/integrationen-innerhalb-von-seatable/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten" >}})
- [Le bouton]({{< relref "help/base-editor/spaltentypen/die-schaltflaeche" >}})
- [Envoyer un e-mail via un bouton]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}})
- [E-mail par automatisation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}})
