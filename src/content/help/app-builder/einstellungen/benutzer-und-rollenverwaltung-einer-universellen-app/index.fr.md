---
title: "Gestion des utilisateurs et des rôles d'une application"
date: 2023-05-02
lastmod: '2024-12-13'
categories:
    - 'universelle-apps'
author: 'nsc2'
url: '/fr/aide/gestion-utilisateurs-et-roles-app-universelle'
aliases:
    - '/fr/aide/benutzer-und-rollenverwaltung-einer-universellen-app'
seo:
    title: 'Gestion des utilisateurs et rôles dans SeaTable Apps'
    description: 'Ajoutez des utilisateurs, définissez des rôles et créez des liens d’invitation pour gérer les droits dans les applications de SeaTable.'
---

Qu'il s'agisse d'ajouter de **nouveaux utilisateurs**, d'attribuer des **rôles** ou de créer des **liens d'invitation** – vous pouvez effectuer diverses tâches administratives dans la gestion des utilisateurs et des rôles d'une application. Vous accédez à la **gestion des utilisateurs et des rôles** via le mode d'édition de votre application.

{{< warning  headline="Autorisation requise dans le groupe"  text="Pour pouvoir modifier une application, vous devez être **propriétaire** ou **administrateur du groupe** dans lequel se trouve la **base** sous-jacente. Les simples **membres du groupe** peuvent uniquement consulter et utiliser les applications." />}}

## Gestion des utilisateurs et des rôles de l'application

1. Ouvrez une **base** à laquelle vous avez déjà ajouté une application.
2. Cliquez sur **Apps** dans l'en-tête de la base.
   ![Cliquez sur Apps dans l'en-tête de la base](images/click-apps-in-the-base-header.jpg)
3. Passez la souris sur l'application et cliquez sur l'**icône en forme de crayon** {{< seatable-icon icon="dtable-icon-rename" >}}.
   ![Cliquez sur l'icône en forme de crayon](images/add-page-to-universal-app-1.png)
4. Ouvrez la **gestion des utilisateurs et des rôles** en haut à gauche de la page.
   ![Icône de la gestion des utilisateurs et des rôles](images/Symbol-fuer-Benutzer-und-Rollenverwaltung.png) 
5. Effectuez les **réglages** souhaités.

## Les réglages en détail

### Utilisateurs

Dans la première section, vous trouverez un aperçu de tous les **utilisateurs** qui ont accès à votre application. Vous y trouverez également le **rôle** et le **statut** de chaque utilisateur.

![Aperçu de l'onglet Utilisateurs de la gestion des utilisateurs et des rôles d'une application](images/user-and-role-management-overview-1.png)

Dans cette section, vous disposez en outre de diverses possibilités pour **gérer les utilisateurs actuels** de votre application.

Utilisez la **fonction de recherche** pour trouver un utilisateur spécifique. Cette fonction peut être particulièrement utile si votre application compte un grand nombre d'utilisateurs.

![Fonction de recherche pour les utilisateurs de l'application](images/search-function-app-users.png)

Pour ajouter un utilisateur à l'application, cliquez sur **Importer des utilisateurs**, recherchez-le dans le champ de saisie, puis attribuez-lui un rôle.

![Cliquez sur Importer des utilisateurs](images/import-user-to-app.jpg)

![Importer un utilisateur dans votre application](images/import-users-to-app.png)

Cliquez sur **Synchroniser les utilisateurs avec la base** pour recenser automatiquement les **utilisateurs de l'application** dans un tableau de votre base.

![Cliquez sur Synchroniser les utilisateurs avec la base](images/click-sync-users-to-base-1.jpg) ![Tableau dans lequel les utilisateurs de l'application sont automatiquement recensés](images/table-with-app-users.png)

Si vous ajoutez d'autres utilisateurs de cette manière à l'avenir, vous pouvez toujours cliquer à nouveau sur **Synchroniser les utilisateurs avec la base** pour ajouter les **nouveaux utilisateurs** au tableau.

![Si vous ajoutez d'autres utilisateurs à votre application à l'avenir, ...](images/if-you-add-more-users-to-your-app.png)

![... vous pouvez toujours cliquer à nouveau sur Synchroniser les utilisateurs avec la base pour ajouter automatiquement les nouveaux utilisateurs au tableau.](images/added-imported-app-users-to-table.png)

Pour **supprimer** un utilisateur de l'application, il suffit de cliquer sur l'**icône X** qui se trouve à droite du statut de l'utilisateur concerné.

![Supprimer un utilisateur](images/delete-user.jpg)

En cliquant sur les **icônes en forme de crayon** {{< seatable-icon icon="dtable-icon-rename" >}} que vous trouverez pour chaque utilisateur, vous pouvez modifier son **rôle** et son **statut**.

{{< warning  headline="Remarque importante"  text="Veuillez noter que l'**utilisateur** qui a ajouté l'application à la base est automatiquement enregistré comme **admin**. Ni le rôle ni le statut de cet utilisateur ne peuvent être modifiés, et cet utilisateur ne peut **pas** non plus être supprimé de l'application." />}}

![Icônes d'édition pour chaque utilisateur](images/edit-icons-users.jpg)

Pour le **rôle d'un utilisateur**, le menu déroulant vous propose tous les rôles que vous pouvez définir dans la section suivante de la gestion des utilisateurs et des rôles.

![Sélection du rôle d'un utilisateur](images/select-role-of-user.png)

Le **statut** d'un utilisateur peut être défini sur **Actif** ou **Inactif**. Alors que les utilisateurs **actifs** ont accès à l'application et à son contenu, les utilisateurs **inactifs** perdent cet accès.

![Modification du statut d'un utilisateur de l'application](images/edit-status-of-app-user.png)

Les utilisateurs qui n'ont pas accès à votre application voient ce message :

![Accès à l'application refusé aux utilisateurs inactifs](images/no-permission-for-inactive-users.png)

### Rôles

Dans cette section, vous pouvez définir un nombre illimité de **rôles** que vous pourrez attribuer aux différents utilisateurs de l'application dans la section précédente.

![Définition de différents rôles pour les utilisateurs de l'application](images/define-roles-for-app-users.jpg)

Ici, vous définissez d'abord uniquement les **noms** des rôles. Vous pouvez définir individuellement pour chaque page de l'application les **autorisations** dont disposent les utilisateurs selon leur rôle.

[Apprenez-en plus sur les autorisations de pages ici.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

### Lien d'invitation

Dans la troisième section de la gestion des utilisateurs et des rôles, vous pouvez générer un **lien d'invitation** individuel pour l'application.

Définissez d'abord le **rôle** des utilisateurs qui accéderont à l'application à l'aide du lien d'invitation.

![Sélection du rôle qui sera attribué aux utilisateurs accédant à l'application à l'aide du lien d'invitation](images/select-role-for-invite-link.png)

Vous avez ensuite la possibilité de définir un **mot de passe** qui doit être saisi après l'ouverture du lien d'invitation pour accéder à l'application.

![Ajouter un mot de passe au lien d'invitation](images/add-password-protection.png)

En option, vous pouvez également ajouter au lien d'invitation un **délai d'expiration** automatique qui détermine sa durée de validité.

![Ajouter un délai d'expiration automatique au lien d'invitation](images/add-auto-expiration.png)

Cliquez sur **Générer** pour créer le lien d'invitation. Le lien s'affiche ensuite en dessous et vous avez la possibilité de le **copier** ou de le **supprimer**.

![Lien d'invitation généré avec les options disponibles pour le copier et le supprimer](images/copy-and-delete-link-universal-app.png)

Vous avez également la possibilité de générer un **code QR** pour ouvrir et partager l'application.

![Affichage du code QR pour ouvrir et partager l'application](images/show-qr-code-universal-app.png)

Scannez le **code QR** affiché pour ouvrir votre application, ou partagez-le avec d'autres utilisateurs pour leur donner **accès** à votre application.

![Code QR pour ouvrir et partager l'application](images/qr-code-to-share-universal-app.png)
