---
title: 'Étape 8 : connecter l''existant avec l''API'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/fr/aide/etape-8-connecter-l-existant-avec-l-api'
aliases:
    - '/fr/aide/schritt-8-api'
seo:
    title: 'Étape 8 du cours SeaTable 4 : faire entrer des données par l''API'
    description: 'Découvrez comment un logiciel existant pousse des données dans SeaTable via son API : l''explorateur api.seatable.com, l''opération append_rows, et le code Python correspondant.'
---

Depuis le début, vos lignes de livraison arrivent, se relient, se valident. Mais une question est restée en suspens : les lignes de **commande** — celles qui disent ce que vous aviez commandé — d'où viennent-elles ? Vous ne les avez jamais saisies. C'est le sujet de cette dernière brique technique, et elle inverse le sens de tout ce qu'on a vu jusqu'ici : au lieu de faire sortir l'information de SeaTable, on va l'y faire entrer, depuis l'extérieur.

## Connecter l'existant, pas le remplacer

Dans une vraie entreprise, les commandes ne naissent pas dans SeaTable : elles vivent déjà dans un logiciel de gestion ou de comptabilité. Quand vous y saisissez une facture fournisseur, ce logiciel connaît déjà les lignes commandées. L'idée n'est donc pas de tout ressaisir dans SeaTable, ni d'y reconstruire ce logiciel : c'est de **connecter celui qui existe déjà**.

Concrètement, à la saisie de la facture, ce système appelle l'**API de SeaTable** pour y déposer les lignes de commande — d'un coup, en une seule requête. C'est ainsi que les lignes de commande de votre base sont apparues sans que vous les touchiez : poussées de l'extérieur, par l'outil qui les détient.

{{< warning headline="On connecte, on ne remplace pas" text="C'est un point de posture important. SeaTable ne cherche pas à remplacer votre logiciel de gestion : il s'y raccorde. L'API est le point de rencontre entre ce que vous construisez ici et les systèmes déjà en place dans l'entreprise — chacun garde son rôle, et les données circulent entre eux." />}}

## L'API en pratique

Vous n'avez pas de logiciel de gestion sous la main, mais vous pouvez jouer son rôle. Rendez-vous sur l'explorateur d'API, [api.seatable.com](https://api.seatable.com) : il liste toutes les opérations possibles sur une base et vous laisse les essayer directement, avec votre propre jeton d'API. Celle qui nous intéresse ajoute plusieurs lignes en un seul appel : `append_rows`.

Indiquez votre base et la table `Line items`, décrivez quelques lignes de commande, puis lancez la requête. Revenez dans votre base : les lignes y sont. Vous venez de faire, à la main, ce que le logiciel de gestion ferait automatiquement à chaque facture — et c'est le moment de le faire confirmer par le plugin.

![L'explorateur api.seatable.com : l'opération append_rows et le code Python généré à côté](images/lvl4-api-explorer.png)

Regardez ce que l'explorateur affiche à côté de la requête : le **code correspondant**, en Python, avec la librairie `requests` que vous avez déjà croisée à l'étape des webhooks. La boucle se referme : l'API, les scripts, les webhooks — partout le même geste, une requête HTTP. Ce que vous venez d'exécuter à la main, un logiciel de gestion le lance en coulisse à chaque facture.

{{< warning headline="Un jeton d'API ouvre votre base" text="L'explorateur vous demande un jeton d'API, celui de votre base. Pratique pour essayer, mais gardez en tête ce qu'il représente : la clé d'accès à vos données. En production, c'est le logiciel appelant qui le détient — il doit le conserver côté serveur, jamais l'exposer dans une page ni l'envoyer à un navigateur." />}}

## Pour aller plus loin

Vos lignes commandées et vos lignes livrées cohabitent désormais dans la même table, rattachées chacune à son document — une commande d'un côté, une livraison de l'autre, pour un même fournisseur. Rien ne vous empêche de les confronter automatiquement : a-t-on livré tout ce qui avait été commandé ? Le principe reprend la comparaison annoncé / reçu de l'étape 3, appliquée cette fois d'un document à l'autre. Nous vous en laissons l'exploration.

## Essayez par vous-même

Avant de lancer votre requête `append_rows`, réfléchissez à ce qui la rend fiable côté logiciel de gestion : que se passe-t-il s'il l'envoie deux fois pour la même facture ? Vous retrouvez, à l'échelle d'un système entier, la question d'idempotence rencontrée avec le bouton de validation à l'étape 3 — un rappel que les mêmes précautions valent, que l'on clique un bouton ou que l'on branche deux logiciels.

## Article d'aide avec plus d'informations

- [Utiliser l'API de SeaTable]({{< relref "help/integrationen/seatable-api/" >}})
- [Créer un jeton d'API]({{< relref "help/integrationen/seatable-api/erzeugen-eines-api-tokens/" >}})
- [L'explorateur d'API interactif](https://api.seatable.com)
