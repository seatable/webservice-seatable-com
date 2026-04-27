---
title: 'Supprimer des applications'
date: 2023-05-02
lastmod: '2024-02-16'
categories:
    - 'apps'
author: 'nsc2'
url: '/fr/aide/supprimer-apps-definitivement-seatable'
aliases:
    - '/fr/aide/apps-loeschen'
seo:
    title: 'Supprimez définitivement des apps de votre base SeaTable'
    description: 'Effacez les apps inutiles de votre base SeaTable simplement et rapidement. Seuls admins ou propriétaires le peuvent, les données ne sont pas supprimées.'

---

Vous souhaitez supprimer de votre base une application dont vous n’avez plus besoin ? Aucun problème! Cela peut être fait à tout moment en quelques clics.

{{< warning  headline="Autorisation requise dans le groupe"  text="Pour pouvoir supprimer une application, vous devez être **le propriétaire** ou **l'administrateur du groupe** dans lequel se trouve la **base** sous-jacente. **Les** simples **membres du groupe** n'y sont pas autorisés." />}}

## Supprimer une application d'une base

1. Ouvrez la **base** dans laquelle vous souhaitez supprimer une application.
2. Cliquez sur **Apps** dans l'en-tête de la base.

![Cliquez sur Apps dans l'en-tête de base](images/click-apps-in-the-base-header.jpg)

4. Passez votre souris sur l’application souhaitée et cliquez sur les **trois points** à droite.
5. Sélectionnez **Supprimer** .
6. Confirmez en cliquant sur **Supprimer**.

![Supprimer une application](images/Delete-an-app.gif)

{{< warning  headline="La suppression est définitive" >}}

Vous **ne pouvez pas récupérer** une application supprimée. Si vous n’êtes pas sûr de pouvoir utiliser une application à une date ultérieure, il est préférable de [désactiver temporairement]({{< relref "help/app-builder/app-verwaltung/apps-zeitweise-deaktivieren" >}}) l’application.

{{< /warning >}}

## Conséquences de la suppression

Commençons par le plus important : **la suppression d'une application ne fait jamais perdre de données dans la base sous-jacente**. Techniquement, vous ne supprimez donc qu'une interface utilisateur et _non_ la base de données en arrière-plan.

Veuillez noter, cependant, que lorsque vous supprimez une application, toutes les pages et tous les dossiers qui se trouvent dans **l’application** sont également **définitivement supprimés** et ne peuvent pas _être restaurés_.[]({{< relref "help/app-builder/einstellungen/seiten-und-ordner-in-einer-universellen-app-anlegen-und-verwalten" >}})

Lors de la suppression d'une **application de galerie**, _seules_ les **galeries** présentées dans l'application sont supprimées, les **images** restent en revanche conservées dans [les colonnes d'images]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) de vos tableaux.

De même, la suppression d'une **application de consultation de données** ne supprime **aucune donnée**, mais uniquement le **masque de recherche**.
