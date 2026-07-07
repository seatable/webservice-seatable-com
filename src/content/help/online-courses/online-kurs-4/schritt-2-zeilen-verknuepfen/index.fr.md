---
title: 'Étape 2 : importer et relier les lignes'
date: 2026-07-02
lastmod: '2026-07-02'
categories:
    - 'online-kurs-4'
author: 'bha'
url: '/fr/aide/etape-2-importer-et-relier-les-lignes'
aliases:
    - '/fr/aide/schritt-2-zeilen-verknuepfen'
seo:
    title: 'Étape 2 du cours SeaTable 4 : relier des lignes automatiquement'
    description: 'Importez les lignes d''une livraison depuis un tableur et construisez votre première automatisation : relier chaque ligne à son produit et à son document par comparaison de références.'
---

Une nouvelle livraison arrive à l'entrepôt. Son en-tête figure déjà dans la table `Documents`, mais le détail — quels produits, en quelles quantités — reste à faire entrer. Dans cette étape, vous importez ces lignes, puis vous construisez votre première automatisation : celle qui les relie, toute seule, au bon produit et au bon document.

## Préparer l'automatisation qui relie

Commençons par l'automatisation, avant même d'avoir les données : ainsi, dès que les lignes arriveront, elles se relieront d'elles-mêmes.

Une automatisation SeaTable suit toujours le même schéma : un **déclencheur** — l'événement qui la met en route — suivi d'une ou plusieurs **actions**. Ici, le déclencheur est l'arrivée d'une nouvelle ligne dans `Line items`, et l'action va la rattacher à sa fiche produit.

L'action à choisir s'appelle *relier par comparaison*. Plutôt que de désigner un enregistrement à la main, elle recherche dans une autre table celui dont une colonne correspond à une valeur de la ligne. Reliez ainsi la colonne `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Product` en comparant le `Product ref` de la ligne à la `Reference` des produits ; puis, de la même façon, reliez la colonne `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Document` en comparant son `Document reference` à l'`Identifier` des documents.

![La configuration de l'action « relier par comparaison », rapprochant le Product ref de la ligne de la Reference des produits](images/lvl4-link-by-comparison.png)

{{< warning headline="Une action à garder sous le coude" text="Relier par comparaison vous épargne de choisir l'enregistrement lié un par un : l'automatisation le retrouve grâce à une valeur commune. C'est exactement ce qu'il faut quand les données arrivent de l'extérieur — un import, un formulaire, ou l'intelligence artificielle plus loin dans ce cours — sans lien déjà établi, mais avec une référence partagée." />}}

## Importer les lignes de la livraison

Le fournisseur vous a transmis le détail de la livraison sous forme de tableur — un cas très courant. Plutôt que de tout ressaisir, importez ce fichier directement dans la table `Line items` : SeaTable crée une ligne par entrée du fichier et fait correspondre ses colonnes aux vôtres.

<!-- TODO: fournir le fichier CSV/XLSX d'exemple et le déposer à ce chemin -->
[SeaTable Course Level 4 - Delivery lines.csv](/SeaTable-Course-Level-4-Delivery-lines.csv)

À l'instant où chaque ligne se crée, votre automatisation se déclenche : les colonnes `Product` et `Document`, absentes du fichier, se remplissent d'elles-mêmes. Vos lignes sont désormais rattachées au catalogue et à leur livraison, sans un seul lien saisi à la main. C'est le bon moment pour faire contrôler votre travail par le plugin — il vérifie que chaque ligne importée a bien trouvé son produit.

Une remarque pour la suite : ces lignes, ici, c'est vous qui les avez importées depuis un tableur bien rangé. Mais un bon de livraison, à l'origine, c'est un document PDF, pas un fichier prêt à l'emploi. Comment passe-t-on de l'un à l'autre ? Vous le découvrirez un peu plus loin dans le cours.

## Essayez par vous-même

Ouvrez une ligne fraîchement importée et suivez son lien `{{< seatable-icon icon="dtable-icon-link-other-record" >}} Product` jusqu'au catalogue : la même référence, devenue une vraie connexion. C'est précisément ce lien que vous exploiterez à l'étape suivante pour mettre le stock à jour — sans lui, SeaTable ne saurait pas quel produit créditer.

## Article d'aide avec plus d'informations

- [Importer des données dans SeaTable]({{< relref "help/startseite/import-von-daten/" >}})
- [Créer et configurer une automatisation]({{< relref "help/base-editor/automationen/" >}})
- [La colonne de liaison]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte/" >}})
