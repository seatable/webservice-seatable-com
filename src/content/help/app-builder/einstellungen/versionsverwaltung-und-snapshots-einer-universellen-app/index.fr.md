---
title: "Gestion des versions et des instantanés d'une application"
date: 2023-11-29
lastmod: '2024-02-16'
categories:
    - 'universelle-apps'
author: 'kgr'
url: '/fr/aide/gestion-versions-et-snapshots-app-universelle'
aliases:
    - '/fr/aide/versionsverwaltung-und-snapshots-einer-universellen-app'
seo:
    title: 'Gestion de versions et snapshots dans l’app'
    description: 'Apprenez à sauvegarder, consulter, restaurer et gérer des versions de votre app grâce aux snapshots pour sécuriser vos modifications.'
---

Les **snapshots** permettent de sauvegarder la version actuelle d'une application. Vous pouvez **créer**, **afficher**, **restaurer** et **supprimer** des snapshots dans la gestion des versions de l'App Builder. Vous pouvez également noter **des notes** sur les différents snapshots afin de conserver des informations sur une version.

{{< warning  headline="Autorisation requise dans le groupe"  text="Pour pouvoir utiliser les App Snapshots, vous devez être **propriétaire** ou **administrateur du groupe** dans lequel se trouve la **base** sous-jacente. **Les** simples **membres du groupe** n'ont pas accès à la gestion des versions." />}}

## Quand les apps snapshots sont utiles

Les App Snapshots sont des **instantanés** de l'état d'une application et fonctionnent de manière similaire aux [Base Snapshots]({{< relref "help/base-editor/historie-und-versionen/speichern-der-aktuellen-base-als-snapshot" >}}). Les apps snapshots vous permettent de sauvegarder la version actuelle d'une application, ce qui peut être utile si vous effectuez des modifications importantes et souhaitez éventuellement restaurer un état antérieur.

{{< warning  headline="Attention à la perte de données"  text="Contrairement aux Base Snapshots, les App Snapshots ne sauvegardent **pas les enregistrements**, mais uniquement la **structure** et **les paramètres** de l'app. Cela signifie que si vous modifiez ou supprimez certaines entrées de la base sous-jacente via l'app, vous ne pourrez pas les restaurer via les apps snapshots." />}}

### Ce que stocke un snapshot d'application

Un snapshot d'application enregistre les éléments et paramètres suivants :

- [Paramètres]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}}) tels que **le nom**, **l'icône** et **le schéma de couleurs** de l'application
- [Pages et dossiers]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) de l'application
- Paramètres et [autorisations]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) pour les différentes pages

### Ce qu'un snapshot d'application ne sauvegarde pas

Un snapshot d'application n'enregistre pas :

- l'**URL personnalisée** d'une application
- les **données** de la base sous-jacente
- les **commentaires** sur les différents enregistrements
- les [rôles des utilisateurs et les liens d'invitation]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}) de l'application

## Créer un snapshot de l'application

1. Ouvrez une **application** en [mode édition]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}).

![App Builder en mode édition avec liste d’apps ouverte](images/Apps-bearbeiten.png)

3. Cliquez en haut à gauche de la page sur {{< seatable-icon icon="dtable-icon-history" >}} **Gestion des versions**.

![Gestion des versions d’une application avec liste des snapshots existants](images/Version-management-in-Universal-App-Builder.png)

5. Une fenêtre s'ouvre. Créez-y un **nouveau snapshot**.
6. En option, vous pouvez ajouter une **note** au snapshot.
7. Confirmez en cliquant sur **Envoyer**.

![Création d’un nouveau snapshot d’app dans la gestion des versions avec remarque optionnelle](images/Version-management-in-Universal-Apps.gif)

{{< warning  headline="Numérotation des versions"  text="Pour chaque snapshot, l'**heure** exacte **de création** et un **numéro de version** sont enregistrés. Ne vous étonnez pas si vos snapshots ne reçoivent pas de numéros consécutifs (1, 2, 3 ...). SeaTable compte chaque modification que vous effectuez dans une application comme une version à part entière. Il peut donc rapidement y avoir des dizaines de versions entre deux snapshots." />}}

Une fois que vous avez créé un snapshot, vous avez le choix entre quatre opérations :

- **Voir la version**
- **Restaurer la version**
- **Remarque**
- **Supprimer la version**

## Voir l'instantané de l'application

Avant de restaurer un snapshot et de revenir précipitamment à une autre version, vous devriez d'abord regarder cette version. Pour cela, suivez la même procédure que ci-dessus : Cliquez sur les **trois points** à l'extrémité droite d'un snapshot et sélectionnez l'opération **Voir la version** dans le menu déroulant.

![Aperçu d’une version enregistrée de l’application dans l’App Builder](images/Preview-version-of-app-snapshot.png)

## Restaurer un snapshot d'application

Pour restaurer un snapshot d'application, cliquez sur les **trois points** et sélectionnez l'opération correspondante dans le menu déroulant.

![Boîte de dialogue pour restaurer un snapshot d’app comme version actuelle](images/Restore-version-of-app-snapshot.png)

{{< warning  headline="Attention"  text="La restauration d'un snapshot dans l'App Builder fonctionne différemment de celle de la base, où le snapshot est restauré dans une nouvelle base et la version actuelle est conservée. **En revanche, dans l'App Builder, la version actuelle est abandonnée lorsque vous restaurez un snapshot.**" />}}

Dès que vous restaurez un instantané, l'application revient à l'état de la mémoire de cette version antérieure. Toutes les **modifications** que vous avez apportées depuis aux pages, dossiers et paramètres de l'application **seront perdues**. C'est pourquoi il est conseillé, avant de restaurer un snapshot, d'enregistrer également la version actuelle dans un snapshot. Vous pouvez ainsi passer d'une version à l'autre.

## Modifier une remarque

Si vous souhaitez ajouter, modifier ou supprimer ultérieurement la note d'une version, vous pouvez le faire à tout moment. Vous ouvrez le champ de texte correspondant en cliquant sur les **trois points** à l'extrémité droite d'un snapshot et en sélectionnant **Remarque** dans le menu déroulant. Enregistrez vos modifications en cliquant sur **Envoyer**.

![Boîte de dialogue pour modifier ou ajouter une remarque à un snapshot d’app](images/Modify-notes-of-app-snapshot.png)

## Supprimer un snapshot d'application

Vous pouvez à tout moment supprimer un snapshot dont vous n'avez plus besoin. Cliquez sur les **trois points** à l'extrémité droite d'un snapshot et sélectionnez l'opération **Supprimer la version** dans le menu déroulant.

![Boîte de dialogue de confirmation pour supprimer définitivement un snapshot d’app](images/Delete-version-of-app-snapshot.png)

{{< warning  headline="Attention"  text="La suppression d'un App Snapshot est définitive. L'état de la mémoire de la version précédente est irrémédiablement perdu et ne peut pas être restauré." />}}
