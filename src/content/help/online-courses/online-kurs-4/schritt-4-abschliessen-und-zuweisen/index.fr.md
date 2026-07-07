---
title: 'Étape 4 : clôturer et alerter'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/fr/aide/etape-4-cloturer-et-alerter'
aliases:
    - '/fr/aide/schritt-4-abschliessen-und-zuweisen'
seo:
    title: 'Étape 4 du cours SeaTable 4 : clôturer une réception et assigner un litige'
    description: 'Clôturez une livraison en la datant, puis construisez une automatisation qui assigne un collègue en cas d''écart — en découvrant au passage l''importance des conditions de déclenchement.'
---

Les lignes sont validées, le stock est à jour. Il reste à clôturer la réception du document et, si tout n'était pas conforme, à faire remonter le problème à la bonne personne. Vous allez construire une deuxième automatisation — et rencontrer, au passage, le réflexe le plus important quand on automatise.

## Clôturer la réception

Jusqu'ici vous avez travaillé ligne par ligne. Prenez maintenant de la hauteur : ouvrez la fiche du document. La même application qu'à l'étape précédente vous en propose une vue d'ensemble — une page par livraison, où vous voyez d'un coup d'œil combien de lignes restent à vérifier et si un écart a été signalé.

Quand vous avez fini de traiter la livraison, datez-la : renseignez `Operator validation`. Ce simple geste — une date posée à la main — signifie « ce document est traité », et c'est lui qui déclenchera la suite.

![La fiche d'un document dans l'application, avec le récapitulatif de la livraison et le champ de validation](images/lvl4-close-document.png)

## Alerter quand il y a un problème

Une livraison conforme n'appelle aucune action particulière. Mais s'il manque des articles, ou si un lot est arrivé abîmé, quelqu'un doit s'en occuper — réclamer au fournisseur, ajuster une commande. Automatisons cette alerte.

Le déclencheur, cette fois, n'est pas l'arrivée d'une nouvelle ligne mais la **modification** d'un document : le moment précis où vous renseignez `Operator validation`. L'action : assigner un `Reviewer`, la personne chargée de régler le litige.

Sur votre base, vous êtes seul : assignez-vous le document à vous-même. Dans une vraie équipe — comme vous l'avez vu au cours de [niveau 3, consacré à la collaboration](/help/level-three-introduction) — ce serait un collègue, le service achats par exemple, qui recevrait la notification et prendrait le relais.

## La condition qui change tout

Construisez l'automatisation telle quelle — déclencheur : `Operator validation` renseignée ; action : assigner le reviewer — puis essayez-la sur une livraison **parfaitement conforme**. Surprise : un reviewer est quand même assigné, alors qu'il n'y a rien à régler.

C'est le piège le plus courant des automatisations : un déclencheur trop large. Votre règle part pour *tout* document validé, qu'il pose problème ou non. Il lui manque une **condition**.

Ajoutez-la : l'action ne doit s'exécuter que si `Review needed` est vrai — autrement dit si au moins une ligne s'écarte du conforme. Rejouez : une livraison sans souci ne dérange plus personne, une livraison avec un écart assigne bien son reviewer.

{{< warning headline="Toujours se demander -- seulement si ?" text="Un déclencheur décide quand une automatisation se lance ; une condition décide dans quels cas seulement. Oublier la condition est l'erreur la plus fréquente : la règle part trop souvent, ou au mauvais moment. Le bon réflexe, pour chaque automatisation, est de se demander non seulement quand elle doit s'exécuter, mais aussi quand elle ne doit surtout pas le faire." />}}

C'est le bon moment pour faire vérifier votre travail par le plugin : il regarde qu'un reviewer a bien été assigné sur le document qui en avait besoin.

## Essayez par vous-même

Ouvrez la fiche d'une livraison que vous avez clôturée sans écart, et confirmez qu'aucun reviewer n'y est assigné : votre condition fait bien son office. Puis imaginez la règle suivante que vous ajouteriez dans un vrai entrepôt — prévenir aussi l'équipe quand une livraison arrive en retard, par exemple. Quel serait son déclencheur, et surtout : quelle condition lui éviterait de partir à tort ?

## Article d'aide avec plus d'informations

- [La colonne collaborateur]({{< relref "help/base-editor/spaltentypen/die-mitarbeiter-spalte/" >}})
- [Créer et configurer une automatisation]({{< relref "help/base-editor/automationen/" >}})
- [Le cours de niveau 3 : collaborer sur des données partagées](/help/level-three-introduction)
