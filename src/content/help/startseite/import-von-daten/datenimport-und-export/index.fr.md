---
title: 'Importation et exportation de données'
date: 2022-08-25
lastmod: '2024-03-11'
categories:
    - 'import-von-daten'
author: 'cdb'
url: '/fr/aide/import-export-donnees-seatable'
aliases:
    - '/fr/aide/datenimport-und-export'
seo:
    title: 'Importer et exporter des données dans SeaTable : bases, Excel, CSV'
    description: 'Apprenez à importer et exporter des bases et tables dans SeaTable : DTABLE, Excel, CSV—guide complet avec conseils et dépannage inclus.'
star: true
weight: 1
---

Les fonctions d'importation de SeaTable permettent de passer d'autres solutions à SeaTable sans trop d'efforts. Il en va de même pour le passage d'un système SeaTable à un autre, par exemple lors de la migration de SeaTable Cloud vers un système auto-hébergé. Vous pouvez continuer à travailler de manière transparente sur une base que vous avez importée d'une autre instance SeaTable.

Comment exporter des bases et des tableaux de SeaTable et les importer dans SeaTable, tel est le sujet de cet article.

## Exporter la base

La **page d'accueil** vous permet d'exporter l'état actuel de vos bases, y compris tous les tableaux, [vues]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}), [formulaires web]({{< relref "help/base-editor/webformulare/webformulare" >}}) et plugins. Les [commentaires]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), les [automatisations]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}) et l'[historique des modifications]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) ainsi que [les données du backend Big Data]({{< relref "help/base-editor/big-data/potenzial-big-data" >}}) ne sont **pas exportés**.

![Exportation de bases](images/export-bases.png)

Pour exporter des bases, SeaTable utilise le [format de fichier DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}). Pour plus d'informations, consultez l'article [Enregistrer une base en tant que fichier DTABLE]({{< relref "help/startseite/bases/speichern-einer-base-als-dtable-datei" >}}).

## Exporter le tableau

Vous pouvez **exporter des tableaux** individuels de chaque base à laquelle vous avez accès **vers des fichiers Excel**. Les contenus des colonnes de texte et de chiffres sont copiés dans le fichier cible sous forme de valeurs. Les [commentaires]({{< relref "help/base-editor/zeilen/zeilen-kommentieren" >}}), les [automatisations]({{< relref "help/base-editor/automationen/uebersicht-ueber-automationen" >}}) et l'[historique des modifications]({{< relref "help/base-editor/historie-und-versionen/historie-und-logs" >}}) ne sont **pas exportés**.

![Exportation de tableaux](images/export-tables.jpg)

Vous lancez l'exportation d'un tableau à partir de la base. Cliquez sur la flèche déroulante à droite du nom du tableau à exporter. Sélectionnez maintenant **Exporter le tableau vers un fichier XLSX**.

![Confirmer l'exportation du tableau](images/confirm-view-export.png)

Décidez si vous souhaitez **inclure les images dans le fichier d'exportation** en activant ou non le curseur. Confirmez avec **Exporter** pour démarrer le téléchargement. Dès que l'exportation est terminée, vous trouverez le fichier XLSX à l'emplacement choisi sur votre appareil.

## Exporter la vue

Vous ne souhaitez pas exporter toutes les données d'un tableau ? Alors limitez la [vue]({{< relref "help/base-editor/ansichten/was-ist-eine-ansicht" >}}) à l'aide de **filtres** et de **colonnes masquées** ! Si vous souhaitez exporter une vue de tableau, cliquez sur les **trois points** dans les options de vue au-dessus du tableau, puis sur **Exporter la vue vers un fichier XLSX**. 

![Exporter la vue](images/export-view.png)

Décidez si vous souhaitez **inclure les images dans le fichier d'exportation** en activant ou non le curseur. 

![Confirmer l'exportation de la vue](images/confirm-view-export.png)

Dès que vous cliquez sur **Exporter**, le téléchargement commence. Ensuite, vous trouverez le fichier XLSX à l'emplacement choisi sur votre appareil.

## Importer la base

SeaTable prend en charge l'importation de bases depuis son propre [format DTABLE]({{< relref "help/startseite/import-von-daten/dtable-dateiformat" >}}), depuis **des fichiers Excel** ainsi que depuis le **format** générique **CSV**. Vous pouvez également importer des bases d'Airtable dans SeaTable.

Lors de l'importation d'un **fichier DTABLE**, la base est restaurée exactement telle qu'elle était au moment de l'exportation. Lors de l'importation de fichiers CSV ou Excel, les valeurs du fichier CSV/XLSX sont copiées dans les colonnes du tableau d'une nouvelle base, SeaTable essayant d'interpréter les types de colonnes en fonction des données.

![Importation de données dans une base](images/import-data-into-your-base.png)

Ce à quoi vous devez faire attention lors de l'importation d'une base dépend du type de fichier d'importation. La procédure est cependant la même pour tous les types de fichiers : allez sur la **page d'accueil** et cliquez sur **Ajouter une base ou un dossier** dans le domaine ou le groupe où vous souhaitez avoir la nouvelle base. Vous trouverez des informations plus précises dans les articles suivants :

- [Création d'une base à partir d'un fichier DTABLE]({{< relref "help/startseite/import-von-daten/erstellen-einer-base-aus-einer-dtable-datei" >}})
- [Importation de fichiers Excel dans SeaTable]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}})
- [Importation de données dans SeaTable à l'aide de CSV]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}})
- [Migration de bases Airtable vers SeaTable]({{< relref "help/startseite/import-von-daten/migration-von-airtable-bases-zu-seatable" >}})

## Importer un tableau

Dans les bases existantes, vous pouvez **remplir** des **tableaux** individuels **par importation CSV ou Excel**. Pour cela, vous avez les options suivantes : Vous pouvez importer les données dans un **tableau existant**.

![Importer des données dans un tableau existant](images/Daten-in-eine-bestehende-Tabelle-importieren.png)

ou importer les données dans un **nouveau tableau**.

![Remplissage de tableaux existants par importation de données](images/import-data-in-table.jpg)

L'importation se fait sous forme de [fichier CSV]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}}) ou [de fichier Excel]({{< relref "help/startseite/import-von-daten/import-von-excel-dateien-in-seatable" >}}) dans le tableau. Pour plus d'informations, consultez les articles en lien.

Si vous avez déjà créé un tableau dans **SeaTable** et que vous en avez besoin **dans une autre base**, vous pouvez simplement le copier. Pour savoir comment importer des tableaux d'une autre base, [cliquez ici]({{< relref "help/base-editor/tabellen/eine-tabelle-in-einer-base-hinzufuegen" >}}).

{{< warning  headline="Limite de mémoire pour les lignes" >}}

Le backend normal de SeaTable peut contenir au maximum 100.000 lignes par tableau. Si vous souhaitez importer un fichier Excel ou CSV contenant plus de 100.000 lignes, vous devez d'abord [activer le backend Big Data]({{< relref "help/base-editor/big-data/aktivieren-des-big-data-backends-in-einer-base" >}}) pour pouvoir l'importer.

{{< /warning >}}

## Autres articles utiles sur le thème de l'importation de données

- [Trucs et astuces pour l'importation de fichiers CSV ou XLSX]({{< relref "help/startseite/import-von-daten/tipps-und-tricks-beim-import-von-csv-oder-xlsx-dateien" >}})
- [Limites de l'importation CSV/Excel]({{< relref "help/startseite/import-von-daten/limitationen-beim-csv-excel-import" >}})
- [Importation d'enregistrements CSV dans une base existante]({{< relref "help/startseite/import-von-daten/daten-import-mithilfe-von-csv-in-seatable" >}})
