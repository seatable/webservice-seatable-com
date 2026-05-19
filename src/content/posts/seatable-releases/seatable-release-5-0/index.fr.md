---
title: "SeaTable 5.0 : constructeur d'applications, nouveaux plug-ins et accessibilité accrue"
description: 'La version 5.0 officialise la création d’applis personnalisées via le builder, ajoute visuels organigramme, whiteboard et relations, optimise l’accessibilité et l’import Excel par colonne. Créez, collaborez, visualisez et maîtrisez vos flux de données sans coder. Innovation, gestion et transformation pour tous !'
date: 2024-07-15
lastmod: '2024-07-15'
author: 'kgr'
url: '/fr/seatable-release-5-0'
color: '#efba4b'
categories:
    - 'product-features'
seo:
    title: 'SeaTable 5.0 : app builder, plugins et accessibilité'
    description: 'Créateur d’apps no code, plugins d’organisation, de relations, accessibilité renforcée et import Excel précis : SeaTable 5.0 est là !'
---

C'est parti : notre App-Builder est officiellement lancé ! Grâce à cette version de notre **base de données No-Code avec No-Code-App-Builder intégré**, tout le monde, programmeurs ou Citizen Developer, pourra désormais créer ses propres applications en toute simplicité ! Avec SeaTable 5.0, nous sommes prêts à occuper une position de leader sur le marché international de la transformation et de l'innovation numériques.

Mais ce n'est pas le seul coup de théâtre - dans SeaTable 5.0, vous disposez de **trois nouveaux plug-ins** pour des visualisations complexes : Organigramme, Relations entre les tableaux et Tableau blanc. L'**accessibilité améliorée** devrait faciliter l'utilisation de SeaTable pour les personnes souffrant d'un handicap (visuel). L'**importation Excel en colonnes** constitue un autre point fort.

Ce matin, nous avons mis à jour SeaTable Cloud à la version 5.0. Tous les auto-hébergeurs peuvent faire de même : L'image de SeaTable 5.0 est disponible en téléchargement dans le célèbre [dépôtDocker](https://hub.docker.com/r/seatable/seatable-enterprise) . Comme toujours, vous trouverez dans le [changelog]({{< relref "pages/changelog" >}}/) la liste complète des modifications.

## Sans code pour une application professionnelle personnalisée

SeaTable 5.0 marque le lancement officiel de notre générateur d'applications sans code. Nos développeurs ont apporté de nombreuses nouvelles fonctions et améliorations à l'App Builder au cours des dernières versions, ce qui vous permet de réaliser vos applications les plus exigeantes. Créez des applications professionnelles personnalisées sans écrire une seule ligne de code et utilisez SeaTable comme front-end et back-end à la fois !

### Nouveau type de page : enregistrement unique

Le développement de l'App-Builder se poursuit sans relâche : avec le [type de page]({{< relref "help/app-builder/seitentypen-in-universellen-apps/ueberblick" >}}) **Enregistrement individuel**, vous avez la possibilité de concevoir une page avec des éléments statiques, des champs de tableau, des couleurs, des cadres, etc. afin de présenter visuellement les données enregistrées sur une ligne. Ce type de page est donc similaire au [plug-in de conception de page]({{< relref "help/base-editor/plugins/anleitung-zum-seitendesign-plugin" >}}) que vous connaissez déjà dans la Base.

Les utilisateurs de l'application peuvent voir, rechercher, parcourir et modifier les différents enregistrements sur cette page - avec l'[autorisation]({{< relref "help/app-builder/einstellungen/seitenberechtigungen-in-einer-universellen-app" >}}) correspondante. Ce type de page convient par exemple pour afficher les données d'une base de données d'employés sous forme de fiches personnelles.

![Page d'enregistrement unique](Single-Record-Page-min.gif)

### Nouvelles fonctions des types de pages existants

Sur les [pages de tableau]({{< relref "help/app-builder/seitentypen-in-universellen-apps/tabellenseiten-in-universellen-apps" >}}), vous pouvez dès à présent **exporter** toutes les données affichées sous forme de **fichier Excel**. En outre, l'en-tête des [colonnes]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) d ['images]({{< relref "help/base-editor/spaltentypen/die-bild-spalte" >}}) et [de fichiers]({{< relref "help/base-editor/spaltentypen/die-datei-spalte" >}}) vous permet de **télécharger toutes les pièces jointes sous forme de fichier zip**. Les nouvelles fonctions d'exportation sont utiles si vous souhaitez mettre certains fichiers à la disposition d'autres utilisateurs via l'application.

Sur les [pages de la galerie]({{< relref "help/app-builder/seitentypen-in-universellen-apps/galerieseiten-in-universellen-apps" >}}), nous avons complété les **paramètres des colonnes de liens**. Vous pouvez par exemple définir si les utilisateurs peuvent lier des entrées existantes ou ajouter des entrées dans une autre table via la page de la galerie. Sur les [pages de requête]({{< relref "help/app-builder/seitentypen-in-universellen-apps/abfrageseiten-in-universellen-apps" >}}), les résultats de la requête sont désormais immédiatement mis à jour lorsque vous déclenchez des actions de bouton qui entraînent des modifications des données.

## Trois plug-ins pour des visualisations complexes

Un autre point fort de SeaTable 5.0 sont les nouveaux [plugins]({{< relref "help/base-editor/plugins/alle-plugins-in-der-uebersicht" >}}) qui permettent de visualiser les dépendances, les structures et les processus dans une base.

### Organigramme

Le plug-in Organigramme permet de représenter les hiérarchies entre les enregistrements d'un tableau, par exemple les postes dans une entreprise ou les [tâches supérieures et inférieures dans un projet]({{< relref "templates/projects/work-breakdown-structure" >}}). Pour visualiser les dépendances entre les enregistrements, vous avez besoin d'une [colonne de lien]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}) qui se réfère à un seul et même tableau. L'entrée avec laquelle vous liez une autre ligne du même tableau est représentée comme enregistrement parent.

![Plugin d'organigramme](Organigramm-Plugin.png)

### Relations entre les tables

Il est facile de perdre la vue d'ensemble des relations entre les différents tableaux d'une base, surtout lorsque celle-ci contient des milliers de lignes. Le nouveau plug-in Relations entre les tableaux permet de voir quels tableaux sont liés entre eux et par quelles colonnes. Il affiche non seulement les liens directs via les [colonnes de liens]({{< relref "help/base-editor/spaltentypen/die-verknuepfungsspalte" >}}), mais aussi les liens indirects via les colonnes de formules de liens.

![Plugin de relations entre les tables](Table-Relationships-Plugin.png)

### Tableau blanc

Le tableau blanc est le premier plugin qui fonctionne indépendamment des données dans une base. Il vous donne la liberté de visualiser graphiquement des processus et des structures que vous ne pouvez pas représenter avec les plugins précédents. De même, vous pouvez esquisser librement des mises en page et des mockups. Pour la conception, vous avez le choix entre différents **éléments** tels que des carrés, des ellipses et des flèches ainsi que **des outils** tels que le stylo et la gomme.

![Plugin de tableau blanc](Whiteboard-Plugin.png)

{{< warning headline="SeaTable ♥ Excalidraw" text="Le plugin pour tableau blanc est basé sur le logiciel populaire [Excalidraw](https://plus.excalidraw.com/), que de nombreux utilisateurs connaissent déjà. Une restriction importante doit être mentionnée : Au lancement de SeaTable 5.0, le tableau blanc ne supportera pas la collaboration en direct. Nous y remédierons prochainement." />}}

## Amélioration de l'accessibilité

SeaTable souhaite offrir à tous les utilisateurs un accès optimal à sa solution numérique sans code. C'est pourquoi nous avons beaucoup investi dans l'amélioration de l'accessibilité pour SeaTable 5.0. Il s'agit notamment d'optimiser les balises ARIA pour une meilleure **prise en charge des périphériques de sortie non visuels**, d'adapter les couleurs pour **renforcer les contrastes** et de revoir les **commandes du clavier**.

Avec la version 5.0, nous atteignons l'objectif d'obtenir un Lighthouse Accessibility Score de 90 ou plus pour les pages les plus importantes de SeaTable. À partir de ce score, les pages Web peuvent être considérées comme essentiellement accessibles. Bien entendu, nous poursuivrons nos efforts en matière d'accessibilité à l'avenir avec nos partenaires.

## Importation Excel au plus près des colonnes

Déjà dans la version 4.4, l'importation de fichiers XLSX est devenue plus rapide, plus flexible et plus stable. Avec SeaTable 5.0, l'assistant d'importation est encore plus performant : dans la fenêtre d'aperçu nettement améliorée, vous pouvez désormais sélectionner en détail les tables - et même **les colonnes d'un classeur XLSX** - que SeaTable doit importer. Il suffit de désélectionner les tables et les colonnes indésirables pour contrôler avec précision l'importation des données.

![Importation Excel](Excel-Import.gif)

## Optimisation de l'API de SeaTable Cloud

Dans le cadre de SeaTable 5.0, nous avons également apporté quelques modifications à l'API SeaTable. Cela ne concerne que les utilisateurs qui utilisent l'API pour mettre en œuvre leurs propres applications et flux de travail. Ces modifications n'ont aucune incidence sur le travail effectué dans le navigateur.

Voici un aperçu des points les plus importants :

- Les points finaux de l'API [Get Row](https://api.seatable.com/reference/getrowdeprecated) et [List Rows](https://api.seatable.com/reference/listrowsdeprecated) sont transférés vers le nouveau _API-Gateway_ redirigé.
- Le format des valeurs de retour des colonnes de liens et de formules de liens est harmonisé.
- Le site _API-Gateway_ renvoie à l'avenir la limite d'utilisation actuelle de l'API.

Si vous souhaitez en savoir plus, vous trouverez tous les détails sur les changements dans ce [post de forum](https://forum.seatable.com/t/important-changes-to-api-and-seatable-cloud-with-version-5-0/4887).

## Et bien plus encore

Vous rencontrez l'**éditeur de texte long** à de nombreux endroits. Lorsque vous remplissez des champs de texte formatés dans les **détails des lignes** ou dans les [formulaires web]({{< relref "help/base-editor/webformulare" >}}), vous remarquerez que l'ergonomie a été améliorée : L'éditeur de texte long ne s'ouvre plus dans une autre fenêtre pop-up, mais en ligne, ce qui vous permet de commencer à écrire directement.

![Éditeur de textes longs dans les formulaires web](Long-text-editor-in-web-forms.png)

Vous connaissez également les **statistiques** de plusieurs endroits dans SeaTable : du [module Statistiques]({{< relref "help/base-editor/statistiken/anleitung-zum-statistik-modul" >}}) dans la Base ainsi que des [pages individuelles dans les Apps universelles]({{< relref "help/app-builder/seitentypen-in-universellen-apps/individuelle-seiten-in-universellen-apps" >}}). Nous avons amélioré et unifié les statistiques avec une nouvelle bibliothèque de graphiques.

Auparavant, vous ne pouviez pas restaurer les lignes que vous aviez déplacées vers l'[espace de stockage Big Data]({{< relref "help/base-editor/big-data/zeilen-ins-big-data-backend-verschieben" >}}) à l'aide de snapshots. Afin d'éviter toute perte de données indésirable, il existe désormais une option permettant de restaurer également l'espace Big Data de la version de l'époque lors de la [restauration de snapshots]({{< relref "help/base-editor/historie-und-versionen/wiederherstellung-eines-snapshots" >}}).
