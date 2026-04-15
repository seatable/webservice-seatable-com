---
title: 'Synchroniser les dates dans SeaTable avec Google Agenda'
date: 2026-03-23
lastmod: '2026-03-23'
categories:
    - 'integrationen-innerhalb-von-seatable'
author: 'rdb'
url: '/fr/aide/synchroniser-les-dates-dans-seatable-avec-google-agenda'
seo:
    title: 'Synchroniser les dates dans SeaTable avec Google Agenda'
    description: 'Instructions pas à pas pour synchroniser les dates de SeaTable avec un agenda Google.'
---

Les dates dans une base de SeaTable peuvent être automatiquement synchronisés avec un ou plusieurs **calendriers de Google**. Ainsi, vous avez toujours vos rendez-vous actuels à portée de main dans votre agenda Google sur votre PC et vos appareils mobiles.

Avant de configurer la synchronisation des événements, vous devez configurer le **compte Google** de l'agenda dans lequel vous souhaitez transférer des dates de SeaTable. Cela se fait en deux étapes : Tout d'abord, créez des **informations d'accès OAuth** dans la Console Google Cloud. Ensuite, vous créez un compte tiers dans SeaTable avec les données d'accès et vous le connectez à Google. Grâce à ce guide étape par étape, c'est très facile.

## Création des données d'accès dans la Google Cloud Console

En tant que plateforme destinée aux développeurs, la Google Cloud Console peut sembler confuse aux utilisateurs ordinaires. Ne vous laissez pas impressionner. Grâce aux instructions pas à pas suivantes, vous pourrez la configurer sans vous prendre la tête.

1. Ouvrez la [Google Cloud Console](https://console.cloud.google.com/) et connectez-vous à votre **compte Google** lorsque vous y êtes demandé.
2. Cliquez sur **Sélectionner un projet** en haut à côté du logo Google Cloud et créez un **nouveau projet**. Tous les paramètres expliqués ci-dessous seront définis dans ce dernier.
   ![Sélection de projet dans Google Cloud](images/GoogleConsole_CreateNewProject_723.png)
3. Saisissez un **nom de projet** (par exemple, SeaTable Base XY) et sélectionnez l'**emplacement**. Si aucune organisation n'est définie, conservez "Aucune organisation". Confirmez en cliquant sur **Créer**.
   ![créer un nouveau projet dans Google Cloud Console](images/GoogleConsole_NewProject_723.png)
4. Autorisez le projet créé à utiliser l'API Google Agenda. Pour ce faire, cliquez avec la souris dans le **champ de recherche** en haut de la page, saisissez **Google Calendar API** et cliquez sur le résultat de recherche correspondant. Activez ensuite l'API Google Calendar.
   ![Activer Google Calendar API](images/GoogleConsole_EnableCalendarAPI_722.gif)
5. Cliquez sur l'icône du menu Burger dans le coin supérieur gauche pour afficher la navigation, puis sélectionnez **Tous les produits** dans la section "Solutions". Sur la page du produit, cliquez sur **Google Auth Platform**.
   ![Accéder à la plateforme Google Auth](images/GoogleConsole_SwitchAuthPlatform_722.gif)
6. Effectuez les configurations nécessaires sur Google Auth Platform en cliquant sur **Premières étapes** : indiquez un **nom d'application** et une **adresse e-mail d'assistance** (par exemple votre adresse Gmail). Sélectionnez **Externe** comme groupe cible. Saisissez une **adresse e-mail de contact** (par exemple, votre adresse Gmail). Acceptez les **conditions d'utilisation** et terminez la configuration.
7. Cliquez sur **Groupe cible** dans la navigation latérale de Google Auth Platform. Ajoutez votre adresse e-mail Google comme **utilisateur test**.
8. Cliquez sur **Clients** dans la navigation latérale de Google Auth Platform et créez un client OAuth 2.0. Sélectionnez l'option "Application Web" comme **type d'application** pour le client OAuth et saisissez un **nom** (par exemple SeaTable). Ignorez "Sources JavaScript autorisées" et insérez l'URI suivant comme **URI de redirection autorisée** avant de cliquer sur **Créer** :

    ```
    https://cloud.seatable.io/oauth/google-calendar/callback/
    ```

    Si vous utilisez votre propre système au lieu de SeaTable Cloud, remplacez cloud.seatable.io par le nom d'hôte de votre instance SeaTable.

   ![Créer un client OAuth](images/GoogleConsole_CreateClient_722.gif)

9. Le client nouvellement créé apparaît maintenant dans la liste des clients OAuth 2.0. Les paramètres du client peuvent être affichés en cliquant sur son nom. L'**identifiant client** et la **clé client** affichés sont essentiels pour la configuration suivante dans SeaTable.

{{< warning headline="Pas de panique" text="Si vous vous êtes trompé pendant la configuration et que vous ne savez plus où vous êtes, cliquez sur l'icône du menu Burger en haut à gauche. De là, vous pouvez naviguer à nouveau vers Google Auth Platform en cliquant sur **Récemment consulté**" />}}

## Création d'un compte Google dans SeaTable

Vous devez maintenant ajouter votre compte Google en tant que **compte tiers dans votre base SeaTable**. Pour cela, vous devez suivre les étapes suivantes :

1. Ouvrez les options avancées de la base en cliquant sur l'icône **à trois points** {{< seatable-icon icon="dtable-icon-more-level" >}} dans le coin supérieur droit.
   ![Ouvrir le menu d'intégration tierce](images/third-party-integration.png)
2. Sélectionnez l'option **Intégration tierce**.
3. Cliquez sur **Google Calendar** dans le menu de navigation à gauche, puis sur **Ajouter un compte Google Agenda** en haut à droite.
   ![Ajouter un compte Google Calendar](images/add-google-calendar-account-in-seatable.png)
4. Saisissez les informations suivantes :
    - **Nom du compte** : n'importe quel nom pour le compte, par exemple Google
    - **ID client** : l'ID client du client OAuth créé
    - **Clé client** : la clé client du client OAuth créé
5. Après avoir cliqué sur **Envoyer**, une fenêtre de navigateur s'ouvre. Cliquez sur **Continuer** lorsqu'il vous est indiqué que cette application n'a pas été vérifiée et autorisez l'accès au compte Google.
6. Vous trouverez le compte créé de la même manière sous **Comptes Google Agenda**.

## Transférer automatiquement les dates vers Google Agenda

Une fois le compte Google créé, vous pouvez transférer automatiquement les événements de SeaTable vers votre agenda Google Cloud et les mettre à jour. La configuration du transfert de données de SeaTable vers Google Agenda se fait via une [action]({{< relref "help/base-editor/automationen/automations-aktionen" >}}) appropriée dans une règle d'automatisation.
