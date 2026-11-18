---
title: 'Étape 6 : Tableau blanc'
date: 2026-10-07
lastmod: '2026-10-07'
categories:
    - 'online-kurs-3'
author: 'bha'
url: '/fr/aide/cours-3-etape-6-tableau-blanc'
seo:
    title: 'Étape 6 du cours SeaTable 3 : le tableau blanc'
    description: "Collaborez en temps réel sur le tableau blanc de SeaTable, dans la base du marketing (curseurs et messages en direct), puis convenez de quelques règles graphiques pour savoir à qui appartient quoi."
---

Toute collaboration ne se passe pas dans un tableau de données. Il arrive qu'une équipe ait besoin d'esquisser un processus, de poser une idée à plat ou de dessiner une maquette ensemble : le genre de réflexion qui a sa place sur une toile partagée plutôt que dans des lignes et des colonnes. SeaTable a précisément l'outil pour cela : le plugin de tableau blanc.

Contrairement à tout ce que nous avons vu jusqu'ici, le tableau blanc ne contient aucune de vos données, et, c'est le point qui structure toute cette étape, il ne garde aucune trace de qui a fait quoi : chaque dessin est un instantané sans historique. Ce qu'il fait remarquablement bien, c'est l'autre moitié de la collaboration : travailler ensemble, en direct, dans le même espace, au même moment.

## La bonne base pour le tableau

Un tableau blanc trouve sa place dans une base que toutes et tous peuvent modifier. Vous venez de passer quatre étapes à apprendre à ne pas donner ce genre d'accès à une base pleine de données sensibles, et la même habitude est valable ici : gardez la coordination et les esquisses hors de vos tableaux de production, comme votre fichier de référence reste séparé de la copie de travail du marketing. Le tableau blanc va dans une base que vos collègues peuvent modifier, jamais dans `Sales CRM`.

Cette base, c'est `Campaign Hub`. C'est celle du marketing, tous les membres du groupe `Marketing` peuvent la modifier, et vos chiffres confidentiels n'y sont jamais arrivés : le jeu de données commun les a laissés dans `Sales CRM`. Elle contient aussi le tableau blanc qui lui revient : `Customers data flow`, le schéma du marketing qui montre comment les données clients lui parviennent, et donc une représentation de cette base même. Mais il montre encore l'ancienne façon de faire, lorsque le marketing travaillait encore à partir d'une copie manuelle. Maintenant que les données arrivent par un jeu de données commun, le schéma est à redessiner, et comme c'est vous qui avez mis en place ce nouveau circuit, c'est à vous de le mettre à jour.

Le plugin de tableau blanc est déjà installé dans `Campaign Hub` : il n'y a rien à installer. Ouvrez-le depuis la zone des plugins de la base, puis affichez le dessin `Customers data flow`. (Sur un serveur auto-hébergé, le tableau blanc est un composant séparé : s'il ne s'ouvre pas, votre administrateur système devra peut-être d'abord [l'installer](https://admin.seatable.com/installation/components/whiteboard/).)

Notez au passage qu'un partage en lecture seule n'aurait pas fonctionné ici : dessiner sur un tableau blanc demande des droits en écriture.

## Dessiner ensemble

Ouvrez le tableau blanc : vous voilà sur une toile partagée, sur laquelle sont présents tous ceux qui l'ont ouverte au même moment. Le curseur de chacun se déplace sur la toile dans les fenêtres des autres, un pointeur laser laisse une traînée qui s'efface le long d'une forme, et un court message peut s'afficher un instant sous un curseur. Le curseur qui se déplace, la traînée du laser qui s'efface, le message éphémère : c'est cette collaboration dans l'instant qu'un tableau de données ne peut pas offrir. La vidéo ci-dessous le montre, avec deux personnes sur le même tableau blanc.

{{< zoom image="images/lvl3-whiteboard-collab.gif" alt="Deux curseurs sur le tableau blanc partagé qui se font signe, avec une traînée de laser et un message sous l'un des curseurs" >}}

## Le tableau blanc ne retient rien

{{< warning headline="Le tableau blanc n'a pas d'historique" text="Contrairement à votre base, le tableau blanc ne garde aucune trace de qui a dessiné quoi, et ne permet pas d'annuler par auteur. Le journal de l'étape 4 n'a pas d'équivalent ici. S'il est important de savoir qui a ajouté quelque chose, c'est au tableau blanc lui-même de le montrer." />}}

Puisque le tableau blanc ne garde aucune trace, mieux vaut convenir de quelques règles graphiques avant de le remplir, comme une équipe convient de règles de nommage pour ses données. Le tableau de départ en applique deux :

- une couleur par service, pour voir d'un coup d'œil à quelle équipe appartient chaque élément ;
- des rectangles sans remplissage autour de ce qui va ensemble, ici un par base.

Ce n'est qu'un point de départ : votre équipe peut adopter les siennes. Fixez des règles simples, en quantité raisonnable, et essayez de vous y tenir. N'hésitez pas à créer une toile spécifique dédiée à ces règles afin que chacun puisse s'y référer plus tard.

## Mettre le tableau blanc à jour

Actuellement, la toile montre encore l'ancienne façon de faire : la liste des clients parvient au marketing par un export manuel vers `Customers list (manual)`. Vous avez passé tout ce cours à remplacer ce mécanisme ; mettez donc le tableau à jour. Renommez certains éléments et changez les couleurs si besoin pour qu'il reflète comment les données clients parviennent aujourd'hui au marketing. Dans ce cas simplifié, l'objectif est de prendre en main les outils du tableau blanc : faites donc vous-même toutes les modifications, en respectant les règles ci-dessus.

Vous avez maintenant toute une panoplie d'outils de collaboration. Il est temps de revenir sur tout ce que vous avez appris, et de le mettre à l'épreuve.

## Pour aller plus loin

Découvrez par vous-même le travail en direct, avec Malika. Ouvrez une fenêtre de navigation privée et connectez-vous dans celle-ci avec le compte de Malika. Une fenêtre privée crée une session à part, donc vous restez connecté à votre propre compte dans votre fenêtre habituelle. Ouvrez le même tableau blanc : elle y a accès, puisqu'elle est membre du groupe `Marketing`. Placez les deux fenêtres côte à côte, puis, dans la vôtre, déplacez votre curseur sur la toile, passez le pointeur laser le long d'une forme ou laissez un court message sous votre curseur, et observez ces actions avoir lieu dans la fenêtre de Malika au moment même.

## Article d'aide avec plus d'informations

- [Instructions pour le plugin de tableau blanc (tldraw)]({{< relref "help/base-editor/plugins/anleitung-zum-whiteboard-plugin-tldraw/" >}})
