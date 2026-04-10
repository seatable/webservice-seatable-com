---
title: "Modifier les paramètres globaux d'une application"
date: 2023-05-03
lastmod: '2025-07-03'
categories:
    - 'universelle-apps'
author: 'kgr'
url: '/fr/aide/einstellungen-einer-universellen-app-aendern'
aliases:
    - '/fr/aide/einstellungen-einer-universellen-app-aendern'
seo:
    title: 'Modifier les réglages globaux d’une app'
    description: 'Découvrez comment ajuster les paramètres globaux, URLs et droits d’accès dans une SeaTable App.'
---

Au sein d'une **application**, il est possible de procéder en quelques clics à différents **réglages globaux** qui concernent la configuration et l'apparence de l'ensemble de l'application.

## Modifier les paramètres d'une application

1. Ouvrez une **base** dans laquelle vous souhaitez modifier une application existante.
2. Cliquez sur **Apps** dans l'en-tête de la base.
![Cliquez sur Apps dans l'en-tête de base](images/click-apps-in-the-base-header.jpg)
3. Passez la souris sur l'application et cliquez sur l'**icône du crayon** {{< seatable-icon icon="dtable-icon-rename" >}}.
![Modifier les apps](images/Apps-bearbeiten.png)
4. Cliquez sur l'**icône en forme d'engrenage** en haut à gauche de la page.
![Icône en forme de roue dentée pour les paramètres de l'application](images/Zahnrad-Symbol-fuer-App-Einstellungen.png)
5. Effectuez les ajustements souhaités dans les **paramètres** de l'application.

{{< warning  headline="Autorisation requise dans le groupe"  text="Pour pouvoir modifier une app, vous devez être **propriétaire** ou **administrateur du groupe** dans lequel se trouve la **base** sous-jacente. **Les** simples **membres du groupe** peuvent uniquement consulter et utiliser les apps." />}}

## Modifier le nom de l'application

Dans la première section des paramètres de l'application, vous pouvez adapter le **nom** de l'application et l'enregistrer en cliquant sur **Envoyer**.

![Changer le nom de l'application](images/Change-app-name.png)

## URL personnalisée

Dans la deuxième section, vous pouvez personnaliser une partie de l'**URL** qui vous permettra d'accéder à votre application et d'y créer un lien. Il vous suffit de saisir l'URL de votre choix dans le **champ de texte** et de respecter les **exigences** ci-dessous. Vous pouvez ensuite **enregistrer** et **copier** l'URL saisie.

![Modifier l'URL personnalisée](images/Edit-custom-URL.png)

**Exigences :** La partie personnalisée de l'URL doit comporter entre 5 et 30 caractères et ne peut contenir que **des lettres (a-z), des chiffres (0-9) et des traits d'union**.

## Afficher ou masquer la navigation

Dans la troisième section, vous pouvez décider si la **barre de navigation** doit être affichée ou masquée par défaut à l'ouverture de l'application. La barre de navigation est la zone située sur le bord gauche par laquelle tous les utilisateurs accèdent aux [pages et aux dossiers]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}}) de l'application.

![Hide app navigation by default](images/Hide-app-navigation-by-default.png)

Il s'agit uniquement d'un réglage par défaut lors de la première ouverture de l'application. Chaque utilisateur de l'application peut afficher ou masquer la barre de navigation à sa guise à l'aide des **icônes** ou **des combinaisons de touches** correspondantes.

![Afficher ou masquer la navigation](images/Hide-and-show-navigation.gif)

## Paramètres de collaboration

Dans la quatrième section, vous pouvez **activer le chargement de tous collaborateurs** si votre liste de collaborateurs doit être visible dans l'application pour tous les utilisateurs. Vous pouvez alors ajouter des personnes dans [les colonnes des collaborateurs]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte" >}}) ou les ajouter aux [commentaires]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}). Si vous souhaitez que vos collaborateurs restent invisibles aux autres, vous devez désactiver cette fonction.

![Charger la liste des collaborateurs dans les applications](images/Load-collaborator-list-in-apps.png)

En outre, vous pouvez définir si vous souhaitez **charger les commentaires de la base sous-jacente**. Par défaut, seuls les commentaires rédigés dans l'application sont visibles dans l'application. Si vous ne souhaitez pas que les utilisateurs de l'application voient les commentaires de la base, vous devez désactiver cette fonction.

{{< warning type="warning" headline="Les commentaires sont possibles sur ces types de pages" text="La fonction de commentaires de l'app est actuellement disponible sur les pages Tableau, Galerie, Kanban, Calendrier et Ligne de temps." />}}

## Gestion des données volumineuses

Cette section n'est pertinente que si vous avez activé la [mémoire Big Data]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) dans votre base. Les applications peuvent alors accéder aux données dans la mémoire Big Data et y enregistrer directement les entrées créées via l'application. Par défaut, les nouvelles entrées sont toutefois enregistrées dans la base. Pour définir la mémoire Big Data comme **emplacement de stockage des nouvelles entrées**, il suffit d'activer le curseur. Comme le montre la capture d'écran, vous pouvez définir précisément pour chaque tableau si les nouvelles lignes doivent être écrites dans la base (case vide) ou dans la mémoire Big Data (case cochée).

![Gestion des grandes données dans les applications](images/Big-data-management-in-apps.png)

## Accès ouvert

Dans la dernière section, vous pouvez définir un accès ouvert pour votre application. Donc, vous pouvez **autoriser les utilisateurs non connectés** à votre application. Ensuite, toute personne qui consulte le lien puisse voir les données (mais pas les modifier).

![Accès ouvert à une application](images/Open-access-to-an-app.png)

Vous pouvez également **autoriser le téléchargement de fichiers et d'images**. Si vous ne souhaitez pas que tout le monde puisse utiliser votre application sans restriction, vous pouvez **activer la protection par mot de passe**. Lorsque les utilisateurs accèdent à l'URL de l'application, ils doivent alors saisir le mot de passe correct pour pouvoir voir les données.

Vous pouvez également activer que **chaque utilisateur connecté qui utilise l'application est automatiquement enregistré en tant qu'utilisateur d'application**. Pour ce faire, vous définissez le **rôle** qui est attribué aux utilisateurs lors de l'enregistrement. En fonction des [autorisations]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) sur les différentes pages, les utilisateurs ayant ce rôle peuvent également ajouter, modifier ou supprimer des lignes.

## Modifier les paramètres des pages individuelles

Les paramètres mentionnés jusqu'ici concernent l'**ensemble** d'une **application**. Si vous souhaitez modifier les paramètres d'une **seule page**, cliquez dans la navigation sur le **symbole de la roue dentée** {{< seatable-icon icon="dtable-icon-set-up" >}} de la page correspondante.

![Ouvrir les paramètres de la page](images/page-permissions-universal-app.png)
