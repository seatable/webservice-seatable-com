---
title: 'Étape 1 : la base de départ'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/fr/aide/etape-1-la-base-de-depart'
aliases:
    - '/fr/aide/schritt-1-die-base'
seo:
    title: 'Étape 1 du cours SeaTable 4 : la base de l''entrepôt'
    description: 'Importez la base Warehouse et faites connaissance avec ses trois tables — les produits, les documents entrants et leurs lignes — avant d''automatiser la réception des livraisons.'
---

Avant d'automatiser quoi que ce soit, il faut une base sur laquelle travailler. Dans ce cours, vous tenez un entrepôt : vous recevez des marchandises, vous vérifiez ce qui arrive, et vous gardez votre stock à jour. Nous partons donc d'une base déjà préparée — comme dans les cours précédents — pour consacrer notre temps à l'automatisation plutôt qu'à la saisie.

Téléchargez le fichier suivant et importez-le comme nouvelle base :

<!-- TODO: exporter la base Warehouse en .dtable et la déposer à ce chemin -->
[SeaTable Course Level 4 - Warehouse.dtable](/SeaTable-Course-Level-4-Warehouse.dtable)

Ajoutez ensuite à cette base le plugin des cours en ligne. Vous continuez à suivre le cours ici, sur le site ; le plugin, lui, est le compagnon vers lequel vous basculerez de temps en temps pour mettre en pratique et faire vérifier votre travail. <!-- TODO: procédure et lien d'installation du plugin -->

Indiquez enfin l'adresse de votre base ci-dessous. Le cours s'en sert pour vous proposer des liens qui ouvrent directement le bon exercice dans le plugin ; cette adresse reste dans votre navigateur et ne quitte jamais votre poste.

{{< st-base-url label="Adresse de votre base" >}}

Même si vous n'avez pas construit la base vous-même, prenez le temps de bien la connaître : le cours y revient à chaque étape, et certains types de colonnes vous seront peut-être nouveaux.

## Les composants de la base

La base `Warehouse` s'organise autour de trois tables : votre catalogue de produits, les documents qui font entrer et sortir la marchandise, et les lignes qui détaillent chacun de ces documents.

### Le catalogue : `Products`

La table `Products` est votre catalogue. Chaque ligne est un produit, identifié par sa `Reference` — le code-barres imprimé sur l'emballage. La colonne `Stock` indique la quantité que vous avez en réserve : c'est le nombre que tout le reste du cours va s'attacher à tenir à jour, sans que vous ayez à y toucher à la main.

{{< warning headline="Le stock est un nombre, pas une formule" text="La colonne Stock est un simple nombre, pas un calcul automatique. C'est un choix voulu pour ce cours : vous allez apprendre à l'ajuster vous-même, d'abord avec une automatisation, puis avec un script. Dans une vraie base, un stock peut aussi se calculer à partir des mouvements — mais l'écrire nous-mêmes est justement ce qui rend les prochaines étapes parlantes." />}}

### Les documents : `Documents`

Chaque enregistrement de la table `Documents` est une pièce qui fait bouger le stock — le plus souvent un bon de livraison reçu d'un fournisseur, parfois une commande passée par un client. La colonne `{{< seatable-icon icon="dtable-icon-single-election" >}} Movement type` indique de quel type il s'agit, et `File` contient le document lui-même : le PDF du bon, par exemple.

Les autres colonnes de cette table — celles qui accueilleront le texte extrait du document, le lien d'archivage ou l'assignation d'un problème à un collègue — se rempliront au fil du cours, à mesure que vous les mettrez en service. Inutile de les détailler maintenant ; chacune arrive à son étape.

### Les lignes : `Line items`

Un document, à lui seul, ne dit pas grand-chose : ce sont ses lignes qui comptent. La table `Line items` détaille chaque document, une ligne par produit. Chaque ligne relie un produit du catalogue à deux quantités : `Qty`, ce que le document **annonce**, et `Received qty`, ce que vous **constatez** réellement à la réception. C'est la comparaison de ces deux nombres qui est au cœur du cours.

![Un bon de livraison de la table “Documents” et, à côté, ses lignes détaillées dans la table “Line items”](images/lvl4-document-and-lines.png)

## Comment tout s'articule

Les tables `Documents` et `Line items` sont reliées : côté document, la colonne `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Line items` regroupe toutes ses lignes ; côté ligne, `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Document` pointe vers le document auquel elle appartient. C'est la structure que suit n'importe quelle pièce commerciale — un en-tête et ses lignes — de la facture au bon de livraison. Chaque ligne relie par ailleurs son `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Product` au catalogue, ce qui lui permet d'afficher la `{{< seatable-icon icon="dtable-icon-link-formulas" >}} Description` du produit sans la ressaisir.

Dans un entrepôt bien tenu, une même marchandise passe par trois états, et votre base les distingue :

- **Commandé**: la référence — ce que vous attendez du fournisseur. Ces lignes viendront plus tard de votre logiciel de gestion ; nous y reviendrons à l'étape sur l'API.
- **Livré**: ce que le bon de livraison annonce à l'arrivée, dans la colonne `Qty`.
- **Reçu**: ce que vous comptez réellement sur le quai, dans la colonne `Received qty`.

Le fil rouge du cours compare les deux derniers. Le fournisseur annonce trois cartons, vous n'en recevez que deux : l'écart doit sauter aux yeux, être tracé, et déclencher ce qu'il faut — mise à jour du stock, notification, ou intervention d'un collègue. C'est exactement ce que vous allez construire, une brique après l'autre.

## Essayez par vous-même

Ouvrez la table `Documents` et repérez le bon de livraison déjà présent. Suivez son lien `Line items` : vous voyez les lignes que le fournisseur annonce, chacune avec sa `Qty`. Leur colonne `Received qty` est encore vide — c'est vous qui la remplirez dès la prochaine étape, et SeaTable se chargera du reste.

## Article d'aide avec plus d'informations

- [Créer une base à partir d'un fichier .dtable]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei/" >}})
- [La colonne de liaison]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte/" >}})
- [La colonne formule pour les liaisons]({{< relref "help/base-editor/spaltentypen/die-spalte-formel-fuer-verknuepfungen/" >}})
