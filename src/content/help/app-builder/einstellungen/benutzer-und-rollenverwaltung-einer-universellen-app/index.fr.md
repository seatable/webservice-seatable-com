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

Qu'il s'agisse d'ajouter **de nouveaux utilisateurs**, d'attribuer **des rôles** ou de créer des **liens d'invitation**, vous pouvez effectuer diverses activités administratives dans la gestion des utilisateurs et des rôles d'une application. Vous accédez à la **gestion des utilisateurs et des rôles** via le mode d'édition de votre application.

{{< warning  headline="Autorisation requise dans le groupe"  text="Pour pouvoir modifier une app, vous devez être **propriétaire** ou **administrateur du groupe** dans lequel se trouve la **base** sous-jacente. **Les** simples **membres du groupe** peuvent uniquement consulter et utiliser les apps." />}}

## Gestion des utilisateurs et des rôles de l'application

1. Ouvrez une **base** à laquelle vous avez déjà ajouté une application.
2. Cliquez sur **Apps** dans l'en-tête de la base.

![Cliquez sur Apps dans l'en-tête de base](images/click-apps-in-the-base-header.jpg)

4. Passez la souris sur l'application et cliquez sur l'**icône du crayon** {{< seatable-icon icon="dtable-icon-rename" >}}.

![Cliquez sur l'icône d'édition](images/add-page-to-universal-app-1.png)

6. Ouvrez la **gestion des utilisateurs et des rôles** en haut à gauche de la page.

![Icône de gestion des utilisateurs et des rôles](images/Symbol-fuer-Benutzer-und-Rollenverwaltung.png)

8. Effectuez les **réglages** souhaités.

## Les réglages en détail

### Utilisateur

Dans la première section, vous trouverez un aperçu de tous les **utilisateurs** qui ont accès à votre application. Vous y trouverez également le **rôle** et le **statut** de chaque utilisateur.

![Aperçu de l'onglet Utilisateurs de la gestion des utilisateurs et des rôles d'une application](images/user-and-role-management-overview-1.png)

Dans cette section, vous disposez en outre de diverses possibilités pour **gérer les utilisateurs actuels** de votre application.

Utilisez la **fonction de recherche** pour trouver un utilisateur spécifique. Cette fonction peut être particulièrement utile si le nombre d'utilisateurs de l'application est élevé.

![Fonction de recherche pour les utilisateurs d'apps](images/search-function-app-users.png)

Pour ajouter un utilisateur à l'application, cliquez sur **Importer un utilisateur**, recherchez-le dans le champ de saisie et attribuez-lui un rôle.

![Cliquez sur Importer des utilisateurs ](images/import-user-to-app.jpg)

![Importer un utilisateur dans votre application](images/import-users-to-app.png)

Cliquez sur **Synchroniser les utilisateurs avec la base** pour relever automatiquement les **utilisateurs de l'app** dans un tableau de votre base.

![Cliquez sur Synchroniser les utilisateurs avec la base](images/click-sync-users-to-base-1.jpg)  
![Tableau dans lequel les utilisateurs de l'application sont automatiquement relevés](images/table-with-app-users.png)

Si vous ajoutez d'autres utilisateurs de cette manière à l'avenir, vous pouvez toujours cliquer à nouveau sur **Synchroniser les utilisateurs avec la base** pour ajouter les **nouveaux utilisateurs** au tableau.

![Si vous ajoutez d'autres utilisateurs à votre application à l'avenir, ...](images/if-you-add-more-users-to-your-app.png)

![... vous pouvez toujours cliquer à nouveau sur Synchroniser les utilisateurs avec la base pour ajouter automatiquement les nouveaux utilisateurs au tableau.](images/added-imported-app-users-to-table.png)

Pour **supprimer** un utilisateur de l'application, il suffit de cliquer sur le **symbole X** qui se trouve à droite du statut de l'utilisateur concerné.

![Supprimer un utilisateur](images/delete-user.jpg)

En cliquant sur les **icônes en forme de crayon** {{< seatable-icon icon="dtable-icon-rename" >}}, que vous trouverez pour chaque utilisateur, vous pouvez modifier son **rôle** et **son statut**.

{{< warning  headline="Remarque importante"  text="Veuillez noter que l'**utilisateur** qui a ajouté l'application à la base est automatiquement enregistré comme **admin**. Tant le rôle que le statut de cet utilisateur ne peuvent **pas** être modifiés et l'utilisateur ne peut **pas** non plus être supprimé de l'application." />}}

![Icônes d'édition pour chaque utilisateur ](images/edit-icons-users.jpg)

Pour le **rôle d'un utilisateur**, vous pouvez choisir dans le menu déroulant tous les rôles que vous pouvez définir dans la section suivante de la gestion des utilisateurs et des rôles.

![Sélection du rôle d'un utilisateur ](images/select-role-of-user.png)

Le **statut** d'un utilisateur peut être défini comme **actif** ou **inactif**. Alors que les utilisateurs **actifs** ont accès à l'application et à son contenu, les utilisateurs **inactifs** perdent cet accès.

![Modification du statut d'un utilisateur d'application](images/edit-status-of-app-user.png)

Les utilisateurs qui n'ont pas accès à votre application verront ce message :

![Accès à l'application refusé aux utilisateurs inactifs ](images/no-permission-for-inactive-users.png)

### Rouleaux

Dans cette section, vous pouvez définir un nombre quelconque de **rôles** que vous pourrez attribuer aux différents utilisateurs de l'app dans la section à ce sujet.

![Définition de différents rôles pour les utilisateurs de l'application ](images/define-roles-for-app-users.jpg)

Ici, vous définissez d'abord uniquement les **noms** des rôles. Vous pouvez définir individuellement pour chaque page de l'application les **autorisations** dont disposent les utilisateurs avec les différents rôles.

[Apprenez-en plus sur les autorisations de pages ici.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

### Lien d'invitation

Dans la troisième section de la gestion des utilisateurs et des rôles, vous pouvez générer un **lien d'invitation** individuel pour l'application.

Définissez d'abord le **rôle** des utilisateurs qui accèdent à l'application à l'aide du lien d'invitation.

![Sélection du rôle qui sera attribué à l'utilisateur qui utilisera l'application à l'aide du lien d'invitation](images/select-role-for-invite-link.png)

Ensuite, vous avez la possibilité de définir un **mot de passe** qui doit être saisi après l'ouverture du lien d'invitation pour avoir accès à l'application.

![Ajouter un mot de passe au lien d'invitation](images/add-password-protection.png)

En option, vous pouvez également ajouter un **délai d'expiration** automatique au lien d'invitation pour indiquer sa durée de validité.

![Ajouter un délai d'expiration automatique au lien d'invitation ](images/add-auto-expiration.png)

En cliquant sur **Générer**, vous pouvez créer le lien d'invitation. Le lien s'affiche ensuite en bas et vous avez la possibilité de le **copier** ou de le **supprimer**.

![Lien d'invitation généré et options disponibles pour copier et supprimer le lien d'invitation.](images/copy-and-delete-link-universal-app.png)

Vous avez également la possibilité de vous faire générer un **code QR** pour ouvrir et partager l'application.

![Affichage du code QR pour ouvrir et partager l'application](images/show-qr-code-universal-app.png)

Scannez le **code QR** affiché pour ouvrir votre application ou partagez-le avec d'autres utilisateurs pour leur donner **accès** à votre application.

![Code QR pour ouvrir et partager l'application](images/qr-code-to-share-universal-app.png)
