---
title: 'Configurer Microsoft 365 pour envoyer des e-mails par SMTP'
date: 2023-04-28
lastmod: '2025-03-07'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'nsc2'
url: '/fr/aide/microsoft-365-smtp-envoi-email'
aliases:
    - '/fr/aide/microsoft-365-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Microsoft 365 et SeaTable : Paramétrez l’envoi d’e-mails SMTP sécurisé'
    description: 'Apprenez à connecter Microsoft 365 avec SeaTable pour des e-mails sécurisés par SMTP : guide d’intégration pas à pas via OAuth2 et configuration avancée.'
---

**Microsoft 365**, le service en ligne populaire pour les applications Microsoft Office, peut être utilisé pour **envoyer des e-mails depuis SeaTable**. L'authentification auprès de votre Microsoft 365 doit être effectuée à l'aide de l'authentification moderne de Microsoft. (L'authentification par nom d'utilisateur et mot de passe utilisateur n'est pas possible avec Microsoft 365).

{{< warning headline="Comptes e-mail Outlook" text="Ces instructions expliquent la procédure à suivre à l'aide d'un compte Microsoft 365. La procédure est toutefois tout aussi valable pour les comptes de messagerie Outlook gratuits." />}}

## Préparation dans l'Entra Admin Center

Pour pouvoir utiliser votre compte Microsoft 365 dans SeaTable pour l'envoi d'e-mails, vous devez d'abord créer et configurer une application dans Entra Admin Center de Microsoft.

1. Connectez-vous au [Microsoft Entra Admin Center](https://entra.microsoft.com/). L'utilisateur doit avoir les droits admin pour le compte qui sera utilisé pour l'envoi.
2. Cliquez sur **Inscriptions d'applications** dans la navigation latérale.
3. Créez une nouvelle inscription en cliquant sur **\+ Nouvelle inscription**. Saisissez un nom (par ex. 'SeaTable') et sélectionnez **Tout locataire Entra ID + compte personnel Microsoft** comme type de compte. Enregistrez l'URI de redirection suivante pour une application de type **Web** :

    ```
    https://cloud.seatable.io/oauth/third-party-email-accounts/callback/
    ```

    Si vous n'utilisez pas SeaTable Cloud, remplacez cloud.seatable.io par le nom d'hôte de votre instance SeaTable. Terminez la création de l'enregistrement de l'application en cliquant sur **S'inscrire**.

4. Notez l'**ID de l'application (client)** sur la page d'aperçu de l'application que vous venez d'enregistrer. Celui-ci est nécessaire pour la configuration du compte e-mail dans SeaTable.
5. Pour générer la clé client, accédez à **Certificats & secrets** dans la navigation latérale de l'application. Cliquez sur **Nouveau secret client**. Saisissez une description et une date d'expiration pour la clé.
   ![Création d'un secret client pour une application enregistrée dans Microsoft Entra](images/Creating_Client_Secret_Microsoft_Entra.gif)

6. Copiez la valeur de la clé créée dans le presse-papiers.

Vous avez ainsi effectué tous les préparatifs nécessaires pour pouvoir utiliser votre compte Microsoft 365 comme compte e-mail dans SeaTable.

## Création du compte e-mail dans SeaTable

Vous devez maintenant ajouter votre compte Microsoft 365 dans votre base SeaTable. Pour cela, il faut suivre les étapes suivantes :

1. Ouvrez les options avancées de la base en cliquant sur l'**icône à trois points** {{< seatable-icon icon="dtable-icon-more-level" >}} dans le coin supérieur droit.
2. Sélectionnez l'option **Intégration de comptes tiers**.
   ![Intégration de fournisseurs tiers via les options de base étendues](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)
3. Cliquez sur **Ajouter un compte e-mail**.
4. Sélectionnez **Microsoft (Microsoft 365 et Outlook)** comme prestataire de services.
5. Saisissez les informations suivantes, puis cliquez sur le bouton **Soumettre** dans le coin supérieur droit :
    - **Nom du compte**: un nom quelconque pour le compte, par exemple 'MS365'
    - **ID d'application (client)**: l'ID d'application (client) de l'app créée
    - **Clé client**: la clé client secrète de l'application créée
6. Accordez les autorisations demandées en cliquant sur **Accepter**.
   ![Screencast accept permissions requested](images/Accept-Permissions-Requested-Microsoft.gif)

## Envoyer des e-mails par automatisation ou par bouton

Ensuite, vous pouvez utiliser le compte e-mail créé dans votre SeaTable Base pour envoyer des e-mails par [automatisation]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}) ou par bouton.

Si vous souhaitez en savoir plus sur cette fonction utile, lisez l'article [Configuration d'un compte e-mail dans une base]({{< relref "help/base-editor/weitere-optionen/einrichtung-eines-e-mail-kontos-in-einer-base" >}}).
