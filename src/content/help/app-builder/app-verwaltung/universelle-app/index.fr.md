---
title: 'Les applications de SeaTable'
date: 2023-05-04
lastmod: '2026-11-17'
categories:
    - 'apps'
author: 'nsc2'
url: '/fr/aide/applications-seatable'
aliases:
    - '/fr/aide/universelle-app'
    - '/fr/aide/app-universelle-seatable'
    - '/fr/aide/quelles-apps-existent'
    - '/fr/aide/welche-apps-gibt-es'
seo:
    title: 'SeaTable Apps : mode d’emploi complet'
    description: 'Découvrez SeaTable Apps : pages, tableaux de bord, droits, gestion d’utilisateurs, partage, duplication et conseils design.'
star: true
weight: 1
---

Les **applications** de SeaTable sont des **frontends** ou applications web individuels destinés à des groupes d'utilisateurs spécifiques ayant des besoins d'information différents (par ex. collaborateurs, chefs de service, directeurs). Le **backend** d'une application est toujours une [base]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}). Vous pouvez créer autant d'applications que vous le souhaitez pour chaque base. En règle générale : une application par groupe d'utilisateurs et par cas d'usage.

## Comment fonctionnent les applications dans SeaTable ?

Pour créer des applications, il existe ce qu'on appelle l'**App Builder**, dans lequel vous pouvez créer différentes interfaces utilisateur et effectuer de nombreux réglages. Vous pouvez laisser libre cours à votre créativité et ajouter à votre application des pages entièrement personnalisées basées sur HTML, JavaScript et CSS (avec ou sans IA). 

L'App Builder propose en outre plusieurs [types de pages]({{< relref "help/app-builder/seitentypen-in-universellen-apps" >}}) prédéfinis, qui vous permettent notamment de présenter vos données sous forme de **tableaux**, de **galeries** ou de **calendriers** et de les partager avec d'autres utilisateurs. Vous pouvez également créer des **formulaires** pour la saisie de données et des **tableaux de bord** avec des statistiques pertinentes. 

Grâce aux **autorisations de page**, vous pouvez définir précisément qui peut voir les pages et ajouter, modifier ou supprimer des lignes. Grâce à l'accès public aux applications, vous pouvez également rendre vos données accessibles à des **utilisateurs externes sans compte SeaTable**.

{{< warning  headline="Autorisation requise dans le groupe"  text="Pour pouvoir créer, modifier, copier ou supprimer une app, vous devez être **le propriétaire** ou **l'administrateur du groupe** dans lequel se trouve la **base** sous-jacente. **Les** simples **membres d'un groupe** peuvent uniquement consulter et utiliser des apps existantes." />}}

## Créer l'application

Pour pouvoir utiliser une application dans votre base, vous devez d'abord l'**ajouter** à votre base.

![Créer l'application](images/universal-app-preview.png)

[Apprenez ici comment ajouter une application à votre base.]({{< relref "help/app-builder/app-verwaltung/apps-zu-einer-base-hinzufuegen" >}})

## Conception de l'application

Après avoir créé votre application avec succès, vous pouvez commencer à la concevoir. Veillez à toujours utiliser l'**icône du crayon** {{< seatable-icon icon="dtable-icon-rename" >}} pour accéder au [mode d'édition]({{< relref "help/app-builder/app-verwaltung/apps-bearbeiten" >}}) de l'application.

![Modifier les apps](images/Apps-bearbeiten.png)

Une application se compose de plusieurs **pages** que vous pouvez regrouper dans des **dossiers**.

[Apprenez ici comment ajouter de nouvelles pages et de nouveaux dossiers à votre application]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}).

Afin de présenter les données de manière attrayante dans votre base, l'application propose un grand nombre de types de pages avec différents éléments de présentation.

## Aperçu d'une application

Lors de la conception d'une application, vous souhaitez certainement tester de temps en temps l'aspect de l'application pour les utilisateurs. Pour cela, il vous suffit d'[afficher]({{< relref "help/app-builder/app-verwaltung/die-vorschau-einer-app-anzeigen-lassen" >}}) en mode édition.

## Modifier les paramètres d'une application

Au sein d'une application, vous pouvez effectuer différents **réglages globaux**. Vous pouvez par exemple modifier le **nom**, la **couleur** et l'**URL** de votre app. Vous pouvez effectuer les adaptations souhaitées en quelques clics via les **paramètres de l'application**.

![Ouvrir les paramètres de l'application](images/global-settings-universal-app.png)

[En savoir plus sur les paramètres globaux de l'application ici.]({{< relref "help/app-builder/einstellungen/einstellungen-einer-universellen-app-aendern" >}})

## Enregistrer les versions d'une application

La **gestion des versions de** chaque app vous offre la possibilité de sauvegarder des instantanés de la structure d'une app. Vous apprendrez [ici]({{< relref "help/app-builder/einstellungen/versionsverwaltung-und-snapshots-einer-universellen-app" >}}) comment créer un **app snapshot**. Notez ce qu'un app snapshot enregistre - et ce qu'il n'enregistre pas.

## Autorisations de pages dans une application

Pour contrôler précisément l'accès à vos données, vous pouvez définir **des autorisations de page individuelles** pour **chaque page** que vous avez ajoutée à une application. L'édition des autorisations de page s'effectue toujours via les **paramètres de page**, auxquels vous accédez via l'icône en forme de roue dentée {{< seatable-icon icon="dtable-icon-set-up" >}}.

![Ouvrir les paramètres de la page](images/page-permissions-universal-app.png)

[Apprenez-en plus sur les différentes autorisations de pages dans l'application ici.]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}})

## Gestion des utilisateurs et des rôles d'une application

Ajouter de nouveaux utilisateurs, créer et attribuer des rôles - dans la **gestion des utilisateurs et des rôles** d'une application, vous pouvez effectuer diverses activités administratives.

![Gestion des utilisateurs et des rôles d'une application](images/open-user-and-role-management-1.png)

[Apprenez-en plus sur la gestion des utilisateurs et des rôles de l'application ici.]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}})

## Partager une application

Vous pouvez également partager une application avec d'autres utilisateurs via la [gestion des utilisateurs et des rôles]({{< relref "help/app-builder/einstellungen/benutzer-und-rollenverwaltung-einer-universellen-app" >}}). Pour ce faire, il vous suffit de générer un **lien d'invitation** individuel ou d'utiliser un **code QR**.

## Copier une application

Avez-vous créé une application que vous aimeriez utiliser sous une forme similaire pour un autre groupe d’utilisateurs ? Ensuite, copiez simplement l’application existante et personnalisez la copie comme vous le souhaitez. Pour savoir comment copier une application, [cliquez ici]({{< relref "help/app-builder/app-verwaltung/apps-kopieren" >}}).

## Désactiver une application

Si vous avez créé une application que vous souhaitez désactiver temporairement, vous pouvez la désactiver en quelques clics pour révoquer l’accès à tous les groupes d’utilisateurs. Pour savoir comment procéder, [cliquez ici]({{< relref "help/app-builder/app-verwaltung/apps-zeitweise-deaktivieren" >}}).

## Supprimer une application

Vous pouvez **supprimer** à tout moment une application dont vous n’avez plus besoin. Veuillez noter les conséquences de la suppression.

[Apprenez-en plus sur la suppression d'une application ici.]({{< relref "help/app-builder/app-verwaltung/apps-loeschen" >}})

## Pas de travail collaboratif dans les apps

Alors que l'application présente de nombreux avantages par rapport au [travail dans la base]({{< relref "help/startseite/bases/allgemeines-zu-bases" >}}), il y a une grande différence si vous souhaitez travailler en équipe sur les données. Dans une base, toute modification effectuée par d'autres utilisateurs vous est immédiatement signalée. Les entrées changent en temps réel. Dans l'application, ce type de travail collaboratif n'est pas pris en charge.

## Commentaires dans les apps

Vous avez néanmoins la possibilité de communiquer avec d'autres membres de l'équipe, même dans une application. Utilisez pour cela la [fonction de commentaire]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}) que vous connaissez déjà sous la même forme dans la base. Consignez vos commentaires ou des informations supplémentaires sur les jeux de données pour les autres utilisateurs de l'app et menez des discussions sur place.

![Fonction de commentaire dans les applications](images/Kommentarfunktion-in-Universellen-Apps.png)

{{< warning  headline="Bon à savoir"  text="Les commentaires dans l'app sont complètement **indépendants** des commentaires dans la base. Cela signifie que chaque commentaire dans l'app n'est visible que là où il a été posté - pas dans la base ni dans d'autres apps, même s'il s'agit du même ensemble de données." />}}
