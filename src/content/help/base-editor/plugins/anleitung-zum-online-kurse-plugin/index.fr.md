---
title: 'Instructions pour le plugin de cours en ligne'
date: 2026-10-07
lastmod: '2026-10-07'
categories:
    - 'plugins'
author: 'bha'
url: '/fr/aide/guide-plugin-cours-en-ligne'
aliases:
    - '/fr/aide/anleitung-zum-online-kurse-plugin'
seo:
    title: 'Guide du plugin de cours en ligne SeaTable'
    description: 'Le plugin de cours en ligne de SeaTable rend chaque cours interactif et vérifie votre travail directement dans votre propre base.'
---

Le **plugin de cours en ligne** n'est pas un plugin comme les autres : il ne vous offre pas une nouvelle façon de voir vos données, il vous **accompagne dans votre apprentissage**. Il vous guide dans les exercices pratiques des [cours en ligne]({{< relref "help/online-courses" >}}) de SeaTable et **vérifie votre travail directement dans votre propre base**. Au fil d'un cours, vous créez par exemple une automatisation, un court script ou une vue, puis vous ouvrez le plugin : il contrôle que le résultat attendu est bien là, dans vos données.

Pour savoir comment activer un plugin dans une base, [cliquez ici]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}}).

![Le plugin de cours en ligne ouvert sous une base : à gauche la liste des étapes, à droite l'exercice en cours et son bouton Verify](images/online-courses-plugin.png)

## Le plugin et les cours

Vous suivez chaque cours principalement sur notre **site web**, où le scénario se déroule étape par étape. À certains moments, le cours vous demande d'**ouvrir le plugin et de choisir une étape** : c'est là que vous passez à la pratique dans votre base, et que le plugin vérifie ce que vous avez fait.

Le site et le plugin ont chacun leur rôle :

- Le **site** raconte l'histoire : il explique chaque notion, ce qu'il faut construire et pourquoi.
- Le **plugin** vous accompagne dans votre base et contrôle votre travail : il lit vos données et vous confirme aussitôt que votre automatisation se déclenche bien, que votre script a produit les bonnes valeurs ou que votre vue est configurée comme prévu.

Le plugin ne se contente pas pour autant de noter votre travail à la fin. Quand une opération se fait en plusieurs temps – le déclencheur d'une automatisation, puis ses conditions, puis chacune de ses actions –, il peut **vous guider pas à pas** : il vous indique ce qu'il faut régler et valide chaque phase avant de passer à la suivante. Vous pouvez donc tout construire par vous-même et ne demander qu'une vérification finale, ou vous laisser guider de bout en bout.

Il peut aussi **modifier lui-même votre base** quand un exercice l'exige : ajouter les lignes dont l'exercice a besoin, ou défaire ce qu'une étape précédente a produit pour que vous puissiez la recommencer de zéro. Il vous annonce chaque fois ce qu'il va faire.

Dans le cours sur la collaboration, il va plus loin : il **joue le rôle d'une collègue** et agit en son nom dans votre base (un commentaire, une modification). Vous pouvez ainsi vous exercer au travail d'équipe sans faire appel à une autre personne.

## Première utilisation

À la première ouverture du plugin, commencez par le **cours d'introduction** intégré : choisissez-le dans la liste à gauche. Cette brève introduction vous montre **comment se déroule un cours**, à quoi servent les **boutons** et comment **réduire le plugin** pour pouvoir le déplacer dans l'interface. Toute la suite suppose que vous sachiez passer aisément du site au plugin : c'est donc par là qu'il faut commencer.

Une fois à l'aise, choisissez dans la même liste le cours que vous suivez, et avancez en parallèle sur le site.

## Cours pris en charge

Le plugin est déployé cours par cours. Le [cours en ligne 3 – Collaboration]({{< relref "help/online-courses/online-kurs-3/level-drei-einfuehrung" >}}) et le [cours en ligne 4 – Automatisation et intégration (en anglais)]({{< relref path="help/online-courses/online-kurs-4/level-vier-einfuehrung" lang="en" >}}) sont entièrement pris en charge aujourd'hui, et d'autres cours suivront. Un cours que le plugin ne vérifie pas encore s'ouvre tout de même, avec un court message qui vous le signale et vous invite à le suivre sur le site en attendant.

## Autres articles utiles

- [Aperçu de tous les plugins]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}})
- [Cours en ligne SeaTable]({{< relref "help/online-courses" >}})
- [Activer un plugin dans une base]({{< relref "help/base-editor/plugins/aktivieren-eines-plugins-in-einer-base" >}})
