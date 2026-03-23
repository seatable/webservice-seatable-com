---
title: 'Configurer Gmail pour envoyer des e-mails par SMTP'
date: 2023-01-10
lastmod: '2025-03-07'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'cdb'
url: '/fr/aide/configurer-gmail-pour-smtp-seatable'
aliases:
    - '/fr/aide/gmail-fuer-den-versand-von-e-mails-per-smtp-einrichten'
seo:
    title: 'Configurer Gmail pour SMTP avec SeaTable'
    description: 'SeaTable : connectez Gmail pour envoyer des emails via SMTP, app password ou OAuth2, guide étape par étape, ports et sécurité inclus.'

---

Gmail, le service de messagerie populaire de Google, peut être utilisé pour envoyer des e-mails à partir de SeaTable. L'authentification par rapport au compte Google peut se faire soit par un mot de passe de l'application, soit via OAuth. OAuth est la méthode préférée de Google, mais elle est en même temps nettement plus difficile à mettre en place. (L'authentification par nom d'utilisateur et mot de passe d'utilisateur n'est pas possible avec Gmail).

{{< warning headline="Attention aux comptes Workspace" text="Ces instructions expliquent la procédure à suivre à l'aide d'un simple compte Gmail. Toutefois, la procédure décrite ici s'applique également aux comptes Google Workspace. Si vous avez un compte Workspace, il vous suffit de vous assurer que la vérification en deux étapes est activée." />}}

## Authentification par mot de passe de l'application

Un [mot de passe d'application](https://support.google.com/accounts/answer/185833?hl=de) est un code de sécurité à 16 chiffres qui permet aux applications ou aux appareils de s'authentifier auprès de Google et d'accéder ainsi à votre compte Gmail. Vous pouvez créer des mots de passe d'application dans votre [compte Google](https://myaccount.google.com/). Les mots de passe d'application ne peuvent être utilisés que pour les comptes pour lesquels l'authentification à deux facteurs est activée.

### Création d'un mot de passe pour l'application

1. Ouvrez la gestion des mots de passe des applications de Google - connectez-vous à votre **compte Google** lorsque vous y êtes invité.
2. Saisissez un **nom**, par exemple 'SeaTable', et cliquez sur 'Créer'.

![Génération d'un mot de passe Google app](images/Google_App_Password.gif)

4. Copiez le mot de passe de l'application généré dans le cache.

{{< warning headline="Les mots de passe des applications sont destinés à un usage unique" text="Le mot de passe de l'application n'est affiché qu'après sa création. Il ne peut pas être consulté ou modifié ultérieurement. Si vous souhaitez utiliser votre compte Gmail dans plusieurs bases pour l'envoi d'e-mails, nous vous recommandons de créer plusieurs mots de passe d'app et de donner à chacun un nom descriptif." />}}

### Création d'un compte e-mail dans SeaTable

Vous devez maintenant ajouter votre compte Gmail en tant que fournisseur tiers dans votre base SeaTable. Pour cela, il faut suivre les étapes suivantes :

1. Ouvrez les options avancées de la base en cliquant sur l'**icône à trois points** {{< seatable-icon icon="dtable-icon-more-level" >}} dans le coin supérieur droit.
2. Sélectionnez l'option **Intégration de tiers**.

![Intégration de fournisseurs tiers via les options de base étendues](images/Integration-von-Drittanbietern-ueber-die-erweiterten-Base-Optionen.png)

4. Cliquez sur **Ajouter un compte de messagerie**.
5. Choisissez comme fournisseur de services **Fournisseur de messagerie générique**.
6. Saisissez les informations suivantes :
    - **Nom du compte**: un nom quelconque pour le compte, par exemple 'Gmail'.
    - **Serveur SMTP**: 'smtp.gmail.com'.
    - **Port SMTP**: '587
    - **Nom d'utilisateur**: votre adresse Gmail, par exemple 'seatable@gmail.com'.
    - **Mot de passe**: le mot de passe de l'application généré dans le cache

![Configurer Gmail avec le mot de passe de l'application pour envoyer des e-mails depuis une base SeaTable](images/ThirdPartyIntegration_Gmail.png)

## Authentification via OAuth 2.0

OAuth 2.0, abréviation de Open Authorization 2.0, est un protocole ouvert qui permet aux applications (web) d'accéder de manière sécurisée aux comptes utilisateurs d'autres applications. Ainsi, un utilisateur peut utiliser les ressources ou les services d'une autre application à partir d'une application, par exemple envoyer des e-mails via Gmail à partir de SeaTable.

Pour que SeaTable puisse accéder à un compte Gmail via OAuth 2.0, vous devez créer un identifiant et une clé client dans la [Cloud Console de Google](<a href=) et les enregistrer dans SeaTable.

### Création des données d'accès dans la Google Cloud Console

En tant que plateforme pour les développeurs, la Cloud Console peut sembler confuse pour les utilisateurs ordinaires. Ne vous laissez pas impressionner. Grâce aux instructions pas à pas suivantes, la configuration est à la portée de tous.

1. Ouvrez la [console Google Cloud](https://console.developers.google.com/) et connectez-vous à votre **compte Google** lorsque vous y êtes invité.
2. Créez d'abord un nouveau projet. Tous les réglages expliqués ci-dessous seront effectués dans celui-ci. Saisissez un nom de projet (par ex. 'SeaTable') et choisissez l'emplacement. (Si aucune organisation n'est définie, conservez "Aucune organisation").
3. Permettez au projet créé d'utiliser l'API Gmail. Pour ce faire, cliquez avec la souris dans le champ de recherche en haut de l'écran, saisissez "Gmail API" et cliquez ensuite sur le résultat de recherche correspondant. Activez l'API Google.
4. Toutes les autres étapes se font dans la **Google Auth Platform**. Cliquez sur l'icône sandwich dans le coin supérieur gauche, puis sélectionnez "Tous les produits" dans la rubrique "Solutions". Sur la page des produits, cliquez sur "Google Auth Platform".

![Naviguer vers la plateforme Google Auth dans Google Cloud Console](images/GoogleAuthPlatform.png)

6. Effectuez les **configurations nécessaires** sur Google Auth Platform : Saisissez un nom d'application, une adresse e-mail d'assistance et une adresse e-mail de contact (par exemple votre adresse Gmail). Sélectionnez "Externe" comme groupe cible. Acceptez les conditions d'utilisation et terminez la configuration.
7. Cliquez sur **"Groupe cible"** dans la navigation latérale de Google Auth Platform **.** Ajoutez votre adresse e-mail Google en tant qu'utilisateur test.
8. Dans la navigation latérale de Google Auth Platform, cliquez sur **"Clients"** et créez un client OAuth 2.0. Sélectionnez "Application web" comme type d'application pour le client OAuth et saisissez un nom (par ex. 'SeaTable'). Sautez les "Sources JavaScript autorisées" et insérez l'URI suivant comme "URI de redirection autorisée" :

    ```
    https://cloud.seatable.io/oauth/third-party-email-accounts/callback/
    ```

    Si vous n'utilisez pas SeaTable Cloud, remplacez cloud.seatable.io par le nom d'hôte de votre instance SeaTable. Faites défiler jusqu'au bas de la page et confirmez la création du client OAuth.

![Un client OAuth 2.0 configuré dans Google Cloud Console](images/Configured_OAuth_Client_GoogleCloudConsole.png)

10. Le client nouvellement créé est maintenant affiché dans la liste des clients OAuth 2.0. Les paramètres du client peuvent être affichés en cliquant sur son nom. L'ID et la clé du client affichés sont essentiels pour la configuration suivante dans SeaTable.

Si vous avez fait un faux clic pendant la configuration et que vous ne savez plus où vous êtes, cliquez sur l'icône sandwich en haut à droite. De là, vous pouvez à nouveau naviguer vers Google Auth Platform.

### Création d'un compte e-mail dans SeaTable

Vous devez maintenant ajouter votre compte Gmail en tant que fournisseur tiers dans votre base SeaTable. Pour cela, il faut suivre les étapes suivantes :

1. Ouvrez les options avancées de la base en cliquant sur l'**icône à trois points** {{< seatable-icon icon="dtable-icon-more-level" >}} dans le coin supérieur droit.
2. Sélectionnez l'option **Intégration de tiers**.
3. Cliquez sur **Ajouter un compte de messagerie**.
4. Sélectionnez **Gmail** comme fournisseur de services.
5. Saisissez les informations suivantes :

    - **Nom du compte**: un nom quelconque pour le compte, par exemple 'Gmail'.
    - **Nom d'utilisateur**: 'me
    - **ID client**: la clé client du client OAuth créé
    - **Clé client**: la clé client du client OAuth créé

6. Confirmez la création du compte e-mail avec l'authentification OAuth2.
7. Connectez-vous maintenant à votre compte Google dans la boîte de dialogue qui s'ouvre.
8. Cliquez sur "Continuer" lorsqu'il vous est indiqué que cette application n'a pas été vérifiée et autorisez l'accès au compte Google.

## Envoyer des e-mails par automatisation

Ensuite, vous pouvez utiliser le compte e-mail créé dans votre SeaTable Base pour envoyer des e-mails par automatisation ou [par bouton]({{< relref "help/base-editor/schaltflaechen/eine-e-mail-per-schaltflaeche-verschicken" >}}).

Si vous souhaitez en savoir plus sur cette automatisation utile, lisez l'article [Envoi d'e-mails par automatisation]({{< relref "help/base-editor/automationen/beispiel-e-mail-versand-per-automation" >}}).
